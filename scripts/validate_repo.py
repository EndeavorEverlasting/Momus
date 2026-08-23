#!/usr/bin/env python3
"""Validate the minimal Momus coordination harness."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "docs/AI_ENGINEERING_LEDGER.md",
    "docs/CURRENT_STATE.md",
    "docs/SPRINTS.md",
    "docs/evidence/2026-08-23-momusstudiofree-carryover.md",
    "harness/manifest.v1.json",
]

PLACEHOLDERS = [
    "lorem ipsum",
    "123 your street",
    "your city, st 12345",
    "a new project repository",
]

LEDGER_HEADINGS = [
    "## Overview",
    "## Goals",
    "## Specifications",
    "## Operating Model",
    "## Milestones",
    "## Known Risks and Failure Modes",
    "## Acceptance Gates",
    "## Next Action",
    "## Provenance",
]

SPRINT_IDS = ["P00", "P01", "P02", "P03", "P04", "P05"]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> int:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            fail(f"missing required file: {rel}")

    tracked_text = "\n".join(
        (ROOT / rel).read_text(encoding="utf-8")
        for rel in REQUIRED_FILES
        if rel.endswith((".md", ".json"))
    ).lower()

    for placeholder in PLACEHOLDERS:
        if placeholder in tracked_text:
            fail(f"placeholder text remains: {placeholder!r}")

    ledger = (ROOT / "docs/AI_ENGINEERING_LEDGER.md").read_text(encoding="utf-8")
    for heading in LEDGER_HEADINGS:
        if heading not in ledger:
            fail(f"ledger missing required heading: {heading}")

    sprints = (ROOT / "docs/SPRINTS.md").read_text(encoding="utf-8")
    for sprint_id in SPRINT_IDS:
        if f"## {sprint_id} —" not in sprints:
            fail(f"sprint registry missing {sprint_id}")

    manifest_path = ROOT / "harness/manifest.v1.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schema_version") != 1:
        fail("manifest schema_version must be 1")
    if manifest.get("current_sprint") != "P01":
        fail("manifest current_sprint must be P01")
    if manifest.get("current_state") != "READY_FOR_P01_BROWSER_PROOF":
        fail("manifest current_state does not match CURRENT_STATE")

    print(f"PASS: Momus harness validation ({len(REQUIRED_FILES)} required artifacts, {len(SPRINT_IDS)} sprint IDs)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
