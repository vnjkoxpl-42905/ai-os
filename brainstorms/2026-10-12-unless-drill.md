# Unless Drill: Brainstorm / Discovery Notes
Date: 2026-10-12 · Goal: pin down exactly how the standalone Unless drill (LSAT U PR #205, `/unless-drill`) should match Joshua's Unless Practice Routine before it ships to students.
Status: complete. Built 2026-10-12 as commit d2c19b44 on PR #205 (not merged yet).
Context sources: LSAT U PR #205 (feat/unless-drill-page); `src/features/conditional-refresher/` (UnlessDrill.tsx, content.ts); Joshua's screenshots of the "Instructions" and "Unless Practice Routine Answer Key" (2026-10-12).

## Source material (from Joshua's screenshots, 2026-10-12)
Instructions:
1. Diagram three out of these four Unless statements: a. ~A, unless B. b. Unless B, A. c. Unless ~B, ~A. d. A, unless ~B.
2. Switch up which three statements you diagram every time.
3. Start every LSAT study session with this quick workout until you can diagram Unless accurately in under 5 seconds.

Answer key:
- ~A, unless B. -> A → B
- Unless B, A. -> ~A → B
- Unless ~B, ~A. -> A → ~B
- A, unless ~B. -> ~A → ~B

Observed against PR #205 (fact, checked in code):
- The drill shows 3 of the 4 patterns per round (matches instruction 1, but Joshua says it should have all 4).
- PR #205's review labels the *contrapositive* of his key as "Correct" (e.g. ~A unless B shows /B → /A) and his key form as "Also counts". The key's form is the reverse.
- PR #205's "Group 3 move" teaches negating the idea after "unless". His key comes from negating the *other* idea and keeping the unless idea unchanged on the right.
- Statements render without commas/periods ("/A unless B" vs "~A, unless B.").

## Summary / key decisions
- Joshua (2026-10-12): the drill should have all four statements, not three.
- Confirmed: all four patterns every round (Q1). Letters vary each round; A/B in the sheet are just symbols (Q4).

## Q&A log
### Round 1
#### Q1 - Four statements per round
- Asked: all four patterns every round, shuffled order?
- Recommended: all four, new order each round.
- Captured: "Add the extra one that's missing... one more that's integrated into those four." -> every round has all four patterns.
#### Q4 - Letters
- Asked: fixed A/B or new letters each round?
- Recommended: new letters each round.
- Captured: "Don't worry about the A and B... It should be just a symbol." "I like that you use a variation of letters. I want you to stick to that."
#### Q2, Q3, Q5, Q6
- Not yet answered; re-asked in Round 2.
### Round 2
- Captured: "go with your recommendations on all of them" (Q2 key form is Correct, contrapositive also counts; Q3 the four steps; Q5 commas/periods + slash; Q6 keep 10s warm-up, goal message only at 5s).
- Joshua asked for a plain explanation of what changes before build. Awaiting confirmation of shared understanding.

## Open flags (pending input)
- (none yet)
