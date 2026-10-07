# Conditional opening: three revision passes and proof

Date: 2026-10-03. Local development only. Three revision passes and local verification completed. Fresh Claude inspection remains blocked by the account session limit; no independent Claude approval is claimed.

## Build and source evidence

- Implementation worker requested `gpt-6-astra`; teaching/research reviewer also requested `gpt-6-astra` through native collaboration tools.
- Checkout: `C:/Users/Joshu/dev/ai-os-projects/lsatu-conditional-bootcamp`.
- HEAD reported and verified by builder: `67230dfae74a1466515d570fcb7b8a96ab5cb9c5`. Existing dirty state preserved. No pre-edit hash inventory was captured in this turn; do not claim a fresh byte-for-byte before/after comparison from it.
- Two Demon transcripts preserved with verified SHA-256 by ingest worker. Source summaries: `wiki/sources/lsat-demon-sufficient-necessary.md` and `wiki/sources/lsat-demon-abstract-conditionals.md`. Neither clip contains embedded screenshots. No video playback claimed.
- Intro to LR comparison: actual route and source inspected. Browser route displayed **Not assigned yet**. The reference lesson itself was not visually inspected or assigned to bypass the gate.

## Pass 1: teaching and retention

Independent Astra review after initial implementation. Full findings and learning-science sources are in `2026-10-03-astra-learning-review.md`.

Findings sent to builder:

- A Group 2 card changed a switching-on event into a being-on state, invalidating its inference. Match the rule's event/state wording.
- Remove teacher difficulty/timing policy from the student FAQ.
- Subdivide the long first-diagram and six-exercise stages without removing their content or changing their order.
- Preserve the reference-sequence CSS ancestor lost during pagination, including its reduced-motion rules.

Disposition: corrected and rechecked by the independent Astra teaching reviewer. The inherited card defect is privately documented in `indicatorFlashcards.ts`; the immutable input remains unchanged. Foundation recall now follows notation. Stage 8 has three subpages and stage 13 has six. Repeated ticket exercises were removed from supplementary units, a Group 1/2 wording comparison was added, and an original negative-condition exercise follows the symbolic prerequisite. The final sequence has 26 orientation pages, 9 sufficient/necessary pages, 17 Group 1 pages and 18 Group 2 pages. All 13 core orientation stages remain in order.

## Pass 2: visual design

Actual IAB preview inspected at 1190, 768, 500 and 320 CSS-pixel widths during initial build.

Findings sent to builder:

- Small-phone card text was constrained by nested padding. Reduce mobile gutters and card padding while retaining readable type.
- Page turns scrolled to the heading but clipped the numbered stage label above it. Keep the section identity visible while focusing the heading.
- A paragraph following the Group 2 reasoning-reveal panel needed more separation.

Observed working: editorial paper/mint presentation, ticket counterexample composition, distinct card front/back, destination-named navigation. No horizontal document overflow in measured 320 and 500 widths. These measurements predate final revisions and will be repeated.

Disposition: mobile padding reduced and visually rechecked; section-start scrolling keeps stage identity with the focused heading; reveal spacing corrected. Heading outlines use focus-visible so pointer page turns do not look like an editor selection. The reference-sequence ancestor was restored. New stylesheet formatted for review. Final responsive results below supersede initial measurements.

## Pass 3: interaction and accessibility

Early browser checks established:

- Next and Back preserve an attempted sufficient-condition answer and its reasoning.
- Page navigation focuses the current heading; one reading panel is visible.
- Space flips a recall card; Enter flips it back. Card navigation resets the answer side. Revisit marking exposes a return-to-saved-card control.
- A ticket inside Drawer R without a blue border receives an explanation that it violates the original rule. A blue-bordered ticket outside Drawer R receives an explanation that it is permitted by the original and disproves the reverse.
- Unit change resets to page 1.
- Group 2 `must` teaches an obligation without inferring compliance. Its reveal button has matching question description, controlled region and expanded state.

Final pass completed after app freeze:

- Swept all 70 reading pages at each of 320, 500, 768 and 1190 CSS-pixel widths. No horizontal document overflow; exactly one reading panel visible. The initial 500px orientation sweep began mid-lesson and was explicitly rerun from page 1; the saved report contains the completed 26-page sweep.
- At 320px, completion was absent on every nonfinal page and present at each unit's end. No completion button was clicked in the real browser.
- Rechecked keyboard operation and actual wrong/correct states in the negative-condition exercise. Both film/no-workshop and no-film/no-workshop satisfy the rule and given fact. Selecting a workshop conflicts with the given fact. The subsequent workshop-present fact correctly rules out a film.
- Verified `aria-describedby`, `aria-controls`, and expanded state for Group 2 reasoning reveals; the must lesson preserves obligation rather than compliance.
- Emulated system reduced motion and verified computed animation `none` and transition `0s` on the visible page and hero. `document.getAnimations()` was unavailable in the browser's read-only evaluation surface, so no global animation enumeration is claimed. Media emulation was restored.
- All temporary viewport overrides reset. The local preview is left open on the embedded foundation deck.
- No browser proof is claimed for authenticated progress persistence or production.

