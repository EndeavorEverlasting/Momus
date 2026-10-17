# Momus Agent Workflows

Read `AGENTS.md` first: creator-confirmed Momus = MomusStudio product identity overrides historical product-division assumptions.

## Intake and sprint selection

1. Fetch latest repository/default branch and open PRs; inventory local `git status --short`, branch, remotes, and recent commits where a checkout exists.
2. Read `AGENTS.md`, then `docs/CURRENT_STATE.md`, `docs/SPRINTS.md`, `harness/manifest.v1.json`, and this document. Compare the active task against an existing owner before branching.
3. Declare repo/branch, lane/mission, owned/forbidden scope, outputs, validators, proof ceiling. Do not reuse an occupied writer branch.
4. Select: governance edits => root contract and its validator; harness changes => `harness/`, `scripts/validate_*.py`, CI; creative changes => `creative/` with evidence; product/runtime => separately authorized implementation sprint after source provenance.

## Execute, validate, and review

Use a bounded hypothesis → build → measure → critique → decide loop. Preserve the prior good Git state; do not reset dirty checkout. Test local code with its real dependencies where possible. For this context repository:

```bash
python scripts/validate_governance.py --self-test
python scripts/validate_repo.py
python scripts/validate_context_workspace.py
python scripts/validate_harness.py --self-test
git diff --check
```

On a PR, inspect the `Validate Momus Harness` exact-SHA check and require green before merge. Compare exact head and refreshed base before merging; after merging verify current main contains the artifact and checks remain relevant.

## Failure response

- Failure in governance or alias validation: **stop product work**, correct canonical contract/legacy references within the appropriate lane. Do not reinstate a separate MomusStudio product to satisfy an old test.
- Failure in static validator: reproduce failing assertion, repair the owning source rather than suppressing test, add a negative control when useful.
- Unknown Git/local directory: record UNKNOWN and resolve on the machine; avoid guessing.
- Missing runtime/cloud access: classify BLOCKED; do not claim deployed, provider-certified, or accepted.
- Security: never print secrets or expose port `0.0.0.0` until independently hardened.

## Operator handoff

Give paths changed; SHA and PR/main state; *commands actually run* and receipts; strongest typed proof (designed/validated/integrated/deployed/observed); blockers and risks; the **first exact executable next command** with owner, dependency, expected artifact, acceptance gate. Record reusable decisions in existing owned artifact, not chat alone.
