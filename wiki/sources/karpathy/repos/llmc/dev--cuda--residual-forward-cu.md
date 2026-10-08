---
type: source
subject: "llm.c / dev/cuda/residual_forward.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cuda/residual_forward.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.968015Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/residual_forward.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `9e55dc9854a546147974e1fb9db8c1a39f43bf39c4c60f5e049ad903c6111073`

## What the complete source contains

Evidence: `version 2 packs input into 128 bit memory reads` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/residual_forward.cu)). The residual-sum benchmark compares elementwise scalar and packed BF16 addition with a CPU reference.

Evidence: `All results match. Starting benchmarks.` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/residual_forward.cu)). The source checks six block sizes before repeated timing and a rough bandwidth calculation. This is harness control flow, not an observed successful benchmark; packed operations assume suitably aligned/compatible shapes.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
