#!/usr/bin/env python3
"""Validate that a specialist handoff contains required fields and a return state."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

REQUIRED_HEADINGS = (
    "Objective",
    "Artifact",
    "Parent outcome and target measure",
    "Baseline and required evidence state",
    "Verified facts",
    "Evidence or commands",
    "Known weaknesses",
    "Constraints and non-goals",
    "May change",
    "Must preserve",
    "Target acceptance criteria",
    "Expected contribution and predicted observation",
    "Actual observation and measured delta",
    "Evidence state",
    "Return state",
)
VALID_STATES = {"PASS", "REWORK_REQUIRED", "BLOCKED", "NEEDS_HUMAN_JUDGMENT"}
VALID_EVIDENCE_STATES = {
    "NO RELIABLE EVIDENCE",
    "ARTIFACT VERIFIED",
    "OUTCOME VALIDATED",
    "DECISION READY",
}


def section(text: str, heading: str) -> str:
    match = re.search(
        rf"^## {re.escape(heading)}\s*$\n(.*?)(?=^## |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    return match.group(1).strip() if match else ""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("handoff", type=Path)
    args = parser.parse_args()

    try:
        text = args.handoff.read_text(encoding="utf-8")
    except OSError as exc:
        parser.error(str(exc))

    problems: list[str] = []
    for heading in REQUIRED_HEADINGS:
        if f"## {heading}" not in text:
            problems.append(f"missing heading: {heading}")

    state_text = section(text, "Return state")
    found_states = {state for state in VALID_STATES if re.search(rf"\b{state}\b", state_text)}
    if len(found_states) != 1:
        problems.append("Return state must contain exactly one completed valid state")

    evidence_text = section(text, "Evidence state")
    found_evidence_states = {
        state for state in VALID_EVIDENCE_STATES if re.search(rf"\b{re.escape(state)}\b", evidence_text)
    }
    if len(found_evidence_states) != 1:
        problems.append("Evidence state must contain exactly one completed valid state")

    for heading in (
        "Objective",
        "Artifact",
        "Parent outcome and target measure",
        "Baseline and required evidence state",
        "Target acceptance criteria",
        "Expected contribution and predicted observation",
        "Actual observation and measured delta",
        "Evidence or commands",
    ):
        if not section(text, heading):
            problems.append(f"empty required section: {heading}")

    if problems:
        for problem in problems:
            print(f"ERROR: {problem}")
        return 1

    print(f"Valid handoff: {args.handoff}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
