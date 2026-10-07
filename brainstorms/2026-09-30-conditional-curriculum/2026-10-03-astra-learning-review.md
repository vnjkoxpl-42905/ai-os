# Make each page require a small act of reasoning

Date: 2026-10-03. Read-only research and source comparison for the Conditional Bootcamp opening through Group 2. Recommendations were sent to the Astra builder before implementation. This record does not establish completed implementation or student learning outcomes.

## What was inspected

Application root: `C:/Users/Joshu/dev/ai-os-projects/lsatu-conditional-bootcamp`.

- `AGENTS.md`, `src/App.tsx` and `src/pages/IntroToLrBootcamp.tsx`: actual Intro to LR registration and gate.
- `src/bootcamps/main-conclusion/content/introToLrPath.ts`: named, ordered lesson and drill destinations.
- `src/bootcamps/main-conclusion/modules/lessons/notes/IntroNotesShell.tsx`: contained reading canvas, local contents navigation, route-change scrolling, previous/next destination titles and descriptions, and completion callback on the next link.
- `src/bootcamps/main-conclusion/modules/lessons/notes/IntroLessonPage.tsx`: concept-specific tools embedded in notes, including anatomy scanning, role labeling, support checks and indicator quizzes.
- `src/bootcamps/main-conclusion/modules/lessons/introGuidedSequence.ts`: note, checkpoint, drill and practice sequencing. This older guided sequence is contextual evidence; it does not supersede the current route map.
- `2026-10-03-claude-pages-build-spec.md` and `references/lsat-teaching-voice-standard.md`: preserved 13-part progression, novice explanations, source boundaries, state/navigation requirements and selected teaching voice.

Actual reference route: `http://127.0.0.1:8097/bootcamp/intro-to-lr/lessons/notes/three-parts-lr-question`. Subsequent note routes include `so-an-argument`, `premises` and `conclusions`. No dedicated Intro to LR development preview was found. The parent opened the actual route and reported **Not assigned yet**. The reference comparison is therefore **source-only**; no visual inspection of the reference lesson itself was established.

## Transfer the teaching decisions, not every shell behavior

Transfer meaningful Next/Back destination titles, a focused reading canvas, revisitable contents, and an explanation followed by a small relevant action. Keep formative choices and card states when returning within the mounted unit. Give the new page heading predictable focus. A new page should introduce a manageable reasoning demand rather than merely cut a long paragraph at an arbitrary point.

Do not transfer IntroNotesShell's completion-on-next behavior to ordinary conditional page flips. The conditional work order requires explicit lesson-read action at the appropriate end. Its animated hero, repeated effects and generic start-card copy are not requirements. Motion should clarify direction, grouping or a learner's action; the static state must teach the same idea.

Useful interaction sequence: show a complete worked example; ask the learner to select the complete condition in a fresh sentence; ask them to repair a reversed diagram and read it back; then give a fresh independent application. Compare equivalent wording while holding the relationship stable. Ask which possible case would break the rule after the relevant inference limits have been taught. Do not introduce transformations or notation before their prerequisite lesson.

For cards, ask for meaning or a reason before the learner flips. Reveal the correct reasoning, allow reflip, and preserve stable card position. Card familiarity and page navigation are not assessed mastery. After both indicator families are taught, mix `if` with `only if` and `only` with `the only` so the lesson heading cannot supply the answer. Feedback should name the precise target or direction mistake and show its repair.

## Evidence used and what it can support

