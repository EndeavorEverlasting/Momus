# Momus Evidence Reports

`reports/` contains durable evidence produced by ledger work. Reports support the canonical ledger; they do not replace it.

## Expected near-term reports

### `carryover-inventory.md`

Owned by MOMUS-002. Records the exact `MomusStudiofree` local path, git remote/ref/HEAD, dirty/untracked state, relevant OpenCode/session context, important files/configs/prompts/assets, known runtime commands, and preserve/import/reference/retire decisions.

### `waoowaoo-runtime-proof.md`

Owned by MOMUS-003. Records local access to `http://localhost:13000`, authentication result, safe text/image/video provider and model names, and each of the three connection-check results. Provider keys and passwords never belong in this report. Generation must be called unproven until a generation actually runs.

### `pat-first-video-sprint.md`

Owned by MOMUS-005. Created after the representative shot exists and Patrick completes the critique/revision loop. Records the concept, Patrick's intent/critique, prompt lineage, safe generation metadata, visible result references, deliberate revision, audio/export findings, and achieved reproducibility ceiling.

## Optional generation evidence

MOMUS-004 may either append a clearly separated generation-proof section to `waoowaoo-runtime-proof.md` or create a focused `representative-shot-proof.md` when the artifact/evidence is substantial enough to deserve its own report. Do not pre-create an empty shell.

## Report rules

Every report must:

- name its owning `MOMUS-NNN` item;
- distinguish observed evidence from inference;
- state the achieved proof gate explicitly;
- include commands/checks actually run when relevant;
- keep credentials, API keys, passwords, and private tokens out;
- avoid large generated video binaries by default;
- separate provider connectivity, generation, audio/export, reproducibility, and LAN/shared readiness claims;
- finish with the evidence-supported next action or state transition.

Do not create empty reports merely to make work appear started.
