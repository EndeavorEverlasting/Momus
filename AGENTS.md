# Momus Agent Operating Contract

`AGENTS.md` is the repository-wide operating contract for Momus. Read it before writing.

## 1. Mission

Turn AI-video ideas and carryover work into recoverable, testable, reusable workflows. The current program is concrete: recover `MomusStudiofree` / OpenCode state, prove the local waoowaoo runtime at `http://localhost:13000`, configure the minimum text → image → video chain safely, generate one representative 9:16 shot, and use the visible prompt/output loop to teach Patrick prompt engineering.

## 2. Mandatory start order

Before mutation, inspect:

1. `README.md`
2. `docs/AI_ENGINEERING_LEDGER.md`
3. `docs/EXECUTION_PLAN.md`
4. `harness/manifest.v1.json`
5. `harness/CODEBASE_MAP.md`
6. `harness/WORKFLOWS.md`
7. recent commits, branches, PRs, reports, and validation state

Repository evidence outranks assumptions. When evidence is incomplete, narrow the proof claim and create the next evidence-producing action instead of guessing.

## 3. Sprint declaration

Every writing sprint must state repository/ref, lane/mission, owned scope, forbidden scope, expected artifacts, validation commands, and proof ceiling. Parallel agents use separate branches/worktrees and explicit ownership.

## 4. Task selection

The canonical queue is `docs/AI_ENGINEERING_LEDGER.md`.

Choose work in this order:

1. an `in_progress` item already owned by the branch;
2. the earliest `ready` item whose dependencies are satisfied;
3. evidence-gathering required to unblock a `blocked` item.

Do not silently skip a higher-priority ready item. Change priority in the ledger if evidence justifies a different order.

## 5. Carryover-before-rebuild rule

The source ledger records prior work under `MomusStudiofree` via OpenCode and a working local waoowaoo target at `http://localhost:13000`. Public source identifies `waooAI/waoowaoo` as the upstream AI Video Studio and documents Docker access at port 13000, but the exact local workspace remote/ref/customization state is not yet proven.

Before replacement, upgrade, or broad source mutation:

- recover the exact local `MomusStudiofree` path and OpenCode/session context;
- inspect git remote, branch, HEAD, dirty state, local changes, configs, prompts, and last known commands;
- record evidence in `reports/carryover-inventory.md`;
- preserve separately owned or uncommitted work;
- decide what Momus should own versus reference upstream.

## 6. Runtime proof gates

Connection, generation, export, audio, and reproducibility are separate claims.

The current runtime sequence is:

1. open `http://localhost:13000`;
2. authenticate with the existing local test account;
3. enter API Configuration / Settings;
4. configure the minimum text → image → video provider chain;
5. enter provider keys in the UI only; never commit them;
6. prove all three connection checks green;
7. create **“The AI Intern Takes Corporate Speak Literally”** in 9:16;
8. generate one representative shot before batching;
9. verify audio explicitly rather than assuming it from visual generation;
10. record whether a clean rerun is reproducible.

Do not promote a lower proof gate into a higher one. Three green provider checks do not prove generation. One generated shot does not prove export, audio, or reproducibility.

## 7. Ledger contract

Every actionable ledger item must have a stable `MOMUS-NNN` ID, state (`ready`, `in_progress`, `blocked`, `done`), objective, evidence/current truth, owned scope, acceptance criteria, dependencies, and one concrete next action.

A work item becomes `done` only when acceptance evidence exists. Notes without an executable next action are not sprint-ready.

## 8. Validation and proof

Run:

```bash
python scripts/validate_repo.py
```

before commit and after ledger, manifest, workflow, or agent-contract changes. CI runs the same validator.

Repository validation proves contract consistency only. It does not prove local source recovery, provider credentials, connection health, video generation, export, audio, LAN exposure, or reproducibility unless those were separately exercised and evidenced.

## 9. Security and network boundaries

- Passwords, provider keys, tokens, and private secrets stay outside Git and reports.
- Prefer UI-entered provider credentials for the current local proof path.
- Do not expose the local app to LAN/shared use while recorded hardcoded-default or network-exposure risks remain unresolved.
- Do not weaken authentication or bind services broadly merely to simplify a demo.

## 10. Artifact discipline

Prefer prompts, prompt revisions, safe configuration metadata, command manifests, screenshots when evidentiary, checksums, and durable references. Do not commit large generated video binaries by default.

## 11. Completion and handoff

A serious sprint report must name completed work, created/modified files, commands/checks and actual results, skipped checks and reasons, evidence artifacts, gaps/blockers/risks, commit SHA and branch/PR state, and exactly one next executable action that advances the first remaining unproven state.

Do not claim completion from prose alone.
