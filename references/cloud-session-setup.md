# Claude Code cloud setup for LSAT U

This reference describes the LSAT U app repository at `../ai-os-projects/lsatu/`, relocated outside the vault on 2026-09-30. The app repository is a separate private GitHub repository, `vnjkoxpl-42905/lsatu-684d89db`, with `origin` set to `https://github.com/vnjkoxpl-42905/lsatu-684d89db.git`. The repository was inspected locally on 2026-09-29. Do not treat this note as permission to publish or deploy. A push to app `main` can trigger production deployment. Follow the app repo's own `AGENTS.md` and `CLAUDE.md` before changing it.

## Runtime and commands

Verified locally: Node `v24.19.0`; npm is the package manager and `package-lock.json` is canonical. `package.json` does not declare a Node version. Install dependencies with `npm ci`.

Setup script to run with the working directory set to the app repository:

```sh
npm ci
```

Verified package commands:

| Purpose | Command |
|---|---|
| Install | `npm ci` |
| Typecheck | `npm run typecheck` |
| Build | `npm run build` |
| Development server | `npm run dev` |
| Unit tests | `npm test` or `npm run test` |
| Browser end-to-end tests | `npm run test:e2e` |
| Lint | `npm run lint` |
| Preview built app | `npm run preview` |
| Booking Edge Function test | `npm run test:booking:edge` |
| Booking database test | `npm run test:booking:db` |

`npm run build` runs `prebuild` first. `prebuild` executes the three local asset builders in `scripts/`. The database booking test and broader booking suite may need access to a database. These commands were read from `package.json`; they were not run as part of this inventory.

## Secrets to add

No secret is required for `npm ci`. Add only values required by the specific task. The names below were found in `.env.example`, the local `.env` name scan, and static references in application, script, configuration, and Edge Function source. No values were read into output. Names that are ordinary runtime controls or public client configuration are marked accordingly.

