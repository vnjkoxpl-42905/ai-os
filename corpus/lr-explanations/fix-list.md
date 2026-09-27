---
type: task-list
subject: Running fix list, LR explanation project
updated: 2026-09-26
---

# Things to fix, noticed along the way

A running list. Anything spotted on the side while working on LR explanations lands here so it is not lost. It is not the revamp list (weak explanations to rewrite: [[revamp-list]]) and not the choice-note list ([[choice-note-issues]]). Each item says where it was seen. Strike through with a date when done.

The database is the source of truth for explanations. The local `Explanations/*.md` files are ignored unless a note says otherwise.

## Open

### Data and question bank
- [ ] **Question bank `questionType` is unreliable.** 110 raw variants, casing duplicates, some types wrong (PT151-S2-Q13 is a Paradox, the bank says Most Strongly Supported; PT143-S1-Q6 is a Paradox, the bank says Strengthen). Needs a canonical ~25-type set. Seen: golden-set survey, 2026-09-26.
- [ ] **110 explained questions have no match in the question bank** (`public/data/PT*-LR.json`), so they carry no features or difficulty. Seen: golden-set survey.
- [ ] **Reasoning-type names don't match the glossary.** Data says "Conditional Reasoning", glossary says "Conditional Logic". Seen: coverage report.
- [ ] **PT123 to PT138 are thin.** 362 words on average and only 51% Complete. Their gaps are in the coverage worklist already; check whether some "Complete" ones are too thin to count. Seen: golden-set survey.

### Schema and loading
- [ ] **Where the LSAT U writer mark (Explanation Source) lives.** Probably a column on `lr_explanations`; that is a migration and needs Joshua's OK. Blocks loading any LSAT U explanation.
- [ ] **`targeted-questions/` layout is unreadable by the parser.** PT134-S1-Q16 and PT158-S4-Q24 are written in LSAT U's voice in a different layout. Decide whether to convert and load them.
- [ ] **Diagrams lose their layout in the database.** PT107-S3-Q5 (chain diagram flattened to inline text), PT146-S1-Q21 (transcription damage). Check how many diagram-bearing explanations render badly in the app.

### Repo housekeeping
- [ ] **Merge PR vnjkoxpl-42905/lsatu-684d89db#138** (PT154 parser fix), then remove the `projects/lsatu-wt-parser` worktree.
- [ ] **Merge PR vnjkoxpl-42905/lsatu-684d89db#141** (glossary: Explanation Source, Coverage State), then remove the `projects/lsatu-wt-glossary` worktree.
- [ ] **Repo `CLAUDE.md` says commit straight to `main`; memory says branch + PR per session.** One of them should change so sessions stop having to choose.
- [ ] **Local `Explanations/PT140-explanations.md` is a thin, different version** of what is in the database (~100 vs ~630 words per question). Harmless while the database is the source, but a re-run of the ingest from local files would overwrite better text with worse. Guard or delete.

## Done
