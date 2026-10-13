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

## Audit findings (Claude, 2026-10-12; code read in src/topics/abstract + live page in Joshua's Chrome)

Structure
1. The full 4-step breakdown method and its worked example (hypothesis / undermine / sufficiency of the evidence) are taught in M1 "Why Abstract Is Hard". M3, named the core method, is a ~100-word definition plus a 3-step list with no example and no interaction.
2. The method has four different versions: M1 (find, translate, combine, check), M3 (extract, translate, match), M4 (extract, analyze, check relevance, match), M7 (pick, translate, identify requirements, check coach notes).
3. M3 Step 2 says "Translate each keyword into LSAT language", which is backwards (you translate out of LSAT language).
4. Note and quiz disagree in M2: the note teaches 8 terms (Presuppose, Illustrate, General Principle, Explanation, Hypothesis, Premise, Intermediate Conclusion, Main Conclusion); the quiz tests a different 7 (adds Facts, Decision, Principle, Generalization) plus Undermine. The subtitle says "Seven terms"; a third "seven" list appears in M5's note.
5. M5 "Spot the Method" note teaches Explanation / Hypothesis / Presuppose again (a repeat of M2), not methods. The 17 patterns live only in the sidebar Methods Library.
6. M6 "Catch the Traps" note teaches five indicator buckets, not traps. Its quiz asks students to label Wrong Role / Wrong Method / Structural Mismatch / Attractive Language, which no note defines. The bucket rule ("every abstract answer choice word belongs in one of five buckets") is false.
7. Drills are sliced 1-20 in order across modules regardless of topic: M5 Spot the Method drills are both Flaw questions; M2 Words gets a flaw + a one-word trap; M3 breaking-down gets Role MC questions where no breakdown is required.
8. M3's drill never asks the student to break anything down. No exercise anywhere asks the student to go from abstract to concrete or concrete to abstract (Joshua's worksheets do both: X/Y mapping, "write a real-world example", reverse-engineer what the stimulus must contain).
9. The same 14 Role answer choices appear three times: M3 quiz (translator items), M7 note (embedded 18-item gauntlet), M7 quiz (same 18 again, different UI). The M1 example sentence also appears as translator item 11, gauntlet item 11 and an orphaned "Decode Practice" lesson.
10. Orphaned / unreachable: Decode Practice lesson, TranslatorWorkspace, DecodingGauntlet view, standalone DrillRunner and LessonReader views.

Grading and data bugs
11. Translation textareas accept any 10 characters and are never compared or self-checked; the verdict ignores them.
12. The M7 quiz gauntlet records a requirements checklist but shows none to the student.
13. Trap quiz grades the wrong thing: the label belongs to the whole drill (drill.trapTag) but is applied to whichever wrong option the code picks first.
14. Answer key position bias: all 20 drill answers are choice 1 or 2, never 3 or 4; drills 14-19 are all choice 1.
15. Drill timer starts once per module, so time per question accumulates.
16. drill_1's explanation says the project "finished early"; the conclusion says it "will be completed ahead of schedule".
17. Drills are invented, but the module row calls them "LSAT questions".
18. M1 quiz distractors are throwaways ("uses the word 'the' too often", "contains numbers"), and its Role answer choices refer to "it" with no statement marked.
19. M3 quiz labels Role answer choices "Stem 1 of 14" / "Next stem"; they are answer choices, not question stems. Clickable words are spans (no keyboard access).

Access and presentation
20. Every module after M1 is locked, including for Joshua; each quiz is locked behind "I read this" and each drill behind a 60% quiz.
21. Sidebar truncates every module name ("M3. STIMULUS + KEYW...").
22. M1 note step headings render at body size; the Step 4 checklist boxes do nothing when clicked; keyword meanings rely on hover popovers.
23. Library card: the 4:3 preview is mostly empty at column-view size; stats line "Chapter + 7 drills" is stale.

Data check (Lovable SQL, read-only, 2026-10-12): only Joshua's own 2 drill attempts (drill_1, drill_2) and 2 lesson rows exist. No student has Abstract progress, so restructuring strands no student work. drill_1 and drill_2 option order kept so his attempts still point at the right choice.

## What was built (2026-10-12, uncommitted, worktree ../ai-os-projects/lsatu-abstract, branch claude/abstract-bootcamp-fix off origin/main 940433e3)

- Unlocked every module, note, quiz and drill (AppContext). Progress still tracked.
- Module map rebuilt by topic: M1 drills 1-2, M2 drills 3 + 10, M3 new Break It Down drill (12 items), M4 drills 5-8, M5 drills 9, 11-13, M6 drills 4, 18-20, M7 drills 14-17. M3 renamed "Break It Down".
- All seven notes rewritten in components/views/AbstractNotes.tsx. The method is taught once, in M3, with a student-driven 4-step demo (pick keywords, translate, plain sentence, check two stimuli). M1 now defines an abstract choice and has a "which sentence?" interaction. M2 teaches the 13 terms the quiz tests. M5 teaches the 17 methods in four families. M6 teaches the four trap labels and the one-word trap. M7 is the short routine.
- New Break It Down drill (data/breakdownDrill.ts + BreakdownDrill.tsx): 5 X/Y direction items (Joshua's parsing worksheets), 3 decode items (plain English, which argument fits, write your own with model self-check), 4 build items (concrete argument to abstract answer choice). Retry until correct; first-try score recorded.
- Quizzes: M1 rewritten ("which sentence is it describing?"); M2 adds explanation, hypothesis, supported premise, defend; M3 uses answer choices 1-7 with a translation self-check; M6 trap labels authored per wrong choice; M7 uses choices 8-18 (minus 11) and adds the stimulus checklist step.
- Drill data: answer key spread across positions (drill_1/2 untouched), drill_1 explanation fixed, "Method N from the 17 Methods source" labels removed.
- Tailwind brutal palette now supports opacity shorthands (color-mix); tinted feedback boxes render for the first time, old code included.
- Sidebar/dashboard names wrap; Library card shows the module outline at large sizes; registry description and stats updated; progress counts only reachable items; dev-only route /dev/abstract-preview for local QA.

Verified: typecheck clean; lint 0 errors; Abstract has no tests of its own; DrillLaunchGate.test.tsx fails 2 tests but imports nothing changed. Walked in Joshua's Chrome on localhost:8080/dev/abstract-preview: dashboard unlocked, M3 note demo all four steps, full 12-item drill (9/12 first try with 3 deliberate misses), M3 quiz partial-credit self-check, M7 quiz checklist, M1 interaction; no console errors.
Not verified: signed-in persistence (preview has no user, writes are skipped), teacher Library card visually, mobile widths, M2/M4/M5/M6 notes clicked through, production build.

## Open flags (pending input)
- Ship it? Commit, PR, merge to main and free deploy_project to lsatprep.study -> Joshua
- Keep the yellow neo-brutalist look or move Abstract to the shared lesson look (Round 1 Q2, unanswered) -> Joshua
- Rename "Abstract" in the Library (Round 1 Q4, unanswered) -> Joshua
- Drills 9 and 20 share the traffic-camera story; drills 4, 18, 19, 20 have only two choices -> Claude, next pass
- Do any students have saved Abstract progress? -> Claude (look up in Supabase)
