---
type: source
subject: "llm.c / dev/vislog.ipynb"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/vislog.ipynb

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.812692Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/vislog.ipynb) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `954eaf404d242383119851afa29c04655197c804201f06f2978a807e94d6a237`

## What the complete source contains

Evidence: `Simple visualizer for log files written by the training loop` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/vislog.ipynb)). The notebook parses per-step loss and evaluation logs and plots training/validation loss plus HellaSwag accuracy against stored GPT-2/3 baselines.

Evidence: `re-wind back and start re-logging older steps` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/vislog.ipynb)). Restarted step records replace earlier same-step values in per-stream dictionaries before sorting; moving-average smoothing is optional. Every captured code cell has no execution count or output, so neither plots nor baseline evaluations were reproduced.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
