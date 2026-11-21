---
type: source
subject: "llm.c / dev/eval/run_eval.sh"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/eval/run_eval.sh

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.055738Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/eval/run_eval.sh) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `47d2448fc11c201cefb0aa90acac7c29d9f402f96fb1697a13cddec022dfdd1e`

## What the complete source contains

Evidence: `git checkout b281b0921b636bc36ad05c0b0b0763bd6dd43463` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/eval/run_eval.sh)). The evaluation recipe names a pinned harness revision and requests two arguments: a model path/name and a result-folder name.

Evidence: `--tasks truthfulqa_mc` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/eval/run_eval.sh)). It launches TruthfulQA, Winogrande, ARC Challenge, HellaSwag, GSM8K and the listed MMLU subjects with task-specific few-shot counts, then invokes the summary script. It converts the model argument with realpath; compatibility with remote names and current harness versions is not established.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
