# Step 3 verification: independent check of rewritten LR explanations

Another worker rewrote LSAT U Logical Reasoning explanations. You are the independent check. Nothing is applied unless you approve it. Be skeptical: catch errors, do not admire the prose.

## Inputs
- Proposals: JSONL at the path you are given (see BRIEF.md in this folder for the format and the writing rules the writer had to follow).
- Packets with the question and the OLD explanation: `PACKETS/<qid>.json` (bank = what students read; DB = admin copy; quote-check against the bank wording).
Load JSON with `python -I`. Scripts go only in your work directory.

## For every `rewrite` item
Solve the question yourself first from the stimulus and choices. Then check the full new explanation, step by step and note by note:
1. Logic: every claim about the argument, conditionals, quantifiers, causation and each choice is correct. The correct letter is argued as correct and every other letter as wrong, for the right reason. Prediction in the Goal step matches the credited answer.
2. Quotes: every quoted phrase matches the bank wording exactly.
3. Teaching: wrong-answer notes give a real reason (not a verdict), the correct note teaches a repeatable move, steps are not padded, nothing good in the old text was destroyed without reason.
4. Rules: no em or en dashes as dashes; no gendered pronouns for stimulus people; no Logic Games; no overbroad "always wrong" rules; no internal labels or filler; reads like plain direct teaching.
5. Structure: every old step row_id is present and none dropped; exactly five notes A to E; reused row_ids belong to the right letter/position.

Verdicts: `approve`, `fix` (give the full corrected item in `new`: the complete steps and notes lists in the proposal's format; fix only what is wrong), or `reject` (say why; wrong logic you cannot fix with confidence, key disagreement, etc.).
For `skip` and `flag` items: agree or not. If you disagree with a skip (the old text is in fact weak or wrong), verdict `reject_skip` with the reason. If a flag claims a mis-key, solve the question and say whether the key is right.

## Output
JSON Lines at the output path, one per proposal in input order:
`{"qid": "...", "verdict": "approve|fix|reject|agree_skip|reject_skip|agree_flag|reject_flag", "new": {"steps": [...], "notes": [...]} (only for fix), "note": "one sentence"}`
Reply with counts per verdict and list every fix/reject with its one-sentence reason.
