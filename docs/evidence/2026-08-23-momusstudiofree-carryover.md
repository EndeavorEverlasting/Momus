# Evidence — MomusStudiofree / OpenCode Carryover

**Captured in source ledger:** 2026-08-23  
**Evidence type:** embedded browser and terminal screenshots in the Google Drive *AI Engineering Ledger*  
**Purpose:** preserve the handoff facts without treating a screenshot as stronger proof than it is.

## Browser evidence

The ledger contains a screenshot of the local waoowaoo sign-in page at:

`http://localhost:13000/en/auth/signin`

Visible facts:

- waoowaoo Beta v0.4.1
- username field populated with `sprint1-test`
- password field masked
- browser is on localhost

The password is intentionally not transcribed into this repository.

## OpenCode terminal evidence

The ledger contains an OpenCode terminal screenshot titled `waoowaoo launch: runtime, skit, docs plan`.

### Risks recorded in the screenshot

1. **LAN exposure:** published ports bind to `0.0.0.0`; the app, MySQL on `13306`, and a board surface can become network-reachable if the firewall allows it. The screenshot recommends binding `127.0.0.1:<port>:<port>` during a future hardening sprint and explicitly says not to expose publicly.
2. **Host proxy flakiness:** transient image-pull failures included `unexpected EOF` and later DNS `no such host` inside the Docker VM; retry recovered.
3. **Hardcoded Compose defaults:** DB password, `NEXTAUTH_SECRET`, and fixed `API_ENCRYPTION_KEY`; described as acceptable for localhost-only use and deferred to a hardening sprint.

### Blockers recorded

`None.`

### Proof ceiling recorded

- Panel 2 must prove generation/export.
- Panel 3 must prove reproducibility.

### Integration state recorded

`No integration lane required (zero tracked mutations expected and observed).`

### Next action recorded

The screenshot directs the operator to:

1. open `http://localhost:13000`;
2. sign in as `sprint1-test` using the password from a temporary local file;
3. enter **API Configuration**;
4. configure the minimum chain `text model -> image model -> video model` using provider keys entered in the UI only;
5. complete the gate of **three green connection checks**;
6. start Panel 2 with project **“The AI Intern Takes Corporate Speak Literally”**, **9:16**;
7. generate **one representative shot before batching**;
8. explicitly verify **audio presence**.

## Evidence limits

These screenshots show a captured local state, not a current runtime check performed by this repository bootstrap. P01 exists specifically to re-establish and prove the browser/runtime state before later sprints rely on it.
