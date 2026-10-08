---
type: source
subject: "GitHub source repos/karpathy/reader3/pyproject.toml"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/reader3/pyproject.toml]
semantic-status: complete-named-text-read
---

# repos/karpathy/reader3/pyproject.toml

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/reader3/pyproject.toml), SHA-256 `d16eafaed191a98ac3819ff20fcaec3ae297327223c6ba46a06a83d10068618a`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
\[project\] name = "reader3" version = "0.1.0" description = "Simple EPUB reader web app" readme
```

The remaining manifests distinguish nanochat mutually exclusive CPU/GPU Torch extras and opt-in development dependencies, with slow-test markers. RustBPE separates Rust library/Python extension linkage so cargo tests can link correctly, enables release LTO with slower compilation, and uses maturin for Python packaging. Reader3 declares EPUB parsing/server dependencies and ignores generated per-book data and EPUB inputs. Rendergit declares a small markdown/pygments utility and console entry point. Other ignore files keep checkpoints, generated event exports, local settings and logs separate from source. License boilerplate preserves permissions and attribution but is not personal doctrine; package metadata and dependencies are historical captured settings, not current verified installations.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
[project]
name = "reader3"
version = "0.1.0"
description = "Simple EPUB reader web app"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "beautifulsoup4>=4.14.2",
    "ebooklib>=0.20",
    "fastapi>=0.121.2",
    "jinja2>=3.1.6",
    "uvicorn>=0.38.0",
]

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
