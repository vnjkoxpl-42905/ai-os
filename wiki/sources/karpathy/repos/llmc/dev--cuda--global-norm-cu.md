---
type: source
subject: "llm.c / dev/cuda/global_norm.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cuda/global_norm.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.909198Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/global_norm.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `a5363d5b09865a047320684fa15d39558b6566518f748f2bd5d4d3b44e182ead`

## What the complete source contains

Evidence: `accumulate in double` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/global_norm.cu)). The CPU reference sums squares in double precision. Four GPU variants compare block or warp atomic accumulation with a two-kernel partial-sum reduction; the output is the squared norm rather than its square root.

Evidence: `grid_size < 1024` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/global_norm.cu)). The non-atomic variant uses a single final block and explicitly constrains partial count. Seeded BF16 inputs are compared over seven block sizes before repeated timing. Determinism and speed comments describe source intent, not reproduced hardware results.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
