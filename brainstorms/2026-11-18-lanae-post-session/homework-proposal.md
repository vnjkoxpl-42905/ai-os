---
title: Homework proposal for Lanae, 2026-11-14 and 2026-11-17 sessions
student: lanae
sessions: [2026-11-14, 2026-11-17]
status: proposed, nothing assigned
internal: true
created: 2026-11-18
---

# Homework proposal · Lanae · 2026-11-14 and 2026-11-17 sessions

Internal only. Nothing here is posted or assigned. The standard home for this file is `students/lanae/homework/`, which is outside this run's write scope, so it sits in the build folder. Move it on approval.

Sources: both transcripts read in full (2026-11-14 to 00:47:07, 2026-11-17 to 01:01:38). Live read `lsatu-admin items "Lanae" --all` on 2026-11-18 (10 items, matches `homework/already-assigned/index.md`). Drill rows read from `references/lsatu-guided-drill-catalog.json`, a snapshot dated 2026-10-25, not a live read. Live `search_assignable_work` was not run (see Unverified).

## What Joshua promised

| # | Promise | Timestamp | Certainty | Status 2026-11-18 |
|---|---|---|---|---|
| 1 | Conditional boot camp | 11-14 00:45:27; 11-17 00:58:26 | Promised | Assigned 2026-11-17 (item 28314761) |
| 2 | A note and a recap, "by tonight" | 11-14 00:45:27 | Promised | Three drafts, unposted. Four days late |
| 3 | Drills for must be true | 11-14 00:45:27; 11-17 01:00:09 | Promised, then "I can assign that" | Easier Set 4 assigned 2026-11-17. Rest proposed below |
| 4 | Quantity statement practice, "different variations" | 11-14 00:45:27, 00:19:43 | Promised | Nothing dedicated assigned. Proposed below |
| 5 | Groups 3 and 4 | 11-17 00:41:18 | Offered, deferred | Not taught. Not homework |
| 6 | Double-check August format and June date | 11-17 00:51:25 | Said | Teacher-side, open |

Promises 3 and 4 set the scope. Group 3 and 4 work, question-type practice and anything else are not proposed.

## Already on her account (not repeated)

Conditional Logic (Easier) Set 4 (`w5-02-conditional-logic-easier-set-4`, due 2026-11-24 in the log, 2026-11-25 in the live read), Conditional Logic Bootcamp, Main Conclusion Questions (note), Must Be True - First Taste, Explain Curious Fact (First Taste), Rebuttal Conclusions, Role + Main Conclusion (set 1), First Sentence Conclusions, two Intro to LR modules. The five 2026-11-07 drills are past due and still read "assigned". None of the five drills below is among them.

## Proposed: one guided drill per day, 2026-11-19 to 2026-11-23

All five: not on her account, beginner level, untimed or with a card the student can follow, chosen for a promise above. Due the next day.

| Day | Unlock | Due | Drill (title shown to her) | Slug | Level | Max difficulty | Questions | Catalog estimate | Why it fits |
|---|---|---|---|---|---|---|---|---|---|
| Thu | 2026-11-19 | 2026-11-20 | Must Be True: Translate the rules (2026-09-30) | `yahunathan-mbt-conditionals-2026-09-30` | beginner | 2 | 4 | 20 min | Promise 3. Must be true, conditional reasoning, difficulty 1 to 2, untimed. Card: say each rule as if-then, use the facts to trigger a rule or its contrapositive. Matches the 2026-11-14 note |
| Fri | 2026-11-20 | 2026-11-21 | Must Be True: Connect the rules (2026-10-01) | `yahunathan-mbt-conditionals-2026-10-01` | beginner | 3 | 4 | 20 min | Promise 3. Difficulty 2 to 3. Linking rules (head and tail), taught 2026-11-14 00:07:23 |
| Sat | 2026-11-21 | 2026-11-22 | Must Be True: Prove the inference (2026-10-03) | `yahunathan-mbt-conditionals-2026-10-03` | beginner | 3 | 4 | 20 min | Promise 3. Difficulty 3 only, the top of beginner. Third step of the same sequence |
| Sun | 2026-11-22 | 2026-11-23 | Conditional Logic (Easier) Set 1 | `w2-04-conditional-logic-easier-set-1` | beginner | 3 | 9 | 56 min | Promise 3 and the keyword work of 2026-11-17 (indicators, contrapositive). Difficulty 1 to 3 |
| Mon | 2026-11-23 | 2026-11-24 | Quantifiers: Trait Overlap inferences | `w8-10-quantifiers-trait-overlap-inferences` | beginner (drill default is intermediate) | 3 | 8 | 70 min | Promise 4. The only quantity drill in the catalog that is not advanced. Matches the some plus some and most plus most teaching |

