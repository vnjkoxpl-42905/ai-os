---
type: source
subject: "NanoGPT chooses a comparable baseline and adapts to hardware"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source]
sources: [../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/README.md]
semantic-status: complete-named-text-read
---

# NanoGPT chooses a comparable baseline and adapts to hardware

Repository owner: Andrej Karpathy; per-line authorship not independently verified. Original: https://github.com/karpathy/nanoGPT. Publication date unknown; captured and compiled 2026-10-08. [Preserved evidence](../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanoGPT/README.md), SHA-256 `8d969370683849a2cc4e46c81bf2449717f2daff657586888151933c3590f85f`. Captured commit and license are in the [manifest](../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## What this source says

> there is a dataset domain gap

The README describes medium-scale GPT reproduction, pretrained finetuning, checkpoints and generation. Its baseline section contrasts closed WebText with OpenWebText and argues that finetuning the reference checkpoint on OpenWebText gives a more appropriate reproduction baseline. CPU examples reduce context, model and evaluation work; distributed runs require interconnect benchmarking. A November2025 banner declares this repository deprecated in favor of nanochat.

## Interpretation and limits

Complete named text read. Historical PyTorch2.0 compile/Windows statements, GPU costs and runtime/loss claims were not verified against current tools. The old active-development paragraph conflicts temporally with the later deprecation banner; retain its history without recommending this as a current supported tool.

Related: [Karpathy hub](../../../karpathy/index.md). Coverage and cross-source conclusions: [repo/X synthesis](../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
