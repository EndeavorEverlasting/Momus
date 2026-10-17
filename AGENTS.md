# Momus Agent Contract

This root `AGENTS.md` is the **single normative governance contract** for agents and developers working in this repository. Supporting manifests, plans, skills, and historical evidence may elaborate workflows but must not contradict this contract.

## Creator-authoritative product identity

**Founder decision, 2026-10-17:** **Momus** and **MomusStudio** were names used for **the same intended AI-video product**. The creator selected **Momus** as the preferred, shorter project name. **MomusStudio is not a separate product** and must not be assigned a second product mission, roadmap, or owner based merely on its name. The canonical accessible repository and governance entrypoint is `EndeavorEverlasting/Momus`.

Earlier documents adopted an artificial `context authority` / `implementation authority` mapping between `EndeavorEverlasting/Momus` and `EndeavorEverlasting/MomusStudio`. **That mapping is superseded as product governance; it is historical evidence only.** Do not route new work away from Momus merely because it concerns implementation. Product code may be added only under a separately authorized, bounded sprint, never as part of a governance or harness-only sprint.

**Repository provenance is a different question from product identity.** A historical `MomusStudiofree` checkout, `EndeavorEverlasting/MomusStudio` Git URL, and the external `waooAI/waoowaoo` reference may have independent Git histories. Their relation remains `REFERENCE_ONLY_UNMAPPED` until actual remotes, branch, commit, and dirty state are inspected. Never claim histories, bytes, or installations have been merged or mapped without evidence; do not overwrite existing checkouts. Lack of Git mapping is **not** evidence of two products.

When older ledgers, the `harness/context-workspace-adoption.v1.json` historical record, or a stale tool assert an implementation-owner split, use this creator decision as the product-identity authority, then repair the stale harness contract in its own bounded lane. Preserve useful historical evidence rather than erasing it.

## Agent operating principles

1. **Evidence before action:** refresh remote/working-tree truth; inspect existing owners, tests, known limitations, and collisions.
2. **Floor before furniture:** establish the current proven code, contracts, and accepted behaviors before changing architecture or UI.
3. **Bounded sprints with declared scope:** keep changes within explicit owned files and forbidden boundaries.
4. **One writer per branch:** coordinate parallel work through isolated branches or worktrees without conflicting filesystem, ports, or data.
5. **Reuse before replacing:** prefer the established file, contract, repository and working code over new duplicate infrastructure.
6. **No completion without proof:** measured validation, actual artifacts, integration state and proof ceiling must support claims.

## Instruction precedence

On conflict, obey the highest applicable authority in this order:

1. Platform requirements, security and legal obligations, and applicable repo-owner instructions.
2. This root governance contract.
3. Task-specific prompts or sprint instructions.
4. Generic defaults.

This order cannot authorize behavior prohibited by a higher-level instruction or erase creator-verified product facts. Preserve and report conflicts; do not silently pick a convenient convention.

## Mandatory writing-sprint declaration

Before any repository write, explicitly declare and record:

- **Repository and branch** (including refreshed base evidence).
- **Lane and mission**.
- **Owned scope and forbidden scope**.
- **Expected artifacts and actual validation commands**.
- **Proof ceiling** (what cannot be demonstrated from this environment).

Confirm current PRs/branches and preserve dirty or separately owned changes; use an isolated lane when necessary. Do not allow an agent to invent a second application or canonical checkout to simplify its task.

## Required execution workflow

1. Read this governance file first; then current `docs/CURRENT_STATE.md`, `docs/SPRINTS.md`, `docs/AI_ENGINEERING_LEDGER.md`, and `harness/manifest.v1.json`. Historical evidence is evidence, not current governance.
2. Refresh Git remote/default-branch state and inspect active PRs, working tree, and source ownership.
3. Choose a bounded sprint, implement the smallest useful slice, and validate changed behavior, preserved behavior, and security constraints.
4. Use hypothesis → build → measure → critique → decide for substantive prototypes. Preserve the last known-good state.
5. Before a completion claim, record named changed files, actually executed checks and results, exact commit SHA, push/PR/merge state, remaining blockers and **one executable next command**.
6. Merge validated authorized work only when checks, permissions, and review gates permit; do not equate an unmerged PR with integration.
7. Distinguish `PLANNED`, `IMPLEMENTED`, `VALIDATED`, `INTEGRATED`, `DEPLOYED`, and `OBSERVED`. GitHub CI cannot certify the operator's Linux Mint installation or live cloud credentials.

## Completion standard

A task is COMPLETE only when its owned artifacts exist, every stated acceptance criterion is proven or explicitly classified as blocked, changed paths are named, validations actually ran, a commit SHA is recorded, push/PR status is stated, and the report contains one concrete NEXT COMMAND. Do not infer a live runtime from a document, test fixture, screenshot, or PR.

## Forbidden behaviors

- Acknowledgment without authorized mutation for a mutation-bearing task.
- Plans without execution when executable owned work remains.
- Summaries without evidence or completion claims without actually running applicable checks.
- Exposing passwords, secrets, tokens, provider credentials, or hidden `.env` values in prompts, logs, Git or screenshots.
- Force-push, destructive cleanup, overwriting existing media, or undocumented migrations.
- Treating `MomusStudio` as a separate product, inventing a second owner solely from old names, or using Git provenance uncertainty to override the founder's product-identity decision.
- Claiming successful external provider calls, local launches, generation/export, or deployment without observed proof.

## Evidence, safety and historical status

Never commit model weights, generated video/image binaries, provider keys or private media. The earlier local waoowaoo evidence noted broad network bindings and development secrets: treat shared-network use as unproven until hardened. Historic `MomusStudiofree` and `waooAI/waoowaoo` artifacts remain reference-only until independently verified. Historical configuration/status entries under `harness/` do not authorize product splitting.

## Verification entrypoints

- `python scripts/validate_governance.py` validates this contract and the founder identity rule.
- `python scripts/validate_governance.py --self-test` proves the validator rejects corrupted contract examples.
- `python scripts/validate_repo.py` runs the existing Momus coordination checks.
- Additional harness and integration validators, when registered, may strengthen these checks but cannot weaken this contract.
