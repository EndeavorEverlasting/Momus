#!/usr/bin/env python3
"""Validate the founder-corrected Momus identity and historical context adoption."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8-sig")


def main() -> None:
    adoption = json.loads(read("harness/context-workspace-adoption.v1.json"))
    require(adoption["schemaVersion"] == 1, "schemaVersion must be 1")
    require(adoption["repository"] == "EndeavorEverlasting/Momus", "wrong repository")
    require(adoption["role"] == "unifiedProduct", "historical ownership split must be retired")
    identity = adoption["projectIdentity"]
    require(identity["canonicalProduct"] == "Momus", "product name changed")
    require(identity["aliases"] == ["MomusStudio"], "MomusStudio must remain an alias")
    require(identity["canonicalRepository"] == "EndeavorEverlasting/Momus", "canonical repo changed")
    require(identity["sameIntendedProduct"] is True, "do not invent two products")
    require(identity["sourceOfTruth"] == "AGENTS.md", "root governance is required")
    require(identity["gitHistoryEquivalence"] == "UNVERIFIED", "cannot infer identical Git histories")
    require("pairedRepositories" not in adoption and "authorityMap" not in adoption,
            "active two-repository ownership map is forbidden")

    portable = adoption["portableContract"]
    require(portable["donorRepository"] == "EndeavorEverlasting/AgentSwitchboard", "donor evidence lost")
    require(re.fullmatch(r"[0-9a-f]{40}", portable["pinnedCommit"]) is not None, "unpinned donor")
    require(portable["pinnedCommit"] == "dab223c4039e5599ae99034fbcce86996c5983a3",
            "donor floor changed without review")
    require(portable["contractId"] == "agentswitchboard.context-workspace-boundary.v1",
            "historical contract ID lost")

    history = adoption["historicalPairedRepositories"]
    require(history == {
        "contextAuthority": "EndeavorEverlasting/Momus",
        "implementationAuthority": "EndeavorEverlasting/MomusStudio",
    }, "historical adoption evidence must be preserved, not enforced")
    require("historicalAuthorityMap" in adoption, "retired historic map missing")
    carryover = adoption["legacyCarryover"]
    require(carryover["status"] == "REFERENCE_ONLY_UNMAPPED", "unverified Git carryover was promoted")
    for word in ("filesystem path", "git remotes", "branch/ref", "HEAD SHA", "dirty/untracked state"):
        require(word.lower() in carryover["rule"].lower(), f"missing provenance gate: {word}")

    agents = read("AGENTS.md")
    require("MomusStudio is not a separate product" in agents, "creator rule missing")
    require("harness/context-workspace-adoption.v1.json" in agents,
            "root contract must index historical adoption")
    manifest = json.loads(read("harness/manifest.v1.json"))
    require(manifest["project_identity"]["same_intended_product"] is True,
            "manifest product identity drift")
    require(manifest["implementation_boundary"]["canonical_implementation_repository"]
            == "EndeavorEverlasting/Momus", "stale implementation routing")
    require(manifest["implementation_boundary"]["product_owner_split"] == "SUPERSEDED",
            "historic owner split reactivated")
    retirement = manifest["implementation_boundary"]
    require(retirement["historical_implementation_repository"] == "EndeavorEverlasting/MomusStudio",
            "retired alias changed unexpectedly")
    require(retirement["historical_implementation_repository_disposition"] in (
        "RETIRED_ALIAS_ARCHIVE_PENDING", "RETIRED_ALIAS_ARCHIVED",
    ), "retired alias was accidentally reactivated")
    receipt = "docs/evidence/2026-10-17-momusstudio-deprecation.md"
    require(retirement["historical_implementation_repository_retirement_evidence"] == receipt,
            "retirement evidence pointer missing or inconsistent")
    require(receipt in manifest["entrypoints"], "retirement evidence must be indexed")
    evidence = read(receipt)
    require("Only" in evidence or "**Only**" in evidence, "canonical routing evidence absent")
    require("GitHub archive: pending" in evidence or "RETIRED_ALIAS_ARCHIVED" in evidence,
            "retirement receipt lost its archive gate")

    require("harness/context-workspace-adoption.v1.json" in manifest["entrypoints"],
            "context adoption not indexed")
    require("python scripts/validate_context_workspace.py" in manifest["validators"],
            "consumer validator not indexed")
    workflow = read(".github/workflows/validate.yml")
    require("python scripts/validate_context_workspace.py" in workflow,
            "CI must run context validator")
    require("EXPECTED_SHA" in workflow and "git rev-parse HEAD" in workflow,
            "exact-head CI proof removed")
    print("PASS: Momus single-product identity and historical provenance separation")


if __name__ == "__main__":
    main()
