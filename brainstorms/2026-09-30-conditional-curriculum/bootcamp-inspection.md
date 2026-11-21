# A progressive conditional bootcamp using the Intro to LR course pattern

## 2026-10-17: One numbered course, with purposeful supporting tools

Status: current code and live navigation audited. Joshua explicitly confirmed that all current opening material remains in Part 1. The structure below is a proposal for review, not an implemented or published change. Earlier Course overview wording was provisional and is now rejected.

Replace Course overview and Lessons with one **Course** destination. Both the root and existing lessons URL should reach the same assignment-filtered curriculum. The current overview recommends legacy work from progress.lessons/progress.attempts, while the rebuilt sequence records progress.course. Its recommendation is therefore not a reliable continuation of the current course.

The course page should show Part 1 expanded, an ordered vertical sequence, lesson numbers, explicitly labelled drills beside the relevant lesson, truthful saved status and one Continue action based on the same course records. This is a teaching sequence, not a calendar: do not invent dates or durations. Do not imply the full future curriculum is already available.

| Lesson | Current content | Following practice, in existing order |
|---|---|---|
| 1.1 | What conditionals are | |
| 1.2 | The Sufficient Condition | |
| 1.3 | The Necessary Condition | |
| 1.4 | Must arrow | |
| 1.5 | The contrapositive: conceptual introduction | Spot the condition |
| 1.6 | Find the complete condition | Read the rule |
| 1.7 | Necessary-condition words | |
| 1.8 | Keep the whole meaning | Find both conditions; Place the conditions; Build the diagram; Write it as if/then; Conditional translation practice |
| 1.9 | Contrapositive: formal lesson | Add the contrapositive; Negate the whole condition; Check your contrapositive; Build both diagrams; Put it into practice |

The conceptual/formal descriptions distinguish the two existing contrapositive lessons for this proposal; they are not approved replacement titles. Every practice row should visibly say Drill. Prefer lesson numbering for the hierarchy and task names for drills rather than competing numbering systems. Preserve existing exercise content and source identifiers; proposed display labels are separate metadata.

Future parts can hold 2.1, 2.2 and subsequent lessons once Joshua supplies or approves their content. Group 3 and Group 4 material already exists in the legacy foundations source, but is not integrated into the rebuilt opening course. Its existence does not establish approval, teaching quality or readiness for the new sequence. Do not auto-publish it as the future curriculum.

Supporting navigation recommendation:

- Course: the ordered curriculum and resumption point.
- Practice drills: an optional shortcut to the same drills, retaining separately assigned legacy skill practice.
- Resources: flashcards and reference. Reference is a lookup aid, not a second path through the course.
- Remove Review attempts and Journal from primary navigation while preserving their routes and all existing data. Review attempts currently covers legacy attempts only, not the current worksheet histories. Journal is one saved freeform text field with no linked-question workflow. Do not claim either is a complete review system.

Implementation contract: add explicit part and lesson display metadata to openingCoursePath.ts. Preserve stable step IDs, unit IDs, access aliases, assignment filters, query context, old URLs, drafts, journal text and save/error recovery. Never derive visible numbering from the filtered list or use display part numbers as backend assignment IDs. Root and lessons must share a course-progress-based continuation rule.

Acceptance before publication: root and old lessons URLs reach one curriculum; all nine lessons and twelve drills stay reachable in current order; restricted assignments retain original lesson numbers without exposing disallowed material; Continue respects actual course progress; existing drafts and journal text survive; supporting routes retain access checks; desktop, docked and mobile sequence remain readable and keyboard accessible. New parts must be addable without renaming existing storage keys.

Audit evidence: app checkout lsatu-drill-focus, openingCoursePath.ts, OpeningCourse.tsx, routes.tsx, progress.ts, courseProgress.tsx, assignments.ts and foundations.source.ts. Live Review displayed zero legacy attempts despite saved worksheet work; live Journal was a single text area. No learner answers or notes were changed. No app implementation, tests, push or deployment occurred in this audit.

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

## Approved structural correction: teacher-assigned stages

