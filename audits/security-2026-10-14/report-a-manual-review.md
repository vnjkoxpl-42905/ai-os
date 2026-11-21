# LSAT U security pass, manual review (2026-10-14)

Claude Security was not run: it needs the Workflow tool and writes a report folder into the target repo. This is a manual review covering RLS, edge functions, Stripe webhooks, secrets and client-side admin checks. Findings 1, 4 and 6 were missed here; see the Cloudflare report. Every finding is from source reading only and needs its read-only SQL check before it counts as live.

## Findings (merged from both tools)

| # | Severity if live | Finding | Where | Read-only check |
|---|---|---|---|---|
| 1 | High | `set_booking_availability_overrides` callable by anon with no admin check; deletes all future overrides and inserts caller rows. Sibling booking functions have public EXECUTE revoked; this one does not. | `supabase/migrations/20260911000000_booking_policy_mirrors_calcom.sql:148` (write at :168) | `select has_function_privilege('anon','public.set_booking_availability_overrides(jsonb)','EXECUTE');` |
| 2 | High | Student can set own `students.class_id` to another student's; 45 legacy policies use `get_user_class_id`, exposing victim attempts, sessions, journal, profile (incl. `lsat_accommodation`) and allowing writes as victim. | `20260406153113_...sql:9-10`, `20260329000000_fix_class_id_fallback.sql:13`, `20251022025825_...sql:24,27,35,41` | `select has_column_privilege('authenticated','public.students','class_id','UPDATE');` |
| 3 | Medium-High | New signup can INSERT own `profiles` row with all paid flags and `access_tier='tier_1'`; guard trigger is UPDATE-only and no server trigger creates the row first. | `20260406153113_...sql:23`, `20260511172245_...sql:34`, `src/components/classroom/OrientationCard.tsx:347` | `select tgname from pg_trigger where tgrelid='auth.users'::regclass;` plus INSERT grant on `profiles` |
| 4 | Medium-High | Student can move own `conversation_participants` row into any conversation and read its messages/attachments; `conversations` UPDATE policy lacks WITH CHECK. | `20260416234013_...sql:99,49,105,173`; policy at :77 | UPDATE privilege on `conversation_participants.conversation_id` |
| 5 | Medium | Booking pass links to any account with matching email; if unconfirmed emails can sign in, an attacker registers a paying student's email and takes their sessions. | `supabase/functions/student-booking/index.ts:38-42`, `_shared/linkPassToAccount.ts` | Lovable Cloud Auth: is "Confirm email" on? |
| 6 | Medium | Anonymous single-session booking prices by typed email; anyone knowing a discounted student's email gets their rate, and the response reveals which emails have discounts. | `supabase/functions/single-session/index.ts:395-403`, `20260830010000_booking_event_types.sql:90` | Rows in `booking_price_overrides` below default |
| 7 | Medium | Paid content gated only client-side; any signed-in account can read full LR/RC banks, explanations and answer keys. | `20260803020348_...sql:108-109`, answer key column :40 | Is signup open? |

Findings 2 and 4 require the victim's user id or conversation id; no exposure path for those was found.

Smaller: `get_or_create_personal_plan(uuid)` callable by anyone; three non-constant-time secret compares (`booking-upload`, `gcal-reconcile`, `preview-transactional-email`); `public-booking` and `booking-upload` rate-limit on a client-controlled header; `supabase/functions/mcp/index.ts` has an uncommitted Vite rebundle with a `C:\` import path that must not be committed.

## Checked and clean
- Stripe webhook verified on raw body, dedicated secret, 300 s tolerance; Cal.com HMAC constant-time; duplicate payment events cannot double-grant.
- Worker-secret/signature checks fail closed when the secret is missing.
- Admin edge functions check admin role before using the service-role key.
- `has_role` and `user_roles` sound.
- No committed secrets (`.env` holds only the public anon key; Google key is a browser key).
- User, Gmail and TA HTML sanitized with DOMPurify.
- All storage buckets private.
