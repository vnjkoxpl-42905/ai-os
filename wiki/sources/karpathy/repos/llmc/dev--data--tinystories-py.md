---
type: source
subject: "llm.c / dev/data/tinystories.py"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/data/tinystories.py

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.035108Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/tinystories.py) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `8fa7f7b6aa2faef9d3e46e08a240a08f56e5117d9bcd65916388826b184006e3`

## What the complete source contains

Evidence: `shard 0 will be the val split` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/tinystories.py)). TinyStories preprocessing reserves the first sorted JSON shard for validation and uses all others for training.

Evidence: `for future in as_completed(futures)` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/tinystories.py)). Each shard is shuffled with a seed based on its submitted index and tokenized in a process pool, then outputs are concatenated in completion order. Per-shard seeds therefore do not guarantee deterministic final ordering across workers. It supports GPT-2 and Llama tokenization and relies on an external tar extraction command.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
