---
type: source
subject: What I learned from competing against a ConvNet on ImageNet
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source-compilation]
sources:
  - ../../../../raw/sources/karpathy-brain/raw/blog/md/github-blog/karpathy.github.io_2014_09_02_what-i-learned-from-competing-against-a-convnet-on-imagenet.md
semantic-status: compiled-text
---

# What I learned from competing against a ConvNet on ImageNet

Author: Andrej Karpathy. Published: 2014-09-02. Captured: 2026-10-08T09:35:25.307109Z.
Original: [What I learned from competing against a ConvNet on ImageNet](https://karpathy.github.io/2014/09/02/what-i-learned-from-competing-against-a-convnet-on-imagenet/). Complete preserved Markdown text read on 2026-10-08, including its code, tables and prose where present. This does not claim complete visual or linked-source review.

[Archived evidence](../../../../raw/sources/karpathy-brain/raw/blog/md/github-blog/karpathy.github.io_2014_09_02_what-i-learned-from-competing-against-a-convnet-on-imagenet.md). SHA-256: `afa4c4b787b869f1104379ae5f39f19e0b81547d31cc26e932ca0b5a6f85a957`.

## What this source says

Karpathy builds a labeling interface and trains himself before comparing 1500 ImageNet test images with GoogLeNet. He reports 5.1 percent personal versus 6.8 percent model error on that sample, analyzes label errors, multiple objects, small objects, filters, abstraction, fine-grained categories and class awareness. He distinguishes binary collection labels from 1000-way classification, then updates the article to reject a single universal human-performance number.

Short exact evidence from the [archived text](../../../../raw/sources/karpathy-brain/raw/blog/md/github-blog/karpathy.github.io_2014_09_02_what-i-learned-from-competing-against-a-convnet-on-imagenet.md):

> Human accuracy is not a point. It lives on a tradeoff curve.

## Interpretation and limits

Audit task definition, label quality and concrete failure types; effort, training and expertise condition a human baseline. This is an attributed small trained-annotator study, not universal human accuracy or current model performance. The reported statistical analysis was not rerun. His suggested 2 to 3 percent expert bounds are hypotheses, not observed results. Figures and linked interface were not separately inspected. The companion HTML is a format counterpart, not an independent supporting article. Statements are attributed to the captured source; no changing external capability was verified live in this compilation.

Related: [Karpathy collection](../../../karpathy/index.md) and [blog synthesis](../../../../research/karpathy-brain-2026-10-08/blog-synthesis.md).
