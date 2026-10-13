# Abstract bootcamp fix: Brainstorm / Discovery Notes
Date: 2026-10-12 · Goal: agree what "fix the Abstract bootcamp" means before any change, so it reaches the solid bar (wiki/tasks.md: "Bring the abstract bootcamp up to the solid bar (in progress, needs work).")
Status: in progress
Context sources:
- App: `../ai-os-projects/lsatu/src/topics/abstract` (route `/topics/abstract`, legacy `/bootcamp/abstraction`), ~10.8k lines. Live on lsatprep.study; listed in Teacher Workspace > Library > Bootcamps as "Abstract" with blurb "Strip-down, decode, match-to-stimulus, method patterns, and trap catching."
- Gold standard: Contrapositive lesson page, `.claude/skills/bootcamp-builder/references/teaching-preferences.md` ("Gold standard" section) + `wiki/COPY-CORRECTIONS.md`.
- Corpus: `corpus/Curriculum/Abstract/` (Homework: parsing worksheets/answer keys, Level 1 Answer Parsing and Mapping, Translation and Cluster Sentences quiz; Notes).

## What exists today (facts found, not decisions)
- 7 modules, each Note + Quiz + Drill: M1 Why Abstract Is Hard · M2 LSAT Words You Must Know (7 terms) · M3 Stimulus + Keyword Extraction (core method) · M4 Match To The Stimulus · M5 Spot The Method (17 patterns) · M6 Catch The Traps · M7 Put It Together (18-item gauntlet). 20 drills, plus Flashcards, Methods Library, Timed Final Set, Completion Report.
- Visual identity: neo-brutalist (electric yellow, cream paper, 4px black borders, uppercase italic), unlike Intro to LR / Conditionals.
- Lesson interactions are mostly "Reveal X" button cycles (e.g. Decode Practice: Reveal Keywords > Reveal Meanings > Reveal Translation > Reveal Checklist). The gold standard rejects reveal-cycling as practice.
- Teacher Library preview card renders mostly blank (Joshua's screenshot 2026-10-12).
- Supabase tables exist for progress/mastery/flashcard reviews (migrations 20260514-20260515), so live student progress may exist. Check pending.

## Summary / key decisions
(none yet)

## Q&A log
### Round 1
Asked: Q1 what "fix" means (recommended: rebuild notes to Contrapositive standard), Q2 keep brutalist look or shared look (recommended shared), Q3 first page (recommended M3 Keyword Extraction), Q4 rename (recommended "Abstract Answer Choices"), Q5 sources (recommended corpus + existing source notes).
- Captured (Joshua, verbatim where it matters): "the note and the drills for the breaking down should be much better. It doesn't have to fit the exact standard. Because right now the structure doesn't really make sense." "They should be able to do the statements that ask them to abstractify. I need to fix that." "Do the full audit and come to me with all the potential issues."
- Decision: Contrapositive gold standard is NOT a strict template here. Priority = the breaking-down note + its drills; the structure itself is a problem.
- Decision: next step is a full audit of problems, delivered to Joshua before any fix.
- Unanswered this round: Q2 look, Q4 name, Q5 sources (deferred until after the audit).
- Tentative (Claude's reading, unconfirmed): "statements that ask them to abstractify" = students must be able to do the actual task of converting between abstract answer-choice language and the concrete stimulus, not just reveal answers.

### Round 2 (interrupted by direct authorization)
- Captured (Joshua, 2026-10-12, verbatim): "it shouldn't be locked it should be fixed. make all the fixes you see are good. go through it. stick to the chrome browser you had before."
- Decision: interview ends here. Claude is authorized to implement every audit fix it judges good, unlock the modules, and verify in Joshua's Chrome (Claude in Chrome), not the built-in browser.
- Live observation (his Chrome, lsatprep.study/topics/abstract): Modules 2-7 show locked even on his account; only M1 opens. Sidebar truncates every module name.

## Open flags (pending input)
- Do any students have saved Abstract progress? -> Claude (look up in Supabase)
