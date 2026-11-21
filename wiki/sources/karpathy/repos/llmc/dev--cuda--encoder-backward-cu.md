---
type: source
subject: "llm.c / dev/cuda/encoder_backward.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cuda/encoder_backward.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.880540Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/encoder_backward.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `4ef9806989d911fccce2631cb9420b786a86b355283d7f743a9fb16ee957c033`

## What the complete source contains

Evidence: `uses atomics to add to dwte, dwpe` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/encoder_backward.cu)). The first backward experiment parallelizes embedding-gradient updates across batch/time/channel elements with atomic accumulation.

Evidence: `gets rid of atomics` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/encoder_backward.cu)). The second assigns channels to threads and loops across batch/time serially, exposing a different parallelism tradeoff. A CPU reference, zeroed output buffers and six block-size comparisons precede timing; comments calling it forward are inconsistent with the backward code.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
