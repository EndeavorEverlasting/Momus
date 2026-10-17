# Momus Creator UX Readiness — Pre-Live-Cert Contract

**Status:** PROVISIONAL DESIGN + STRUCTURAL GATE; **LIVE UX NOT CERTIFIED**
**Evidence floor:** `EndeavorEverlasting/Momus` main `b6149a50b999f490c4d5b9ba5c6da63ed54990f5`, inspected 2026-10-17.
**Identity:** Momus = MomusStudio, alternate names for the same intended product; no independent product assignment. Physical Git provenance for older source remains unverified.

## Sprint declaration: P08 — Creator Interface Readiness

- **Repo / branch:** `EndeavorEverlasting/Momus`, `ux/creator-readiness-gate-20261017` based on the pinned main head above.
- **Lane / mission:** UX strategy and *fail-closed live-cert acceptance definition*, in advance of launching the Momus operator runtime.
- **Owned scope:** this canonical UX design/readiness contract; `harness/ux-readiness.v1.json`; its structural/receipt validator; CI and harness entrypoint registration.
- **Forbidden scope:** inventing a second Momus app; implementing or replacing the unknown local UI; editing historical `MomusStudiofree` worktrees; installing models or credentials; calling unobserved output generation successful; public network exposure; media binaries; sweeping unrelated redesign.
- **Artifacts:** this document, machine-readable acceptance cases, executable validator and CI check; PR + mainline integration only if validation gates permit.
- **Proof ceiling:** the accessible repository contains no launchable first-party UI. Structural validation cannot prove browser geometry, interaction, user experience or local workstation readiness. The actual source/route/runtime, supported device contract, browser traces, screenshots and one-shot output remain **UNKNOWN/BLOCKED**, not green.

## Audience and design goal

**Primary:** a first-time, nontechnical creator who wants to make an AI video without seeing graphs, ports, providers, tokens, node parameters or command lines.
**Secondary:** an advanced creator/operator who needs control of reproducible workflows, model/runtime settings and provenance.

**One first-use journey:** open Momus -> start a project -> write the premise -> see editable shot cards/storyboard -> set a 9:16 preview -> choose/generate **one** representative shot -> see genuine queue/progress/error state -> review video and audio -> deliberately revise or export -> reopen without losing the work. Use the existing `creative/ai-intern/shot-001.json` as the initial realistic fixture; *do not fake a generation response*.

### Proposed interaction architecture (design; not implemented)

1. **Studio entry / projects:** clear `New Project`, `Open`, recent drafts and recoverable empty state. An optional beginner walkthrough is skippable.
2. **Creative workspace:** cinematic preview has visual priority; project and shot navigation remain legible. A succinct prompt/brief composer and one prominent `Generate one shot` action lead the workflow. Keep version history and export reachable without hiding them behind hover.
3. **Storyboard / filmstrip:** explicit shot title, duration, 9:16 aspect, image/reference, prompt and status. Editing a shot must not erase unrelated selections or active search.
4. **Review and export:** visually separate playable preview from queued, errored and exported output; audio-present indicator and real exported-file evidence. Display runtime/model/seed/settings in a secondary provenance drawer.
5. **Advanced mode:** progressive disclosure to model/backend selection, ComfyUI graph and parameter tuning. Simple and advanced controls modify the *same* canonical shot state, not duplicate interpretations.
6. **Failure/recovery:** save drafts as edits occur (with honest save status); prevent generation double-submit; allow cancel/retry; present actionable errors without losing text. Distinguish queued, running, failed, succeeded and exported.
7. **Aesthetic direction:** calm, cinematic, dark-tinted work surface with intentional accent color; generous video preview and restrained controls. Text contrast, font clarity, whitespace and predictable motion matter more than decorative effects. Avoid generic nested-card dashboards or excessive animations.
8. **Accessibility / ergonomics:** labeled actions, keyboard-visible focus, screen-reader meaningful status, reduced motion, non-color-only states, appropriately sized touch targets where touch is supported. Never rely exclusively on hover or shortcut memorization.

**Layout is a candidate, not a frozen implementation:** wide desktop uses contextual left navigator, dominant preview, optional properties pane, bottom storyboard. Constrained desktop collapses secondary properties before shrinking essential preview/actions. Phone support must be declared from actual product/runtime ownership before certification; if supported, use native tap surfaces and rotate portrait -> landscape -> portrait without resetting state. No tiny transplanted desktop chrome.

## External precedent and disposition (inspected 2026-10-17)

