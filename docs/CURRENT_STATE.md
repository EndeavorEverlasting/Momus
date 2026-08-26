# Current State

**State ID:** `MOMUS-2026-08-25-CONTEXT-WORKSPACE-ADOPTION`
**Status:** `READY_FOR_P01_BROWSER_PROOF`  
**Primary lane:** AI-video carryover / Patrick pilot  
**Canonical plan:** `docs/AI_ENGINEERING_LEDGER.md`  
**Bootstrap merge:** PR #1 -> `158b3876aff0bd577941eb2656de7b40fdd5ce7e`

## What is proven

- `EndeavorEverlasting/Momus` exists and the ledger/harness bootstrap is merged to `main`.
- The human AI Engineering Ledger exists in Google Drive and records two initial milestones: Patrick's AI-video prompt-engineering plan and MomusStudiofree/OpenCode carryover.
- The Google Drive ledger's template placeholders have been replaced with project-specific Overview, Goals, Specifications, Operating Model, and milestone content.
- Embedded source evidence shows a local waoowaoo sign-in flow at `http://localhost:13000` using the test username `sprint1-test`.
- Embedded OpenCode evidence records **BLOCKERS: None** at the captured handoff.
- The same evidence records the minimum model-chain target, the representative project title, 9:16 format, one-shot-before-batching rule, and explicit audio verification.
- Public GitHub evidence identifies `waooAI/waoowaoo` as a useful waoowaoo source reference whose README independently documents the Docker `localhost:13000` path and Settings-based API configuration. See `docs/evidence/2026-08-23-waoowaoo-public-source.md`.
- `EndeavorEverlasting/MomusStudio` exists as a separate GitHub repository. Momus now designates it as the **implementation authority for new canonical Momus product/content implementation work**, while this repository remains the **context authority** for project intent, sprint definitions, coordination, evidence requirements, and project lessons. The adoption contract is `harness/context-workspace-adoption.v1.json`.
- The Momus adoption pins AgentSwitchboard's portable `agentswitchboard.context-workspace-boundary.v1` contract at donor commit `dab223c4039e5599ae99034fbcce86996c5983a3`; this proves the static authority mapping only, not MomusStudio product/runtime completeness.
- Repository bootstrap validation passed before merge: `PASS: Momus harness validation (7 required artifacts, 6 sprint IDs)` and `python -m py_compile scripts/validate_repo.py` passed.

## What is not yet proven

- Three green API/provider connection checks.
- Successful representative-shot generation.
- Successful export.
- Reproducibility from a documented clean-enough starting point.
- Closure of LAN exposure / hardcoded-default risks.
- Presence of the historical MomusStudiofree implementation source inside this GitHub repository.
- The exact git relationship among the local `MomusStudiofree` / waoowaoo carryover, the public `waooAI/waoowaoo` source reference, and `EndeavorEverlasting/MomusStudio`. Local filesystem path, remotes, branch/ref, HEAD SHA, and dirty/untracked state must be captured before importing, upgrading, or treating the historical carryover as MomusStudio history.
- That the current MomusStudio repository already contains or reproduces the previously observed local waoowaoo runtime. Its existence and authority role do not prove implementation or runtime equivalence.

## Current decision

Treat Momus as the canonical coordination/context repository and `EndeavorEverlasting/MomusStudio` as the implementation authority for **new canonical implementation work**. Implementation-derived evidence from MomusStudio outranks authored Momus status for implementation claims. Preserve the older `MomusStudiofree` / local waoowaoo carryover as **reference-only evidence** until its Git provenance and relationship to MomusStudio are established; do not infer equivalence from naming or timestamps. Continue using the public waoowaoo repository as reference evidence only unless a later adoption/import decision explicitly changes that relationship.

## Next sprint

**P01 — Recover Carryover and Complete Browser Proof** — GitHub issue **#2**. The new-work repository boundary is resolved, but P01 still owns historical carryover/browser proof and the provenance gate needed before historical source import or upgrade work.

## Handoff fields to update after every sprint

- timestamp
- operator/agent
- repo + branch + commit
- sprint ID / issue
- files changed
- commands/tests run
- artifacts/screenshots/logs produced
- acceptance checks passed/failed
- blockers
- risks discovered or closed
- exact next action
