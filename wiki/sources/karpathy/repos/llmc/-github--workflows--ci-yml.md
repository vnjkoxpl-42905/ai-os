---
type: source
subject: "llm.c / .github/workflows/ci.yml"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: .github/workflows/ci.yml

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.774351Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/.github/workflows/ci.yml) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `e5859af89047b23d299c1a71f650ebc082c2fe04a0d00f99f7193942c8bb6133`

## What the complete source contains

Evidence: `os: [ubuntu-latest, macos-latest, windows-latest]` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/.github/workflows/ci.yml)). The main CI file defines CPU build/test jobs across Linux, macOS and Windows with platform-specific OpenMP and compiler handling.

Evidence: `PRECISION=FP16` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/.github/workflows/ci.yml)). Separate jobs compile CUDA FP32, BF16, FP16, standalone kernels, Windows CUDA and an older Ubuntu/CUDA combination. Build-only jobs are distinct from runtime tests; no execution status is established by this YAML.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
