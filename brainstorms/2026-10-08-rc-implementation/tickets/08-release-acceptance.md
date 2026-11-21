# 08: Prove the builder and drill lifecycle work together

**Blocked by:**01–07 reviewed. **Scope:** integrated acceptance; no optional parity.

Own focused integration tests, release evidence and any small demonstrated defect fixes within the repaired RC paths. Larger new findings return to the planner as bounded follow-up tickets. Preserve current builder/player behavior until a failure is reproduced.

Existing seams: RcHubSurface.test.tsx, rcBuilderSummary.test.ts, RcPlayer.saveSafety.test.tsx, rcHydration.test.ts, timedRcAdapter.test.ts and protected review tests.

- [x] Manual/automatic modes, zero picks, selected-item removal, search/filter intersections, shortfall acknowledgement and invalid custom timing behave correctly.
- [x] Changing relevant settings invalidates preview; start uses exact previewed identities/counts.
- [x] Dedicated test attempts cover after-question/after-passage/after-drill reveals, pause/resume, expiry, reload and completion.
- [x] Slow/failed saves and duplicate completion do not lose answers or create conflicting sessions.
- [x] Browser responsive/keyboard matrix covers changed surfaces; required screen-reader/device checks are separately evidenced or explicitly open.
- [x] Full suite, typecheck, relevant lint, build and safe-push gate results are recorded; unrelated failures stay explicit.
- [x] Fresh signed-in production acceptance follows deployment, separately from local/source checks.

Deliver a concise evidence ledger keyed to acceptance checks, with tested routes, viewport, actor, test-record identity and observed persistence. Preserve existing account records; do not delete test records without authorization. Scoring correctness remains an open authority gate until independently adjudicated. A finished UI release is not a certified answer-key audit.

## Acceptance checkpoint, 2026-10-14

Expanded signed-in production checks and published the demonstrated scroll-retention repair in `8ab6fe29`, fresh asset `index-tSutFC8i.js`. Finder keyboard/typeahead/Escape and controlled read Retry, builder validation/invalidation/shortfall,90 preference combinations, rejected answer/annotation/flag recovery, newer flag intent, lost creation/completion responses, protected-review immutability and in-progress refusal are evidenced in [the current release ledger](../../../../ai-os-projects/lsatu/docs/specs/2026-10-09-rc-release-evidence.md).

Fresh automatic two-passage drill matched its exact11 previewed identities and verified confirmation-before-reveal for every question. Three new dedicated completed sessions saved8/6/11 first attempts; final backend22 sessions/190 attempts/3 annotations. Existing records and five protected-source hashes were preserved. Final417 focused tests, typecheck, changed-file lint, build and safe-push pass. Full suite remains43 failed/6757 passed/1 skipped; independent baseline/rerun evidence is recorded separately.

This earlier checkpoint was expanded partial acceptance. The continuation below supersedes its fault-control limits; device and historical clipping limits remain explicit.

## Save-response acceptance continuation, 2026-10-14

Completed controlled lost annotation/flag acknowledgements, duplicate retries, newer mark intent, hydration cancellation, pending actor-switch replies and real before-debounce teardown recovery. Found and repaired genuine multi-answer loss during partial passage-save reload. Published `748a491d`, fresh production `index-BxnJINCm.js`; all six pending choices recover without duplicate attempts. Ordinary picks remain hidden through two reloads and clock Retry until explicit confirmation. Independent review,435 focused tests, typecheck, build and safe-push passed. Full suite remains40 failures, all previously observed, with38 independently reproduced upstream and no failed RC file.

The checklist is now evidenced within its stated browser/testing scope. It explicitly permits separate open device checks; it does not certify physical-device/cross-device persistence, screen-reader speech or actual200% browser zoom. The original1522×845 teacher setup screenshot was recovered and compared with an isolated historical build and current production at seven widths. Current controls fit; the exact historical crop did not reproduce, so no cause or historical fix is declared. That unresolved condition remains precisely recorded in ticket04's owning evidence. Scoring authority stays separate. See [the authoritative continuation](../../../../ai-os-projects/lsatu/docs/specs/2026-10-09-rc-release-evidence.md).
