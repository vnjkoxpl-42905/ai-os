---
type: task-list
subject: Fix list, LR explanation project
updated: 2026-09-27
---

# Fix list

The one running list of everything to fix that turns up while working on LR explanations. One line per item here. Anything that needs more than a line gets its own file in this folder, linked from its item. Strike items through with a date when done.

The database is the source of truth for explanations, not the local `Explanations/*.md` files.

## Open

### Explanation content
- [ ] **Five explanations belong to a different question** (students see reasoning for the wrong question). PT108-S3-Q6 (whole explanation, even the stimulus), PT137-S3-Q25, PT143-S4-Q18, PT135-S4-Q25, PT133-S3-Q4. Highest priority. Detail: [[side-issues]] section 1.
- [ ] **PT158-S4-Q22 breakdown steers students to D; the key is E.** Rewrite the breakdown. Detail: [[side-issues]] section 2.
- [ ] **Revamp weak existing explanations: 523 found** (192 Revamp, 100 Weak, 231 Watch), plus ~136 unread rows that probably rate Weak. Joshua does this later, after the 772. Detail: [[revamp-list]]; scores in `revamp-inventory.csv`.
- [ ] **Empty or partial explanations:** 2 with nothing, 16 with no choice notes, 8 with some notes missing, 2 with a placeholder as the correct-answer note (PT147-S4-Q3 D, PT147-S4-Q4 A). Detail: [[side-issues]] section 4.
- [ ] **Fix individual Choice Note problems.** Misquotes, reversed logic, typos, verdict-only notes. Detail: [[choice-note-issues]].

### Data and question bank
- [ ] **The question bank's answer key is wrong on 18 questions** (the DB is right in all 5 checked). PT113-S3-Q21 to Q24 all show key A, which looks like a placeholder. Anything reading the bank key (drills, analytics) marks students wrong. Detail: [[side-issues]] section 2.
- [ ] **Bank misalignment:** PT119-S2-Q19 is matched to a different question, and PT101-S3-Q1's bank text differs from the DB. Detail: [[side-issues]] section 3.
- [ ] **Transcription damage, LSAT Lab leftovers, and small typos in explanations.** Detail: [[side-issues]] sections 5, 6 and 8.
- [ ] **Rename the "Games-y LR" feature tag.** There are no Logic Games on the LSAT.
- [ ] **Question bank `questionType` is unreliable.** 110 raw variants, casing duplicates, some wrong (PT151-S2-Q13 is a Paradox, bank says Most Strongly Supported; PT143-S1-Q6 is a Paradox, bank says Strengthen). Needs a canonical ~25-type set.
- [ ] **110 explained questions have no match in the question bank** (`public/data/PT*-LR.json`), so they have no features or difficulty.
- [ ] **Reasoning-type names don't match the glossary.** Data: "Conditional Reasoning". Glossary: "Conditional Logic".
- [ ] **PT123 to PT138 are thin.** 362 words on average, 51% Complete. Check whether some "Complete" ones are too thin to count.
- [ ] **Diagrams lose their layout in the database.** PT107-S3-Q5 (chain flattened to inline text), PT146-S1-Q21 (transcription damage). Count how many render badly in the app.

### App and loading
- [ ] **The app has two explanation paths.** `useLrExplanation` reads the database; `questionLoader.mergeExplanationSidecars` also fetches `public/data/explanations/PT<n>-explanations.json`, built from the local markdown for PT139 to PT159. Find out which one students see, and retire the sidecars if the database has replaced them. Until then, the PT140 sidecar JSON still carries the thin text.
- [ ] **Where the LSAT U writer mark (Explanation Source) lives.** Probably a column on `lr_explanations`; a migration, needs Joshua's OK. Blocks loading any LSAT U explanation.
- [ ] **`targeted-questions/` layout is unreadable by the parser.** PT134-S1-Q16 and PT158-S4-Q24, in LSAT U's voice. Convert and load, or drop.

### Repo housekeeping
- [ ] **Merge PR vnjkoxpl-42905/lsatu-684d89db#138** (PT154 parser fix), then remove the `projects/lsatu-wt-parser` worktree.
- [ ] **Merge PR vnjkoxpl-42905/lsatu-684d89db#141** (glossary), then remove the `projects/lsatu-wt-glossary` worktree.
- [ ] **Merge PR vnjkoxpl-42905/lsatu-684d89db#142** (removes the thin local `PT140-explanations.md`).
- [ ] **Repo `CLAUDE.md` says commit straight to `main`; memory says branch + PR per session.** One should change.

## Done
