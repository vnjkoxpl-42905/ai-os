---
type: source
subject: "Karpathy video VMj-3S1tku0"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, youtube]
sources: ["../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/VMj-3S1tku0.md"]
semantic-status: bounded-semantic-review
---

# The spelled-out intro to neural networks and backpropagation: building micrograd

Original: [VMj-3S1tku0](https://www.youtube.com/watch?v=VMj-3S1tku0); channel Andrej Karpathy. Upload date 2022-08-16. Captured2026-10-08, compilation2026-10-08. Automatic English captions, not verified against audio.

[Physical raw Markdown](../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/VMj-3S1tku0.md). SHA-256: `359016a0d9045af81fc9622ad3f23fca3e65e8d15fc056a93ed20ac55043746f`. Hash matches collection manifest: **False**.

## Reviewed evidence

Karpathy begins with an executable scalar autograd engine to expose the mechanism before tensor efficiency. In the reviewed bug section, a repeated node (a+a) gives an incorrect gradient of one instead of two because assignments overwrite contributions; gradient accumulation is the proposed fix. This is pedagogical simplification, not a recommendation to deploy scalar neural networks.

> [00:06:44] the fundamental level and then you can

> [00:06:46] speed it up later okay so here's the fun

> [01:22:28] now we shouldn't be too happy with

## Coverage and interpretation

Status: **bounded-semantic-review**. Reviewed line ranges: 1-323, 2392-2491. Full file remains local and linked; hashing and indexing do not mean full semantic reading. Sections outside these ranges remain unreviewed. This page summarizes only the indicated passages.

The quoted passages support local teaching/building methods only within their stated scope. Captions contain recognition errors; quotations preserve those errors rather than silently correcting them. No linked code, papers, diagrams or media was independently executed or inspected. Source upload dates do not establish current tool capabilities.

Related: [Karpathy index](../../../karpathy/index.md), [principles](../../../karpathy/principles.md), [methods](../../../karpathy/methods.md).
