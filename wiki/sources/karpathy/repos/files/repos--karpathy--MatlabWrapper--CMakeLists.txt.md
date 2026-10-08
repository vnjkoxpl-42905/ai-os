---
type: source
subject: "GitHub source repos/karpathy/MatlabWrapper/CMakeLists.txt"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/MatlabWrapper/CMakeLists.txt]
semantic-status: complete-named-text-read
---

# repos/karpathy/MatlabWrapper/CMakeLists.txt

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/MatlabWrapper/CMakeLists.txt), SHA-256 `8b5846c792179368da42dc900379b34d94ca1fed7387dceede4c7bf122ca4133`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
cmake_minimum_required (VERSION 2.6) project (MatlabWrapper) # includes MATLAB dependenices. You may have to modify this
```

This batch contains package manifests, ignore rules, licenses and build settings, not new personal philosophies. MIT notices preserve attribution and warranty terms without proving per-line authorship. Ignore files separate datasets, runtime caches, artifacts and secrets from tracked code; autoresearch additionally excludes generated per-session agent prompt files and results. Requirements range from historical pins to unconstrained dependencies; no current compatibility or security is certified. Autoresearch pins a CUDA-specific Torch index and Python>=3.10, while several newer utilities use uv project manifests and .env exclusions. MatlabWrapper and EigenLibSVM build files explicitly encode local include/link paths and tiny demo targets, supporting the need to establish a working local environment rather than assume copied paths. Micrograd packaging declares its scalar educational scope; minGPT setup depends on Torch. Council frontend manifest is a React/Vite template configuration. These operational sources are preserved individually but not inflated into dozens of independent behavioral examples.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
cmake_minimum_required (VERSION 2.6)
project (MatlabWrapper)

# includes MATLAB dependenices. You may have to modify this based on
# your installation directories, exactly :(
set(MATLAB_LIBS eng mx m)
set(MATLAB_INCLUDES /usr/local/MATLAB/R2011b/extern/include /usr/local/MATLAB/R2011b/simulink/include /usr/local/MATLAB/R2011b/extern/include/cpp /usr/local/MATLAB/R2011b/extern/include)
set(MATLAB_LIB_PATHS /usr/local/MATLAB/R2011b/bin/glnxa64)
set(MATLAB_DEFS -DMATLAB_MEX_FILE -D_GNU_SOURCE -DGLNXA64 -DGCC -DMX_COMPAT_32 -DNDEBUG)
include_directories(${MATLAB_INCLUDES})
link_directories(${MATLAB_LIB_PATHS})
add_definitions(${MATLAB_DEFS})

# eigen library dependency. May have to change this too depending on where
# your eigen is. Good news is that eigen is just a bunch of header files,
# no library linking needed!
include_directories(/usr/local/include/eigen3)

# specify our library
add_library(mwlib src/MatlabWrapper.cpp)
include_directories(${PROJECT_SOURCE_DIR}/include)

# the provided test example of usage
add_executable (test1 test/test1.cpp)
target_link_libraries (test1 mwlib ${MATLAB_LIBS})

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
