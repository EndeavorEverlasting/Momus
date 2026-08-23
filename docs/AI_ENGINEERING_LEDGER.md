# AI Engineering Ledger

**Repository:** `EndeavorEverlasting/Momus`  
**Canonical execution ledger since:** 2026-08-23  
**Origin:** Google Doc titled *AI Engineering Ledger*  
**Current theme:** AI video engineering, carryover recovery, and guided prompt engineering with Pat

## Overview

Momus is a durable execution ledger and engineering workspace for creative AI projects. Its job is to prevent ideas, experiments, prompts, and partially completed local work from disappearing into individual chats or tool sessions. Work enters Momus as evidence-backed ledger items, is executed in bounded sprints, and leaves artifacts that a later agent can inspect and continue.

The initial program is AI video generation. Two source notes define the starting direction:

- **AI Videos with Pat:** use the existing AI production / AI video-generation repository to help Pat begin learning prompt engineering through real creative work.
- **AI Video Carryover:** preserve and continue work previously performed under `MomusStudiofree` via OpenCode.

During bootstrap on 2026-08-23, connected GitHub and Google Drive searches did not locate a repository or file named `MomusStudiofree` beyond the source ledger note, and did not identify a clearly named AI video-generation repository. Those are explicit recovery and dependency-resolution tasks below; no agent should fabricate the missing source or create a competing stack simply to remove the blocker.

## Goals

1. **Preserve continuity.** Recover prior AI-video work, tool context, prompts, configuration, and decisions before replacing or redesigning them.
2. **Make creative work sprintable.** Every active idea has a stable ID, evidence, scope, acceptance criteria, dependencies, and one next action.
3. **Teach through production.** Give Pat a guided route into prompt engineering by producing a real AI-video artifact using the correct existing generation system.
4. **Build reusable practice.** Convert successful experiments into repeatable prompt, generation, review, and evidence workflows.
5. **Keep authority clear.** The repository ledger owns executable project state; human notebook content is reconciled into it rather than becoming a second operational truth.

## Specifications

### Source of truth

`docs/AI_ENGINEERING_LEDGER.md` owns current work-item state. `docs/EXECUTION_PLAN.md` owns phase sequencing. `harness/manifest.v1.json` provides machine-readable entrypoints and dependency state. The originating Google Doc remains useful as a human notebook but does not override newer repository evidence.

### Work-item states

- `ready` — evidence and dependencies are sufficient for an agent to start.
- `in_progress` — a branch/sprint is actively producing the acceptance evidence.
- `blocked` — a named dependency prevents responsible execution; the item must identify the evidence-producing unblock action.
- `done` — acceptance criteria have been met and evidence is recorded.

### Carryover policy

Recover before rebuilding. A local/OpenCode artifact that is known to exist but is not currently connected is treated as missing evidence, not as permission to reconstruct it from memory.

### Dependency policy

Reuse before duplicating. The AI video-generation repository referenced by the source note must be identified and inspected before a new generation stack is introduced.

### Artifact policy

Large generated video binaries are not committed by default. Preserve prompts, configurations, commands, model/provider metadata when safe, checksums, small reference assets, and durable storage references so results can be reproduced without bloating the repository.

### Proof policy

Repository validation proves ledger/harness consistency only. Successful video generation, provider access, local OpenCode recovery, or runtime compatibility require separate execution evidence.

## Work Ledger

### MOMUS-001 — Bootstrap repository execution layer

**State:** `in_progress`  
**Priority:** P0  
**Objective:** Convert the empty repository and template Drive ledger into a durable, agent-runnable project surface.  
**Evidence/current truth:** `main` began with only a minimal README. The source Google Doc contained real milestone notes but template copy in Overview, Goals, and Specifications.  
**Owned scope:** repository governance, canonical ledger, execution plan, manifest, workflows, validator, CI, source-ledger cleanup.  
**Dependencies:** none.  
**Acceptance criteria:** required harness files are tracked; canonical ledger contains no template filler; validator passes; CI result is recorded; bootstrap changes are merged to `main`; Google Doc no longer contains its template filler.  
**Next action:** run repository validation and CI on the bootstrap branch, reconcile the Google Doc, then mark this item `done` before final integration.

### MOMUS-002 — Recover MomusStudiofree and OpenCode carryover

