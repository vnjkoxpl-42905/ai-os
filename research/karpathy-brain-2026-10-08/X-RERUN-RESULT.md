# Collector fixed and rerun on 2026-10-08

The rerun stopped on a confirmed X HTTP 429 response at 12:44:57 UTC. It is not running. Three-year coverage remains incomplete.

## Reliability and efficiency changes

The collector now saves mounted posts before handling errors, waits for actual page readiness, bounds ordinary Retry recovery, and stops on rate limits or authentication challenges. A single-writer lock prevents competing runs. In-memory ledgers and conditional exports avoid repeated full-file work. Seventeen tests and independent review passed before the live rerun.

## Actual results

- Base weekly windows attempted: 38 of 157. Another 119 base windows remain untouched; stalled and adaptive windows also remain unresolved.
- Cumulative captured own-author IDs: 432, up from 265 in the first supplement. The 167 additional IDs were already in the original archive; this rerun added zero previously missing IDs.
- The cumulative repair still contributes 237 previously missing IDs and nine longer texts compared with the original archive. These counts must not be added to the earlier supplement as separate discoveries.
- Four loaded observations were saved in the final window before the HTTP 429 stop, exercising the error-preservation fix.
- One captured version remains flagged partial, ID `1761467904737067456`; its longer original version remains preserved. No incompatible text conflicts were found.

The [dated comparison snapshot](x-rerun-progress.generated.json) records the inventory. Original source ledgers remain unchanged.

## Physical evidence and resumption

The cumulative [Markdown archive](../../raw/sources/karpathy-brain/supplements/x-browser-20261008T124542Z/posts.generated.md) is a physical local file. The frozen bundle also contains append-only observations, attempt receipts, comparison and provenance records. All nine copied payload files were hash-verified. Diagnostic screenshots in this cumulative bundle are historical images from the first run; the current rate-limit evidence is the HTTP monitor and attempt receipt.

Resume only from the external working run using the [operating instructions](../../references/ai-workspace/x-archive-collector.md), once X permits requests again. Do not resume into either frozen supplement. Search coverage cannot certify every historical post, and media remain links. No new source material was semantically ingested or promoted to persona instructions during this rerun.
