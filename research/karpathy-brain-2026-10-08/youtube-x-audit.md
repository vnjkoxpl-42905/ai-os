# YouTube and X collection can be compiled, with explicit gaps

Read-only structural audit completed 2026-10-08. Every JSONL row was parsed with UTF-8, saved post IDs compared across both ledgers, all monthly archive headings cross-checked, and collection/coverage claims compared with actual files. Original sources remain unchanged. This is structural verification, not a claim that every source's meaning has already been analyzed.

## X totals are rows, not unique Karpathy posts

| Measure | Verified local count |
|---|---:|
| Main ledger rows / distinct IDs | 1,706 / 1,706 |
| Dedicated replies rows / distinct IDs | 269 / 269 |
| IDs repeated across both ledgers | 29 |
| Combined unique IDs | 1,946 |
| Combined unique Karpathy-authored IDs | 1,835 |
| Combined unique foreign-authored IDs | 111 |
| Main ledger rows with reply context | 1,041 |
| Main archive month files | 40 |
| Dedicated reply archive month files | 8 |
| Calendar months in Jan 2023 through Oct 2026 | 46 |

The main ledger includes replies and foreign authors, so calling it 1,706 main Karpathy posts is inaccurate. Foreign posts may be quoted/reposted/contextual material, but they must not be attributed to Karpathy. All archive headings map to ledger IDs, and all ledger IDs appear in the archives. Monthly Markdown is a rendering of ledger evidence, not an independent corroborating source.

## Coverage and truncation remain unresolved

- Main month archives are absent for 2024-08, 2024-09, 2024-10, 2024-11, 2025-08 and 2025-09. Dedicated replies provide some saved items for the latter two; **no Karpathy items exist in either ledger for 2024-08 through 2024-11**. This does not prove the account was inactive or that retrieval exhausted all results.
- Main data spans 2023-01-01 through 2026-10-04; dedicated replies span 2025-08-03 through 2026-03-08. Capture on 2026-10-08 does not establish exhaustive coverage through that date.
- Fifteen main rows retain `textHasShowMore=true`; nine are Karpathy-authored. This explicitly contradicts the assertion that every Show More expansion succeeded. IDs are listed in the JSON audit. A missing flag in the replies schema is not proof that reply text was fully expanded.
- Post `1980665134415802554` has 1,549 characters in the main ledger and only 279 in the dedicated reply ledger. Retain both immutable observations and use the longer version when compiling, with the discrepancy recorded. A naive last-write-wins union would discard real content.
- There are 34 empty text rows in main and two in dedicated replies. Image-only posts may legitimately have no text, so inspect their context rather than automatically discarding them.
- The saved query log contains only 25 weekly windows (2023-01-01 through 2023-06-25), six marked unsuccessful. The gap filler runs only 30 scrolls per month and prints “ALL GAPS FILLED” without proving search exhaustion. These are collection attempts, not a complete X export.
- Images and video are recorded as URLs/flags; **no image or video attachment files are downloaded under raw/x**. No X article bodies were recognized by saved link/flag fields; that absence cannot establish that every article or attachment was collected.
- All 48 monthly archive normalized-text hashes match their recorded manifest hashes. This verifies saved bytes after line-ending normalization, not capture completeness.

## YouTube has 15 channel transcripts plus two new interviews

All 17 official channel upload IDs are enumerated. Fifteen physical timestamped Markdown transcripts match their local raw caption JSON cue-for-cue, totaling **276,900 caption words**. The old manifest's 325,686 words counts entire Markdown files, including description, chapters, timestamp tokens and metadata.

Two animation uploads (`vEnetcj_728`, `Jv1ayv-04H4`) have no available caption tracks, checked with yt-dlp on 2026-10-08. The collector's music-only assertion has not been independently confirmed by listening. The 15 saved videos also include animation/lyric content, so they are not all teaching lectures.

One official-channel caption timing gap exceeds 15 seconds: `TCH_1BHY58I`, 3809.92 through 3830.12 seconds. It may be silence. Caption accuracy and every spoken word have not been independently checked against audio.

The two verified 2026 interview originals additionally have English public-mirror transcripts (Sequoia 6,325 words; No Priors 15,492 words), saved with HTML/provenance/hashes. Their timestamps are grouped mirror start times, not certified fresh original YouTube captions. The author-published cleaned Sequoia transcript remains a separate edited version in the blog domain. Guest talks deferred in the original collection, including Microsoft Build 2023 and Stanford CS231n 2016, remain gaps.

## The collection report overstates completeness

`raw/COLLECTION-REPORT.md` claims all public sources, 100% collection, verbatim fidelity, 1,975 unique X items and continuous 40-month coverage. The actual evidence above does not support those claims. Keep the original report immutable as an operational record; the compiled wiki should cite this audit when explaining coverage.

## Recommended source units for prompt two

- One source page per official YouTube video, with metadata plus raw caption JSON and Markdown as versions of the same source. Keep interviews distinct and label mirror/edited variants explicitly.
- One X source unit per **Karpathy-authored post ID**. Prefer the longest saved text when versions conflict, preserve pointers to both observations, mark truncated items and missing media. Thread links can group units without treating thread members as independent corroboration of repeated claims.
- Foreign-authored posts remain separately authored context; they cannot support claims about Karpathy's personal beliefs solely because the collector included them.
- Monthly X files and manifests are navigation/projection records. They should not count as independent supporting sources.
- Do not promote unverified “complete” labels or infer all speech, all history, all media or all current articles have been acquired.

Full machine-readable counts, exact affected IDs, hashes and evidence paths: [youtube-x-structural-audit.json](youtube-x-structural-audit.json). Existing all-channel cue audit: [all-17 report](../karpathy-channel-all-17-2026-10-08/report.md).
