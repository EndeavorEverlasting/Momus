# AI Engineering Ledger

**Repository:** `EndeavorEverlasting/Momus`  
**Canonical execution ledger since:** 2026-08-23  
**Origin:** Google Doc titled *AI Engineering Ledger*  
**Current program:** MomusStudiofree / waoowaoo carryover, local runtime proof, and hands-on prompt engineering with Patrick

## Overview

Momus is the coordination ledger and engineering harness for AI-assisted video work. It turns prior local/OpenCode carryover and the Patrick prompt-engineering pilot into evidence-backed, agent-executable sprints.

The current plan is no longer abstract. The source ledger identifies:

- prior work under `MomusStudiofree` via OpenCode;
- the local waoowaoo application at `http://localhost:13000` as the first runtime proof target;
- a minimum **text model → image model → video model** configuration chain;
- three provider connection checks that must all be green before generation is claimed;
- a first **9:16** concept named **“The AI Intern Takes Corporate Speak Literally”**;
- one representative shot before batching;
- explicit audio verification;
- generation/export and reproducibility as separate proof ceilings;
- shared/network use deferred until recorded LAN-exposure and hardcoded-default risks are closed.

Public-source inspection also identifies `waooAI/waoowaoo` as the upstream waoowaoo AI Video Studio. Its documentation confirms Docker-based access at port 13000 and API-key configuration through the application Settings UI. The exact git provenance, local changes, and relationship of the `MomusStudiofree` workspace to that upstream remain local evidence to recover rather than assumptions to make.

## Goals

1. **Preserve continuity.** Recover the exact `MomusStudiofree` / OpenCode workspace state before replacement or broad upgrades.
2. **Prove the runtime incrementally.** Separate provider connectivity, generation, export, audio, and reproducibility into distinct evidence gates.
3. **Keep secrets out of Git.** Use the existing local test account and enter provider keys through the UI; record only safe metadata.
4. **Teach through visible output.** Give Patrick a practical prompt-engineering path that generates a real representative shot, critiques what is visible, and revises deliberately.
5. **Make work sprintable.** Every active item has a stable ID, evidence, scope, acceptance criteria, dependencies, and one concrete next action.
6. **Avoid premature network exposure.** Keep the current proof path local until recorded LAN/hardcoded-default risks are explicitly closed.

## Specifications

### Source of truth

`docs/AI_ENGINEERING_LEDGER.md` owns current work-item state. `docs/EXECUTION_PLAN.md` owns phase sequencing and proof gates. `harness/manifest.v1.json` owns machine-readable runtime/dependency registration. The originating Google Doc remains the human notebook but does not override newer repository evidence.

### Work-item states

- `ready` — evidence and dependencies are sufficient for an agent to start.
- `in_progress` — a branch/sprint is actively producing acceptance evidence.
- `blocked` — a named dependency prevents responsible execution; the item names the unblock action.
- `done` — acceptance criteria have evidence.

### Proof gates

Use these proof ceilings in order and do not collapse them:

1. **Source/provenance proof** — exact local workspace, git state, OpenCode context, and upstream relationship are recorded.
2. **Runtime-access proof** — local app opens at `http://localhost:13000` and the existing test account can authenticate.
3. **Provider-connectivity proof** — text, image, and video provider checks are each green.
4. **Generation proof** — one representative 9:16 shot is actually generated.
5. **Audio/export proof** — audio presence/behavior and export are explicitly exercised and recorded.
6. **Reproducibility proof** — a clean rerun from documented repository instructions reaches the expected state without hidden session context.

### Carryover policy

Recover before rebuilding. `MomusStudiofree` is known prior work, not a blank slate.

### Upstream policy

`waooAI/waoowaoo` is the identified public upstream project, but local remote/ref/customization state must be proven before an agent treats the local workspace as a clean clone or upgrades it.

### Security policy

Passwords and provider keys remain outside Git and evidence reports. Current provider configuration is performed through the application UI. No agent may expose secrets merely to make automation easier.

### Artifact policy

Do not commit large generated video binaries by default. Preserve prompts, configurations, safe model/provider metadata, commands, screenshots when evidentiary, checksums, and durable result references.

## Work Ledger

### MOMUS-001 — Bootstrap repository execution layer

**State:** `in_progress`  
**Priority:** P0  
**Objective:** Convert the minimal repository and source notebook into a durable, agent-runnable execution surface that reflects the concrete waoowaoo plan.  
**Evidence/current truth:** `main` began with only a minimal README. The source Google Doc originally contained template filler, but its current revision now contains the local waoowaoo runtime, provider-chain, representative-shot, audio, and proof-ceiling plan.  
**Owned scope:** repository governance, canonical ledger, execution plan, manifest, workflows, validator, CI, source reconciliation.  
**Dependencies:** none.  
**Acceptance criteria:** required harness files are tracked; canonical ledger contains the current concrete plan and no stale template filler; validator passes; CI result is recorded; bootstrap changes are merged to `main`; the Google Doc remains free of source-template filler.  
**Next action:** validate the reconciled bootstrap branch through CI, then mark this item `done` and integrate it to `main`.

### MOMUS-002 — Recover MomusStudiofree / OpenCode provenance

