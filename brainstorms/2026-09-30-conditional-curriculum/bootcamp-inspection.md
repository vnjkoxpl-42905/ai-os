# A progressive conditional bootcamp using the Intro to LR course pattern

Draft: 2026-10-01. This is the delivery and implementation inspection for the existing [conditional curriculum](curriculum-analysis.md). [Interview decisions](../2026-09-30-conditional-curriculum.md) remain authoritative. No app code, existing Activities, student work or publication changed.

## Use the course pattern, with conditional-specific teaching

Recommendation: deliver the conditional curriculum as a bootcamp with an ordered main path, interleaved practice, reference tools and review. Keep the confirmed full learning sequence and separately assignable practice drill for every skill. Teachers retain whole-path, area, specific-skill and general-practice assignment at Beginner, Medium and Advanced. Quantifier reasoning follows conditionals and remains independently assignable.

The proposed course name is Conditional Logic Bootcamp. A route such as `/bootcamp/conditionals` is a proposal, not an existing route. Reuse Intro to LR's visual design and navigation. Its lesson content and main-conclusion interactions are not conditional teaching material.

## The current Intro to LR main path has thirteen actions

Read-only inspection used `C:/Users/Joshu/dev/lsatu-connected-experience`. These are local code findings, not a fresh live walkthrough.

The current [path source](C:/Users/Joshu/dev/lsatu-connected-experience/src/bootcamps/main-conclusion/content/introToLrPath.ts:34) interleaves eight authored note lessons, three native practice labs and two official-question practice pools. Its lesson landing recommends the first incomplete recorded action. Notes offer Mark Complete & Continue. This is recorded completion, not evidence of skill mastery.

Its actual order is:

1. The Three Parts of an LR Question
2. So, An Argument
3. Premises
4. Conclusions
5. Five Types of Conclusions
6. Conclusion Type Lab
7. Beyond Premises and Conclusions
8. The 2-Part Conclusion Check
9. Main Conclusion Lab
10. First-Sentence vs. Rebuttal Structures
11. First-Sentence vs. Rebuttal Lab
12. First-Sentence Main Conclusion official-question practice
13. Rebuttal Main Conclusion official-question practice

The [authored lesson page](C:/Users/Joshu/dev/lsatu-connected-experience/src/bootcamps/main-conclusion/modules/lessons/notes/IntroLessonPage.tsx) combines explanation, examples, traps and selected checks: question anatomy, support, indicators, conclusion selection and classification. Beyond Premises and Conclusions is explanatory without an embedded scored exercise. Copy the teach-then-consolidate pattern; do not invent a rule that every note contains the same interaction. The focused labs and official pools carry additional practice.

The [route set](C:/Users/Joshu/dev/lsatu-connected-experience/src/bootcamps/main-conclusion/routes.tsx:120) also contains reference tools, flashcards, indicators, simulator, hard sentences, diagnostics, spaced review, journal and settings. These are supporting destinations, not thirteen more sequential requirements. The workbook route currently redirects to lessons.

The three [native labs](C:/Users/Joshu/dev/lsatu-connected-experience/src/bootcamps/main-conclusion/modules/drills/introDrills.ts) contain 20 Main Conclusion, 20 First Sentence versus Rebuttal and 12 Conclusion Type items. Two fixed six-question official pools launch through Guided Drills and return their completion to the course. The exact Intro-specific launcher is in [GuidedDrillStart](C:/Users/Joshu/dev/lsatu-connected-experience/src/pages/GuidedDrillStart.tsx:317).

Do not copy an inherited unlocking inconsistency: [ordering.ts](C:/Users/Joshu/dev/lsatu-connected-experience/src/bootcamps/main-conclusion/lib/ordering.ts) unlocks Simulator after Conclusion Type Lab alone, while its hint describes three labs. Neither behavior establishes the prerequisite policy for conditionals.

## Build a repeating lesson, practice and transfer rhythm

Each skill's learning sequence should contain:

1. A concrete worked problem showing the inputs, result and reason.
2. A short explanation of the operation, with complete predicates and scope preserved.
3. A guided attempt that supports that operation.
4. Independent production before answer reveal, using a suitable existing Activity or a fresh native exercise.
5. An explanation that diagnoses the missed operation, followed by fresh practice.
6. A transfer task in unfamiliar wording or a suitable LSAT question when its prerequisites have been taught.

