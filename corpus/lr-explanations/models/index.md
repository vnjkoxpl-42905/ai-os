---
type: teaching-notes
subject: LR explanation model library, 10 to 20 top-tier models per question type
updated: 2026-09-27
---

# LR explanation model library

334 existing explanations from the LSAT U database, picked as models for writing the missing ones. The [[../golden-set|golden set]] (51) is the short list of the very best; this library is the deep bench, 10 to 20 per question type, spread across difficulty and across each type's sub-patterns (each famous flaw on Flaw, conditional vs story-style on Parallel, and so on). Most picks are new; golden picks that turned up are marked.

**How it was built.** `system/scripts/lr-explanations/score_corpus.py` scored all 3,640 complete explanations (Evaluate depth, a Goal that names the answer, verdict-only notes, explicit tests, examples, stated rules, correct-answer note length, whether the most popular trap got the most attention; penalties for the em-dash register and for mocking the question). The top 25 to 40 per type were then read in full, every choice note checked against the printed answer text, and scored on the golden-set rubric (P prediction, X precision, E eliminations, T transfer, C clarity, L learner value; /12). Reading was split across 9 parallel readers; each file is one reader's judgment, so treat 11 vs 12 as a tie.

**How to use it.** When writing a missing explanation, find its type here, read the 2 or 3 picks that share its sub-pattern, and follow the "What the best ones do" section for that type. `system/scripts/lr-explanations/neighbors.py` finds the closest picks by features and stimulus shape; `show.py SLOT` prints one in full. Joshua's cram sheet and LR guideline PDFs (paths in [[../golden-set]]) name the moves and traps.

| Type | Models | File | Notes |
|---|---|---|---|
| Flaw | 20 | [[Flaw]] | Leans on flaws the golden set lacks: ad hominem, sampling, anti-causal, percent vs number, aggregate vs subgroup, best vs only, false choice |
| Must Be True / Most Supported | 20 | [[MBT-MBF]] | Conditional chains, Most + conditional, weighted averages, pivots, logical completion |
| Must Be False | 17 | [[MBT-MBF]] | Only 8 are truly top-tier; the type has 42 complete explanations in total |
| Necessary Assumption | 20 | [[NA]] | EXCEPT is thin: one usable model (PT103-S2-Q22, 8/12) |
| Sufficient Assumption | 20 | [[Strengthen-SA]] | Includes PT129-S2-Q7, a clean Refute-a-Conditional model the golden set lacked |
| Strengthen | 20 | [[Strengthen-SA]] | Plausibility boosters, ruled-out alternatives, plans, EXCEPT |
| Weaken | 20 | [[Weaken-Evaluate]] | Third factor, reverse cause, base rate, analogies, term shifts, EXCEPT |
| Evaluate | 17 | [[Weaken-Evaluate]] | About 12 are true models; the type has 25 complete explanations |
| Paradox | 20 | [[Paradox-Method]] | Difference-makers, math, plan-didn't-work, EXCEPT |
| Method | 20 | [[Paradox-Method]] | Includes three Method on Plans / Recommendations models the golden set lacked |
| Principle-Strengthen | 20 | [[Principle]] | Principles in answers and in the stimulus, weighing tradeoffs |
| Principle-Conform | 20 | [[Principle]] | Stimulus principles as checklists, implicit principles as slogans |
| Main Conclusion | 20 | [[MC-Role-Agree]] | Only 5 are difficulty 1-2; more easy models would need a second search |
| Role | 20 | [[MC-Role-Agree]] | Concessions, opposing views, intermediate-conclusion chains |
| Agree / Disagree | 20 | [[MC-Role-Agree]] | Explicit and assumption-level clashes, EXCEPT, Agree stems |
| Parallel | 20 | [[Parallel]] | No difficulty-1 pick besides the golden PT154-S1-Q10 |
| Parallel Flaw | 20 | [[Parallel]] | Each famous flaw; no clean Unproven vs Proven False model |

**Do not copy from a pick without reading its Weakness column.** Several picks carry a slip, a political example or a flattened diagram that has to be fixed in the new writing, not reproduced. Every defect found, picked or not, is in [[../fixes/model-library-defects]].

**Recurring moves across all types** (each file has the type-specific version):
- The Evaluate step argues with the argument before the choices ("Given that ... how could we argue ..."), with worked numbers or one everyday analogy.
- The Goal names the answer's content, often in two acceptable shapes (formal and conversational, or linking and defender).
- Each choice note runs the test its type or wording calls for, and says so in the first line.
- The most popular wrong answer gets the longest note, and it says why it tempts before why it fails.
- Wrong answers are often rewritten into the version that would have been right.
- Recurring rules are stated as rules, so they transfer to the next question.
