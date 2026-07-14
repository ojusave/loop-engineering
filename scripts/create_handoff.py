#!/usr/bin/env python3
"""Create a structured specialist-loop handoff receipt."""

from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")[:48] or "loop"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--from-loop", required=True)
    parser.add_argument("--to-loop", required=True)
    parser.add_argument("--objective", required=True)
    parser.add_argument("--artifact", required=True)
    parser.add_argument("--state-dir", required=True, type=Path)
    args = parser.parse_args()

    state_dir = args.state_dir.expanduser().resolve()
    if not (state_dir / "state.md").is_file():
        parser.error(f"state.md not found in state directory: {state_dir}")

    handoffs = state_dir / "handoffs"
    handoffs.mkdir(exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S-%f")
    path = handoffs / f"{timestamp}-{slug(args.from_loop)}-to-{slug(args.to_loop)}.md"
    path.write_text(
        f"""# Specialist handoff

- **from:** {args.from_loop}
- **to:** {args.to_loop}
- **created_utc:** {timestamp}
- **status:** OPEN

## Objective

{args.objective}

## Artifact

{args.artifact}

## Current version or path

## Parent outcome and target measure

## Baseline and required evidence state

## Verified facts

## Evidence or commands

## Known weaknesses

## Constraints and non-goals

## May change

## Must preserve

## Target acceptance criteria

## Expected contribution and predicted observation

## Actual observation and measured delta

## Evidence state

Choose exactly one: `NO RELIABLE EVIDENCE`, `ARTIFACT VERIFIED`, `OUTCOME VALIDATED`, `DECISION READY`.

## Return state

Choose exactly one: `PASS`, `REWORK_REQUIRED`, `BLOCKED`, `NEEDS_HUMAN_JUDGMENT`.

## Specialist findings

## Parent disposition
""",
        encoding="utf-8",
    )
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
