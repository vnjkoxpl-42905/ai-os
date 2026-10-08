---
type: source
subject: "GitHub source repos/karpathy/llama2.c/.github/workflows/build.yml"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llama2.c/.github/workflows/build.yml]
semantic-status: complete-named-text-read
---

# repos/karpathy/llama2.c/.github/workflows/build.yml

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llama2.c/.github/workflows/build.yml), SHA-256 `94ad59b6f59c7a404b335aff99256088ed9715e29fd8f95192db7c42dfe47f75`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
name: Continuous Integration on: push: branches: - master paths: \['.github/workflows/**', '**/Makefile', '**/*.c', '**/*.h', '**/*.py'\] pull_request:
```

Five llama2.c CI/config/document sources fully read. CI builds Ubuntu and macOS, MSVC amd64/x86/arm64 matrix and MinGW, runs pytest except crosscompiled ARM64 and tolerates only brew update failure; configuration expresses coverage not proof current runs pass. MSVC batch uses optimized fast FP and OpenMP. Configurator explicitly dislikes complexity, executes trusted config files into globals then literal-evaluates known exact-type CLI overrides, rejects unknown keys; arbitrary config execution is not safe for untrusted input. Stories260K documents custom512token vocab, grouped shared KV heads, tiny baseline loss1.2968, uncertain ten-minute time, poor greedy sample and exact Python/C comparison with manual257 token bound due termination mismatch. Tokenizer note inspects actual Meta protobuf settings, recommends coverage1, digit split, whitespace pieces, byte fallback and identity normalization, explicitly approximate reproduction and newline/max-sentence assumptions.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
name: Continuous Integration

on:
  push:
    branches:
      - master
    paths: ['.github/workflows/**', '**/Makefile', '**/*.c', '**/*.h', '**/*.py']
  pull_request:
    types: [opened, synchronize, reopened]
    paths: ['**/Makefile', '**/*.c', '**/*.h', '**/*.py']
  # for manual triggering
  workflow_dispatch:

env:
  BRANCH_NAME: ${{ github.head_ref || github.ref_name }}

jobs:
  # check basic builds to avoid breaking changes
  ubuntu-focal-make:
    runs-on: ubuntu-latest

    steps:
      - name: Clone
        id: checkout
        uses: actions/checkout@v3

      - name: Dependencies
        id: depends
        run: |
          sudo apt-get update
          sudo apt-get install build-essential -y

      - name: Set up Python 3.10
        uses: actions/setup-python@v3
        with:
          python-version: "3.10"

      - name: Pip setup
        run: |
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

      - name: Build
        id: make_build
        run: |
          make

      - name: Build runfast
        id: make_build_runfast
        run: |
          make runfast

      - name: Test with pytest
        run: |
          pytest

  macOS-latest-make:
    runs-on: macos-latest

    steps:
      - name: Clone
        id: checkout
        uses: actions/checkout@v3

      - name: Dependencies
        id: depends
        continue-on-error: true
        run: |
          brew update

      - name: Set up Python 3.10
        uses: actions/setup-python@v3
        with:
          python-version: "3.10"

      - name: Pip setup
        run: |
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

      - name: Build clang
        id: make_build_clang
        run: |
          make run CC=clang

      - name: Build
        id: make_build
        run: |
          make

      - name: Build runfast
        id: make_build_runfast
        run: |
          make runfast

      - name: Test with pytest
        run: pytest




  windows-latest-make:
    runs-on: windows-latest

    strategy:
      fail-fast: false  #necessary, otherwise the matrix breaks
      matrix:
        arch:
          - amd64
          - amd64_x86
          - amd64_arm64

    steps:
      - name: Clone
        id: checkout
        uses: actions/checkout@v3

      - name: Setup MSBuild
        uses: microsoft/setup-msbuild@v1

      - name: Setup MSVC ${{ matrix.arch }}
        uses: ilammy/msvc-dev-cmd@v1
        with:
          arch: ${{ matrix.arch }}

      - name: Set up Python 3.10
        if: matrix.arch != 'amd64_arm64'
        uses: actions/setup-python@v3
        with:
          python-version: "3.10"

      - name: Pip setup
        if: matrix.arch != 'amd64_arm64'
        run: |
          python -m pip install --upgrade pip
          if (Test-Path requirements.txt) {
            pip install -r requirements.txt
          }

      - name: Build ${{ matrix.arch }}
        id: build_msvc
        run: |
          .\build_msvc.bat

      #cross-comiled, cannot be run on host
      - name: Test with pytest
        if: matrix.arch != 'amd64_arm64'
        run: pytest

  windows-latest-mingw:
    runs-on: windows-latest

    defaults:
      run:
        shell: msys2 {0}

    strategy:
      matrix:
        include:
          - { sys: mingw64, env: x86_64 }

    steps:
      - name: Checkout
        id: checkout
        uses: actions/checkout@v3

      - uses: msys2/setup-msys2@v2
        id: setup-msys2
        with:
          msystem: ${{ matrix.sys }}
          install: mingw-w64-${{matrix.env}}-gcc make

      - name: Build ${{ matrix.sys }} ${{ matrix.env }}
        id: build_mingw
        run: |
          make win64

      - name: Set up Python 3.10
        uses: actions/setup-python@v3
        with:
          python-version: "3.10"

      - name: Pip setup
        shell: powershell
        run: |
          python -m pip install --upgrade pip
          if (Test-Path requirements.txt) {
            pip install -r requirements.txt
          }

      - name: Test with pytest
        shell: powershell
        run: pytest

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
