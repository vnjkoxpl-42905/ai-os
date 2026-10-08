---
type: source
subject: "GitHub source repos/karpathy/nanochat/pyproject.toml"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/pyproject.toml]
semantic-status: complete-named-text-read
---

# repos/karpathy/nanochat/pyproject.toml

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/pyproject.toml), SHA-256 `c91fdd03ae9705565572eee31924d4c0bca24bf5431a8eabff4c061882f94929`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "\\[project\\] name = \"nanochat\" version = \"0.1.0\" description = \"the minimal full-stack ChatGPT clone\" readme".

The remaining manifests distinguish nanochat mutually exclusive CPU/GPU Torch extras and opt-in development dependencies, with slow-test markers. RustBPE separates Rust library/Python extension linkage so cargo tests can link correctly, enables release LTO with slower compilation, and uses maturin for Python packaging. Reader3 declares EPUB parsing/server dependencies and ignores generated per-book data and EPUB inputs. Rendergit declares a small markdown/pygments utility and console entry point. Other ignore files keep checkpoints, generated event exports, local settings and logs separate from source. License boilerplate preserves permissions and attribution but is not personal doctrine; package metadata and dependencies are historical captured settings, not current verified installations.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
[project]
name = "nanochat"
version = "0.1.0"
description = "the minimal full-stack ChatGPT clone"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "filelock>=3.19.0",
    "kernels>=0.11.7",
    "numpy>=1.26.0",
    "psutil>=7.1.0",
    "pyarrow>=21.0.0",
    "rustbpe>=0.1.0",
    "tiktoken>=0.11.0",
    "torch==2.9.1",
    "wandb>=0.21.3",
]

[dependency-groups]
dev = [
    "ipykernel>=7.1.0",
    "matplotlib>=3.10.8",
    "pytest>=8.0.0",
    "python-dotenv>=1.2.1",
]

[tool.pytest.ini_options]
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]

# target torch to cuda 12.8 or CPU
[tool.uv.sources]
torch = [
    { index = "pytorch-cpu", extra = "cpu" },
    { index = "pytorch-cu128", extra = "gpu" },
]

[[tool.uv.index]]
name = "pytorch-cpu"
url = "https://download.pytorch.org/whl/cpu"
explicit = true

[[tool.uv.index]]
name = "pytorch-cu128"
url = "https://download.pytorch.org/whl/cu128"
explicit = true

[project.optional-dependencies]
cpu = [
    "setuptools>=65.0.0",
    "torch==2.9.1",
]
gpu = [
    "torch==2.9.1",
]

[tool.uv]
default-groups = []
conflicts = [
    [
        { extra = "cpu" },
        { extra = "gpu" },
    ],
]

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
