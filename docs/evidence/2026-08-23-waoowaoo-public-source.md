# Evidence — Public waoowaoo Source Reference

**Captured:** 2026-08-23  
**Evidence type:** public GitHub repository inspection  
**Purpose:** reduce repeated discovery while preserving the boundary between public source evidence and the unverified local `MomusStudiofree` checkout.

## Observed public source

A public repository is available at `waooAI/waoowaoo`.

Its English README identifies the project as **waoowaoo AI Video Studio** and describes an AI-video workflow that generates storyboards, characters, scenes, voiceover, and complete videos.

The same README documents:

- Docker-based startup paths that are visited at `http://localhost:13000`;
- a separate local-development path at `http://localhost:3000`;
- API-service configuration through the application's **Settings** UI;
- Docker Compose as a supported launch path.

These public-source details align with the local runtime facts captured in `2026-08-23-momusstudiofree-carryover.md` strongly enough to make this repository useful reference evidence for P01/P04 discovery.

## Important provenance limit

This evidence does **not** prove that the local `MomusStudiofree` workspace is a clean checkout, fork, branch, or specific commit of `waooAI/waoowaoo`.

The public README itself contains historical clone/update references using another repository path, which is another reason not to infer the local remote or commit from public naming alone.

Before source mutation, upgrade, or security-hardening changes, the operator must capture the local checkout's actual:

- filesystem path;
- `git remote -v`;
- branch/ref and HEAD SHA;
- dirty/untracked state;
- relevant local changes or patches.

## Effect on current sprint

P01 remains a **browser/runtime proof** sprint. This public-source reference does not expand P01 into source-code modification.

When the local implementation path is identified, record the exact binding in `docs/CURRENT_STATE.md` and update `harness/manifest.v1.json` rather than replacing this evidence note with an assumption.
