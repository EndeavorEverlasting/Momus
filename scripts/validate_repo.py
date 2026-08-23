#!/usr/bin/env python3
"""Validate the Momus coordination harness and machine-readable execution contract."""

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
    "docs/evidence/2026-08-23-waoowaoo-public-source.md",
    "harness/manifest.v1.json",
    ".github/workflows/validate.yml",
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

EXPECTED_RUNTIME = {
    "application": "waoowaoo",
    "local_url": "http://localhost:13000",
    "minimum_provider_chain": ["text", "image", "video"],
}

EXPECTED_PROJECT = {
    "title": "The AI Intern Takes Corporate Speak Literally",
    "aspect_ratio": "9:16",
    "generation_rule": "one representative shot before batching",
    "audio_check": "explicitly verify audio presence",
}

EXPECTED_PUBLIC_SOURCE = "waooAI/waoowaoo"


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

    required_ledger_facts = [
        "http://localhost:13000",
        "The AI Intern Takes Corporate Speak Literally",
        "9:16",
        "three green connection checks",
        "one representative shot before batching",
    ]
    for fact in required_ledger_facts:
        if fact not in ledger:
            fail(f"ledger lost required execution fact: {fact!r}")

    sprints = (ROOT / "docs/SPRINTS.md").read_text(encoding="utf-8")
    for sprint_id in SPRINT_IDS:
        if f"## {sprint_id} —" not in sprints:
            fail(f"sprint registry missing {sprint_id}")

    manifest_path = ROOT / "harness/manifest.v1.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"manifest is invalid JSON: {exc}")

    if manifest.get("schema_version") != 1:
        fail("manifest schema_version must be 1")
    if manifest.get("repository") != "EndeavorEverlasting/Momus":
        fail("manifest repository identity is incorrect")
    if manifest.get("current_sprint") != "P01":
        fail("manifest current_sprint must be P01")
    if manifest.get("current_state") != "READY_FOR_P01_BROWSER_PROOF":
        fail("manifest current_state does not match CURRENT_STATE")

    for entrypoint in manifest.get("entrypoints", []):
        if not (ROOT / entrypoint).is_file():
            fail(f"manifest entrypoint does not exist: {entrypoint}")

    for workflow in manifest.get("ci_workflows", []):
        if not (ROOT / workflow).is_file():
            fail(f"manifest CI workflow does not exist: {workflow}")

    runtime = manifest.get("runtime_contract", {})
    for key, expected in EXPECTED_RUNTIME.items():
        if runtime.get(key) != expected:
            fail(f"runtime_contract.{key} must be {expected!r}")

    project = runtime.get("representative_project", {})
    for key, expected in EXPECTED_PROJECT.items():
        if project.get(key) != expected:
            fail(f"runtime_contract.representative_project.{key} must be {expected!r}")

    proof_gates = manifest.get("proof_gates", {})
    expected_gate_owners = {
        "provider_connectivity": "pending_P01",
        "representative_shot": "pending_P02",
        "generation_export": "pending_P02",
        "reproducibility": "pending_P03",
        "shared_use_hardening": "pending_P04",
    }
    for gate, expected in expected_gate_owners.items():
        if proof_gates.get(gate) != expected:
            fail(f"proof gate {gate!r} must be routed as {expected!r}")

    boundary = manifest.get("implementation_boundary", {})
    if boundary.get("momus_contains_product_source") is not False:
        fail("manifest must not claim product source is present in Momus")
    if boundary.get("local_checkout_binding") != "unproven":
        fail("local MomusStudiofree binding must remain unproven until local git evidence is captured")

    public_sources = manifest.get("public_source_references", [])
    if not any(source.get("repository") == EXPECTED_PUBLIC_SOURCE for source in public_sources):
        fail(f"manifest must preserve public source reference {EXPECTED_PUBLIC_SOURCE}")

    print(
        "PASS: Momus harness validation "
        f"({len(REQUIRED_FILES)} required artifacts, {len(SPRINT_IDS)} sprint IDs, runtime contract sealed)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