**State:** `ready`  
**Priority:** P0  
**Objective:** Recover the exact local workspace and OpenCode state so no agent rewrites or upgrades the carryover blindly.  
**Evidence/current truth:** the source ledger says prior work was conducted against `MomusStudiofree` via OpenCode and that the local waoowaoo app is the current proof target. Public upstream is identifiable as `waooAI/waoowaoo`, but the local path, remote/ref, dirty state, custom changes, and session context are not present in connected GitHub/Drive evidence.  
**Owned scope:** local path discovery, git remote/branch/HEAD/dirty-state evidence, OpenCode session/context discovery, source/config/prompt inventory, known runtime command/state, provenance classification.  
**Dependencies:** access to the workstation/storage where the work was performed.  
**Acceptance criteria:** `reports/carryover-inventory.md` records exact local path, remote(s), branch/ref/HEAD, dirty/untracked state, important files/configs/prompts, OpenCode/session evidence, last known commands, relevant assets, and a preserve/import/reference/retire recommendation without destroying existing work.  
**Next action:** on the original workstation, locate `MomusStudiofree`, capture `git status`, remote/ref/HEAD and relevant OpenCode evidence, then write the inventory before changing source.

### MOMUS-003 — Prove local waoowaoo access and provider connectivity

**State:** `ready`  
**Priority:** P0  
**Objective:** Reopen the existing local app and prove the minimum text → image → video provider chain without conflating connectivity with generation.  
**Evidence/current truth:** the source ledger identifies `http://localhost:13000`, the existing local test account, API Configuration, and three green connection checks as the next runtime gate. Upstream waoowaoo documentation independently confirms port 13000 for Docker runs and Settings-based API configuration.  
**Owned scope:** local runtime access, authentication with the existing test account, UI provider configuration, safe provider/model metadata, three connection checks, evidence capture.  
**Dependencies:** the existing local runtime/database and valid provider credentials available to the operator; credentials remain outside Git.  
**Acceptance criteria:** `reports/waoowaoo-runtime-proof.md` records that the app opened at the expected local URL, authentication succeeded, the selected text/image/video providers and model names are recorded without keys, and all three connection checks are evidenced green. Generation is explicitly still unproven at this gate.  
**Next action:** reopen `http://localhost:13000`, authenticate, configure the minimum text → image → video chain in the UI with keys entered only there, run all three connection checks, and record the results.

### MOMUS-004 — Generate the first representative 9:16 shot

**State:** `blocked`  
**Priority:** P1  
**Objective:** Move from green provider checks to actual generation with one bounded representative shot before batching.  
**Evidence/current truth:** the captured carryover next action names the concept **“The AI Intern Takes Corporate Speak Literally”**, requires 9:16, and requires one representative shot before batching. Generation/export and reproducibility remain separate proof ceilings.  
**Owned scope:** create the named project/concept, first prompt/story input, 9:16 configuration, one representative generation, visible result review, safe generation metadata and result reference.  
**Dependencies:** MOMUS-003 must prove all three provider checks green.  
**Acceptance criteria:** at least one representative 9:16 shot is actually generated; prompt/input and safe generation metadata are recorded; the result is referenced; generation is distinguished from export; no batch generation is started merely to prove the first shot.  
**Next action:** after MOMUS-003 is green, create **“The AI Intern Takes Corporate Speak Literally”** in 9:16 and run exactly one representative shot through the proven chain.

### MOMUS-005 — Run Patrick's prompt critique loop and close higher proof gates

**State:** `blocked`  
**Priority:** P1  
**Objective:** Use visible AI-video output as Patrick's prompt-engineering practice, then codify the repeatable workflow without overstating audio/export/reproducibility.  
**Evidence/current truth:** the source milestone says Patrick should learn through one visually testable concept, real output, critique, and deliberate iteration instead of prompt theory in isolation. The operating model requires audio, export, reproducibility, and shared/network readiness to be proven separately.  
**Owned scope:** Patrick's prompt/input contribution, critique of the representative output, deliberate prompt revision, follow-up generation when useful, explicit audio/export checks, reproducibility attempt, workflow documentation.  
**Dependencies:** MOMUS-004 generation proof; required provider/runtime access.  
**Acceptance criteria:** `reports/pat-first-video-sprint.md` records Patrick's initial intent/contribution, prompt lineage, visible-output critique, deliberate revision, safe result metadata, explicit audio/export findings, and the achieved reproducibility ceiling; `harness/WORKFLOWS.md` is updated only with steps actually proven. LAN/shared exposure remains blocked unless its recorded risks are separately closed.  
**Next action:** once the representative shot exists, review it with Patrick, identify a concrete prompt-to-output mismatch, revise one prompt dimension deliberately, rerun when useful, and record the evidence before generalizing the workflow.

## Current sprint order

1. Finish MOMUS-001 and integrate the repository bootstrap.
2. Run MOMUS-002 and MOMUS-003 in parallel only with separate owned scopes: provenance recovery versus runtime/provider proof.
3. Start MOMUS-004 only after MOMUS-003 has three green provider checks.
4. Start MOMUS-005 only after an actual representative shot exists.
5. Do not claim shared/LAN readiness until its security and hardcoded-default risks are separately closed.

## Ledger maintenance rule

Update the existing `MOMUS-NNN` owner when new evidence belongs to the same responsibility. Create a new work item only for a genuinely distinct objective, ownership boundary, or proof gate. Never leave actionable work without one concrete next action.
