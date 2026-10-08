---
type: source
subject: "GitHub source repos/karpathy/llama2.c/build_msvc.bat"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llama2.c/build_msvc.bat]
semantic-status: complete-named-text-read
---

# repos/karpathy/llama2.c/build_msvc.bat

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llama2.c/build_msvc.bat), SHA-256 `6c0670ef0c15967fb941c3b7b27e4aa33d3b56a4e7ed7156e1fe07a743b7a3d7`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
cl.exe /fp:fast /Ox /openmp /I. run.c win.c
```

Five llama2.c CI/config/document sources fully read. CI builds Ubuntu and macOS, MSVC amd64/x86/arm64 matrix and MinGW, runs pytest except crosscompiled ARM64 and tolerates only brew update failure; configuration expresses coverage not proof current runs pass. MSVC batch uses optimized fast FP and OpenMP. Configurator explicitly dislikes complexity, executes trusted config files into globals then literal-evaluates known exact-type CLI overrides, rejects unknown keys; arbitrary config execution is not safe for untrusted input. Stories260K documents custom512token vocab, grouped shared KV heads, tiny baseline loss1.2968, uncertain ten-minute time, poor greedy sample and exact Python/C comparison with manual257 token bound due termination mismatch. Tokenizer note inspects actual Meta protobuf settings, recommends coverage1, digit split, whitespace pieces, byte fallback and identity normalization, explicitly approximate reproduction and newline/max-sentence assumptions.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
cl.exe /fp:fast /Ox /openmp /I. run.c win.c 

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
