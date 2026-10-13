# Abstract answer-choice drill redesign: Brainstorm / Discovery Notes
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