Separately assignable practice starts at step 4 and keeps teaching accessible. It does not require repeating the full sequence. The proposed hint-and-retry policy remains unanswered; worked solutions and optional hints are authored draft content, not approved grading behavior.

Not every lesson needs an official LSAT question immediately. Early labs can isolate a rule's direction or the difference between possible and guaranteed. Later guided drills coordinate learned operations in actual question demands. This avoids substituting question exposure for teaching the underlying skill.

## Keep the existing curriculum order and make smaller skills addressable

The following is the bootcamp adaptation of the existing sixteen-step proposal, not a new competing curriculum.

| Main-path section | Learning and practice focus | Existing material to reuse, with coverage review |
|---|---|---|
| 1. See a rule establish a conclusion | Worked guarantee; explain what the evidence establishes | Existing MBT teaching and an original introductory example |
| 2. Understand sets, sufficiency and necessity | Allowed-case comparisons; requirements versus guarantees | Refresher and conditional notes; fresh focused case practice needed |
| 3. Separate truth from validity | Assume premises; explain a valid move or construct a countercase | Notes; dedicated lab needs authoring |
| 4. Separate rules from facts | Produce a new rule versus a conclusion about a supplied case | MBT teaching/hub; focused contrast practice needed |
| 5. Negate and contrapose | Preserve complete terms; distinguish equivalence from an unsupported reversal | General/refresher and notes; targeted breadth review needed |
| 6. Translate Groups 1 and 2 | Two separate learning sequences and standalone drills | Refresher and General; [Group 1 draft](group-1-learning-and-drills.md) supplements existing content |
| 7. Translate Groups 3 and 4 | Two separate learning sequences; meaning checks before mechanical procedures | Unless patterns, refresher and General; group-specific packaging needed |
| 8. Choose the translation method | Mixed expressions; contextual indicator exceptions | General translation bank, reviewed by item rather than label |
| 9. Connect compatible rules | Direct and hidden links; no-link and look-alike contrasts | Linking, MBT and SA material; fresh no-link coverage needed |
| 10. Apply facts to chains | Four fact cases; forced versus unknown claims | MBT hub and lecture; verify coverage of each fact case |
| 11. Preserve meaning beyond indicators | Complete semantic equivalents; avoid word-spotting | General and notes; contextual items require review |
| 12. Handle AND and OR | Each placement on sufficient/necessary sides; partial triggers | General/hub and teaching notes; separate placement practice needed |
| 13. Negate compounds and whole claims | De Morgan, compound contraposition, counterexample to a whole rule | Existing compound material; whole-rule negation needs its own sequence before NA/refutation |
| 14. Preserve domains and qualifications | Retain subgroup, time, permission and obligation scope | General and MBT explanations; dedicated scoped practice needed |
| 15. Handle two-way rules and exclusive alternatives | Compare one-way, biconditional and exactly-one meanings | Relevant General items; inspected complete teaching bank not established |
| 16. Transfer to Logical Reasoning | Separate MBT/MSS, sufficient bridge, necessary requirement, flaw/parallel and principle units | MBT, Missing Link, SA bootcamp and guided pools; weaker application areas require original teaching |

The following quantifier phase covers meaning and denominators, existence, reversal limits, whole-statement negation, valid and invalid linking, and mixed application. It can be assigned directly without silently imposing an unapproved readiness test.

The [28-row teaching/practice map](curriculum-analysis.md) specifies smaller operations within these sections. A main-path section is a navigation grouping; its independently assignable skills remain separate.

## Difficulty and scope remain independent

Joshua approved the recommended progression on 2026-10-01 and explicitly requested execution: learn foundations across the skills first, then revisit them through Medium and Advanced passes. Complete the conditional passes before the following quantified phase. Targeted work remains independently accessible.

At every level, teachers can assign a specific skill directly. Beginner Group 1 work does not become mixed conditional practice merely because it sits inside a bootcamp. Advanced Group 1 work names any compound or chaining prerequisites instead of surprising the student with untaught operations.

