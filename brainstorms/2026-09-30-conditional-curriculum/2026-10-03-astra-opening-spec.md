# Make the conditional opening teach through pages and practice

## Current authorization and scope

Joshua requested GPT-6 Astra implementation on 2026-10-03, continuing the unfinished opening work order. This document supersedes the earlier Claude-only build routing. The current host coordinates native Astra workers. The earlier failed Claude build remains a failed result; its two isolated files are unverified references only.

Work locally in `C:/Users/Joshu/dev/ai-os-projects/lsatu-conditional-bootcamp`, preserving the existing dirty opening implementation and all unrelated changes. Do not import the older Git baseline over it. No commit, push, deployment, student assignment, backend write, paid media generation or Lovable spend is included in this local correction.

## Acceptance criteria

- Review the actual Intro to LR page progression and relevant notes. Use natural Next/Back reading pages, page position and revisitable contents. Preserve answers and card state when returning within the lesson. Reset state appropriately when changing units.
- Preserve the full approved 13-part HTML teaching skeleton, complete expression inventories, six paired-diagram exercises, modality boundaries, assignments/progress contracts and later units.
- Finish the opening orientation, sufficient/necessary, Group 1 and Group 2 reading experiences. Keep teacher-controlled assignments and difficulty out of student lesson controls.
- Ingest the newly clipped LSAT Demon conditional sources using the existing ingest workflow. Preserve sources and hashes, document transcript defects, adapt sound reasoning into original examples and meaningful practice. Do not import vendor persona, unsupported prevalence claims or source mistakes.
- Embed the reviewed foundation/Group 1/Group 2 flashcards after their prerequisites. Cards flip in both directions with click and keyboard, have clear position and previous/next controls, conceal answers from assistive technology until revealed, and reset the revealed face when moving to another card.
- Use creative practice beyond blank filling, including constructing or testing counterexamples, interpreting complete conditions and comparing what follows with what remains open. Explain wrong and correct choices.
- Apply the full `references/lsat-teaching-voice-standard.md`, `wiki/teaching-voice.md`, and `wiki/COPY-CORRECTIONS.md`. Review all opening prose for novice prerequisites, complete intermediate reasoning, natural cadence and logical strength.
- Carry all five accepted earlier findings into the build: obligation wording for must; natural always prompting and controlled subject contrast; remove dead motion-control CSS but preserve system reduced motion; remove unreachable older Fundamentals orientation; associate repeated reasoning-reveal controls with their question.
- Preserve editorial paper/mint styling while improving hierarchy, purposeful visuals, responsive composition and restrained motion. Interactions must remain readable and operable without animation.
- Keep explicit lesson-read completion at the end. Page navigation and formative practice must not silently count as assessed mastery.

## Three post-build revision passes

1. Teaching and retention: check conceptual order, fresh practice, feedback, retrieval opportunities and source adaptation. Use bounded primary learning-science evidence; do not promise measured retention improvements.
2. Visual design: inspect the running pages, revise concrete hierarchy/spacing/contrast/composition problems, and check narrow, medium, wide and docked layouts.
3. Interaction and accessibility: exercise navigation, back-state retention, cards, correct/wrong/retry states, keyboard/focus, hidden-page exposure and reduced motion. Repair findings and rerun affected checks.

These are actual reviews after an initial implementation, with findings and dispositions recorded. A checklist or three unchanged screenshots does not count as three iterations.

## Independent verification and inspection

Run meaningful opening/reference/card/pagination and preservation tests, typecheck, scoped lint, direct Vite build without bank/finder prebuild generation, and canonical-content exclusion. Verify the actual local UI and preserve screenshots/measurements. Production and authenticated persistence remain outside this local preview proof.

After revisions, obtain fresh read-only Claude inspection through the installed claudex runner, host=codex, builder=codex. Use configured Claude model unless explicitly changed by Joshua. At most two inspection rounds and two fix rounds. Record actual verdict, coverage, limitations, observed model and snapshot. A failed or blocked run is not approval. Earlier approval does not cover these new changes.

## Inputs

- `2026-10-03-claude-pages-build-spec.md`: earlier substantive acceptance criteria, not current provider/worktree routing.
- `2026-10-02-opening-lessons-source-map.md`: approved skeleton and source supplements.
- `notebooklm-opening-assets/2026-10-03-indicator-flashcards-reviewed.json`: reviewed 25-card source.
- Canonical voice files named above.
- Newly preserved Demon source summaries and archives, resolved by the ingest worker.

## Implemented state for final inspection

