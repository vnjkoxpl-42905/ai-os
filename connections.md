# Connections

Registry of every live system Jay 2 can reach, mapped to the 7 Tier-1 data domains. The `/audit` skill reads this for domain coverage and freshness. When a new tool is wired, add a row **and** (if it has an API) save `references/{tool}-api.md` — researched-once-saved-forever.

**Access rule:** all Google surfaces go through the `gws` CLI (never the connector MCPs). All secrets live in the root `.env`. See CLAUDE.md → "Tools, keys, and connections."

> **Windows verification, 2026-10-08.** The current root is `C:/Users/Joshu/dev/ai-os`.
> Narrow live reads succeeded for Gmail, Google Calendar, native Drive/Docs session records,
> Cal.com, LSAT U admin access and the private GitHub repository. Stripe's connected app requires
> reauthentication. Credential presence is not access proof, and this registry does not inventory
> secret values. Recheck person-specific operational state before acting.

| # | Domain | Tool | Mechanism | Auth | Last checked |
|---|---|---|---|---|---|
| 1 | Revenue / Financials | Stripe | Codex Stripe app (OAuth); CLI/API key (`.env`) | **blocked**: connected-app account read requires reauthentication; CLI/API access not verified | 2026-10-08 |
| 2 | Customer interactions | Gmail-as-CRM · TutorOcean | `gws` CLI · manual | **Gmail read verified**; TutorOcean not checked | 2026-10-08 |
| 3 | Calendar | Cal.com · Google Calendar | Cal.com `/v2/me` · `gws calendar events list` | **read verified**: Cal.com user record and two confirmed events in bounded 2026-10-08 Calendar window | 2026-10-08 |
| 4 | Communication | Gmail | `gws gmail users getProfile`; OAuth in configured keyring | **read verified**: `contact@aspiringattorneys.com`; profile only, not delivery verification | 2026-10-08 |
| 5 | Project / task tracking | `wiki/tasks.md` ledger | local file (no external tracker) | **route verified**; item status must be reconciled with its dated source/live backend | 2026-10-08 |
| 6 | Meeting intelligence | Gmail/Drive session notes · Gemini Meet notes | `gws drive files list`, `gws docs documents get`, preserved student exports | **read verified**: exact 2026-10-06 Yahunatan source and matching local source hashes; not a complete session sweep | 2026-10-08 |
| 7 | Knowledge / files | Google Drive · this vault | `gws` CLI · local files | **read verified**; filtered GitHub/Drive workspace receipts separate from raw archives and Obsidian Sync | 2026-10-08 |
| 7b | LSAT U backend | Lovable Cloud `atrcqxpmqrynmtvvyjju` | `node system/scripts/lsatu-admin.mjs access <exact-email>` | **admin read verified**; no fresh write or complete feature/permission check | 2026-10-08 |
| 8 | Web access | **Firecrawl** | CLI/API key (`.env`) · `references/firecrawl.md` | **verified** - `/v1/search`, `/v1/scrape`, `/v2/agent` active | 2026-09-19 |
| 9 | Code hosting | **GitHub** | `gh` CLI (account `vnjkoxpl-42905`) | **read verified**: private `vnjkoxpl-42905/ai-os`; snapshots use private local-sync branch, separate from main | 2026-10-08 |

**Tier-2 (bonus):** NotebookLM (`nlm` CLI) and YouTube Data API were not reverified in the 2026-10-08 audit. Browser availability is session-specific; use the actual exposed browser tools rather than assuming a retired VS Code integration.

**Obsidian Sync is a separate connection.** The installed Obsidian 1.14.4 CLI read confirms `C:/Users/Joshu/dev/ai-os` is **disconnected** on 2026-10-08, despite the core Sync plugin being enabled. GitHub/Drive success does not connect this vault to the phone. `ai-os` and old `Ai-os` differ only by case; the installed CLI's name targeting returned the current root for both, so verify the reported absolute vault path before any operation. Do not infer the old vault's remote status from that ambiguous name lookup.

