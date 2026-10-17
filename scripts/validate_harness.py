#!/usr/bin/env python3
"""Validate completeness of the Momus operational harness; no network or dependencies."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "AGENTS.md",
    "harness/codebase-map.md",
    "harness/workflows.md",
    "harness/manifest.v1.json",
    "harness/context-workspace-adoption.v1.json",
    "harness/paths.v1.json",
    "harness/artifacts.v1.json",
    "harness/operator-report.md",
    "harness/skills/creative-shot-handoff.md",
    "scripts/validate_repo.py",
    "scripts/validate_governance.py",
    "scripts/validate_context_workspace.py",
    "scripts/validate_harness.py",
    ".github/workflows/validate.yml",
)


def validate_contract(manifest: dict, paths: dict, artifacts: dict, adoption: dict) -> list[str]:
    issues: list[str] = []
    def check(ok: bool, why: str) -> None:
        if not ok:
            issues.append(why)

    for name, value in (("manifest", manifest), ("paths", paths),
                        ("artifacts", artifacts)):
        check(value.get("schema_version") == 1, f"{name}: unsupported schema")
    identity = manifest.get("project_identity", {})
    check(identity.get("canonical_name") == "Momus", "manifest: canonical product")
    check(identity.get("historical_aliases") == ["MomusStudio"], "manifest: historical alias")
    check(identity.get("same_intended_product") is True, "manifest: must represent one product")
    check(identity.get("canonical_repository") == "EndeavorEverlasting/Momus",
          "manifest: canonical repository")
    check(identity.get("git_equivalence") == "UNVERIFIED",
          "manifest: unverified code histories may not be unified by assumption")
    check(manifest.get("implementation_boundary", {}).get("product_owner_split") == "SUPERSEDED",
          "manifest: historical product split reappeared")
    check(manifest.get("implementation_boundary", {}).get("canonical_implementation_repository")
          == "EndeavorEverlasting/Momus", "manifest: implementation sent to arbitrary other repo")
    check(adoption.get("projectIdentity", {}).get("sameIntendedProduct") is True,
          "adoption: product alias contradiction")
    check("pairedRepositories" not in adoption and "authorityMap" not in adoption,
          "adoption: active two-repository routing forbidden")
    check(adoption.get("legacyCarryover", {}).get("status") == "REFERENCE_ONLY_UNMAPPED",
          "adoption: Git provenance proof was fabricated")

    check(paths.get("canonical_product") == "Momus", "paths: product identity")
    check(paths.get("canonical_repository") == "EndeavorEverlasting/Momus",
          "paths: canonical remote changed")
    check(paths.get("historical_product_aliases") == ["MomusStudio"],
          "paths: historical alias drift")
    profile = paths.get("profile", {})
    for key in ("development_checkout", "production_use_path",
                "temporary_worktree_root"):
        entry = profile.get(key, {})
        check(entry.get("state") in ("UNKNOWN", "VERIFIED"), f"paths: {key} state missing")
        if entry.get("state") == "UNKNOWN":
            check(entry.get("path") is None, f"paths: {key} fabricated path")
            check(bool(entry.get("resolution")), f"paths: {key} lacks discovery action")
        else:
            check(isinstance(entry.get("path"), str) and entry["path"].startswith("/"),
                  f"paths: {key} verified path invalid")
    entry = profile.get("operator_entrypoint", {})
    check(entry.get("state") in ("UNKNOWN", "VERIFIED"), "paths: entrypoint missing status")
    if entry.get("state") == "UNKNOWN":
        check(entry.get("url") is None, "paths: historical URL promoted as live")
        check(bool(entry.get("resolution")), "paths: entrypoint no proof route")
    check(profile.get("proof", {}).get("real_entrypoint_observed") == "UNKNOWN"
          or entry.get("state") == "VERIFIED", "paths: contradictory live proof")

    check(artifacts.get("canonical_repository") == "EndeavorEverlasting/Momus",
          "artifact registry wrong remote")
    entries = artifacts.get("artifacts", [])
    check(len(entries) >= 5, "artifact registry has insufficient real consumers")
    ids = [a.get("id") for a in entries]
    check(len(set(ids)) == len(ids), "artifact registry duplicates IDs")
    for a in entries:
        raw_path = a.get("path", "")
        parts = Path(raw_path).parts if isinstance(raw_path, str) else ()
        check(bool(parts) and not Path(raw_path).is_absolute() and ".." not in parts,
              f"artifact registry invalid path: {raw_path!r}")
        check(bool(a.get("owner")) and bool(a.get("validate")),
              f"artifact registry lacks owner/validator: {raw_path!r}")
    for required in REQUIRED:
        check(required in manifest.get("entrypoints", []) or required in (
            "scripts/validate_repo.py", "scripts/validate_governance.py",
            "scripts/validate_context_workspace.py", "scripts/validate_harness.py",
            ".github/workflows/validate.yml"), f"manifest: unregistered harness input {required}")
    for val in ("python scripts/validate_governance.py --self-test",
                "python scripts/validate_harness.py --self-test",
                "python scripts/validate_context_workspace.py"):
        check(val in manifest.get("validators", []),
              f"manifest missing validator {val}")
    return issues


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    missing = [p for p in REQUIRED if not (ROOT / p).is_file()]
    if missing:
        print("FAIL: missing harness components: " + ", ".join(missing))
        return 1
    def load(p: str) -> dict:
        return json.loads((ROOT / p).read_text(encoding="utf-8"))
    m = load("harness/manifest.v1.json")
    p = load("harness/paths.v1.json")
    a = load("harness/artifacts.v1.json")
    adoption = load("harness/context-workspace-adoption.v1.json")
    errors = validate_contract(m, p, a, adoption)
    for problem in errors:
        print("FAIL: " + problem)
    if errors:
        return 1
    for artifact in a["artifacts"]:
        if not (ROOT / artifact["path"]).is_file():
            print("FAIL: indexed artifact missing: " + artifact["path"])
            return 1
    if args.self_test:
        import copy
        negative = copy.deepcopy(m)
        negative["project_identity"]["same_intended_product"] = False
        assert validate_contract(negative, p, a, adoption), "identity mutation escaped"
        negative_paths = copy.deepcopy(p)
        negative_paths["profile"]["development_checkout"]["path"] = "/invented/checkout"
        assert validate_contract(m, negative_paths, a, adoption), "path fabrication escaped"
        negative_adoption = copy.deepcopy(adoption)
        negative_adoption["pairedRepositories"] = {"implementationAuthority": "other"}
        assert validate_contract(m, p, a, negative_adoption), "old split escaped"
        print("PASS: harness negative controls (3) and positive control")
    print(f"PASS: harness components and project identity ({len(REQUIRED)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