Joshua corrected the progression on 2026-10-01 and said to execute. No student difficulty picker and no three whole-course passes. Teachers assign the full sequence, a starting stage, an area or a particular skill activity; Levels 1–3 describe task demands at points in the sequence. New code preserves content/progress and adds a persistent action rail, lesson contents, separate guided activity route, assigned drill and repair review, in-place reference, shared Intro heading/tokens and contextual existing Activity/drill links. Focused 80 tests, typecheck, targeted lint and browser fixture checks at 390/600/768/1280/1440 passed. Production build and corrected release still pending at this checkpoint. Earlier published implementation remains live until the correction is verified. No account permission or real student assignment change.

Corrected release verified: 688aa22 (owned correction 2706937), deployment 642fe70e-cb43-4129-91f4-55bf56b07312. Merged typecheck and production build passed; postbuild scanned 766 files. Live entry /assets/index-C2IZpe-r.js contains 688aa22; ConditionalBootcamp-BEbeh810.js contains assigned-stage and guided activity structure and omits the old difficulty-picker label. Publication confirmed by live assets. Account access is unchanged. This supersedes the earlier whole-course difficulty-pass architecture; full historical Intro parity and production cross-device saving are not certified.

## Source alignment with actual assigned notes (2026-10-01)

Read the complete live `content_html` of four conditional notes through an authenticated, read-only Classroom query. All four returned `status: assigned` and `visible_to_student: true`:

| Student | Title | Classroom item ID |
|---|---|---|
| Asia | Conditional Logic: Cheat Sheet | `75133805-ff98-4dea-8851-168205733da4` |
| Asia | Conditional Logic: The Breakdown | `089ce68a-4eb4-4acc-90a1-cd4d5ac4f30a` |
| Yahunathan | Before you start: Conditional Logic (Easier) Set 4 | `5aa2bb01-2103-4fab-b25d-3a26427498e5` |
| Yahunathan | Before you start: Conditional Logic (Easier) Set 1 | `0faaffff-fb5c-40c9-949b-72521bea662f` |

Asia's full local teaching copies are [Cheat Sheet](../../students/asia/conditional-logic-cheat-sheet-2026-08-24.html) and [The Breakdown](../../students/asia/conditional-logic-the-breakdown-2026-08-24.html). Breakdown anchors `#bd-1` through `#bd-5` cover language; `#bd-6` compound contraposition; `#bd-7` biconditionals and otherwise; `#bd-8` quantities; `#bd-9` illegal moves; `#bd-10` chaining/triggering; `#bd-11` when diagramming helps. The four word lists contain **44 expressions**, not 49: 19 left, 16 right, four negate-left, five negate-right. Additional phrases occur outside those lists. The earlier 49 count was an arithmetic error, corrected here.

The actual Yahunathan notes teach guarantee and sufficient/necessary roles before contraposition, then paper translation of only-if/unless before answer choices. They ask for untimed blind review before checking. Preserve this training purpose without copying personal performance comments or making diagramming permanently mandatory for every question. His newer [Facts, Rules, and What Follows V10](../../students/yahunatan-zetvy/recaps/2026-09-16-recap.md:2330) was also reviewed, but remains a local draft with `posted: false`; it is not one of the verified assigned notes. Sofia's [conditional lecture](../../students/sofia/recaps/2026-09-11-recap.md:13) has the same draft limitation.

Current source edits incorporate Joshua's What Test, Personalized If/Then, explicit six-step translation, Recall and Rephrase practice and visual result-to-trigger chaining. Further source alignment emphasizes complete predicates, new rules versus same-person facts, intermediate chain conclusions, contextual language coverage, and choosing notation when it makes reasoning visible. Source edits are distinct from proof of a published release.

Do not reproduce source shortcuts as universal rules: the older word-position rule conflicts with the meaning-based What Test; guarantees/implies/ensures require sentence-level direction; signals need not supply certainty; not alone does not create a universal; permission must not become actual entry. Asia's fixed few = most-not claim conflicts with Charles's newer context-sensitive quantity note. Yahunathan's contrapositive explanation should say the same conditional relationship, rather than the same fact. Earlier recovered PDFs also contain mistaken prose about necessary conditions and activation despite correct diagrams; the reviewed logical relationship governs.

