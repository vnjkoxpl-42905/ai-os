# The Karpathy collection is usable, but Prompt 1 is not exhaustively verified

Verified on 2026-10-08 against the local collection at `raw/sources/karpathy-brain/raw/`. Original sources and collection reports were preserved. This report supersedes the handoff's completeness claims, not its source files.

**Later update on 2026-10-08:** the [X repair result](X-REPAIR-RESULT.md) adds 237 previously missing post IDs and longer text for all nine previously flagged Karpathy posts in a separate frozen supplement. Its collection stopped on a persistent X site error after 20 of 157 weekly windows. The baseline counts below describe the original collection; they are not the updated combined total.

## What physically exists

A recursive local file count found **1,540 files, totaling 80,301,723 bytes**, including companion representations, metadata, scripts and the two subsequently acquired interview bundles. The handoff's 3,278 figure mixes logical articles, GitHub files, videos and X ledger rows; it is not a physical file count. Thousands of X records are stored inside a few ledgers and monthly Markdown files. These different units must not be added together as files.

| Domain | Verified saved material | Important limit |
|---|---|---|
| Blog | 79 Markdown pages match recorded hashes; 79 companion HTML files and one RSS file exist | Medium is best effort; three course URLs failed; 30 course pages have shared authorship; Markdown punctuation was transformed |
| GitHub | 1,209 files match recorded hashes across 54 repository and 13 gist snapshots | Histories, issues, branches and some file types were excluded; imported datasets and third-party material dominate word count |
| Official YouTube channel | 17 upload IDs inventoried; 15 timestamped transcripts match saved caption cues | Two uploads have no captions; caption fidelity to every spoken word remains unverified; saved videos include animation material |
| Additional 2026 interviews | Two physical English mirror transcripts, with provenance | Mirror grouping and editing may differ from original audio; these do not establish every 2026 appearance was found |
| X | 1,975 rows represent 1,946 distinct IDs, including 1,835 Karpathy-authored and 111 foreign-authored IDs | Nine Karpathy records explicitly remain truncated; four months have no saved Karpathy items; attachments are links/flags, not downloaded media |

## Corrections that matter for the brain

- Do not infer Karpathy's beliefs or voice from the 111 foreign-authored X items, government occupation pages, Shakespeare text, generated scores, dependencies or vendor libraries. Preserve them as attributed context or data.
- The 4,892,153 GitHub words include 3,068,239 words of government HTML. Conservative screening leaves 742,795 candidate code/documentation words, without proving sole authorship. Raw volume is not personal knowledge volume.
- The 15 channel transcripts contain 276,900 caption words. The older 325,686 metric includes Markdown metadata and timestamp tokens.
- X has 29 cross-ledger duplicate IDs and one differing text version. Preserve both observations for post `1980665134415802554`; the longer saved version contains additional text. Neither version is an independent source.
- January 2023 through October 2026 spans 46 calendar months. Forty monthly main files do not establish continuous or exhaustive coverage. Both ledgers lack Karpathy items for 2024-08 through 2024-11; this is an unresolved collection gap, not proof of account inactivity.
- Image/video URLs are not equivalent to physical attachment files. Media contents remain unreviewed.
- Do not repeat claims of every public source, every expanded post, every spoken word or character-verbatim Markdown. The saved evidence does not establish those claims.

## Prompt 2 can begin with explicit coverage

The original LLM Wiki framework gist is present. Apply it within the current AI OS schema: immutable evidence, source pages, supported principles/methods, an index, an append-only log and a Karpathy hot page under 500 words. Preserve Joshua's identity, teaching voice and current routing.

One logical source means an article, repository/gist snapshot, video or identifiable X post/thread. HTML plus Markdown, monthly projections and duplicate copies do not become independent corroboration. Every attributed claim needs an exact source quote. Representative reads do not establish whole-corpus semantic ingestion.

The initial wiki compilation is deliberately labeled partial. Final seven rules, runtime agents, teaching skills and hooks are later video stages; none is verified or installed by this handoff audit.

## Collection repair remains open

Recover the nine explicitly truncated Karpathy posts; investigate the four empty month ranges and unsuccessful searches; enumerate the previously deferred talks; establish what media contains useful evidence. Preserve provenance and observed text versions. Do not mark a source complete merely because an extraction script finished.

Detailed evidence and exact affected records:

- [Blog/GitHub findings](blog-github-audit.md) and [per-file ledger](blog-github-audit.json).
- [YouTube/X findings](youtube-x-audit.md) and [record-level evidence](youtube-x-structural-audit.json).
- [All 17 channel uploads](../karpathy-channel-all-17-2026-10-08/report.md).

The integrity audit is complete for the registered text payloads described in these reports. Full semantic reading and compilation of the entire collection are **not complete**.
