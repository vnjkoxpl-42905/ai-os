# Loophole LR question database

The reading library is **inside this Loophole folder**, under `question-database/library/`. Each of the 5,015 question folders contains captured written metadata and Correct CLIR. Questions with speech recordings also contain the full automatic transcript directly in their README, plus separate transcript and original MP3 files. The reader filters by PrepTest, question type, CLIR type and recording status.

- [Search the local question, MP3 and transcript library](library/index.html)
- [Complete question file index and actual file counts](library/INDEX.md)
- [Library usage and provenance](library/PUBLICATION.md)
- [Copied-byte and local-link verification](library/publication-verification.json)

The 2026-10-15 capture covers **168 source pages, 5,015 distinct LR questions, 713 questions with exposed recordings and 4,302 without exposed recordings**. All 5,015 have captured written Correct CLIR. No stimulus, answer choices or correct-answer reveal was collected. The immutable source capture is archived under `raw/sources/loophole-lr-database-2026-10-15/`.

A recording shared by several question citations remains attached to each citation. The reader counts source availability, complete speech text, silent audio and subtitle availability separately. Source URLs remain provenance; reading the files does not require opening the website.

[Source summary and immutable completion proof](../../../wiki/sources/loophole-lr-recordings-2026-10-15.md)

## Verified complete source coverage on 2026-10-15

All **658 unique recordings containing speech** have complete, unreviewed S1 transcripts in **712 question folders**, with the full text included directly in each question README. The remaining source, **PT2.S4.Q19**, is 104.8533125 seconds of exact digital silence. Its original MP3 and independently checked zero-PCM evidence are preserved; it is explicitly marked as having no speech, not given an invented transcript. Together these account for all **659 unique sources and 713 question-linked recordings**.

All 713 original MP3 hashes were verified. There are **710 available S1 subtitle files**. Two speech recordings retain complete transcripts but have no current subtitles: **PT140.S1.Q15** has unordered native timestamps; **PT1.S3.Q11** has a native word ending at 95.013 seconds beyond its 93.12-second audio. Their exact native data are preserved and the reader labels both exceptions. Existing 181 MP4 copies remain optional.

[Portable publication verification](library/publication-verification.json) checks the copied files and local routes. Original processing receipts and native provenance are retained in the library's provenance records. File integrity establishes preservation, not human accuracy review.

The original Desktop folder `Loophole LR Recordings` remains a preserved processing archive, including historical transcript generations, native caches and operational receipts. The portable copy here is the reading home; it excludes machine runtimes, private dictionary backups and processing caches. Existing lecture audio stays in the lecture archive, linked from [the source catalog](../source-catalog.generated.md).

Machine transcripts are unreviewed. Written Correct CLIR and the spoken transcript are kept separate. MP4 copies show a static title card with the recording. Actual question stimuli and answer choices were outside this capture, and correct-answer reveals were not activated.

[Back to Loophole library](../README.md)
