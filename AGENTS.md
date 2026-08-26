# Momus Agent Contract

## Mission

Convert the AI Engineering Ledger into small, evidence-backed sprints that advance the Patrick AI-video pilot and preserve the existing MomusStudiofree carryover without inventing missing product state.

## Evidence order

Before action, inspect these in order:

1. `docs/AI_ENGINEERING_LEDGER.md`
2. `docs/CURRENT_STATE.md`
3. `docs/SPRINTS.md`
4. `harness/context-workspace-adoption.v1.json` when work crosses the Momus / MomusStudio boundary
5. relevant files under `docs/evidence/`
6. current Git/GitHub branch, commits, issues, PRs, and CI state

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

1. **Recover truth:** read the ledger, current state, sprint registry, evidence, context-workspace adoption when applicable, and current GitHub state.
2. **Select one sprint:** do not execute multiple lanes implicitly.
3. **Act within scope:** make the smallest changes needed to satisfy acceptance.
4. **Capture proof:** screenshots, logs, validator output, changed files, commit SHA, and PR/merge status as applicable.
5. **Update state:** revise `docs/CURRENT_STATE.md` and the sprint entry when evidence changes.
6. **Validate:** run `python scripts/validate_repo.py` and `python scripts/validate_context_workspace.py` for repository-document/boundary changes plus any product-specific checks in the implementation repository.
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

## Context / implementation authority boundary

Momus is the canonical **context authority** for project intent, AI Engineering Ledger normalization, epics/sprint definitions, cross-repository architecture decisions, coordination/evidence requirements, and project lessons. `EndeavorEverlasting/MomusStudio` is the canonical **implementation authority** for new product/content implementation work: source and content assets, tests/build scripts, runtime configuration, and implementation-derived status.

The portable boundary is adopted through `harness/context-workspace-adoption.v1.json`, pinned to AgentSwitchboard's `agentswitchboard.context-workspace-boundary.v1` contract. Do not copy either repository's authoritative material into the other as a competing truth store. Implementation claims require MomusStudio Git/CI/runtime evidence; a Momus plan or authored status cannot prove that implementation exists or works.

The source ledger and earlier evidence also refer to `MomusStudiofree` and a local waoowaoo application. That historical carryover remains **`REFERENCE_ONLY_UNMAPPED`**. Do not infer that it is the same repository/history as `EndeavorEverlasting/MomusStudio` from its name or timestamps. Before importing, upgrading, or mutating that carryover, capture its filesystem path, Git remotes, branch/ref, HEAD SHA, and dirty/untracked state and reconcile the relationship explicitly.

## Implementation-repository boundary

The current `EndeavorEverlasting/Momus` repository remains coordination/context-oriented and does not own MomusStudio product source. Route new canonical implementation changes to `EndeavorEverlasting/MomusStudio` and record exact repository/commit evidence in `docs/CURRENT_STATE.md`. Historical `MomusStudiofree` / waoowaoo evidence remains reference-only until its provenance gate closes.