**Mechanism legend:** `mcp` (MCP server) · `script` (Python/Bash hitting an API) · `export` (dump pipeline) · `key+ref` (`.env` key + `references/{tool}-api.md`) · `local` (file in this vault) · `not yet connected`.

**The LSAT U backend: what Jay 2 can and cannot do.** The broader notes below record the 2026-07-20 checks; the 2026-10-08 recheck establishes admin read/authentication only.

"Lovable" and "Supabase" are not two backends. **Lovable Cloud IS a managed Supabase stack**
(Postgres, Auth, Storage, Edge Functions) that Lovable provisions and operates. That is why
both names appear. Full platform detail in [[wiki/lovable-cloud]]; live schema in
[[wiki/lsatu-backend-map]].

**CAN do programmatically** — no browser, no paste. Authenticate as admin against the public
auth API with `LSATPREP_ADMIN_EMAIL` / `LSATPREP_ADMIN_PASSWORD` from the root `.env`, using
the anon key in `../ai-os-projects/lsatu/.env`, then call PostgREST and the deployed edge functions
with that JWT. Verified: token issued, and `booking_passes` read back through RLS as admin.
This covers essentially all **data**-level work — reading and writing rows, calling RPCs like
`grant_booking_access` and `regenerate_booking_link`, driving the booking/homework/messaging
admin functions. The JWT expires in 3600s; re-auth rather than caching it.

**Interactive Classroom lesson path (verified 2026-09-29):** Codex has a local stdio MCP server named `lsat-u-lessons` at `system/scripts/lsatu-lesson-mcp.mjs`. Its `publish_interactive_lesson` tool takes an exact student email, title, and absolute path to marked, self-contained HTML under 500 KB. It wraps `system/scripts/lsatu-admin.mjs post-lesson`, calls LSAT U's `mcp_post_classroom_note` RPC under the admin JWT, verifies byte-for-byte HTML and student visibility, and archives only older versions with the same lesson ID. A repeat of the current version returns the same item without notifying again. Use `dry_run: true` when identity or replacement is uncertain; otherwise post in one call. This local MCP is separate from the Supabase MCP described below. A newly registered MCP may need a new Codex session to become callable; the Node command runs the same operation immediately. No browser or Lovable step is part of daily content assignment. The in-app browser is for investigating a visual defect or changed renderer.
The student can open the full note from Classroom Notes and recaps, the in-app notification, or its Inbox link. Classroom Home can show a recent “Read” row, but urgent work may fill its four visible rows; Home placement is not guaranteed by the publishing API.

**CANNOT do — genuinely Lovable-UI-only, Joshua must drive:** DDL and migrations, secrets,
storage file browsing/download, backups and restore, instance sizing, auth provider config,
DB exports. There is no service-role key or DB connection string outside Lovable, by design.
Schema changes go through the `lovable-migrate` skill (Cloud tab → SQL editor + verification
probe). Note pushed migrations do **not** auto-apply — two booking migrations sat unapplied
on 2026-07-19 while edge functions synced.

**HAZARD — never resolve the project by name.** The connected Supabase MCP sees only
Joshua's *own* org `ostsvacinxuehptsniry`, which does not contain the live backend but does
contain a different project *also named "LSATU"* (`tlqltiklhmrceksqnwsl`, ACTIVE_HEALTHY).
SQL aimed at "the LSATU project" via the MCP applies cleanly to the wrong database and
reports success. Match the ref `atrcqxpmqrynmtvvyjju` exactly, or do not run it. The MCP is
not a path to this backend at all.

**Notes / gaps:**
- Task tracking is deliberately the `wiki/tasks.md` Now/Next/Done ledger, not an external tool (ClickUp/Asana). This is the intended design — the wiki is the tracker.
- Session-note intake is an active workflow through `ingest` and `post-session-recap`, with preserved student exports and packages. The old estimate of ~191 notes/year and <10% ingested was historical, not a current coverage statistic. Determine present coverage from a bounded Calendar/Drive reconciliation and the student indexes; do not infer it from file counts alone.
