---
type: source
subject: "llm.c / dev/data/hellaswag.py"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/data/hellaswag.py

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.010121Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/hellaswag.py) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `c8412c9402419791e3af48e4de5d2d058e8296326eef44d3fcd23ca92e82b43e`

## What the complete source contains

Evidence: `Also writes the data (tokens, labels) to .bin files` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/hellaswag.py)). HellaSwag reference evaluation also exports tokenized validation examples through the common binary format for C evaluation.

Evidence: `pred_norm = avg_loss.argmin().item()` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/hellaswag.py)). It tokenizes four context-completion candidates, scores shifted next-token losses only in masked completion regions, and reports summed-loss and mean-loss accuracy. The docstring explicitly distinguishes completion-style results from harness multiple-choice results; those figures were not regenerated.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
