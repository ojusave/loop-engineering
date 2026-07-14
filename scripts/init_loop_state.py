#!/usr/bin/env python3
"""Initialize gitignored project-local state for an orchestrated loop task."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path


def find_project_root(start: Path) -> Path:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=start,
            check=True,
            capture_output=True,
            text=True,
        )
        return Path(result.stdout.strip()).resolve()
    except (FileNotFoundError, subprocess.CalledProcessError):
        return start.resolve()


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug[:56].rstrip("-") or "task"


def ensure_gitignore(root: Path) -> None:
    gitignore = root / ".gitignore"
    existing = gitignore.read_text(encoding="utf-8") if gitignore.exists() else ""
    if any(line.strip() == ".loop/" for line in existing.splitlines()):
        return
    separator = "" if not existing or existing.endswith("\n") else "\n"
    gitignore.write_text(
        existing + separator + "# Local loop-engineering state\n.loop/\n",
        encoding="utf-8",
    )


def create_task(root: Path, task: str, mode: str) -> Path:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S-%f")
    task_dir = root / ".loop" / f"{slugify(task)}-{timestamp}"
    (task_dir / "handoffs").mkdir(parents=True, exist_ok=False)

    state = f"""# Loop state

- **status:** ACTIVE
- **mode:** {mode}
- **task:** {task}
- **created_utc:** {timestamp}
- **assignment_status:** ACTIVE
- **evidence_state:** NO RELIABLE EVIDENCE

## Outcome owner or beneficiary

## Outcome class

Choose one: state change | artifact | decision | knowledge | capability | risk reduction

## Baseline

## Target state

## Intended context of use

## Primary measure and threshold

## Guardrails

## Required evidence state

Choose one: ARTIFACT VERIFIED | OUTCOME VALIDATED | DECISION READY

## Strongest feasible evidence now

## Next decision or use

## Artifact-verification and outcome-validation evidence

## Constraints and exclusions

## Fresh observations and repository findings

## Current direction and assumptions

## Selected specialist loops and order

## Artifacts and handoffs

## Cycle receipts

For each meaningful cycle record: hypothesis and mechanism; intervention or test; predicted observation; actual observation; delta from baseline or prior cycle; guardrail result; learning; next decision.

## Verification, validation, and evidence limitations

## Rejected directions

## Recovery and meta-improvement proposals

For each proposed persistent loop, prompt, rubric, routing, tool, or evaluator change record: recurring failure pattern; proposed change; predicted benefit; representative success, failure, and regression cases; before-and-after evidence; authority or approval required; adoption decision.

## Risks and unresolved decisions

## Next action

## Stop condition
"""
    (task_dir / "state.md").write_text(state, encoding="utf-8")
    (task_dir / "metadata.json").write_text(
        json.dumps(
            {
                "task": task,
                "mode": mode,
                "status": "ACTIVE",
                "evidence_state": "NO RELIABLE EVIDENCE",
                "created_utc": timestamp,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return task_dir


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task", required=True, help="Concise task description")
    parser.add_argument("--root", default=".", help="Project path; defaults to current directory")
    parser.add_argument(
        "--mode",
        choices=("light", "standard", "deep"),
        default="standard",
        help="Initial loop depth",
    )
    args = parser.parse_args()

    start = Path(args.root).expanduser()
    if not start.is_dir():
        parser.error(f"Project path is not a directory: {start}")

    root = find_project_root(start)
    ensure_gitignore(root)
    task_dir = create_task(root, args.task.strip(), args.mode)
    print(task_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