Charles's complete live **Some, Most, and All** note, item `c9228402-da0e-4411-984e-17831a798e5c`, was read and returned assigned/visible. Its [local teaching text](../2026-09-28-recap-format/09-quantity-statements-classroom.md) supports the later quantity phase: some/most may include all, exact negations, fixed denominators, existence limits, same-group overlaps, partial-chain gaps and contextual few/many. Its count slider and rearrangeable majority overlap teach guarantees through concrete witnesses. **Group-size comparison from opposing majority claims and manipulable witness/overlap activities remain unimplemented bootcamp gaps**, rather than claimed completed coverage. Charles's assigned Conditional Indicators Refresher is a shared existing module; no assigned Conditional Breakdown note for Charles was identified in this review.

No live assignments or content were changed during this source review. Original archived sources remain unchanged.

Four-stage correction published on 2026-10-01: source/release 1f0bef735b3265bb3ea885711c529a58efaef5de, deployment 6af313b9-96f2-44fb-91b0-ba328feb6cf2. Final guarded typecheck, production build (766 postbuild files), targeted lint and14 route tests passed. Fixture browser verified four stage regions, exact Group1/2 lesson labels and Group1/4 guided six-step methods; desktop width had no page overflow. Live entry /assets/index-BKSuZwgq.js contains1f0bef7; ConditionalBootcamp-D8XJUrcP.js contains the four-stage title and omits the old assigned-stage heading. Lovable Publish shows Published/up to date with Publish changes disabled. Teaching content is separately bundled; method verification used rendered fixture and exact source release, not a claim that the main route chunk contains every lesson. Existing unassigned-account gate and production cross-device limits remain. No paid Lovable agent call, real student write or migration. Fixture stopped and temporary QA tab closed. Earlier generated stash and unrelated bank/index/MCP changes preserved.

Student note-flow correction published on 2026-10-01: source `0ee5ecb`, merged release `67230dfae74a1466515d570fcb7b8a96ab5cb9c5`, deployment `212bbe39-4c6f-417e-ac10-1327d9feacd7`. The previous student catalogue/Teaching Sequence rail was the wrong experience. Current entry presents actual assigned work; explanatory notes modeled on Intro presentation include worked examples, inline relationships, methods and mistake repair, then guided work and attached drills. First note explicitly defines conditionals. Trusted visible/unlocked assignment rows control unit/mode/level, metadata invalidity fails closed and URL edits do not expand scope. Teacher preview is separate. Current Intro gate itself permits its entire bootcamp after any module grant, so assignment-only behavior here is a deliberate correction rather than claimed Intro parity. All 30 unit IDs and270 question IDs/answers remain. Later interactions are worked-reasoning comparisons, not fully bespoke capstones. Remaining quantity gaps above persist.

Merged40 tests passed (38 conditional +2 payments from concurrent merge), merged typecheck and build/postbuild770files passed, targetedlint passed. Browser fixture inspected first definition/fourcases, Group2targetdirectionreveal, note-to-guidance-to-drill, practice-onlyadvanced, unassignedaccount and390/600/768/1440widths. Fixed duplicateTOC entries andtabletbrand overflow. Live entry `/assets/index-Dr3WEnnl.js` contains exact67230df; routechunk `ConditionalBootcamp-Ws35yIhF.js` contains currentwork/richnote andnoassignedstageheading. Refreshed userCodex tab10 andopened actual live FindtheGuarantee note. No realassignment, notification, permission, migration, paidLovableagent or Introfilechanges. Crossdevice studentpersistence/historical-documentparity remain unverified. Fixturestopped/ownedtabclosed, viewportreset; unrelatedMCP/bank/indexchanges andpriorstash preserved.

### 2026-10-17: Clarify the proposed lesson boundaries

Newest Joshua correction: the separate introductory and writing-contrapositive lessons are confusing; the complete-condition stage is unclear; sufficient and necessary indicator words belong on their respective sufficient and necessary condition pages.

This supersedes the proposed 1.1–1.9 table above as a final outline. Revise the proposal toward one coherent contrapositive lesson covering meaning, reason and procedure. The existing split distinguished a conceptual missing-requirement explanation from later formal writing, but that implementation distinction does not justify two confusing course entries. Preserve teaching-before-testing dependencies when moving either content or drills; do not simply move the advanced lesson earlier without reviewing its prerequisites.

