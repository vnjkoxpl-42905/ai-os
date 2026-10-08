---
type: source
subject: "GitHub source repos/karpathy/rustbpe/.gitignore"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/rustbpe/.gitignore]
semantic-status: complete-named-text-read
---

# repos/karpathy/rustbpe/.gitignore

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/rustbpe/.gitignore), SHA-256 `944a221618286781d197ce29d0e1284c7f601ea79fae76829e8a4b80f6a41342`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "# Rust build output target/ # Python-generated files __pycache__/ *.py\\[oc\\] build/ dist/ wheels/ *.egg-info/ #".

The remaining manifests distinguish nanochat mutually exclusive CPU/GPU Torch extras and opt-in development dependencies, with slow-test markers. RustBPE separates Rust library/Python extension linkage so cargo tests can link correctly, enables release LTO with slower compilation, and uses maturin for Python packaging. Reader3 declares EPUB parsing/server dependencies and ignores generated per-book data and EPUB inputs. Rendergit declares a small markdown/pygments utility and console entry point. Other ignore files keep checkpoints, generated event exports, local settings and logs separate from source. License boilerplate preserves permissions and attribution but is not personal doctrine; package metadata and dependencies are historical captured settings, not current verified installations.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
# Rust build output
target/

# Python-generated files
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info/

# Virtual environments
.venv/

# IDE
.idea/
.vscode/
*.swp
*.swo

# OS
.DS_Store

# Test cache
.pytest_cache/
.cache/

# Ignore dir for various dev files and artifacts
ignore/

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
