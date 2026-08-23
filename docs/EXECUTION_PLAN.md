# Momus Execution Plan

## Mission

Convert the two seed ideas in the original AI Engineering Ledger into a recoverable AI-video program that can be continued by agents without hidden chat context: preserve `MomusStudiofree`, bind the correct existing video-generation system, teach Pat prompt engineering through a real generation sprint, and then codify the proven workflow.

## Phase 0 — Repository bootstrap

**Ledger item:** MOMUS-001  
**Outcome:** a fresh agent can enter Momus, understand current truth, select the next safe work item, run validation, and hand off with evidence.

Required proof:

- canonical ledger exists and contains executable work items;
- agent contract, codebase map, workflow, manifest, validator, and CI are tracked;
- the source Google Doc no longer contains template filler;
- repository validation passes;
- bootstrap is integrated to `main`.

## Phase 1A — Carryover recovery

**Ledger item:** MOMUS-002  
**Goal:** recover before rewriting.

Execution sequence:

1. Inspect known development roots on the machine where OpenCode was used.
2. Search for the exact project/session name `MomusStudiofree`.
3. Inspect recovered git state, source tree, prompts, configs, scripts, media references, and OpenCode/session artifacts.
4. Determine the last known runnable command or workflow from evidence.
5. Record a component inventory in `reports/carryover-inventory.md`.
6. Classify each material component as preserve, import into Momus, reference externally, or retire with reason.
7. Run only non-destructive checks until the recovered state is understood.

Proof gate: no replacement implementation starts until the inventory names the recovered source or records a documented exhaustive search and the evidence ceiling reached.

## Phase 1B — Video-system dependency resolution

**Ledger item:** MOMUS-003  
**Goal:** reuse the intended AI video-generation system instead of creating a parallel stack.

Execution sequence:

1. Inspect local repository roots, git remotes, and project notes for the existing AI production/video-generation repository.
2. Compare candidate repositories by actual generation entrypoints, prompts/configs, provider/model integration, and history rather than by name alone.
3. Record the evidence-backed match in `reports/video-repo-resolution.md`.
4. Record its exact path or repository URL, ref, prerequisites, and reusable entrypoints.
5. Update `harness/manifest.v1.json` so the dependency state is `resolved` and agents no longer need to rediscover it.
6. Exercise the smallest safe diagnostic or generation-adjacent command that proves the integration boundary without spending unnecessary provider credits.

Proof gate: MOMUS-004 remains blocked until the dependency is named and its intended entrypoint is evidenced.

## Phase 2 — Pat guided prompt-engineering sprint

**Ledger item:** MOMUS-004  
**Goal:** teach prompt engineering through production rather than abstract instruction.

Execution sequence:

1. Pick one bounded creative concept with Pat.
2. Capture Pat's initial intent in his own words.
3. Turn that intent into a first structured generation prompt while explaining the transformation.
4. Execute the proven generation entrypoint from the resolved video system.
5. Review the result together and identify concrete prompt-to-output relationships.
6. Revise the prompt deliberately and run another generation when useful and affordable.
7. Save the prompt lineage, safe generation metadata, result reference, and short learning retrospective in `reports/pat-first-video-sprint.md`.

Proof gate: the milestone is complete only after an actual generation is run and the report shows what Pat changed or learned from the prompt/output loop.

## Phase 3 — Workflow consolidation

**Ledger item:** MOMUS-005  
**Goal:** make the successful path reusable by a new agent or collaborator.

Execution sequence:

1. Compare the recovered `MomusStudiofree` path with the exercised Pat sprint.
2. Keep steps supported by evidence; reject obsolete, duplicated, or accidental workflow details.
3. Update `harness/WORKFLOWS.md` with the proven prompt → generate → review → revise → evidence path.
4. Register reusable scripts/configs/entrypoints in `harness/manifest.v1.json`.
5. Add focused validation for any new machine-readable contracts.
6. Run one clean reproduction from repository instructions without relying on previous chat/session context.

Proof gate: a fresh operator can follow the documented workflow and produce the expected evidence artifacts.

## Parallelism

MOMUS-002 and MOMUS-003 may run in parallel because one owns local/OpenCode carryover recovery and the other owns dependency discovery. They must use separate branches/worktrees and may not rewrite each other's reports or manifest fields without a handoff.

MOMUS-004 is downstream of MOMUS-003. MOMUS-005 is downstream of MOMUS-002 and MOMUS-004.

## Boundaries

Do not:

- recreate `MomusStudiofree` from memory before recovery is exhausted;
- create a new AI video-generation repository before the intended dependency is resolved;
- commit credentials or provider secrets;
- commit large generated videos by default;
- claim a provider/runtime/generation path is working without execution evidence;
- let Google Doc notes silently override newer repository ledger state.

## Definition of program success

Momus reaches its first stable program state when:

- prior AI-video work is recovered or its recovery ceiling is documented;
- the canonical generation dependency is registered;
- Pat completes a real guided prompt-to-video cycle;
- a new agent can reproduce the workflow from repository instructions and evidence alone.
