# Connections

Registry of every live system Jay 2 can reach, mapped to the 7 Tier-1 data domains. The `/audit` skill reads this for domain coverage and freshness. When a new tool is wired, add a row **and** (if it has an API) save `references/{tool}-api.md` — researched-once-saved-forever.

**Access rule:** all Google surfaces go through the `gws` CLI (never the connector MCPs). All secrets live in the root `.env`. See CLAUDE.md → "Tools, keys, and connections."

> **Machine note (2026-09-07).** This vault now runs on **Windows** (`C:/Users/Joshu/dev/ai-os`).
> The root `.env` did **not** transfer from the Mac. It was recreated from scratch on 2026-09-07 and
> currently holds only `FIRECRAWL_API_KEY`, `LSATPREP_ADMIN_EMAIL`, `LSATPREP_ADMIN_PASSWORD`.
> Rows marked **unverified (Windows)** were last confirmed on the Mac and have no key on this box
> yet. Treat them as not connected until re-tested here.

| # | Domain | Tool | Mechanism | Auth | Last checked |
|---|---|---|---|---|---|
| 1 | Revenue / Financials | Stripe | Codex Stripe app (OAuth); CLI/API key (`.env`) | **verified via Codex app** - Aspiring Attorneys account listed in live mode; CLI/API key remains unverified | 2026-09-14 |
| 2 | Customer interactions | Gmail-as-CRM · TutorOcean | `gws` CLI · manual | **verified** (Gmail via OS keyring; project skills activated) | 2026-09-15 |
| 3 | Calendar | Cal.com · Google Calendar | key+ref · `gws` CLI | GCal **verified** · Cal.com **verified** | 2026-09-14 |
| 4 | Communication | Gmail | `gws gmail users getProfile`; OAuth token in OS keyring; routing skills in `.agents/skills/{gws-shared,gws-gmail,gws-gmail-read,gws-gmail-triage}` | **verified** - `contact@aspiringattorneys.com`, 4,113 msgs | 2026-09-15 |
| 5 | Project / task tracking | `wiki/tasks.md` ledger | local file (no external tracker) | n/a | 2026-07-17 |
| 6 | Meeting intelligence | Gmail/Drive session notes · Gemini Meet notes | `gws` CLI (export→`raw/`) | **verified** - Gemini notes in Drive | 2026-09-07 |
| 7 | Knowledge / files | Google Drive · this vault | `gws` CLI · local | **verified** | 2026-09-07 |
| 7b | LSAT U backend | Lovable Cloud `atrcqxpmqrynmtvvyjju` | REST + edge fns via admin JWT (`LSATPREP_ADMIN_*`) | **verified** - JWT issued, 3600s | 2026-09-07 |
| 8 | Web access | **Firecrawl** | CLI/API key (`.env`) · `references/firecrawl.md` | **verified** - `/v1/search`, `/v1/scrape`, `/v2/agent` active | 2026-09-19 |
| 9 | Code hosting | **GitHub** | `gh` CLI (account `vnjkoxpl-42905`) | **verified** | 2026-09-07 |

**Tier-2 (bonus):** NotebookLM (`nlm` CLI), YouTube Data API (**unverified (Windows)** - no key in `.env`), Integrated Browser MCP (VS Code).

**Mechanism legend:** `mcp` (MCP server) · `script` (Python/Bash hitting an API) · `export` (dump pipeline) · `key+ref` (`.env` key + `references/{tool}-api.md`) · `local` (file in this vault) · `not yet connected`.

**The LSAT U backend: what Jay 2 can and cannot do.** Verified end-to-end 2026-07-20.

"Lovable" and "Supabase" are not two backends. **Lovable Cloud IS a managed Supabase stack**
(Postgres, Auth, Storage, Edge Functions) that Lovable provisions and operates. That is why
both names appear. Full platform detail in [[wiki/lovable-cloud]]; live schema in
[[wiki/lsatu-backend-map]].

**CAN do programmatically** — no browser, no paste. Authenticate as admin against the public
auth API with `LSATPREP_ADMIN_EMAIL` / `LSATPREP_ADMIN_PASSWORD` from the root `.env`, using
the anon key in `projects/lsatu/.env`, then call PostgREST and the deployed edge functions
with that JWT. Verified: token issued, and `booking_passes` read back through RLS as admin.
This covers essentially all **data**-level work — reading and writing rows, calling RPCs like
`grant_booking_access` and `regenerate_booking_link`, driving the booking/homework/messaging
admin functions. The JWT expires in 3600s; re-auth rather than caching it.

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
- Session-note ingestion (Domain 6) is the highest-leverage under-used pipe: ~191 notes/yr, <10% currently ingested. Target of the planned post-session dispatch skill.
