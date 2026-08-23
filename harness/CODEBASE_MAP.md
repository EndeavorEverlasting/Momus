# Momus Codebase Map

## Current repository shape

Momus is documentation/harness-first while the local carryover is being recovered. Product code is not duplicated into this repository merely because the local source relationship is not yet fully proven.

```text
Momus/
├── AGENTS.md                         # repository-wide agent operating contract
├── README.md                         # human entrypoint and current runtime focus
├── docs/
│   ├── AI_ENGINEERING_LEDGER.md      # canonical work queue and current truth
│   └── EXECUTION_PLAN.md             # phase sequencing and proof gates
├── harness/
│   ├── CODEBASE_MAP.md               # this map
│   ├── WORKFLOWS.md                  # task pickup / runtime proof / handoff flows
│   └── manifest.v1.json              # machine-readable registry
├── reports/
│   └── README.md                     # evidence-report contract
├── scripts/
│   └── validate_repo.py              # canonical repository validator
└── .github/
    └── workflows/
        └── validate.yml              # CI wrapper for the validator
```

## Canonical owners

| Concern | Canonical owner | Notes |
| --- | --- | --- |
| Agent behavior | `AGENTS.md` | Do not create a second governance authority. |
| Current work state | `docs/AI_ENGINEERING_LEDGER.md` | Stable `MOMUS-NNN` IDs and next actions. |
| Program sequencing/proof gates | `docs/EXECUTION_PLAN.md` | Runtime → connectivity → generation → higher proofs. |
| Harness/runtime discovery | `harness/manifest.v1.json` | Machine-readable entrypoints, runtime and dependency state. |
| Execution workflow | `harness/WORKFLOWS.md` | How an agent proves each gate and hands off. |
| Validation | `scripts/validate_repo.py` | CI calls the same validator. |
| Evidence reports | `reports/` | Proof artifacts; not a second ledger. |

## External and local surfaces

### Public upstream: `waooAI/waoowaoo`

Public upstream AI Video Studio. Its documentation describes Docker-based startup at `http://localhost:13000`, Settings-based API configuration, and the AI-video stack used by this program. Treat this as upstream reference authority, not automatically as the exact local checkout state.

### Local carryover: `MomusStudiofree`

Prior work performed via OpenCode. The source ledger identifies the existing local waoowaoo app at `http://localhost:13000` as the first proof target. MOMUS-002 owns exact local path, git remote/ref/dirty-state, OpenCode context, and customization recovery.

### Local runtime

- URL: `http://localhost:13000`
- Authentication: existing local test account
- Provider configuration: application API Configuration / Settings UI
- Minimum chain: text model → image model → video model
- Connectivity gate: three green provider checks
- First generation target: **“The AI Intern Takes Corporate Speak Literally”**, 9:16, one representative shot

Secrets are not stored in Momus.

## Product-code boundary

Do not create an arbitrary Momus `src/`, `app/`, or copied waoowaoo tree until local provenance establishes what this repository should own. If `MomusStudiofree` is an independently useful clone/fork/worktree, preserve that boundary and reference it. Import only material Momus actually needs to own.

## Commands

Repository validation:

```bash
python scripts/validate_repo.py
```

The runtime launch command is intentionally not declared canonical here until MOMUS-002 recovers the exact local workspace command and git state. Public upstream documents Docker startup, but the local carryover command must come from local evidence before agents automate it.
