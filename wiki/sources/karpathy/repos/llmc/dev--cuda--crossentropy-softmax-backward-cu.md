---
type: source
subject: "llm.c / dev/cuda/crossentropy_softmax_backward.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cuda/crossentropy_softmax_backward.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.874051Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/crossentropy_softmax_backward.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `b1825fd7b498f28851df5c5bbf380877b32a1ca627234278c627974981e5a660`

## What the complete source contains

Evidence: `backwards through both softmax and crossentropy` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/crossentropy_softmax_backward.cu)). The CPU reference and GPU kernel add probability-minus-target-indicator gradients scaled by per-position loss derivatives, parallel over batch/time/vocabulary in CUDA.

Evidence: `cudaMemset(d_dlogits, 0` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/crossentropy_softmax_backward.cu)). The harness zeroes accumulated GPU gradients before each correctness comparison, then benchmarks the chosen kernel across block sizes. The introductory forward-pass wording is stale relative to this backward implementation; no tests were executed.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