| NAME | Purpose | Who uses it | Where Joshua finds the value |
|---|---|---|---|
| `VITE_SUPABASE_URL` | Supabase API URL | Browser app | Lovable Cloud project settings |
| `VITE_SUPABASE_PROJECT_ID` | Supabase project identifier | Browser app | Lovable Cloud project settings |
| `VITE_SUPABASE_PUBLISHABLE_KEY` | Public Supabase client key; access is governed by grants and RLS | Browser app | Lovable Cloud project settings |
| `VITE_GOOGLE_CLIENT_ID` | Google sign-in or picker client identity | Browser app | Google Cloud Console OAuth credentials |
| `VITE_GOOGLE_API_KEY` | Browser-side Google API integration | Browser app | Google Cloud Console API credentials |
| `VITE_TURNSTILE_SITE_KEY` | Public Turnstile widget key | Browser app | Cloudflare Turnstile dashboard |
| `VITE_DEV_BYPASS_GATES` | Local development gate bypass switch | Browser app, development only | Set locally only when needed; not a credential |
| `VITE_BUILD_SHA` | Optional build revision label | Vite build config | Build system; not a credential |
| `SUPABASE_URL` | Supabase API URL | Edge Functions and scripts | Lovable Cloud project settings |
| `SUPABASE_ANON_KEY` | Supabase anonymous API key | Edge Functions and MCP helper code | Lovable Cloud project settings |
| `SUPABASE_PUBLISHABLE_KEY` | Supabase publishable API key | MCP helper code | Lovable Cloud project settings |
| `SUPABASE_SERVICE_ROLE_KEY` | Elevated Supabase access, bypasses RLS | Edge Functions and lifecycle scripts | Lovable Cloud secrets; do not give to a general-purpose cloud session |
| `EDGE_INTERNAL_KEY` | Internal authorization between Edge Functions and lifecycle checks | Edge Functions and integration scripts | Lovable Cloud secrets; ask Joshua for scoped access if required |
| `LOVABLE_API_KEY` | Lovable AI/runtime API access | Edge Functions | Lovable Cloud secrets |
| `LOVABLE_SEND_URL` | Lovable transactional email service endpoint | Email Edge Function helper | Lovable Cloud configuration |
| `LOVABLE_DB_MIGRATION_URL` | Database connection for Drizzle migration tooling | Migration tooling | Lovable Cloud database settings; not documented as available outside Lovable |
| `GEMINI_API_KEY` | Gemini model requests | Edge Functions | Google AI Studio or Google Cloud, depending on the configured project |
| `DEEPGRAM_API_KEY` | Speech transcription or audio processing | `grade-rrc-section` Edge Function | Deepgram console |
| `GOOGLE_OAUTH_CLIENT_ID` | Google OAuth client identity | Shared Google Calendar Edge Function code | Google Cloud Console OAuth credentials |
| `GOOGLE_OAUTH_CLIENT_SECRET` | Google OAuth client secret | Shared Google Calendar Edge Function code | Google Cloud Console OAuth credentials |
| `GOOGLE_CALENDAR_REFRESH_TOKEN` | Google Calendar delegated access | Shared Google Calendar Edge Function code | Joshua's authorized Google OAuth setup; do not copy into chat |
| `GOOGLE_CALENDAR_API_KEY` | Google Calendar API access | `teacher-operator-chat` Edge Function | Google Cloud Console API credentials |
| `GOOGLE_DRIVE_API_KEY` | Google Drive API integration | Drive, session ingestion, and teacher operator Edge Functions | Google Cloud Console API credentials |
| `GOOGLE_MAIL_API_KEY` | Gmail API integration | Gmail, session scan, and teacher operator Edge Functions | Google Cloud Console API credentials |
| `GMAIL_CLIENT_ID` | Gmail OAuth client identity | `ta-agent` Edge Function | Google Cloud Console OAuth credentials |
| `GMAIL_CLIENT_SECRET` | Gmail OAuth client secret | `ta-agent` Edge Function | Google Cloud Console OAuth credentials |
| `GMAIL_REFRESH_TOKEN` | Gmail delegated access | `ta-agent` Edge Function | Joshua's authorized Google OAuth setup; do not copy into chat |
| `GITHUB_TOKEN` | GitHub API access for the `inspect` Edge Function | Edge Function | GitHub account or organization token settings, scoped to the required repository access |
| `GITHUB_REPO` | Repository selector used with the GitHub token | `inspect` Edge Function | Repository identifier; configuration, not a secret |
| `BOOKING_WORKER_SECRET` | Authorizes booking reconciliation worker calls | `gcal-reconcile` Edge Function | Lovable Cloud secrets |
| `BOOKING_IP_HMAC_KEY` | HMAC protection for booking IP data | `single-session` Edge Function | Lovable Cloud secrets |
| `BOOKING_ADMIN_EMAIL` | Admin email used by booking functions | Public and student booking Edge Functions | Joshua's app configuration; not a secret |
| `APP_ORIGIN` | Allowed application origin for booking functions | Booking, admin, and single-session Edge Functions | Production/app configuration; not a secret |
| `APP_BASE_URL` | Application URL used in email links | Assignment and section report Edge Functions | Production/app configuration; not a secret |
| `SESSION_SYNTHESIS_MODEL` | Model selection for session synthesis | Edge Function | Lovable Cloud configuration; not a secret |
| `TA_AGENT_GEMINI_MODEL` | Model selection for TA agent | Edge Function | Lovable Cloud configuration; not a secret |
| `DATABASE_URL` | Direct database connection used by knowledge ingestion | `scripts/knowledge/ingest-lr-explanations.mjs` | Lovable Cloud database settings; no external read-only URL was found in repo documentation |
| `ADMIN_JWT` | Admin authorization for integration verification | `scripts/knowledge/verify-integration.mjs` | Generate through the authorized app environment; do not copy into chat |
| `STUDENT_JWT` | Student authorization for integration verification | `scripts/knowledge/verify-integration.mjs` | Generate through a designated test account; do not use a real student's token |
| `ALLOW_DRIFT` | Controls content import drift behavior | `scripts/main-conclusion/import-content.ts` | Set only when needed; not a credential |
| `DRY_RUN` | Requests non-writing mode for knowledge ingestion | `scripts/knowledge/ingest-lr-explanations.mjs` | Set only when needed; not a credential |
| `EMIT_SQL` | Controls SQL output generation | `scripts/knowledge/ingest-lr-explanations.mjs` | Set only when needed; not a credential |
| `EMIT_SQL_DIR` | Output directory for generated SQL | `scripts/knowledge/ingest-lr-explanations.mjs` | Set only when needed; not a credential |
| `SQL_CHUNK_BYTES` | Generated SQL chunk size | `scripts/knowledge/ingest-lr-explanations.mjs` | Set only when needed; not a credential |
| `DEBUG` | Debug output switch | `scripts/main-conclusion/import-content.ts` | Set only when needed; not a credential |
| `OUT` | Local output path override | `scripts/_dl.ts` | Local script option; not a credential |
| `HOME` | Home directory path | `scripts/grade-census.ts` | Supplied by the operating system; not a credential |
| `PORT` | Local server port | Vite and sample server scripts | Set by the runner; not a credential |
| `CI` | Continuous integration mode switch | Playwright config | Set by the CI runner; not a credential |
| `DEV` | Vite development mode flag | Browser app and Vite | Supplied by Vite; not a credential |
| `NODE_ENV` | Node runtime mode | Vitest config | Supplied by the runner; not a credential |

