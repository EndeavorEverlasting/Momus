# MomusStudio repository deprecation — evidence and handoff (2026-10-17)

## Operator decision and canonical target

The creator confirms that `MomusStudio` was an accidental duplicate repository for the **same intended product**, not a second product or implementation owner. **Only** `EndeavorEverlasting/Momus` is authorized for new Momus issues, code, sprints, agent work, governance, and product coordination. This decision supersedes the historical context/implementation split without rewriting historical Git provenance.

## Provider inspection on 2026-10-17 (America/New_York)

- Canonical: `EndeavorEverlasting/Momus` (`main`, public, unarchived).
- Deprecated: `EndeavorEverlasting/MomusStudio` (private, **still unarchived** at the last direct GitHub read).
- Deprecated repository's `main`: redirect README, root `AGENTS.md` stop rule, `.gitignore`, empty placeholder directories; no observed first-party application implementation.
- Deprecated repository's only additional branch: `feat/context-workspace-adoption`. Its PR #1 is **closed unmerged**; it contained the now-rejected context-vs-implementation ownership split and static validator scaffolding, not a certified working product.
- No open PRs, no open issues, no releases observed on the deprecated remote.
- All previously observed duplicate contents and branch history were **preserved**. This is not an assertion of equivalence with local `MomusStudiofree` / waoowaoo history.

## Completed remote deprecation

- `MomusStudio/main/README.md` redirects to Momus; root `AGENTS.md` refuses new work under the duplicate name.
- `Momus/main/AGENTS.md`, `README.md` and project manifests establish the sole product/repository.
- `MomusStudio` PR #1 closed without merging.
- `github-config` PR #4 merged at `b3a3938acbdb5e693cb1f343dd3b3bbbe61ffdd1`: the retained 47-entry Entire fleet inventory now classifies the duplicate as `RETIRED_ALIAS` and skips its local checkout before probing Git or Entire. The exact-branch static checks passed; GitHub Actions runners were unavailable on current and historical CI attempts.

## Retirement versus archival

Historical pre-archive state on 2026-10-17: `RETIRED_ALIAS_ARCHIVE_PENDING`. **Current verified state on 2026-10-19: `RETIRED_ALIAS_ARCHIVED`.**

**Completed October 19, 2026:** The operator archived the repository using GitHub's native admin UI. GitHub displayed a success message that the repository was archived by its owner on October 19, 2026 and is read-only. An independent connected GitHub `get_repo` read on 2026-10-19 returned `archived=true` for the exact repository `EndeavorEverlasting/MomusStudio`. GitHub's archive action was performed by the owner, not by this agent.

Post-archive canonical closeout: GitHub provider metadata verified `archived=true`; canonical `harness/manifest.v1.json` is now marked `RETIRED_ALIAS_ARCHIVED` with verification date and method. Do not delete Git history or erase the historical aliases from evidence. Any local `MomusStudiofree` working tree remains separately `REFERENCE_ONLY_UNMAPPED` and requires its own provenance inventory (path, origin/remotes, branch, HEAD SHA and dirty/untracked state) before any relocation or retirement.

## Acceptance and proof ceiling

Remote routing: committed in both repositories and fleet inventory. Historical PR: closed. Local Windows fleet runtime: untested. GitHub Actions runner status: unresolved independent limitation. **GitHub archive: verified complete 2026-10-19 (`archived=true` confirmed via GitHub).** Local historical checkout relation: unverified. No repository deletion, force-push, checkout reset, runtime migration, or media/secret transfer was performed.

## Owner action completed — 2026-10-19

The owner confirmed GitHub's **Archive this repository** action. The screenshot shows a successful archive banner and read-only notice dated October 19, 2026. The subsequent connected GitHub repository metadata independently confirmed `archived=true`. No further operator action is needed for the **remote duplicate retirement**. The active Momus project proceeds separately on its existing roadmap.
