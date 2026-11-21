# Existing material can seed the conditional curriculum

Date: 2026-09-30. Read-only inventory of teaching and practice content; no application or platform changes. The six areas are the accepted discovery map, not a settled teaching order. Quantifier scope remains unresolved.

## Evidence and the checkout correction

The routed checkout `C:/Users/Joshu/dev/ai-os-projects/lsatu` is on `feat/calendar-strip-deeplink` at `190ff7b`, with extensive local changes. Its absence of the newer conditional hub is not evidence that the hub does not exist. The first inventory missed that distinction.

The preserved conditional release checkout is `C:/Users/Joshu/dev/lsatu-conditional-update`, detached at `486f33b`. A newer inspected checkout, `C:/Users/Joshu/dev/lsatu-connected-experience`, is on `codex/connected-experience` at `db55fd4`; it contains the hub and additional Conditional Indicators Refresher. Paths below use that newer checkout for app content unless stated otherwise.

The 2026-09-14 discovery record documents publication and production verification of the hub on 2026-09-16 and the paired-choice General update on 2026-09-17. This report inspected code and those records; it did not freshly verify the live site. Guided-drill metadata comes from the saved live snapshot at `2026-09-30T11:47:46.909Z`. Legacy corpus extracts are teaching evidence, not proof of current availability or full source recovery.

## What is usable already

