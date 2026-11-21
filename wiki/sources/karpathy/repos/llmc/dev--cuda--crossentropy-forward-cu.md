---
type: source
subject: "llm.c / dev/cuda/crossentropy_forward.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cuda/crossentropy_forward.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.868312Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/crossentropy_forward.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `bd2f6db35e07170173faa00b76d543709dcc9eca90b30c978bb98b242dfe4867`

## What the complete source contains

Evidence: `loss = -log(probs[target])` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/crossentropy_forward.cu)). The benchmark implements target-probability negative log loss in both CPU reference and a CUDA kernel parallel over batch/time positions.

Evidence: `All results match. Starting benchmarks.` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/crossentropy_forward.cu)). Its harness is structured to compare selected kernels at six block sizes before timing repeated launches and reporting per-token latency. The message is program text, not evidence that a benchmark ran or passed.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
