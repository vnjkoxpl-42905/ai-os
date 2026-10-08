---
type: source
subject: "llm.c / dev/loss_checker_ci.py"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/loss_checker_ci.py

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.799719Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/loss_checker_ci.py) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `a8d3c422ed3b16eb2ebdb590e71ca5e4a9da5d4316b5ba0690a77a407189aa95`

## What the complete source contains

Evidence: `step    1/10` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/loss_checker_ci.py)). The checker locates a fixed textual step marker and reads up to ten following rows from caller-selected character columns.

Evidence: `abs(percent_difference) > percent_accuracy` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/loss_checker_ci.py)). It compares values with a ten-loss reference and fails on excessive relative difference or read error. It does not explicitly require exactly ten extracted values; a short matching tail could pass without all expected steps.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
