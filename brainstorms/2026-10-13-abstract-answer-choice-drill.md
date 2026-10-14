# Abstract answer-choice drill redesign: Brainstorm / Discovery Notes
## Latest release and assignment checkpoint, 2026-10-13

Joshua explicitly requested making the course easy to follow, ensuring account/homework progress tracking, and assigning it to Gianna. The revised frontend is now published at https://lsatprep.study/topics/abstract. Release HEAD is 289582910708a66dfcb794ce25c26be227409651; PR #210 merged; Lovable ingested the exact SHA before the free publish control was called. New live assets contain the homework instructions, original applied question and Classroom tracking.

The assignment is verified for Gianna Jean (giannajean005@gmail.com): Classroom item dd42a851-5af5-49e9-af7c-b097db98f379, visible, assigned, correct /topics/abstract route and abstraction registry ID. Inbox, bell and email notifications succeeded. No due date was invented. See students/gianna/assignment-log.md for exact readback and release evidence.

Account-scoped caches, saved-note restoration, save-first attempts, seven-module Classroom completion and honest teacher accuracy are implemented. Completion requires saved notes and current drills; Module 3 requires all fifteen written exercises, while review-only work is separate and quizzes are optional. Final Set remains outside the required path. Browser acceptance recovered and now includes M6/M7 lessons/practice, the final dashboard return, homework instructions at 375/800/1440/docked574 widths, and the teacher progress screen. Relevant checks passed: 39 Abstract/progress/metrics tests plus 5 registry tests, typecheck, production build and whitespace check. Gianna's first real interaction has not been simulated; the assistant did not impersonate her or write test progress into her account. Earlier local-only checkpoints below are historical.

## Current verification checkpoint, 2026-10-13

Joshua's latest scope keeps all seven modules and rebuilds the teaching in Modules 4-7. Local implementation is present: M4 maps the original John/David example; M5 works through the tax-rate objection; M6 teaches exact strength and compatibility traps; M7 integrates the process on the anonymous-source analogy. M5-7 each have one original five-choice practice question, new attempt IDs, and no duplicate quiz layer. Old completion records cannot complete these new activities, and a single question cannot grant mastery. The original fifteen source choices and breakdowns remain exact and can be reviewed without typing.

Final local checks passed: 30 tests across nine Abstract test files, TypeScript typecheck, production build including pre/postbuild checks, and diff whitespace check. Root browser checks verified M4's full matching lesson and M5's lesson, reveal, full question, feedback, saved answer and completion. The final typography pass and M6-7 browser acceptance remain unverified: the interrupted app reset browser bindings, and reconnecting was rejected by the browser security policy. No workaround was attempted. The local Vite server had also stopped; root restarted it and verified localhost port 8080 listening. Signed-in account acceptance, publication and final course parity are not claimed. The defective synthetic Final Set remains outside the required path. Nothing was committed, pushed or deployed.

Earlier discovery and checkpoints below are historical; newest explicit scope and source-fidelity corrections take precedence.

Date: 2026-10-13 · Goal: pin down the word bank, question-then-breakdown format, and AI grader for the Abstract bootcamp's answer-choice practice
Status: complete (shared understanding confirmed 2026-10-13; building)
Context sources: C:\Users\Joshu\Downloads\role_question_answer_choices_exercise_format.html (15 exercises); lsatu-abstract worktree `src/topics/abstract/data/{modules,terms,translatorItems,breakdownDrill}.ts`, `lib/coach.ts`; `supabase/functions/activity-coach/`; brainstorms/2026-10-12-abstract-bootcamp-fix.md

