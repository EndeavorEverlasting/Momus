# Momus Evidence Reports

`reports/` contains durable evidence produced by ledger work. Reports support the canonical ledger; they do not replace it.

## Expected near-term reports

### `carryover-inventory.md`

Owned by MOMUS-002. Created only after local/OpenCode recovery work actually runs. It records recovered `MomusStudiofree` paths/sources, important files, git/session state, known runnable commands, assets, provenance, and preserve/import/reference/retire decisions.

### `video-repo-resolution.md`

Owned by MOMUS-003. Created after the intended AI production / AI video-generation dependency is evidence-backed. It records the exact repository/path/ref, generation entrypoint, prerequisites, integration boundary, and why the selected dependency matches the original plan.

### `pat-first-video-sprint.md`

Owned by MOMUS-004. Created after an actual guided generation sprint with Pat. It records the concept, prompt lineage, safe generation metadata, result reference, review observations, and prompt-engineering lessons.

## Report rules

Every report must:

- name its owning `MOMUS-NNN` work item;
- distinguish observed evidence from inference;
- include commands/checks actually run when relevant;
- avoid credentials, secrets, or private tokens;
- avoid large generated video binaries by default;
- finish with the evidence-supported next action or state transition.

Do not pre-create empty report shells merely to make a work item look started. The report should appear when there is evidence to record.
