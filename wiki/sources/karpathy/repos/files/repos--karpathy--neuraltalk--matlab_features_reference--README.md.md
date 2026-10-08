---
type: source
subject: "GitHub source repos/karpathy/neuraltalk/matlab_features_reference/README.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/matlab_features_reference/README.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/neuraltalk/matlab_features_reference/README.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/neuraltalk/matlab_features_reference/README.md), SHA-256 `56a0000823c2814c4ecbe983a5f7a1dd85092f72594a6f85df5569577f5d45df`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "This directory contains the files I used to extract CNN features for my images. This".

Neuraltalk documentation separates feature extraction, model inference and HTML visualization, warns on distribution mismatch, and uses log probabilities as a rough confusion indicator rather than guaranteed truth. Its architecture separates dataset APIs, batching, optimizers and generator modules. The root explicitly deprecates the NumPy code in favor of GPU-batched Neuraltalk2 and restricts tested-platform claims to Ubuntu; an unresolved Python-versus-Matlab feature-reproduction issue remains visible. Matlab/Python feature reference docs point to Caffe and VGG third-party models and describe starter code rather than a ready utility. Status and checkpoint folders are operational outputs. Neuraltalk2 cross-validation tools isolate each worker GPU, give runs distinct IDs, write checkpoints to shared storage and inspect outcomes in notebooks before changing search ranges; the notebook is explicitly hacky. Documented infinite worker loops were read, not executed.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
This directory contains the files I used to extract CNN features for my images. This is not meant to be a ready-to-use utility. I just wanted to provide this code in hope that it can be useful to someone as starter code to work on top of.

- This code uses [Caffe](http://caffe.berkeleyvision.org/) and their Matlab wrapper.
- I use VGG Net which can be found in the [Model Zoo ](https://github.com/BVLC/caffe/wiki/Model-Zoo) under the title *Models used by the VGG team in ILSVRC-2014*. I use the [16-layer version](https://gist.github.com/ksimonyan/211839e770f7b538e2d8#file-readme-md).
- Note that I provide my _features deploy network def as well, which is exactly what you see on that page but I chopped off the softmax to get the 4096-D codes below.

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
