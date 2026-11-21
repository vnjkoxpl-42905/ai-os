---
type: reference
subject: Rules for naming and filing downloaded files
created: 2026-10-14
updated: 2026-10-14
status: draft, awaiting Joshua's answers
aliases: [file rulebook, Downloads rulebook]
tags: [ai-workspace, files, aq-014]
---

# File rulebook: where a downloaded file goes and what it is called

Draft for queue item AQ-014, steps 1 and 2. Nothing has been moved, renamed or deleted. The rules below become active only after Joshua answers the questions at the bottom and approves a proposal table (step 4). Until then this page is a proposal.

## 1. Snapshot of ~/Downloads (read-only, 2026-10-14)

Taken with `os.scandir` and file stats only. File contents were read once, solely to hash same-named copies.

**182 files, 0 folders, 7.2 GB.** Oldest 2026-09-06, newest 2026-10-14. Everything older seems to have been cleared around 2026-09-06.

| Type | Files | Size |
|---|---:|---:|
| .html / .htm | 71 | 13 MB |
| .pdf | 31 | 277 MB |
| .exe (installers) | 22 | 2.0 GB |
| .crdownload (unfinished downloads) | 13 | 705 MB |
| .md | 11 | 0.1 MB |
| .jpg / .jpeg / .png | 15 | 1.3 MB |
| .zip | 9 | 3.3 GB |
| .json | 3 | 1.9 MB |
| .mp4 | 1 | 887 MB |
| .csv, .epub, .dmg, .txt, .ini, .winmd | 6 | 67 MB |

| Age (by modified date) | Files |
|---|---:|
| 0 to 7 days | 107 |
| 8 to 30 days | 47 |
| 31 to 90 days | 28 |
| over 90 days | 0 |

**What stands out**

- **Repeat downloads.** 80 files carry a browser `(n)` suffix. 19 name groups have copies; in 15 of them every copy is byte-identical (SHA-256), which is 73 redundant files. The biggest are `SMAKR_interactive_framework` (23 copies), `SMAKR` (18), `LSAT_U_Command_Center_Project_Instructions` (8). Four groups differ by content: the Antigravity, ChatGPT and Chrome installers (different versions) and `@Kling_ai.htm`.
- **Half the space is three archives**: an AI-OS Drive export zip (1.6 GB, 2026-09-06), `kali natesa.zip` (1.6 GB) and one 887 MB video.
- **13 unfinished `.crdownload` files** (705 MB), 11 of them from 2026-09-06.
- **22 installers**, several already superseded by a later copy (Antigravity x3, Brave x3, Chrome x2, ChatGPT x2).
- **LSAT material**: 17 PrepTest PDFs (`pt 101.pdf` and so on), two copies of a 126 MB LR book, LR guideline and quantifier notes, an LSAT Lab JSON export, the conditional cheat sheet PNG, and about 40 lesson HTML drafts (SMAKR, conditional charts, role-question formats, answer-choice traps).
- **Finance**: two invoices and two receipts (2026-10-14) and one bank-style `accountactivity.csv`.
- **Identity documents**: two passport scans. Under the vault rule, government IDs stay outside this OS.
- **Admissions**: three fee-waiver PDFs (University of Toronto / OLSAS).
- **Personal**: a book (.epub), a personal video, an academic article PDF.
- **Vault leftovers**: an LSAT U database backup zip (2026-09-22), Obsidian Web Clipper settings JSON, a `session-handoff` SKILL.md, two README links files.

## 2. Proposed tree

Two kinds of destination. **Vault homes** take only what the vault already has a place for. Everything else goes to a plain folder outside the vault, so personal and sensitive files never enter the git-backed OS.

```
C:\Users\Joshu\dev\ai-os\                (vault: existing homes only)
  raw\inbox\                             teaching or research sources to ingest (lesson drafts, notes, clips)
  students\<name>\                       anything about one student, per students/README.md

C:\Users\Joshu\Documents\Files\          (outside the vault; name is a proposal)
  Business\
    Finance\YYYY\                        invoices, receipts, statements, account exports
    Admin\                               contracts, platform paperwork
  LSAT\
    PrepTests\                           PT PDFs, one per test
    Books\                               published prep books
    Lesson-drafts\                       HTML/MD drafts not yet ingested
  Admissions\                            fee waivers, applications
  Personal\
    Identity\                            passport and other IDs (outside the vault by rule)
    Reading\                             personal books
    Media\                               personal video and photos
  Software\Installers\                   latest installer per app, older versions flagged
  Archives\                              large exports and backups (Drive exports, DB backups)

Downloads\                               stays the landing zone; files older than N days get proposed
```

