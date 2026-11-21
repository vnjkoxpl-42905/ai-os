---
type: source
subject: "llm.c / llmc/fused_classifier.cuh"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: llmc/fused_classifier.cuh

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.221630Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/fused_classifier.cuh) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `64e591d812bc530b5bdba07eb6baa6c8ffaab4d3150276f6e5e58dc5ccc609f9`

## What the complete source contains

Evidence: `Never materializes the full normalized logits` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/fused_classifier.cuh)). The fused classifier computes cross-entropy and, when selected, writes logit gradients directly, avoiding a full probability tensor during training.

Evidence: `without this synchronization point we have a race condition` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/fused_classifier.cuh)). A block barrier separates target-loss computation from in-place logit replacement. Online stabilized softmax, padded versus actual vocabulary handling, packed reads and optional probability output are part of the implementation; no local numerical validation occurred.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
