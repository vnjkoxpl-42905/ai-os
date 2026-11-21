---
type: source
subject: "llm.c / llmc/dataloader.h"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: llmc/dataloader.h

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.208061Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/dataloader.h) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `66ff78fec30531d6f5e7220935ca81639933c4c1eff38f693c8f9627d4d6550a`

## What the complete source contains

Evidence: `inspect and validate all shards` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/dataloader.h)). The training loader validates shard magic/version, byte length and minimum batch capacity before serving shifted input/target token pairs, with per-rank batch offsets, optional shard/sample permutations and resume positions.

Evidence: `ASSUMED_NUM_COMPLETIONS 4` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/dataloader.h)). The evaluation loader divides examples among processes, reads variable-length binary records, packs four candidates per example, aligns next-token targets and masks only completion losses. It picks the lowest mean masked loss for correctness statistics and handles inactive final-batch rows. Captured token storage is GPT-2 uint16; other formats require a different compatible reader.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
