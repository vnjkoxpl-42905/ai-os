---
type: source
subject: "GitHub source repos/karpathy/llama2.c/win.c"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llama2.c/win.c]
semantic-status: complete-named-text-read
---

# repos/karpathy/llama2.c/win.c

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llama2.c/win.c), SHA-256 `33a6df145d7c7ad3ff444b61795d54f2823ab04e5705a80e9c89abdbb165abd4`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
#include "win.h" #include <errno.h> #include <io.h> #ifndef FILE_MAP_EXECUTE #define FILE_MAP_EXECUTE 0x0020 #endif /* FILE_MAP_EXECUTE */
```

Six sources fully read. Tokenizer.py explicitly Meta-derived lightly modified under Llama Community License, exports piece scores/UTF8 bytes, whitespace replacement/BOS EOS labels and max length to C format; not independent Karpathy belief. Train.py supports smalldebug or DDP, validates tokenizer and accumulation divisibility, records tokens-per-iteration, seed offsets, mixed precision/scaler, resume architecture/model/optimizer, compile, train/val loss, warmup-cosine LR, validation checkpoints, gradient accumulation with last-step sync, unscale-before-clip and prefetch. Optional logging failure surfaced with print; max_iters strict-greater termination adds extra iteration. Comments admit unexplained checkpoint prefix, prefer direct DDP flag over duplicative context; preserve contextual simplicity choice. Windows mmap shim is credited mman-win32, maps file/protection/flush/locks, error mapping TODO and GetTickCount wraps, no independent persona. Council package marker and config load .env key by name, four historical model IDs, Gemini chair, OpenRouter endpoint and local conversations path; no credentials read or API run.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
#include "win.h"
#include <errno.h>
#include <io.h>

#ifndef FILE_MAP_EXECUTE
#define FILE_MAP_EXECUTE    0x0020
#endif /* FILE_MAP_EXECUTE */

static int __map_mman_error(const uint32_t err, const int deferr)
{
    if (err == 0)
        return 0;
    //TODO: implement
    return err;
}

static uint32_t __map_mmap_prot_page(const int prot)
{
    uint32_t protect = 0;
    
    if (prot == PROT_NONE)
        return protect;
        
    if ((prot & PROT_EXEC) != 0)
    {
        protect = ((prot & PROT_WRITE) != 0) ? 
                    PAGE_EXECUTE_READWRITE : PAGE_EXECUTE_READ;
    }
    else
    {
        protect = ((prot & PROT_WRITE) != 0) ?
                    PAGE_READWRITE : PAGE_READONLY;
    }
    
    return protect;
}

static uint32_t __map_mmap_prot_file(const int prot)
{
    uint32_t desiredAccess = 0;
    
    if (prot == PROT_NONE)
        return desiredAccess;
        
    if ((prot & PROT_READ) != 0)
        desiredAccess |= FILE_MAP_READ;
    if ((prot & PROT_WRITE) != 0)
        desiredAccess |= FILE_MAP_WRITE;
    if ((prot & PROT_EXEC) != 0)
        desiredAccess |= FILE_MAP_EXECUTE;
    
    return desiredAccess;
}

void* mmap(void *addr, size_t len, int prot, int flags, int fildes, ssize_t off)
{
    HANDLE fm, h;
    void * map = MAP_FAILED;
    
#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable: 4293)
#endif

    const uint32_t dwFileOffsetLow = (uint32_t)(off & 0xFFFFFFFFL);
    const uint32_t dwFileOffsetHigh = (uint32_t)((off >> 32) & 0xFFFFFFFFL);
    const uint32_t protect = __map_mmap_prot_page(prot);
    const uint32_t desiredAccess = __map_mmap_prot_file(prot);

    const ssize_t maxSize = off + (ssize_t)len;

    const uint32_t dwMaxSizeLow = (uint32_t)(maxSize & 0xFFFFFFFFL);
    const uint32_t dwMaxSizeHigh = (uint32_t)((maxSize >> 32) & 0xFFFFFFFFL);

#ifdef _MSC_VER
#pragma warning(pop)
#endif

    errno = 0;
    
    if (len == 0 
        /* Unsupported flag combinations */
        || (flags & MAP_FIXED) != 0
        /* Unsupported protection combinations */
        || prot == PROT_EXEC)
    {
        errno = EINVAL;
        return MAP_FAILED;
    }
    
    h = ((flags & MAP_ANONYMOUS) == 0) ? 
                    (HANDLE)_get_osfhandle(fildes) : INVALID_HANDLE_VALUE;

    if ((flags & MAP_ANONYMOUS) == 0 && h == INVALID_HANDLE_VALUE)
    {
        errno = EBADF;
        return MAP_FAILED;
    }

    fm = CreateFileMapping(h, NULL, protect, dwMaxSizeHigh, dwMaxSizeLow, NULL);

    if (fm == NULL)
    {
        errno = __map_mman_error(GetLastError(), EPERM);
        return MAP_FAILED;
    }

    map = MapViewOfFile(fm, desiredAccess, dwFileOffsetHigh, dwFileOffsetLow, len);

    CloseHandle(fm);

    if (map == NULL)
    {
        errno = __map_mman_error(GetLastError(), EPERM);
        return MAP_FAILED;
    }

    return map;
}

int munmap(void *addr, size_t len)
{
    if (UnmapViewOfFile(addr))
        return 0;
        
    errno =  __map_mman_error(GetLastError(), EPERM);
    
    return -1;
}

int mprotect(void *addr, size_t len, int prot)
{
    uint32_t newProtect = __map_mmap_prot_page(prot);
    uint32_t oldProtect = 0;
    
    if (VirtualProtect(addr, len, newProtect, &oldProtect))
        return 0;
    
    errno =  __map_mman_error(GetLastError(), EPERM);
    
    return -1;
}

int msync(void *addr, size_t len, int flags)
{
    if (FlushViewOfFile(addr, len))
        return 0;
    
    errno =  __map_mman_error(GetLastError(), EPERM);
    
    return -1;
}

int mlock(const void *addr, size_t len)
{
    if (VirtualLock((LPVOID)addr, len))
        return 0;
        
    errno =  __map_mman_error(GetLastError(), EPERM);
    
    return -1;
}

int munlock(const void *addr, size_t len)
{
    if (VirtualUnlock((LPVOID)addr, len))
        return 0;
        
    errno =  __map_mman_error(GetLastError(), EPERM);
    
    return -1;
}

// Portable clock_gettime function for Windows
int clock_gettime(int clk_id, struct timespec *tp) {
    uint32_t ticks = GetTickCount();
    tp->tv_sec = ticks / 1000;
    tp->tv_nsec = (ticks % 1000) * 1000000;
    return 0;
}

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
