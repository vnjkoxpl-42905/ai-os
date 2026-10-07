# Celia's payment waited for teacher approval by design

Investigated 2026-10-02 through direct authenticated Stripe API reads, authenticated LSAT U admin reads, a safe unsigned endpoint probe, and the local app source. No payment event was replayed and no app code was changed.

## Verified payment and manual restoration

- Student: Celia, `celiacutler@gmail.com`, account `749e2eae-7969-464f-bf96-a4d4cfafe2bf`.
- Completed payment: USD 200.00, live mode, at `2026-10-01T23:39:21Z` (2026-10-01 19:39:21 America/Toronto).
- Event: `evt_1ULtZOIULVCj6rqqOYGA3CEa`.
- Checkout: `cs_live_a1uWZ6oEgv2q3RdBlE51zR8EUSiWB9ygxH2nlZs1oqfv8wAwG6tLxcQpek`.
- Payment intent: `pi_3ULtZLIULVCj6rqq0akU648V`.
- Payment link: `plink_1STvqYIULVCj6rqqJb70Prhb`. This matches active live offer `package-5`, worth five credits.
- Checkout email matches her account exactly. Current payment-link line-item total is also USD 200.00. Checkout has no discount, shipping, or tax adjustment.
- Parent agent independently restored and verified active pass `014de9d0-5d10-45da-80be-483c01aaba35`, created `2026-10-02T17:18:47Z`, five total and zero used. Earlier ten-credit pass remains exhausted.

## What the evidence rules out

Stripe endpoint `we_1U9Sw2IULVCj6rqqkkoe7Isw` is enabled and targets `https://atrcqxpmqrynmtvvyjju.supabase.co/functions/v1/booking-commerce-webhook?provider=stripe`. It subscribes to `checkout.session.completed`, among other events.

An unsigned POST with body `{}` returned HTTP 400 `invalid_signature`, confirming the function is reachable without a JWT and performs signature validation. This does not test valid-signature delivery.

The payment event reports zero pending webhooks. This means no outstanding deliveries, not proof of successful crediting. The parent subsequently inspected Stripe delivery `wc_1ULtZQIULVCj6rqqkFdSHw5H` at `2026-10-01 19:39:24 America/Toronto`: HTTP 200, response `{received:true,student_id:'749e2eae-7969-464f-bf96-a4d4cfafe2bf',grant:'awaiting_teacher'}`. Payment receipt and student matching succeeded. The deployed package branch deliberately stops before granting credits.

Direct authenticated admin REST independently confirmed live `stripe_payments` row `bb89e821-778f-4ae8-bdc7-7a42478d5bda`, charge `ch_3ULtZLIULVCj6rqq0wLbrlFN`, status `succeeded`, match_state `matched`, offer `package-5`, grant_state `awaiting`, source `webhook`. That is the verified cause of the missing sessions.

## The checkout examined first was stale

The working checkout is on `feat/calendar-strip-deeplink`, with existing unrelated edits. Its visible webhook called `apply_booking_package_payment`; this was older code than the deployed system. That initially made the case look unexplained. Git history corrected the diagnosis: commit `215936574186be9a38ed302323d54284c93b4f8a`, titled "Stripe payments ledger on Today: 90-day sync, grant confirmation, review queue", contains the exact `awaiting_teacher` response.

That commit explicitly implements `decisions/log.md`, 2026-09-27: recognized package payments wait for Joshua to click "Grant N passes" on teacher Home. The live response and live ledger match that implementation. There is no configuration flag to enable automatic package grants in this version. Joshua's current request asks to reconsider this deliberate prior policy.

`../ai-os-projects/lsatu/supabase/migrations/20260819075740_aaf80471-b8b9-452a-8713-02cc380f7608.sql` defines that RPC. It increments the newest pass or inserts one and records a `paid` commerce event in the same transaction. Event ID is its idempotency boundary. Its authenticated execution grant was subsequently revoked; admin JWT cannot invoke it directly.

Local gaps:

- Unknown payment links return HTTP 200 with `ignored: unknown_payment_link`, without a durable diagnostic record.
- Unmatched email creates `unmatched_paid` and returns HTTP 200 pending, but no package reconciliation worker exists locally.
- `checkout.session.async_payment_succeeded` is subscribed but ignored by the handler; a delayed successful payment would not receive credits.
- Successful package ledger records omit checkout session, amount, and currency despite schema support, which limits diagnosis and reconciliation.
- Admins have no visible commerce-ledger policy in the inspected migrations, making the existing REST read uninformative.
- Validation uses the payment link's current price/active state rather than the purchase-time facts, so later price changes or link deactivation can reject a valid purchase replay.

## Reconcile the manual grant before enabling automatic grants

The manual pass's notes now contain the exact event, intent, charge, ledger ID, amount, payment date, and an explicit statement that this pass fulfills the purchase. This was written through `booking-pass-admin` action `update`, then independently reread. Five total, zero used, and active status remained unchanged.

