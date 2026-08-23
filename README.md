# Momus

Momus is the execution repository for AI-engineering experiments that begin as creative ideas and become reproducible, evidence-backed workflows.

## Current focus

1. Recover the prior `MomusStudiofree` work and its OpenCode context before rebuilding anything.
2. Identify and bind the existing AI video-generation repository that the project is meant to reuse.
3. Run a first guided prompt-to-video sprint with Pat so the workflow teaches prompt engineering through a real creative artifact.
4. Turn successful experiments into repeatable, documented workflows with evidence and clean handoffs.

## Start here

A fresh agent should read these files in order:

1. [`AGENTS.md`](AGENTS.md) — repository operating contract.
2. [`docs/AI_ENGINEERING_LEDGER.md`](docs/AI_ENGINEERING_LEDGER.md) — canonical work ledger and current truth.
3. [`docs/EXECUTION_PLAN.md`](docs/EXECUTION_PLAN.md) — phased plan and proof gates.
4. [`harness/manifest.v1.json`](harness/manifest.v1.json) — machine-readable entrypoints and dependencies.
5. [`harness/WORKFLOWS.md`](harness/WORKFLOWS.md) — how to pick up, validate, and hand off a sprint.

## Validation

```bash
python scripts/validate_repo.py
```

The validator checks required harness files, manifest integrity, canonical ledger structure, work-item IDs, and stale template text.

## Source-of-truth policy

The Google Doc named **AI Engineering Ledger** is the human-origin notebook that seeded this repository. After reconciliation, `docs/AI_ENGINEERING_LEDGER.md` is the canonical execution source for agents. New actionable decisions belong in the repository ledger first; human notes may be reconciled into it later.

At bootstrap on 2026-08-23, connected GitHub and Google Drive evidence did not contain a repository or file named `MomusStudiofree` beyond the ledger note, and no clearly named AI video-generation repository was discoverable. Those facts are tracked as explicit recovery work rather than guessed away.

## Artifact policy

Do not commit large generated video binaries by default. Commit prompts, configuration, manifests, metadata, checksums, small reference assets when justified, and durable links or storage references for large outputs.
