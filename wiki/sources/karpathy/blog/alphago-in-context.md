---
type: source
subject: AlphaGo, in context
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source-compilation]
sources:
  - ../../../../raw/sources/karpathy-brain/raw/blog/md/medium/karpathy.medium.com_alphago-in-context-c47718cb95a5.md
semantic-status: compiled-text
---

# AlphaGo, in context

Author: Andrej Karpathy. Published: Wed, 31 May 2017 20:41:38 GMT. Captured: 2026-10-08T09:36:44.615987Z.
Original: [AlphaGo, in context](https://karpathy.medium.com/alphago-in-context-c47718cb95a5). Complete preserved Markdown text read on 2026-10-08, including its code, tables and prose where present. This does not claim complete visual or linked-source review.

[Archived evidence](../../../../raw/sources/karpathy-brain/raw/blog/md/medium/karpathy.medium.com_alphago-in-context-c47718cb95a5.md). SHA-256: `06d1e70280d6c872eeefbe385839942be191f9da0a4ef7030b6731e82a4842cd`.

## What this source says

Karpathy explains the combination of supervised policy initialization, reinforcement learning, value estimation and Monte Carlo tree search, while cautioning that the resulting agent is narrow. He lists favorable Go properties: deterministic, fully observed, discrete actions, a perfect simulator, short episodes, cheap repeated evaluation and abundant demonstrations. He contrasts robotics, where many assumptions fail. An update explicitly distinguishes the discussed earlier AlphaGo from later AlphaGo Zero.

Short exact evidence from the [archived text](../../../../raw/sources/karpathy-brain/raw/blog/md/medium/karpathy.medium.com_alphago-in-context-c47718cb95a5.md):

> perfect **simulator**

## Interpretation and limits

Check the evaluation environment and transfer assumptions before generalizing a benchmark win to real-world autonomy. This directly supports Verifiability's later emphasis on resettable inexpensive feedback. Algorithm descriptions and projections are attributed 2017 context, not current capability judgments. Linked papers and figures were not separately reviewed. The companion HTML is a format counterpart, not an independent supporting article. Statements are attributed to the captured source; no changing external capability was verified live in this compilation.

Related: [Karpathy collection](../../../karpathy/index.md) and [blog synthesis](../../../../research/karpathy-brain-2026-10-08/blog-synthesis.md).
