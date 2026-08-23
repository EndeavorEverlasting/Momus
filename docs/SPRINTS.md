# Sprint Registry

Each sprint is intentionally small enough that a fresh agent can execute it without silently absorbing adjacent work.

## P00 — Ledger and Agent Harness Bootstrap

**Lane:** repository coordination  
**Owned scope:** replace template placeholders with canonical plan content; establish agent entrypoints, current state, sprint registry, evidence record, manifest, and validator.  
**Forbidden scope:** product-code changes, provider credentials, destructive cleanup, claims that MomusStudiofree source is in this repository.  
**Expected artifacts:** `AGENTS.md`, ledger, current state, sprint registry, evidence note, manifest, validator, updated README.  
**Acceptance:** validator passes; no placeholder template text remains in tracked coordination files; branch/PR/merge evidence recorded.  
**Status:** in progress until merged and verified.

## P01 — Recover Carryover and Complete Browser Proof

**Lane:** local browser/runtime proof  
**Owned scope:** verify the recorded local application is reachable; authenticate using the existing local test account; open API Configuration; configure the minimum text/image/video chain; capture three green connection checks.  
**Forbidden scope:** committing credentials, network exposure, security-hardening changes, bulk generation, unrelated UI work.  
**Expected artifacts:** timestamped screenshots or logs showing reachability, authenticated state, API Configuration, and three successful connection checks; current-state update.  
**Acceptance:** all three provider/model connections are visibly healthy and no secret value appears in committed artifacts.  
**Status:** ready.

## P02 — Representative Shot and Generation/Export Proof

**Lane:** AI-video generation  
**Owned scope:** create **“The AI Intern Takes Corporate Speak Literally”** in **9:16**, generate exactly one representative shot before batching, verify audio presence, then prove generation/export.  
**Forbidden scope:** batch production before the one-shot gate, unrelated creative variants, shared-network deployment.  
**Expected artifacts:** final prompt/settings summary with secrets removed, screenshot of representative shot, audio verification note, exported artifact reference, generation/export log.  
**Acceptance:** one representative shot is generated and an export artifact is proven.  
**Status:** blocked on P01.

## P03 — Reproducibility Seal

**Lane:** repeatability  
**Owned scope:** reproduce the successful P02 flow from documented prerequisites and capture exact steps, expected timings, recoverable failures, and outputs.  
**Forbidden scope:** architectural rewrite, security redesign, feature expansion.  
**Expected artifacts:** reproducibility runbook, second-run evidence, failure/retry notes, current-state update.  
**Acceptance:** another agent/operator can reproduce the same class of output without relying on unstated memory.  
**Status:** blocked on P02.

## P04 — Shared-Use Security Hardening

**Lane:** runtime hardening  
**Owned scope:** constrain local-only ports to loopback where appropriate; eliminate/override unsafe hardcoded Compose defaults; assess the unauthenticated board/media surface; document residual risk.  
**Forbidden scope:** public deployment, unrelated auth redesign, secret disclosure.  
**Expected artifacts:** configuration diff in the implementation repository, port-binding proof, secret/default handling proof, security test results, residual-risk note.  
**Acceptance:** no unnecessary service is bound to all interfaces for localhost-only use; hardcoded development secrets are not relied on for shared use; exposed surfaces are explicitly authenticated, constrained, or documented as intentionally local-only.  
**Status:** ready after implementation repository/path is identified; not a blocker for localhost-only P01/P02 proof.

## P05 — Patrick Prompt-Engineering Pilot

**Lane:** guided creative workflow  
**Owned scope:** turn the proven P02/P03 workflow into a short exercise for Patrick: premise -> prompt -> one shot -> critique -> deliberate revision.  
**Forbidden scope:** broad curriculum design, unrelated model benchmarking, mass production.  
**Expected artifacts:** compact exercise, example prompt anatomy, critique rubric, one completed iteration with evidence.  
**Acceptance:** Patrick can explain what changed between two prompt iterations and connect the change to visible output.  
**Status:** blocked on P02; reproducibility from P03 is preferred before repeat use.
