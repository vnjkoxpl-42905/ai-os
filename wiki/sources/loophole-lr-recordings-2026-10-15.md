---
type: source
subject: Loophole LR question recordings and complete transcript library
created: 2026-10-15
updated: 2026-10-15
aliases: [Loophole LR audio database, Loophole MP3 transcripts, LR Correct CLIR recordings]
tags: [lsat, loophole, logical-reasoning, recordings]
evidence: ../../raw/sources/loophole-lr-database-2026-10-15/final-transcription/superwhisper-completion-status.json
sha256: f0da5496009443904556265c8da78d65018ae1691de3555a126d5cd925c25ca0
contradictions: []
sources:
  - ../../raw/sources/loophole-lr-database-2026-10-15/manifest.json
  - ../../raw/sources/loophole-lr-database-2026-10-15/final-transcription/library-verification.json
---

# Every exposed LR recording is accounted for

The signed-in Loophole Online database capture on 2026-10-15 covered 168 pages and 5,015 distinct LR question records. All have captured written Correct CLIR and classifications. There were 713 question-linked recordings, representing 659 distinct audio hashes, and 4,302 records with no exposed recording. Source publication dates are unknown. [Original manifest](../../raw/sources/loophole-lr-database-2026-10-15/manifest.json).

## Verified delivered coverage

- All 713 original MP3 files are preserved and match their captured download hashes.
- 658 unique recordings containing speech have full clean-profile S1 transcripts, mapped to 712 question folders. Full text is included inside each question README, with exact native word data retained separately.
- PT2.S4.Q19 contains 104.8533125 seconds of exact digital silence, independently decoded and checked. Its MP3 and zero-PCM evidence are retained; no speech transcript is invented.
- 710 subtitle files are available. PT140.S1.Q15 and PT1.S3.Q11 retain their full text but have invalid native timestamps, so current subtitles are withheld rather than repaired with invented timings.
- 181 previously generated MP4 copies remain optional. MP3 and full transcript delivery is the completed scope.

[Final verification evidence](../../raw/sources/loophole-lr-database-2026-10-15/final-transcription/superwhisper-completion-status.json), [independent audit](../../raw/sources/loophole-lr-database-2026-10-15/final-transcription/library-verification.json), [provenance and hashes](../../raw/sources/loophole-lr-database-2026-10-15/final-transcription/PROVENANCE.md).

## Mentions in source

> "complete_all_sources_accounted_machine_transcripts_unreviewed" (final verification status)

> "digital_silence_no_speech" (silent-source finding)

## Find and maintain the material

Start at the [Loophole library](../../corpus/loophole-online/README.md), choose [Logical Reasoning](../../corpus/loophole-online/logical-reasoning/README.md), then the [question database](../../corpus/loophole-online/question-database/README.md). The [published local reader](../../corpus/loophole-online/question-database/library/index.html) and [complete question index](../../corpus/loophole-online/question-database/library/INDEX.md) live inside the current Loophole folder. Their links are relative and the publication is byte-verified against the preserved Desktop processing source.

The publication is generated, not a second manually edited collection. Its manifest distinguishes preserved source files from regenerated reader views. Earlier local-ASR and custom-dictionary generations remain in the Desktop processing tree, outside the preferred clean publication. The [organization report](../../corpus/loophole-online/organization.md) explains ownership and the [router](../../corpus/loophole-online/ROUTER.md) specifies filing.

The [Camo lecture source](loophole-how-to-camo-2026-10-15.md) describes a separate review procedure in which answer and score reveals are delayed. That is relevant context for using this reference library during review; the source does not prescribe these local publication files. The [primary organization-method comparison](loophole-organization-methods-2026-10-15.md) supports preserving captured evidence while compiling portable reading routes.

Coverage and file integrity are verified; word-level human accuracy is not. Written Correct CLIR and spoken captions remain distinct sources. The capture did not acquire question stimuli, answer choices or correct-answer reveals. These are instructor research sources, not approved LSAT U lessons or student assignments. No new curriculum-adoption task is inferred from this integration.

Schema suggestion: none.
