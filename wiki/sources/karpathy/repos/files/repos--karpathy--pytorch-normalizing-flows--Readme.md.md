---
type: source
subject: "GitHub source repos/karpathy/pytorch-normalizing-flows/Readme.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/pytorch-normalizing-flows/Readme.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/pytorch-normalizing-flows/Readme.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/pytorch-normalizing-flows/Readme.md), SHA-256 `820dc89dfdf93c0507385c25c4524e045c235f90676c10e4d777e532b35ca718`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "# pytorch-normalizing-flows Implementions of normalizing flows (NICE, RealNVP, MAF, IAF, Neural Splines Flows, etc) in".

PyTorch MADE reimplements a paper with masked autoregressive dependencies, contrasts cheap likelihood with sequential sampling and admits failure to reproduce claimed single-pass multi-mask gains; averaged multiple passes improve reported loss at added cost. Normalizing-flows README lists GPU/high-dimensional/image support and stable-update work as TODO, not implemented capability. Matlab Random Forest explicitly restricts itself to learning and recommends mature alternatives for serious use. Randomfun Rust notes are learning notes and broad claims about language safety need qualifications before practical reuse. Reader3 is a chapter-oriented EPUB-to-local-library/LLM co-reading illustration, explicitly mostly vibe-coded and unsupported. RecurrentJS exposes values/derivatives, expression graphs and optimizers but warns beta users must understand backprop; its example variable inconsistencies are not certified executable code. ReinforceJS marks continuous policy/actor-critic work very alpha and reuses RecurrentJS, so these are not independent implementation evidence. Researchlei separates citation acquisition and visual library while admitting sparse indexes and aggressive external throttling. RustBPE aims at a small fast training component interoperating with tiktoken inference; it explicitly discloses LLM-assisted Rust and compares equality against an author-understood Python reference rather than treating passing tests as proof of idiomatic Rust design.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
# pytorch-normalizing-flows

Implementions of normalizing flows (NICE, RealNVP, MAF, IAF, Neural Splines Flows, etc) in PyTorch.

![Normalizing Flow fitting a 2D dataset](https://github.com/karpathy/pytorch-normalizing-flows/blob/master/assets/moon_flow.png)

**todos**
- TODO: make work on GPU
- TODO: 2D -> ND: get (flat) using MNIST
- TODO: ND -> images (multi-scale architectures, Glow nets, etc) on MNIST/CIFAR/ImageNet
- TODO: more stable residual-like IAF-style updates (tried but didn't work too well)
- TODO: parallel wavenet
- TODO: radial/planar 2D flows from Rezende Mohamed 2015?

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
