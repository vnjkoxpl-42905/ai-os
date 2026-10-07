# Review brief: LR explanation coverage work (Claude, 2026-09-26 to 2026-09-27)

You are reviewing work done by another AI (Claude) for Joshua Fisseha, who runs LSAT U (lsatprep.study), an LSAT prep platform. He teaches the LSAT. You are read-only. Do not modify any file. Form your own judgment from the files; this brief states facts and pointers only, not an assessment.

## The goal
LSAT U has Logical Reasoning (LR) questions from PrepTests. Most have written explanations stored in a database. A set of questions have no explanation or an incomplete one. The goal is to write the missing explanations so they match the quality and voice of the best existing ones, then load them into the database.

Joshua's stated method, in order:
1. Build a "golden set": the best existing explanations, across question types and features, to define the standard.
2. Write a 20-question pilot that Joshua reads in full and judges.
3. If the pilot passes, write the rest in batches. Joshua only sees previews and low-confidence drafts.

Things Joshua said along the way:
- "You don't have to make a guide... don't make this complicated." No per-type writing guides. Write from the reference set directly.
- Use his two PDFs (an LR cram sheet and an LR question-type/reasoning-type guideline) and the database. Find similar questions by type, features and nature.
- "Find 10 to 20 for each question type, at least 10... really well explained... to model future explanations." This became the model library.
- The explanations are the teaching product. The reasoning is the product. Plain, direct voice. No em dashes.

## Where things live
Vault root: C:\Users\Joshu\dev\ai-os (vault instructions: CLAUDE.md there).
- Decisions log for this work: brainstorms/2026-09-26-lr-explanation-coverage.md
- Golden set: corpus/lr-explanations/golden-set.md (plus golden-set-candidates.md, golden-set-observations.md)
- Model library: corpus/lr-explanations/models/index.md and the 9 per-type files beside it
- Pilot (20 drafts, not yet loaded, not yet read by Joshua): corpus/lr-explanations/drafts/pilot-2026-09-27.md
- Fix lists and audits: corpus/lr-explanations/fixes/ (index.md is the open-items list; model-library-defects.md; lsatlab-audit-2026-09-27.*; revamp-*; choice-note-issues.md; side-issues.md)
- Scripts: system/scripts/lr-explanations/score_corpus.py, neighbors.py, show.py
- Read-only database dump (JSON, one file per table): system/scripts/lsatlab-pull/data/db/ (lr_questions, lr_explanations, lr_explanation_steps, lr_explanation_choice_notes, lr_answer_choices)
- The question bank (what students see and are graded on): C:\Users\Joshu\dev\ai-os\projects\lsatu-wt-glossary\public\data\PT*-S*-LR.json
- Joshua's PDFs as text: C:\Users\Joshu\AppData\Local\Temp\claude\C--Users-Joshu-dev-ai-os\d175f546-f515-4224-a5ed-1afb844b5971\scratchpad\pilot\cram.txt and guideline.txt (also gaps.json = the list of missing slots, neighbors.json, picks.json)
- Session log entries: wiki/log.md (entries dated 2026-09-26 and 2026-09-27)

## Other things done in the same session (context)
- Loaded 221 explanations from a third-party source (LSAT Lab) into the database.
- Deleted one stray bank question (PT128-S2-Q26), fixed one answer choice (PT148-S3-Q26 D), and deleted a leftover Codex worktree.
- About 560 slots still have gaps (348 unexplained, 179 unloaded, 17 notes-only, 16 steps-only).

## What Joshua asked for from you
Review this work hard. Grill it. Say what is good and what is not. Say whether the approach actually serves the goal, and whether any of it is not worth doing or not worth continuing. Check claims against the files and data rather than trusting the documents. In particular, consider:
- Is the pilot good enough to show Joshua? Check several drafts against the actual question (bank stimulus, choices, correct answer) for correctness of the reasoning, not only style.
- Is the golden set / model library a sound basis, and is the scoring script measuring what matters?
- Is the plan for the remaining ~540 sound, or is there a simpler or better route?
- Anything wrong, risky, wasted, or missing.

Structure your reply as: (1) what is good, (2) what is wrong or weak, with evidence (file + slot or line), (3) what is not worth continuing, (4) what you would do next, ranked. Be specific. End with exactly one line: VERDICT: SOUND or VERDICT: REVISE.
