---
type: source
subject: microgpt
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source-compilation]
sources:
  - ../../../../raw/sources/karpathy-brain/raw/blog/md/github-blog/karpathy.github.io_2026_02_12_microgpt.md
semantic-status: compiled-text
---

# microgpt

Author: Andrej Karpathy. Published: 2026-02-12. Captured: 2026-10-08T09:34:52.019287Z.
Original: [microgpt](https://karpathy.github.io/2026/02/12/microgpt/). Complete preserved Markdown text read on 2026-10-08, including its code, tables and prose where present. This does not claim complete visual or linked-source review.

[Archived evidence](../../../../raw/sources/karpathy-brain/raw/blog/md/github-blog/karpathy.github.io_2026_02_12_microgpt.md). SHA-256: `dfc1f1c2f8bf71dcdde157cd24feecfd435de218320dfafb3471fbf52493256f`.

## What this source says

Karpathy walks through a dependency-free Python GPT teaching implementation: a name dataset, character tokenizer with a boundary token, scalar automatic differentiation, token/position embeddings, attention and MLP blocks, Adam updates, cross-entropy training and autoregressive sampling. The autograd explanation explicitly sums contributions when values branch. A progression adds count tables, manual gradients, autograd, attention, multiple heads/layers and Adam one component at a time. The final sections distinguish the toy algorithmic core from production data, tensor computation, architectural variants, distributed training, post-training and serving.

Short exact evidence from the [archived text](../../../../raw/sources/karpathy-brain/raw/blog/md/github-blog/karpathy.github.io_2026_02_12_microgpt.md):

> Everything else is just efficiency.

## Interpretation and limits

Build a runnable minimal mechanism first, explain the data-to-loss-to-update loop and add complexity progressively. The small model is educational, not a production chatbot or factual database. Runtime, size and frontier-model estimates are author claims; no code was executed here. The triptych image was not inspected. The companion HTML is a format counterpart, not an independent supporting article. Statements are attributed to the captured source; no changing external capability was verified live in this compilation.

Related: [Karpathy collection](../../../karpathy/index.md) and [blog synthesis](../../../../research/karpathy-brain-2026-10-08/blog-synthesis.md).
