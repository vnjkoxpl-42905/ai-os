---
type: source
subject: "GitHub source repos/karpathy/llm-council/frontend/README.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm-council/frontend/README.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/llm-council/frontend/README.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm-council/frontend/README.md), SHA-256 `7a6f004c103a2e323a5677758071ad4dfe22ea8a92883aadd5f5b39b46dd729d`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "# React + Vite This template provides a minimal setup to get React working in".

The council frontend README is an unchanged React/Vite template voice, not personal Karpathy opinion. Llm.c CUDA development begins with a naive kernel, compares CPU reference outputs on GPU, times launch configurations, then substitutes a measured faster kernel; documented complexity and runtime tradeoffs are explicit. Data scripts own per-dataset cache directories and share helpers. The evaluation README pins a harness version for comparability and admits unresolved bfloat16 scoring and unexpectedly expensive runtime issues instead of hiding them. The root llm.c README keeps simple frozen CPU/fp32 references alongside fast production-oriented kernels, cross-checks logits/loss/training trajectories against PyTorch, supplies a stepwise layernorm tutorial, and distinguishes platform-specific distributed launch options without declaring one universally superior. It explicitly may reject 2-percent performance for 500 lines and an exotic dependency, while accepting a standard one-line library call. These are project constraints rather than universal bans on dependency use.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) (or [oxc](https://oxc.rs) when used in [rolldown-vite](https://vite.dev/guide/rolldown)) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
