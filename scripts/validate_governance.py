#!/usr/bin/env python3
"""Fail-closed root governance validator for Momus. Stdlib only."""

from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "AGENTS.md"

REQUIRED_HEADINGS = (
    "# Momus Agent Contract",
    "## Creator-authoritative product identity",
    "## Agent operating principles",
    "## Instruction precedence",
    "## Mandatory writing-sprint declaration",
    "## Required execution workflow",
    "## Completion standard",
    "## Forbidden behaviors",
    "## Evidence, safety and historical status",
    "## Verification entrypoints",
)
REQUIRED_RULES = (
    "MomusStudio is not a separate product",
    "EndeavorEverlasting/Momus",
    "same intended AI-video product",
    "Evidence before action",
    "Floor before furniture",
    "One writer per branch",
    "Reuse before replacing",
    "No completion without proof",
    "Platform requirements",
    "This root governance contract",
    "Task-specific prompts",
    "Generic defaults",
    "Repository and branch",
    "Lane and mission",
    "Owned scope and forbidden scope",
    "Expected artifacts",
    "Proof ceiling",
    "commit SHA",
    "push/PR",
    "NEXT COMMAND",
    "REFERENCE_ONLY_UNMAPPED",
    "secrets",
)


def validate_contract(source: str) -> list[str]:
    problems = []
    if not source.startswith("# Momus Agent Contract\n"):
        problems.append("not the expected root contract")
    for heading in REQUIRED_HEADINGS:
        if source.count(heading) != 1:
            problems.append(f"missing or duplicate governance heading: {heading}")
    for rule in REQUIRED_RULES:
        if rule not in source:
            problems.append(f"missing governance requirement: {rule}")
    if source.count("MomusStudio is not a separate product") != 1:
        problems.append("founder identity authority must occur exactly once")
    if "That mapping is superseded as product governance" not in source:
        problems.append("historical split has not been explicitly superseded")
    return problems


def self_test(source: str) -> None:
    assert not validate_contract(source), "positive governance control failed"
    negatives = (
        source.replace("MomusStudio is not a separate product", "MomusStudio is a separate product"),
        source.replace("## Instruction precedence", "## Old heading"),
        source.replace("One writer per branch", "Any number of writers per branch"),
        source.replace("That mapping is superseded as product governance", "That mapping still governs"),
    )
    for i, candidate in enumerate(negatives, 1):
        assert validate_contract(candidate), f"negative mutation {i} escaped governance check"
    print(f"PASS: governance mutation controls ({len(negatives)} negative, 1 positive)")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if not CONTRACT.is_file():
        print("FAIL: missing root AGENTS.md")
        return 1
    source = CONTRACT.read_text(encoding="utf-8")
    problems = validate_contract(source)
    for problem in problems:
        print(f"FAIL: {problem}")
    if problems:
        return 1
    if args.self_test:
        self_test(source)
    print("PASS: founder identity and agent governance contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
