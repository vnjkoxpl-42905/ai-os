---
type: source
subject: "Micrograd makes reverse-mode differentiation inspectable"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, source]
sources: [../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/micrograd/micrograd/engine.py]
semantic-status: complete-named-text-read
---

# Micrograd makes reverse-mode differentiation inspectable

Repository owner: Andrej Karpathy; per-line authorship not independently verified. Original: https://github.com/karpathy/micrograd. Publication date unknown; captured and compiled 2026-10-08. [Preserved evidence](../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/micrograd/micrograd/engine.py), SHA-256 `95f19fa3734458d868e067d770f0773027763a2f654900bfbc1df8c5413acf84`. Captured commit and license are in the [manifest](../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## What this source says

> go one variable at a time and apply the chain rule

Value stores scalar data, a gradient, parent nodes and a backward closure. Addition, multiplication, powers and ReLU build the graph. backward creates a topological ordering, seeds the output gradient at one, and runs closures in reverse order. Gradients accumulate using +=, allowing shared parents to receive contributions from multiple paths.

## Interpretation and limits

The complete engine text was read; numerical behavior was not executed in this compilation. This demonstrates an inspectable implementation, not production readiness.

Related: [Karpathy hub](../../../karpathy/index.md). Coverage and cross-source conclusions: [repo/X synthesis](../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
