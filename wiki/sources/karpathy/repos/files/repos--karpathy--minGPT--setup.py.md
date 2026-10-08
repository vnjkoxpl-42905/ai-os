---
type: source
subject: "GitHub source repos/karpathy/minGPT/setup.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/minGPT/setup.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/minGPT/setup.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/minGPT/setup.py), SHA-256 `377a58d3f8d07b51d82e5e3ac6dda46d844895becce73a292b96b07539f06708`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "from setuptools import setup setup(name='minGPT', version='0.0.1', author='Andrej Karpathy', packages=\\['mingpt'\\], description='A PyTorch re-implementation of GPT', license='MIT',".

This batch contains package manifests, ignore rules, licenses and build settings, not new personal philosophies. MIT notices preserve attribution and warranty terms without proving per-line authorship. Ignore files separate datasets, runtime caches, artifacts and secrets from tracked code; autoresearch additionally excludes generated per-session agent prompt files and results. Requirements range from historical pins to unconstrained dependencies; no current compatibility or security is certified. Autoresearch pins a CUDA-specific Torch index and Python>=3.10, while several newer utilities use uv project manifests and .env exclusions. MatlabWrapper and EigenLibSVM build files explicitly encode local include/link paths and tiny demo targets, supporting the need to establish a working local environment rather than assume copied paths. Micrograd packaging declares its scalar educational scope; minGPT setup depends on Torch. Council frontend manifest is a React/Vite template configuration. These operational sources are preserved individually but not inflated into dozens of independent behavioral examples.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
from setuptools import setup

setup(name='minGPT',
      version='0.0.1',
      author='Andrej Karpathy',
      packages=['mingpt'],
      description='A PyTorch re-implementation of GPT',
      license='MIT',
      install_requires=[
            'torch',
      ],
)

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
