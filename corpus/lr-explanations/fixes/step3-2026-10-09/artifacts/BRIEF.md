# Step 3 brief: rewrite weak LR explanations in LSAT U

You rewrite explanations that students read after answering an LSAT Logical Reasoning question. You write NOTHING to any database. You produce a proposal file; an independent verifier checks every item before anything is applied. Precision beats volume.

## Your inputs
Batch file: a JSON list of qids. Per qid, a packet at `PACKETS/<qid>.json` (load with `python -I`, never read big files wholesale). A packet has: the question (stimulus, stem, five choices, key; `bank` is what students actually read, so quote the bank wording when it differs from the DB), the current explanation (`steps` with position/label/body/row_id; `notes` with letter/body/row_id), and `known_problem` (a reader's note on what is wrong; it may be stale or wrong).

Read the standard before writing:
- `C:/Users/Joshu/dev/ai-os/corpus/lr-explanations/golden-set.md` (what top-tier looks like) and `golden-set-observations.md` (step structure per question type, rubric).
- `C:/Users/Joshu/dev/ai-os/wiki/teaching-voice.md`, `references/lsat-teaching-voice-standard.md` (voice), `wiki/COPY-CORRECTIONS.md`.
- Study 2 to 3 strong explanations of the same type: `python -I C:/Users/Joshu/dev/ai-os/system/scripts/lr-explanations/show.py PT146-S1-Q21` prints one in full (use golden-set qids of your question's family). Model the structure, never copy sentences or examples. Two golden picks (PT145-S2-Q23, PT138-S2-Q25) are reference-only because their logic is wrong; do not use them.

## For each qid
1. Read the stimulus, stem, all five choices and the key from the packet. Work out the correct answer yourself first. If you disagree with the key, do not rewrite: output a `flag`.
2. Read the current explanation. Decide:
   - `rewrite`: it is weak, thin, wrongly registered, wrong, or missing parts.
   - `skip`: it is already good (record why in one sentence). Do not churn good text.
3. A rewrite keeps the existing step structure and reuses each existing row. For every existing step keep its `row_id`, and set `body` (and `label` if needed). Keep a step's body verbatim when it is already sound; improve only what is weak. Do not drop any existing step; if one is junk, rewrite it into something useful. You may add steps (row_id null). If the explanation has no breakdown steps, create the standard set for the type (usually Conclusion, Evidence, Evaluate, Goal; see golden-set-observations for other types).
4. Choice notes: exactly five, letters A to E, each reusing its `row_id` (null if the letter has no row). Standards:
   - Correct-answer note: teaches the move so a student can repeat it on the next question (what in the choice matches the prediction, what it does with the stimulus's words).
   - Each wrong-answer note: says exactly why it fails, tied to the choice's own words and the stimulus, and usually gives a test or counterexample. 1 to 3 sentences, about 20 to 60 words. The most tempting trap may run longer.
   - Never a bare verdict ("This is irrelevant"). Never a role label as the whole note. Never restate the choice and stop.
5. Re-read every quote against the choice or stimulus: exact match to the bank wording. Check every logical claim, especially conditionals (sufficient vs necessary, contrapositive, negation).

## Writing rules (hard)
- No em dashes or en dashes used as dashes. Use a comma, colon, period, or a new sentence. Arrows `→` are fine in diagrams (one chain per line).
- No gendered pronouns (he, she, his, her, him, hers, himself, herself) for people in the stimulus. Use the name, "the author", "the speaker", or "they".
- Never mention Logic Games. Never claim answer-position patterns. No jokes about students, no politics, no "this is always wrong" overbroad rules.
- No internal labels in student text: no "concept lesson", "golden set", "Revamp", production metadata. No filler ("Great question", "it's important to note", "that's the point"). No word "door" as a unit of content.
- Plain, direct, confident, short sentences. Teach the reasoning; do not assert the conclusion. Concrete beats abstract. Speak to the student as "we" or "you". A personal jab at the test is fine, sparingly.
- Keep paragraph breaks as `\n\n` inside a body when helpful. Do not use markdown headers or bullets unless the existing steps already do.
- Never change which choice is credited.

## Output
Write JSON Lines to the output path you are given, one object per qid, in input order:
`{"qid": "...", "action": "rewrite", "explanation_id": "<from packet>", "steps": [{"row_id": "<uuid or null>", "position": 1, "label": "...", "body": "..."}], "notes": [{"row_id": "<uuid or null>", "letter": "A", "body": "..."}], "why": "one sentence: what was weak", "neighbors": ["qids you modelled on"]}`
or `{"qid": "...", "action": "skip", "why": "..."}` or `{"qid": "...", "action": "flag", "why": "suspected mis-key or bank/DB mismatch: ..."}`.
In a rewrite, `steps` lists ALL steps (existing in position order, then any added) and `notes` lists all five.

Write the file with a Python script that builds dicts and `json.dumps(..., ensure_ascii=False)`; put scripts only in your work directory. Double-check each item against the question before you finish.
Reply with: counts of rewrite, skip, flag; and any item you are unsure of, with the reason.
