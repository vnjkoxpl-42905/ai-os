# Claude review of V7

2026-09-30. Model observed: `claude-opus-5-5`. Claude Code 2.1.280. Verdict: **REVISE**. Read-only static review; V7 unchanged.

The biggest problem: the two operations the opening promises are split apart. Applying a rule starts in section 03, but linking rules does not start until section 05, about 60% of the way down (line 197 of 323). Several things sit between them that are not prerequisites for linking. These are the advice/permission ("should"/"may") material in 02 (lines 61-75), which already asks the student to apply a rule before 03 teaches how. Then comes an overloaded section 03 with three overlapping checks, and the compound-negation section 04, which neither linking section uses. Inside the linking material, the student is quizzed on invalid links before they are taught: the chain lab (line 229) offers mismatched, shared-start and reversed options, and quiz 2 (line 271) comes before the prose that explains it (lines 273-277). The "whole middle must match" warning (lines 231-237) also sits between two valid linking techniques. Smaller issues: "only if" is never taught as a translation pattern, section 01 includes quantity-scope and requires-vs-received detail long before either is used, and section 07 adds new material after its summary table. The numbered two-scenario opening works and should stay. It needs one sentence pointing to where each operation is taught, and the free-floating 'treat statements as true' instruction should move into 01. Recommended order: Opening → 01 Facts (shortened) → 02 Rules (with 'only if' translation; modality removed) → 03 Apply forward → 04 Contrapositive and the four fact cases (one consolidated check) → 05 Link rules (rules only, add a fact, chain contrapositive, hidden chain via contrapositive) → 06 When a link fails (mismatched middle, shared start, shared end; chain lab and quiz 2 placed after the prose) → 07 Keep the claim intact (advice/permission, requires vs received, compound negation) → 08 Choose the move and test the claim (table, counterexample, scope of 'some') → 09 Mix the moves → 10 Assigned work (drills before LSAT questions). This puts the two central operations next to each other. Each boundary is taught before it is tested, and every topic is kept. Decisions for Joshua: (a) whether advice/permission and compound negation become one combined 'keep the claim intact' section or two short ones, as recommended above; (b) which of the three overlapping section-03 checks to keep (FACT-LAB/CASE-GRID, POP-QUIZ-1, Try it); (c) whether the chain lab is moved to after section 06 or trimmed to valid-link options in 05. VERDICT: REVISE

## ORD-1 (high)

The advice/permission subsection 'Rules can connect different kinds of claims' (lines 61-75) sits inside 02, before the student learns to apply a rule (03, line 77) or take a contrapositive (03, line 113). Line 65 relies on negating a 'should' claim ('it is not true that it should be inspected'), which only matters for contraposition, taught later. Line 67 turns 'may enter only if ... badge' into May enter → Has a badge and uses 'necessary', but 'only if' is never taught as a pattern. The Try-it at line 73 asks the student to apply 'Every damaged item should be inspected' to 'this damaged item', which is the forward-application move defined at line 79. Line 117 then comes back to the same advice qualifier. The result: the student does a central operation as part of a side topic before learning it, and the arrow from 02 is immediately complicated before it has ever been used.

Recommended fix: Keep 02 to the definition, T → B, arrow direction, sufficient/necessary, and the existence limit. Add one short 'only if' translation example there, because section 04's compound rules depend on it. Move lines 61-75, the MODALITY block, the contrapositive-with-qualifier note (line 117) and line 45 (requires vs received) into one 'Keep the kind of claim intact' section after linking and its failure cases.

## ORD-2 (high)

The opening introduces two operations side by side (lines 5-27), but linking does not start until 05 (line 197). In between: section 03 runs 95 lines (77-171) and contains forward application, the contrapositive, TWO-MOVES, four fact cases (Facts 1 and 2 repeat the two demonstrations just given), FACT-LAB on a new rule, CASE-GRID, POP-QUIZ-1 and a Try-it that tests the same two cases again (line 167). Then section 04 (lines 173-195), on compound AND/OR negation, comes next. Linking (05-06) never uses it; only Practice 4 does. A student reading for the two operations meets the second one after about 60% of the page.

Recommended fix: Split 03 into '03 Apply forward' and '04 Use the contrapositive; four fact cases'. Keep one interactive check plus one Try-it with a different example, and drop or merge the duplicate checks. Put Facts 1-2 in a compact table or grid instead of repeating the full prose. Move compound negation to the 'Keep the claim intact' section after 06 so linking comes straight after application.

## ORD-3 (medium)

The CHAIN-LAB ('Can these rules form a chain?') is placed at line 229 in the Markdown. It offers the options 'Has received special approval → Needs a signature', 'Submitted late → Needs a signature' and 'Needs a signature → Requires special approval', with feedback on 'requires ≠ has received', shared starting points, and 'both rules point into the middle'. Mismatched middles are first taught at line 231, shared starts in section 06 (line 263), and shared ends at line 275. The lab tests three failure types before any of them is taught.

Recommended fix: Move CHAIN-LAB to after the section-06 prose (after line 277), where it works as a combined check of valid and invalid links. Otherwise, keep it in 05 with only the valid-match option and move the failure options to 06.

