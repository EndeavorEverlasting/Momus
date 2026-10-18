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

Current machine-readable state: `RETIRED_ALIAS_ARCHIVE_PENDING`.

**Not yet performed:** GitHub's native **Archive this repository** admin action. The current connected GitHub interface exposes read/write content and PR APIs but **does not expose the archive-admin mutation**. The deprecated repository remains writable until archive is performed through a trusted admin UI/API with appropriate authority. This is a genuine external-action blocker, not a reason to resurrect work under this remote.

After GitHub owner archival: verify `archived=true` from GitHub provider metadata, update the canonical `harness/manifest.v1.json` state to `RETIRED_ALIAS_ARCHIVED`, and record exact evidence/date. Do not delete repository history. Do not remove historical aliases from evidence. Any local `MomusStudiofree` working tree must be inventoried (path, origin/remotes, branch, HEAD SHA, dirty/untracked work) before any separately justified relocation or retirement.

## Acceptance and proof ceiling

Remote routing: committed in both repositories and fleet inventory. Historical PR: closed. Local Windows fleet runtime: untested. GitHub Actions runner status: unresolved independent limitation. **GitHub archive: pending**. Local historical checkout relation: unverified. No repository deletion, force-push, checkout reset, runtime migration, or media/secret transfer was performed.

## One owner-only action remaining

Open `https://github.com/EndeavorEverlasting/MomusStudio/settings` and choose **General > Danger Zone > Archive this repository**, then confirm; GitHub owner must perform it unless an authorized archive-capable interface becomes available. Verify the archive flag before marking the canonical receipt complete.