The student-facing notes say "one drill a day, from Thursday, November 19 through Monday, November 23" and, in the quantity note, "the quantity practice I send on Monday, November 23". If this table changes, edit those two lines.

Plan file shape, for after approval only (not created):

```json
{"id":"lanae-2026-11-19-daily-drills","student":"<exact email>","student_folder":"students/lanae","assignments":[
 {"kind":"guided_drill","drill":"yahunathan-mbt-conditionals-2026-09-30","schedule":"2026-11-19","due":"2026-11-20","level":"beginner","max_difficulty":2},
 {"kind":"guided_drill","drill":"yahunathan-mbt-conditionals-2026-10-01","schedule":"2026-11-20","due":"2026-11-21","level":"beginner","max_difficulty":3},
 {"kind":"guided_drill","drill":"yahunathan-mbt-conditionals-2026-10-03","schedule":"2026-11-21","due":"2026-11-22","level":"beginner","max_difficulty":3},
 {"kind":"guided_drill","drill":"w2-04-conditional-logic-easier-set-1","schedule":"2026-11-22","due":"2026-11-23","level":"beginner","max_difficulty":3},
 {"kind":"guided_drill","drill":"w8-10-quantifiers-trait-overlap-inferences","schedule":"2026-11-23","due":"2026-11-24","level":"beginner","max_difficulty":3}]}
```

Run a dry run first, then one `assign_student_work` call after Joshua approves.

## Considered and not proposed

- `w2-03-must-be-true-first-taste`, `w1-06-explain-curious-fact-first-taste`, `w3-07-rebuttal-conclusions`, `w3-15-role-main-conclusion-set-1`, `w1-01-first-sentence-conclusions`: already assigned.
- `w3-12-conditional-logic-easier-set-2` (2 to 3, 7 questions): a fine swap for Sunday if Set 1 is too long. Not duplicated anywhere.
- Medium and Harder conditional sets: not beginner.
- Conditional Rephrase and other activities: not promised, and activities are assigned only when Joshua names them.
- Any drill for question-type identification: none exists in the catalog for it, and it was not promised.

## Cautions for Joshua

1. **Load.** Her account already holds five past-due drills, the boot camp (no due date) and Set 4. She said she had not done drills before 2026-11-17 and that school crowded out study. Five more in five days is the instruction; a lighter plan is two drills and the quantity one.
2. **Weekend.** 2026-11-21 and 2026-11-22 are Saturday and Sunday. She said she studies daily except weekends, but 2026-11-17 00:00:00 says she has a week off for school. The exact dates of that week are not in the record. Sunday carries a 56 minute drill; Saturday carries a 20 minute one.
3. **Titles carry dates.** The three `yahunathan-` drills show "(2026-09-30)", "(2026-10-01)", "(2026-10-03)" in the title and have another student's name in the slug. Her card text is generic. Joshua may want them renamed before she sees them, or may prefer `w2-04` and `w3-12` instead. They are pinned to four fixed questions each, so she sees the same four Yahunathan did.
4. **Pool overlap.** Easier Set 1 (difficulty 1 to 3) shares its question pool with Easier Set 4 (1 to 2), which is already assigned. The catalog warns that pool reattempts redraw and can overlap. She may see questions twice.
5. **Card advice conflicts with his advice.** The Easier Set 1 card says to diagram with generic variables like A, B, C. On 2026-11-17 (00:22:13) he told her to write full words. The Easier cards also say to try the set in 12 minutes, while the note tells her to read each card first.
6. **Quantity drill is the hardest fit.** It is intermediate by default (2 to 4). Level beginner with max difficulty 3 leaves 27 eligible questions. The card uses trait overlap language and symbols (the tilde and arrows), and the combinations beyond two somes and two mosts were never taught in session. She has the boot camp lessons, but whether she has started them is unknown. A smaller count would need Joshua's request and does not change the card.
7. **Lateness.** Promises 1 and 2 were "by tonight" on 2026-11-14.

## Unverified

- Live existence and published status of all five slugs. The catalog is a 2026-10-25 snapshot; live `search_assignable_work` was blocked for this agent.
- Question-level content of each drill (not opened; the bank was not read).
- Her access flags. `access` was not run. She holds assigned drills, so the drill flag is presumed on.
- Her exact email for the plan file. Not read here.
- Whether she has finished the boot camp sections on conditionals, must be true, or quantity.
