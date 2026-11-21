---
type: reference
subject: Resumable X public-post collection
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [x, karpathy, source-collection, browser]
sources: []
---

# Collect visible X posts without replacing the older archive

The free Python collector lives outside this Obsidian vault at `C:\Users\Joshu\dev\ai-os-projects\x-archive-collector\collector.py`, with a local `.venv`, README and tests. It attaches to the already authenticated persistent agent Chrome through `http://127.0.0.1:9223`. Existing tabs stay open. Only owned scratch tabs are navigated. Credentials are never exported.

The default search covers **2023-10-08 through 2026-10-08 inclusive**, prioritizing the missing 2024-08 through 2024-11 interval. Nine known truncated posts receive explicit detail-page repairs, including one older than that search range. Replies returned by `from:karpathy` are included; foreign quoted text remains separately attributed.

## Resume the authorized collection

Run from the external project directory, with only one collector writing this run:

```powershell
.\.venv\Scripts\python.exe collector.py --resume --out '.\runs\karpathy-20261008' --repair-audit 'C:\Users\Joshu\dev\ai-os\research\karpathy-brain-2026-10-08\youtube-x-structural-audit.json' --max-windows 5000 --max-scrolls 40 --delay 1.5
```

`--inspect` checks the existing X login without navigation. `--plan` lists date windows offline. `--max-windows` bounds an invocation; hitting a budget never means complete. Base weekly windows precede adaptive splits; resume gives untouched windows priority so early stalled dates cannot monopolize later invocations.

## Evidence survives interruption

Append-only `observations.jsonl` stores distinct observed versions with author, timestamp, URL, primary text, separately attributed quoted content, media links, truncation state and query window. Append-only `window-attempts.jsonl` records attempts and their actual outcomes. Generated Markdown/JSONL select the longest available text but retain truncation and conflict flags; all original versions remain in the observations ledger. A longer flagged partial version must not be described as verified complete.

The collector captures the mounted DOM before scrolling and before/after visible expansion clicks. Search results outside the requested window are flagged; post timestamps enforce the global date boundary. Known targeted repairs are explicitly exempted from that boundary. Images, videos and attached articles remain unreviewed media links, not downloaded attachments.

Keep active runs in the external project. After stopping or finishing, freeze a separate evidence bundle under `raw/sources/karpathy-brain/supplements/`, verify its hashes, and never resume into that frozen bundle. Compare new IDs and text variants against the original collection; do not overwrite old observations or silently adjudicate incompatible versions.

## What has been verified

On 2026-10-08, the persistent Chrome had a signed-in Karpathy profile tab. A live priority-window test saved 27 distinct posts/replies and stopped with an explicit stalled status. Eight offline tests passed, including complete date-plan coverage, quote-only attribution, foreign-author rejection, variant preservation, resume splitting, fair scheduling and corrupt-ledger rejection. The full collection was launched afterwards; inspect its current attempt ledger for progress.

That expanded run stopped after 20 of 157 weekly windows on a persistent X site error. One visible Retry failed to clear it. The [frozen result](../../research/karpathy-brain-2026-10-08/X-REPAIR-RESULT.md) contains 237 previously missing IDs and longer text for all nine known partial posts. Eleven tests passed after follow-up corrections; the script is ready to resume, but is not currently running.

Joshua authorized another reliability pass and rerun on 2026-10-08. Seventeen tests and independent review passed after adding loaded-row preservation before errors, adaptive readiness, one bounded generic-error Retry, X-host HTTP 429 detection, a single-writer lock and in-memory ledger/export optimizations. That rerun stopped on confirmed HTTP 429 after 38 of 157 base windows. Cumulative capture contains 432 IDs; its 167 additional recaptures were already in the original archive. See the [rerun result](../../research/karpathy-brain-2026-10-08/X-RERUN-RESULT.md) and dated [comparison snapshot](../../research/karpathy-brain-2026-10-08/x-rerun-progress.generated.json). Resume after X permits requests; do not retry through its limit.

X search does not establish an exhaustive account export. Missing results, deleted/private/withheld posts, unavailable media and stalled windows remain limitations. Login challenges, human verification and rate-limit errors stop collection. No stealth, proxies or attempts to bypass restrictions are included.

Related: [Karpathy compilation](../../wiki/karpathy/index.md), [verified handoff](../../research/karpathy-brain-2026-10-08/HANDOFF-VERIFICATION.md), [browser playbook](../browser-agent-playbook.md), [AI workspace hub](index.md).
