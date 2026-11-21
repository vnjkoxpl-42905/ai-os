---
type: source
subject: "llm.c / profile_gpt2.cu"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: profile_gpt2.cu

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.699844Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/profile_gpt2.cu) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `c7dfee21c237a8de1581db34efd018a7a92e385876e532435b2dec597ee5ad63`

## What the complete source contains

Evidence: `only profile once` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/profile_gpt2.cu)). This profiling harness reduces a loaded GPT-2 checkpoint to one repeating layer before a synthetic training step.

Evidence: `finish all CUDA work to get correct precise timings` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/profile_gpt2.cu)). It synchronizes device work after forward, backward, gradient norm and update; the introductory instructions describe Nsight Compute collection and viewing. Input data are synthetic token IDs, not an evaluation dataset.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