## 3. Naming patterns

| Kind | Pattern | Example |
|---|---|---|
| Dated record (invoice, receipt, statement) | `YYYY-MM-DD_<who>_<what>.<ext>` | `2026-10-14_<vendor>_invoice-0017.pdf` |
| Document | `<subject>_<short-description>.<ext>`, lowercase, hyphens | `lr_question-type-guideline.pdf` |
| PrepTest | `PT<nnn>.pdf` | `PT101.pdf` |
| Student file | follow the student folder's existing names | `students/celia-cutler/...` |
| Project folder | `<project>-<YYYY-MM>` | `smakr-2026-10` |
| Installer | keep the vendor name, which carries the version | `Git-2.55.0.5-64-bit.exe` |

Common rules: no `(1)` suffixes (a byte-identical copy is proposed for removal only on Joshua's word, never deleted automatically); no spaces in new names; dates in `YYYY-MM-DD`; keep the original name in the proposal table so every rename is traceable.

## 4. When to ask instead of filing

- The file names a person and could be a student record, a prospect or neither.
- Two copies share a name but differ in content.
- The file is an identity document, bank export or anything with account numbers: propose the outside-vault location, never the vault.
- The file is over 500 MB, or is an unfinished `.crdownload`.
- The area is unclear from name and type alone. Content is not opened to decide unless Joshua allows it.
- Any delete. Removal happens only on Joshua's explicit word, item by item.

## 5. Questions for Joshua

1. **Outside-vault root.** Is `C:\Users\Joshu\Documents\Files\` the right home for non-vault files, or do you want Google Drive (`G:\My Drive\...`) so they reach the phone?
2. **Areas.** Are Business, LSAT, Admissions, Personal, Software and Archives the right top level? Anything missing (church, Aspiring Attorneys versus LSAT U split)?
3. **Lesson HTML drafts** (SMAKR, conditional charts, role-question formats): do they go to `raw/inbox/` for ingest, to the LSAT U repo, or to an outside `Lesson-drafts` folder?
4. **PrepTest PDFs and the LR book**: is there already a canonical home for these (corpus or elsewhere) that they should join?
5. **Duplicates.** 73 byte-identical copies exist. Do you want the proposal to list them for removal (you approve each batch), or leave them and only file one copy?
6. **Installers and `.crdownload` files** (2.7 GB together): propose removal of superseded installers and dead partial downloads, or keep everything?
7. **Passport scans**: confirm they leave Downloads for an outside-vault Identity folder, and which one.
8. **Large archives** (AI-OS Drive export, `kali natesa.zip`, the 2026-09-22 LSAT U backup): keep, move to Archives, or are they already backed up elsewhere?
9. **Age threshold.** After how many days should a file in Downloads appear on the next proposal (7, 14, 30)?
10. **Recurring trigger** (step 5): one-off proposal only for now, or do you want it weekly later?


## Proposal defaults adopted for this review (2026-10-26)

Joshua authorized choosing practical source improvements. Use the existing area-first tree and naming examples above to produce proposals, with a 14-day review age as an operational default, not a claimed personal preference. The outside-vault root remains a proposed destination until an actual row is approved. Student evidence uses existing student homes; raw research enters the single inbox. Identity documents remain outside this vault.

Do not move, rename or delete Downloads based on this general source-implementation request. A concrete original/new-name/destination proposal still needs approval for its rows, and unresolved student identity or different-content generations stay explicit. No recurring trigger is created. The historical ten questions remain preserved; ask only a question that changes an actual proposed row rather than making all ten prerequisites to a read-only proposal.

[Refreshed metadata snapshot](../research/2026-10-26-source-implementation/downloads-snapshot.json): 194 regular files, 5305489837 bytes. This count supersedes the old snapshot only; file contents, duplicates and existing backup coverage were not rechecked. AQ-014 remains open for a concrete filing batch.