The implemented opening has 26 orientation reading pages, 9 sufficient/necessary pages, 17 Group 1 pages and 18 Group 2 pages. The 13 core orientation stages remain ordered; long stage 8 has three subpages, and all six stage 13 exercises have individual pages. There are 25 adapted cards. Foundation retrieval follows notation, and the two Demon-informed exercises separately test a concrete counterexample and two possibilities under a negative requirement. Group 2 adds mixed wording discrimination.

This turn changed `ConditionalOpeningLesson.tsx`, `ConditionalReferenceSequence.tsx`, `ConditionalOpeningLesson.review.test.tsx`, `opening.css`, `opening-polish.css`, `reference-sequence.css`, plus the existing `ConditionalLessonNote.test.tsx` and `routes.test.tsx` to navigate the actual paginated experience. New files are `LessonPages.tsx`, `StudyDeck.tsx`, `CounterexampleLab.tsx` (also contains NegativeCaseLab), `lesson-pages.css`, `content/indicatorFlashcards.ts`, and `LessonPages.test.tsx`, all under the conditional bootcamp. Inspect the added files directly.

The Git baseline is older than this task's initial dirty state. Other manifest entries, especially public generated question-bank/finder data, MCP/backend code, assignment and progress wiring, were pre-existing changes and are outside this turn's authoring scope. The preservation audit compares protected files with the older frozen input; it is not an exact turn-start snapshot. Report inspection coverage and this limitation explicitly rather than implying the full dirty checkout was newly authored or approved here.

The actual three-pass record is `2026-10-03-astra-iteration-proof.md`. The teaching review is `2026-10-03-astra-learning-review.md`; preservation evidence is `2026-10-03-astra-preservation-audit.md`. Host build passed (7150 modules), canonical-content exclusion passed (771 files), typecheck passed and all 182 tests across 11 files passed. Old tests that assumed all lesson sections were simultaneously visible now navigate the actual pages while retaining their contract assertions. All 70 pages were swept at 320/500/768/1190 CSS pixels without horizontal document overflow. Fresh Claude inspection could not run because of an API 429 session-limit response, reset 2026-10-03 08:10 America/Toronto. No fresh independent Claude approval is claimed; the exact failed runs and bounded proof are recorded in the iteration record.

## 2026-10-04 correction: use Intro to LR's sidebar page structure

Joshua rejected the expandable two-column Lesson pages grid above the reading. His screenshot and instruction require the actual Intro to LR sidebar/page model across the opening: ordered numbered rail beside the active page, clear current position, persistent Next/Back, and compact narrow-screen navigation. Existing 70-page teaching, approved raffle example, flashcard state and answers stay intact. This supersedes the earlier generic revisitable-contents implementation, not the 13-stage teaching skeleton. Inspect IntegratedPathRail.tsx and IntroPathLearningLayout.tsx as source evidence; the skill's named legacy archive anchor documents could not be found. Local correction only; no publication or assignment changes.

## 2026-10-04 sequencing audit: compress teaching and interleave practice

Status: audited recommendation, not implemented or approved as a migration. Joshua requested dedicated pages for what conditionals are, sufficient and necessary, followed by indicator words and the must arrow. This supersedes the earlier strict relative order where needed while preserving substantive concepts. The sidebar correction alone did not solve over-fragmentation.

### What Intro to LR actually does

Current primary path in src/bootcamps/main-conclusion/content/introToLrPath.ts has 13 actions: 8 teaching notes, 3 standalone labs and 2 six-question practice sets. Its order is:

1. The Three Parts of an LR Question
2. So, An Argument
3. Premises
4. Conclusions
5. Five Types of Conclusions
6. Conclusion Type Lab
7. Beyond Premises and Conclusions
8. The 2-Part Conclusion Check
9. Main Conclusion Lab
10. First-Sentence vs Rebuttal Structures
11. First-Sentence vs Rebuttal Lab
12. First-Sentence Main Conclusion (6 questions)
13. Rebuttal Main Conclusion (6 questions)

It does not put a standalone drill after every note. IntroLessonPage.tsx renders seven answer/check widgets across four of the eight notes: premise indicator choices, support choice, conclusion indicator choices, an eight-item indicator classification quiz, sentence conclusion selection, five conclusion-type classifications and the two-part conclusion check (three claims with two yes/no judgments each). Anatomy scanning, support visualization, five explanatory type cards and four definition reveals are different interaction categories, not additional independent quizzes. Imported but unrendered role-labeling components are not counted. The older introGuidedSequence.ts workbook and routed reference/flashcard/simulator extras are not included in the current primary-path count.

