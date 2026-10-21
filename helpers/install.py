"""Preview, install, or check the minimal Remora payload from a trusted checkout."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys


SOURCE_ROOT = Path(__file__).resolve().parents[1]
PAYLOAD = {
    "standards/engineering.md": ".remora/standards/engineering.md",
    "standards/documentation.md": ".remora/standards/documentation.md",
    "skills/remora-audit-documentation/SKILL.md":
        ".agents/skills/remora-audit-documentation/SKILL.md",
}
INPUTS = ("helpers/install.py", *PAYLOAD,
          "skills/remora-bootstrap/SKILL.md", "templates/AGENTS.md")
MANIFEST = ".remora/installation.json"
ENVIRONMENTS = ("codex", "cursor", "antigravity")
FIELDS = {"schema_version", "remora_version", "source_revision", "selected_profiles",
          "target_environments", "managed_files"}


class Conflict(Exception):
    """An unsafe operation or an integrity failure; no replacement is permitted."""


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def inspect_path(path: Path):
    """Reject links/reparse points, including dangling links and ancestors."""
    for part in (*reversed(path.parents), path):
        try:
            info = part.lstat()
        except FileNotFoundError:
            continue
        if (stat.S_ISLNK(info.st_mode)
                or getattr(info, "st_file_attributes", 0)
                & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)):
            raise Conflict(f"Unsafe link or reparse point: {part}")
        if part != path and not stat.S_ISDIR(info.st_mode):
            raise Conflict(f"Ancestor is not a directory: {part}")


def source_payload(root: Path) -> tuple[str, dict[str, bytes]]:
    """Read only fixed, committed regular files; never run target tooling."""
    def git(*arguments):
        result = subprocess.run(["git", "--no-optional-locks", "-C", str(root),
                                 *arguments], capture_output=True, check=False)
        if result.returncode:
            raise OSError(f"Cannot read pinned source: git {' '.join(arguments)}: "
                          f"{result.stderr.decode('utf-8', errors='replace').strip()}")
        return result.stdout

    top = Path(os.fsdecode(git("rev-parse", "--show-toplevel").strip())).resolve()
    if top != root.resolve():
        raise Conflict("Installer must belong to the source checkout root")
    revision = git("rev-parse", "--verify", "HEAD^{commit}").decode("ascii").strip()
    committed = {}
    for name in INPUTS:
        inspect_path(root / name)
        entry = git("ls-tree", revision, "--", name)
        if not entry.startswith((b"100644 blob ", b"100755 blob ")):
            raise Conflict(f"Source input is not a committed regular file: {name}")
        committed[name] = git("show", f"{revision}:{name}")
        # Index flags can hide edits from git diff. Permit only checkout LF/CRLF
        # differences when comparing the actual inputs with committed bytes.
        if (root / name).read_bytes().replace(b"\r\n", b"\n") != committed[name].replace(b"\r\n", b"\n"):
            raise Conflict(f"Source input has local modifications: {name}")
    if git("diff", "--no-ext-diff", "--no-textconv", "--name-only", revision,
           "--", *INPUTS) or git("diff", "--cached", "--no-ext-diff", "--no-textconv",
                                "--name-only", revision, "--", *INPUTS):
        raise Conflict("Installation inputs have local modifications; use a pinned clean source")
    return revision, {destination: committed[source]
                      for source, destination in PAYLOAD.items()}


def expected_manifest(revision: str, payload: dict[str, bytes], environments: list[str]):
    return {"schema_version": 1, "remora_version": "development",
            "source_revision": revision, "selected_profiles": [],
            "target_environments": sorted(set(environments)),
            "managed_files": {name: digest(data) for name, data in payload.items()}}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise Conflict(f"Duplicate manifest field: {key}")
        result[key] = value
    return result


def read_manifest(path: Path) -> dict:
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    except (ValueError, UnicodeError, RecursionError) as error:
        raise Conflict(f"Malformed manifest: {error}") from error
    if not isinstance(manifest, dict) or set(manifest) != FIELDS:
        raise Conflict("Unsupported manifest fields")
    if type(manifest["schema_version"]) is not int or manifest["schema_version"] != 1:
        raise Conflict("Unsupported manifest schema_version")
    if manifest["remora_version"] != "development" or manifest["selected_profiles"] != []:
        raise Conflict("Unsupported release label or selected_profiles")
    revision = manifest["source_revision"]
    if not isinstance(revision, str) or not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", revision):
        raise Conflict("Invalid source_revision")
    environments = manifest["target_environments"]
    if (not isinstance(environments, list) or not environments
            or any(not isinstance(item, str) or item not in ENVIRONMENTS for item in environments)
            or environments != sorted(set(environments))):
        raise Conflict("Invalid target_environments")
    files = manifest["managed_files"]
    # The fixed inventory also prevents arbitrary manifest paths from being read.
    if not isinstance(files, dict) or set(files) != set(PAYLOAD.values()):
        raise Conflict("Unsupported managed_files inventory or unsafe path")
    if any(not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{64}", value)
           for value in files.values()):
        raise Conflict("Invalid managed file digest")
    return manifest


def inspect_target(target: Path, payload: dict[str, bytes]):
    inspect_path(target)
    if not target.is_dir():
        raise ValueError("Target must be an existing directory")
    for name in (*payload, MANIFEST):
        inspect_path(target / name)
        if (target / name).exists() and not (target / name).is_file():
            raise Conflict(f"Destination is not a regular file: {name}")


def validate(target: Path, expected: dict):
    manifest = read_manifest(target / MANIFEST)
    if manifest != expected:
        raise Conflict("Manifest differs from pinned source or requested selections; updates are unsupported")
    for name, wanted in expected["managed_files"].items():
        path = target / name
        if not path.is_file():
            raise Conflict(f"Missing managed file: {name}")
        if digest(path.read_bytes()) != wanted:
            raise Conflict(f"Modified managed file: {name}")


def create_file(target: Path, name: str, data: bytes, created: list[str]):
    path = target / name
    inspect_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    inspect_path(path)
    try:
        with path.open("xb") as stream:
            created.append(name)
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
    except FileExistsError as error:
        raise Conflict(f"Destination appeared before creation: {name}") from error
    inspect_path(path)
    if path.read_bytes() != data:
        raise Conflict(f"Written file failed byte verification: {name}")


def install(target: Path, payload: dict[str, bytes], expected: dict, created: list[str]):
    # Repeat the whole preflight after preview and before any writes.
    inspect_target(target, payload)
    for name in (*payload, MANIFEST):
        if (target / name).exists():
            raise Conflict(f"Unmanaged destination is occupied: {name}")
    for name, data in payload.items():
        create_file(target, name, data, created)
    inspect_target(target, payload)
    for name, data in payload.items():
        if (target / name).read_bytes() != data:
            raise Conflict(f"Payload changed before manifest publication: {name}")
    data = (json.dumps(expected, indent=2, sort_keys=True) + "\n").encode("utf-8")
    create_file(target, MANIFEST, data, created)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, required=True)
    parser.add_argument("--environment", choices=ENVIRONMENTS, action="append")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--apply", action="store_true", help="create the declared installation")
    modes.add_argument("--check", action="store_true", help="check against this pinned source")
    arguments = parser.parse_args(argv)
    if arguments.check and arguments.environment:
        parser.error("--check reads environments from the manifest; omit --environment")
    if not arguments.check and not arguments.environment:
        parser.error("preview/apply requires at least one --environment")
    created = []
    try:
        # Inspect lexical ancestors before collapsing '..', which could hide a link.
        inspect_path(arguments.target.absolute())
        target = Path(os.path.abspath(arguments.target))
        revision, payload = source_payload(SOURCE_ROOT)
        inspect_target(target, payload)
        manifest_path = target / MANIFEST
        if arguments.check:
            if not manifest_path.is_file():
                raise Conflict("Missing installation manifest")
            environments = read_manifest(manifest_path)["target_environments"]
        else:
            environments = arguments.environment
        expected = expected_manifest(revision, payload, environments)
        if manifest_path.exists():
            validate(target, expected)
            print("Installation verified against pinned source; no changes")
            return 0
        for name in payload:
            if (target / name).exists():
                raise Conflict(f"Unmanaged destination is occupied: {name}")
        if not arguments.apply:
            print(f"Preview pinned source {revision}; no changes")
            for name in (*payload, MANIFEST):
                print(f"Would create: {name}")
            return 0
        install(target, payload, expected, created)
        print(f"Installed and verified pinned source {revision}")
        return 0
    except Conflict as error:
        print(f"Installation conflict: {error}", file=sys.stderr)
        return 1
    except (OSError, ValueError, UnicodeError) as error:
        print(f"Installation incomplete: {error}", file=sys.stderr)
        return 2
    finally:
        if created:
            print("Created files: " + ", ".join(created))


if __name__ == "__main__":
    sys.exit(main())
