---
type: source
subject: "llm.c / dev/data/mmlu.py"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/data/mmlu.py

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.014780Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/mmlu.py) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `977586f5585e727eb9347c865a10a5d3cf62c827db50f2df65ad7c7852e05ffe`

## What the complete source contains

Evidence: `mask (is 1 in the region of the candidate completion` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/mmlu.py)). The MMLU reference renderer produces four padded candidate sequences and masks only their answer regions; answers are formatted after a Question/Answer prompt.

Evidence: `pred_norm = avg_loss.argmin().item()` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/mmlu.py)). GPT-2 checkpoint evaluation compares both total and length-normalized autoregressive completion losses to choose predictions, then reports cumulative accuracy. It downloads CSV tests from the Hendrycks archive; docstring results are captured claims, not reproduced evaluations.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
