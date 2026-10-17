# Skill — Creative Shot Handoff

**Trigger:** the operator asks to turn an idea into an AI video shot, reproduce a prior shot, or hand a generation job to a second agent.

**Inputs:** project name, premise, prompt, aspect ratio, target duration, runtime/provider choice if confirmed, references and nonsecret settings. Read `AGENTS.md` and the selected creative package under `creative/` first.

**Procedure:**
1. Reuse the existing package schema at `creative/ai-intern/shot-001.json`; create a new project-specific path only with an authorized creative sprint.
2. Preserve prompt, negative prompt, requested aspect ratio, audio intent and exactly-one-representative-shot-before-batching gate.
3. Check actual runtime availability; distinguish planned SwarmUI/ComfyUI from verified local applications. Creator name MomusStudio refers to Momus, not another product.
4. Run a single real shot if user approves any paid inference; verify generated artifact, audio presence, SHA/path, settings and timestamp. Never commit media or keys.
5. Return explicit PASS/FAIL/UNKNOWN proof and next command. Update the canonical creative package and evidence receipt without moving or deleting the user's media.

**Outputs:** tracked JSON creative package, redacted nonsecret provenance/evidence, human handoff. **Validation:** `python scripts/validate_repo.py`; generation proof requires a separate real runtime observation. **Forbidden:** paid generations without approval, fake shots, historical source mutation, shared-network exposure.
