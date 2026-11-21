---
type: source
subject: "llm.c / llmc/attention.cuh"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: llmc/attention.cuh

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:50.171163Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/attention.cuh) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `d86bcbfaa91d46c30f8e98f4fef693da038ab3ef9b1be18c446e30077808d450`

## What the complete source contains

Evidence: `fallback when we do not use the Flash Attention` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/attention.cuh)). The fallback attention implementation permutes packed QKV, calls cuBLASLt for attention matrix products, applies scaled causal online softmax and reassembles head outputs.

Evidence: `we re-use it as a scratch buffer` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/llmc/attention.cuh)). It overwrites a forward input buffer not needed for backward, retains QKV/attention state, and reverses the chain with matrix products, in-place softmax derivatives and permutation gradients. Shape and stream assumptions require runtime validation; none was performed here.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
