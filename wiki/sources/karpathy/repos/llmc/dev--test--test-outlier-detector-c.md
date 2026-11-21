---
type: source
subject: "llm.c / dev/test/test_outlier_detector.c"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/test/test_outlier_detector.c

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.100982Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/test/test_outlier_detector.c) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `1c0f7760e0ad95c159f8cde91e9a03c910178c2ae58262437f552d271b91ae24`

## What the complete source contains

Evidence: `Expected nan` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/test/test_outlier_detector.c)). The test checks the warmup window emits NaN and later seeded random values have bounded z-scores.

Evidence: `double outlier = 10.0;` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/test/test_outlier_detector.c)). It injects a spike of ten and expects a score of at least five, exiting on violations. This is source-defined test intent, not a recorded passing run.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