General practice mixes skills already taught at the selected difficulty. Optional Medium and Advanced timing is confirmed; exact limits, defaults, consequences and advancement gates are not. Course completion, independent performance, hints and answer reveals must remain distinguishable.

## Reuse the shell and existing materials, add the missing connections

| Reuse | Adapt or add |
|---|---|
| Workspace layout, path rail, next-step presentation, lesson/reference layouts and practice shells | Conditional-specific routes, content and skill identifiers; do not copy Intro IDs |
| Saved-session and signed-in synchronization mechanisms | Separate conditional progress namespace; [useModuleProgress](C:/Users/Joshu/dev/lsatu-connected-experience/src/bootcamps/main-conclusion/hooks/useModuleProgress.ts) currently uses Intro-specific progress IDs |
| Existing whole-resource Activities and guided-drill assignment | Explicit learning-sequence versus practice targets, skill and difficulty selection; [assignWork](C:/Users/Joshu/dev/lsatu-connected-experience/src/lib/assignWork.ts:16) does not currently express these bootcamp choices |
| Existing conditional Refresher, General, Linking, MBT and Missing Link practice | Item-level skill tagging and appropriate subsets; whole Activity assignment is not a verified skill filter |
| Guided Drill start/resume/review engine | Conditional registered pools and return/completion handling; Intro's source-string bridge is hardcoded |
| Reference, flashcard and review presentation | Actual conditional reference and review content, honest progress and no fabricated analytics |

Signed-in persistence is local-first with Supabase synchronization; anonymous persistence uses local storage/IndexedDB. See [factory.ts](C:/Users/Joshu/dev/lsatu-connected-experience/src/bootcamps/main-conclusion/persistence/factory.ts). Reuse infrastructure with course-specific records, not shared progress keys.

Verified local conditional assets include 62 General items, 40 hub items, the four-group Refresher, SA bootcamp and 13 named conditional guided drills. Those totals do not establish uniqueness, complete coverage or current live availability. Keep covered Activities intact. A fresh skill drill may reuse their content or interaction when appropriate; it must not silently require a rebuild of the Activity.

## Record build status honestly

| Skill stage | Current status |
|---|---|
| Scope/interview | Independent study, scopes, three levels, two-part skill package, Intro-model direction and foundation-first progression approved. Exact mastery/time thresholds remain unspecified. |
| Content intake/audit | Existing inventory available; item-level coverage and complete per-module sufficiency remain open |
| Inspection before code | Joshua approved the concrete recommendation and execution on 2026-10-01. |
| Build and module checks | Implementation in isolated checkout `C:/Users/Joshu/dev/ai-os-projects/lsatu-conditional-bootcamp`, baseline `72df696`, released commit `796b943`. 30 lessons, 30 guided examples, 270 original questions. Content and integration reviews completed; 134 tests, typecheck, targeted ESLint, generated-content freshness and production build passed. |
| Polish | Browser fixture checks performed for lessons, exact teacher targeting, reload, assistance, timing, journal, failed-save retry, account isolation and 390/600/768/1440 widths. Uses local test actors and simulated cloud, not real student assignments. |
| Final parity | Not performed; historical quality/product/design anchors are missing, so no final parity certification is claimed |

The [bootcamp-builder skill](C:/Users/Joshu/.agents/skills/bootcamp-builder/SKILL.md) was found and its stale template/intake/checkpoint routes repaired. Its explicit quality rules remain: teach before calibration, real lesson introductions, explanations that teach, shared design, meaningful progress, no dead controls and no invented analytics. Missing historical references were reported rather than reconstructed or treated as read.

The authored bootcamp and teacher targeting are implemented and published at [Conditional Logic Bootcamp](https://lsatprep.study/bootcamp/conditionals). On 2026-10-01 the live entry bundle contained commit `796b943` and the conditional route, the browser showed the correct unassigned-account gate, and Lovable Publish reported up to date. Deployment: `156bd49f-e0e3-4d23-9d8b-ab3ba58ba09c`. Live signed-in cross-device saving remains unverified. Existing-asset item-level coverage and historical-document parity remain separate audit limits.
