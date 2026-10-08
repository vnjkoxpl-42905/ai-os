---
type: source
subject: "GitHub source repos/karpathy/rendergit/pyproject.toml"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/rendergit/pyproject.toml]
semantic-status: complete-named-text-read
---

# repos/karpathy/rendergit/pyproject.toml

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/rendergit/pyproject.toml), SHA-256 `0288b6fedfc95e8671f27cedd47149601310eb9157cf6feada0516888d82caef`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "\\[build-system\\] requires = \\[\"setuptools >= 61.0\"\\] build-backend = \"setuptools.build_meta\" \\[project\\] name = \"rendergit\" version =".

The remaining manifests distinguish nanochat mutually exclusive CPU/GPU Torch extras and opt-in development dependencies, with slow-test markers. RustBPE separates Rust library/Python extension linkage so cargo tests can link correctly, enables release LTO with slower compilation, and uses maturin for Python packaging. Reader3 declares EPUB parsing/server dependencies and ignores generated per-book data and EPUB inputs. Rendergit declares a small markdown/pygments utility and console entry point. Other ignore files keep checkpoints, generated event exports, local settings and logs separate from source. License boilerplate preserves permissions and attribution but is not personal doctrine; package metadata and dependencies are historical captured settings, not current verified installations.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
[build-system]
requires = ["setuptools >= 61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "rendergit"
version = "0.1.0"
description = "Flatten a GitHub repo into a single static HTML page for fast skimming and Ctrl+F"
readme = "README.md"
license = "0BSD"
authors = [
    {name = "Andrej Karpathy"},
]
requires-python = ">=3.10"
dependencies = [
    "markdown>=3.8.2",
    "pygments>=2.19.2",
]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Topic :: Utilities",
]

[project.scripts]
rendergit = "rendergit:main"

[project.urls]
Homepage = "https://github.com/karpathy/rendergit"
Repository = "https://github.com/karpathy/rendergit"

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
