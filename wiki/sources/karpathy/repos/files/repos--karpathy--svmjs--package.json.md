---
type: source
subject: "GitHub source repos/karpathy/svmjs/package.json"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/svmjs/package.json]
semantic-status: complete-named-text-read
---

# repos/karpathy/svmjs/package.json

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/svmjs/package.json), SHA-256 `d5df672254b840ba22ef0c113891c67110bfdfcb1d5c39d377614d005a596d95`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "{ \"name\": \"svm\", \"description\": \"Support Vector Machines\", \"version\": \"0.1.0\", \"author\": \"Andrej Karpathy <andrej.karpathy@gmail.com>\", \"main\": \"./lib/svm\",".

The remaining manifests distinguish nanochat mutually exclusive CPU/GPU Torch extras and opt-in development dependencies, with slow-test markers. RustBPE separates Rust library/Python extension linkage so cargo tests can link correctly, enables release LTO with slower compilation, and uses maturin for Python packaging. Reader3 declares EPUB parsing/server dependencies and ignores generated per-book data and EPUB inputs. Rendergit declares a small markdown/pygments utility and console entry point. Other ignore files keep checkpoints, generated event exports, local settings and logs separate from source. License boilerplate preserves permissions and attribution but is not personal doctrine; package metadata and dependencies are historical captured settings, not current verified installations.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
{
  "name": "svm",
  "description": "Support Vector Machines",
  "version": "0.1.0",
  "author": "Andrej Karpathy <andrej.karpathy@gmail.com>",
  "main": "./lib/svm",
  "repository": {
    "type": "git",
    "url": "http://github.com/karpathy/svmjs.git"
  },
  "keywords": ["support vector machines", "machine learning", "classifier", "svm"]
}

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
