---
name: reading-center-standalone-first
description: "Reading Center is built as a standalone web app first (dev/ai-os-projects/reading-center), integrated into LSAT U later; access-flag assignment comes with integration."
metadata:
  node_type: memory
  type: project
  originSessionId: 95fbd50f-6898-4412-a19a-7fd02386eb44
  modified: 2026-10-13T11:39:36.096Z
---

Decided 2026-10-13: Reading Center (Spreeder-style speed reader) is built as its own web app at `dev/ai-os-projects/reading-center` (Vite, port 8100, browser storage), not inside LSAT U yet. The Teacher Workspace "Tools" room was built then reverted on `feat/reading-center` at his request.

**Why:** Joshua wants the platform finished on its own before integrating it into LSAT U.

**How to apply:** Joshua wants it identical to Spreeder in look and behaviour (2026-10-13); the source of truth is research/2026-10-13-spreeder-reconstruction-spec.md (live capture + shipped-code analysis), not the older build spec. Build features in the standalone app. Keep `src/features/reading-center/` in step with the LSAT U branch copy; only `hooks/useReadingCenterData.ts` (storage vs Supabase) and `lib/routes.ts` differ. When integrating, "assign" means granting a student access to the whole tool (an access flag), not assigning individual passages. The Supabase migration is unapplied and not needed until integration.
