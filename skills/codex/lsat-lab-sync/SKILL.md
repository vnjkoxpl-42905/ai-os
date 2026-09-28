---
name: lsat-lab-sync
description: Pull LSAT Lab's data in bulk and audit or sync the LSAT U LR question bank and database against it, with scripts instead of clicking through pages. Use when Joshua says "pull from LSAT Lab", "sync with LSAT Lab", "tag these questions", "check the bank against LSAT Lab", "are any answer keys wrong", "is anything misfiled", "which explanations does LSAT Lab have that we don't", "full scan", or after any import into public/data/PT*-LR.json or the lr_* tables. Covers difficulty, reasoning type, features, answer keys, question text, choice text, missing slots and explanation coverage.
---

# LSAT Lab sync

Everything lives in `system/scripts/lsatlab-pull/` in the vault; its `README.md` has the endpoint details. Run the LSAT U steps from an LSAT U checkout on its own branch (never the main checkout another session may be using), and ship bank changes as a PR.

## Two sources, pick by need

| Need | Source | Login |
|---|---|---|
| Difficulty, question type, features, reasoning type for all 10,171 LSAT Lab questions | `app.lsatlab.com/my/services/get-questions-just-props.php` + `/api/question-properties`, fetched inside a logged-in tab | Yes |
| Full question and answer-choice text, answer key, and written explanations for one question | `app.lsatlab.com/api/questions/<id>`, using `qid` from `data/questions-props.json` | Yes |
| Answer key, answer %, trap labels, written explanation, question text, first words of each choice, each test's question list | public pages `www.lsatlab.com/lsat-explanations/PT<n>-S<s>-Q<q>` via `crawl_public.py` | No |

The public pages cut choices short. Use the logged-in `/api/questions/<id>` response's `answers[]` for full choice text; the official PrepTest PDFs Joshua keeps in Downloads are another source for adjudicating a disagreement.

## 1. Refresh the logged-in data (only when tags may have changed)

Use a logged-in Codex browser tab, or skip this step and use the existing data/ files. Joshua must already be logged in to `app.lsatlab.com`; never enter his password. Run the two snippets in the README with the browser JavaScript tool: `properties.json` comes back inline; the big question list downloads to Downloads, then move it to `data/questions-props.json`.

## 2. Crawl the public pages

```bash
python <vault>/system/scripts/lsatlab-pull/crawl_public.py            # every LR slot in the bank
python <vault>/system/scripts/lsatlab-pull/crawl_public.py --pts 113  # one test
```
~4,000 pages, 6 workers, resumable (skips slots already in `data/public/`). Run it in the background. Delete `data/public/` to force a refresh.

## 3. Pull the database (read-only)

```bash
python system/scripts/lsatlab-pull/db_pull.py   # from the vault root; writes data/db/
```

## 4. Audit

```bash
python <vault>/system/scripts/lsatlab-pull/audit_bank.py --db <vault>/system/scripts/lsatlab-pull/data/db --out <report.md>
```
Findings: `key_mismatch` (bank / database / LSAT Lab disagree), `stimulus_not_on_lsatlab` / `stem_not_on_lsatlab` / `choice_not_on_lsatlab` (wrong or damaged question text), `db_stimulus_not_on_lsatlab`, `in_lsatlab_not_in_bank` / `in_bank_not_in_lsatlab_list` (missing or extra slots), `lsatlab_explained_lsatu_not` (LSAT Lab has a written explanation where LSAT U's Coverage State is not Complete), `labels_differ`.

Read a sample of every finding type before reporting it. Text checks compare normalized prefixes, so a hit can be a formatting difference; say which you confirmed.

## 5. Fix

- **Labels:** `tag_bank.py --slots ... | --slots-file ... | --missing`, then `node scripts/build-question-bank.mjs`. LSAT Lab's current tags win (Joshua, 2026-09-27). Never touches question type.
- **Wrong question in a slot:** the database text is usually right. Confirm on the LSAT Lab page, then rebuild the slot: stimulus + stem + key from the database, choices from the PDF. See `corpus/lr-explanations/fixes/` for the 2026-09-27 repair.
- **Answer keys:** a disagreement goes to Joshua before anything changes ("I think this question is marked wrong"), with the three sources side by side.
- **Explanations:** database edits go through a snapshot in `raw/sources/lsatu-lr-snapshots/` first, then Lovable `query_database`.
- Ship: PR, merge when Joshua says, then `deploy_project` (free) and confirm the change on lsatprep.study by fetching the file.

## Record

Append findings to `corpus/lr-explanations/fixes/index.md` and a line to `wiki/log.md`.