Evidence directory: `visual-proof/astra-opening/`. Saved sweeps: `desktop-page-sweep.json`, `phone-page-sweep.json`, `mid-docked-page-sweeps.json`. Screenshots: `desktop-flashcard.jpg`, `desktop-counterexample.jpg`, `phone-flashcard.jpg`, `negative-cases-tablet.jpg`.

## Automated checks and independent Claude inspection

Host verification:

- `npm run test -- src/bootcamps/conditionals src/lib/conditionalBootcampAssignment.test.ts src/components/teacher/ConditionalAssignmentFields.test.tsx`: final **182/182 tests, 11/11 files passed**, exit 0, 13.50s. Exact output: `visual-proof/astra-opening/host-tests.log`.
- The first broader run had 9 failures in legacy tests that assumed every lesson control was visible at once. The builder updated `ConditionalLessonNote.test.tsx` and `routes.test.tsx` to navigate actual pages, retaining assignment/progress/completion assertions. No hidden-element workaround was used. The final run above passed.
- Host `npm run typecheck`: exit 0. Builder also ran typecheck successfully.
- Host direct Vite build: exit 0, **7150 modules, 1m7s**. Existing warnings include Browserslist age, ambiguous Tailwind classes, unresolved `/noise.png` at build time and large chunks. No prebuild bank/finder generator ran.
- Host canonical exclusion: exit 0, **771 dist files scanned**, no canonical guide content present.
- Builder and host scoped lint: **0 errors, 9 Fast Refresh warnings**, exit 0. Host covered all changed/new TypeScript implementation and regression-test files. No lint-clean claim for the whole repository.
- New interaction acceptance file: 5 tests passed, covering focus, hidden pages, retained answers/cards, end-only completion, unit reset and the negative exercise.
- Final preservation audit: **31 protected files match frozen hashes**, 32/40 total unchanged, eight authorized manifest revisions and six new files. All 30 units and 296 recorded questions preserved. This is a comparison to the older frozen input, not proof of every unrelated dirty file at this turn's start.

Claude inspection attempts:

1. `claude-astra-opening-inspection/claudex-fa7barsq/result.json`: failed before launch because the runner rejected the npm command wrapper.
2. Located native executable from the earlier verified command record, verified **Claude Code 2.1.280**, and retried with explicit `--cli` under the same safe-mode/read-only tool constraints. `claude-astra-opening-inspection/claudex-h4ny6scs/result.json`: API **429**, session limit, reset **2026-10-03 08:10 America/Toronto**. Zero model input/output tokens, no inspection verdict, no observed model identity. The trust warning about ignored project entries was present, but the actual blocking result was the session limit. No trust or permissions were changed.

There were two launch attempts and zero completed inspection rounds. No model/provider fallback and no fresh Claude approval. The earlier handoff's approval does not cover these revisions. The specification's outcome paragraph was updated after the failed attempts to record final host checks and the limit; the failed-run plan hashes therefore describe the earlier spec text. Application files remained frozen. The final implementation is locally verified and ready for a new read-only inspection when the account is available.

## Publication boundary

No commit, push, deployment, assignment or backend writes performed. Production and authenticated student persistence are not established by this preview proof.


## 2026-10-04: Dedicated course structure implemented locally

The prior 70-page reference-reader approach is superseded for the opening course entry. The local course now mirrors the actual Intro to LR course structure: Lessons/Practice Drills/Drill Lab/Flashcards sidebar, vertical note/drill cards, nine dedicated notes and four interleaved labs. Definitions of conditional, sufficient and necessary each have their own lesson. Four labs have separate entry and run surfaces; all 25 cards and complete expression coverage remain.

Three review passes completed:

1. Teaching and content: checked prerequisites, grouped repeated material, retained all core and supplementary expressions, repaired stale transitions and required checked attempts before advancing paired exercises. Removed student-facing progress-accounting prose.
2. Independent routing review: repaired the primary Begin lesson entry, explicit assignment source-unit mappings and query preservation. No implicit legacy completion writes. Legacy routes and recorded banks remain.
3. Parent browser review: traversed 21 screens at 320/500/768/1190 CSS pixels (84 measurements), with no horizontal document overflow. Verified wrong/correct feedback, retry, checked-attempt gates, retained answers across Next/Previous, and mobile drawer selection/Escape focus. Repaired destination heading focus. Original old-query preview now opens the new course index.

Final automated checks after source freeze: 146 tests across seven files passed; typecheck passed; scoped new-file lint passed with no output; direct Vite build passed (7,154 modules, 57.01 seconds); canonical exclusion passed across 771 files. Logs: visual-proof/astra-opening/course-tests.log, course-typecheck.log, course-lint.log and course-build.log. Browser evidence: course-responsive-measurements.json, course-index-desktop.png and course-index-phone.png in that directory.

New app files: openingCoursePath.ts, OpeningCourse.tsx, OpeningCourseContent.tsx, OpeningCourse.test.tsx and opening-course.css. Modified routing/tests, opening/reference component exports and optional check callback, and ConditionalOpeningPreview.tsx. No bank, progress-schema, assignment implementation or generated-content edits in this correction. Session-local course answers are not recorded assessment completion. Authenticated student persistence and production remain unverified. No commit, push, deployment, backend write or paid action. Fresh Claude inspection remains pending from the previously failed run; no new approval claimed. Temporary browser tab closed; user preview and live IntroLR tabs retained, viewport restored. Task statuses unchanged.