- **Retrieval:** [Karpicke and Blunt, 2011](https://pubmed.ncbi.nlm.nih.gov/21252317/) studied retrieval practice with science material, including conceptual questions. Design inference: invite an actual attempt before showing an answer. It does not show that clicking a flip control by itself improves conditional reasoning.
- **Fading and self-explanation:** [Atkinson, Renkl and Merrill, 2003](https://experts.azregents.edu/en/publications/transitioning-from-studying-examples-to-solving-problems-effects-/) reports two experiments combining fading of worked steps with prompts about the underlying principle. Design inference: gradually remove help while retaining a meaningful question about why the direction follows. Fading alone does not establish broad transfer.
- **Corrective feedback:** [Butler and Roediger, 2008, author-hosted paper](https://psychnet.wustl.edu/memory/wp-content/uploads/2018/04/Butler-Roediger-2008_MemCog.pdf) examines feedback after multiple-choice testing and the risk of learning wrong alternatives. Design inference: explain why the selected wrong answer fails and provide the correct relationship; a color change alone is inadequate teaching.
- **Mixed practice:** [Rohrer and Taylor, 2007, university publication record](https://digitalcommons.usf.edu/psy_facpub/1767/) reports mathematics experiments involving spaced and mixed practice. Design inference: after initial teaching, mix confusable conditional formulations so learners must choose the appropriate interpretation. This is not direct evidence about LSAT instruction.
- **Instructional synthesis:** [IES, Organizing Instruction and Study to Improve Student Learning](https://ies.ed.gov/ncee/wwc/practiceguide/1) recommends worked-example/problem alternation, integrating concrete and abstract representations, combining verbal and graphical explanations, and retrieval and spacing. These support purposeful diagrams and repeated reasoning opportunities. Same-session revisiting is not evidence of a longitudinal spaced-review system.

No retention percentage, score gain, optimal pacing interval or guaranteed outcome is claimed. These are bounded design inferences from general learning research. Authenticated student persistence, production behavior and learning effectiveness were not evaluated by this review.

## Post-build teaching and retention pass

Pass 1 performed on the initial local implementation on 2026-10-03 while the builder continued test and pagination work. This was an application-source review, not a browser pass. Findings were sent directly to the builder and parent; the parent owns browser verification. Line references below identify the reviewed snapshot and can move during corrections.

Reviewed `LessonPages.tsx`, `StudyDeck.tsx`, `CounterexampleLab.tsx`, `indicatorFlashcards.ts`, all rendered sections and exercise data in `ConditionalOpeningLesson.tsx` and `ConditionalReferenceSequence.tsx`, relevant pagination/reference CSS, and the newly added Demon source map. The map explicitly identifies original adaptations and the source's negative-condition discrepancy. No screenshot or video inspection is inferred from reading that map.

### Corrections requested

1. **Temporal meaning in a reviewed card.** `indicatorFlashcards.ts`, card `g2-only-when`, starts from a light *switching on* only when the drawer is closed, but asks what follows when the light *is on*. The drawer could open after the switching event. Change the front to “The reading light is on only when the desk drawer is closed,” keeping the state consistent with the question and answer. A programmatic comparison found all 25 cards and every per-card field identical to the reviewed JSON at review time. This error was inherited from the reviewed derivative, not introduced by the builder. Keep that archived JSON unchanged and record the local correction privately.
2. **Restore the reference style ancestor.** `ConditionalOpeningLesson.tsx`, `OpeningLessonBody`, flattens `conditionalReferenceContent().props.children`, losing the enclosing `.cr-sequence`. `reference-sequence.css` line 1 defines its CSS variables there; lines 2, 8, 11, 31, 32 and 34 depend on that ancestor for reference styling, controls, reduced motion and narrow layouts. Preserve the ancestor around orientation pagination, then recheck the actual rendered mobile and static states. This is a functional presentation regression, not merely a preferred aesthetic.
3. **Remove teacher-facing policy from the reading.** `ConditionalReferenceSequence.tsx`, stage 10 timing FAQ (initial lines 297-299), tells students their teacher can add timing to medium or advanced practice. Remove that implementation/policy sentence; retain the useful advice to establish accuracy before pursuing speed. The accepted scope keeps assignment/difficulty explanation out of the lesson.
4. **Subdivide the two remaining long stages.** Stage 8 (initial lines 255-281) combines diagram roles, moved clauses, `only`/`only if`, target-before-indicator, construction and a fresh check. Use meaningful subpages while keeping stage 8 and all its content. Stage 13 (initial lines 325-330) has six original-plus-contrapositive items; give each item or a small pair its own revisitable page. The six original exercise records were present and logically intact at review time. Builder reported this subdivision already planned.

### Teaching refinements requested

- The identical Drawer R counterexample initially appears at the end of all four units. Retain a stable first demonstration, but use a fresh subject or equivalent-wording challenge later, or label the repeat as recall. Repeating the exact solved answer cannot demonstrate transfer to a fresh case. The current lab correctly distinguishes an allowed possible case from an asserted existing ticket.
- Stage 3's page title “Different words can give you the same connection” is vague when isolated in navigation. Prefer “Different words can preserve the same rule,” and name the concrete locker implication in nearby prose. The opening definition itself already explains the meaning; the word “connection” does not require indiscriminate removal where its referent is clear.
- Change “Say the rule without the scaffold” to “Say the rule without the clues” to keep instructional jargon off the student surface.
- Recall decks currently follow all unit prose. A foundation recall opportunity can move earlier **after** role and notation prerequisites, and a mixed Group 2 recall can follow the comparison section. Do not place arrow-bearing foundation backs before notation has been introduced.
- The new ticket activity is concrete. Its comment's concrete-to-abstract attribution does not establish that the abstract note has a new negative-condition practice application. At the parent's request, sent a specific fresh adaptation to place after stage 9: “If a room is showing a film, it is not hosting a workshop” (`F → ~W`). Given only `~W`, compare a film/no-workshop room with a no-film/no-workshop room; both are allowed, so film status remains open. Separately ask what `W` establishes: `~F`. This gives the abstract source insight a visible teaching use while preserving the skeleton and keeping sign-pattern prerequisites first.

### What passed the source review

- All 25 reviewed card IDs/order and per-card fields matched the supplied derivative before the requested temporal correction. Group 1 and Group 2 cards preserve complete qualifications and the distinction between obligations and completed actions. No Group 3/4 or chain cards were introduced.
- The initial placement of each deck respects its prerequisites: foundation after notation/roles; expression decks after their individual explanations. The `must` obligation explanation precedes its recall card.
- `StudyDeck` renders the answer only when flipped, rather than exposing a visually hidden answer before reveal. Navigation resets the next card to its question. Saved-card wording makes no claim of assessed mastery or a longitudinal scheduling system.
- Hidden mounting in `LessonPages` preserves component state across page returns; unit-keyed remounting resets units. End-only footer rendering separates reading navigation from the explicit lesson-read action. Browser and test proof remain separate responsibilities.
- Existing practice includes choices with reasoned feedback, target identification, direction construction, a four-case explorer, sign-pattern work, fresh expression examples and six paired-diagram items. The counterexample builder adds a different reasoning action rather than another fill-in-the-blank task.

These findings are not final approval of the evolving snapshot. The builder must confirm corrections and the parent must complete fresh tests and browser proof. No app edits were made by this reviewer.

## Correction recheck and interaction acceptance tests

Rechecked the builder's frozen source on 2026-10-03. The temporal card now consistently uses “is on,” with a private correction comment and the archive unchanged. `.cr-sequence` is retained by the page shell. The teacher timing sentence is removed. Stage 8 has three subpages and stage 13 has six exercise subpages. Foundation recall follows stage 8, after roles and notation. The concrete ticket activity now appears only in orientation; Group 2 has fresh mixed envelope-wording practice. `NegativeCaseLab`, inserted after stage 9, explicitly contrasts two allowed `~W` cases with the separate `W → ~F` inference. The stage 3 heading and scaffold wording were revised. No new logic blocker was found in that correction recheck.

Parent then granted this reviewer exclusive ownership of the new `src/bootcamps/conditionals/components/LessonPages.test.tsx`. Five meaningful acceptance tests were added; no production application files were edited by this reviewer. They verify current-page accessibility and heading focus, checked-case retention, actual lesson card index/flip/saved state across page navigation, next-card answer reset, explicit end-only reading completion, real unit-remount state reset, and the negative-room exercise's wrong/incomplete/correct paths with gated contrapositive feedback and retained answers.

Command: `npm run test -- src/bootcamps/conditionals/components/LessonPages.test.tsx`.

Latest result: **5 tests passed**, exit 0, total 7.14 seconds. Existing Browserslist age and React Router future-flag warnings appeared. This is automated DOM/interaction proof, not a replacement for the parent's responsive, keyboard and motion browser passes. Production/authenticated persistence and student learning outcomes remain unverified by this review.

## 2026-10-04 concept-page pacing audit after course reconstruction

Read-only application review. Compared the current nine-note/four-lab composition with actual Intro to LR source, using `references/lsat-teaching-voice-standard.md` as the writing authority. Parent separately inspected authenticated live IntroLR; this reviewer did not repeat that browser inspection. Findings below concern source composition and instructional judgment, not measured learning outcomes or timings. No application edits were made.

### What the reference actually divides

`src/bootcamps/main-conclusion/content/introToLrPath.ts` organizes eight concept notes, three standalone labs and two practice sets. `modules/lessons/notes/IntroLessonPage.tsx:451–539` keeps the Premises definition, contrast, indicators and short checked application together. Conclusions (`:546–651`) similarly joins the claim, language and checked identification. Five Types (`:654–756`) teaches examples, then a switchboard, followed by its separate lab in the path. These are conceptual articles, not one example per route. The conditional nine-note/four-lab structure now follows that useful pattern. Keep the dedicated meaning, sufficient and necessary destinations; none needs padding merely to equal the length of an indicator lesson.

The reference is not uniformly better: its Beyond Premises note has no rendered role-labeling exercise, despite unused imports; its structure note's ClaimBucketInspector reveals definitions rather than assessing classifications. Do not copy those gaps or count them as independent practice.

### Ranked findings and proposed corrections

1. **Narrow the must-arrow lesson to its stated job.** Evidence: `OpeningCourseContent.tsx:121` imports all of reference stage 8 (`ConditionalReferenceSequence.tsx:259–285`). Besides arrow roles and a moved if-clause, that section already teaches both indicator families, only versus only if, and required/requires target placement. Those topics recur in the following indicator notes and whole-meaning note. Keep the arrow meaning, one raffle diagram, moved if-clause, incremental writer and its check here. Move the full only/only-if comparison to Necessary-condition words and target-before/after contrast to Keep the whole meaning. This is a pacing recommendation grounded in visible repeated content; it is not a claim that the earlier material is logically wrong.

2. **Make the first lab transfer the ideas instead of immediately replaying the same questions.** `FoundationPractice` (`OpeningCourseContent.tsx:74`) extracts the four exact ReferenceQuestion elements from stages 1, 2 and 4. Learners have just answered these on the preceding three notes. Two further tasks add value: a fresh collected-delivery example and a counterexample choice. Keep one raffle retrieval question as a bridge; replace the other three repeated prompts with fresh, short cases testing rule versus fact, sufficient versus necessary, and what stays open. Keep notation out. The voice standard says to repeat an anchor when the repetition changes the learner's view, rather than merely repeat wording.

3. **Make the mixed lab genuinely mix diagram production.** `OpeningCourseContent.tsx:129` runs `GroupPractice` only for group 2, so its target finder and diagram builder use the seven necessary-family examples. `CounterexampleLab.tsx:28–50` then supplies four envelope equivalence judgments, including if and the only. That is meaningful comparison, but the bulk of the run still announces the family before every translation. Keep the envelope contrast; add a short alternating set of sufficient- and necessary-family sentences with the group label withheld, requiring target identification and arrow construction. Do not add another destination. This better tests the stated mixed-family purpose; no universal benefit is asserted.

4. **Give Keep the whole meaning one visible progression.** `OpeningCourseContent.tsx:124` concatenates five substantial blocks: target-position lesson, two separately titled Keep the whole condition sections, only/the only comparison, and Personalized If/Then plus What Test. The two qualification cases are useful contrasts, not identical material, but the repeated heading restarts the explanation. Combine them as one paired qualification check (late applicant/current pass), then present target position, only/the only, and the imagined-case test as successive checks on one translation process. A short orienting sentence should explain what each check catches. Prefer this consolidation before splitting another page.

5. **Signal the intended expression-selector path before the cards.** `IndicatorNote` (`OpeningCourseContent.tsx:59–71`) defaults to expression one, keeps six panels hidden, then presents the full 10- or 11-card family deck. A reader can naturally scroll to cards without opening the other six named examples. This is an affordance issue, not grounds for a mastery lock. Add concise guidance to work through each expression, and a local next-expression affordance or viewed-position cue. Offer the deck as retrieval after those examples. Keep manual selection and revisit state.

6. **Use one fresh bridge case in the early definition notes, not more explanation.** The first three notes correctly use the raffle to distinguish rule/fact, enough and required, and already include checks. The fresh case currently arrives in the lab. Optionally add one compact comparison to Necessary (required result versus an earlier entry requirement) before its final check, using the existing temporal clarification as the model. This is a lower-priority design preference; the current definition is accurate and the lab already supplies transfer.

### Preserve during revision

Keep nine genuine concept destinations and four practice transitions; no return to the 70-page reader. Retain the approved raffle anchor, first-three-note notation boundary, complete expression inventories and modality caveats, all 25 cards, both Demon-derived exercises, four cases, sign patterns and six paired final exercises. Preserve attempt-before-feedback, retry and retained answers. Do not interpret reviewed reading or card flips as assessed mastery. No route, assignment, backend or completion-policy change is proposed by this pacing audit.

Recommended order: resolve findings 1–3 first, then consolidate whole-meaning and improve expression navigation. Finding 6 is optional. The evidence supports improving task boundaries and repetition, not a particular word count or a guarantee of retention.


## 2026-10-04 audit disposition: implemented by Claude

All five primary recommendations implemented locally through actual Claude build and one correction round. Independent read-only source reinspection approved the bounded four-file change after repairing omitted depot qualification and phone intake timing, plus terrace/cafe feedback. Host214tests and browser24responsivechecks passed; final typecheck/build passed. CLI inspector was blocked before file access, so no CLI approval claim. [Complete authorship, hashes and proof](claude-pacing-20261004/build-log.md). Optional sixth bridge-example suggestion was not added; existing fresh lab supplies transfer.
