---
type: operating-layer
subject: Lovable Cloud (LSAT U backend platform)
updated: 2026-07-19
aliases: []
---

# Lovable Cloud (LSAT U backend platform)

Source: [Lovable Cloud docs clipping](<../raw/sources/clips/lovable-cloud/Lovable Cloud.md>) (`raw/sources/clips/lovable-cloud/`) (docs.lovable.dev/integrations/cloud, ingested 2026-07-19). This is what runs the LSAT U production backend (`atrcqxpmqrynmtvvyjju.supabase.co`).

## What it is

Lovable Cloud is Lovable's managed backend: a Supabase-based stack (Postgres, Auth, Storage, Edge Functions, Realtime, scheduled Jobs, AI gateway) that Lovable itself provisions and operates. The project is **not** in Joshua's own Supabase org and has no supabase.com dashboard — everything is managed through the Lovable editor's Cloud tab or by prompting Lovable in chat.

## Capabilities that matter for LSAT U

- **Database**: schema changes via SQL migrations that *Lovable* applies (pushed migrations do not auto-apply — confirmed 2026-07-19 when two booking migrations sat unapplied while edge functions synced). Daily backups, ~14 days retained, restorable from Cloud tab (restore is destructive/permanent).
- **Storage**: private-by-default buckets, files up to 2 GB. Public buckets blocked by default (workspace setting). Files are NOT included in DB exports — downloaded separately from Cloud tab → Storage.
- **Edge Functions**: deployed automatically on git push (this part does auto-sync). Logs visible in Cloud tab.
- **Jobs**: cron-style scheduled tasks, created/changed via SQL or Lovable chat.
- **Auth**: email/phone/Google/Apple; settings managed in Cloud tab.
- **Secrets**: write-only store for backend keys, injected into edge functions. `SUPABASE_*` and `LOVABLE_*` are reserved/auto-managed; the service-role key exists in the edge-function env (`Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")`) but is never shown to the user.
- **`.env` rule**: `VITE_*` values live in the committed `.env` (must NOT be gitignored in the lsatu repo — breaks Lovable previews); backend secrets live in the Secrets UI, never in `.env`.
- **Ops via chat**: health checks, slow-query analysis + auto-indexing, instance resize (Tiny→Large with approval card).
- **Billing**: one credit balance; Cloud + AI usage = Run credits; 20-credit monthly Cloud grant + 4-credit AI grant on paid plans. Auto-pause on inactivity (scheduled jobs prevent auto-pause).

## Control boundaries (Jay 2 vs Lovable)

Jay 2 can reach the backend only through: the deployed edge functions (admin JWT via `LSATPREP_ADMIN_*` creds), the public REST/auth APIs (anon key), and the git repo (code + migrations that Lovable then deploys/applies).

**Lovable-UI-only** (no API path, but Joshua can drive manually): the **Cloud tab → SQL editor** runs arbitrary SQL including DDL — discovered 2026-07-19 — so pending migrations never actually block on Lovable chat: Jay 2 writes the SQL, Joshua pastes and Runs. Still UI-only with no external path: secrets management, storage browsing/download, backups/restore, instance sizing, auth provider config, pause/remove, DB exports. There is no service-role key or DB connection string available outside Lovable, by design.

**Escape hatches**: full DB export (≤5 GB, 1/day) + GitHub repo = migration path to a self-owned Supabase project, but Lovable offers no one-click transfer, storage/auth/secrets must be rebuilt by hand, and Cloud→Supabase switching of a live project is explicitly unsupported. Decision 2026-07-19: stay on Lovable Cloud; treat Lovable chat as the operator for DB-level actions ("apply the pending migrations", "run a health check").
