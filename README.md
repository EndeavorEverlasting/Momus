# Momus

Momus is the execution repository for AI-assisted video engineering: preserve prior work, prove the local generation stack, turn creative prompting into reproducible sprints, and leave enough evidence that another agent can continue without hidden chat context.

## Current focus

1. Recover the exact `MomusStudiofree` / OpenCode workspace state and bind it to its real git provenance.
2. Reopen the existing local **waoowaoo** app at `http://localhost:13000` and verify the minimum **text → image → video** provider chain.
3. Prove three green provider connection checks with API keys entered through the UI only and kept outside Git.
4. Create **“The AI Intern Takes Corporate Speak Literally”** in **9:16** and generate one representative shot before any batching.
5. Treat generation/export, audio, and reproducibility as separate proof gates; do not infer them from a successful connection test.
6. Use the proven workflow as a hands-on prompt-engineering environment for Patrick: create, critique visible output, revise deliberately, and record what changed.

## Start here

A fresh agent should read these files in order:

1. [`AGENTS.md`](AGENTS.md) — repository operating contract.
2. [`docs/AI_ENGINEERING_LEDGER.md`](docs/AI_ENGINEERING_LEDGER.md) — canonical work ledger and current truth.
3. [`docs/EXECUTION_PLAN.md`](docs/EXECUTION_PLAN.md) — phased plan and proof gates.
4. [`harness/manifest.v1.json`](harness/manifest.v1.json) — machine-readable entrypoints, runtime, and dependencies.
5. [`harness/WORKFLOWS.md`](harness/WORKFLOWS.md) — task pickup, runtime proof, validation, and handoff.

## Validation

```bash
python scripts/validate_repo.py
```

The validator checks required harness files, manifest integrity, canonical ledger structure, work-item IDs, and stale source-template text.

## Source-of-truth policy

The Google Doc named **AI Engineering Ledger** is the human-origin notebook that seeded this repository. On 2026-08-23 it was refreshed with the concrete waoowaoo runtime plan. After reconciliation, `docs/AI_ENGINEERING_LEDGER.md` is the canonical execution source for agents. New actionable state belongs in the repository ledger and evidence reports.

## Known runtime and upstream

The plan identifies a local waoowaoo instance at `http://localhost:13000`. Public-source inspection also identifies `waooAI/waoowaoo` as the upstream AI Video Studio; its documentation confirms Docker-based runs at port 13000 and UI-based API configuration. The exact relationship between the local `MomusStudiofree` workspace and upstream git ref still requires local evidence, so agents must recover provenance before rewriting or upgrading it.

## Artifact policy

Do not commit passwords, provider keys, or large generated video binaries by default. Commit prompts, configuration intent, safe command/model/provider metadata, checksums, small reference assets when justified, and durable references to large outputs.