**State:** `ready`  
**Priority:** P0  
**Objective:** Locate and inventory the prior `MomusStudiofree` work before any replacement implementation.  
**Evidence/current truth:** the source ledger explicitly says work was conducted with `MomusStudiofree` via OpenCode. Connected GitHub and Drive searches did not locate that project as a repository/file during bootstrap.  
**Owned scope:** local workspace discovery, OpenCode session/state discovery, source/config/prompt inventory, runnable-state assessment, import/reference recommendation.  
**Forbidden scope:** recreating missing product code from memory; destructive cleanup of recovered work.  
**Dependencies:** access to the machine or storage where the OpenCode work was performed.  
**Acceptance criteria:** `reports/carryover-inventory.md` records exact recovered paths/sources, important files, commands, current runnable state, relevant assets, provenance, and a preserve/import/reference/retire decision for each material component.  
**Next action:** on the workstation where the work was performed, search known development roots and OpenCode state for the exact string `MomusStudiofree`, then write the inventory report from recovered evidence.

### MOMUS-003 — Resolve the canonical AI video-generation dependency

**State:** `ready`  
**Priority:** P0  
**Objective:** Identify the existing AI production / AI video-generation repository the Pat milestone is intended to use.  
**Evidence/current truth:** the source ledger requires reuse of an existing video-generation repository, but connected repository search did not reveal an obvious match by project name or description.  
**Owned scope:** repository/local-remote discovery, entrypoint inspection, runtime requirements, integration boundary, dependency registration.  
**Forbidden scope:** creating a new competing generation repository before discovery is exhausted and evidence justifies it.  
**Dependencies:** access to local repositories/remotes or additional project notes if the dependency is not hosted in the connected GitHub account.  
**Acceptance criteria:** `reports/video-repo-resolution.md` names the exact repository/path/ref, identifies usable generation entrypoints and prerequisites, records why it is the intended dependency, and updates `harness/manifest.v1.json` from unresolved to resolved.  
**Next action:** inspect local development roots, git remotes, and project notes for the existing AI video-generation system, then record the first evidence-backed match instead of guessing from repository names.

### MOMUS-004 — Run Pat's first guided prompt-to-video sprint

**State:** `blocked`  
**Priority:** P1  
**Objective:** Help Pat learn prompt engineering by taking one creative concept through prompt drafting, generation, review, and revision in the existing AI-video system.  
**Evidence/current truth:** the source ledger explicitly names Pat and states the intent to get him started with prompt engineering through the AI production/video-generation repository.  
**Owned scope:** one bounded creative concept, prompt iterations, generation invocation, result review, learning notes, reproducibility metadata.  
**Dependencies:** MOMUS-003 must identify the generation system; required runtime/provider access must be available.  
**Acceptance criteria:** Pat contributes to the prompt; at least one generation is actually executed; the final prompt and material revisions are recorded; generation command/config metadata is captured safely; the result is referenced without unnecessary media bloat; a short retrospective explains what prompt changes mattered.  
**Next action:** after MOMUS-003 is resolved, choose one small creative concept with Pat and execute the repository's proven generation entrypoint end to end.

### MOMUS-005 — Consolidate a repeatable AI-video production workflow

**State:** `blocked`  
**Priority:** P1  
**Objective:** Turn recovered carryover and the first guided sprint into a reusable Momus workflow future agents and collaborators can follow.  
**Evidence/current truth:** a reusable workflow should be derived from recovered and exercised behavior, not invented before those inputs exist.  
**Owned scope:** prompt lifecycle, generation invocation, artifact metadata, review loop, evidence capture, handoff instructions, focused validation.  
**Dependencies:** MOMUS-002 and MOMUS-004.  
**Acceptance criteria:** `harness/WORKFLOWS.md` contains the proven production path; required reusable scripts/config references are registered in the manifest; one fresh run follows the documented path without relying on hidden chat context.  
**Next action:** once carryover is inventoried and Pat's first sprint has execution evidence, compare both paths and codify only the steps that were actually proven.

## Current sprint order

1. Finish MOMUS-001 and merge the repository bootstrap.
2. Run MOMUS-002 and MOMUS-003 in parallel only if separate agents have separate owned scopes and source access.
3. Start MOMUS-004 when MOMUS-003 is resolved.
4. Start MOMUS-005 only after both carryover and a real guided generation have evidence.

## Ledger maintenance rule

When new work appears, update an existing item when it is the same responsibility. Create a new `MOMUS-NNN` item only when it has a distinct objective, owner boundary, or acceptance proof. Never leave an actionable item without a concrete next action.
