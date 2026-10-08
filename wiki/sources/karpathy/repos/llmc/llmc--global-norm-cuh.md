---
type: source
subject: "llm.c / llmc/global_norm.cuh"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: llmc/global_norm.cuh

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.235787Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/global_norm.cuh) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `24ccc138bcb15d4755bd0e37371c29c79d586883e40af5a50e917c489f0e03b9`

## What the complete source contains

Evidence: `we want to avoid using atomic add` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/global_norm.cuh)). Gradient-norm computation writes per-block squared-norm partials rather than atomically accumulating a single shared scalar.

Evidence: `out[0] ends up with the final norm squared` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/global_norm.cuh)). A separate aggregate kernel reduces partials; the launcher supports tensor slices/strides, optionally clears storage and bounds the partial count for single-block aggregation. It computes squared norm, with square root or clipping decisions expected in callers.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
