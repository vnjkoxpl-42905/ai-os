# Rewrite brief: Revamp LR explanations (cloud, 2026-10-08)

You are rewriting existing LR Question Explanations that were rated **Revamp** (they fail as teaching or contain errors). Students read these after answering an LSAT Logical Reasoning question on LSAT U. Joshua approved full rewrites with no personal review, so a separate reviewer will solve each question independently and check your draft. Precision beats volume. You do NOT write to any database, and you do not run git.

## Read first (once)
1. `/home/user/ai-os/wiki/teaching-voice.md` (teaching-content register) and `/home/user/ai-os/references/lsat-teaching-voice-standard.md` (the current Joshua-selected standard; it takes precedence over older habits in the corpus). Skim its review rubric.
2. `/home/user/ai-os/wiki/COPY-CORRECTIONS.md`.
3. `/home/user/ai-os/corpus/lr-explanations/golden-set.md` (sections "What separates..." and "Do not copy") and `/home/user/ai-os/corpus/lr-explanations/golden-set-observations.md` sections 5 and 6 (step structure per type, tests, trap names).
4. The model file for your types in `/home/user/ai-os/corpus/lr-explanations/models/` (read its "What the best ones do" section and the Weakness column; never reproduce a listed weakness).
5. One finished example of the output format: `/home/user/ai-os/corpus/lr-explanations/drafts/batch-13-role-part-a.md`.

## Tools
- `python3 -I /home/user/ai-os/corpus/lr-explanations/work/2026-10-08-cloud/qshow.py <qid> [...]` prints the bank text students read (stimulus, stem, five choices, key; bank text has PDF line wraps, ignore them), any DB difference flagged with `!!`, then every explanation style with row ids. Your target is the explanation id given in your list (the `standard` style, or `single` when that is the only one).
- `/home/user/ai-os/corpus/lr-explanations/work/2026-10-08-cloud/revamp/known-defects.json` maps qid -> defects earlier readers found (the inventory note plus step-2 proposals). Your rewrite must not carry any of them.

## For each question
1. Solve it yourself from the bank text before reading the current explanation: conclusion and support (or what the stem asks), the gap or inference, a prediction, why the key is right, why each wrong answer fails, and which wrong answer is the most tempting.
2. Read the current target explanation and the other styles. Reuse any sound reasoning, worked numbers or diagrams, but write fresh text in the house voice.
3. Write the complete Argument Breakdown and all five Choice Notes.

## What a model explanation does (reasoning, not length)
- Breakdown steps follow the type's usual structure (observations section 5): e.g. Conclusion / Evidence / Evaluate / Goal for most argument types; Statements / Evaluate / Goal for Must Be True; speaker-named steps for Agree/Disagree; "Given that ... / How can it be that ... / Evaluate / Goal" or similar for Paradox. Add Intermediate Conclusion, Opposing Point or Concession only where the argument has one. Labels are short nouns (no trailing colon text).
- Evaluate argues with the argument: name the gap, the flaw, the inference or the conflict, with a concrete example or worked numbers when that makes it click.
- Goal predicts the answer's content (often in two acceptable shapes), not just the task.
- Each choice note runs the test its type calls for (negate it for NA; "fails to consider X" -> does X weaken; a rule proves only its right-hand side; "why should we believe this?" for Role/MC; can both Agree and Disagree positions be supported; etc.), quotes the choice's own words where it matters, and says exactly why it is right or wrong. The most tempting wrong answer gets the most attention. The correct-answer note teaches the transferable move.
- Wrong-answer notes are usually 1-3 sentences; the correct note and the main trap can be longer. No padding.

## Hard rules
- **No em dashes (U+2014)** anywhere. Use a comma, colon, parentheses or a new sentence. Arrows `→` are fine in diagrams; put each diagram chain on its own line.
- **No gendered pronouns for people in the stimulus.** Use the name, "the author", "the speaker", "they".
- No Logic Games analogies or mentions. No mocking the question or answers, no political asides, no unsupported outside facts, no invented quotations, no broad false rules ("always wrong"), no claims about answer placement. No filler ("Great question", "It's important to note").
- Never argue for a letter other than the key. If you believe the key or the question text is wrong, do not draft; record a flag.
- Preserve modality (must / most / some / could) and logical direction exactly. Every quote must match the bank text exactly.

## Output
Write one markdown file to the output path you are given, in exactly this format (the parser depends on it):

```
## PT157-S2-Q12 | Flaw | B
explanation_id: 395281fb-7c82-4015-ac20-8df0d0b7beaa

### Argument Breakdown

**Conclusion:** ...

**Evidence:** ...

**Evaluate:** ...

**Goal:** ...

### Choice Notes

**(A) Circular.** ...

**(B) Correct.** ...

**(C) Wrong Flaw.** ...

**(D) Wrong Flaw.** ...

**(E) Wrong Flaw.** ...
```
- Header: `## <qid> | <type as listed> | <key>`, then the `explanation_id:` line.
- Steps: `**Label:** body` paragraphs. A step body can contain several paragraphs separated by a blank line, and diagram lines; never start a body paragraph with `**`.
- Notes: `**(X) Tag.** body`, letters A to E in order. The tag is a short trap name from the observations list ("Correct" for the key); it is shown to students next to the note.
- If you flag a question instead of drafting it, write `## <qid> | FLAG` followed by one paragraph explaining why.

Write each question to the file as soon as it is done so progress survives interruption. When finished, run
`python3 -I /home/user/ai-os/corpus/lr-explanations/work/2026-10-08-cloud/revamp/parse_drafts.py <your output path>`
and fix everything it reports. Reply with the count drafted, any flags, and any question you are less than confident about.
