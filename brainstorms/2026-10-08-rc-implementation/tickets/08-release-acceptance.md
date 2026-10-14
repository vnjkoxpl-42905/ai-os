# 08: Prove the builder and drill lifecycle work together

**Blocked by:**01–07 reviewed. **Scope:** integrated acceptance; no optional parity.

Own focused integration tests, release evidence and any small demonstrated defect fixes within the repaired RC paths. Larger new findings return to the planner as bounded follow-up tickets. Preserve current builder/player behavior until a failure is reproduced.

Existing seams: RcHubSurface.test.tsx, rcBuilderSummary.test.ts, RcPlayer.saveSafety.test.tsx, rcHydration.test.ts, timedRcAdapter.test.ts and protected review tests.

- [ ] Manual/automatic modes, zero picks, selected-item removal, search/filter intersections, shortfall acknowledgement and invalid custom timing behave correctly.
- [ ] Changing relevant settings invalidates preview; start uses exact previewed identities/counts.
- [ ] Dedicated test attempts cover after-question/after-passage/after-drill reveals, pause/resume, expiry, reload and completion.
- [ ] Slow/failed saves and duplicate completion do not lose answers or create conflicting sessions.
- [ ] Browser responsive/keyboard matrix covers changed surfaces; required screen-reader/device checks are separately evidenced or explicitly open.
- [ ] Full suite, typecheck, relevant lint, build and safe-push gate results are recorded; unrelated failures stay explicit.
- [ ] Fresh signed-in production acceptance follows deployment, separately from local/source checks.

Deliver a concise evidence ledger keyed to acceptance checks, with tested routes, viewport, actor, test-record identity and observed persistence. Preserve existing account records; do not delete test records without authorization. Scoring correctness remains an open authority gate until independently adjudicated. A finished UI release is not a certified answer-key audit.

## Acceptance checkpoint, 2026-10-14

Expanded signed-in production checks and published the demonstrated scroll-retention repair in `8ab6fe29`, fresh asset `index-tSutFC8i.js`. Finder keyboard/typeahead/Escape and controlled read Retry, builder validation/invalidation/shortfall,90 preference combinations, rejected answer/annotation/flag recovery, newer flag intent, lost creation/completion responses, protected-review immutability and in-progress refusal are evidenced in [the current release ledger](../../../../ai-os-projects/lsatu/docs/specs/2026-10-09-rc-release-evidence.md).

Fresh automatic two-passage drill matched its exact11 previewed identities and verified confirmation-before-reveal for every question. Three new dedicated completed sessions saved8/6/11 first attempts; final backend22 sessions/190 attempts/3 annotations. Existing records and five protected-source hashes were preserved. Final417 focused tests, typecheck, changed-file lint, build and safe-push pass. Full suite remains43 failed/6757 passed/1 skipped; independent baseline/rerun evidence is recorded separately.

This is expanded partial acceptance, not full ticket closure. Required actual200% browser zoom, physical-device/cross-device and screen-reader speech checks remain open, as do the unidentified original clipping condition and broader controlled delayed/lost/duplicate annotation, rapid-passage/teardown and pending-write actor-switch combinations. In-app raw-CDP continuation failed; its interceptors were cleared. Scoring authority remains separate. The unchecked checklist is retained until its complete contracts can be closed.