Complete condition means the whole idea, including restrictions. For example, in If a student submits the form before Friday, they receive a confirmation, the condition includes submitting the form before Friday. Dropping before Friday changes what the rule guarantees. Teach this within the sufficient/necessary lessons and relevant drill instructions rather than retaining an unexplained standalone stage by default.

User explicitly directs sufficient indicator words onto the sufficient condition page and necessary indicator words onto the necessary condition page. Dedicated flashcards remain supplementary practice. No app changes or content moves have been made by this proposal correction. Final numbering must follow the revised teaching sequence, not preserve redundant pages merely to retain the earlier table.

### 2026-10-17: Simplified Part 1 implementation awaiting PR and final verification

Parent-reported implementation is complete on branch `codex/conditional-course-structure`, pending PR. One Course presents five numbered notes, 1.1–1.5, and twelve clearly labelled drills. The contrapositive lesson combines the Maya explanation and formal template; the existing law-school video remains optional and preserved. Sufficient/necessary pages now include their respective indicators and complete-condition qualification teaching. Dedicated group flashcard decks have restored access and separate storage keys. Existing routes, data and assignment-scope filtering remain preserved; non-opening assigned continuation closes the details view appropriately.

Reported local verification: 148 affected tests passed cleanly; after adding one regression, the final content suite passed all 26 tests. A broader unchanged mixed suite had four timeouts plus a worker RPC timeout and did NOT pass. The first typecheck passed; final typecheck and final production build remain pending. Browser checks covered widths 390, 768, 1005 and 1440, preserved Question 26 selections through Reference navigation/back, and verified Group 1 flashcard resume locally. These are parent-reported local checks. Actual-account acceptance and live verification of this branch have not been performed. No merge or publication is claimed.
Final local verification and PR follow-through, 2026-10-17: app commit `a5933632` was pushed on `codex/conditional-course-structure`; PR [#221](https://github.com/vnjkoxpl-42905/lsatu-684d89db/pull/221) is attached to the chat. Final production build and typecheck passed. Six affected suites passed 148/148 tests, and the final content suite passed 26/26. Four broader MixedDrill timeouts remain an explicit limitation; no full-suite pass is claimed. The app working tree was clean. The local preview on port 8092 was opened in Codex; screenshot: `C:/Users/Joshu/.codex/visualizations/2026/10/14/01a13b38-4823-78b0-ba01-9c5f786fa0b6/conditional-course-structure-preview.png`. This supersedes the pending final-build/typecheck and PR-creation status above. The PR is not merged and the change is not published; the updated standing instructions require Joshua's explicit merge authorization. Actual-account/live acceptance of this change remains unverified.
### 2026-10-17: Course visual refinement scope

Newest explicit direction: percentage progress, text/icon/color distinction between lessons and drills, no boxed course rows, Classroom at the bottom, and a clear explanation of Reference's purpose. Parent implementation candidate: open vertical timeline, blue book-marked lessons, teal drills and Quick reference wording. Candidates are provisional; this checkpoint records scope only, with no verification, merge or publication result. The 21st.dev MCP was unavailable; the parent read its skill and researched the public Modern Timeline catalogue, then made an original adaptation without paid calls or connector generation. Preserve course order, truthful progress, assignment context, drafts and accessible navigation.
### 2026-10-17: Twelve-drill audit and separate progress scopes

Joshua explicitly confirmed that each drill's saved question progress must remain separate from the Course percentage for completed lessons and drills. Completion percentages describe work completed, not accuracy or mastery. Audit scope covered all twelve banks and their operations; it did not exercise every runtime answer path or fully reread original PDF/DOCX instructions.

Recommended consolidation, not an implemented deletion: present three main practice paths, Translate a rule, Check the contrapositive and Mixed practice, while retaining the other banks as optional work. These names are recommendation candidates. Preserve facts/inference practice, complete qualifications, rewriting and fresh transfer rather than reducing the course to indicator matching.

Overlap findings: the ten-item Place conditions bank repeats Find both conditions throughout. The fifteen-item diagram bank also repeats prior material, but adds productive diagram work. Two contrapositive revisit banks clone earlier banks. The thirty-five-item independent bank uses the same eight-stage scaffold as the twenty-item full-translation bank, so its current interaction is not genuinely independent production. Retaining content does not require presenting every overlapping bank as a separate required main-path drill.

Completion policy caveat: worksheet completion currently excludes the final self-review even though visible reviewed progress depends on it. This audit flags the discrepancy for a policy decision; it does not claim a fix. Preserve saved question position, answers and review state separately from aggregate Course completion.
### 2026-10-17: Newest drill-review decisions supersede consolidation proposal

Joshua rejected the proposed three main practice paths: review the drills one by one before deciding their broader organization. He explicitly directs removing Place conditions (`source-roles`) from the active course and removing the entire first/last-word condition-selection stage wherever it occurs in the affected drills. Preserve source banks, saved data and complete-condition/qualification teaching. His exact newest rewrite prompt is `Rewrite this conditional as if/then.`, superseding the earlier own-words/no-if-then prompt preference for this step only; semantic-equivalence grading remains intact. Use sequential active-order drill badges and remove stale embedded source-worksheet numbering without renaming stable route/item/storage identifiers. Review restored attempts carefully when a removed stage changes numeric positions. This records directions and supersessions, not completed implementation or publication.
### 2026-10-17: Drill-by-drill corrections verified locally

Parent-reported app commit `e9673a3d` implements the scoped corrections on the feature branch; branch push is in progress and is not yet claimed successful. The rejected three-path consolidation was not implemented. Final focused checks passed: 113 route/course tests, 30 worksheet/bank tests and eight staged-drill tests, totaling 151; typecheck and production build passed. Browser checks confirmed eleven sequentially numbered active drills with Place conditions absent; the next Build the diagram drill supplies the conditions before symbol work, gives a hint for reversed placement, accepts correct placement and retains saved letters. Drill 4 is open in the local preview for review. These are local checks; the change is not on main and is not live. Earlier broader-suite timeout limitations are not converted into a full-suite pass by these focused results.
### 2026-10-18: Condensed-condition workflow requested

Newest explicit directions, implementation pending: replace W/R letter assignment with learner-written condensed conditions; preserve their meaning and use clear sufficient/necessary sides and arrow. Use exact Next step buttons. Use consistent visual drill progress bars and percentages without visible reviewed/remaining prose, keeping position and aggregate Course progress separate. Remove the My reasoning matched / Needs another look final gate and provide actual-work feedback without falsely grading free writing. Preserve drafts, save-error handling and honest grader-failure states. Previous letter-only and self-rating implementation records remain historical, superseded where they conflict.

Branch status follow-through: the parent confirmed commit `e9673a3d` was successfully pushed to `codex/conditional-course-structure`, and PR #221's body was updated. This supersedes the earlier push-in-progress status. The PR remains unmerged and the change is not live.
### 2026-10-18: Condensed-condition implementation, final draft fix pending

Parent-reported local implementation, not yet committed: condensed phrases replace letter production throughout worksheet flows, demos and reference. Next step uses semantic validation through the existing nano endpoint, with no backend edits; exact full-condition/model identity can pass offline. The checks cover short condition pairs with task-specific verdict/explanation and rewrite/contrapositive readbacks. Self-rating and acknowledgement gates are removed; final results show the actual diagram and explanation with optional full wording. Shared segmented percentage progress is used across all four drill families. The mobile arrow remains visible and browser widths 390/768/1005/1440 had no overflow. Flow-v4 recovery retains drafts while requiring old letters and previously ungraded writing to be checked again. No three-path consolidation was implemented.

Reported tests passed after a stale-expectation correction: 35 worksheet/bank, 31 header/family and 43 content tests, totaling 109 unique tests; a subsequent 23-test component rerun also passed and is not added to that unique total. Build and typecheck passed, but final acceptance is pending a picker in-progress bug fix: saved short-field drafts were ignored. Do not treat the earlier green checks as final verification of that fix.

No paid live-provider grading calls were made. Browser checks exercised identity acceptance; service-error guards were unit-mocked. Actual response quality for the new semantic prompt remains unverified. The 21st.dev MCP was not exposed; the parent used its public segmented catalogue as a reference for an original adaptation, without installing a component. PR #221 remains unmerged and this implementation is not live.
Final condensed-flow verification follow-through, 2026-10-18: parent confirmed commit `ff3eab06` was committed and pushed to PR #221. Final production build exited 0 and typecheck passed. The affected unique-test total is now 110: 36 worksheet/bank, 31 progress/foundation/mixed/staged and 43 content/reference/course-content tests. The final component rerun passed 24 tests; it is not added again to the unique total. The saved-short-draft not-started bug was fixed, and browser inspection showed an unsubmitted Question 1 containing short phrases correctly marked in progress at 0%. This supersedes the pending bug, commit and final-verification status above for these local paths. Prior historical completions remain preserved rather than cleared; current question progress requires the new checks. The new semantic AI prompt has not been verified through paid live calls, and no endpoints or model configuration were deployed. PR #221 remains unmerged and this change is not live.
### 2026-10-18: Remove duplicate question navigation and clean known preview drafts

Newest explicit direction: remove the bottom numbered question map, retaining the top bar and bottom Previous / Next question. Fresh short-condition fields remain blank while genuine saved drafts resume. The parent acknowledged that handed-over filled fields were its own test drafts; clear only those known test values through the UI. No persistence wipe, unrelated draft reset or historical-completion reset is authorized. Leave future user-review previews free of the assistant's unlabelled test answers. Implementation/cleanup verification is pending, not established by this capture.
Follow-up dependency correction, 2026-10-18: changing a short condition invalidates downstream placement, NOT selections and accepted grades, retaining written text. Untouched resumed drafts still restore. Parent preview cleanup uses UI edits of its own known test draft, not account-record removal. Current code and final checks remain pending; no completion claim.

Preview/navigation verification follow-through, 2026-10-18: parent confirmed commit `2ec57a2b` was pushed to PR #221. All 25 focused tests passed: 24 navigation/blank/resume tests plus one dependent-selection regression. Final production build and typecheck passed. Browser reload showed both short-condition inputs blank, no bottom picker DOM, only Previous question / Next question at the bottom, and the top progress bar at 0%. The parent cleared only its own known preview draft through normal UI input edits; learner-draft resume remains preserved, with no account-progress wipe. Responsive checks at 390, 1005 and 1440 found no overflow. This supersedes the pending implementation/cleanup checks for these inspected paths. PR #221 remains unmerged; the change is not on main and not live.
### 2026-10-18: Chapter naming, panel-fit diagrams and authorized release pending

Newest directions: visible Part labels become Chapter; stable internal keys and 1.1 numbering remain. Diagram choices need clear sufficient/necessary contrast and an actual question, with responsiveness based on the real panel width. The 658px content panel plus rail exposed cramped presentation despite a larger viewport. Parent reports latest six-file UI commit `43a5fa7a` and a local merge of origin/main. Joshua explicitly authorized current-work merge/publication, but main merge/publication and final build remain pending; no live claim. Chapter 2 AND/OR is planning through second-brain query/grilling, not implemented or locked. Parent-owned planning capture: `brainstorms/2026-10-18-conditional-and-or-chapter.md`; awaiting answers before final curriculum decisions.
### 2026-10-18: PR #221 merged and frontend publication verified

Parent-reported release: PR #221 merged into main as `ca44df9185970038d93685d01a4f118dd1a838bd`. Focused checks passed: 113 course/routes tests and 25 worksheet tests; reconciled-main production build and typecheck also passed. Local browser checks covered widths 390, 658, 768, 1005 and 1440. Lovable get_project matched the merged SHA before free deployment `5d450276-3852-4d29-914d-4bc37f9f34a2`. Initial old assets were not accepted as live evidence. Final production `/assets/index-FjB0Le0n.js` and `ConditionalBootcamp-0ToRNgPE.js` contain the new diagram prompt and Chapter label; Lovable read_file at the merged SHA confirmed source. This supersedes the earlier unmerged/not-live and pending-build status for PR #221.

Acceptance limits: the production browser was signed out, so this release has no new signed-in acceptance. New live-grader prompts were not tested through paid calls. No paid calls were made and Chapter 2 was not implemented. The AND/OR planning capture remains separately parent-owned and unresolved; frontend publication does not establish that future chapter's approval or completeness.