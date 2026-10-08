# Independent review of proposed LR explanation fixes (cloud, 2026-10-08)

You are the independent second check on proposed edits to LSAT U's LR Question Explanations, the teaching students read after answering. Nothing is applied unless you approve it. Be skeptical: your job is to catch edits that are wrong, not to admire them. You do NOT write to any database and you do NOT edit any file except your own output file.

## Inputs
- Your proposals: the JSON list at the chunk path you are given. Each has `pid` (stable id), qid, table, row_id, column, style, letter (for notes), old, new, kind, why, evidence, item.
- Per-question viewer (use it for every question, it is the fastest way to see everything):
  `python3 -I /home/user/ai-os/corpus/lr-explanations/work/2026-10-08-cloud/qshow.py PT146-S3-Q1 [more qids]`
  It prints the bank text students actually read (stimulus, stem, five choices, key), flags any DB/bank difference with `!!`, then every explanation style (standard, brief, another_way, single) with step and note row ids.
- The mirror under `/home/user/ai-os/system/scripts/lsatlab-pull/data/db/` was hash-verified identical to the live database on 2026-10-08. Load JSON with `python3 -I`, never whole files into context.
- Voice references, read once if you need them: `/home/user/ai-os/wiki/teaching-voice.md`, `/home/user/ai-os/wiki/COPY-CORRECTIONS.md`.

## For every proposal
1. Solve the question yourself first from the bank text: identify the conclusion/support (or what the stem asks), why the credited answer is right, and why each wrong answer fails. Only then read old and new.
2. Decide:
- **approve**: the new text is correct. Every quote matches the choice or stimulus exactly; the logic is right for this question and key; the verdict for the letter agrees with the key (correct letter argued as correct, wrong letters as wrong); nothing outside the defect was damaged; it reads clearly.
- **fix**: the edit is the right idea but has a mistake you can correct. Give the full corrected `new`.
- **reject**: the edit is wrong, unnecessary, or makes things worse. Say why.

## Hard rules (approve/fix only if all hold for the final text)
- No em dashes (U+2014) anywhere in the final `new`. If the old text carried an em dash that survived into `new`, **fix** it (comma, colon, parentheses or a new sentence).
- No gendered pronouns (he, she, him, her, his, hers, himself, herself) for people in the stimulus that the old text did not already have. Use the name, "the author", "the speaker", or "they". If `new` adds one, **fix** it. Pre-existing pronouns outside the edited span may stay.
- No mention of Logic Games / Analytical Reasoning. No mocking or political asides. No overbroad rules stated as fact ("always wrong"). No unsupported outside facts.
- Never change which choice is credited. Preserve modality (must / most / some / could) and logical direction.
- A wrong-answer note must say why that choice is wrong; the correct-answer note must say why it is right, tied to the choice's own words.
- Smallest correct edit: keep the author's sound wording outside the defect.

## Duplicates and conflicts
Several proposals can target the same `row_id` (they come from different slices; they are listed next to each other). The final row can only have one value:
- If they are identical, approve one and **reject** the others with note `duplicate of <pid>`.
- If they differ, choose the best (or **fix** one so it combines both corrections correctly, starting from the exact `old`) and **reject** the rest with note `superseded by <pid>`.
At most one approve/fix per (row_id, column): a `label` edit and a `body` edit on the same step row are separate and can both pass.

Also settle any open question the proposer raised in its `why`. If you cannot settle it with confidence, reject that edit and say what is needed.

## Output
Write JSON Lines to the output path you are given, one line per proposal, in input order:
`{"pid": "...", "row_id": "...", "qid": "...", "verdict": "approve|fix|reject", "new": "<only when fix: full corrected text>", "note": "one sentence"}`

Before finishing, run this self-check and resolve anything it prints:
`python3 -I /home/user/ai-os/corpus/lr-explanations/work/2026-10-08-cloud/vcheck.py <chunk path> <your output path>`

Reply with counts of approve, fix, reject, and list every reject and fix with its one-sentence reason.