| Resource and exact home | Verified content | Role and limits |
|---|---|---|
| `C:/Users/Joshu/dev/lsatu-connected-experience/src/features/conditional-refresher/content.ts` and `ConditionalIndicatorsRefresher.tsx` | Four-group cheat sheet; 22 indicator entries for sorting; 16 diagram items; 12 flashcards; four symbolic Unless patterns | Usable introductory review/practice in local app. Tabs: Cheat Sheet, Sort Drills, Flashcards, Diagram Drills, Unless Drill. Progress saved in this browser, not account-wide teacher mastery records. The Unless tab gives three statements, five seconds each. Counts are entries, not independent skills. |
| `.../src/features/activity-centre/content/conditional-rephrase.json`; `.../conditionals/generalPhases.ts` | 62 General items, including indicators, negation, look-alikes, jargon, compounds, biconditionals and a multi-rule sentence | Usable translation/contraposition practice. Paper-first, four paired diagram/contrapositive options. General phases: 1–12 untimed, 13–37 at 45 seconds, 38–62 at 30 seconds for diagramming; timed statement disappears when choices open. It is not a dedicated multi-rule linking bank. |
| `.../src/features/activity-centre/conditionals/questions.json` and `content.ts` | 22 Missing Link + 10 Must Be True + 8 Linking = 40 authored questions | Usable local practice, with paper attempt, five choices, explanations, retry/reveal and saved sessions. Variables and words/phrases are selectable. Includes direct chains, contraposition, negative links, AND/OR and short prose. Linking and Missing Link both ask for an additional conditional; their labels do not establish distinct mastered abilities. |
| `.../src/features/activity-centre/conditionals/ConditionalPractice.tsx` and `practiceStore.ts` | Four-world hub: General Conditionals, Linking, Missing Link, Must Be True | `/activities/conditionals` hosts the practice. General opens the student's assigned Activity; other worlds are self-practice under Activity access. Run history includes unfinished, retry and reveal records. No six-area placement or prerequisite chain found. |
| `.../src/features/activity-centre/worlds/switchyard/wings/rounds.ts`, `SortingYard.tsx`, `TriggerGallery.tsx` | Sorting sufficient/necessary clauses and hard-indicator groupings from the same General bank | Existing companion code, not additional independent authored banks. Runtime availability of these wings was not rechecked. |
| `.../src/bootcamps/sufficient-assumption/content.ts`; `.../src/lib/bootcamps.ts` | Ten chapters, six official questions, twelve written conditional exercises | Substantial application teaching and practice: bridge premises/conclusion, confirm sufficient, missing links, two independent chains, negated recurring elements, irrelevant conditional premises. Whole bootcamp assignment; written exercises and navigation progress are not a full conditional mastery assessment. |
| `C:/Users/Joshu/dev/ai-os/corpus/lectures/logical-reasoning/must-be-true/core/2026-08-27-33013/` | One complete filed lecture package: 97-minute source, five worked questions, 22 mapped images; teacher teleprompter, continuous script, Socratic steps, teaching brief and coverage ledger | Strong private teacher guide. Opening explains rules, facts, contraposition, linking and triggering; applications include MBT/MSS, AND/OR, requirements, scope, and passive voice. Not a student curriculum or assignable lesson pack. Full audio fidelity remains unverified; source logic slips are explicitly corrected in adaptation. |
| `C:/Users/Joshu/dev/ai-os/corpus/Curriculum/Conditional Logic/Homework/conditional practice.md` | Three named stages, two five-question sets each, 30 official question references | Legacy real-question practice list. No stated skill distinction between stages. Old PT references need canonical app mapping before use; not counted as new questions beyond existing bank. |
| `C:/Users/Joshu/dev/ai-os/corpus/Curriculum/Conditional Logic/Notes/_megadoc_notes_conditionals.md` | 28 source entries, including sufficient/necessary, four groups, six-step process, What Test/indicator target, personalized if/then, chaining versus triggering, illegal moves, AND/OR, intuition, question-type methods, timed sets and workbook references | Teaching/reference pool with useful substantive passages, duplicates and abbreviated extracts. Source-entry count is not 28 ready lessons. Some purported workbook material is only a short excerpt. Requires editorial consolidation and source completeness checks. |
| `.../Notes/homework_conditionals.md` | 12 source entries: Group 1/2 and 3/4 translation, rephrasing, chaining, Some/Most, fallacy identification, staged homework and review instructions | Legacy practice/reference pool. Several extracts stop mid-sentence. Historical 5/5 advancement instruction exists; no evidence it governs current platform progression. |
| `.../Notes/_megadoc_reference_conditionals.md`, `_megadoc_lecture_conditionals.md`, `_megadoc_other_conditionals.md` | Answer-key references, older lesson extracts and additional translation/quantifier material | Reference/evidence only unless passage completeness is checked. The answer-key `.gdoc` entry contains its filename rather than the key. Do not count filename-only content as recovered teaching or exercises. |
| `C:/Users/Joshu/dev/ai-os/references/lsatu-guided-drill-catalog.md` and JSON companion | Snapshot records 13 named Conditional Logic drills: three Easier, six Medium, four Harder; plus three student-specific MBT translate/connect/prove drills | Real-question application practice. Multiple drills draw from overlapping pools, so do not sum counts as unique questions. Beginner/intermediate/advanced affect preferred bands; titles do not establish exact difficulty or specific mastered subskill. |
| `C:/Users/Joshu/dev/ai-os/corpus/Curriculum/_question-feature-index/complex-conditionals.md`, `conditional-conclusion.md`, `_reasoning-types/conditional-logic.md` | Indexed reference locations for locating conditional questions | Retrieval aids, not instruction. Exact question suitability still needs question-level review. |
| `C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-16-conditional-linking-question-bank.md` | 32 draft entries: 22 Missing Link and 10 MBT, including twelve photo-derived prompts, explanations and documented Boolean validation | Authoring/provenance record. Much of this is reused in the app bank, so not an extra 32 questions. Intentional equivalent photo pairs should not be counted as independent transfer evidence. |
| `C:/Users/Joshu/dev/ai-os/brainstorms/2026-09-14-conditional-drill-input-design.md` | Decisions, workflow, release and verification records | Governing design history. Early proposals are superseded by later dated clarifications; preserve paper-first, deterministic grading and the existing content rather than reviving rejected interactions. |

## Coverage against the six areas

