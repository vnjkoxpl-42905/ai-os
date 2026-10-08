---
type: source
subject: "llm.c / dev/data/fineweb.sh"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/data/fineweb.sh

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.003583Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/fineweb.sh) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `e082f1a0fda7b994e9ad00ae0e7fdb4e9a5d11b371c269328e4d8abd510c6c01`

## What the complete source contains

Evidence: `MAX_SHARDS=1028` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/fineweb.sh)). The tokenized FineWeb downloader defaults to 1028 train shards and caps larger requested counts.

Evidence: `run_in_parallel 40` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/fineweb.sh)). It downloads one validation shard and numbered training shards from the chrisdryden Hugging Face mirror using forty parallel jobs. Curl output is saved directly without explicit checksum or HTTP-failure checks; completion messages do not prove valid downloads.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