## Scripts that need network access or credentials

These paths were identified by static inspection. The names listed are the relevant inputs seen in source. A script can also depend on an authenticated CLI session or a browser session rather than an environment variable. Do not run scripts that write to production data unless the task explicitly calls for that and the target is verified.

| Path | What it does | Network or credential needs |
|---|---|---|
| `scripts/access-audit.ts` | Queries Supabase-backed access state | Supabase client configuration and network |
| `scripts/assign.ts` | Assigns student work through app/Supabase helpers | Supabase client configuration and network; writes app data |
| `scripts/booking-link.ts` | Creates or inspects booking links | Supabase client configuration and network; may write booking state |
| `scripts/content-push.ts` | Pushes content to the app backend | Supabase client configuration and network; writes app data |
| `scripts/db-pull.mjs` | Pulls database content for local use | Supabase/database access and network; no direct env accessor was found in this file, so its credential source was not verified |
| `scripts/knowledge/ingest-lr-explanations.mjs` | Ingests or emits LR explanation data | `DATABASE_URL`; optional `DRY_RUN`, `EMIT_SQL`, `EMIT_SQL_DIR`, `SQL_CHUNK_BYTES`; database/network access unless only generating SQL |
| `scripts/knowledge/test-full-lifecycle.mjs` | Exercises a full application lifecycle | `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`, `EDGE_INTERNAL_KEY`; network and elevated access. Use only against a designated test environment |
| `scripts/knowledge/verify-integration.mjs` | Verifies admin and student integrations | `SUPABASE_URL`, `ADMIN_JWT`, `STUDENT_JWT`; network and test identities |
| `scripts/grade-census.ts` | Runs grading census/model work | Gemini API network access; `GEMINI_API_KEY` is used by grading Edge Functions, but this script's own direct credential source was not established in the static scan |
| `scripts/rrc-census.ts`, `scripts/rrc-mark-pause.ts`, `scripts/rrc-ungraded.ts` | RRC census and status operations | Supabase-backed data access; network. `rrc-mark-pause.ts` changes status |
| `scripts/student-work.ts` | Reads or manages student work | Supabase-backed data access and network; may write state depending on command |
| `scripts/test-booking-db.sh` | Runs booking database checks | Database/Supabase access and network; credential source was not verified in the script |
| `scripts/rc-recovery-pull.js` | Pulls LSAT Lab recovery data | `app.lsatlab.com` network access; browser login/session appears to be required. No env credential name found |
| `system/scripts/lsatlab-pull/crawl_public.py` | Crawls public LSAT Lab question pages | Public network access; no login needed according to the `lsat-lab-sync` skill |
| `system/scripts/lsatlab-pull/db_pull.py` | Pulls LSAT Lab database data into the vault | Network and the applicable LSAT Lab/database access; the skill describes this as read-only. Exact credential source was not found in the inspected skill text |

Some path groups above are summarized together because they serve the same operation family. The scripts were inspected statically, not executed. `scripts/knowledge/test-full-lifecycle.mjs`, content push, assignment, booking, and status scripts can write data. Keep them out of an unattended setup step.

## Supabase and Edge Functions