The newer migration `20260927090000_stripe_payments_ledger.sql` provides `admin_dismiss_stripe_payment(_payment_id uuid)`. Following parent authorization and a conditional preread of the exact intent, charge, and awaiting state, this investigation invoked it for Celia's ledger row. An independent reread confirmed `grant_state: dismissed`, `match_state: matched`, and the manual pass still active with five total and zero used; notes remained present. This clears the already handled purchase from the grant queue while preserving its payment record. `dismissed` is not a formal `granted` fulfillment record. **Do not call `admin_grant_stripe_payment` now**: it would add another five sessions. Its current implementation protects `granted` rows but does not reject `dismissed` rows, so future automatic grants must explicitly skip dismissed rows.

Minimal policy change: preserve the existing Stripe ledger and teacher review for unmatched or unknown purchases; after successful live-mode, paid-status, known-package, price/currency, and exact account matching checks, invoke a service-role-only transactional grant function keyed by the existing Stripe payment row. It must lock the payment row, only accept `awaiting`, grant exactly once, and preserve `dismissed`/`granted` decisions. Use this shared transaction for both automatic and teacher-confirmed grants, with a separate admin-authorized reconciliation operation that can mark an existing manual pass as fulfilling a payment without changing its balance. Handle delayed payment success using the same checks. Update the prior decision explicitly when the new policy is approved, and deploy through the approved Lovable route.

Meaningful verification should cover duplicate event delivery, manual fulfillment followed by delayed retry, unmatched email resolved after signup, unknown link remediation, delayed payment success, price changes after purchase, and transactional rollback when credit or receipt persistence fails. These changes involve Edge Functions/database work and require the approved Lovable deployment route before being called live.

## Automatic crediting implementation prepared on 2026-10-02

Joshua explicitly authorized the focused Lovable deployment and minimal credit spend. Isolated app checkout: `C:/Users/Joshu/dev/ai-os-projects/lsatu-auto-credits`. Local commit `726ca50` changes only six backend/test/runbook files. New validated Checkout completions and async success events call a service-role-only atomic grant RPC. Existing payment rows default `auto_grant_eligible=false`, protecting historical and manually handled payments. New live rows preserve their eligibility during charge-first/delayed event sequencing; terminal grant states are never overwritten by refresh. Both automatic and admin grants share a locked transaction. The migration fixes first-pass creation's required creator/token fields. No student communication or tier changes.

Local evidence: nine Deno payment-ledger regressions passed, webhook Deno check passed, application typecheck passed, full production build passed, 769-file canonical-content exclusion passed. Independent code review found two issues (historical awaiting replay and partial ledger-write retry recovery); both were addressed and re-reviewed with no remaining material finding. Existing build warnings were unchanged. Backend SQL smoke checks remain pending until Lovable applies the migration. Stripe's enabled endpoint already subscribes to both Checkout completed and async payment success.

Planned paid Lovable work is one standard deployment-only prompt, with Max mode disabled. It will apply the committed migration, deploy the one webhook function, and execute the synthetic SQL verification transaction with rollback. No historical backfill or real payment will be created. Celia's actual Stripe event may be replayed only after those checks, to verify the deployed dismissal guard and unchanged five-session balance.

The implementation was pushed to GitHub main via the typecheck-gated safe-push script as `726ca5011e966c4a33abda6b8177ff585c479603`. Lovable get_project confirmed that exact commit synced before the deployment request. Submitted one standard-mode deployment-only request, Max disabled, message `umsg_01m3yxp6nyey2axkffw470tzjm`, thread `main`, project `53b9a6f2-aba7-4ae4-8dd1-fa5b8aab4d76`. Deployment and database verification remain pending at this point.

## Deployed and independently verified

Lovable's completed response applied the migration as `drizzle/migrations/0027_automatic_stripe_package_credits.sql` and deployed only `booking-commerce-webhook`. The SQL verification executed with its BEGIN/ROLLBACK intact and no assertion error. The SQL tool does not expose NOTICE output, so the literal pass notice was not captured; its successful completion plus the follow-up zero fixture counts are the remote evidence. It reported zero smoke offers, charges, or synthetic auth users remaining. One standard request cost **3.1 credits**. Lovable reported automatic generated-type/migration-record edits in snapshot `ecb98736c90b86379ce75aa443bc3959d5d59eae`; a concurrent bank update moved GitHub/Lovable main to `1071efe48621cf1d0cc21d2af8a13f18a4310745`. Independent Git comparison confirms the deployed webhook, shared helper, and prepared canonical migration are unchanged from tested `726ca50`; the remote branch's only delta from that commit is an unrelated question-bank correction. No additional Lovable request was made.

Independent production verification used the existing admin credentials and unchanged original Stripe event, fetched from Stripe's live API, signed with the existing webhook credential, and posted to the configured live endpoint. Prereads required Celia's payment to remain dismissed with auto_grant_eligible=false and her manual pass to remain active with five total credits. The deployed endpoint returned HTTP 200 with `{received:true,student_id:749e2eae-7969-464f-bf96-a4d4cfafe2bf,grant:dismissed}`. Fresh after-reads confirmed the payment remains dismissed and both passes, their balances, statuses, and notes are byte-for-byte unchanged. Her new pass is still five total, zero used, active. No charge, historical batch grant, or student communication was made.

Automatic crediting is enabled for new confidently matched, validated package Checkout payments, including delayed successes. Unknown/unmatched and historical purchases remain review cases. No new paid purchase was created for testing; positive fulfillment was verified by the rollback-only live database fixture, while the real webhook replay verified the deployed path and manual-fulfillment protection. Frontend publication was not needed for this server-only change.
