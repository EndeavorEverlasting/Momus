# AI Engineering Ledger

**Date established:** 2026-08-23  
**Repository:** `EndeavorEverlasting/Momus`  
**Human ledger:** Google Drive document, *AI Engineering Ledger*  
**Purpose:** turn the existing plan and carryover evidence into agent-executable work.

## Overview

Momus coordinates AI-assisted video-engineering work with an evidence-first operating model. The first concrete use case is to give Patrick a bounded path for learning prompt engineering through an actual AI-video production flow, while preserving the work already performed against the local MomusStudiofree/waoowaoo application via OpenCode.

The repository does not assume that the local application source is present in Momus. Its job is to preserve intent, current state, risks, proof ceilings, and sprint contracts so an agent can resume from evidence rather than restart discovery.

## Goals

1. Give Patrick a practical prompt-engineering path that produces a real representative AI-video shot rather than stopping at theory.
2. Preserve the MomusStudiofree/OpenCode carryover so agents can continue from the existing local browser state and known next action.
3. Separate planning, proof, reproducibility, and security-hardening work into bounded sprints with explicit acceptance criteria.
4. Keep credentials and provider secrets out of the repository while still documenting the configuration flow.

## Specifications

- The initial proof target is the locally running waoowaoo application at `http://localhost:13000` as recorded in the ledger evidence.
- Authentication proof uses the existing local test account. The username may be referenced for continuity; its password remains outside Git and was recorded as living in a temporary local file.
- Provider keys are entered in the application UI only and are never pasted into prompts, committed, or stored in this repository.
- The minimum model chain recorded in the carryover is: `text model -> image model -> video model`.
- The first representative project recorded in the carryover is **“The AI Intern Takes Corporate Speak Literally”** in **9:16** format.
- The first generation gate should produce **one representative shot before batching** and explicitly verify audio presence.
- Generation/export proof and reproducibility are separate acceptance gates.
- Shared/network use is forbidden until the LAN exposure and hardcoded-default risks are closed.

## Operating Model

Momus uses a durable loop:

`source evidence -> canonical ledger -> current state -> bounded sprint -> execution -> proof -> state update -> next sprint`

Documentation is an operational input. A fresh agent should be able to identify what is known, what is inferred, what remains unproven, and what exact proof is required next.

## Milestones

### M1 — AI Videos with Patrick

Use the AI-video production workflow as a hands-on prompt-engineering environment for Patrick. Start with one small, visually testable concept and teach prompt iteration against actual model output. The current representative concept is **“The AI Intern Takes Corporate Speak Literally.”**

**Outcome:** Patrick can move from an idea to a usable prompt, inspect one generated shot, describe what failed or succeeded, and iterate deliberately.

### M2 — AI Video Carryover

The source ledger records work against `MomusStudiofree` via OpenCode and shows the local waoowaoo browser flow. The carryover evidence records:

- local target: `http://localhost:13000`
- local test username: `sprint1-test`
- password location: temporary local file only; never copy into Git
- next UI area: **API Configuration**
- minimum chain: `text model -> image model -> video model`
- completion gate: **three green connection checks**
- next project: **“The AI Intern Takes Corporate Speak Literally”**
- format: **9:16**
- generation rule: **one representative shot before batching**
- explicit check: **audio presence**

The same evidence states that there were **no blockers** at the captured handoff point.

### M3 — Generation and Export Proof

Prove the first end-to-end generation/export path. Evidence must show the configured chain, the generated representative shot, the export result, and enough context to distinguish a real generated artifact from an intermediate preview.

### M4 — Reproducibility

Repeat the proven flow from a clean enough starting point that another agent can follow the documented steps and achieve the same class of result. Record prerequisites, commands, UI steps, timing, failure modes, and the produced artifact.

### M5 — Shared-Use Hardening

Before exposing the application beyond localhost-only development, close the observed security risks:

1. published ports were observed bound to `0.0.0.0`; prefer loopback binding such as `127.0.0.1:<port>:<port>` for local-only use;
2. the board/media surface was observed as unauthenticated network-reachable if the firewall allows it;
3. Compose was observed shipping hardcoded defaults including a DB password, `NEXTAUTH_SECRET`, and a fixed `API_ENCRYPTION_KEY`.

The carryover classified the hardcoded defaults as acceptable only for localhost development and explicitly deferred closure to a hardening sprint.

## Known Risks and Failure Modes

- **LAN exposure:** published ports may bind on all interfaces and become reachable on the local network.
- **Unauthenticated surface:** the carryover notes a network-reachable board/media surface if firewall policy permits it.
- **Hardcoded defaults:** development Compose values are not suitable for shared/production use.
- **Host-proxy flakiness:** transient pulls failed with `unexpected EOF` and later DNS `no such host` inside the Docker VM; retry recovered the pull.
- **Source boundary:** the local MomusStudiofree implementation is not currently present in the Momus GitHub repository, so implementation claims require external repo/path evidence.

## Acceptance Gates

| Gate | Required proof | Status at ledger import |
| --- | --- | --- |
| A. Local launch | app reachable at the recorded local URL | evidenced in screenshots |
| B. Authentication | local account can sign in | evidenced in screenshots, full post-login proof still part of next sprint |
| C. API configuration | text/image/video providers configured with three green checks | not yet evidenced |
| D. Representative shot | one 9:16 shot generated for the recorded concept; audio explicitly checked | not yet evidenced |
| E. Generation/export | representative artifact exported and captured | not yet evidenced |
| F. Reproducibility | second agent/run can reproduce from documented prerequisites | not yet evidenced |
| G. Shared-use hardening | LAN exposure and hardcoded defaults closed or deliberately contained | not yet evidenced |

## Next Action

Execute **P01 — Recover Carryover and Complete Browser Proof** from `docs/SPRINTS.md`.

The next operator should open the local app, authenticate with the existing test account without copying credentials into Git or chat, enter **API Configuration**, configure the minimum `text -> image -> video` chain using provider keys in the UI only, and capture proof of the three green connection checks. If that gate passes, continue only within the sprint's stated scope.

## Provenance

This ledger was codified from the Google Drive document *AI Engineering Ledger* dated 2026-08-23. The source document contained placeholder template text in Overview, Goals, Specifications, and a secondary section; those placeholders were intentionally replaced with source-grounded engineering content. Its embedded screenshots supply the carryover details summarized above. See `docs/evidence/2026-08-23-momusstudiofree-carryover.md` for the extracted evidence record.
