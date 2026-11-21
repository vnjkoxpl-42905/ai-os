# Host dispositions after first resumed review

NRT-2 accepted. The hook synchronizes same-key geometry, observes the real stage and rail, refreshes idle baselines, and coordinates a late permission rail without replaying reader content. Tests cover an in-place rail then note entry and delayed rail insertion, including reduced motion.

NRT-3 modified and implemented. Suppression is now scoped to data-note-transition-active, removed on completion/reset. The archive prelayout geometry/transform exception remains intentional to preserve child anchor measurement and is explicit in the revised plan. It does not create a new archive tween.

NRT-5 accepted. Interactive NOTE_TYPES iframe content exposes the same confirmed reader and block boundaries. Existing sandbox, srcDoc, sizing, controls and Back behavior are retained. The reader/journey tests pass and the fixture includes an interactive note.

NRT-1 and NRT-4 rejected as unsupported causal claims in the inspected source: play() returns immediately when expectedId is absent, so non-item destinations and archive Back cannot acquire the alleged stage tween. New regressions prove flagged-to-review creates zero timelines and rapid archive reopen retains full stage displacement. Please reassess these against the current guard and tests rather than presuming they are fixed by a new route guard.

The plan now includes late/in-place rail readiness, interactive notes, validated archive origin through sidebar selections, and the explicit archive prelayout exception. The original approved remediation plan is unchanged and remains required for the broader source inspection.

Host proof so far: real fixture normal desktop entrance has intermediate stage positions and crisp stagger, phone390 has no overflow/desktop rail, reduced motion is immediately visible, and A-to-B-to-Back focuses original A. Read count fixture updates immutably. Tests are mocked for GSAP; natural playback is separate evidence in this directory. Final expanded rerun/build and fresh source inspection are still required. No commit, push, merge or publish.
