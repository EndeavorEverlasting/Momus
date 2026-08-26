#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADOPTION_PATH = ROOT / "harness/context-workspace-adoption.v1.json"


def require(condition: bool, message: str):
    if not condition:
        raise AssertionError(message)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8-sig")


adoption = json.loads(ADOPTION_PATH.read_text(encoding="utf-8-sig"))
require(adoption["schemaVersion"] == 1, "schemaVersion must be 1")
require(adoption["adoptionId"] == "momus.context-workspace-boundary.v1", "unexpected adoption id")
require(adoption["adoptionVersion"] == "1.0.0", "unexpected adoption version")
require(adoption["repository"] == "EndeavorEverlasting/Momus", "unexpected repository")
require(adoption["role"] == "contextAuthority", "Momus must remain the context authority")

portable = adoption["portableContract"]
require(portable["donorRepository"] == "EndeavorEverlasting/AgentSwitchboard", "unexpected donor")
require(re.fullmatch(r"[0-9a-f]{40}", portable["pinnedCommit"]) is not None, "donor commit must be pinned")
require(portable["pinnedCommit"] == "dab223c4039e5599ae99034fbcce86996c5983a3", "donor floor moved without an adoption review")
require(portable["contractPath"] == ".ai/harness/context-workspace-boundary.contract.json", "contract path changed")
require(portable["schemaPath"] == ".ai/harness/schemas/context-workspace-boundary.schema.json", "schema path changed")
require(portable["contractId"] == "agentswitchboard.context-workspace-boundary.v1", "contract id changed")
require(portable["contractVersion"] == "1.0.0", "contract version changed")

paired = adoption["pairedRepositories"]
require(paired == {
    "contextAuthority": "EndeavorEverlasting/Momus",
    "implementationAuthority": "EndeavorEverlasting/MomusStudio",
}, "paired repository authority changed")

expected_context = {
    "projectIntentAndGoals",
    "epicsAndSprintDefinitions",
    "crossRepositoryArchitectureDecisions",
    "coordinationAndEvidenceRequirements",
    "projectLessons",
}
expected_implementation = {
    "sourceAndContentAssets",
    "testsAndBuildScripts",
    "runtimeConfiguration",
    "implementationDerivedStatus",
}
for key in expected_context:
    require(adoption["authorityMap"].get(key) == "EndeavorEverlasting/Momus", f"Momus authority changed: {key}")
for key in expected_implementation:
    require(adoption["authorityMap"].get(key) == "EndeavorEverlasting/MomusStudio", f"MomusStudio authority changed: {key}")

legacy = adoption["legacyCarryover"]
require(legacy["status"] == "REFERENCE_ONLY_UNMAPPED", "legacy carryover must remain unmapped until Git provenance is captured")
for field in ("filesystem path", "git remotes", "branch/ref", "HEAD SHA", "dirty/untracked state"):
    require(field.lower() in legacy["rule"].lower(), f"legacy provenance gate missing: {field}")

stale = adoption["staleReferenceHandling"]
require(stale["timestampOnlyResolutionAllowed"] is False, "timestamp-only conflict resolution is forbidden")
require(stale["authorityMismatch"] == "CONFLICT", "authority mismatch must fail closed")
require(stale["twoSidedDivergence"] == "CONFLICT", "two-sided divergence must fail closed")
require(adoption["consumerValidator"] == "python scripts/validate_context_workspace.py", "consumer validator identity changed")
require(len(adoption["rejectedDuplication"]) >= 3, "duplication boundaries missing")

agents = read("AGENTS.md")
current = read("docs/CURRENT_STATE.md")
sprints = read("docs/SPRINTS.md")
manifest = json.loads(read("harness/manifest.v1.json"))
workflow = read(".github/workflows/validate.yml")

for token in (
    "EndeavorEverlasting/MomusStudio",
    "context authority",
    "implementation authority",
    "REFERENCE_ONLY_UNMAPPED",
    "harness/context-workspace-adoption.v1.json",
):
    require(token.lower() in agents.lower(), f"AGENTS.md boundary token missing: {token}")

require("EndeavorEverlasting/MomusStudio" in current, "CURRENT_STATE must record the selected implementation authority")
require("reference-only" in current.lower() and "MomusStudiofree" in current, "CURRENT_STATE must preserve legacy carryover uncertainty")
require("EndeavorEverlasting/MomusStudio" in sprints, "SPRINTS must route implementation work to MomusStudio")
require("MomusStudiofree" in sprints and "provenance" in sprints.lower(), "SPRINTS must retain the legacy provenance gate")
require("harness/context-workspace-adoption.v1.json" in manifest.get("entrypoints", []), "harness manifest must register adoption manifest")
require("python scripts/validate_context_workspace.py" in manifest.get("validators", []), "harness manifest must register consumer validator")
require("python scripts/validate_context_workspace.py" in workflow, "CI must run consumer context validator")
require("EXPECTED_SHA" in workflow and "git rev-parse HEAD" in workflow, "CI must prove exact-head checkout")

print("PASS: Momus context workspace adoption")
