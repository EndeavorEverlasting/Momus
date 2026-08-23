# Momus

Momus is the coordination repository for AI-video engineering work, beginning with the Patrick prompt-engineering pilot and the carryover from the local `MomusStudiofree` / waoowaoo workflow.

This repository is intentionally **evidence-first**. It does not pretend that the local video application source code is already present here. Instead, it preserves the engineering ledger, current state, executable sprint boundaries, proof requirements, and handoff rules so a fresh agent can continue without rediscovering the work.

## Start here

1. Read [`AGENTS.md`](AGENTS.md).
2. Read [`docs/AI_ENGINEERING_LEDGER.md`](docs/AI_ENGINEERING_LEDGER.md) for the canonical plan and provenance.
3. Read [`docs/CURRENT_STATE.md`](docs/CURRENT_STATE.md) for the live handoff point.
4. Pick exactly one bounded sprint from [`docs/SPRINTS.md`](docs/SPRINTS.md).
5. Review supporting evidence under [`docs/evidence/`](docs/evidence/).
6. Run `python scripts/validate_repo.py` before handing off or merging documentation changes.

## Current program

The first program is a vertical proof of the AI-video workflow for Patrick:

`idea/prompt -> authenticated local app -> API configuration -> text model -> image model -> video model -> representative 9:16 shot -> generation/export proof -> reproducibility`

The source ledger records a local waoowaoo instance at `http://localhost:13000`, work performed via OpenCode, and a test-account browser flow. Credentials and provider keys are **not** repository artifacts and must never be committed.

## Repository contract

- **Canonical ledger:** `docs/AI_ENGINEERING_LEDGER.md`
- **Live state:** `docs/CURRENT_STATE.md`
- **Sprint registry:** `docs/SPRINTS.md`
- **Evidence:** `docs/evidence/`
- **Harness manifest:** `harness/manifest.v1.json`
- **Validation:** `scripts/validate_repo.py`

The Google Drive document named **AI Engineering Ledger** remains the human-readable source ledger; the Markdown ledger in this repository is the agent-executable representation.
