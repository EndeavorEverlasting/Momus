# Local Creator Baseline Evidence — 2026-09-29

**Purpose:** record the external open-source generation baseline for Momus without copying an inference engine into this repository.

## Decision

Momus remains the creative-content/context management layer. It does not become the image/video inference engine.

For the immediate "create AI content now" lane, the preferred external baseline is:

`Momus creative package -> SwarmUI -> ComfyUI -> local model -> local output files`

Historical MomusStudiofree / waoowaoo evidence remains preserved as `REFERENCE_ONLY_UNMAPPED`, but its provenance gate does **not** block this independent local-creator baseline.

## Pinned public references

The following repository heads were observed on 2026-09-29 and are recorded as reference floors, not vendored dependencies:

| Role | Repository | Branch | Observed commit |
| --- | --- | --- | --- |
| creator-facing UI / workflow front end | `mcmonkeyprojects/SwarmUI` | `master` | `dde9cb8a718830d98a1ef43b5159bd357feadc2a` |
| local workflow / inference engine | `Comfy-Org/ComfyUI` | `master` | `ebd432a78af0607a4d72df386920362e8f6836ce` |
| local video model family reference | `Wan-Video/Wan2.2` | `main` | `1ea34ff48f87168174e12956e200b1d908b1c5ff` |

These pins prove only which upstream revisions were inspected. They do **not** prove local installation, hardware compatibility, model download, generation success, export success, or reproducibility on Patrick's machine.

## Mechanism boundary

- Momus owns premise, shot intent, prompt text, aspect ratio, references, requested output naming, and returned provenance metadata.
- SwarmUI / ComfyUI own generation workflow execution.
- Model weights remain outside Momus.
- Generated image/video binaries remain outside Git.
- Secrets, API keys, and credentials remain outside Git.
- A returned local output path may be recorded as evidence, but the binary itself should not be committed.

## First creative package

The first package is `creative/ai-intern/shot-001.json`.

It is intentionally runtime-agnostic. It can be mapped to SwarmUI/ComfyUI today and to another local creator runtime later without rewriting the creative intent.
