# Architecture summary (Cloudflare security-audit skill, quick profile)

Recon note: the four Phase 1 research agents were launched but terminated on an API rate limit before returning. Under the coordinator's 2-3 agent cap after the reset, the parent performed reconnaissance directly from source. This is a deviation from the skill and is disclosed in REPORT.md.

## 1. Product, principals, protected resources
LSAT U (lsatprep.study): LSAT tutoring platform. Principals: anonymous web visitor; authenticated student (Supabase Auth); admin/teacher (role in a roles table, checked by SQL helper functions); scheduled workers holding a shared worker secret; external webhook senders (Stripe, Cal.com, Lovable email); MCP clients holding a Supabase OAuth token; LLM tool-calling agents running inside edge functions. Protected resources: student profiles and PII, homework and attempt history, session notes and transcripts, booking passes and payment ledger, admin operations (user management, email/Gmail/Drive/Calendar access), LLM spend.

## 2. Comparable baseline
Standard Supabase SaaS: browser talks to PostgREST with the anon key and a user JWT, so Row Level Security is the primary authorization boundary; edge functions with the service-role key bypass RLS and must authorize callers themselves.

## 3. Stack and deployment
React + Vite + TypeScript client (src/). Supabase Postgres with 344 migrations (supabase/migrations). Deno edge functions (supabase/functions, about 50). Deployed through Lovable Cloud; supabase/config.toml lists per-function verify_jwt. No offline sandbox; source-only.

## 4. Entry surfaces
- PostgREST table and RPC access with anon key or user JWT (supabase/migrations).
- Storage buckets and storage.objects policies (supabase/migrations).
- Edge functions with verify_jwt=false (supabase/config.toml): public-booking, booking-upload, preview-transactional-email, gemini-proxy, gcal-sync-pull, gcal-reconcile, booking-pass (retired, 410), booking-commerce-webhook (Stripe and Cal.com signatures), single-session (Turnstile), single-session-sweeper, single-session-outbox, sweep-rrc-grading (worker secret), mcp (OAuth issuer via @lovable.dev/mcp-js; src/lib/mcp).
- Edge functions with default verify_jwt=true that use SUPABASE_SERVICE_ROLE_KEY: admin-manage-users, gmail, gdrive, gcal-*, memory-admin, admin-tutor-corpus, booking-pass-admin, send-assignment-email, send-section-report, teacher-operator-chat, ta-agent, tutor-chat, etc.
- LLM functions with tools: ta-agent, ta-chat, teacher-operator-chat, tutor-chat, study-chat, activity-coach, gemini-proxy.
- Client HTML rendering sinks and client-side admin gating in src/.

## 5. Trust boundaries
RLS policies and SECURITY DEFINER functions (role helper functions, search_path); service-role edge functions' own caller checks; webhook signature verification; worker shared secret comparison; Turnstile on public booking; LLM tool dispatch authority.

## 6. Starting paths
supabase/config.toml, supabase/migrations/, supabase/functions/_shared/, supabase/functions/*/index.ts, src/lib/mcp/, src/integrations/supabase/, src/contexts/, src/components/ (admin routes and HTML sinks).

## 7. Prior coverage
No prior run.

## 8. Companion selection
ATTACK-CLASSES.md (Access control, Cryptography and secrets, Business logic, Feature abuse and data leakage, Injection); DATA-ISOLATION-AND-LIFECYCLE.md (RLS owner enforcement, storage); WEB-PROTOCOL-AND-AUTH.md (JWT verification, API-key scope); PROTOCOLS-RPC-AND-MESSAGING.md (webhooks, duplicate delivery); AI-AND-LLM.md (tool authority); CLIENT-SIDE.md (DOM XSS). Not selected: MEMORY-SAFETY (no native code), DESKTOP-MOBILE (no native app), CLOUD-AND-DEPLOYMENT (no IaC in repo beyond config.toml, covered under the function unit), SUPPLY-CHAIN (out of scope for this quick pass), RESOURCE-EXHAUSTION (no availability testing allowed).