| Accepted area | Existing teaching | Existing practice | Sufficiency judgment |
|---|---|---|---|
| Understand what rules mean | Refresher cheat sheet; legacy intro/What Test/personalized if-then; MBT opening and explicit rule/fact definition | Indicator sorting; relationship-recognition Activity; illegal-move questions embedded elsewhere | Starting material exists. A short beginner lesson and independent diagnostic distinguishing rules, facts and unsupported converse/inverse are not yet packaged. Indicator memorization alone does not establish understanding. |
| Translate rules | Four groups, diagram/flashcard explanations; substantial legacy notes | 62 General items; 16 refresher diagrams; 12 flashcards; Unless patterns | Best-covered area. Need expose specific skills as subsections, preserve scope/compound lessons, and separate untimed accuracy from timing. A broad bank is not itself a placement rubric. |
| Use facts with rules | MBT lecture explicitly teaches triggering and contraposition with facts | Ten authored MBT questions include negative facts/compound triggers; real MBT drills | Real content exists. Limited dedicated beginner reps isolating all four fact/rule relationships were verified; ten mixed questions cannot prove breadth or unseen transfer sufficiency. |
| Connect rules | MBT lecture and SA chapters; legacy chaining notes | Eight Linking, twenty-two Missing Link, SA written exercises, MBT chains | Far more exists than the first inventory found. Still needs explicit direct-link, turn-before-link, shared-result/no-link and negative-link subskills, teaching before practice, and targeted transfer pools. Linking and Missing Link currently overlap in task. |
| Complex conditionals | Refresher compounds; General explanations; MBT AND/OR board; SA chains | General compounds/biconditionals/stacked negatives; authored AND/OR and mixed negative chains | Coverage exists but is scattered. No complete progression or sufficient independent reps per advanced operation was established. Some/Most belongs here only if Joshua settles that boundary. |
| Apply to LSAT questions | Full MBT/MSS lecture; SA bootcamp; legacy question-type method notes | Easier/Medium/Harder real-question drills; 30 staged legacy references; official worked examples | Good starting application pool across MBT/MSS, SA, principle, parallel and flaw. Question-specific purpose and explanation quality need review before treating every filter match as a useful conditional lesson. |

## Assignment and self-study boundaries

The newer local bootcamp registry **does register Conditional Indicators Refresher** at `/conditional-indicators-refresher`, so the whole refresher can be assigned through the bootcamp mechanism. This corrects the earlier outdated-checkout claim that only SA was available for this teaching.

A student can select **Unless Drill** as a dedicated tab, and inspect the Group 3 cheat-sheet section. That is narrower self-study than taking all 62 General questions. There is no Group 3-only filter on the mixed Diagram Drills or Flashcards queues in the inspected component. The group buttons in Sort Drills are answer choices, not curriculum filters. Selecting Unless Drill is not proof of a teacher-assignable Group 3 subsection.

The shared `assignWork.ts` API assigns whole Activity, guided drill, homework set or registered bootcamp. It has no specific-skill/item-subset kind. The hub filters variables/words/all rather than indicator groups. Scheduling, bundles and item order exist; a mastery prerequisite chain across the six areas was not found. Current teacher visibility is uneven: General has indicator-family ledgers, hub practice has saved run history, refresher uses browser-local progress.

## What is missing versus merely unassembled

The material is sufficient to start assembling a real curriculum and to avoid writing everything again. It is not sufficient evidence to declare a complete beginner-to-expert course ready. Strong assets already exist for translation, chaining, MBT applications and SA linking.

Packaging gaps are the unified home, teaching sequence, independently assignable subsections, notes attached to the right practice, entry diagnostics, advancement criteria, remediation and review schedule. Many can be solved using current content.

Content gaps requiring closer question review are beginner rule/fact/invalid-move contrast reps; no-link/shared-result contrasts; enough fresh items for each advanced AND/OR, negation, biconditional and mixed-chain skill; and application teaching beyond the well-supported MBT/SA examples. These are unproven sufficiency gaps, not claims that all such material is absent. Legacy truncated sources need recovery before counting them.

Do not use question count, a named stage, a difficulty band, or successful repetition of an explained structure as proof of mastery. The next discovery decision is what a student must demonstrate independently in each area before advancing, and whether quantifiers enter this curriculum or a separate linked pathway.

