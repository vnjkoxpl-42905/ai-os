---
type: source
subject: "llm.c / dev/cuda/benchmark_on_modal.py"
created: 2026-10-08
updated: 2026-10-08
tags: [llm-wiki, karpathy, source-code]
---

# llm.c: dev/cuda/benchmark_on_modal.py

Captured repository source, owned by the Karpathy repository; individual contributor authorship is not established by repository ownership. Publication date: 2024-04-08T16:58:11Z (created); pushed 2025-06-26T17:03:40Z. Captured: 2026-10-08T09:34:49.848574Z.

[Archived file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/benchmark_on_modal.py) · [Original source](https://github.com/karpathy/llm.c)

SHA-256: `10cd8f84ef1c1d7092142a9ee7169ffa406f8f66d9117117a877a70f1c43698d`

## What the complete source contains

Evidence: `folks who do not have access to expensive GPUs locally` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/benchmark_on_modal.py)). The Modal harness describes running remote GPU benchmarks and Nsight profiling, with environment-selected A100/H100/A10G classes, GPU count and memory.

Evidence: `subprocess.run(command_args` ([raw](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/benchmark_on_modal.py)). It builds a remote CUDA/cuDNN/MPI image, mounts local files, executes space-split compile/run commands and moves reports into a named volume. Subprocess return codes are not checked explicitly; quoted shell arguments are not preserved by simple splitting. It was not run and does not establish a free or working service configuration.

## Interpretation and limits

Source text was fully read. Code was not run, dependencies were not installed, and performance, costs, model quality and correctness were not independently verified. This page records an educational or experimental implementation, not production acceptance. It does not independently establish a general personal belief or operating rule.
