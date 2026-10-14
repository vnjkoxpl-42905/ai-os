---
name: vite-rebundles-mcp-function
description: Running the LSAT U dev server rewrites supabase/functions/mcp/index.ts into a near-empty stub; never commit that change.
metadata:
  node_type: memory
  type: project
  originSessionId: 9e2e52ef-70a6-4763-a599-5a2d1b96a303
  modified: 2026-10-13T19:03:58.380Z
---

Starting Vite in an LSAT U checkout lets the @lovable.dev/mcp-js plugin rebundle `supabase/functions/mcp/index.ts` from `src/lib/mcp/`. In a worktree it dropped about 590 lines, leaving a stub (seen 2026-10-13 in `lsatu-four-situations`).

**Why:** a stray `M supabase/functions/mcp/index.ts` looks like another session's work, and committing it would break the MCP edge function.

**How to apply:** after any preview run, check `git status`. If that file is modified and nobody edited `src/lib/mcp/`, `git restore` it. Never stage it with unrelated work. Related: [[push-only-your-own-commits]], [[branch-per-session-in-lsatu]].
