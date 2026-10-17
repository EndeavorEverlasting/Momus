# Momus Codebase Map

Governance starts at root `AGENTS.md`. **Momus is the canonical product name and repo.** MomusStudio is its earlier name, not a separate product; consult the root contract before interpreting legacy references.

| Path | Role | How to validate or use |
|---|---|---|
| `AGENTS.md` | Product identity, precedence, agent governance | `python scripts/validate_governance.py --self-test` |
| `README.md` | Public project entrypoint and currently selected external creator path | Read before creator changes |
| `docs/AI_ENGINEERING_LEDGER.md` | Canonical engineering plan and historical evidence | `python scripts/validate_repo.py` |
| `docs/CURRENT_STATE.md` | Human-readable current proof and next actions | Check latest sections, verify against Git |
| `docs/SPRINTS.md` | Existing sprint IDs P00-P07, not the new governance/harness lane names | Check declared scope |
| `docs/evidence/` | Historical screenshots/source-provenance receipts | Never upgrade historical claim without fresh evidence |
| `creative/` | Creative intent packages and shot plans (JSON), **no media binaries** | `python scripts/validate_repo.py` |
| `harness/manifest.v1.json` | Agent navigation registry, proof gates, references | `python scripts/validate_harness.py` |
| `harness/context-workspace-adoption.v1.json` | Historical AgentSwitchboard adoption plus superseding unified product identity | `python scripts/validate_context_workspace.py` |
| `harness/paths.v1.json` | Canonical repo/machine-profile path discovery and provenance | `python scripts/validate_harness.py` |
| `harness/artifacts.v1.json` | Tracked artifact roles, generators, expected proof | `python scripts/validate_harness.py` |
| `harness/workflows.md` | Intake, validate, defect handling, handoff | Read in every writing sprint |
| `harness/skills/` | Scoped repeatable procedures | Use when trigger applies |
| `harness/operator-report.md` | Operator summary and current proof ceiling | Verify fresh before reliance |
| `scripts/validate_*.py` | Deterministic static validators; stdlib only | Run all three validators |
| `.github/workflows/validate.yml` | Exact-candidate hosted validation | Inspect checks on actual PR SHA |

## Known executables and runtime

No first-party Momus application executable, build command, production installer, or deployed server is proven inside this repository. `python scripts/validate_repo.py`, `python scripts/validate_context_workspace.py`, `python scripts/validate_governance.py --self-test`, and `python scripts/validate_harness.py --self-test` are **repository static validation**, not runtime certification.

Selected external creator path (not proof of installation): `SwarmUI -> ComfyUI -> Wan 2.2`. Historical waoowaoo UI: `http://localhost:13000` (unverified currently). Prototype media bridge is a separate archived local artifact, not yet integrated into Momus code.

## Repository evidence floor

Default branch `main`; prefer fresh GitHub remote refs, not remembered commits. Canonical development checkout and production/use paths on the operator's Linux Mint machine are **UNKNOWN** until physically inspected and recorded in `harness/paths.v1.json`. Do not invent `~/Momus` as if verified, clone repeatedly, or claim a successful merge means production was updated.
