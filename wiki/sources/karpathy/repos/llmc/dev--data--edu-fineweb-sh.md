---
type: source
subject: "llm.c / dev/data/edu_fineweb.sh"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/data/edu_fineweb.sh

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.992495Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/edu_fineweb.sh) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `efe37963e7f94420252a37808f7b3d7f89110a8bd002285575b9120dade609db`

## What the complete source contains

Evidence: `MAX_SHARDS=1001` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/edu_fineweb.sh)). The FineWeb-EDU downloader defaults to 1001 shards and caps larger counts.

Evidence: `run_in_parallel 40` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/edu_fineweb.sh)). It downloads tokenized shards from the karpathy Hugging Face dataset with forty concurrent jobs and a separate validation shard. Saved downloads are not hash-validated in this file.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
