---
type: source
subject: "GitHub source repos/karpathy/jobs/pyproject.toml"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/jobs/pyproject.toml]
semantic-status: complete-named-text-read
---

# repos/karpathy/jobs/pyproject.toml

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/jobs/pyproject.toml), SHA-256 `673e593a1cc9a451ddbdc1c2c446979665fa3669a51d62da11166ba6711a8c4e`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "\\[project\\] name = \"jobs\" version = \"0.1.0\" description = \"Add your description here\" readme =".

This batch contains package manifests, ignore rules, licenses and build settings, not new personal philosophies. MIT notices preserve attribution and warranty terms without proving per-line authorship. Ignore files separate datasets, runtime caches, artifacts and secrets from tracked code; autoresearch additionally excludes generated per-session agent prompt files and results. Requirements range from historical pins to unconstrained dependencies; no current compatibility or security is certified. Autoresearch pins a CUDA-specific Torch index and Python>=3.10, while several newer utilities use uv project manifests and .env exclusions. MatlabWrapper and EigenLibSVM build files explicitly encode local include/link paths and tiny demo targets, supporting the need to establish a working local environment rather than assume copied paths. Micrograd packaging declares its scalar educational scope; minGPT setup depends on Torch. Council frontend manifest is a React/Vite template configuration. These operational sources are preserved individually but not inflated into dozens of independent behavioral examples.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
[project]
name = "jobs"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "beautifulsoup4>=4.14.3",
    "httpx>=0.28.1",
    "playwright>=1.58.0",
    "python-dotenv>=1.2.2",
]

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
