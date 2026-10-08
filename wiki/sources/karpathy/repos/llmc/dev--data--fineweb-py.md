---
type: source
subject: "llm.c / dev/data/fineweb.py"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/data/fineweb.py

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.998554Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/fineweb.py) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `02280d6a851e2bb128f2a448ed12e363fd91914799186ce23a511497643fb427`

## What the complete source contains

Evidence: `nprocs = max(1, os.cpu_count() - 2)` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/fineweb.py)). FineWeb preprocessing leaves two logical processors unused when choosing a worker pool, and processes documents with ordered imap.

Evidence: `split = "val" if shard_index == 0 else "train"` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/data/fineweb.py)). Classic or educational 10B/100B samples are tokenized into GPT-2 uint16 or Llama uint32 shards, with end-of-text document delimiters. It fills fixed-size buffers, carries split-document remnants forward and assigns the first shard to validation. Historical runtime estimates in the docstring are not local measurements.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
