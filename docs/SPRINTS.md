# Sprint Registry

Each sprint is intentionally small enough that a fresh agent can execute it without silently absorbing adjacent work.

## P00 — Ledger and Agent Harness Bootstrap

**Lane:** repository coordination  
**Owned scope:** replace template placeholders with canonical plan content; establish agent entrypoints, current state, sprint registry, evidence record, manifest, and validator.  
**Forbidden scope:** product-code changes, provider credentials, destructive cleanup, claims that MomusStudiofree source is in this repository.  
**Expected artifacts:** `AGENTS.md`, ledger, current state, sprint registry, evidence note, manifest, validator, updated README.  
**Acceptance:** validator passes; no placeholder template text remains in tracked coordination files; branch/PR/merge evidence recorded.  
**Status:** complete — PR #1 merged to `main` as `158b3876aff0bd577941eb2656de7b40fdd5ce7e`; local validator and Python compile checks passed before merge.

## P01 — Recover Carryover and Complete Browser Proof

**GitHub issue:** #2  
**Lane:** local browser/runtime proof + historical carryover provenance  
**Owned scope:** capture the local `MomusStudiofree` checkout's filesystem path, Git remotes, branch/ref, HEAD SHA, and dirty/untracked state; determine its relationship to `EndeavorEverlasting/MomusStudio` and `waooAI/waoowaoo`; verify the recorded local application is reachable; authenticate using the existing local test account; open API Configuration; configure the minimum text/image/video chain; capture three green connection checks.  
**Forbidden scope:** committing credentials, network exposure, destructive Git reconciliation, silently importing historical source into `EndeavorEverlasting/MomusStudio`, security-hardening changes, bulk generation, unrelated UI work.  
**Expected artifacts:** provenance receipt for the historical checkout; explicit relationship disposition (`same history`, `fork/ancestor`, `separate`, or `UNKNOWN`); timestamped screenshots or logs showing reachability, authenticated state, API Configuration, and three successful connection checks; current-state update.  
**Acceptance:** historical carryover provenance is captured without mutation; all three provider/model connections are visibly healthy; no secret value appears in committed artifacts. The existence of `EndeavorEverlasting/MomusStudio` does not satisfy the historical provenance gate by itself.  
**Status:** ready — `EndeavorEverlasting/MomusStudio` is now the implementation authority for new canonical work, but the older `MomusStudiofree` / waoowaoo carryover remains reference-only until provenance is proven.

## P02 — Representative Shot and Generation/Export Proof

**GitHub issue:** #3  
**Lane:** AI-video generation  
**Owned scope:** create **“The AI Intern Takes Corporate Speak Literally”** in **9:16**, generate exactly one representative shot before batching, verify audio presence, then prove generation/export. New canonical implementation/source changes belong in `EndeavorEverlasting/MomusStudio`; Momus records intent, acceptance, and evidence pointers.  
**Forbidden scope:** batch production before the one-shot gate, unrelated creative variants, shared-network deployment, duplicating MomusStudio implementation into Momus.  
**Expected artifacts:** final prompt/settings summary with secrets removed, screenshot of representative shot, audio verification note, exported artifact reference, generation/export log, exact MomusStudio commit when implementation changes are required.  
**Acceptance:** one representative shot is generated and an export artifact is proven.  
**Status:** blocked on P01.

## P03 — Reproducibility Seal

**GitHub issue:** #4  
**Lane:** repeatability  
**Owned scope:** reproduce the successful P02 flow from documented prerequisites and capture exact steps, expected timings, recoverable failures, and outputs.  
**Forbidden scope:** architectural rewrite, security redesign, feature expansion.  
**Expected artifacts:** reproducibility runbook, second-run evidence, failure/retry notes, current-state update, exact implementation-repository commit references where applicable.  
**Acceptance:** another agent/operator can reproduce the same class of output without relying on unstated memory.  
**Status:** blocked on P02.

## P04 — Shared-Use Security Hardening

**GitHub issue:** #5  
**Lane:** runtime hardening  
**Owned scope:** in `EndeavorEverlasting/MomusStudio` or the subsequently proven historical implementation owner, constrain local-only ports to loopback where appropriate; eliminate/override unsafe hardcoded Compose defaults; assess the unauthenticated board/media surface; document residual risk. Momus owns the acceptance/risk record, not the implementation diff.  
**Forbidden scope:** public deployment, unrelated auth redesign, secret disclosure, duplicating implementation code into Momus, importing the unproven `MomusStudiofree` carryover into MomusStudio by assumption.  
**Expected artifacts:** configuration diff in the proven implementation repository, exact commit, port-binding proof, secret/default handling proof, security test results, residual-risk note in Momus.  
**Acceptance:** no unnecessary service is bound to all interfaces for localhost-only use; hardcoded development secrets are not relied on for shared use; exposed surfaces are explicitly authenticated, constrained, or documented as intentionally local-only.  
**Status:** repository authority for new work is resolved to `EndeavorEverlasting/MomusStudio`; execution remains gated on P01 when the hardening target is the historical carryover runtime.

## P05 — Patrick Prompt-Engineering Pilot

**GitHub issue:** #6  
**Lane:** guided creative workflow  
**Owned scope:** turn the proven P02/P03 workflow into a short exercise for Patrick: premise -> prompt -> one shot -> critique -> deliberate revision.  
**Forbidden scope:** broad curriculum design, unrelated model benchmarking, mass production.  
**Expected artifacts:** compact exercise, example prompt anatomy, critique rubric, one completed iteration with evidence.  
**Acceptance:** Patrick can explain what changed between two prompt iterations and connect the change to visible output.  
**Status:** blocked on P02; reproducibility from P03 is preferred before repeat use.
