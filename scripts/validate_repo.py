#!/usr/bin/env python3
"""Validate Momus repository harness and canonical ledger contracts."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "README.md",
    "AGENTS.md",
    "docs/AI_ENGINEERING_LEDGER.md",
    "docs/EXECUTION_PLAN.md",
    "harness/CODEBASE_MAP.md",
    "harness/WORKFLOWS.md",
    "harness/manifest.v1.json",
    "reports/README.md",
    "scripts/validate_repo.py",
    ".github/workflows/validate.yml",
]

LEDGER_REQUIRED_FIELDS = [
    "**State:**",
    "**Priority:**",
    "**Objective:**",
    "**Evidence/current truth:**",
    "**Owned scope:**",
    "**Dependencies:**",
    "**Acceptance criteria:**",
    "**Next action:**",
]

FORBIDDEN_LEDGER_TEXT = [
    "lorem ipsum",
    "your street",
    "your city",
    "consectetuer adipiscing",
    "duis autem",
]

EXPECTED_BOOTSTRAP_ITEMS = {
    "MOMUS-001",
    "MOMUS-002",
    "MOMUS-003",
    "MOMUS-004",
    "MOMUS-005",
}

ALLOWED_STATES = {"ready", "in_progress", "blocked", "done"}


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)
    print(f"FAIL: {message}")


def main() -> int:
    failures: list[str] = []

    for rel in REQUIRED_PATHS:
        if not (ROOT / rel).is_file():
            fail(f"required file missing: {rel}", failures)

    ledger_path = ROOT / "docs/AI_ENGINEERING_LEDGER.md"
    manifest_path = ROOT / "harness/manifest.v1.json"

    if ledger_path.is_file():
        ledger = ledger_path.read_text(encoding="utf-8")
        lowered = ledger.lower()

        for phrase in FORBIDDEN_LEDGER_TEXT:
            if phrase in lowered:
                fail(f"canonical ledger contains stale template text: {phrase!r}", failures)

        heading_matches = list(
            re.finditer(r"^### (MOMUS-\d{3}) — .+$", ledger, flags=re.MULTILINE)
        )
        ids = [match.group(1) for match in heading_matches]

        if not ids:
            fail("canonical ledger contains no MOMUS work items", failures)
        if len(ids) != len(set(ids)):
            fail("canonical ledger contains duplicate MOMUS work-item IDs", failures)

        missing_bootstrap = EXPECTED_BOOTSTRAP_ITEMS.difference(ids)
        if missing_bootstrap:
            fail(
                "canonical ledger is missing bootstrap work items: "
                + ", ".join(sorted(missing_bootstrap)),
                failures,
            )

        for index, match in enumerate(heading_matches):
            item_id = match.group(1)
            section_end = (
                heading_matches[index + 1].start()
                if index + 1 < len(heading_matches)
                else ledger.find("\n## Current sprint order", match.end())
            )
            if section_end == -1:
                section_end = len(ledger)
            section = ledger[match.end() : section_end]

            for field in LEDGER_REQUIRED_FIELDS:
                if field not in section:
                    fail(f"{item_id} missing required field {field}", failures)

            state_match = re.search(
                r"\*\*State:\*\* `([a-z_]+)`", section, flags=re.MULTILINE
            )
            if not state_match:
                fail(f"{item_id} has no parseable state", failures)
            elif state_match.group(1) not in ALLOWED_STATES:
                fail(
                    f"{item_id} has invalid state {state_match.group(1)!r}", failures
                )

    manifest: dict = {}
    if manifest_path.is_file():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(f"manifest is not valid JSON: {exc}", failures)

    if manifest:
        if manifest.get("schema_version") != "1.0":
            fail("manifest schema_version must be '1.0'", failures)
        if manifest.get("repository") != "EndeavorEverlasting/Momus":
            fail("manifest repository identity is incorrect", failures)

        canonical = manifest.get("canonical")
        if not isinstance(canonical, dict) or not canonical:
            fail("manifest canonical registry is missing", failures)
        else:
            for name, rel in canonical.items():
                if name == "reports_root":
                    if not (ROOT / rel).is_dir():
                        fail(f"manifest reports root does not exist: {rel}", failures)
                elif not (ROOT / rel).is_file():
                    fail(f"manifest canonical path does not exist: {name} -> {rel}", failures)

        ledger_ids = set()
        if ledger_path.is_file():
            ledger_ids = set(
                re.findall(
                    r"^### (MOMUS-\d{3}) — .+$",
                    ledger_path.read_text(encoding="utf-8"),
                    flags=re.MULTILINE,
                )
            )

        focus = manifest.get("work_items", {}).get("current_focus", [])
        for item_id in focus:
            if item_id not in ledger_ids:
                fail(f"manifest current_focus references unknown item: {item_id}", failures)

        dependencies = manifest.get("external_dependencies", [])
        dependency_ids: list[str] = []
        for dep in dependencies:
            dep_id = dep.get("id")
            owner = dep.get("owned_by")
            state = dep.get("state")
            resolution = dep.get("resolution")
            if not dep_id:
                fail("external dependency missing id", failures)
            else:
                dependency_ids.append(dep_id)
            if owner not in ledger_ids:
                fail(f"external dependency {dep_id!r} has unknown owner {owner!r}", failures)
            if not state:
                fail(f"external dependency {dep_id!r} missing state", failures)
            if not resolution:
                fail(f"external dependency {dep_id!r} missing resolution path", failures)

        if len(dependency_ids) != len(set(dependency_ids)):
            fail("manifest contains duplicate external dependency IDs", failures)

    if failures:
        print(f"\nMomus validation FAILED with {len(failures)} issue(s).")
        return 1

    print("PASS: required repository harness files are present")
    print("PASS: canonical ledger has no stale source-template filler")
    print(f"PASS: {len(EXPECTED_BOOTSTRAP_ITEMS)} bootstrap work items are registered and structured")
    print("PASS: manifest paths, work-item references, and dependency owners are valid")
    print("Momus validation PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
