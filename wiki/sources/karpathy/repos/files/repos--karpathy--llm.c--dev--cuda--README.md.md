---
type: source
subject: "GitHub source repos/karpathy/llm.c/dev/cuda/README.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/README.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/llm.c/dev/cuda/README.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm.c/dev/cuda/README.md), SHA-256 `8e97bdc99da7f86312d46864c1d0a2dbe34acfc2a7b6bc3ae83b38ba8c7042ee`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
# dev/cuda This directory is scratch space for developing various versions of the needed CUDA
```

The council frontend README is an unchanged React/Vite template voice, not personal Karpathy opinion. Llm.c CUDA development begins with a naive kernel, compares CPU reference outputs on GPU, times launch configurations, then substitutes a measured faster kernel; documented complexity and runtime tradeoffs are explicit. Data scripts own per-dataset cache directories and share helpers. The evaluation README pins a harness version for comparability and admits unresolved bfloat16 scoring and unexpectedly expensive runtime issues instead of hiding them. The root llm.c README keeps simple frozen CPU/fp32 references alongside fast production-oriented kernels, cross-checks logits/loss/training trajectories against PyTorch, supplies a stepwise layernorm tutorial, and distinguishes platform-specific distributed launch options without declaring one universally superior. It explicitly may reject 2-percent performance for 500 lines and an exotic dependency, while accepting a standard one-line library call. These are project constraints rather than universal bans on dependency use.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

````text
# dev/cuda

This directory is scratch space for developing various versions of the needed CUDA kernels. Each file develops a kernel, and usually multiple versions of that kernel that could have different running times and of different code or time complexity.

See the top of each file for how to compile and run the kernel. Alternatively, the commands are also all grouped in the `Makefile` in this directory for convenience.

For example, we can look at the top of `layernorm_forward.cu` to build the forward pass kernels for the LayerNorm:

```bash
nvcc -O3 --use_fast_math -lcublas -lcublasLt layernorm_forward.cu -o layernorm_forward
```

or simply

```bash
make layernorm_forward
```

The comments at the top then document the different versions of this kernel available, usually these are in increasing complexity and decreasing running times. For example, inspecting the comments in the file on top, the most naive kernel we can then run as:

```bash
./layernorm_forward 1
```

You'll see that this first forwards the reference code on the CPU, then it runs kernel 1 on the GPU, compares the results to check for correctness, and then runs a number of configurations of this kernel (most often and most notably the block size), to time the kernel in these launch configurations. We can then run one of the faster kernels (kernel 4) instead:

```bash
./layernorm_forward 4
```

You'll see that this matches all the CPU results but runs much much faster. The typical process from here on is we copy paste the kernel that ran fastest, adjust it manually (e.g. to hardcode the best block size) and drop it into the training code file, e.g. `train_gpt2.cu`.

To add a new version of a kernel, add the kernel to the corresponding file and adjust the docs. To add a new kernel, add the new file and adjust the Makefile. Run `make clean` to clean up binaries from your directory.

If you do not have a GPU or is having trouble with CUDA dependencies, you can run the benchmarks on the [Modal platform](http://modal.com). For example, to run the benchmark for the attention forward pass on an A100 GPU with 80GB of memory, you can run the following command:

```bash
GPU_MEM=80 modal run benchmark_on_modal.py --compile-command "nvcc -O3 --use_fast_math attention_forward.cu -o attention_forward -lcublas" --run-command "./attention_forward 1"
```

````

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
