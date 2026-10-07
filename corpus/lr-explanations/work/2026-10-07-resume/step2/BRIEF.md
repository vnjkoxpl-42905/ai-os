# Step 2 brief: propose exact fixes for defective LR explanations

You are fixing **real errors** in LSAT U's LR Question Explanations, the teaching students read after answering. You do NOT write to any database. You produce a proposal file. Another reviewer checks every proposal against the question before anything is applied, so precision matters more than volume.

## Read-only sources (local mirror of the live database, refreshed 2026-10-02/03)
Directory: `C:/Users/Joshu/dev/ai-os/system/scripts/lsatlab-pull/data/db/`
- `lr_questions.json` — id, qid (e.g. PT146-S3-Q1), stimulus, prompt (the stem), correct_choice, question_type
- `lr_answer_choices.json` — question_id, letter, choice_text, tag, is_correct
- `lr_explanations.json` — id, question_id, style (`standard`, `brief`, `another_way`, `single`)
- `lr_explanation_steps.json` — id, explanation_id, position, label, body (the Argument Breakdown steps)
- `lr_explanation_choice_notes.json` — id, explanation_id, letter, body (the Choice Notes)

Students see the first style present in the order standard, brief, another_way, single, and the selector lets them see the others. Fix the defect in **every style where it occurs**, not just one.

Also available, the question bank students are graded on: `C:/Users/Joshu/dev/ai-os-projects/lsatu/public/data/PT{n}-S{s}-LR.json` (fields questionNumber, stimulus, questionStem, answerChoices, correctAnswer). When the DB and bank wording differ, the bank is what students read.

Load the JSON with Python (`python -I`), never by reading the whole file into your context. Write helper scripts to your own scratch directory.

## What to do for each item on your list
1. Find the question and the row(s) the item describes. Read the stimulus, the stem, all five choices, the key, and the full explanation (all styles).
2. Confirm the defect is real. The list was written by earlier readers and may be wrong or already fixed. If it is not real, record a `skip` with the reason.
3. Write the smallest edit that makes the text correct:
   - Keep the author's voice, structure and wording everywhere outside the defect.
   - A misquote, slip or wrong-letter reference: correct the words.
   - Garbled or flattened transcription (scrambled diagrams, run-together words, truncation): reconstruct the intended text from the stimulus and the surrounding explanation. Put each diagram chain on its own line, with `→` arrows. If you cannot reconstruct it with confidence, rewrite only that sentence or chain plainly and correctly.
   - A note that never says why its choice is wrong or right (verdict-only, pasted from another letter, identical to another note, empty, placeholder): write a real note of 1–3 sentences that states exactly why, tied to the choice's own words and the stimulus.
   - Overbroad rules stated as fact ("this answer is always wrong"), mocking or political asides, Logic Games analogies, claims about answer placement: remove or soften them so the teaching point stands. There are no Logic Games on the current LSAT; never mention them.
   - Never change which choice is credited. If you believe the key itself is wrong, record a `flag`, not an edit.
4. New or rewritten text rules: no em dashes (use a comma, colon, or a new sentence); no gendered pronouns for people in the stimulus (use the name, "the author", "they"); plain, direct sentences; teach the reasoning, do not just assert it; no filler ("Great question", "it's important to note").
5. Double-check every proposal: re-read the edited text next to the choice text and stimulus, and confirm the logic and every quote are exact.

## Output
Write JSON Lines to the output path you were given. One object per proposed row edit:
```json
{"item": "short quote of the list item", "qid": "PT146-S3-Q1", "table": "lr_explanation_choice_notes", "row_id": "<uuid>", "column": "body", "style": "standard", "letter": "A", "old": "<exact current full body>", "new": "<full corrected body>", "kind": "slip|misquote|transcription|verdict-only|register|empty|wrong-question", "why": "one sentence: what was wrong and how the new text is correct", "evidence": "the exact stimulus/choice words that prove it"}
```
`old` must be the exact full current value of that column, copied from the mirror. `new` is the full replacement value.

For items you do not fix, write one line: `{"item": "...", "qid": "...", "skip": "reason"}` or `{"item": "...", "qid": "...", "flag": "suspected mis-key or needs a source: reason"}`.

Allowed tables and columns: `lr_explanation_steps.body`, `lr_explanation_steps.label`, `lr_explanation_choice_notes.body`. Do not propose edits to lr_questions or lr_answer_choices; if the problem is in the question or choice text itself, use `flag`.

When finished, reply with: counts of edits, skips and flags; and any item you are unsure of, with the reason.
