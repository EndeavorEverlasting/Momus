# Current State

## MomusStudio repository retirement — active governance

**Canonical target:** `EndeavorEverlasting/Momus`. **Deprecated GitHub repository:** `EndeavorEverlasting/MomusStudio`. Remote routing redirects and obsolete PR closure have been committed; the shared Entire inventory `RETIRED_ALIAS` exception is merged. As of the last direct provider read on 2026-10-17, **GitHub archival is still pending**; no archive-capable GitHub admin action is available through the current connection. Do not use the duplicate for new issues, source code, PRs or agent ownership. See `docs/evidence/2026-10-17-momusstudio-deprecation.md` for exact evidence, scope and the one remaining archive-admin action. Historical `MomusStudiofree` / waoowaoo local source remains `REFERENCE_ONLY_UNMAPPED`.

## Creator identity correction (2026-10-17) — authoritative for product routing

The creator confirms **Momus and MomusStudio were alternate names for the same intended product; Momus is the chosen name**. The prior context-owner/implementation-owner mapping was an engineering assumption and is **SUPERSEDED for product governance**. `AGENTS.md` is the normative contract; `harness/context-workspace-adoption.v1.json` retains the older mapping only as historical evidence. Different physical Git repositories or historic checkout commits may still exist and their exact Git relationships remain UNVERIFIED, but that does not create distinct products. Do not route new implementation to a separate app on the basis of its older name. The current harness sprint does not authorize product-code or runtime changes.


**State ID:** `MOMUS-2026-09-29-LOCAL-CREATOR-BASELINE`  
**Status:** `READY_FOR_LOCAL_CREATION_BASELINE`  
**Primary lane:** immediate AI-content creation / Patrick pilot  
**Canonical plan:** `docs/AI_ENGINEERING_LEDGER.md`  
**Active sprint:** **P06 — Local Creator Baseline and First Creative Package** — GitHub issue **#10**

## What is proven

- `EndeavorEverlasting/Momus` exists and the coordination harness is merged on `main`.
- Momus is the canonical creative-content/context management layer for this program; it does not own the local image/video inference engine.
- Public reference repositories were inspected for an immediate local creator baseline.
- The preferred external baseline is `SwarmUI -> ComfyUI -> local model`.
- Reference floors observed on 2026-09-29 are recorded in `docs/evidence/2026-09-29-local-creator-baseline.md`.
- The first runtime-agnostic creative package exists at `creative/ai-intern/shot-001.json`.
- The historical `MomusStudiofree` / waoowaoo carryover remains preserved as **reference-only** evidence with status `REFERENCE_ONLY_UNMAPPED`; its unresolved provenance does not block the independent P06 local-creator lane.
- The original context-workspace ownership split is a historical adoption record, now superseded as product routing by the creator identity correction above. Momus is the unified product; no local product/runtime implementation is proven by this correction.

## What is not yet proven

- SwarmUI is installed on Patrick's local machine.
- ComfyUI is installed/reachable underneath the selected creator flow.
- Hardware/VRAM compatibility for the selected local model set.
- A local image generation from the first creative package.
- A local video generation from the first creative package.
- The exact workflow/model/seed/output-path provenance for a successful generation.
- Successful export and reproducibility.
- The exact Git relationship among the historical `MomusStudiofree` checkout, public `waooAI/waoowaoo`, and Git references once named `MomusStudio`; product identity itself is creator-confirmed.

## Current decision

Proceed with the smallest proven external creator stack instead of inventing a new inference architecture inside Momus.

Momus owns the creative package and returned generation provenance. The local creator stack owns inference execution. Generated binaries and model weights stay outside this repository.

The historical P01 carryover lane remains available for provenance recovery, but it is no longer a blocker for creating new AI content through the independent P06 baseline.

## Next action

On Patrick's local machine:

1. establish a local SwarmUI checkout;
2. confirm the creator UI launches;
3. confirm ComfyUI/local backend availability;
4. load or map `creative/ai-intern/shot-001.json` into a supported video workflow;
5. generate exactly one representative shot;
6. record runtime/workflow/model/seed/output-path/audio evidence back into Momus without committing the generated binary.

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

## Parallel Storage Work — 2026-10-17 (does not supersede P06)

**Evidence state:** external standalone `MomusMediaBridge` local prototype: IMPLEMENTED and locally VALIDATED (23 focused tests, 8 real HTTP cert checks). Local Git commit `269b1ee417546c7d94cee56f05a54f654d0223df` exists only in the downloadable standalone artifact; it has NOT been pushed to GitHub. A local browser was unable to open loopback due sandbox policy, but a Chromium rendering of its actual HTML was inspected offline.

**Additional proven invariant:** reused S3 provider IDs cannot silently change bucket/endpoint/region; negative cases reject this configuration. The HTTP cert preserves a fingerprint of implementation/launcher inputs.\n\n**Unproven:** installation and functionality on the operator's Linux Mint PC; live Backblaze B2/R2/MinIO credentials, durability, cloud upload/retrieval, actual automatic backups, and interoperability with the unverified historical local MomusStudiofree/waoowaoo runtime. Cloud storage account creation and any spending were deliberately avoided. System interpreter local cert was proven; fresh-venv dependency download was blocked by sandbox network restrictions.

**Historic implementation boundary:** The prior split between the Momus and MomusStudio names was superseded as a product distinction by the creator's 2026-10-17 decision. Any old checkout still requires Git provenance checks before import or mutation; the current harness sprint does not add product code. See `docs/AI_ENGINEERING_LEDGER.md` (Media Storage Boundary) and `docs/SPRINTS.md` (P07) for acceptance and dependency-order continuation. P06 remains active and unchanged.

## Creator UX pre-live-cert gate — 2026-10-17

**Scope:** P08, a parallel creator-interface acceptance lane that does not supersede active P06 or imply that MomusStudio is a second product. **Status:** UX strategy and structural readiness-gate code tracked in the P08 Git branch; the live creative interface itself is **NOT CERTIFIED**.

**Observed repository limitation:** at the 2026-10-17 main evidence floor `b6149a50b999f490c4d5b9ba5c6da63ed54990f5`, no runnable first-party Momus UI source, browser-launch target, or current machine installation was present in the accessible repository. The separately named historic local source and localhost route remain unverified.

**Canonical acceptance:** `docs/UX_READINESS.md`, `harness/ux-readiness.v1.json`, `python scripts/validate_ux_readiness.py --self-test`. Only actual browser/device checks with exact candidate and generated-shot/export proof can promote live UX readiness. The structural validator explicitly prints `NOT CERTIFIED` without receipts; even passing receipt syntax requires independent inspection of screenshots, browser traces and device observations.

**Next gate:** local implementation owner first resolves the exact known-good app checkout with `git status --short && git remote -v && git branch --show-current && git rev-parse HEAD`, without resetting or cloning over existing work; then launch the verified local app and execute the one-shot creator journey with real browser instrumentation. No credentials, model weights, media binaries or private logs should be added to Git.
