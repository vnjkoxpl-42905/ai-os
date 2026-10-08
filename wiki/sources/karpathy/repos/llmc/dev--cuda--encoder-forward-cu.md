---
type: source
subject: "llm.c / dev/cuda/encoder_forward.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cuda/encoder_forward.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.885688Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/encoder_forward.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `cfa029e2005618cc499cc8cc280199b1778b26d29fed382e2e35f1dc5649beb9`

## What the complete source contains

Evidence: `parallelizes over B,T, loops over C` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/encoder_forward.cu)). Three experimental embedding-sum kernels progressively move from per-position channel loops to per-element parallelism and packed vector memory operations.

Evidence: `validate_result(d_out, out` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/encoder_forward.cu)). The CPU reference checks selected variants across block sizes with precision-specific tolerances, then the harness times repeats and estimates bandwidth. Packed BF16 implementation details supersede the introductory float4 wording; no results were produced here.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
