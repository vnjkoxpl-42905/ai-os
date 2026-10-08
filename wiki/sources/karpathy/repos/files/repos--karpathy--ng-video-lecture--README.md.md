---
type: source
subject: "GitHub source repos/karpathy/ng-video-lecture/README.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/ng-video-lecture/README.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/ng-video-lecture/README.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/ng-video-lecture/README.md), SHA-256 `427c41751495aa0cfff5fd6a13e2b9e803f3dbd3b194456088e40e7ca8a1395a`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "# nanogpt-lecture Code created in the \\[Neural Networks: Zero To Hero\\](https://karpathy.ai/zero-to-hero.html) video lecture series, specifically".

Neuraltalk2 documents captioning, pretrained evaluation, data preprocessing, staged CNN finetuning and visualization, with explicit beam-search speed/quality tradeoffs and a known corrupt input-image failure. Its 2016 update recommends Google im2txt and preserves this as educational Torch code; projected leaderboard placement and speed are dated reports. Ng-video-lecture keeps lecture-identical code while acknowledging missing initialization treatment and slower convergence, and warns a differently named successor implementation cannot simply be pasted in. Nipspreview breaks PDF and metadata acquisition into thumbnail, word-cloud, topic-model and abstract stages and admits malformed-paper extraction needs human intervention; its LDA implementation is credited externally. Zero-to-Hero sequences scalar autograd, bigrams, MLP, activation/gradient diagnostics, manual backpropagation, hierarchical CNNs, GPT and tokenization; the backprop lesson asks learners to work the exercise and unpause only when stuck, rather than merely watch. Notpygamejs abstracts game/event boilerplate while admitting globals; paper-notes README is an informal placeholder.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text

# nanogpt-lecture

Code created in the [Neural Networks: Zero To Hero](https://karpathy.ai/zero-to-hero.html) video lecture series, specifically on the first lecture on nanoGPT. Publishing here as a Github repo so people can easily hack it, walk through the `git log` history of it, etc.

NOTE: sadly I did not go too much into model initialization in the video lecture, but it is quite important for good performance. The current code will train and work fine, but its convergence is slower because it starts off in a not great spot in the weight space. Please see [nanoGPT model.py](https://github.com/karpathy/nanoGPT/blob/master/model.py) for `# init all weights` comment, and especially how it calls the `_init_weights` function. Even more sadly, the code in this repo is a bit different in how it names and stores the various modules, so it's not possible to directly copy paste this code here. My current plan is to publish a supplementary video lecture and cover these parts, then I will also push the exact code changes to this repo. For now I'm keeping it as is so it is almost exactly what we actually covered in the video.

### License

MIT

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
