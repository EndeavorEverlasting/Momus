# Momus Codebase Map

## Current repository shape

Momus is intentionally documentation/harness-first at bootstrap. Product code has **not** been invented because the known `MomusStudiofree` carryover and the intended AI video-generation dependency still need to be recovered/resolved.

```text
Momus/
├── AGENTS.md                         # repository-wide agent operating contract
├── README.md                         # human entrypoint and current focus
├── docs/
│   ├── AI_ENGINEERING_LEDGER.md      # canonical work queue and project truth
│   └── EXECUTION_PLAN.md             # phase sequencing and proof gates
├── harness/
│   ├── CODEBASE_MAP.md               # this map
│   ├── WORKFLOWS.md                  # task pickup / validation / handoff flows
│   └── manifest.v1.json              # machine-readable harness registry
├── reports/
│   └── README.md                     # evidence-report contract and expected reports
├── scripts/
│   └── validate_repo.py              # canonical repository validator
└── .github/
    └── workflows/
        └── validate.yml              # CI wrapper for the canonical validator
```

## Canonical owners

| Concern | Canonical owner | Notes |
| --- | --- | --- |
| Agent behavior | `AGENTS.md` | Do not create a second governance file. |
| Current work state | `docs/AI_ENGINEERING_LEDGER.md` | Stable `MOMUS-NNN` IDs and next actions. |
| Program sequencing | `docs/EXECUTION_PLAN.md` | Dependencies and proof gates. |
| Harness discovery | `harness/manifest.v1.json` | Machine-readable entrypoints/dependency states. |
| Execution workflow | `harness/WORKFLOWS.md` | How an agent picks up and hands off work. |
| Validation | `scripts/validate_repo.py` | CI calls the same validator. |
| Evidence reports | `reports/` | Sprint-produced evidence; not a second ledger. |

## Known external/unrecovered surfaces

### MomusStudiofree

Known from the source ledger as prior work performed via OpenCode. It was not found in connected GitHub/Drive evidence at bootstrap. MOMUS-002 owns recovery. No product-code directory should be invented to represent it until recovery evidence exists.

### Existing AI video-generation repository

Known from the source ledger as the intended production dependency for Pat's prompt-engineering work. It was not identifiable from connected repository names/descriptions at bootstrap. MOMUS-003 owns resolution. When found, add its exact repository/path/ref and entrypoints to `harness/manifest.v1.json`.

## Future product-code placement

The repository does not reserve arbitrary `src/`, `app/`, or `studio/` trees yet. After MOMUS-002 and MOMUS-003 establish real boundaries, import only code Momus actually owns. Keep external production systems as dependencies when they remain independently authoritative.

## Commands

Repository validation:

```bash
python scripts/validate_repo.py
```

No build, test, generation, or deployment command is canonical yet because the actual generation runtime has not been resolved. Agents must not manufacture those commands; MOMUS-003 exists to discover and register them from evidence.
