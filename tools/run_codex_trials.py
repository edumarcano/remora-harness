"""Collect fresh native Codex sessions for prepared tasks; no semantic auto-scoring."""

import argparse
import json
import os
from pathlib import Path
import subprocess
import time

from prepare_trials import snapshot


def run(task, destination):
    destination.mkdir(parents=True, exist_ok=False)
    (destination / "task.json").write_text(json.dumps(task, indent=2) + "\n", encoding="utf-8")
    start = time.monotonic()
    timeout = False
    command = ["codex", "exec", "--json", "--color", "never", "--sandbox", "workspace-write",
               "--ephemeral", "-C", task["target"]]
    personal = Path.home() / ".agents/skills/remora-bootstrap/SKILL.md"
    if task["condition"] == "baseline" and personal.is_file():
        # Session-local documented disable: retain all other user configuration.
        command.extend(("-c", "skills.config=[{path=" + json.dumps(str(personal)) + ",enabled=false}]"))
    command.append("-")
    (destination / "command.json").write_text(json.dumps(command, indent=2) + "\n", encoding="utf-8")
    with (destination / "events.jsonl").open("w", encoding="utf-8") as out, (destination / "stderr.txt").open("w", encoding="utf-8") as err:
        process = subprocess.Popen(command,
                                   stdin=subprocess.PIPE, stdout=out, stderr=err, text=True, encoding="utf-8")
        try:
            process.communicate(task["prompt"], timeout=600)
        except subprocess.TimeoutExpired:
            timeout = True
            # Kill only this task's process tree, never unrelated host processes.
            if os.name == "nt":
                subprocess.run(["taskkill", "/PID", str(process.pid), "/T", "/F"], capture_output=True)
            else:
                process.kill()
            process.wait()
    result = {"id": task["id"], "seconds": round(time.monotonic() - start, 2),
              "exit_code": process.returncode, "timeout": timeout,
              "after": snapshot(Path(task["target"])), "semantic_status": "unscored"}
    (destination / "result.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in ("id", "seconds", "exit_code", "timeout")}), flush=True)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tasks", type=Path, required=True)
    parser.add_argument("--condition", choices=("baseline", "remora", "functional"), required=True)
    parser.add_argument("--only", help="exact task ID, for a reviewed retry")
    parser.add_argument("--results", type=Path, required=True, help="new result parent; retries need a new directory")
    args = parser.parse_args()
    if args.results.exists():
        parser.error("results parent must not exist")
    tasks = json.loads(args.tasks.read_text(encoding="utf-8"))
    selected = [task for task in tasks if task["host"] == "codex" and task["condition"] == args.condition
                and (args.only is None or task["id"] == args.only)]
    if not selected:
        parser.error("no matching tasks")
    args.results.mkdir(parents=True)
    for task in selected:
        result = run(task, args.results / task["id"])
        if result["exit_code"] != 0 or result["timeout"]:
            raise SystemExit("Actor incomplete: inspect evidence before continuing or retrying")


if __name__ == "__main__":
    main()
