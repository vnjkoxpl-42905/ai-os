# Verify proposed fixes to LR explanations

Another worker proposed edits to LSAT U's LR Question Explanations. You are the independent check. Nothing is applied unless you approve it. Be skeptical: your job is to catch edits that are wrong, not to admire them.

## Inputs
- The proposals: a JSON list at the path you are given. Each has qid, table, row_id, column, style, letter (for notes), old, new, kind, why, evidence.
- Read-only mirror of the database: `C:/Users/Joshu/dev/ai-os/system/scripts/lsatlab-pull/data/db/` (`lr_questions.json` has stimulus, prompt = stem, correct_choice; `lr_answer_choices.json` has choice_text, tag per letter; `lr_explanations.json`, `lr_explanation_steps.json`, `lr_explanation_choice_notes.json`).
- The bank students read: `C:/Users/Joshu/dev/ai-os-projects/lsatu/public/data/PT{n}-S{s}-LR.json`.
Load JSON with Python (`python -I`), never whole files into context. Write scripts only in your work directory.

## For every proposal
Read the question's stimulus, stem, all five choices, the key, and the old and new text in full. Then decide:
- **approve** — the new text is correct: every quote matches the choice or stimulus exactly, the logic is right for this question and key, the verdict for the letter agrees with the key (correct letter is argued as correct, wrong letters as wrong), nothing outside the defect was damaged, and it reads clearly.
- **fix** — the edit is the right idea but has a mistake you can correct. Give the full corrected `new`.
- **reject** — the edit is wrong, unnecessary, or makes things worse. Say why.

Hard rules for approve/fix: no added em dashes; no added gendered pronouns (he, she, his, her...) for people in the stimulus; no mention of Logic Games; never change which choice is credited; a wrong-answer note must say why that choice is wrong, a correct-answer note why it is right.

Also settle any open question the proposer raised in its `why` (for example a disputed verdict). If you cannot settle it with confidence, reject that edit and say what is needed.

## Output
Write JSON Lines to the output path you are given, one per proposal, in input order:
`{"row_id": "...", "qid": "...", "verdict": "approve|fix|reject", "new": "<only when fix: full corrected text>", "note": "one sentence"}`

Reply with counts of approve, fix, reject, and list every reject and fix with its one-sentence reason.
