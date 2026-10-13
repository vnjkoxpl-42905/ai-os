# Abstract answer-choice drill redesign: Brainstorm / Discovery Notes
Date: 2026-10-13 · Goal: pin down the word bank, question-then-breakdown format, and AI grader for the Abstract bootcamp's answer-choice practice
Status: in progress
Context sources: C:\Users\Joshu\Downloads\role_question_answer_choices_exercise_format.html (15 exercises); lsatu-abstract worktree `src/topics/abstract/data/{modules,terms,translatorItems,breakdownDrill}.ts`, `lib/coach.ts`; `supabase/functions/activity-coach/`; brainstorms/2026-10-12-abstract-bootcamp-fix.md

## Facts found before the interview (verified on disk)
- The 15 answer choices in the source file already live in Module 3's Quiz as `TRANSLATOR_ITEMS` (verbatim stems, `idealTranslation`, verbatim walkthroughs).
- Module 2 "LSAT Words You Must Know" already teaches the terms (subtitle says 13; `terms.ts` holds 7 with MC options).
- Module 3 Drill = `BreakdownDrill` (tap direction words, pick the conclusion letter). That is the drill Joshua saw.
- `lib/coach.ts` is rule-based token overlap; the Anthropic/LLM coach was deferred ("v2.1").
- `supabase/functions/activity-coach` already does source-bound free-text grading via the Gemini proxy. Extending it means an Edge Function deploy, which goes through Lovable (credits; needs Joshua's confirmation).

## Summary / key decisions
(pending)

## Q&A log

## Open flags (pending input)
- Rename "Abstract" in the Library? (asked 3x earlier, unanswered) -> Joshua
