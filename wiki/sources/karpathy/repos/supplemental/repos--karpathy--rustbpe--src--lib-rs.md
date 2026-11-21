---
type: source
subject: "repos/karpathy/rustbpe/src/lib.rs"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-preserved-text-read
---

# repos/karpathy/rustbpe/src/lib.rs

Captured repository text; ownership does not establish individual authorship. Original date: 2026-01-03T21:20:46Z (created); pushed 2026-01-03T22:24:54Z. Captured: 2026-10-08T09:35:34.077372Z.

[Immutable raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/rustbpe/src/lib.rs). SHA-256 `2b6bdae64ab82cf7c6731766bb94d2feecb27cacddae8d37ef6c94b4f0f3b450`. Manifest hash match: True.

## Reviewed content

Rust/PyO3 byte-pair tokenizer: regex pretokenization, parallel weighted chunk/pair counting, incremental heap and local pair-count deltas, deterministic merge ordering, streamed Python iterator refill, GIL release for Rust work, mergeable ranks and batched encoding. Decode rejects unknown tokens and invalid UTF-8; encoding logs regex errors and skips those chunks. Tests cover overlapping/nonoverlapping merges, chained ordering, byte reconstruction, round trips, empty inputs, count deltas and zero counts. Static review only; test declarations are not execution evidence.

> log::warn!("Regex match error, skipping chunk: {}", e);

## Limits

Complete preserved text read, lines 1-1070. No captured code executed or linked sources inspected. Static source review does not establish current correctness, performance or compatibility.
