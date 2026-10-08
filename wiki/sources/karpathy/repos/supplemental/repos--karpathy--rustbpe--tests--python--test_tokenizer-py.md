---
type: source
subject: "repos/karpathy/rustbpe/tests/python/test_tokenizer.py"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-preserved-text-read
---

# repos/karpathy/rustbpe/tests/python/test_tokenizer.py

Captured repository text; ownership does not establish individual authorship. Original date: 2026-01-03T21:20:46Z (created); pushed 2026-01-03T22:24:54Z. Captured: 2026-10-08T09:35:34.082313Z.

[Immutable raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/rustbpe/tests/python/test_tokenizer.py). SHA-256 `0002da26593c84f99c50c2ce643dd9b82047257d99703356a2d576cf56b10554`. Manifest hash match: True.

## Reviewed content

Four-way tokenizer comparison uses slow Python reference, incremental optimized Python, HuggingFace byte-alphabet BPE and RustBPE, then exports Rust ranks to tiktoken. Identical token-ID sequences are asserted for Python/Rust/tiktoken; HuggingFace byte-ID differences use a custom permutation comparison. Tie ambiguity is explicitly warned. Tests add batch equivalence, vocabulary size, encode/decode round trips and invalid-token rejection. Performance tests time 10MB training and parallel encoding, verify results before reporting speedup and warn below 1.5x. Static review of test definitions, not benchmark execution or proof of passing results.

> assert tiktoken_ids == rustbpe_ids, "Tiktoken should match RustBPE"

## Limits

Complete preserved text read, lines 1-743. No captured code executed or linked sources inspected. Static source review does not establish current correctness, performance or compatibility.
