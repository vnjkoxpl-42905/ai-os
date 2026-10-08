---
type: source
subject: Visualizing Top Tweeps with t-SNE in Javascript
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source-compilation]
sources:
  - ../../../../raw/sources/karpathy-brain/raw/blog/md/github-blog/karpathy.github.io_2014_07_02_visualizing-top-tweeps-with-t-sne-in-Javascript.md
semantic-status: compiled-text
---

# Visualizing Top Tweeps with t-SNE in Javascript

Author: Andrej Karpathy. Published: 2014-07-02. Captured: 2026-10-08T09:35:31.717446Z.
Original: [Visualizing Top Tweeps with t-SNE in Javascript](https://karpathy.github.io/2014/07/02/visualizing-top-tweeps-with-t-sne-in-Javascript/). Complete preserved Markdown text read on 2026-10-08, including its code, tables and prose where present. This does not claim complete visual or linked-source review.

[Archived evidence](../../../../raw/sources/karpathy-brain/raw/blog/md/github-blog/karpathy.github.io_2014_07_02_visualizing-top-tweeps-with-t-sne-in-Javascript.md). SHA-256: `23fd144d7942d94ff2ba2c453c497096695f2225b94455f8d39f48747fa1522f`.

## What this source says

Karpathy describes a one-day project: identify popular accounts, collect their tweets into UTF-8 files while respecting rate limits, create TF-IDF vectors, convert similarities to JSON and animate a JavaScript t-SNE visualization using D3. He reimplements t-SNE to learn it, explains its emphasis on local neighbors and checks analytic against numerical gradients. A second demo visualizes word embeddings.

Short exact evidence from the [archived text](../../../../raw/sources/karpathy-brain/raw/blog/md/github-blog/karpathy.github.io_2014_07_02_visualizing-top-tweeps-with-t-sne-in-Javascript.md):

> double checked with `debugGrad()` gradient check

## Interpretation and limits

Understand by implementing, preserve intermediate artifacts and check a core numerical primitive against an independent calculation before trusting the visualization. The old scraping services/API and sampled account list were not reproduced or verified live. A two-dimensional embedding is an exploratory view, not proof of global distances or causal relationships. Figures were not inspected. The companion HTML is a format counterpart, not an independent supporting article. Statements are attributed to the captured source; no changing external capability was verified live in this compilation.

Related: [Karpathy collection](../../../karpathy/index.md) and [blog synthesis](../../../../research/karpathy-brain-2026-10-08/blog-synthesis.md).