## Facts found before the interview (verified on disk)
- The 15 answer choices in the source file already live in Module 3's Quiz as `TRANSLATOR_ITEMS` (verbatim stems, `idealTranslation`, verbatim walkthroughs).
- Module 2 "LSAT Words You Must Know" already teaches the terms (subtitle says 13; `terms.ts` holds 7 with MC options).
- Module 3 Drill = `BreakdownDrill` (tap direction words, pick the conclusion letter). That is the drill Joshua saw.
- `lib/coach.ts` is rule-based token overlap; the Anthropic/LLM coach was deferred ("v2.1").
- `supabase/functions/activity-coach` already does source-bound free-text grading via the Gemini proxy. Extending it means an Edge Function deploy, which goes through Lovable (credits; needs Joshua's confirmation).

## Summary / key decisions
1. Module 1 Note ("Why Abstract Answer Choices Feel Hard") stays as is; Answer Choice Traps (Types 1-3, Type 3 weighted) is added as a closing section, polished with no references to chapters/the book.
2. The seven-step box gets its own page right before the Module 3 drill, formatted as in the source box (no acronym), original wording and emphasis.
3. Module 3 = steps page, then the 15-item answer-choice drill. Tap-the-chips drill retired; old translator Quiz cut (same content).
4. Each item: see the answer choice -> tap keywords (step 1) -> write plain-English meaning (step 2) -> AI grade (verdict Got it / Partly / Missed + 1-2 sentences naming the misread keyword) -> one retry on a miss -> seven-step walkthrough for that choice -> the breakdown, identical apart from light polish and removal of chapter/prior references.
5. Word bank before item 1, collapsible during every item; covers every keyword in the 15 choices; drafted definitions flagged for Joshua's approval.
6. Claude drafts the 15 walkthroughs from the breakdowns only; Joshua approves before live.
7. Grader Edge Function: Claude writes the code; Joshua deploys it himself.

## Q&A log
### Round 1
Asked Q1 (which part changes), Q2 (what the student does before the breakdown), Q3 (word bank placement), Q4 (which words), Q5 (grader strictness), Q6 (gating). Joshua answered with new direction instead of item by item:
- Captured: the Note before the drill = `C:\Users\Joshu\Downloads\answer_choice_traps_formatted.html` (Answer Choice Traps: Type 1 half right/half wrong, Type 2 describes something that did not happen, Type 3 too vague/abstract). "The higher focus is keeping the last part of this focused", i.e. Type 3.
- Captured: the 7-step box ("When faced with an abstract answer choice, this is what we do") gets its own page, each step numbered, with an acronym, worded "as it was on the page".
- Captured: integrate the 7 steps into the 15 answer-choice items "on top of" each answer breakdown.
- Captured: keep the 15 answer-choice breakdowns identical, "slightly polish", with no reference to chapters or anything prior (e.g. "See PT43-S3-Q23 in the Find the Conclusion chapter", "we briefly touched upon ... in the last chapter", "throughout the book").
### Round 2
Asked Q7 (DECODES acronym), Q8 (how steps sit on each item), Q9 (who drafts walkthroughs), Q10 (which Module 3 part), Q11 (word bank/grader/retry bundle).
- Captured (overrides Round 1's "Note before the drill" placement): "keep the part Why Abstract Is Hard as we have it now but add this on top of it on the note we have." Module 1's existing Note (`why_hard`, "Why Abstract Answer Choices Feel Hard") stays unchanged; the Answer Choice Traps content is added to it, positioned "on top of" the current note.
- Tentative (my reading, to confirm): "on top of" = Traps content first, existing Why Hard note after it, in the same Module 1 Note.
- Not answered: Q7-Q11. Carried to Round 3.

### Round 3
Asked Q12 (order inside Module 1 note), Q13 (steps page lives in Module 3 before the drill), plus Q7-Q11 bundle.
- Captured Q7 (supersedes Round 1 "with an acronym" and my DECODES recommendation): no acronym. "Make it like this ... make this clear and format as you see it here prior to the drill." The steps page reproduces the original box: heading "When faced with an abstract answer choice, this is what we do:", seven numbered steps, original wording, original emphasis (bold+underline "extract any keywords"; bold noun / verb / adjective/adverb; underline "Read the answer choice again"; bold+underline "Don't be afraid to go back and forth").
- Captured Q13 (partly): the steps page sits "prior to the drill".
- Not answered: Q12, Q8, Q9, Q10, Q11. Carried to Round 4.

### Round 4
- Captured: "I'll add the edge function myself, have it be the same and have the rest ... think methodically how to place this and make this powerful and highest quality." = all Round 4 recommendations (Q8-Q12) accepted; Joshua deploys the Edge Function.

- Round 1 not yet answered: Q1 (which Module 3 part this replaces), Q3 (word bank placement), Q4 (word list), Q5 (grader), Q6 (gating). Carried to Round 2.

## Open flags (pending input)
- Rename "Abstract" in the Library? (asked 3x earlier, unanswered) -> Joshua


## Session checkpoint: local draft build in progress, 2026-10-13

Joshua confirmed: **Keep the existing four-step notes in Modules 3 and 7 and retain Module 7’s repeated choices for this draft.** This resolves those teaching choices for the local draft; it does not approve new walkthrough or definition wording.

The local Module 3 redesign is being built in `C:\Users\Joshu\dev\ai-os-projects\lsatu-abstract`. Content now includes all 15 exact source choices, the original seven-step procedure with its emphasis, lightly polished source breakdowns, seven-step applied walkthrough drafts, and a word bank covering every selected keyword. The bank has 45 terms, including 35 newly drafted definitions awaiting Joshua’s approval. Grading requirements preserve choice meaning without demanding details from examples the learner has not yet seen.

Review artifact: [Abstract answer-choice draft for Joshua review](2026-10-13-abstract-answer-choice-review.md). It records source hashes, draft meanings and definitions, walkthroughs, grading requirements, and source limitations.

Status remains **local draft build in progress**. No new content approval, commit, publication, deployment, or AI runtime validation is claimed. Joshua retains deployment of the grader Edge Function. Existing source records and prior checkpoint text are preserved.


### Verification addendum, 2026-10-13

Root verified the final local draft with typecheck and production build (both exit 0), six focused tests passing, and a clean diff check. Browser checks covered Module 3 steps, word bank, item 1 keyword taps and written response, an honestly ungraded unavailable-grader fallback, walkthrough and breakdown, then saving and moving to item 2. Module 1 Traps content was present in the DOM; 375px CSS checks showed no horizontal overflow. Item-start scrolling reset to 0, and navigation between modules reset to overview.

Preview progress is session-only and clears after reload. Signed-in account resume was not tested. No deployed endpoint, AI verdict, or AI retry runtime was tested. This remains a local draft pending Joshua’s content approval; nothing was committed, deployed, or shipped. Final parity is not certified because the skill’s approved quality reference remains unavailable.

### Navigation crash correction, 2026-10-13

The earlier effect-only stage reset was insufficient: switching from Module 7 drill question 3 to Module 1 briefly rendered Module 1's two-item drill with the old question index and crashed while reading an undefined stimulus. Root reproduced the blank page in the browser. The module view now remounts synchronously by module identity before the new module renders; module/stage navigation also resets scroll position.

Root reproduced the same Module 7 question 3 to Module 1 transition after the fix: Module 1 overview and its first drill question opened successfully. A focused React regression covers the longer-to-shorter module switch. Focused tests now pass 7/7; typecheck and production build both exit 0, including prebuild/postbuild checks; diff check is clean.

This corrects the earlier cross-module verification claim. The implementation remains a local draft; content approval, signed-in acceptance, deployed AI grading, publication and parity are not claimed. No commit, push or deployment was performed.

### Newest source-fidelity correction, 2026-10-13

Joshua's newest explicit direction supersedes the earlier active word-bank, AI-verdict/retry and drafted applied-walkthrough flow. The authoritative exercise is now `C:\Users\Joshu\Desktop\role_question_answer_choices_complete_transcription.html`. Its four original introduction paragraphs and all 15 original answer-choice/breakdown sections are preserved exactly, including source definitions, examples, emphasis and chapter references. The source fixture and fidelity tests compare every section, not merely selected excerpts. The old drafted word bank, applied walkthroughs and Edge Function remain preserved as inactive artifacts; they are not part of the exercise or publication approval.

Each item displays the full untappable original choice, then two written responses: what must be present for the choice to be correct, and the student's own example argument identifying the described statement. Both responses are required before Show breakdown. That action immediately reveals the original breakdown, without AI judgment, retry gate or a drafted walkthrough inserted first. Source examples retain their original underlining. The previously approved exact seven-step page remains before the exercise. Invented Module 1 introduction and Module 3 routine/example material were replaced with the source introduction/instruction; other module scope was not cut or consolidated.

Both written responses are saved together through the existing translator record. A separately tagged source_exercise_ungraded attempt records practice completion without a correctness score. Only this newest task format counts for resume and source-exercise progress; older coach/self-check attempts with the same IDs remain preserved but do not skip the new written work. Completed work opens an explicit Practice again state. Ungraded work does not enter accuracy, confidence, trap statistics or Module 3 mastery.

Final checks: 17 focused tests pass across four files, covering exact-source fidelity, two-response reveal gating, source rendering, saving/failure, format-aware resume, intentional replay, and module-navigation isolation. Typecheck and production build both exit 0; prebuild/postbuild checks and diff check pass. Root browser verified item 1's two fields, disabled-until-written reveal, immediate original breakdown with underlined example, save/advance to item 2, and no horizontal overflow at 375px and 300px.

Local implementation only. No commit, push, deployment, paid model request, signed-in account acceptance or final parity claim. The inactive grader was not invoked. Prior preservation decisions above are historical where they conflict with this newest correction.

### Answer-choice presentation restyle with 21st.dev, 2026-10-13

Joshua authorized a more visually stimulating hierarchy and clearer original source examples. Root explicitly used the 21st.dev MCP search/get_component workflow and retrieved ruixen.ui Timeline-02, demo 5534: https://21st.dev/@ruixen.ui/components/timeline-02. Its actual source pattern was adapted locally in ChoiceResponseTimeline.tsx: timeline rail and numbered nodes, existing shadcn Card/CardContent, and the fetched opacity/y entrance pattern with reduced-motion support. No hosted AI generation, added runtime service or package installation was needed. Component provenance is recorded in the code comment.

The unchanged original answer choice now appears in a larger, readable nonitalic question card with a steel-blue heading and Amber Slate accent. The existing two response prompts use numbered timeline panels. Original breakdown HTML is untouched: source definitions appear as steel-blue cards with prominent source term headings; source example paragraphs are bounded slate cards with orange borders; original underlined statements retain underlining with stronger visual emphasis. Paragraph spacing and reading width were adjusted. No new teaching examples, definitions, grading or curriculum consolidation was introduced.

This presentation work preserves the newest unrestricted Show breakdown behavior: students may reveal and continue without writing; viewing alone does not save empty work or mark source exercises complete. The eight UI tests include reviewing all 15 source breakdowns without recording empty attempts. Final verification passed: 18 focused tests across four files, typecheck, production build including prebuild/postbuild checks, and diff check. Root browser inspected question/response/source-definition/source-example layouts at actual CSS widths 375px, 800px and 1400px, plus the docked desktop preview; no horizontal overflow was found. Screenshots were saved by root.

Local preview only. No commit, push, deployment, paid generation, new source-content approval or final parity claim. The inactive draft bank/walkthrough/Edge artifacts stay preserved and unused.

### Separate review progress, saved drafts and contrapositive reading benchmark, 2026-10-13

Joshua requested a full 15-choice run with retained progress, plus stronger instruction hierarchy using the existing contrapositive note as the visual standard. The implementation now keeps reviewed breakdowns separate from completed written exercises. Reveal records an actual rendered source breakdown as source_breakdown_reviewed; written requirements/example work uses source_exercise_ungraded. Both tags are ungraded and excluded from accuracy, trap/confidence statistics and mastery. Reviewing cannot replace or erase written evidence, and the end screen says how many breakdowns were reviewed and how many written exercises were saved instead of generic module completion.

A validated, source-fingerprint-versioned session stores current choice, revealed state, reviewed/practiced IDs and per-choice unfinished text. Preview and each account have separate keys. Typing is saved immediately; browser progress and drafts survive navigation/reload. Existing cloudMirror provides draft mirroring, and existing drill-attempt APIs store signed-in review/written history without a schema migration. Account-owner hydration gates, per-await owner guards and confirmed-success source attempts prevent old-account state or failed optimistic saves from becoming another account's progress. Delayed cloud restoration does not overwrite an active draft. Storage/account failures are surfaced; reviewed drafts remain editable for continuing written work.

The visual benchmark was inspected in the current checkout: ContrapositiveNote in src/bootcamps/conditionals/components/OpeningCourseContent.tsx with opening.css, opening-course.css and contrapositive-visuals.css. Its reading hierarchy was adapted into the source exercise: 19px desktop body with 1.8 line height, regular Georgia section headings, navy definition panels, selective bold and distinct requirement/example colors. No conditional examples, media or teaching were imported. The exact source choice/breakdown HTML and order remain unchanged. The completion report now separates reviewed breakdowns from written work and does not describe ungraded reviews as incorrect graded drills.

Final focused checks passed: 24 tests across six files, including all 15 review-only items, finished-summary remount, unfinished drafts/current reveal, separate written saves, account switching during hydration and pending writes, failed-review retry, source fidelity and navigation regression. Typecheck, production build (including prebuild/postbuild verification) and diff check all passed. Root's local browser run verified reviewed counts 1 through 15 with written count 0, a 15-reviewed/0-written summary that survived reload/reopen, partial item-1 draft and revealed-state restoration, then item-1 written practice yielding 15-reviewed/1-written with item-2 cursor/count retained after reload. Desktop/docked instruction emphasis was clear; actual 300px and 375px viewports had no horizontal overflow. Root left the preview at item 2.

This is local preview acceptance only. Signed-in cross-device/account cloud persistence was not accepted in a live browser; its API integration and account-isolation cases were tested locally. No commit, push, deployment, migration or paid model call. No final bootcamp parity claim.


### Source-grounded lecture framing draft, 2026-10-13

A substantive review draft now lives in [the existing answer-choice review artifact](2026-10-13-abstract-answer-choice-review.md#lecture-proposal-understand-the-choice-then-make-it-concrete). It proposes an opening, source-example-based transitions after choices 3 and 9, and a closing after choice 15. Its source map connects the Desktop Role lecture to the corpus Advanced Parsing answer key and bounded Method/Flaw strategy evidence. New connective wording is explicitly draft; reused source examples are exact HTML. All 15 source breakdowns remain unchanged.

The proposed learning task is decoding the choice, listing its requirements and building an argument with a statement that fulfills them. Later full-stimulus matching and a broader methods bank stay outside this proposed lecture pending Joshua’s scope answer. No extra examples or 17-method lesson sequence were invented. No app code, publication, commit, deployment or user memory was changed by this drafting task.


### Retain and rebuild Modules 4–7: current scope and implementation, 2026-10-13

Joshua explicitly chose to keep the later modules and rebuild their teaching. This supersedes the earlier course-ending-at-M3 assumption. The original four introduction paragraphs and fifteen answer-choice breakdowns remain exact. Four substantive source-grounded lesson drafts are at the top of [the review artifact](2026-10-13-abstract-answer-choice-review.md): M4 maps every requirement to the original John/David exchange; M5 works through PT103-S1-Q18; M6 diagnoses precise qualification/relationship traps in PT139-S1-Q23; M7 applies the whole procedure to fresh PT118-S4-Q12. All three full question texts, prompts, choices and keys were verified in the captured local source database dated 2026-08-03. New connective explanations remain review drafts.

Root approved these drafts for local implementation, and notes/build agents are applying them. Implementation and checks are still in progress; this checkpoint does not mark the work complete. The legacy Final Set is held because defective synthetic questions are not accepted source practice. No commit, publication, deployed grading, signed-in account acceptance or final parity claim is made. Historical narrower scope records above stay preserved but are superseded by this explicit decision.