## Desktop final-set audit, 2026-10-11
Reviewed all 11 files in the user-named Desktop Group 1 and 2 - EVERYTHING folder: 42 PDF pages plus the complete DOCX. See [integration audit](2026-10-11-desktop-group-1-2-integration-audit.md), its three item-level/source reports, and [SHA256 manifest](source-audit-2026-10-11/manifest.json). 133 worksheet task instances include deliberate repeats;108 is the sum of within-set distinct statement entries, not a globally deduplicated new bank. The new keys expose correctness, modality, scope and classification defects. This is source analysis and version reconciliation, not formal ingestion, application import or deployment. Originals unchanged.

## 2026-10-25: organize the whole bootcamp from the source material

Joshua clarified that “scored” was a typo. The request is complete topic coverage and purposeful organization using his other conditional notes, specifically Groups 3/4 and linking drills. No grading redesign is requested. The chapter map below is a source-backed recommendation, not a claim that the remaining chapters are built or that exact titles/divisions have been approved.

### Proposed chapter and lesson homes

| Chapter | Lessons and learning purpose | Practice that earns a place |
|---|---|---|
| 1. Conditional basics | Preserve current 1.1–1.5: conditional meaning; sufficient and Group 1; necessary and Group 2; must arrow; contrapositive. Include complete conditions, all four fact/rule situations, unsupported converse/inverse, natural readback and when diagramming helps within these existing homes. | Existing reviewed foundation/translation/contrapositive work. Audit overlap before adding or deleting drills. Do not revive the rejected first/last-word operation or retired placement drill. |
| 2. AND and OR | Preserve the local three-lesson draft: both/at least one; compounds on either side; whole-group negation and all four contrapositives. Existing negatives and scope remain attached to full ideas. | Existing four local practice sets: meaning, placements, negation, mixed original/contrapositive production. Nested transfer comes after these basics. |
| 3. Group 3 and Group 4 | Proposed 3.1 Unless/until/without and contextual except; 3.2 no/none/never/cannot and exclusion; 3.3 mixed negative wording, double negatives and the differences among no, not all and not both. Explain meaning before conversion procedure. | Purposeful targeted Group 3 and Group 4 translation, then fresh mixed translation. Use recovered worksheet items only after checking their complete wording and keys; a filename is not a complete bank. |
| 4. Two-way rules and negating rules | Proposed 4.1 if and only if and two independently established implications; 4.2 contextual otherwise and mixed formulations; 4.3 negating an entire universal rule versus writing its equivalent contrapositive. | Distinguish one-way/two-way statements, construct faithful paired rules, and give a counterexample that falsifies a universal. Whole-rule negation must not be hidden inside the AND/OR negation lesson. |
| 5. Use facts and connect rules | Proposed 5.1 rule + fact -> new fact versus rule + rule -> new rule; 5.2 direct and negative chains; 5.3 contrapose before linking; 5.4 shared beginnings/endings and other invalid connections; 5.5 find a missing link, including compound restrictions. | Separate tasks: infer from given rules; apply a supplied fact; decide whether a connection follows; supply an additional rule. Combine targeted sets only when doing so preserves the distinct reasoning task. |
| 6. Some, most and all | Proposed explicit related chapter, because the requested whole-note audit finds substantial quantity material: meaning/existence; valid reversals and exact negations; quantity-through-all chains; majority overlap and fixed comparison groups; invalid chains. These are not all ordinary universal conditionals. | Reuse reviewed Some/Most exercises and the newer complete teaching source. Keep headcount, probability, overlap and universal guarantees distinct. Full inclusion versus a linked quantity course remains a scope decision; the material must have an explicit destination either way. |
| 7. Apply the reasoning | Proposed final application chapter: MBT/MSS; sufficient versus necessary assumption uses; principle; parallel/flaw/parallel flaw. Finish with unseen mixed translation, fact use and linking in context. Teach the relevant conditional move rather than duplicate entire question-type bootcamps. | Reviewed official-question applications and independent mixed transfer. Preserve separate untimed accuracy and later fluency. The existing timed lists need canonical question mapping and suitability review. |

Lesson numbers after Chapter 2 are proposed homes, not newly assigned persistence IDs. Chapters 1 and 2 retain their stable IDs. This seven-chapter recommendation expands the earlier six-chapter proposal solely to give the substantive quantity notes an explicit destination before final applications; no app restructure has happened.

