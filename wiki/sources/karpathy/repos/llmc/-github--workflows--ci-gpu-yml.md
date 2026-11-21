---
type: source
subject: "llm.c / .github/workflows/ci_gpu.yml"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: .github/workflows/ci_gpu.yml

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.783657Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/.github/workflows/ci_gpu.yml) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `80819f7f92260c8b024bf401473ef86d87554ec21445bd72f15369c3a0dfc18e`

## What the complete source contains

Evidence: `runs-on: ubicloud-gpu-standard-1-latest` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/.github/workflows/ci_gpu.yml)). The GPU workflow defines hosted GPU build/test jobs after Tiny Shakespeare preprocessing and Python reference generation.

Evidence: `Run no master weights` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/.github/workflows/ci_gpu.yml)). Its matrix-like steps exercise FP32/BF16, recomputation settings, optional master weights, OpenMP and cuDNN variants, as well as loss comparisons and device/file IO. Workflow configuration is test intent, not retrieved CI run evidence.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
