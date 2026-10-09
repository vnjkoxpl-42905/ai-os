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
