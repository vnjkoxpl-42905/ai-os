---
type: source
subject: "llm.c / dev/eval/summarize_eval.py"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/eval/summarize_eval.py

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.062434Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/eval/summarize_eval.py) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `2820b787be482a2049e0df10ad233e8a729308903fd5dbab26b7932feb49920a`

## What the complete source contains

Evidence: `average = total / 6.0` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/eval/summarize_eval.py)). This optional script reads six evaluation JSON files, averages each task-family score across result entries and prints their unweighted mean.

Evidence: `"truthfulqa_0shot.json": "mc2"` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/eval/summarize_eval.py)). Metrics differ by task: normalized accuracy for ARC and HellaSwag, accuracy for GSM8K/MMLU/Winogrande, and mc2 for TruthfulQA. It reports existing results rather than generating predictions.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
