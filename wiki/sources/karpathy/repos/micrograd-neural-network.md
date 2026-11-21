---
type: source
subject: "Micrograd builds neural networks from inspectable scalar parts"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source]
sources: [../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/micrograd/micrograd/nn.py]
semantic-status: complete-named-text-read
---

# Micrograd builds neural networks from inspectable scalar parts

Original repository: https://github.com/karpathy/micrograd. Publication date unknown; captured and compiled 2026-10-08. [Raw evidence](../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/micrograd/micrograd/nn.py), SHA-256 `f54453501abc4fd38ae724a8b378d6a5d23bfdd0a49c77e619b95f86ad16594d`. Commit and license: [manifest](../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json). Per-line authorship was not independently established.

## What this source says

> self.nonlin = nonlin

Module exposes parameter enumeration and gradient reset. A neuron composes scalar weighted inputs, bias and optional ReLU. Layers aggregate neurons; an MLP composes layers and makes the final layer linear. The zip-based input computation does not explicitly enforce input dimensionality. This is a compact educational abstraction, not a validated production interface.

## Interpretation and limits

Complete named source text read. The code was not executed or numerically tested; limitations above are inspection findings, not reproduced failures. Small explicit mechanisms support learning and review without establishing general model quality.

Related: [Karpathy hub](../../../karpathy/index.md). [Coverage](../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
