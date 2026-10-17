#!/usr/bin/env python3
"""Validate the Momus creator UX contract; optionally reject incomplete live-cert receipts.

Static structural success is NOT evidence that a browser/device test actually ran.
"""
import argparse
import json
import re
import sys
from pathlib import Path

DEFAULT_CONTRACT = Path(__file__).resolve().parents[1] / "harness" / "ux-readiness.v1.json"
REQUIRED_CASES = {
    "desktop_creator_journey", "desktop_constrained_geometry", "keyboard_terminal_actions",
    "firefox_browser_parity", "state_failure_recovery", "persistence_and_no_loss",
    "accessibility_motion",
}
PHONE_CASES = {"phone_portrait_touch", "phone_orientation_cycle"}
SHA = re.compile(r"^[0-9a-f]{40}$")


def validate_contract(document):
    if not isinstance(document, dict) or document.get("schema_version") != 1:
        raise ValueError("unsupported UX contract schema")
    if document.get("product") != "Momus" or document.get("proof_state") != "NOT_CERTIFIED":
        raise ValueError("contract must preserve canonical identity and uncertified baseline")
    policy = document.get("supported_mode_policy", {})
    if policy.get("desktop") != "required" or policy.get("phone_touch") != "explicit_candidate_decision_required":
        raise ValueError("desktop and phone-disposition policies must be explicit")
    cases = document.get("cases")
    if not isinstance(cases, list) or not cases:
        raise ValueError("missing cases")
    ids = [case.get("id") for case in cases if isinstance(case, dict)]
    if len(ids) != len(cases) or len(ids) != len(set(ids)):
        raise ValueError("missing or duplicate case id")
    if not REQUIRED_CASES.issubset(ids) or not PHONE_CASES.issubset(ids):
        raise ValueError("required acceptance case missing")
    for case in cases:
        if case.get("id") in REQUIRED_CASES and case.get("required") is not True:
            raise ValueError("required desktop check downgraded")
        if case.get("mode") not in {"desktop_pointer", "desktop_keyboard", "phone_touch"}:
            raise ValueError("invalid input mode")
        if not isinstance(case.get("description"), str) or len(case["description"]) < 24:
            raise ValueError("non-actionable acceptance check")
    return ids


def validate_receipt(receipt, document):
    if not isinstance(receipt, dict):
        raise ValueError("missing receipt")
    for field in ("candidate_sha", "candidate_source", "runtime_url", "tested_at", "browser_run_artifact"):
        value = receipt.get(field)
        if not isinstance(value, str) or not value.strip() or "placeholder" in value.lower():
            raise ValueError(f"missing or placeholder {field}")
    if not SHA.fullmatch(receipt["candidate_sha"]):
        raise ValueError("candidate_sha must be an exact 40-character Git commit")
    if not receipt["runtime_url"].startswith(("http://", "https://")):
        raise ValueError("runtime URL must be HTTP(S)")
    phone = receipt.get("phone_support")
    if phone not in {"supported", "explicitly_unsupported"}:
        raise ValueError("phone support decision is unresolved")
    if phone == "explicitly_unsupported" and len(str(receipt.get("phone_exclusion_reason", ""))) < 25:
        raise ValueError("unsupported phone policy needs a substantive public rationale")
    results = receipt.get("results")
    if not isinstance(results, list):
        raise ValueError("missing case results")
    ids = validate_contract(document)
    by_id = {case.get("id"): case for case in results if isinstance(case, dict)}
    if len(by_id) != len(results):
        raise ValueError("duplicate or malformed case result")
    required = REQUIRED_CASES | (PHONE_CASES if phone == "supported" else set())
    for identifier in required:
        item = by_id.get(identifier)
        if item is None or item.get("status") != "pass":
            raise ValueError(f"live case not passed: {identifier}")
        for field in ("browser", "viewport", "input_mode", "evidence_artifact", "terminal_observation"):
            if not isinstance(item.get(field), str) or not item[field].strip():
                raise ValueError(f"missing {field} for {identifier}")
    if set(by_id) - set(ids):
        raise ValueError("receipt has unknown cases")
    if receipt.get("blocking_defects") != []:
        raise ValueError("blocking defects present or not explicitly dispositioned")
    # This proves receipt consistency only, not whether attachments or observed actions are real.
    return len(required)


def self_test(document):
    ids = validate_contract(document)
    assert len(ids) >= 9
    invalid = json.loads(json.dumps(document))
    invalid["cases"] = [item for item in invalid["cases"] if item["id"] != "keyboard_terminal_actions"]
    try:
        validate_contract(invalid)
    except ValueError:
        pass
    else:
        raise AssertionError("missing keyboard check was accepted")
    sample = {
        "candidate_sha": "a" * 40, "candidate_source": "local source checkout",
        "runtime_url": "http://127.0.0.1:13000", "tested_at": "2026-10-17T22:00:00Z",
        "browser_run_artifact": "reports/playwright-run.json", "phone_support": "explicitly_unsupported",
        "phone_exclusion_reason": "Desktop creative editing is the explicitly supported release target.",
        "results": [
            {"id": case_id, "status": "pass", "browser": "Firefox", "viewport": "1280x800",
             "input_mode": "keyboard", "evidence_artifact": "reports/result.json",
             "terminal_observation": "Real action completed"}
            for case_id in REQUIRED_CASES
        ], "blocking_defects": []
    }
    assert validate_receipt(sample, document) == len(REQUIRED_CASES)
    sample["results"][0]["status"] = "blocked"
    try:
        validate_receipt(sample, document)
    except ValueError:
        pass
    else:
        raise AssertionError("blocked browser case was accepted")
    print("PASS: UX contract and negative-control receipt checks")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--receipt", type=Path, help="Verify the current live-cert evidence receipt")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    try:
        document = json.loads(args.contract.read_text(encoding="utf-8"))
        count = len(validate_contract(document))
        if args.self_test:
            self_test(document)
        if args.receipt:
            receipt = json.loads(args.receipt.read_text(encoding="utf-8"))
            count = validate_receipt(receipt, document)
            print(f"STRUCTURALLY COMPLETE: {count} live UX cases; verify runtime artifacts independently")
        else:
            print(f"PASS: {count} UX case definitions; NOT CERTIFIED without live browser receipt")
    except (OSError, ValueError, json.JSONDecodeError, AssertionError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
