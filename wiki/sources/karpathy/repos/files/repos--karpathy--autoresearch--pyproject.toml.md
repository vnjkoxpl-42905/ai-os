---
type: source
subject: "GitHub source repos/karpathy/autoresearch/pyproject.toml"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/autoresearch/pyproject.toml]
semantic-status: complete-named-text-read
---

# repos/karpathy/autoresearch/pyproject.toml

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/autoresearch/pyproject.toml), SHA-256 `675c150a9e0769f0e39a43eb7d836934266fa348d6e2403521f1ff99f9b9f1af`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
\[project\] name = "autoresearch" version = "0.1.0" description = "Autonomous pretraining research swarm" readme =
```

This batch contains package manifests, ignore rules, licenses and build settings, not new personal philosophies. MIT notices preserve attribution and warranty terms without proving per-line authorship. Ignore files separate datasets, runtime caches, artifacts and secrets from tracked code; autoresearch additionally excludes generated per-session agent prompt files and results. Requirements range from historical pins to unconstrained dependencies; no current compatibility or security is certified. Autoresearch pins a CUDA-specific Torch index and Python>=3.10, while several newer utilities use uv project manifests and .env exclusions. MatlabWrapper and EigenLibSVM build files explicitly encode local include/link paths and tiny demo targets, supporting the need to establish a working local environment rather than assume copied paths. Micrograd packaging declares its scalar educational scope; minGPT setup depends on Torch. Council frontend manifest is a React/Vite template configuration. These operational sources are preserved individually but not inflated into dozens of independent behavioral examples.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
[project]
name = "autoresearch"
version = "0.1.0"
description = "Autonomous pretraining research swarm"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "kernels>=0.11.7",
    "matplotlib>=3.10.8",
    "numpy>=2.2.6",
    "pandas>=2.3.3",
    "pyarrow>=21.0.0",
    "requests>=2.32.0",
    "rustbpe>=0.1.0",
    "tiktoken>=0.11.0",
    "torch==2.9.1",
]

[tool.uv.sources]
torch = [
    { index = "pytorch-cu128" },
]

[[tool.uv.index]]
name = "pytorch-cu128"
url = "https://download.pytorch.org/whl/cu128"
explicit = true

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
