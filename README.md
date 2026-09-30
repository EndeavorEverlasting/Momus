# Momus

Momus is the creative-content and coordination repository for the AI-video program.

Momus manages **creative intent**: projects, shot packages, prompts, references, acceptance criteria, and returned generation provenance. It intentionally does **not** implement the image/video inference engine.

## Immediate creation path

The active baseline is:

`Momus creative package -> SwarmUI -> ComfyUI -> local model -> local output file`

Start with:

- `docs/CURRENT_STATE.md` for the live handoff point.
- `docs/evidence/2026-09-29-local-creator-baseline.md` for the pinned external creator baseline.
- `creative/ai-intern/shot-001.json` for the first runtime-agnostic creative package.
- `docs/SPRINTS.md` for bounded sprint contracts.
- `AGENTS.md` for evidence and security rules.

The first active creation target remains **“The AI Intern Takes Corporate Speak Literally”** in **9:16**, with exactly one representative shot before batching.

## Historical carryover

Earlier work against a local `MomusStudiofree` / waoowaoo runtime is preserved as evidence. Its Git provenance is still unresolved and remains `REFERENCE_ONLY_UNMAPPED`.

That historical provenance lane no longer blocks the independent local-creator baseline for making new AI content.

## Repository contract

- **Canonical ledger:** `docs/AI_ENGINEERING_LEDGER.md`
- **Live state:** `docs/CURRENT_STATE.md`
- **Sprint registry:** `docs/SPRINTS.md`
- **Evidence:** `docs/evidence/`
- **Creative packages:** `creative/`
- **Harness manifest:** `harness/manifest.v1.json`
- **Validation:** `python scripts/validate_repo.py`

## Safety and storage boundaries

- Never commit passwords, API keys, tokens, or secret `.env` values.
- Do not commit model weights.
- Do not commit generated image/video binaries.
- Record output paths, workflow/model identifiers, seed, settings, timestamp, and audio presence as provenance instead.
