---
type: source
subject: "GitHub source repos/karpathy/llama2.c/win.h"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llama2.c/win.h]
semantic-status: complete-named-text-read
---

# repos/karpathy/llama2.c/win.h

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llama2.c/win.h), SHA-256 `718d5c4d246a4262e7b8c6caaf7191d3e5d6d73050ec4c54a75916c00df1d833`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
#ifndef _WIN_H_ #define _WIN_H_ #define WIN32_LEAN_AND_MEAN // Exclude rarely-used stuff from Windows headers #include <windows.h>
```

Six sources fully read. Tokenizer.py explicitly Meta-derived lightly modified under Llama Community License, exports piece scores/UTF8 bytes, whitespace replacement/BOS EOS labels and max length to C format; not independent Karpathy belief. Train.py supports smalldebug or DDP, validates tokenizer and accumulation divisibility, records tokens-per-iteration, seed offsets, mixed precision/scaler, resume architecture/model/optimizer, compile, train/val loss, warmup-cosine LR, validation checkpoints, gradient accumulation with last-step sync, unscale-before-clip and prefetch. Optional logging failure surfaced with print; max_iters strict-greater termination adds extra iteration. Comments admit unexplained checkpoint prefix, prefer direct DDP flag over duplicative context; preserve contextual simplicity choice. Windows mmap shim is credited mman-win32, maps file/protection/flush/locks, error mapping TODO and GetTickCount wraps, no independent persona. Council package marker and config load .env key by name, four historical model IDs, Gemini chair, OpenRouter endpoint and local conversations path; no credentials read or API run.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
#ifndef _WIN_H_
#define _WIN_H_

#define WIN32_LEAN_AND_MEAN      // Exclude rarely-used stuff from Windows headers
#include <windows.h>
#include <time.h>
#include <stdint.h>

#define ssize_t int64_t
#define ftell _ftelli64

// Below code is originally from mman-win32
//
/*
 * sys/mman.h
 * mman-win32
 */

#ifndef _WIN32_WINNT            // Allow use of features specific to Windows XP or later.
#define _WIN32_WINNT    0x0501  // Change this to the appropriate value to target other versions of Windows.
#endif

/* All the headers include this file. */
#ifndef _MSC_VER
#include <_mingw.h>
#endif

#include <sys/types.h>

#ifdef __cplusplus
extern "C" {
#endif

#define PROT_NONE       0
#define PROT_READ       1
#define PROT_WRITE      2
#define PROT_EXEC       4

#define MAP_FILE        0
#define MAP_SHARED      1
#define MAP_PRIVATE     2
#define MAP_TYPE        0xf
#define MAP_FIXED       0x10
#define MAP_ANONYMOUS   0x20
#define MAP_ANON        MAP_ANONYMOUS

#define MAP_FAILED      ((void *)-1)

/* Flags for msync. */
#define MS_ASYNC        1
#define MS_SYNC         2
#define MS_INVALIDATE   4

/* Flags for portable clock_gettime call. */
#define CLOCK_REALTIME  0

void*   mmap(void *addr, size_t len, int prot, int flags, int fildes, ssize_t off);
int     munmap(void *addr, size_t len);
int     mprotect(void *addr, size_t len, int prot);
int     msync(void *addr, size_t len, int flags);
int     mlock(const void *addr, size_t len);
int     munlock(const void *addr, size_t len);
int     clock_gettime(int clk_id, struct timespec *tp);

#ifdef __cplusplus
};
#endif

#endif /*  _WIN_H_ */

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
