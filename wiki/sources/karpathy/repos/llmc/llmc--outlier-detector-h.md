---
type: source
subject: "llm.c / llmc/outlier_detector.h"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: llmc/outlier_detector.h

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.263079Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/outlier_detector.h) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `5c0a71a5f3e6bda91e11ec227423633dda3f4ad21d2b98ce0a0293d0b51996f0`

## What the complete source contains

Evidence: `#define OUTLIER_DETECTOR_WINDOW_SIZE 128` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/outlier_detector.h)). A fixed 128-observation ring buffer tracks double-precision sums and squares for loss or gradient-norm monitoring.

Evidence: `return nan("");` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/outlier_detector.h)). The initial filling phase reports no score. Once full, it removes the oldest observation, inserts the new one, and computes its z-score against the updated window including that new value; zero standard deviation returns zero.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
