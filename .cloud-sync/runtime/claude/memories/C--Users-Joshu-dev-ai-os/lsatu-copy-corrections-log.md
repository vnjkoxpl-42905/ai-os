---
name: lsatu-copy-corrections-log
description: Before writing or editing LSAT U student copy, read wiki/COPY-CORRECTIONS.md — it lists every wording fix and why it was wrong.
metadata:
  type: feedback
---

Read `wiki/COPY-CORRECTIONS.md` before writing or editing any student-facing LSAT
U copy, and append to it whenever a new correction is made. It pairs with
`wiki/teaching-voice.md`: the voice doc says how the writing should sound, the
corrections log says what has actually gone wrong.

**Why:** Joshua asked for it on 2026-09-07 after a single pass turned up seven
wording errors, several of which broke rules that were already written down.

**How to apply:** never put an implementation name on the page. "Beat" is code
for a method step, students see **step**; "chunk" is code, students see
**piece**. Never "say it back" (it is "tell it back") and never "The Read" (it is
"The Recall"). Never an em dash. Delete a line that repeats the line above it
rather than rewording it.

The deeper lesson, worth applying beyond copy: each rule existed and was enforced
per component, so every new surface started uncovered and the same rules leaked
again. Guards belong with the content, not with whichever component renders it.
`content/instructions-voice.test.ts` now does that.

See also [[lsatu-content-lives-in-postgres]].
