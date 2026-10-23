"""Prepare disposable host trials and private task inputs; never score agent prose."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from helpers import install

ROOT = Path(__file__).resolve().parents[1]
COMMON = ("Use only this fresh task's repository evidence. Do not consult prior chats, "
          "memory, evaluation guides, or other trial directories. Preserve unrelated files. "
          "Do not install dependencies, use network services, commit, or publish. "
          "Report actual changes, checks, evidence, and uncertainty. ")
PROMPTS = {
    "F02": "Inspect the specification and establish minimal root AGENTS.md guidance. Preserve approved intentions, proposals, and unknowns distinctly. Do not implement the application or invent tooling.",
    "F05": "Inspect existing guidance and approved requirements. Update root AGENTS.md only for an essential operating gap, obsolete claim, or broken pointer. Preserve existing workflows and adequate wording. Do not implement the application or tooling.",
    "F07": "Audit current documentation against this repository. Preserve accurate history and clean material. Do not edit files or save a report.",
    "F10": "Audit the sampled test protection using production paths and assertions. Identify supported weaknesses and retained protections. Do not edit files, inject faults, or save a report.",
}
SKILLS = {"F02": "remora-bootstrap", "F05": "remora-bootstrap",
          "F07": "remora-audit-documentation", "F10": "remora-audit-tests"}
FUNCTIONAL = {
    "F01": ("remora-bootstrap", "Initialize this empty repository without inventing application decisions or commands."),
    "F03": ("remora-fix-regression", "Repair the internal-whitespace normalization regression using existing tests. Preserve project tooling and unrelated files. Demonstrate failure before and success after when possible."),
    "F04": ("remora-plan-change", "Read-only: assess the configured project tooling and deployment boundaries, separating configured commands from executed or deployed behavior."),
    "F06": ("remora-plan-change", "Read-only: plan verification of components/ledger normalization's whitespace, order, and duplicate-preservation contract. Inspect applicable nested instructions, identify meaningful existing assertions and missing evidence, and preserve distinct component tooling. No behavior change is requested."),
    "F08": ("remora-audit-documentation", "Reconcile current documentation ownership and explanation coherently against implementation. Preserve unrelated files and adequate content."),
    "F09": ("remora-implement-plan", "Repair normalization to satisfy the approved specification, with meaningful production tests and current documentation where needed. Review the actual diff; preserve requirements."),
    "F09-review": ("remora-review-change", "Read-only: review the named queue_labels.py implementation against approved SPEC.md. No history range is requested. Do not repair or save a report."),
    "F11": ("remora-audit-tests", "Read-only: audit domain/service test protection, explaining distinct boundaries. Do not inject faults or recommend deleting coverage without evidence."),
    "F12": ("remora-audit-harness", "Read-only: inspect this installation and guidance. Report deterministic integrity results separately from semantic interpretation and native compatibility."),
    "F13": ("remora-remediate-project", "Conduct a phased repository remediation. Establish the initial punch list, ground AGENTS.md, sanitize documentation, audit test protection, and plan debt remediation. Stop at each review gate and preserve unrelated project files."),
}


def snapshot(target):
    install.inspect_path(target.absolute())
    result = {}
    def onerror(error):
        raise error
    for parent, children, files in os.walk(target, followlinks=False, onerror=onerror):
        for name in list(children):
            path = Path(parent) / name
            if name in {".git", "__pycache__"}:
                children.remove(name)
                continue
            try:
                install.inspect_path(path.absolute())
            except install.Conflict:
                result[path.relative_to(target).as_posix()] = {"unsafe_path": True}
                children.remove(name)
        for name in files:
            path = Path(parent) / name
            key = path.relative_to(target).as_posix()
            try:
                install.inspect_path(path.absolute())
            except install.Conflict:
                result[key] = {"unsafe_path": True}
                continue
            info = path.stat()
            result[key] = {"sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                           "size": info.st_size, "mtime_ns": info.st_mtime_ns}
    return dict(sorted(result.items()))


def prepare(distribution, output):
    distribution = distribution.absolute()
    revision, files = install.source_inputs(distribution)
    payload = {target: files[source] for source, target in install.PAYLOAD.items()}
    manifest = install.expected_manifest(revision, payload, list(install.ENVIRONMENTS))
    install.inspect_path(output.absolute())
    if output.exists():
        raise install.Conflict("Trial output must not exist")
    output.mkdir(parents=True)
    tasks = []
    for host in install.ENVIRONMENTS:
        cases = [(fixture, condition, repeat, SKILLS[fixture], PROMPTS[fixture])
                 for condition in ("baseline", "remora") for fixture in PROMPTS for repeat in (1, 2)]
        cases += [(case, "functional", 1, skill, prompt) for case, (skill, prompt) in FUNCTIONAL.items()]
        for case, condition, repeat, skill, prompt in cases:
            identity = f"{host}-{condition}-{case}-{repeat}"
            target = output / "targets" / identity
            fixture = case.split("-")[0]
            if fixture in {"F01", "F12"}:
                target.mkdir(parents=True)
            else:
                shutil.copytree(ROOT / "evals/fixtures" / fixture, target)
            if case == "F03":
                # The regression protocol requires a broken revision, not the
                # passing adoption fixture (evals/README.md).
                implementation = target / "ledger.py"
                original = implementation.read_bytes()
                expression = b'" ".join(label.split())'
                if original.count(expression) != 1:
                    raise install.Conflict("F03 regression seed no longer matches its fixture")
                implementation.write_bytes(original.replace(expression, b'label.strip()'))
            subprocess.run(["git", "init", "--quiet", str(target)], check=True, capture_output=True)
            if fixture not in {"F01", "F02", "F05"}:
                subprocess.run(["git", "-C", str(target), "-c", "core.autocrlf=false", "add", "."], check=True, capture_output=True)
                subprocess.run(["git", "-C", str(target), "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                                "-c", "commit.gpgsign=false", "commit", "--quiet", "--allow-empty", "-m", "trial input"], check=True, capture_output=True)
            if fixture not in {"F01", "F02"}:
                (target / "local-note.txt").write_text("Unrelated operator note: preserve these bytes.\n", encoding="utf-8")
            prepared_adoption = host == "codex" and fixture == "F05" and condition == "remora"
            if condition != "baseline" and (skill != "remora-bootstrap" or prepared_adoption):
                if prepared_adoption:
                    # Explicit fixture setup, not automatic target architecture selection.
                    selected_payload = {**payload, ".remora/profiles/local.md": files["profiles/local.md"]}
                    selected_manifest = install.expected_manifest(revision, selected_payload, list(install.ENVIRONMENTS), ["local"])
                    install.install(target, selected_payload, selected_manifest, [])
                else:
                    install.install(target, payload, manifest, [])
                if case == "F12":
                    (target / ".remora/standards/testing.md").unlink()
            invocation = ""
            if condition != "baseline":
                invocation = (f"Use the native ${skill} skill for the task. " if host == "codex"
                              else f"Select the native skill named {skill} for this task. ")
                if skill == "remora-bootstrap":
                    invocation += (f"Use trusted distribution {distribution} pinned to {revision}. "
                                   "Install for codex, cursor, antigravity; adopt existing root guidance only as requested below. ")
            tasks.append({"id": identity, "host": host, "condition": condition, "fixture": case,
                          "prepared_adoption": prepared_adoption,
                          "repeat": repeat, "target": str(target.absolute()), "source_revision": revision,
                          "prompt": COMMON + invocation + prompt, "before": snapshot(target)})
    if install.source_inputs(distribution) != (revision, files):
        raise install.Conflict("Distribution changed during preparation; no actors may start")
    (output / "tasks.json").write_text(json.dumps(tasks, indent=2) + "\n", encoding="utf-8")
    return tasks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--distribution", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    tasks = prepare(args.distribution, args.output)
    print(f"Prepared {len(tasks)} private tasks; actors must not read tasks.json or other targets")


if __name__ == "__main__":
    main()