## ORD-4 (medium)

POP-QUIZ-2 ('Late applications need approval and a signature. What does approval alone prove?') is at line 271, right after SHARED-TRIGGER. The explanation is in lines 273-277: applying both rules to a known late application, the on-time counterexample, shared endings, and the matching test. The quiz asks before the prose teaches.

Recommended fix: Move POP-QUIZ-2 to after line 277, next to the section's Try-it (line 279), or merge the two checks.

## ORD-5 (medium)

Section 05 runs in this order: valid link (201-213), add a fact (215-223), chain contrapositive (227), CHAIN-LAB, then the boundary 'The whole middle idea must match' (231-237), then the valid technique 'A contrapositive can uncover the match' (239-261). The invalid-match warning interrupts two valid linking moves. It belongs with section 06's other failures, and line 277 already says 'keep the rules separate or see whether a valid contrapositive produces a match'.

Recommended fix: Order 05 as: rules-only link → chain contrapositive → hidden chain via contrapositive → add a fact to the chain. That ends linking on the apply-to-a-case connection back to opening scenario 1. Move lines 231-237 to the start of 06 so it becomes 'When a link fails': mismatched middle, shared start, shared end.

## ORD-6 (medium)

Section 01 includes a 'some' existence/scope Try-it (lines 39-43) and a requires-vs-received note (line 45) before any rule exists. 'Some' scope is next used at line 296 (07), and requires-vs-received at line 233. Neither prepares the student for 02-03, and the Try-it is a quantity-statement exercise in a section whose job is to define 'fact' for the rule operations.

Recommended fix: Keep 01 to the definition, the Mira example and the negative-fact example. Move the 'some' scope example next to the 'Some applications ... therefore some' passage in 08 (choose the move). Move line 45 into the 'Keep the claim intact' section.

## ORD-7 (low)

Section 07 is framed as a summary ('Choose the move', table at lines 287-292) but then teaches new material: the counterexample method (line 294) and applying a rule to a 'some' group fact (line 296). Section 03 only shows rules applied to individuals. The reasoning is sound but placed after the summary, so it is new content arriving inside the wrap-up.

Recommended fix: Put the counterexample method and the group-fact paragraph before the table, or label them as one final boundary. Add one sentence to 03 noting that a group fact ('some X') can satisfy a starting condition while keeping its scope.

## ORD-8 (low)

The FACT-LAB opens with <h2>What does this fact let you conclude?</h2> inside numbered section 03, so the heading tree shows it as a peer of the numbered sections. In the Markdown, 'Fact 1'-'Fact 4' are h3 siblings of 'Four facts, one unchanged rule' (lines 121-155) rather than its children. Both flatten the progression a reader sees.

Recommended fix: Change the lab heading to h3 (or a non-heading label with aria-label) and make the Fact 1-4 headings h4, or present them as a grid under one h3.

## ORD-9 (low)

Line 29 ('Treat the statements given in an inference question as true...') sits between the opening scenarios and section 01 and is not connected to either. The opening also uses 'starting condition' (line 13) and 'shared condition' (line 25) before 02 defines them. That is acceptable for a preview, but nothing tells the reader the two numbered scenarios are where the lesson is heading.

Recommended fix: Keep the numbered scenarios as Joshua requested. Add one bridging sentence after them, such as 'Section 03 teaches the first move; section 05 the second', and move line 29 into the opening of 01, next to the definition of a given fact.

## Coverage

- Read the full concept-lesson-v7.md (lines 1-323) and mapped where each concept is first used and where it is defined
- Read the lesson-quality-bar.md reference, including its requirements on teaching sequence, prerequisites and checks
- Read the reference 07-quantity-statements-lesson.md and compared its meaning → components → compare/combine sequence
- Inspected conditional-reasoning-v7.html by grep: rendered h2/h3 order, the placement and heading level of FACT-LAB and POP-QUIZ, CHAIN-LAB options, and CHAIN-LAB feedback text
- Confirmed the V7 marker block in students/yahunatan-zetvy/recaps/2026-09-16-recap.md (lines 1261-1586) has the same section structure and opening text as concept-lesson-v7.md

## Limits

- Static source review only; the rendered page was not viewed live, so visual hierarchy, spacing and interaction behaviour were not checked
- The HTML is minified on one line; interactive blocks were inspected only through targeted grep excerpts, and the full content of MODALITY, NEGATION, TWO-MOVES, CASE-GRID and HIDDEN-CHAIN was not read
- Did not read .agents/skills/post-session-recap/SKILL.md, wiki/teaching-voice.md, or the lecture transcript/teleprompter; findings rest on the lesson-quality-bar reference and the reference lesson
- Compared the recap V7 block with concept-lesson-v7.md by headings and opening lines only, not line by line
- No tests or build scripts were run; no files were modified

## Codex disposition

The sequencing findings warrant revision planning. Keep the two numbered opening scenarios; teach definitions and operations before qualifier complications and checks. Do not treat the source review as visual approval. The summary and ORD-5 recommend different internal chain orders, so that detail needs arbitration when revising. No note edits or publication are authorized by this review alone.
