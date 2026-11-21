# Coordinated reader transition: local verification

Status on 2026-10-28: COMPLETE locally. Claude Opus 5.5 Medium's fresh expanded inspection `claudex-88z3wz0e/result.json` returned APPROVED with an empty findings array. No commit, push, merge or publication.

## Final verification

254 tests across13 suites passed with exit0 and no unhandled errors. Typecheck, full production build, fixture build and scoped diff check passed. `final-snapshot-proof.json` verifies every inspected file hash still matches and the unrelated backend hash is unchanged. Current plan SHA256 is17eaea83d33432e97f473ad60785abd4a955ef6fb60a49438423d2ef26f62a37. No source edits followed inspection.

The local note-opening jump is replaced by coordinated GSAP stage travel, secondary rail reveal and crisp staggered reader blocks. Charcoal/off-white styling is preserved. Back, native history, original archive focus/position, note switching, unknown/non-note items, interactive lessons, reduced motion, rapid cleanup and delayed scrollbar behavior have focused regressions. Real fixture traces verify normal and delayed natural playback; the delayed trace directly captures a classic scrollbar appearing while the stagger remains active.

Limits: Claude's sign-off is source inspection of the declared scope. It did not run tests or view the host screenshots/traces. Host runtime proof uses synthetic data and the real rail/stage components, not the full authenticated production shell. Production persistence/RLS, physical phones and Safari were not certified. Existing build warnings remain. Several screenshots have capture calibration margins/cropping and are explicitly diagnostic; readable historical desktop and calibrated phone evidence are retained. All browser overrides and instrumentation were reset.

## Earlier correction pass

All findings from completed review rounds have been implemented, including Space and Shift+Space as page scroll on ordinary links, note-only shell ownership, same-key layout-read gating, late-mounted root initialization, interactive iframe notes, same-ID stale anchor protection and removal of unused markers/import duplication. The broad regression run now passes all 252 tests across 13 suites with exit code 0 and no unhandled errors (`.taste-skill/note-reader-final-tests-clean.log` in the app checkout).

The earlier teardown error was captured precisely: ScrollTrigger's application-lifetime `_sync` interval fired after jsdom teardown. Test-only `afterAll(ScrollTrigger.disable)` in the Layout and refetch suites clears that service. Product hook cleanup remains scoped; there is no production global disable or error suppression.

Latest natural playback is `local-desktop-owned-final-trace.json`: 24 sampled intermediate stage positions, final left600/activefalse, all five reader blocks opacity1 and transformnone. Final Space-scroll plus pointer Load more remains usable with16 rows and no horizontal overflow. Current phone/reduced checks in `local-phone-reduced-final.json` show390px width, hidden desktop rail, no overflow and all blocks immediately visible. Browser overrides and instrumentation were reset. A later `fromSurface:false` screenshot captured app chrome and is diagnostic only; do not use it as page evidence. The calibrated phone screenshot shows the complete readable page viewport with blank capture margins.

Historical expanded inspection `claudex-b5d7tzg6` completed with one remaining scrollbar finding. Its correction is covered by the final inspection above.

The real delayed-reader fixture proves that correction in `local-delayed-reader-final-trace.json`: window width stays1441px, stage width changes841.194→818.507px when the classic scrollbar appears, and the reader remains active with intermediate opacity on that frame and the next. There are33 intermediate-opacity frames; the final frame has every block opacity1/transformnone. This directly exercises short loading→long note, unlike the earlier always-long archive trace. Instrumentation and viewport overrides were removed afterward.

The live stage previously moved from left 280px to 600px in one sampled frame. The local GSAP sequence now coordinates stage travel, secondary rail and crisp reader blocks. The first desktop natural-playback trace in `local-desktop-open-first.json` records intermediate positions 449, 577, 599, then 600px, with all owned styles cleared at rest.

The latest real-rail fixture verifies archive A to sidebar B to Back focuses A's archive link. Its synthetic unread count updates from 3 to 2 after opening A. At 390px the rail has zero width, no horizontal overflow, and reader blocks stagger. Reduced motion yields immediate opacity 1 and transform none on every reader block. `local-reader-phone-final.png` was opened and is readable. A later desktop CDP screenshot was clipped by screenshot/zoom calibration; do not use it as full-width visual proof. The earlier readable desktop screenshot remains historical.

First expanded regression run: 230 of 231 tests passed, with one archive keyboard test timing out during a roughly two-hour machine pause. The full archive suite passed on rerun. Typecheck and production build passed. Build retains existing chunk-size, utility ambiguity and unresolved noise asset warnings. Fixture build passed. Backend file SHA256 remains 5359c2de7a28b626a3d2523d83b6fbd3e1777a0d5a60bb9757ed4bb2ee446f26.

Claude Opus 5.5 Medium resumed in `claudex-5avs8vtg/result.json`. It requested late-rail synchronization, narrower transition suppression, and interactive lesson note coverage. Those corrections and route-guard regression tests are in progress. No final independent approval yet. Reviewer did not inspect external rendered evidence in that round; synthetic fixture is not production authentication, RLS or persistent read-state acceptance. Physical phones and Safari remain unverified.
