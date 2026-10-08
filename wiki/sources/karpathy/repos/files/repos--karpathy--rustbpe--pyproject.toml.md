---
type: source
subject: "GitHub source repos/karpathy/rustbpe/pyproject.toml"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/rustbpe/pyproject.toml]
semantic-status: complete-named-text-read
---

# repos/karpathy/rustbpe/pyproject.toml

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/rustbpe/pyproject.toml), SHA-256 `e6bf40aed81fe07a33aea4bdd459687b274ac527e9d34bb60722f97ece538f2d`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "\\[project\\] name = \"rustbpe\" version = \"0.1.0\" description = \"A BPE (Byte Pair Encoding) tokenizer".

The remaining manifests distinguish nanochat mutually exclusive CPU/GPU Torch extras and opt-in development dependencies, with slow-test markers. RustBPE separates Rust library/Python extension linkage so cargo tests can link correctly, enables release LTO with slower compilation, and uses maturin for Python packaging. Reader3 declares EPUB parsing/server dependencies and ignores generated per-book data and EPUB inputs. Rendergit declares a small markdown/pygments utility and console entry point. Other ignore files keep checkpoints, generated event exports, local settings and logs separate from source. License boilerplate preserves permissions and attribution but is not personal doctrine; package metadata and dependencies are historical captured settings, not current verified installations.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
[project]
name = "rustbpe"
version = "0.1.0"
description = "A BPE (Byte Pair Encoding) tokenizer written in Rust with Python bindings"
readme = "README.md"
license = { text = "MIT" }
requires-python = ">=3.9"
classifiers = [
    "Programming Language :: Rust",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
]

# Optional: runtime Python dependencies (if any)
dependencies = []

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "pytest-cov>=4.0",
]

# Tells Python to use maturin as the build backend
[build-system]
requires = ["maturin>=1.7,<2.0"]
build-backend = "maturin"

# Maturin-specific configuration
[tool.maturin]
# Build features - enables extension-module only for Python builds
features = ["extension-module"]

[tool.pytest.ini_options]
testpaths = ["tests/python"]
python_files = "test_*.py"
markers = [
    "slow: marks tests as slow (use -m 'not slow' to skip)",
]

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
