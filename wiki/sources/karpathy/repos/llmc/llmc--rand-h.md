---
type: source
subject: "llm.c / llmc/rand.h"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: llmc/rand.h

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.268068Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/rand.h) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `5319491c12f5dfa2b8b33ea8abac64ee2161c5ddda430fe765c813ac482ad73b`

## What the complete source contains

Evidence: `Copyright(c) Makoto Matsumoto and Takuji Nishimura` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/rand.h)). The random header credits the Mersenne Twister authors and states its implementation follows PyTorch for verification parity; it must not be treated as exclusively Karpathy-authored.

Evidence: `Box-Muller transform` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/rand.h)). It implements seed/state advancement, integer and floating draws, uniform filling, size-dependent Gaussian filling and permutation helpers. Its demonstration output claims PyTorch numerical parity, but no comparison was executed in this compilation.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
