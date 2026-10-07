---
type: handoff
subject: LR explanation coverage, full pickup for Codex (or any fresh agent)
created: 2026-09-27
from: Claude (Opus 5.5) session d175f546
---

# Handoff: write the missing LR explanations for LSAT U

Read this whole file before doing anything. It is written so a fresh agent can pick up with no other context.

## 1. The goal

LSAT U (lsatprep.study) shows Logical Reasoning questions from official PrepTests. Each question should have a written explanation in the database. About 560 slots have no explanation or an incomplete one. The job is to write them in the voice and quality of the best existing explanations, load them into the database, and verify them.

Joshua Fisseha owns the product and the teaching voice. The explanations are the product: they teach the reasoning, not just the answer.

## 2. Joshua's method, and where we are in it

1. **Golden set** (done): the 51 best existing explanations. `corpus/lr-explanations/golden-set.md`.
2. **Model library** (done): 334 top-tier existing explanations, 10 to 20 per question type, with a "What the best ones do" section per type. `corpus/lr-explanations/models/index.md` + 9 type files.
3. **Pilot of 20** (written, NOT loaded, WAITING for Joshua's read): `corpus/lr-explanations/drafts/pilot-2026-09-27.md`.
4. **The rest in batches** (NOT started). Joshua sees only a preview of each batch and the low-confidence drafts.

**Gate: do not write or load step 4 until Joshua has read the pilot and said it is good (or said what to change).** If he has not given a verdict, your first job is to ask him for one.

## 3. Rules Joshua set (do not re-ask these)

- No intermediate guides, cheat sheets or style docs. Write directly from the models. "Don't make this complicated."
- Use his two PDFs for the named moves and traps: text at `corpus/lr-explanations/work/pilot-inputs/cram.txt` and `guideline.txt` (originals: `C:\Users\Joshu\OneDrive\Desktop\2024-Updated-LR-cram-sheet.pdf`, `C:\Users\Joshu\Downloads\LR GUIDELINE QUESTION TYPE AND REASONING TYPE.pdf`).
- For each new explanation, find the closest existing ones by question type, features (Sampling, EXCEPT, Principles in Answers ...) and kind of stimulus, and follow them. The pilot names its models in a "Modelled on" line.
- Voice: plain, direct, short sentences, teach the reasoning. **No em dashes anywhere.** No mocking the question, no political examples, no Logic Games references (there are no Logic Games on the LSAT). The "Do not copy from the corpus" section of `golden-set.md` lists what not to inherit from old explanations.
- Trap tags use the vocabulary the database already uses for that question type.
- Dropped by Joshua, do not revive: a writer-mark column; fixing the ensure/insure and Packaging/Packing spellings; per-type writing guides.
- Never delete files or records without his explicit yes. Absolute dates only.

## 4. Where everything is

Vault root: `C:\Users\Joshu\dev\ai-os`. Read its `AGENTS.md` (Codex) or `CLAUDE.md` (Claude) first.

| What | Path |
|---|---|
| Decision log for this work (all rounds of Q&A) | `brainstorms/2026-09-26-lr-explanation-coverage.md` |
| Golden set | `corpus/lr-explanations/golden-set.md` |
| Model library | `corpus/lr-explanations/models/` (start at `index.md`) |
| Pilot | `corpus/lr-explanations/drafts/pilot-2026-09-27.md` |
| Open-items list (update it as you go) | `corpus/lr-explanations/fixes/index.md` |
| Defects found in existing explanations (revamp track, not this job) | `corpus/lr-explanations/fixes/model-library-defects.md`, `revamp-list.md` |
| Gap list + helper scripts used for the pilot | `corpus/lr-explanations/work/pilot-inputs/` (`gaps.py` builds `gaps.json`; `neighbors.py`; `show.py`) |
| Scoring / neighbor / print scripts | `system/scripts/lr-explanations/score_corpus.py`, `neighbors.py`, `show.py` |
| Read-only database dump | `system/scripts/lsatlab-pull/data/db/*.json` (refresh with `python system/scripts/lsatlab-pull/db_pull.py` from the vault root; add `lr_answer_choices` and the four default tables as args to pull all five) |
| The question bank (what students see and are graded on) | `projects/lsatu-wt-glossary/public/data/PT*-S*-LR.json` (worktree of the app repo; `projects/lsatu/` is the main checkout) |
| SQL load pattern that worked (221 loads, 2026-09-27) | `corpus/lr-explanations/work/load-pattern/` (batch-01 = steps only; batch-01/02/09 have choice notes; batch-23/26/33-36 insert a whole new question) |
| Codex's independent review of this work | `corpus/lr-explanations/work/codex-review/` (BRIEF.md = what it was asked; round1.txt = its verdict, once saved) |
| Session log | `wiki/log.md` (entries 2026-09-26, 2026-09-27) |
| Earlier bank repairs (PRs #146 to #154), for background only | `corpus/lr-explanations/fixes/index.md`, "Data and question bank" |

## 5. The data model (verified against the dump 2026-09-27)

- `lr_questions` (preptest, section, question_number, stimulus, prompt, correct_choice, question_type, section_id, qid, is_explained, source_note)
- `lr_explanations` (question_id, style). Use style `single`. One explanation per question.
- `lr_explanation_steps` (explanation_id, position from 0, label, body). The Argument Breakdown. Labels follow the type: e.g. Conclusion / Evidence / Evaluate / Goal; Paradox uses Given That / How Can It Be That / Evaluate-Goal.
- `lr_explanation_choice_notes` (explanation_id, letter, body). One per choice A to E.
- `lr_answer_choices` (question_id, letter, choice_text, tag, is_correct, student_percent). The trap tag lives here, per choice.

**The bank and the database hold each question twice.** The bank shows and grades; the database explains. After any load, compare stimulus and correct answer per slot between the two. The bank key is what students are graded against.

Gap states in `gaps.json`: Unexplained (question in DB, no explanation), Unloaded (question not in DB at all: insert question + choices + explanation, see batch-23), Notes-only (write the breakdown), Steps-only (write the notes). Counts as of the last build: 348 / 179 / 17 / 16. **`gaps.json` may predate the 221-question load. Re-pull the dump and re-run `gaps.py` before trusting it.**

## 6. How to load (after Joshua approves)

- The database is reached through the **Lovable connector**, `query_database`, project `53b9a6f2-aba7-4ae4-8dd1-fa5b8aab4d76`. Write SQL in the load-pattern shape: dollar-quoted text (`$lsat$...$lsat$`), look up the explanation by preptest/section/question_number, `ON CONFLICT DO NOTHING`, guards so nothing overwrites an existing step or note.
- `query_database` and `deploy_project` are free. **Never use the Lovable agent chat (`send_message`); it spends credits** and needs Joshua's explicit yes each time.
- Explanations are read from the database at runtime, so a load is live with no deploy. Bank (JSON) changes go through a branch + PR on `vnjkoxpl-42905/lsatu-684d89db` (never commit to main), then free `deploy_project` once `list_edits` shows the commit `completed`.
- Before each batch, snapshot any rows you will touch into `raw/sources/lsatu-lr-snapshots/`.

## 7. Verify every batch

For each slot: steps exist and positions run 0..n; exactly 5 choice notes; the note for the correct letter matches the **bank** key; every quoted choice matches the bank's choice text; zero em dashes (`\u2014`); no emphasis marker glued to a word; stimulus and key agree between bank and DB. Re-pull the dump and re-run `gaps.py`; the gap count should drop by exactly the batch size.

## 8. State of the live site (as of 2026-09-27 12:30)

- PR #153 (stray PT128-S2-Q26 deleted) and #154 (PT148-S3-Q26 choice D "novel") are merged and published. #154 verified live by fetching `lsatprep.study/data/PT148-S3-LR.json`.
- PRs #138, #141, #142 on the app repo are still open (not part of this job; don't merge without Joshua).

## 9. Open questions to raise with Joshua first

1. His verdict on the 20-question pilot. This gates everything in step 4.
2. About 30 answer choices differ in meaning between the bank and the database (list in `fixes/index.md`). Should they be settled against LSAT Lab's `/api/questions` (needs LSAT Lab logged in; method in `skills/codex/lsat-lab-sync/SKILL.md`, which is in the catalog but not activated for Codex)? Unanswered.
3. Whatever Codex's review (section 4) recommends that changes the plan. Put those to him as decisions, don't act on them silently.

## 9b. Codex review (2026-09-27) and what was done about it

Full text: `corpus/lr-explanations/work/codex-review/round1.txt` (VERDICT: REVISE). Accepted and DONE 2026-09-27 by Claude (pilot has a "Fixed 2026-09-27 after Codex review" note; golden-set picks #2 and #35 are marked REFERENCE ONLY):
- Pilot errors: PT120-S4-Q9 (note wrongly rules out A), PT114-S4-Q12 (proof swaps "cannot help" for "cannot affect"), PT128-S3-Q16 (invented premise and a "10%" figure).
- Golden picks PT145-S2-Q23 (reversed predicates in the correct-answer note) and PT138-S2-Q25 (calls the "only if" term sufficient) marked reference-only.
- Gap count is at least 567, not 560: also count the 7 slots with a breakdown but only 3 or 4 notes (`fixes/side-issues.md` section 4).
- Every load must touch only approved slots and never delete. Do not use the app's `scripts/knowledge/ingest-lr-explanations.mjs`; it deletes and rebuilds.
Rejected: "score_corpus.py has a syntax error" (it compiles). The scorer only builds shortlists; it is not a quality measure, and nothing publishes on its score.

## 10. Next actions, in order

1. Read this file, then the decision log, `golden-set.md`, `models/index.md`, the pilot, and the review in `work/codex-review/`.
2. Ask Joshua the open questions in section 9.
3. When the pilot is approved: revise it as he says, load its 20, verify (section 7).
4. Write the rest by type in batches of about 40. Each batch goes into a draft file in `corpus/lr-explanations/drafts/`, with a preview for Joshua and any low-confidence drafts marked. Load only after he approves the batch. Verify, then update `fixes/index.md` and append `wiki/log.md`.
