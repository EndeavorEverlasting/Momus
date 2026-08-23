# Momus Workflows

## 1. Pick up a task

1. Read `AGENTS.md`, then `docs/AI_ENGINEERING_LEDGER.md`.
2. Refresh repository/branch/PR truth and inspect existing reports for the target item.
3. Prefer an `in_progress` item already owned by the branch; otherwise choose the earliest `ready` item whose dependencies are satisfied.
4. State repo/ref, lane, mission, owned scope, forbidden scope, expected artifacts, validation commands, and proof ceiling before the first write.
5. Use a separate branch/worktree when another agent owns overlapping work.

## 2. Evidence review

Before implementation, distinguish these evidence classes:

- **repository evidence:** Momus ledger/contracts/reports;
- **local carryover evidence:** `MomusStudiofree`, git state, OpenCode context, local runtime;
- **upstream evidence:** `waooAI/waoowaoo` documentation/source;
- **runtime evidence:** browser/UI connection checks, generated outputs, export/audio/reproduction behavior.

Do not use upstream defaults to overwrite local carryover facts that have not been inspected.

## 3. MOMUS-002 — Recover local provenance

**Output:** `reports/carryover-inventory.md`

On the original workstation:

1. locate `MomusStudiofree`;
2. capture git remote(s), branch, HEAD, status, dirty/untracked state, and recent relevant commits;
3. inspect OpenCode session/state tied to the work;
4. record important prompts/configs/scripts/assets and the last known runtime command from evidence;
5. compare with `waooAI/waoowaoo` without assuming the local tree is clean/current;
6. classify components as preserve, import, reference, or retire.

No destructive cleanup or blind upgrade belongs in this flow.

## 4. MOMUS-003 — Prove local runtime and provider connectivity

**Output:** `reports/waoowaoo-runtime-proof.md`

1. Open `http://localhost:13000`.
2. Authenticate with the existing local test account.
3. Open API Configuration / Settings.
4. Configure the minimum text model → image model → video model chain.
5. Enter provider keys in the UI only. Never place keys in Git, chat artifacts, screenshots, or reports.
6. Run all three provider connection checks.
7. Record safe provider/model names and each check result.
8. Stop the claim at connectivity. Do not mark generation proven here.

Failure handling: record the exact failed gate and safe error text; change only the minimum configuration needed to retest that gate.

## 5. MOMUS-004 — Prove one representative generation

**Prerequisite:** MOMUS-003 has three green provider checks.

1. Create **“The AI Intern Takes Corporate Speak Literally”**.
2. Set the project/output to **9:16**.
3. Use one representative, visually testable prompt/story input.
4. Generate exactly one representative shot first.
5. Record prompt/input lineage, safe generation metadata, visible result, and durable result reference.
6. Do not batch merely to prove generation.
7. Record export as a separate gate.

## 6. MOMUS-005 — Patrick critique and revision loop

**Output:** `reports/pat-first-video-sprint.md`

1. Review the representative shot with Patrick.
2. Capture Patrick's desired outcome and visible critique.
3. Isolate one meaningful prompt-to-output mismatch.
4. Revise one prompt dimension deliberately rather than changing everything.
5. Generate a follow-up when useful and affordable.
6. Record what changed in the prompt and what visibly changed in the output.
7. Verify audio explicitly.
8. Verify export explicitly.
9. Attempt a clean reproduction and record the achieved ceiling.
10. Update this workflow only with steps that were actually proven.

## 7. Proof-gate vocabulary

Use these terms precisely in reports and handoffs:

- source/provenance proven;
- runtime access proven;
- provider connectivity proven;
- generation proven;
- audio proven/unproven;
- export proven/unproven;
- reproducibility proven/unproven;
- LAN/shared readiness proven/unproven.

A lower gate never implies a higher gate.

## 8. Validate before commit

Run:

```bash
python scripts/validate_repo.py
```

Any nonzero result blocks a clean completion claim. Fix the canonical owner rather than weakening the validator to hide a contract failure.

## 9. Network/shared-use safety

The current workflow is local-first. Do not expose the local service to LAN/shared use while recorded LAN-exposure or hardcoded-default risks remain open. Do not weaken authentication or broad-bind services merely for convenience.

## 10. Handoff

Every handoff names the `MOMUS-NNN` item, branch/ref and commit SHA, files changed, reports/evidence created, checks and actual results, skipped checks and reasons, achieved proof ceiling, unresolved blockers/risks, exact ledger state, and one next executable action.

A later agent should be able to continue from repository and report evidence without reconstructing the previous chat.
