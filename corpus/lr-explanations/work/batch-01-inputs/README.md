# Batch 01 Flaw SQL preparation

Generated from the 40 drafts in `corpus/lr-explanations/drafts/batch-01-flaw-part-a.md` and `batch-01-flaw-part-b.md`, the designated app bank in `projects/lsatu-wt-glossary/public/data`, and the read-only database pull dated 2026-09-28. Run `python system/scripts/lr-explanations/generate_batch01_sql.py` to refresh after any draft or source changes.

**Status: draft, not approved or loaded.** The manifest lists 40 per-slot transactions. Each uses exact current database text guards, inserts only explanation rows, breakdown steps, and choice notes, and aborts if the relevant database rows have changed. `PT102-S3-Q14` and `PT119-S2-Q24` retain their four existing breakdown steps and receive only five missing choice notes. No question, choice, answer key, or existing explanation text is changed.

Preexisting bank/database text disagreements found during preflight:

| Slot | Difference | Effect on this batch |
|---|---|---|
| PT101-S3-Q2 | Database stimulus has “time of drought” and “lush liveliness” where bank has “times” and “lush loveliness”; database choice B has “its the cause” where bank has “is the cause.” | SQL guards exact current database bytes and leaves them unchanged. |
| PT105-S2-Q15 | Database stimulus says “school of official”; bank says “school official.” | SQL guards current database bytes and leaves them unchanged. |
| PT106-S3-Q5 | Bank includes the shared-passage header for questions 5 and 6; database starts with Jane's statement. | SQL guards current database bytes and leaves them unchanged. |

The quoted question text in the drafts uses the bank wording. None of these known differences changes the keyed answer or the intended explanation. No unrecognized draft/bank or database/bank differences passed preflight. The generator's known-variant list is limited to the cases above.

Validation after generation: 40 slots, 156 new steps, 200 new notes. All 40 per-slot files were checked against their draft bodies for exact paragraph breaks and Markdown emphasis. The two notes-only transactions preserve all existing step text and order through exact guards. No database write was performed.
