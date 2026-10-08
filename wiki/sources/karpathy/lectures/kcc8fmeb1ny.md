---
type: source
subject: "Karpathy video kCc8FmEb1nY"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, youtube]
sources: ["../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/kCc8FmEb1nY.md"]
semantic-status: complete-preserved-text-no-media-review
---

# Let's build GPT: from scratch, in code, spelled out.

Original: [kCc8FmEb1nY](https://www.youtube.com/watch?v=kCc8FmEb1nY); channel Andrej Karpathy. Upload date 2023-01-17. Captured2026-10-08, compilation2026-10-08. Automatic English captions, not verified against audio.

[Physical raw Markdown](../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/kCc8FmEb1nY.md). SHA-256: `0d26bcdd852a0db6043d5cbde19842113565b26ce70b853e0d252ee6c0f21ae5`. Physical byte hash differs from the older manifest. CRLF-to-LF normalized SHA-256 matches its hash `c675d4d399318ad8d176758af9ab2442b2df3e22796b472ec29df93d069a08ec` exactly. Raw bytes were preserved; normalized matching does not make the physical byte hashes identical.

## Reviewed evidence

He bounds the project to a small character-level Transformer, distinguishing it from reproducing the complete production ChatGPT system. The small Shakespeare text and simple character tokenizer make the training mechanism inspectable.

> [00:02:52] the context of machine translation in

He withholds a validation split to distinguish generalization from memorizing training text. Short chunks contain multiple next-character examples, and batches process independent sequences for efficiency.

> [00:13:24] here so I believe for example that zero

He predicts a uniform-vocabulary baseline loss, diagnoses why randomly initialized predictions differ, then tests generation and optimization in a bigram model before adding context communication.

> [00:28:12] loss is

The prototype becomes a script with averaged train/validation measurements, explicit train/evaluation modes, and no-grad evaluation. He explains why these practices matter even before this particular model contains mode-dependent layers.

> [00:40:26] loss we're we're going to report the uh

He first implements causal prefix averaging with explicit loops. A triangular matrix implementation is then checked for equality against that reference before using softmax masks and learned attention.

> [00:45:15] like um a term that people use when you

Queries, keys and values are introduced as data-dependent information requests, matching content and communicated values. Causal masking prevents future information from leaking into next-token predictions.

> [01:03:18] single row has these um uniform numbers

He distinguishes positional information, independent batch examples, self-attention and cross-attention. Encoder connectivity can be bidirectional, whereas this autoregressive decoder requires causal masking.

> [01:12:38] of scenario like language modeling but

Scaled dot-product attention controls score variance so initialization does not prematurely sharpen softmax into near one-hot selections. He connects the scaling to a concrete numerical experiment.

> [01:17:03] query key and value we've U multiplied

He iteratively adds multiple heads, per-token feed-forward computation and repeated blocks, reporting validation results along the way. Deeper blocks introduce optimization difficulties that motivate residual paths and normalization.

> [01:23:40] self

Layer normalization acts within each example rather than across the batch and therefore needs no running batch statistics. The implemented pre-normalization arrangement is explicitly identified as a departure from the original paper.

> [01:34:00] every single column of this uh input now

He scales context, depth and embedding size and adds dropout, then reports better validation loss and more structurally recognizable but still nonsensical Shakespeare output. These are this demonstrated run's results and hardware assumptions.

> [01:39:54] uh I brought down the learning rate a

He compares the teaching implementation with nanoGPT: batching heads, checkpoint/loading infrastructure and compatibility details add efficiency and usability while preserving the explained mathematical structure.

> [01:47:41] inside a single causal self attention

He separates pretraining as document completion from later assistant alignment. Supervised examples, preference ranking, a reward model and reinforcement learning describe the dated ChatGPT explanation; the lesson implements the pretraining stage only.

> [01:51:27] other to train models of this size so

## Coverage and interpretation

Status: **complete-preserved-text-no-media-review**. Reviewed line ranges: 1-3064 sequentially in bounded chunks. All preserved caption text was read. Original audio/video, code and missing speech were not independently reviewed.

The quoted passages support local teaching/building methods only within their stated scope. Captions contain recognition errors; quotations preserve those errors rather than silently correcting them. No linked code, papers, diagrams or media was independently executed or inspected. Source upload dates do not establish current tool capabilities.

Related: [Karpathy index](../../../karpathy/index.md), [principles](../../../karpathy/principles.md), [methods](../../../karpathy/methods.md).
