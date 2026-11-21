---
type: source
subject: Loophole Book Extras Bootcamps capture
created: 2026-10-18
updated: 2026-10-18
aliases: [Loophole Bootcamps, Referential Phrasing drill, Book Extras drill questions, Loophole answer feedback]
evidence: ../../raw/sources/loophole-bootcamps-2026-10-18/inventory.json
sha256: 4339638229d0c9c91f634a50c167cff12aae0239b19378e7b26ba7b3a5dce8c8
contradictions: []
sources:
  - ../../raw/sources/loophole-bootcamps-2026-10-18/inventory.json
  - ../../raw/sources/loophole-bootcamps-2026-10-18/PROVENANCE.md
  - ../../raw/sources/loophole-bootcamps-2026-10-18/SHA256SUMS
  - ../../raw/sources/loophole-bootcamps-2026-10-18/referential-initial.json
  - ../../corpus/loophole-online/bootcamps/verification.generated.json
tags: [llm-wiki, lsat, loophole, teacher-research]
---

# Preserve each Bootcamp question with its observed response

Ellen Cassidy / Loophole Online. Publication dates unknown. Capture date: 2026-10-18. Joshua requested the open Referential Phrasing drill and the full Bootcamps collection, including questions, choices, correct answers and instructor comments in their source format. These are attributed private teacher-research captures. Filing them does not approve LSAT U adoption, publishing or assignment.

## All 57 visible drill sequences are captured; 13 licensed stimulus occurrences remain gated

The rendered chapter inventory exposed **57 drills**. The [Bootcamps library](../../corpus/loophole-online/bootcamps/README.md) preserves all 57 observed drill sequences and **616 question pages: 607 answerable questions and nine information pages**. All 607 answers have observed success proof; all 14 observed instructional images are preserved locally, with zero image-download gaps. Its [generated verification report](../../corpus/loophole-online/bootcamps/verification.generated.json) records `uiCaptureComplete: true` and `fullReferencedStimuliCaptured: false`.

**Thirteen question occurrences** reference licensed LSAT stimuli hidden by the source's Upgrade to Practice control. Their citations, visible drill prompts, choices, successful response states and available feedback are preserved; their hidden stimulus text was not recovered. This includes Referential Phrasing questions 4 and 5. Full source-content completeness remains false even though the observed UI sequence is captured and the archive is finalized. No access controls were bypassed.

Each drill contains the original observed JSON, readable exact-source question/choice/feedback HTML in Markdown, standalone formatted HTML and locally preserved instructional image assets. The site stylesheet is not reproduced. Strong/emphasis markup and instructional list structure are retained. Original captured HTML remains in JSON. Referential Phrasing also includes nine [original first-traversal states](../../raw/sources/loophole-bootcamps-2026-10-18/referential-initial.json), keeping the transient instructor comments shown after correct responses to questions 1, 2 and 5. These comments no longer appeared during the later replay; both source generations remain explicit and the earlier states are included as supplements.

The browser capture uses rendered page content and actual question/answer controls, not guessed private endpoints or authentication extraction. Observed attempts and final states are distinct. An already-answered question may expose a successful state without a newly submitted attempt. Correct-answer annotations derive only from captured successful final selection styling or a successful submitted attempt. Information pages need no answer. Missing proof remains explicit.

Only response branches actually observed are preserved. The collection does not claim every possible wrong-answer comment, independent pedagogical validation, or an audio transcription. Scripted answer interactions change the signed-in account's drill attempt/progress state as part of the requested traversal.

## Mentions in source

> "BOOTCAMP NAME" (rendered chapter inventory)

> "STARS EARNED" (rendered chapter inventory)

> "BEST ATTEMPT" (rendered chapter inventory)

## Capture and retrieval can be repeated

[Packaging helper](../../system/scripts/package-loophole-bootcamps.py) builds the portable library and generated catalogs from source JSON, preserves browser-observed instructional image URLs as local files, and refuses finalization until all 57 inventoried drills have resolved question sequences and verified answers. Finalization wrote archive provenance and a SHA-256 manifest after question capture and image preservation. Finalization certifies the observed UI inventory and saved bytes; it does not certify hidden licensed stimuli or every alternative wrong-answer feedback branch.

[Shared retrieval](../../corpus/loophole-online/AI-RETRIEVAL.md) supports `python system/scripts/query-loophole.py search "Referential Phrasing" --kind bootcamp --limit 3`. The retrieval index was rebuilt after final packaging so catalog freshness guards and source fingerprints reflect this generation. Returned excerpts locate the source; read the complete drill before relying on its teaching.
