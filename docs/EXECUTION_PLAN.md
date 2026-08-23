# Momus Execution Plan

## Mission

Turn the current MomusStudiofree / waoowaoo carryover into a proven local AI-video workflow, then use that real output loop to teach Patrick prompt engineering. Preserve existing work, separate proof gates, keep credentials out of Git, and leave evidence that a later agent can continue without hidden tool-session context.

## Phase 0 — Repository bootstrap

**Ledger item:** MOMUS-001

Required proof:

- canonical ledger and execution plan reflect the current Google Doc plan;
- agent contract, codebase map, workflows, manifest, validator, CI, and report contract are tracked;
- no stale source-template filler remains;
- repository validator and CI pass;
- bootstrap is integrated to `main`.

## Phase 1A — Recover MomusStudiofree / OpenCode provenance

**Ledger item:** MOMUS-002  
**Goal:** know exactly what the local workspace is before changing it.

Execution sequence:

1. On the original workstation, locate the `MomusStudiofree` working directory.
2. Capture git remote(s), branch, HEAD, status, dirty/untracked state, and recent relevant commits without cleaning anything.
3. Inspect OpenCode session/state associated with the carryover.
4. Inventory important prompts, configs, scripts, provider/model selections, runtime commands, and local assets.
5. Compare local provenance with public upstream `waooAI/waoowaoo`; do not assume the local tree is clean or current.
6. Record evidence in `reports/carryover-inventory.md`.
7. Classify material components as preserve, import into Momus, reference upstream/local, or retire with reason.

Proof gate: no source rewrite, upgrade, or destructive cleanup until provenance and dirty-state evidence are recorded.

## Phase 1B — Prove local app and provider connectivity

**Ledger item:** MOMUS-003  
**Goal:** prove the runtime and provider chain without overstating generation.

Execution sequence:

1. Reopen `http://localhost:13000`.
2. Authenticate with the existing local test account.
3. Enter API Configuration / Settings.
4. Configure the minimum **text model → image model → video model** chain.
5. Enter provider keys in the UI only; never record them in Git, reports, screenshots, or prompts.
6. Run the three provider connection checks.
7. Record selected provider/model names, safe runtime details, and the three check results in `reports/waoowaoo-runtime-proof.md`.
8. Stop the proof claim at connectivity even if the UI looks otherwise healthy.

Proof gate: all three checks are green. Generation remains unproven.

## Phase 2 — Generate one representative 9:16 shot

**Ledger item:** MOMUS-004  
**Goal:** cross from connection proof to actual video-generation proof with the smallest useful artifact.

Execution sequence:

1. Create the concept **“The AI Intern Takes Corporate Speak Literally”**.
2. Configure the project/output for **9:16**.
3. Use one representative prompt/story input that is visually easy to judge.
4. Generate **one representative shot**.
5. Record prompt/input lineage, safe generation metadata, result reference, and visible outcome.
6. Do not batch merely to establish the first generation proof.
7. Record export state separately; a visible/generated shot is not automatically an export proof.

Proof gate: one representative shot is actually generated and evidenced.

## Phase 3 — Patrick prompt-engineering critique loop

**Ledger item:** MOMUS-005  
**Goal:** teach prompt engineering by connecting a deliberate prompt change to a visible output change.

Execution sequence:

1. Review the representative shot with Patrick.
2. Capture Patrick's own initial reaction and intent.
3. Identify one concrete mismatch between desired and visible output.
4. Explain which prompt dimension is likely responsible: subject, action, environment, composition, camera, style, pacing, continuity, or another evidenced control.
5. Revise that dimension deliberately rather than rewriting everything at once.
6. Run a follow-up generation when useful and provider cost/runtime allows.
7. Record prompt lineage, visible differences, and the lesson learned in `reports/pat-first-video-sprint.md`.
8. Exercise audio and export explicitly and record the result separately.
9. Attempt a clean rerun from documented instructions to establish the reproducibility ceiling.
10. Update `harness/WORKFLOWS.md` only with steps actually proven.

Proof gates:

- Patrick prompt/output critique proof;
- audio proof;
- export proof;
- reproducibility proof.

Each gate may pass or remain open independently.

## Network/shared-use boundary

The current program is local-first. Do not expose the waoowaoo service to LAN/shared use until the recorded hardcoded-default and LAN-exposure risks are closed with explicit evidence. Do not weaken authentication or bind more broadly merely to simplify access.

## Parallelism

MOMUS-002 and MOMUS-003 may run in parallel because provenance recovery and local runtime/provider proof have distinct owned scopes. Use separate branches/worktrees and evidence artifacts.

MOMUS-004 is downstream of MOMUS-003. MOMUS-005 is downstream of MOMUS-004.

## Program success

The first stable Momus AI-video program state exists when:

- `MomusStudiofree` provenance and OpenCode carryover are recovered;
- the local waoowaoo app and three-provider chain are evidenced;
- one representative 9:16 shot is generated;
- Patrick completes a visible prompt critique/revision loop;
- audio/export/reproducibility proof ceilings are explicitly recorded;
- a new agent can follow repository instructions to the achieved proof ceiling without relying on prior chat context.