### Source-to-chapter evidence and limits

- **Foundations:** [selected opening source map](2026-10-02-opening-lessons-source-map.md) and [desktop source audit](2026-10-11-desktop-group-1-2-integration-audit.md). Later approved five-lesson structure supersedes the earlier thirteen-section presentation, but each conceptual beat still needs a home.
- **AND/OR:** [current chapter checkpoint](../2026-10-18-conditional-and-or-chapter.md), build-spec, build-log and linked October 19 verification. Local three lessons, four sets/24 items, twelve quiz checks and three films are recorded. Local implementation is not publication proof.
- **Group 3/4:** [assigned cheat sheet](../../students/asia/conditional-logic-cheat-sheet-2026-08-24.html), sections cs-negleft/cs-negright; [legacy note extracts](../../corpus/Curriculum/Conditional%20Logic/Notes/_megadoc_notes_conditionals.md), sources Conditional LOGIC Group 3 & 4.pdf and Logic (3+4).pdf; [homework extracts](../../corpus/Curriculum/Conditional%20Logic/Notes/homework_conditionals.md), Group3&4 homework PT 1.pdf. Several legacy extracts stop mid-sentence; do not count them as fully recovered exercises.
- **Two-way rules/otherwise:** [assigned breakdown](../../students/asia/conditional-logic-the-breakdown-2026-08-24.html), bd-7. Its otherwise counterexample explicitly prevents assuming that every otherwise sentence states a biconditional.
- **Facts/chains:** same breakdown bd-10/bd-11; [Core MBT teaching brief](../../corpus/lectures/logical-reasoning/must-be-true/core/2026-08-27-33013/teaching-brief.md) and teleprompter; legacy Conditional Chains.pdf/Chaining .pdf extracts; current local app direct-linking/no-link/triggering units and Activity Centre banks.
- **Quantity:** [complete newer teaching text](../2026-09-28-recap-format/09-quantity-statements-classroom.md), read in full by the source auditor; existing Some & Most homework is supplementary and truncated. The newer text qualifies few/many contextually, superseding unsafe fixed-cutoff reuse from the older breakdown.
- **Applications:** Core MBT package, Conditional Logic Theory By Question Types.pdf and timed-set passages in the legacy notes, existing SA material and guided-drill catalog. Source presence does not prove every application has enough suitable independent examples.

### Linking drills: preserve the actual task, avoid duplicate counting

Read-only inspection of lsatu-and-or-20261019 finds Activity Centre questions.json has 22 Missing Link and 10 MBT items; content.ts adds eight Linking items. The eight Linking items also ask for a missing link, so their title does not establish a separate direct-chain inference bank. Reused bridge templates and intentional equivalent photo pairs are not independent skill coverage. Existing legacy direct-linking, no-link and triggering units can supply distinct teaching/practice candidates, but are not yet integrated into the numbered course.

Each relevant current legacy direct-linking/no-link/triggering/MBT/SA unit has a guided item and nine practice entries. Candidate examples include MBT1/7 direct inference, MBT2/8 contrapose-before-link, MBT3 negative facts, MBT4 partial AND trigger and MBT5 disjunctive result with an eliminated alternative. Inspect actual items before selecting them. The historical separate sufficient-assumption/content.ts ten-chapter/twelve-exercise asset is absent from this checkout; do not count it as currently integrated. Its older inventory pointer remains historical evidence only.

Audit each candidate against the actual operation: matching a valid join, deriving first-to-last, contraposing before a join, rejecting shared-result/shared-trigger inferences, applying a fact, satisfying a complete compound trigger, or supplying a missing rule. One mixed set can cover several operations; no fixed number of new drills is approved.

### Corrections and completion criteria

