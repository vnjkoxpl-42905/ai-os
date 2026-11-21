# X collection recovered 237 missing posts, then stopped on a persistent site error

Run on 2026-10-08 through the authenticated persistent agent Chrome at localhost port 9223. The original X profile and managed tabs were preserved. Only owned scratch tabs were navigated. This is source collection, not semantic ingestion or persona construction.

## Saved evidence is physical and hash-verified

[Frozen supplement](../../raw/sources/karpathy-brain/supplements/x-browser-20261008T122430Z/PROVENANCE.json) contains append-only observed versions, attempt records, timestamped [Markdown posts](../../raw/sources/karpathy-brain/supplements/x-browser-20261008T122430Z/posts.generated.md), JSONL, comparison metadata, screenshots and [SHA256SUMS](../../raw/sources/karpathy-brain/supplements/x-browser-20261008T122430Z/SHA256SUMS). Nine payload files passed copy/hash verification; the checksum file is additional. Do not resume into this frozen source bundle.

| Result | Verified count |
|---|---:|
| Captured unique Karpathy-authored IDs | 265 |
| IDs absent from both original ledgers | 237 |
| Known truncated posts with longer captured text | 9 of 9 |
| Original weekly windows attempted | 20 of 157 |
| Original plus supplement unique Karpathy IDs, all saved dates | 2,072 |
| Original plus supplement unique Karpathy IDs, requested three-year range | 1,609 |

The 265 capture IDs are not all new. Primary-author checks exclude foreign authors; quoted content remains separately attributed. All nine targeted repairs have nonempty observed versions without a visible truncation flag, but this is not independent certification of every historical word. One additional captured partial (`1980435985730269351`) already has a longer version in the original archive; that original remains intact and must not be replaced by the shorter capture. Incompatible text versions were not found in this comparison.

The formerly empty month ranges now have saved evidence:

| Month | Newly saved IDs |
|---|---:|
| 2024-08 | 62 |
| 2024-09 | 56 |
| 2024-10 | 48 |
| 2024-11 | 62 |

These counts establish recovered posts, not exhaustive coverage of those months. The exact IDs, original/captured text lengths, baseline hashes and unresolved window statistics are in [COMPARISON.json](../../raw/sources/karpathy-brain/supplements/x-browser-20261008T122430Z/COMPARISON.json).

## Why the three-year run is incomplete

The plan spans 2023-10-08 through 2026-10-08 inclusive, plus nine explicit repairs, one older than the search boundary. Nineteen windows stalled after capture. At `since:2023-10-15 until:2023-10-22`, X displayed **Something went wrong. Try reloading.** The collector stopped. One ordinary visible Retry-button click did not clear that error. No further retrieval was attempted, and no rate-limit cause was inferred from this generic error.

There are 137 base weekly windows not yet attempted, plus adaptive retries and detail repairs. The run is stopped, not running in the background. Deleted, private, withheld, deindexed or omitted search results cannot be guaranteed retrievable. Media are URLs/flags, not downloaded attachments. Captured X article bodies remain unreviewed.

## The reusable tool is ready to resume when X works again

External project: `C:\Users\Joshu\dev\ai-os-projects\x-archive-collector`.

- `collector.py`: authenticated-browser DOM collection, date windows, source attribution, visible expansion, append-only records, fair resume scheduling and adaptive splits.
- `analyze_capture.py`: exact comparison against both older ledgers, including new IDs, text variants, repair results and missing-month counts.
- `README.md`: setup and resume command. Active working evidence stays under `runs/karpathy-20261008`; frozen copies remain unchanged.

Eleven tests passed after the next-resume corrections. The script also automatically schedules newly discovered truncated posts. Its error checks read visible UI text only, excluding posts and hidden page code so quoted phrases do not masquerade as browser failures. The stopped run loaded an earlier version; source provenance explicitly distinguishes that from the updated tool version.

The [operating reference](../../references/ai-workspace/x-archive-collector.md) contains the exact resume command and safeguards. The [initial handoff verification](HANDOFF-VERIFICATION.md) remains the baseline audit. This supplement updates its X evidence without rewriting the original collection.

One diagnostic initially read hidden page code rather than just visible UI text. It was corrected, and that output was not saved as source evidence. No cookies, credentials, private API headers, paid service, proxy or stealth tooling were used. Original ledger hashes still match the baseline audit.
