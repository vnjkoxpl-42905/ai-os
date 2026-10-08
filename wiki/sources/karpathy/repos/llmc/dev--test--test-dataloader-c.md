---
type: source
subject: "llm.c / dev/test/test_dataloader.c"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/test/test_dataloader.c

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.094969Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/test/test_dataloader.c) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `c6e0547b6ca66f34960d14be94282b5f214457aefdc95fa397d944724a60d5d2`

## What the complete source contains

Evidence: `test load/save state of DataLoader` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/test/test_dataloader.c)). The standalone suite generates four sequential-token binary shards and checks shifted targets, shard cycling, rank-partitioned batches and token occurrence counts over four epochs. State save/resume coverage remains a TODO.

Evidence: `int should_shuffle = 0;` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/test/test_dataloader.c)). The routine named multiprocess_shuffled actually sets shuffle false, while the single-process shuffled case enables it. Multiprocess operation is simulated serially rather than launched concurrently. Check helpers terminate on mismatch; generated shard files would be removed by the program, which was not executed.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
