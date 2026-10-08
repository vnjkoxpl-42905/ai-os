---
type: source
subject: "Karpathy video P6sfmUTpUmc"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, youtube]
sources: ["../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/P6sfmUTpUmc.md"]
semantic-status: bounded-semantic-review
---

# Building makemore Part 3: Activations & Gradients, BatchNorm

Original: [P6sfmUTpUmc](https://www.youtube.com/watch?v=P6sfmUTpUmc); channel Andrej Karpathy. Upload date 2022-10-04. Captured2026-10-08, compilation2026-10-08. Automatic English captions, not verified against audio.

[Physical raw Markdown](../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/P6sfmUTpUmc.md). SHA-256: `2e2eff587c196512efd3abe51827628c9fbe7a9e6e72912b5b63939d30b7954c`. Physical byte hash differs from the older manifest. CRLF-to-LF normalized SHA-256 matches its hash `b1eb0438a0d9ef27f6ba98e2c1b57bdfe93aa080505f126bbb5b761120738302` exactly. Raw bytes were preserved; normalized matching does not make the physical byte hashes identical.

## Reviewed evidence

The reviewed introduction deliberately pauses architectural expansion to understand activations and backward gradients intuitively. It motivates that pause by trainability problems in expressive recurrent architectures, then describes refactoring magic numbers without functional changes. Later diagnostic plots and normalization implementation remain unreviewed.

> [00:00:32] this because I would like us to have a

> [00:00:33] very good intuitive understanding of the

## Coverage and interpretation

Status: **bounded-semantic-review**. Reviewed line ranges: 1-147. Full file remains local and linked; hashing and indexing do not mean full semantic reading. Sections outside these ranges remain unreviewed. This page summarizes only the indicated passages.

The quoted passages support local teaching/building methods only within their stated scope. Captions contain recognition errors; quotations preserve those errors rather than silently correcting them. No linked code, papers, diagrams or media was independently executed or inspected. Source upload dates do not establish current tool capabilities.

Related: [Karpathy index](../../../karpathy/index.md), [principles](../../../karpathy/principles.md), [methods](../../../karpathy/methods.md).