| Reference | Observed mechanism / evidence | Disposition |
| --- | --- | --- |
| Paul Bakaus, [Impeccable](https://github.com/pbakaus/impeccable) | `/impeccable init`, audit/critique/harden/adapt/optimize/craft, deterministic design checks and live visual iteration described in the canonical repository | **ADOPT principles; ADAPT tool integration** after actual UI source is resolved. No claim that its detector ran here. |
| [SwarmUI](https://github.com/mcmonkeyprojects/SwarmUI/blob/master/src/Pages/Text2Image.cshtml) | Source includes separate Simple and Generate tabs; docs explain editable simplified workflow inputs and advanced Comfy access | **ADAPT** simplified front door, not the full external app or its node surface. |
| [InvokeAI](https://github.com/invoke-ai/InvokeAI) | Documented integrated canvas, graph workflows and board/gallery model; code-backed project has a real UI, but Momus equivalence is untested | **ADAPT** integrated creative context and asset recall; reject wholesale UI cloning. |
| [InvokeAI workspace RFC](https://github.com/invoke-ai/InvokeAI/issues/8988) | Proposal separates structured panel state from editable graph state; an RFC is **not proof of shipped behavior** | **CONSIDER** one state owner with clear conversion boundary; verify implementation before adopting code. |

**External availability vs local gap:** simplified workflow entry, unified creative canvases and galleries exist elsewhere. Momus currently has a documented first shot, orchestration/harness and a proposed external local runtime, but no accessible first-party UI source or fresh browser pass in this repository. The high-leverage first gap is **resolve the actual local UI source/runtime and execute a credible live UX acceptance matrix**, *not* create a second frontend.

## Fixed acceptance rubric

The canonical cases are `harness/ux-readiness.v1.json`; required case identifiers must not disappear to make a certification go green:

- Desktop pointer: full one-shot creative journey including genuine render/export; 1024x768 geometry; loading/empty/failure/retry/success; preservation through reload.
- Keyboard + browser parity: complete terminal actions without a mouse in Chromium/Firefox, visible focus, dialogs and Escape semantics, no duplicate commands.
- Accessibility: real focus/announcement/label/contrast checks plus reduced-motion handling.
- Touch if declared supported: portrait tap journey and portrait/landscape/portrait preservation; test actual device ergonomics separately from Chromium emulation.
- For every case: exact UI-source Git SHA, app URL/route, browser/version, viewport, input, date, artifact and terminal observation. Required output cases are **not** satisfied by mocked video files or static HTML.
- Failure severity: any loss of creative draft, unavailable primary action, nonfunctional generation/export, accidental destructive transition, credential disclosure or serious focus/geometry blocker prevents certification.
- A passing JSON receipt validates its **shape only**; separately inspect actual browser traces/screenshots/device behavior. Static source inspection is insufficient.

## Prototype → measure → refine ladder

1. **Baseline / provenance (BLOCKED on operator runtime):** recover local checkout path/remotes/HEAD/dirty state without modifying it; resolve actual application URL, tested browser versions and supported screen/input modes. Capture baseline screenshots before changes.
2. **One journey / functional candidate (REQUIRED SUCCESSOR):** instrument the existing app around real shot editing, one queued generation and export, with the source fixture above. Test mouse + keyboard actions and save/reload.
3. **Responsive + failure iterations (REQUIRED SUCCESSOR):** falsify computed geometry and target reachability at wide/constrained viewports, and touch orientations if supported; test meaningful empty/error/retry state sequences. Repair shared layout/state owner; rerun impacted neighbors.
4. **Craft pass (REQUIRED SUCCESSOR):** run approved `/impeccable audit`, `critique`, `harden`, `adapt`, `polish` against the actual implementation; only then adjust typography, contrast, motion and creative immersion without breaking function.
5. **Exact-head live cert (BLOCKED until above):** run browser/device matrix against the exact integrated UI revision; attach artifacts and a receipt using `python scripts/validate_ux_readiness.py --receipt PATH_TO_RECEIPT.json`. This only checks receipt structure; the evidence reviewer must open traces/screenshots and confirm the reported interactions. If head changes, repeat affected proof. Shared-network distribution also depends on P04 security.

**Measured success criteria proposed for pilot:** first-time creator can complete one shot without CLI or knowledge of ComfyUI nodes; zero lost drafts, duplicate generations, unexplained errors or blocked primary actions; no essential control clipped in supported target modes. Capture completion/failure/assistance, not only satisfaction scores. These targets remain unmeasured.

## Next executable action / owner

**Owner:** local interface/runtime implementation maintainer on the operator's Linux Mint machine. **Dependency:** inspect actual known-good source checkout and running UI; no safe standalone Momus GitHub command can inspect the user's localhost environment.

After resolving the real checkout non-destructively, start with this command **inside that verified checkout** (not a guessed path):

```bash
git status --short && git remote -v && git branch --show-current && git rev-parse HEAD
```

Record the output and browser route in the existing Momus state/harness evidence (no credentials); use the proven application's own launcher to open its UI locally, then capture actual screenshots and complete `desktop_creator_journey`. **Expected artifact:** exact runtime-source identity and first browser trace. **Gate:** a real one-shot action and terminal outcome at that exact head; until then **NOT CERTIFIED**.

Do not represent this design/gate implementation as a live production launch.
