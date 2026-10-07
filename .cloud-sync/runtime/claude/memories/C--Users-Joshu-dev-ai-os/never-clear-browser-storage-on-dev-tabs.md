---
name: never-clear-browser-storage-on-dev-tabs
description: Clearing localStorage in the in-app browser signs Joshua out of LSAT U; each localhost port is its own sign-in.
metadata:
  node_type: memory
  type: feedback
  originSessionId: 98b8acde-805c-4df0-919e-cf0b5ab52342
  modified: 2026-09-23T18:10:31.456Z
---

Never run `localStorage.clear()` / `sessionStorage.clear()` on an LSAT U tab in the in-app browser. The Supabase session lives in localStorage, so clearing it signs Joshua out and he has to log in again. On 2026-09-23 Claude cleared it to get past a "page failed to load" screen and cost him a login; he said he wants to "never log in again."

**Why:** he logs in by hand (Claude may not type passwords), so every lost session costs him time.

**How to apply:** for a stale-cache error, unregister service workers or hard-reload instead, and leave storage alone. Reuse the same dev port (8091 for the home-v2 worktree): each port is a separate origin with its own sign-in. Related: [[no-fake-urls-on-his-servers]].