Conclusion Type Lab has 12 items and requires a category choice before revealing feedback. Main Conclusion Lab requires selecting and analyzing a sentence and a correct result before Next. First-Sentence vs Rebuttal Lab has 20 stimuli and four reasoning stages, but also has an explicit assisted Skip/Reveal All route. IntroNotesShell can mark a note complete on Next without requiring embedded checks. Therefore neither every interaction nor every completion checkmark proves independent mastery. Adopt the substantive teaching/application sequence, not these completion assumptions.

Intro LR comparison is code-based. Its live reference route was assignment-gated, and no student completion/usage claim is made.

### Why the conditional opening has 70 pages

| Current unit | Pages | Main source of excess |
|---|---:|---|
| Orientation | 26 | Covers nearly the whole opening; one diagram stage split into three pages and six exercise pairs split into six pages, plus separate recall/lab/repair destinations. |
| Sufficient/necessary | 9 | Repeats definitions, relationships, four cases and foundation recall already introduced in orientation. |
| Group 1 | 17 | Two introductions, seven expression pages, six recurring method/practice pages, recall and repair. |
| Group 2 | 18 | Same structural pattern plus mixed-wording practice. |

The problem is not that everything is unnecessary. The navigation gives explanations, examples, reminders and individual questions equal weight, while the following units repeatedly restart teaching. Keep useful depth; combine overlapping explanation and turn repetition into retrieval or application.

Existing practice inventory: 25 unique reviewed cards (4 foundation,10 Group1,11 Group2) with29 placements because foundation is repeated;14 additional legacy recall examples;14 target examples;14 diagram-builder examples; four-case explorer; three target-position examples; four sign-pattern questions; six original/contrapositive exercise pairs; three applied labs for counterexample construction, negative cases and equivalent wording. Recorded banks remain separate from this reading-page count. Do not imply there is no practice code because the preview fails to interleave it visibly.

### Recommended smaller path

Nine reading pages and four practice checkpoints, arranged as follows:

1. What conditionals are. Rule versus fact, guarantee versus usually, approved raffle example, LSAT purpose.
2. The sufficient condition. Enough for what; winning is enough for getting a bicycle, but not the only possible route.
3. The necessary condition. Required for what; required result does not mean earlier prerequisite or sufficient on its own.
4. Practice checkpoint: rule/fact, enough/required, fresh case and a counterexample.
5. Read the must arrow. Sufficient left, necessary right; the left requires the right. Compare if-clause first/last without changing the arrow. Sentence position is flexible; arrow roles are not.
6. Sufficient-condition words. One grouped lesson with all seven core expressions and supplementary forms; in-page named examples/attempts rather than seven destinations.
7. Practice checkpoint: identify the whole sufficient condition, build a diagram, explain or repair its direction.
8. Necessary-condition words. One grouped lesson retaining all expressions, extended requirement wording and obligation/permission versus compliance.
9. Keep the whole meaning when wording changes. Complete conditions, only/the only, target position, What Test and Personalized If/Then as applications.
10. Practice checkpoint: mixed families and unfamiliar sentences, with qualifications and modality.
11. What a missing requirement tells you. Conceptual contrapositive and four cases, including what stays open and settled outcome versus still waiting.
12. Write and read the contrapositive. Negate both whole conditions and reverse; existing negatives/sign patterns. Practical FAQ embedded as optional help.
13. Practice checkpoint: all six paired original/contrapositive exercises in one item-by-item sequence, retaining feedback and answers.

Every teaching page can retain a brief meaningful check. Flashcards follow prerequisites within lessons; a flip is not treated as an assessed response. Full practice checkpoints should require an attempt, explain wrong choices and provide retry/repair. This proposal does not yet specify a new mastery gate or change student completion policy.

Keep: complete definitions, reasoning, original examples, indicator nuances, explanations of errors and useful practice. Combine: repeated introductions, arrow/word-order subpages, duplicated method explanations and recall pages. Move: six individual exercise pages into one practice destination, FAQs beside the relevant activity, mistake recaps into answer feedback. Remove: duplicate transitions and repeated recaps that add no reasoning task.

### Implementation boundary

Current material belongs to four unit/progress contracts. A coherent compressed path must preserve assignments, historical responses, recorded banks and difficulty. Do not silently reinterpret old completions. No app edits were made in this audit. This recommendation is the next curriculum correction, not a claim that the current preview already has thirteen stages.

## 2026-10-04 live reference correction: mirror the course, not the reference rail

Joshua opened https://lsatprep.study/bootcamp/intro-to-lr/lessons and explicitly identified its structure as the intended model. Parent now inspected that authenticated live course index, the Premises note and Conclusion Type Lab landing page. This supersedes the earlier reference-rail interpretation and the prior statement that live inspection was unavailable (that limitation applied to the earlier local route/session).