- Project ref: `atrcqxpmqrynmtvvyjju`.
- The repository notes identify it as a Lovable Cloud-managed backend, not a separately managed Supabase project.
- There are 321 SQL migration files under `supabase/migrations/`.
- There are 49 Edge Function directories containing `index.ts`; `_shared` is a helper directory and is excluded from that count. The folder names are:

  `activity-coach`, `activity-link`, `admin-manage-users`, `admin-tutor-corpus`, `analyze-stem-response`, `booking-commerce-webhook`, `booking-pass`, `booking-pass-admin`, `booking-upload`, `gcal-event-write`, `gcal-list-calendars`, `gcal-reconcile`, `gcal-smoke`, `gcal-sync-pull`, `gdrive`, `gemini-proxy`, `gmail`, `grade-rrc-section`, `handle-email-events`, `ingest-lsat-knowledge`, `ingest-session-note`, `inspect`, `mcp`, `mcp-scratch`, `memory-admin`, `motivation-engine`, `onboarding-intake-notify`, `parse-drill-request`, `parse-external-work`, `polish-message`, `preview-transactional-email`, `public-booking`, `retrieve-lsat-knowledge`, `scan-session-notes`, `send-assignment-email`, `send-section-report`, `single-session`, `single-session-outbox`, `single-session-sweeper`, `student-booking`, `study-chat`, `sweep-rrc-grading`, `synthesize-session-bundle`, `ta-agent`, `ta-chat`, `teacher-link-search`, `teacher-operator-chat`, `tutor-chat`, `voice-coach-respond`.