1. Group labels vary across older sources. Preserve the verified assigned-note lineage and explain every expression contextually. In particular, permission is not actual entry; cannot and until retain modal/temporal scope; only and the only are different constructions.
2. Do not teach that a rule disappears when its trigger is absent, or that diagramming is useful only when multiple rules can link. Do not turn every otherwise into a two-way rule or every even-if into AND.
3. Maintain an item-level topic map: exact teaching source -> lesson -> worked example -> learner operation -> independent practice -> later application. A topic is unverified until those homes have been checked; a heading or large question count is not completion.
4. Reconcile existing local Chapter 2 against current main before further integration. Preserve routes, assignments, historical work and media. No app edits, provider calls or publication were performed by this query.
5. Remaining gaps: full source recovery for truncated Group 3/4 and chaining worksheets; independent-example sufficiency by operation; final placement of the full quantity chapter; reviewed official-question mapping; exact later lesson/drill consolidation. These are concrete follow-up work, not reasons to omit the topics from the curriculum map.

## 2026-10-25: screenshot resources and full Loophole source audit

Joshua supplied screenshots of Unless Drill, Conditional Reasoning Activity Centre and Conditional Indicators Refresher, and explicitly requested gathering all sources into a rounded bootcamp. [Full build specification](full-bootcamp.build-spec.md) and [Claude review log](full-bootcamp.review-log.md) own the concrete next work. No application build or release is established by this audit.

### Exact app resources behind the screenshots

Inspected root: C:/Users/Joshu/dev/ai-os-projects/lsatu-and-or-20261019.

| Resource | Code/data owner | Reuse and qualifications |
|---|---|---|
| Unless Drill | src/features/quick-drills/unless-drill/UnlessDrill.tsx, UnlessDrillPage.tsx, unlessProgress.ts; conditional-refresher/content.ts helpers | Four randomized sign/order patterns,10s then5s unlock; existing records preserved. This is fluency after instruction, not a substitute for meaning. Refresher embeds the same component. Account fallback/save-error and timeout lock semantics need review before adopting a chapter prerequisite. |
| Conditional Indicators | src/features/conditional-refresher/ConditionalIndicatorsRefresher.tsx, content.ts, Notation.tsx |22sort entries,16diagram entries,12flashcards. Data/control reuse is possible, but old immediate reveal, correct-state retry, exact order checking and browser-local progress differ from refined bootcamp standards. f11 overstates until equivalence. |
| Conditional Reasoning hub | src/features/activity-centre/conditionals/ConditionalPractice.tsx, content.ts, questions.json, DrillEntrance.tsx, practiceStore.ts |62General translation items plus8Linking/22MissingLink/10MBT entries; keep snapshot IDs/history/assignments. Linking/MissingLink overlap in task. General rubric contains contradictory blanket negative placement guidance. |
| Existing Group3/4 teaching | src/bootcamps/conditionals/content/foundations.source.ts:373–434 and generated curriculum | Substantive lesson/method/worked/guided+nine-question units. Better starting point than copying the refresher page wholesale. Use authored sources/generator. |

### Loophole sources read for curriculum purposes

Root: [saved conditional lecture archive](../../Loophole%20Lecture/Conditional%20Reasoning%202026-10-18/README.md). Retrieval used search/open and full source bodies, not just titles. Core auditor read full rendered transcripts and available written notes for Unless, Inclusion, Exclusion, If and Only If, Chaining, Worst Conditional Habit, Why You Shouldn't Diagram the Contrapositive for No Reason, Diagramming Drama and How to Watch. Advanced auditor read full native transcripts for nested conditional conclusions, Some/Most, valid quantity inferences, Not All, Few, SA strategy, Necessary Condition Trick and causal/conditional contrast, with selected parallel-flaw notes. Complete automatic transcripts are not listening verification; diagram-only quiz images were not visually independently checked.

