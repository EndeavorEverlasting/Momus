# Momus Workflows

## 1. Pick up a task

1. Read `AGENTS.md`, then `docs/AI_ENGINEERING_LEDGER.md`.
2. Refresh repository/branch/PR truth and inspect any existing report for the target work item.
3. Prefer an `in_progress` item already owned by the branch; otherwise choose the earliest `ready` item whose dependencies are satisfied.
4. State repo, branch, lane, mission, owned scope, forbidden scope, expected artifacts, validation command, and proof ceiling before the first write.
5. Create a separate branch/worktree when another agent owns overlapping work.

## 2. Evidence review

Before implementation, search existing repository and external/local evidence relevant to the item. Momus has two especially important search rules:

- MOMUS-002: search for the exact prior `MomusStudiofree` / OpenCode work before creating replacement code.
- MOMUS-003: search for the intended existing AI video-generation repository before creating a new generation stack.

When evidence is absent, document the search ceiling and next evidence-producing action. Do not replace missing facts with plausible guesses.

## 3. Execute a bounded sprint

For the selected ledger item:

1. Re-read its objective, scope, dependencies, acceptance criteria, and next action.
2. Produce only artifacts that advance those criteria.
3. Update the same ledger item when state/evidence changes; do not create a competing task tracker.
4. Put durable proof in `reports/` when the acceptance criteria call for an inventory, resolution record, or experiment result.
5. Keep large generated media outside git by default; record safe metadata and references instead.

## 4. Validate before commit

Run:

```bash
python scripts/validate_repo.py
```

Any nonzero result blocks a clean completion claim. Fix the owning source rather than weakening the validator to hide a real failure.

For future product/runtime work, run the generation system's own focused checks in addition to the Momus validator. Register canonical commands in `harness/manifest.v1.json` only after they are proven.

## 5. Handle failures

### Missing carryover

If `MomusStudiofree` cannot be found in the first known development root, broaden the search deliberately to other known roots and OpenCode state. Record locations searched and evidence. Do not immediately recreate the project.

### Ambiguous video repository

If multiple candidates could be the intended generation system, compare actual entrypoints, history, configs, and source-note alignment. Record the comparison in `reports/video-repo-resolution.md`. Do not choose by repository name alone.

### Runtime/provider failure

Separate repository correctness from external/runtime failure. Capture the exact command, safe error output, environment assumptions, and proof ceiling. Never expose credentials in a report.

### Validator failure

Treat the failing message as the contract owner. Repair the ledger/manifest/path first. If the validator itself is wrong, change it only with a specific regression case demonstrating the false failure.

## 6. Handoff

A handoff must include:

- selected `MOMUS-NNN` item;
- branch/ref and latest commit SHA;
- files changed;
- artifacts/reports created;
- validation commands and results;
- skipped checks and reasons;
- unresolved blockers/risks;
- exact ledger state after the sprint;
- one next executable action.

The next agent should be able to continue from repository state without recovering the previous chat.

## 7. Work-item-specific flows

### MOMUS-002 — Carryover recovery

**Output:** `reports/carryover-inventory.md`

The report must name recovered paths/sources, git state when present, important source/config/prompt files, relevant OpenCode/session evidence, last known runnable commands inferred from evidence, asset locations, and preserve/import/reference/retire decisions.

### MOMUS-003 — Video dependency resolution

**Output:** `reports/video-repo-resolution.md`

The report must name the exact repository/path/ref, show evidence tying it to the intended AI-video workflow, identify the generation entrypoint and prerequisites, and drive a manifest update from unresolved to resolved.

### MOMUS-004 — Pat guided sprint

**Output:** `reports/pat-first-video-sprint.md`

Capture the concept, initial intent, prompt lineage, safe generation metadata, command/entrypoint used, result reference, review observations, and the prompt-engineering lesson drawn from the output. Do not store provider secrets or unnecessary video binaries.

### MOMUS-005 — Workflow consolidation

Update this file only from recovered/exercised evidence. The final production workflow should be a concrete prompt → generate → review → revise → evidence loop with canonical entrypoints registered in the manifest.