- Repo notes do not document an existing dedicated read-only database role or key available to an external cloud session. The publishable/anon key is not itself a read-only permission boundary. Supabase documentation says access depends on grants and RLS, while service-role/secret keys have elevated access. See [Securing your data](https://supabase.com/docs/guides/database/secure-data), [Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security), and [API keys](https://supabase.com/docs/guides/getting-started/api-keys).

### Recommended read-only access

Do not provide `SUPABASE_SERVICE_ROLE_KEY` or a production `DATABASE_URL` to a general-purpose coding session. No existing read-only role/key was found in the repo notes. Joshua can ask the Lovable Cloud project administrator to create a dedicated, least-privilege access path for the cloud session. Recommended steps:

1. In the Lovable Cloud project for ref `atrcqxpmqrynmtvvyjju`, use the SQL editor to create a dedicated database role or a separate authenticated test user. Do not reuse an owner or service role.
2. Grant only `CONNECT`, schema usage, and `SELECT` on the specific tables or read-only views the task needs. Revoke write privileges and ensure future tables do not receive broad default grants.
3. Review RLS policies for the chosen role and test that reads succeed while insert, update, delete, and function execution are denied.
4. Provide the session only the required connection/API endpoint and scoped credential through the cloud environment's secret manager. Never paste the credential into chat or commit it.
5. Rotate or revoke the credential when the work ends.

Lovable Cloud may limit direct external database connections. If it does not expose a safe scoped connection, use a read-only Edge Function or export prepared by Joshua instead. Joshua must perform this setup in the Lovable dashboard; this note does not create a role or key.

## Not available in a Claude Code cloud checkout

- The local `gws` CLI authentication in the Windows OS keyring and files under `~/.config/gws/`.
- Claude native memory stored on Joshua's local machine.
- `raw/data-about-me/` and other local raw data. These were not read or copied for this inventory.
- Joshua's active browser sessions, including any LSAT Lab login needed by authenticated recovery pulls.
- Local Windows-only tools and integrations, including Windows paths, PowerShell-only workflows, and locally installed app/Obsidian integrations. They must be installed or connected separately if a cloud task requires them.
- Lovable dashboard access and its managed SQL editor unless the cloud session is explicitly given access.

## Environment variable inventory

This is a name-only inventory. It includes app source, scripts, Edge Functions, configuration, and names present in `.env` or `.env.example`. A listed name is not a recommendation to add it to the cloud environment. The descriptions distinguish application configuration from credentials where possible.

| NAME | Read by | Purpose |
|---|---|---|
| `ADMIN_JWT` | Script | Admin test authorization in integration verification |
| `ALLOW_DRIFT` | Script | Content import behavior switch |
| `APP_BASE_URL` | Edge Function | Base URL for email links |
| `APP_ORIGIN` | Edge Function | Allowed application origin for booking flows |
| `BOOKING_ADMIN_EMAIL` | Edge Function | Booking admin identity/configuration |
| `BOOKING_IP_HMAC_KEY` | Edge Function | HMAC protection for booking IP data |
| `BOOKING_WORKER_SECRET` | Edge Function | Worker request authorization |
| `CI` | Test config | Continuous integration mode |
| `DATABASE_URL` | Script/config | Direct database connection |
| `DEBUG` | Script | Debug logging switch |
| `DEEPGRAM_API_KEY` | Edge Function | Deepgram API credential |
| `DEV` | Browser/Vite | Development mode flag |
| `DRY_RUN` | Script | Non-writing ingestion mode |
| `EDGE_INTERNAL_KEY` | Edge Function and script | Internal function authorization and lifecycle test credential |
| `EMIT_SQL` | Script | SQL emission switch |
| `EMIT_SQL_DIR` | Script | SQL output directory |
| `GEMINI_API_KEY` | Edge Function | Gemini API credential |
| `GITHUB_REPO` | Edge Function | Repository selector for inspection integration |
| `GITHUB_TOKEN` | Edge Function | GitHub API credential |
| `GMAIL_CLIENT_ID` | Edge Function | Gmail OAuth client identity |
| `GMAIL_CLIENT_SECRET` | Edge Function | Gmail OAuth secret |
| `GMAIL_REFRESH_TOKEN` | Edge Function | Gmail delegated access credential |
| `GOOGLE_CALENDAR_API_KEY` | Edge Function | Google Calendar API credential/configuration |
| `GOOGLE_CALENDAR_REFRESH_TOKEN` | Edge Function | Google Calendar delegated access credential |
| `GOOGLE_DRIVE_API_KEY` | Edge Function | Google Drive API credential/configuration |
| `GOOGLE_MAIL_API_KEY` | Edge Function | Gmail API credential/configuration |
| `GOOGLE_OAUTH_CLIENT_ID` | Edge Function | Google OAuth client identity |
| `GOOGLE_OAUTH_CLIENT_SECRET` | Edge Function | Google OAuth secret |
| `HOME` | Script | Operating system home path |
| `LOVABLE_API_KEY` | Edge Function | Lovable AI/runtime credential |
| `LOVABLE_DB_MIGRATION_URL` | Build/migration config | Database URL for Drizzle migration tooling |
| `LOVABLE_SEND_URL` | Edge Function | Transactional email service endpoint |
| `NODE_ENV` | Test config | Node runtime mode |
| `OUT` | Script | Local output path override |
| `PORT` | Vite/sample server | Local listening port |
| `SESSION_SYNTHESIS_MODEL` | Edge Function | Session synthesis model selection |
| `SQL_CHUNK_BYTES` | Script | SQL output chunk size |
| `STUDENT_JWT` | Script | Student test authorization in integration verification |
| `SUPABASE_ANON_KEY` | Edge Function/MCP helper | Supabase anonymous API key |
| `SUPABASE_PUBLISHABLE_KEY` | MCP helper | Supabase publishable API key |
| `SUPABASE_SERVICE_ROLE_KEY` | Edge Function, script, MCP helper | Elevated Supabase credential |
| `SUPABASE_URL` | Edge Function, script, MCP helper | Supabase API URL |
| `TA_AGENT_GEMINI_MODEL` | Edge Function | TA model selection |
| `VITE_BUILD_SHA` | Vite build config | Build revision label |
| `VITE_DEV_BYPASS_GATES` | Browser app | Local development gate bypass |
| `VITE_GOOGLE_API_KEY` | `.env.example` and browser integration configuration | Google API configuration; direct source use was not located by the static scan |
| `VITE_GOOGLE_CLIENT_ID` | `.env.example` and browser integration configuration | Google OAuth client identity; direct source use was not located by the static scan |
| `VITE_SUPABASE_PROJECT_ID` | `.env` and browser app | Supabase project identifier |
| `VITE_SUPABASE_PUBLISHABLE_KEY` | `.env` and browser app | Supabase public client key |
| `VITE_SUPABASE_URL` | `.env` and browser app | Supabase API URL |
| `VITE_TURNSTILE_SITE_KEY` | Browser app | Public Turnstile site key |

The scan is source-based, so dynamic lookups or third-party tools may read configuration not visible as a direct environment accessor. The local app `.env` was scanned for variable names only. Never print or copy its values.
