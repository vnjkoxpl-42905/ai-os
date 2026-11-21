# Plan review log: Famous Flaws note

Append-only.

## Setup (2026-11-14)

- Host: Claude Code. Planner and coordinator: Claude. Reviewer: Codex. Builder (if approved): Codex. Inspector: fresh session of the other provider.
- Requested model: `gpt-6-astra`, effort `high` (from "use 6 astra"). Codex CLI 0.167.0.
- Plan: `brainstorms/2026-11-11-ore-post-session/PLAN-famous-flaws.md`. Round limit 5, fix rounds 2.
- Scope authorized: plan only. Building is not authorized yet.
- Review ran on an isolated curriculum-only pack (the plan, the compiled catalog, the design artifact, the app's `flaws.ts`). No student records were included. The plan text names no student.

## Round 1

- Result: **BLOCKED**, not approved. Plan SHA256 `2b2126a17f36f460b7b41fa75cfdbf0a63071d77877fb79a26fc692223bf7587`.
- Cause: operational. Codex's read-only shell could not start inside its sandbox (`CryptUnprotectData failed: 2148073483`), twice, so it could not read any file. It reviewed only the plan text in its prompt.
- Findings: none. A BLOCKED verdict with no findings is not evidence that the plan is sound.
- Coverage actually achieved: the plan text only. Not inspected: the compiled catalog, the design artifact, the shell, `flaws.ts`, the validator.
- Effective settings read back: model `gpt-6-astra`, effort `high`, sandbox `read-only`.
- Artifacts: `scratchpad/review-artifacts/claudex-v2gtmct6/` (outside the checkout).
- Disposition: no plan change. No retry yet: a blind retry would likely hit the same sandbox error.

## Status

Plan is **unreviewed**. Building through Codex may hit the same sandbox error. Next step needs Joshua's choice: fix the Codex sandbox and re-review, or proceed on the recorded unreviewed path.

## Build attempts (2026-11-14), builder Codex, model gpt-6-astra, effort high, unreviewed spec

The owner chose to build although the plan review was BLOCKED. Plan SHA256 `7ce7e813bac2cb316a8928e18dfcd837eb888896981d69e660ed2bf348336ce1`. Baseline commit `71259a2` in an isolated checkout with curriculum inputs only (no student records). Pre-build files changed: none, on every attempt.

| Attempt | Setup | Result |
|---|---|---|
| 1 | Installed runner, checkout in the scratchpad (Temp) | Stopped after 26 s. Shell could not start: `CryptUnprotectData failed: 2148073483`. No files changed. |
| Probe | `codex sandbox` with `-c windows.sandbox="unelevated"` started a shell; `"elevated"` (the configured mode) failed with the same CryptUnprotectData error | Cause for attempt 1: the elevated Windows sandbox cannot decrypt its stored credentials from this context. |
| 2 | Copy of the runner with a per-run `windows.sandbox="unelevated"` override (copy at `scratchpad/runner-unelevated.py`; installed runner and `~/.codex/config.toml` untouched), checkout in the scratchpad | Stopped after 37 s. `CreateProcessAsUserW failed: 5 (Access is denied.)`. No files changed. |
| 3 | Same patched runner, checkout moved to `C:\Users\Joshu\dev\famous-flaws-build` | Stopped after 22 s. Same `CreateProcessAsUserW failed: 5`. No files changed. |

Conclusion: not a folder-permission problem. The Codex Windows sandbox cannot launch processes from this Claude session context in either mode. No retries beyond this. Nothing was built; no inspection was possible.

Deviation recorded: the unelevated override in attempts 2 and 3 is a weaker sandbox than the configured one.

## Codex sandbox root cause and fix (2026-11-14)

- `~/.codex/.sandbox/` logs: the Codex desktop app ran with sandbox selection `mxc` on 2026-11-13 without errors. The CLI used `elevated` (from `[windows] sandbox = "elevated"` in `~/.codex/config.toml`), whose stored account credentials cannot be decrypted from this Claude session (`CryptUnprotectData` 0x8009000B, NTE_BAD_KEY_STATE). `unelevated` failed differently: `CreateProcessAsUserW failed: 5`. The process has no package identity (`GetCurrentPackageFullName` returned 15700) and runs at medium integrity with a filtered admin token.
- Probe: `codex exec -s workspace-write -c windows.sandbox="mxc"` ran a shell command successfully.
- Fix applied per run only: a copy of the runner, `scratchpad/runner-mxc.py`, adds `-c windows.sandbox="mxc"`. The installed runner and `~/.codex/config.toml` are untouched. Permanent option for the owner: set `[windows] sandbox = "mxc"` in `~/.codex/config.toml`.

## Plan review rounds with the fixed Codex (reviewer gpt-6-astra, effort high, sandbox read-only)

| Round | Verdict | Findings and dispositions |
|---|---|---|
| 2 | REVISE | FF-001 (high): only 11 of 15 entries have a What-if counter in the source. Accepted, verified. FF-002 (medium): coverage must be block-level, not string counts. Accepted. FF-003 (medium): the Internal Contradiction canonical example is arguable. Kept verbatim and flagged to the owner. |
| 3 | REVISE | FF-002 remainder: validate each adaptation rule by rule. Accepted: the verifier owns a closed table of permitted changes. |
| 4 | REVISE | FF-004 (medium): two R2 spans used "section 5" instead of the source's literal section sign. Accepted, all five spans checked verbatim. |
| 5 | **APPROVED** | Plan SHA256 `2a5fc9b1c74de29dcd077b4aea637200673b342b73e9e2570f8c1f1ea8b66389`. FF-003 remains an owner-flagged risk. |

Reviews ran on an isolated curriculum-only copy (`famous-flaws-review`). The build folder holds the same plan bytes (same SHA256).

## Build (builder: Claude, authorized by the owner on 2026-11-14)

The Codex builder never ran (sandbox, above). After the fix the owner asked Claude to build. Built in `C:\Users\Joshu\dev\famous-flaws-build` (baseline commit `71259a2`) to `PLAN.md`: `build-famous-flaws-full.py`, `make-svgs.py`, `out/famous-flaws.layer.{css,js}`, `out/extras.json`, `verify-all.mjs`, `verify-browser.mjs`.

Proof run by Claude: `py -I build-famous-flaws-full.py && node verify-all.mjs` gives 34/34. `node verify-browser.mjs` gives 34/34 (1280 px and 375 px). Output 380 KB, validator passes.

Claude-only step: `finish-for-student.py` fills the session slots in the vault copy. It was not sent to Codex.

## Inspection of the neutral build

- Attempt 1 (06:3x): FAILED, not a verdict. Codex returned "You've hit your usage limit ... try again at 6:41 AM" after 104 s (`turn.failed`), before producing a result. No findings, no coverage. Not counted as approval. One scheduled retry after the reset time, same model and effort, fresh session; no provider switch.

- Attempt 2 (after the 6:41 reset): completed, 363 s, gpt-6-astra, effort high, sandbox read-only, 28 files inspected. Verdict **REVISE**, nine findings. Dispositions (Claude, builder):

| Finding | Severity | Disposition |
|---|---|---|
| FF-001 my Internal Contradiction check was not a strict contradiction | high | Accepted. Replaced with "every employee finished the training" versus "three never finished it". Canonical example still preserved verbatim and owner-flagged. |
| FF-002 matrix row 9 "license" is not a shift of meaning | medium | Accepted. Replaced with "light" (low weight versus pale colour) inside a correctly applied rule. |
| FF-003 verifier counted text inside hidden elements and SVG metadata | medium | Accepted. Structural visible-text walker; two self-tests prove a hidden definition and an SVG desc are not counted. |
| FF-004 verifier did not require the R7 records or one R6 record per flaw | medium | Accepted. It now builds the complete expected manifest and compares exact entries and multiplicities. |
| FF-005 Secret Downsides label clipped | medium | Accepted, and widened: a bounds check on every SVG label found two more overflows (Internal Contradiction, Equivocation) and a third (Inappropriate Appeal). All fixed. |
| FF-006 panels emitted class fx-session, not session-slot | low | Accepted. Both classes emitted; verifier and browser test check the contract. |
| FF-007 empty next-steps slot showed its marker | low | Accepted. The layer hides that section and its rail link while unfilled; browser test added. |
| FF-008 Equivocation SVG description reversed the senses | low | Accepted. Description corrected. |
| FF-009 Elvis left in an example | low | Accepted. Two new R4 adaptations; added to the verifier-owned table. |

Re-proof after fixes: `verify-all.mjs` 40/40, `verify-browser.mjs` 38/38. Fresh Codex re-inspection follows (inspection round 2 of 2).

- Attempt 3 (fresh session, gpt-6-astra, effort high, read-only, 318 s): verdict **REVISE**, four findings. Inspection budget (initial plus one after fixes) is now used. Dispositions:

| Finding | Severity | Disposition |
|---|---|---|
| FF-R01 hiding the empty next-steps section moved the rail marker to the hidden link (the shell counts hidden sections) | medium | Accepted, real bug. The layer recomputes the marker among visible sections after the shell's handler; browser test added and passes (marker rests on part-6 with next steps hidden). |
| FF-R02 Part vs. Whole example (small budget, small projects) did not cleanly isolate the flaw | medium | Accepted. Replaced with "the committee reached a wise decision, so every member must be wise". |
| FF-R03 the verifier's normaliser dropped symbols and digits (not-equal sign, 99.9%) | medium | Accepted. Exact comparison (case, whitespace, quote style only); inline tags no longer insert spaces; labels compared separately. Two self-tests prove "≠ to =" and "99.9% to 999%" are caught. |
| FF-R04 a stylesheet rule could hide canonical text and still pass static coverage | medium | Accepted. Static CSS audit with an allow-list (and a self-test that an injected hide rule is caught) plus a browser check that all 417 canonical elements render with the panels open. |

Final proof run by Claude after these fixes: `verify-all.mjs` 44/44, `verify-browser.mjs` 41/41 (1280 px and 375 px). Output 382 KB.

**Unreviewed by Codex:** everything changed after inspection attempt 3 (the four fixes above, the two new verifier self-tests, the CSS audit, the rail handler, the new Part vs. Whole example). The inspection budget was spent, so no fresh Codex session has seen these edits. The slot-filling step (`finish-for-student.py`) was never shown to Codex by design.

Status: plan APPROVED by Codex (round 5). Build inspected twice by Codex, both REVISE, all findings accepted and fixed. Final edits not re-inspected.

- Attempt 4 (extra round authorized by the owner, 07:1x): FAILED, not a verdict. Codex returned "You've hit your usage limit ... try again at 11:44 AM" after 185 s, having read files but produced no result. No findings, no coverage. Not counted as approval. No provider switch. The final fixes (rail handler, committee example, exact-comparison verifier, CSS audit, browser render check) remain un-inspected by Codex. Retry possible after 11:44 AM, same model and effort, fresh session.
