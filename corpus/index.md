---
type: teaching-notes
subject: Corpus LSAT teaching knowledge
updated: 2026-07-17
aliases: []
---

# Corpus — LSAT teaching knowledge

The second knowledge system: Joshua's LSAT teaching knowledge, built incrementally on the Karpathy LLM-wiki pattern as materials are ingested (books + notes, LSAT Lab, 7Sage material, drills, explanations). Eventually integrates into LSAT U as platform feedstock.

Fills through supervised ingests, one source at a time, logged in [[../wiki/log|the wiki log]]. Raw materials land in `raw/` first (immutable); the corpus holds the synthesized, interlinked teaching pages.

## Conventions

- Pages are LLM-written and LLM-maintained; Joshua curates sources and directs emphasis.
- Wikilink corpus concepts into `students/<name>/` pages when a student is working that area, and into LSAT U material as it ships.
- Question-type taxonomy, method pages, and drill-design principles get their own pages as they accumulate — no empty scaffolding in advance.

## Pages

### `Curriculum/` — the LR curriculum (ingested 2026-07-17)

118 markdown pages recovered from `raw/sources/lsat-curriculum/_stragglers/local-ai-gather/…/Curriculum/` — the corpus folder tree had been scaffolded from this source in the 2026-07-16 rebuild, but the files themselves were never copied. Each topic carries `Notes/` (the teaching) and `Homework/` (the assigned drills).

| Topic | Pages | Topic | Pages |
|---|---|---|---|
| Main Conclusion | 21 | Necessary Assumption | 7 |
| Flaw and Famous Flaws | 11 | Conditional Logic | 7 |
| Abstract | 6 | Causation | 6 |
| Principle | 4 | Role | 4 |
| Sufficient Assumption | 4 | Must be True | 3 |
| Strengthen | 2 | Parallel | 2 |
| Rebuttals | 2 | Comparison | 1 |
| Method | 1 | Most Supported | 1 |
| Parallel Flaw | 1 | | |

- `Curriculum/_question-feature-index/` — 33 pages indexing question features across PTs 101–159 (famous-flaws, complex-conditionals, 2-speaker, science, except, …).
- `Curriculum/_meta/lr-taxonomy.md` — the LR question-type taxonomy.
- `Curriculum/LR/` — 2 homework pages exported live from Google Drive (pilot, 2026-07-17).

**Known gaps:** topics scaffolded but still unfilled — Agree Disagree, Bootcamp, Match Family, Must Be False, Paradox, Quantifiers, Weaken, Reading Comprehension. Their source material is split between `raw/sources/lsat-curriculum/LSAT DUMP/` (many entries are stale `.gdoc` Drive pointers whose IDs no longer resolve) and Google Drive itself, where a past migration converted docs to PDFs/scans under new IDs. Recovering those needs a Drive-side pass, not a local copy.

### `lr-explanations/` — models for writing LR explanations (2026-09-26)

- [[lr-explanations/golden-set]] — the 50 LSAT Lab explanations new LSAT U explanations are modelled on, with the quality rubric.
- [[lr-explanations/golden-set-observations]] — strong-vs-loose comparison, step structure per type, voice notes.
- [[lr-explanations/golden-set-candidates]] — all 80 candidates and the type x feature coverage grid.
- [[lr-explanations/fixes/index]] — the fix list: one line per issue, with detail files beside it (revamp list, Choice Note issues).

