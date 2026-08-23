# Momus Agent Operating Contract

`AGENTS.md` is the repository-wide operating contract for agents working in Momus. Read it before writing.

## 1. Mission

Turn creative AI-engineering ideas into recoverable, testable, reusable workflows. Current scope is the AI-video work described in the canonical ledger: preserve prior work, reuse the correct existing production system, and make each sprint leave evidence the next agent can act on.

## 2. Mandatory start order

Before mutation, inspect:

1. `README.md`
2. `docs/AI_ENGINEERING_LEDGER.md`
3. `docs/EXECUTION_PLAN.md`
4. `harness/manifest.v1.json`
5. `harness/CODEBASE_MAP.md`
6. `harness/WORKFLOWS.md`
7. recent commits, branches, PRs, reports, and validation state

Repository evidence outranks assumptions. When evidence is missing, narrow the claim and create the evidence-producing task instead of inventing an answer.

## 3. Sprint declaration

Every writing sprint must state:

- repository and exact branch/ref;
- sprint/lane and mission;
- owned scope;
- forbidden scope;
- expected artifacts;
- validation command(s);
- proof ceiling.

Keep the mutation inside the declared boundary. Parallel agents use separate branches or worktrees and explicitly separate owned scope.

## 4. Task selection

The canonical work queue is `docs/AI_ENGINEERING_LEDGER.md`.

Choose work in this order:

1. an `in_progress` item already owned by the current branch;
2. the earliest `ready` item whose dependencies are satisfied;
3. evidence-gathering needed to unblock a `blocked` item.

Do not silently skip a higher-priority ready item because another task is more interesting. If priority should change, change the ledger deliberately and explain why.

## 5. Carryover-before-rebuild rule

`MomusStudiofree` is recorded as prior work performed via OpenCode, but it was not found in connected GitHub or Drive sources during repository bootstrap. Treat that as a recovery problem, not permission to recreate it from memory.

Before writing replacement product code:

- inspect known development roots and OpenCode state for the exact prior project/session;
- inventory recovered source, configuration, prompts, assets, commands, and runnable state;
- record evidence in `reports/carryover-inventory.md`;
- identify what is safe to import, reference, or retire.

No fresh implementation may claim to replace the carryover until that inventory exists.

## 6. Reuse-before-duplicate rule

The original ledger says the Pat work should use an existing AI production / video-generation repository. That dependency is not yet resolved in connected sources.

Before creating a new video-generation stack, search existing repositories, local remotes, workspaces, and project notes. When found, record its exact repository/path/ref and reusable entrypoints in `reports/video-repo-resolution.md` and update `harness/manifest.v1.json`.

Do not create a duplicate authority merely to make progress look easier.

## 7. Ledger contract

Every actionable ledger item must have:

- stable `MOMUS-NNN` ID;
- state: `ready`, `in_progress`, `blocked`, or `done`;
- objective;
- evidence/current truth;
- owned scope;
- acceptance criteria;
- dependencies;
- one concrete next action.

A work item becomes `done` only when its acceptance criteria have evidence. Notes without an executable next action are not sprint-ready.

## 8. Validation and proof

Run:

```bash
python scripts/validate_repo.py
```

before commit and again after any ledger, manifest, workflow, or agent-contract change. CI runs the same validator.

A green validator proves repository structure and contract consistency only. It does not prove local OpenCode recovery, third-party generation services, GPU/runtime behavior, or successful video output unless those were actually exercised and evidenced.

## 9. Artifact discipline

Prefer small, durable evidence:

- prompts and prompt revisions;
- config and command manifests;
- structured metadata;
- checksums;
- screenshots only when they add evidence;
- links/references for large generated media.

Do not commit credentials, API keys, private tokens, personal secrets, or large video binaries by default.

## 10. Completion and handoff

A serious sprint report must name:

- completed work;
- created/modified files;
- validation commands and actual results;
- skipped checks and why;
- evidence artifacts;
- gaps, blockers, and risks;
- commit SHA and branch/PR state;
- exactly one next executable action that advances the first remaining unproven state.

Do not claim completion from prose alone.