Verified structure: persistent course-level sidebar with Lessons under Intro Path; Practice Drills and Drill Lab under Practice; tools such as Flashcards under Tools. Lessons index is a vertical ordered series of cards labeled NOTE, DRILL or PRACTICE, each with a clear title, one purpose sentence and Read Lesson/Start Drill/View Instructions action. Notes open as dedicated concept pages. Live Premises combines definition, contrasting examples, indicator selector and answer/check practice in one article, followed by previous/next lesson links. Conclusion Type Lab has its own12-question entry page. No live question was answered and no Mark Complete action was clicked.

Correct conditional target: course-level navigation and a Lessons index containing separate concept lessons and interleaved drill cards. What conditionals are, Sufficient condition and Necessary condition must each be genuine dedicated lessons. Keep examples, quick checks and recall within the relevant lesson. Use separate drill destinations for substantive practice transitions. Do not retain a70-page sidebar inside orientation or relabel micro-pages as lessons. The9lesson+4practice proposal describes course destinations, not nested reader pages. Match the clean card hierarchy and restrained layout of the supplied live index; preserve approved conditional copy and persistence/assignment semantics rather than copying IntroLR's completion side effects.

No application changes in this live analysis. Earlier sidebar implementation remains current but is superseded as the desired structural model. Original user index tab retained; temporary note/lab inspection tabs closed.

## 2026-10-04 implementation authorized: dedicated conditional course path

Joshua asked to make the conditional version structurally similar to the live IntroLR course, including its sidebar and drills. Proceed with the9-note/4-lab course path discussed above. Scope: local course shell, Lessons index, dedicated notes, separate lab entry/run surfaces, meaningful existing practice and tools. Keep legacy unit assignments, recorded responses and assessment banks compatible. Current agents split shell/routing/path/style integration from content composition; independent reviewer audits reference patterns and final result. Parent verifies browser and files results. No publication, backend migration or paid action authorized by this correction.

Use actual IntroLR course-level LeftRail/WorkspaceShell and LessonsHub patterns, not IntegratedPathRail from reference pages. New experience must not embed the70page LessonPages navigation inside its notes. Retain approved teaching while combining repetition, and retain quick checks within each focused lesson. Practice stages require attempts and explanatory feedback/retry. Explicit reading review must not silently establish assessed mastery. Existing legacy contracts are not reassigned merely because the new visual path has13stages.


## 2026-10-04: Dedicated course structure implemented locally

The prior 70-page reference-reader approach is superseded for the opening course entry. The local course now mirrors the actual Intro to LR course structure: Lessons/Practice Drills/Drill Lab/Flashcards sidebar, vertical note/drill cards, nine dedicated notes and four interleaved labs. Definitions of conditional, sufficient and necessary each have their own lesson. Four labs have separate entry and run surfaces; all 25 cards and complete expression coverage remain.

Three review passes completed:

1. Teaching and content: checked prerequisites, grouped repeated material, retained all core and supplementary expressions, repaired stale transitions and required checked attempts before advancing paired exercises. Removed student-facing progress-accounting prose.
2. Independent routing review: repaired the primary Begin lesson entry, explicit assignment source-unit mappings and query preservation. No implicit legacy completion writes. Legacy routes and recorded banks remain.
3. Parent browser review: traversed 21 screens at 320/500/768/1190 CSS pixels (84 measurements), with no horizontal document overflow. Verified wrong/correct feedback, retry, checked-attempt gates, retained answers across Next/Previous, and mobile drawer selection/Escape focus. Repaired destination heading focus. Original old-query preview now opens the new course index.

Final automated checks after source freeze: 146 tests across seven files passed; typecheck passed; scoped new-file lint passed with no output; direct Vite build passed (7,154 modules, 57.01 seconds); canonical exclusion passed across 771 files. Logs: visual-proof/astra-opening/course-tests.log, course-typecheck.log, course-lint.log and course-build.log. Browser evidence: course-responsive-measurements.json, course-index-desktop.png and course-index-phone.png in that directory.

New app files: openingCoursePath.ts, OpeningCourse.tsx, OpeningCourseContent.tsx, OpeningCourse.test.tsx and opening-course.css. Modified routing/tests, opening/reference component exports and optional check callback, and ConditionalOpeningPreview.tsx. No bank, progress-schema, assignment implementation or generated-content edits in this correction. Session-local course answers are not recorded assessment completion. Authenticated student persistence and production remain unverified. No commit, push, deployment, backend write or paid action. Fresh Claude inspection remains pending from the previously failed run; no new approval claimed. Temporary browser tab closed; user preview and live IntroLR tabs retained, viewport restored. Task statuses unchanged.
