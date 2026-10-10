# LR correctness cleanup, 2026-10-10

Continued after Step 3's verified 191 rewrites and one agreed skip. Production is authoritative; historical side-issue lists and local mirrors are not current completion counts.

## Verified live corrections

The first two atomic batches applied 18 edits: four question stimuli, six answer-choice fields, three step bodies and five choice-note bodies. Both received independent content and SQL review before application. Fresh read-after queries matched 16/16 and 2/2 edits exactly, including ownership and slots, with no question/choice snapshot mismatches or extra choices. Answer keys were preserved.

- PT157-S3-Q25: corrected Brief and Another Way note D's claim that dietary vitamin C in the placebo group strengthens the no-benefit conclusion. It could blur the comparison; dose and subgroup remain unknown. Changed the choice tag from Strengthens to Too Weak. Preserved the already-correct Standard note exactly.
- PT108-S2-Q18: `grass:` to `grass.`. PT141-S2-Q5: `Lemaitre` to `Lemaître` and `primeval in atom` to `primeval atom`. PT143-S4-Q1: `Trinidadians` to `Trinidadian`. Published bank supports these minimal corrections; PT108 also agrees with original PDF page 17, Q18.
- PT143-S1-Q13: `Bums` to `Burns` in the stimulus, choices B/C, Evaluate and notes B/C/E. The altered E note also replaces the gendered pronoun with the speaker's role.
- PT112-S3-Q8 E: removed serialized quotation/backslash and internal level markup from the tag.
- PT108-S3-Q6: normalized two retained step bodies from CRLF to LF without changing their words or slots.
- Official PDFs settled PT102-S4-Q2 C `insure` to `ensure`, and PT134-S1-Q12 E `government only do` to `government to do only`. The published bank already has the verified wording.

PT132-S2-Q3 modality review is a separate batch. Its Strengthen label is supported by the recorded manual taxonomy decision, the strongest-support stem, and the qualified premise/conclusion. Any later receipt in this folder documents that batch separately; it must not be inferred from the 18-edit receipts.

## Sources and provenance

The targeted Drive downloads were read-only. Canonical source IDs, pages and hashes:

| Question | Official PDF | PDF page | SHA256 |
|---|---|---|---|
| PT102-S4-Q2 C | [pt-102.pdf](https://drive.google.com/file/d/1JPpqybFnHc6QxpSIM5E_-hYDhgvCOr-a/view) | 28 | 34802007018F498CCE8E4412EDA6709956EBFCEA5DF748A4D6C64A5C44B09AC8 |
| PT134-S1-Q12 E | [pt-134.pdf](https://drive.google.com/file/d/1jNXf9y8RxCjmUScBvwzPqp-USBmP0LE_/view) | 7 | 3794A7CF8BC594D018374BE1E1DA25FE695FC77C47D18A546E5818FEBBBADEA0 |

Both are 40-page PrepTest PDFs. A second reviewer independently extracted the relevant pages and confirmed each minimal replacement. PT141 and both PT143 stimulus corrections have published-bank evidence only; no original-PDF claim is made for them. Drive's PT104-105 candidates were one-page set-builder printouts without choices and cannot resolve the remaining disputes.

## Snapshot and guard evidence

`initial-live-snapshot.json`, additional targeted snapshots and `live-bank-source.json` preserve pre-edit evidence. Approved payloads record exact old/new text and MD5. SQL guards require exact source IDs, question ownership, keys, all choices and correctness flags, row identity, old text/hash, positions/letters and labels. Updates enforce exact expected write and verified-hash counts atomically. A wrong-source-hash negative preflight returned false before the first write.

All SQL content uses escaped PostgreSQL E literals and UTF-8/LF file bytes. Old CRLF body guards remain explicit escaped bytes, avoiding the Windows transport error encountered and repaired during Step 3. The Step 4 newline changes intentionally supersede two old Step 3 retained-body expectations.

`apply-receipt.json` and `read-after-receipt.json` document 16 edits; `pdf-apply-receipt.json` and `pdf-read-after-receipt.json` document two. `SHA256SUMS` inventories this evidence folder when closeout finishes.

## Inventory and historical issue reconciliation

PT119-S2-Q19's stale inventory match to PT103-S2-Q24 was corrected to its own bank match, difficulty 4 and no features. The before CSV, dry-run/apply receipt and hashes are retained. All other inventory fields and dated survey prose were preserved. Current published bank and DB agree on PT119-S2-Q19 and PT101-S3-Q1 stimuli, stems, choices and keys after typography/whitespace normalization.

Earlier small typo/platform-leftover targets inspected in this pass no longer contain the reported bad strings. Fifteen Brief styles lack their own notes but have complete Standard/Another Way notes; optional missing Brief notes were not fabricated. PT102-S4-Q19's null tags were also left alone.

## Remaining work and limits

PT104-S1-Q4 A `small/smaller` and PT104-S4-Q8 A `Packing/Packaging` still need authoritative choice text. Documented source-version differences stay explicit. Broader Weak/Watch, unread quality work, model-library depth, diagrams, optional styles and unrelated app housekeeping remain queued.

This is live database content verification, not student visual acceptance. No whole-mirror refresh, app code edit, commit, push, deployment, bootcamp change or Lovable credit spend. Writes used the approved Lovable query_database route on project `53b9a6f2-aba7-4ae4-8dd1-fa5b8aab4d76`, link `link_6a9ad615dcd0819191c81175b974b204`. Task statuses were left unchanged.
