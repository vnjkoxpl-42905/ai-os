---
type: source
subject: "llm.c / llmc/tokenizer.h"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: llmc/tokenizer.h

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.281116Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/tokenizer.h) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `0f578cbdb2ef7668fbae737af89d5ad876648bdd4fa6e399dfe96a9d481827b9`

## What the complete source contains

Evidence: `Only supports decoding` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/tokenizer.h)). This token-table reader supports integer-token decoding for unconditional generation, not text encoding or full prompt tokenization.

Evidence: `header[0] == 20240328` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/tokenizer.h)). It validates a binary header, supports versions one and two with different EOT handling, reads length-prefixed byte tokens, and filters unprintable single-byte tokens during output. Missing initialization yields a warning and null decoding.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
