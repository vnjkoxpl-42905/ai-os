---
type: source
subject: "GitHub source repos/karpathy/deep-vector-quantization/README.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/deep-vector-quantization/README.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/deep-vector-quantization/README.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/deep-vector-quantization/README.md), SHA-256 `604cb9a8791c585cb14d338b967d81d29c44bd0b3f1f529a33aba0083deeedd6`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "# deep vector quantization Implements training code for VQVAE's, i.e. autoencoders with categorical latent variable".

Cryptos presents a zero-dependency educational Bitcoin implementation and compares SHA-256 with a reference tool; it explicitly restricts use to education and distinguishes partial transaction/header verification from a complete full node. Demonstration keys are source examples, not private workspace credentials. Deep-vector-quantization separates attempted VQVAE reproduction, data-driven initialization needed to avoid index collapse, finicky Gumbel tuning and unfinished DALL-E work; reconstruction loss alone is qualified evidence. EigenLibSVM documents a dense linear-kernel wrapper with a tiny installation demo. Find-birds separates resumable rate-limited social-graph acquisition from reports that can use partial results, while historical Twitter credentials/API instructions are not current recommendations. ForestJS makes weak learners pluggable and advises cross-validation of depth/tries; its universal tree-count and dimensionality statements remain historical source opinions. Gitstats is a small generated-repository-activity visualization. HN Time Capsule stages historical retrieval, prompts, paid analysis, parsing and HTML rendering; it is explicitly 99-percent vibe-coded and unsupported, so hindsight grades are model judgments rather than verified prediction accuracy.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text

# deep vector quantization

Implements training code for VQVAE's, i.e. autoencoders with categorical latent variable bottlenecks, which are then easy to subsequently plug into existing infrastructure for modeling sequences of discrete variables (GPT and friends). `dvq/vqvae.py` is the entry point of the training script and a small training run can be called e.g. as:

`cd dvq; python vqvae.py --gpus 1 --data_dir /somewhere/to/store/cifar10`

This will reproduce the original DeepMind VQVAE paper (see references before) using a semi-small network on CIFAR-10. Work on this repo is ongoing and for now requires reading of code and understanding these approaches. Next up aiming to reproduce DALL-E result, for this most of the code is in place but we need to train with the logit laplace distribution, tune the gumbel softmax hyperparameters, and train on ImageNet+.

### References

**DeepMind's [VQVAE](https://github.com/deepmind/sonnet/blob/v2/examples/vqvae_example.ipynb)**

The VQVAE from the paper can be trained with `--vq_flavor vqvae --enc_dec_flavor deepmind`. I am able to get what I think are expected results on CIFAR-10 using VQVAE (judging by reconstruction loss achieved). However I had to resort to a data-driven intialization scheme with k-means (which is with current implementation not multi-gpu compatible), and which the sonnet repo does not use, potentially due to more careful model initialization treatment. When I do not use data-driven init the training exhibits catastrophic index collapse.

**Jang et al. [Gumbel Softmax](https://arxiv.org/abs/1611.01144)**

For this use `--vq_flavor gumbel`. Trains and converges to slightly higher reconstruction loss, but tuning the scale of the kl divergence loss and the temperature decay rate and the version of gumbel (soft/hard) has so far proved a little bit finicky. Also the whole thing trains much slower. Requires a bit more thorough hyperparameter search than a few one-off guesses.

**OpenAI's [DALL-E](https://openai.com/blog/dall-e/)**

Re-implementation is not yet complete, e.g. we still use MSE is still used as a loss, we still only train on CIFAR and use a smaller network, etc. However, the different encoder/decoder architecture trains and gives comparable results to the (simpler) DeepMind version on untuned 1-GPU trial runs on stride /4 VQVAEs. Situation is developing...

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