- **Inclusion/exclusion:** give at-least-one, at-most-one and exactly-one explicit homes. Inclusion permits both; exclusion permits neither; together they require exactly one. Their two single-arrow forms can be contrapositives rather than a positive biconditional.
- **Whole-rule denial:** an argument concluding a conditional is falsified by its trigger true and requirement false. Do not confuse this with an outer/inner syntactically nested rule. Explain the actual task rather than reproduce the vendor's ambiguous nested terminology.
- **SA/principle:** keep premises, added assumption and target conclusion separate. A bridge is added, not inferred. Necessary-condition wording is not an answer-location shortcut; a contrapositive can reverse visible placement. A matched result without an established trigger does not apply a principle.
- **Quantity:** include existence, reversible overlap, directional most, exact negations, same-reference-group majority overlap, valid quantity-through-all chains and invalid unrelated-witness/serial-most/different-denominator patterns. Three taught patterns are not all possible quantity reasoning.
- **Strategic diagrams:** meaning before notation; write contrapositives when useful rather than mechanically; diagrams may clarify a single complex rule as well as connect several rules. Causal claims are not automatically invalid, and conditional sufficiency alone does not establish causation.

### Captured practice and routines

[Book Extras conditional sets](../../corpus/loophole-online/bootcamps/conditional-reasoning/README.md):7foundation,14compound/pair/two-way,10Unless,16Some/Most and5integrated questions. These are vendor source entries, not automatically reusable LSAT U questions. Core auditor read full question/choice/final observed feedback bodies for14compound,10Unless and5integrated entries. Final observed site success does not independently validate every key or feedback branch; gated official stimuli are not reconstructed.

[Unless Practice Routine](../../corpus/loophole-online/workouts/unless-practice-routine/README.md) and [Conditional Rehab Routine](../../corpus/loophole-online/routines/the-conditional-rehab-routine/README.md) were retrieved with complete instructions, one page each and no missing linked workout routes. Vendor warmup selects3of4forms, varies letters/selection and derives rather than memorizes; LSAT U's existing drill uses all4. Vendor targets under5s/item and15s/3 are optional fluency advice, not approved gates. Rehab order is Unless -> Question Stem Training3+sections -> Acronym -> Unofficial Diagramming Marathon using previously seen sections untimed. It is remediation, not four new compulsory chapters; protect unseen answer choices.

### Concrete source defects to correct rather than copy

- Unless narration slips between strict/inclusive thresholds before correcting it; preserve exact boundaries.
- Unless source quiz Q8 assumes not-faux means live without an explicit exhaustive category premise; Q9 confuses should with occurrence; Q10 treats typically as universal. Replace with clean original cases.
- Few source alternates some-but-not-most and strict-minority; exactly half separates them. Do not teach a fixed1–49% definition or derive most-not from not-most. Use the newer context-qualified quantity source and explicit quantities.
- Exclusion examples can split subjects awkwardly. Keep the same subject/domain in both conditions.
- Do not import the vendor's blanket all-causal-reasoning-is-bad claim, keyword-only iff shortcut or a universal ban on set visualizations. Label source disagreement and use sound original explanations.

This audit expands the earlier source map rather than replacing Joshua's teaching with vendor doctrine. It does not certify every saved lecture or all question-bank entries; named full reads and remaining limits are the evidence boundary.

### Intake ratings for the expanded course

| Tier | Input | Use |
|---|---|---|
| S for governing structure | Joshua's approved five-lesson Chapter1 decisions, Contrapositive template and later corrections | Preserve exact approved wording where specified. This is governing authority, not proof new pages passed. |
| A for reuse after reconciliation | Current Group3/4/direct-linking/no-link/triggering authored units; local Chapter2 draft and films | Starting point for chapter assembly, with selected-item and behavior review and preserved IDs. |
| A for teaching concepts | Assigned notes, newer full quantity text, corrected MBT guide, complete relevant Loophole lectures | Independently write student lessons; retain source corrections and vendor/Joshua distinction. |
| B for selected practice | General62, linking/missing/MBT40,16refresher diagrams,12recall cards and Book Extras sources | Select by operation, correct feedback and avoid counting duplicates as fresh transfer. Vendor questions are not copied into the app. |
| B for optional fluency/repair | Existing Unless Drill and captured warmup/rehab/marathon procedures | Use after understanding, with safe timer/storage semantics; no compulsory new speed gate. |
| C until recovered | Truncated legacy worksheet/PDF snippets | Use complete individual passages only; do not invent missing keys or count a full bank. |

No collection alone earns a complete-course readiness verdict. Every required skill needs actual teaching, fresh attempts, useful feedback and transfer before acceptance.

