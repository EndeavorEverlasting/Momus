# Momus Agent Contract

## Mission

Convert the AI Engineering Ledger into small, evidence-backed sprints that advance the Patrick AI-video pilot and preserve the existing MomusStudiofree carryover without inventing missing product state.

## Evidence order

Before action, inspect these in order:

1. `docs/AI_ENGINEERING_LEDGER.md`
2. `docs/CURRENT_STATE.md`
3. `docs/SPRINTS.md`
4. relevant files under `docs/evidence/`
5. current Git/GitHub branch, commits, issues, PRs, and CI state

If repository evidence conflicts with remembered chat context, prefer current repository/provider evidence and record the discrepancy.

## Scope discipline

Every sprint must name:

- repo
- branch
- sprint ID and title
- lane
- owned scope
- forbidden scope
- expected artifacts
- acceptance checks

Do not broaden a sprint because adjacent work is interesting.

## Security boundaries

- Never commit passwords, API keys, tokens, `.env` values, or provider credentials.
- The carryover evidence explicitly says provider keys are entered in the UI only.
- The local runtime was observed with published ports bound to `0.0.0.0`; do not treat it as safe for shared/network use until the hardening sprint closes that risk.
- The carryover evidence also records hardcoded Compose defaults (`DB password`, `NEXTAUTH_SECRET`, `API_ENCRYPTION_KEY`). Names may be documented; values must not be committed.

## Execution loop

1. **Recover truth:** read the ledger, current state, sprint registry, evidence, and current GitHub state.
2. **Select one sprint:** do not execute multiple lanes implicitly.
3. **Act within scope:** make the smallest changes needed to satisfy acceptance.
4. **Capture proof:** screenshots, logs, validator output, changed files, commit SHA, and PR/merge status as applicable.
5. **Update state:** revise `docs/CURRENT_STATE.md` and the sprint entry when evidence changes.
6. **Validate:** run `python scripts/validate_repo.py` for repository-document changes plus any product-specific checks in the implementation repository.
7. **Hand off:** state completed work, proof, gaps/risks, important paths, Git state, and the next command/action.

## Proof rules

A claim is not complete because an agent says it is complete. Prefer, in order:

- observed browser/UI behavior
- generated/exported artifact
- repeatable second run
- test/validator output
- logs
- Git diff/status and commit SHA
- PR/merge/CI evidence

For the video workflow, generation/export and reproducibility are separate proof ceilings.

## Implementation-repository boundary

The source ledger refers to `MomusStudiofree` and a local waoowaoo application, but the current `EndeavorEverlasting/Momus` repository began as a documentation-only repository. Do not claim product-code changes in Momus unless that code is actually added here. If work occurs in another repository or local checkout, record its exact path/repository and commit evidence in `docs/CURRENT_STATE.md`.
