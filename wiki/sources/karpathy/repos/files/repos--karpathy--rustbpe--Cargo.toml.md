---
type: source
subject: "GitHub source repos/karpathy/rustbpe/Cargo.toml"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/rustbpe/Cargo.toml]
semantic-status: complete-named-text-read
---

# repos/karpathy/rustbpe/Cargo.toml

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/rustbpe/Cargo.toml), SHA-256 `3a5782f2060de2474a471e4be8071c87fd15b1cc943e3af3d5ae0aeebd04e8d1`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "\\[package\\] name = \"rustbpe\" version = \"0.1.0\" edition = \"2021\" description = \"A BPE (Byte".

The remaining manifests distinguish nanochat mutually exclusive CPU/GPU Torch extras and opt-in development dependencies, with slow-test markers. RustBPE separates Rust library/Python extension linkage so cargo tests can link correctly, enables release LTO with slower compilation, and uses maturin for Python packaging. Reader3 declares EPUB parsing/server dependencies and ignores generated per-book data and EPUB inputs. Rendergit declares a small markdown/pygments utility and console entry point. Other ignore files keep checkpoints, generated event exports, local settings and logs separate from source. License boilerplate preserves permissions and attribution but is not personal doctrine; package metadata and dependencies are historical captured settings, not current verified installations.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
[package]
name = "rustbpe"
version = "0.1.0"
edition = "2021"
description = "A BPE (Byte Pair Encoding) tokenizer written in Rust with Python bindings"
license = "MIT"
readme = "README.md"

[lib]
# "cdylib" is required for Python bindings (shared library)
# "rlib" allows it to also be used as a normal Rust crate
crate-type = ["cdylib", "rlib"]

[dependencies]
# pyo3 provides the Python bindings
# "extension-module" is enabled via feature flag (see below)
pyo3 = { version = "0.27" }
dary_heap = "0.3"
indexmap = "2.2"
fancy-regex = "0.16.1"
log = "0.4.28"
pyo3-log = "0.13"
ahash = "0.8.12"
rayon = "1.11.0"
compact_str = "0.9.0"

[dev-dependencies]
# For Rust-side testing
criterion = "0.5"  # benchmarking (optional)

[features]
default = []
# extension-module is enabled by maturin during Python builds
# but NOT during cargo test, allowing tests to link properly
extension-module = ["pyo3/extension-module"]

# Profile for release builds - optimize for speed
[profile.release]
lto = true          # Link-time optimization
codegen-units = 1   # Better optimization, slower compile

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
