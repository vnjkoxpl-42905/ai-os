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
- [ ] **Revamp weak existing explanations.** Joshua fixes these later, after the 772 missing ones. Includes all ~126 PT157/158 explicit-Standard explanations. Detail: [[revamp-list]].
- [ ] **Fix individual Choice Note problems.** Misquotes, reversed logic, typos, verdict-only notes. Detail: [[choice-note-issues]].

### Data and question bank
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
