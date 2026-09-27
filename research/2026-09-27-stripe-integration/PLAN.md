# Stripe connection and teacher Home, 2026-09-27

## Verified connection state

- A read-only call using the locally stored `STRIPE_SECRET_KEY` returned HTTP 200 from `GET /v1/account` for `acct_1PJnXRIULVCj6rqq` and HTTP 200 from `GET /v1/payment_intents?limit=1`. No key or payment data was copied into this report.
- The live Stripe event destination points to LSAT U's `booking-commerce-webhook`. A completed Checkout event returned 200 on 2026-09-23. A completed Checkout event on 2026-09-21 had a 500 attempt and was marked recovered after retry. The precise exception behind that 500 still needs a Lovable Cloud log lookup.
- The Codex Stripe connector independently requires reauthentication. This does not invalidate the server API key or existing Stripe webhook.
- The current webhook handles booking Checkout completion/expiration and refunds. It is not a complete transaction feed. The teacher's `/classroom` Home is still the student Home.
- A fresh Stripe Dashboard view on 2026-09-27 showed the destination subscribed to 15 event types: eight `charge.*` and `charge.dispute.*` types, two asynchronous Checkout outcomes, `checkout.session.completed`, `checkout.session.expired`, and three `refund.*` types. The current handler processes only the final five and returns success for the other ten. An older open tab still showed five, so use the fresh 15-event view as the current setting and recheck before changing subscriptions.
- Stripe Account status showed an unstarted business-liquidity information request for a routine credit review. Payments and payouts were active; Cartes Bancaires payments were paused. This is an account status matter separate from webhook delivery.

## Fastest implementation path

1. Inspect the 2026-09-21 Lovable Cloud function error and fix its cause. Keep existing destination in place while adding coverage.
2. Create a dedicated, signed Stripe event ingest with an append-only event inbox, event-ID deduplication, processing status, and an exception queue. Add only the Stripe events needed for the actual payment channels. Keep the existing booking processing intact until the new ledger is reconciled.
3. Normalize Checkout Sessions, PaymentIntents, invoices, charges, refunds, and disputes to one payment activity record per underlying transaction. Store Stripe object IDs, UTC timestamps, amount/currency, customer, payment status, and provenance. Display failed and pending events as such; do not label them paid.
4. Use server-side Stripe API reads and cursor pagination to backfill the 3 months before activation. Read historical activity first; do not automatically grant old sessions or access. Reconcile the count and totals against Stripe and flag missing/ambiguous records.
5. Match future payments using an internal student ID in Checkout `client_reference_id` or metadata, then Stripe customer ID, with verified email as a fallback. Put ambiguous payments in the teacher exception queue for review.
6. Route teacher/admin Home to a teacher dashboard showing new payments, bookings, package balances, exceptions, webhook health, and searchable payment history. Keep the student study Home for students.
7. Test in Stripe sandbox, deploy through Lovable Cloud, add the required events to the existing live Stripe destination, then verify a new payment, refund, replay, duplicate event, and 3-month reconciliation in production.

## Stripe-side configuration

- The existing webhook signing secret and server API key are present in configuration; verify their Lovable Cloud secret values without exposing them.
- Create a restricted **read** key for the activity/backfill reader with only the resources it needs. Keep any write authority in a separate server-side key. The webhook signing secret is separate from API keys.
- Add the new event types to the existing live destination only when its receiver is ready. Stripe may deliver out of order and retry failed deliveries, so ingestion must be idempotent.
- The Codex Stripe connector can be reauthenticated separately to make administrative inspection easier. It is not required for LSAT U runtime payments.

## Current blockers and decisions

- The old decision that booking passes are the sole source of sessions owed conflicts with automatic package entitlement grants. Supersede it explicitly before enabling grants.
- Decide whether unmatched payers and unrelated Stripe payments appear only in the teacher ledger or also receive student access. Default: show every transaction, grant nothing without a confirmed product and student match.
- Lovable Cloud deployment requires confirmation of that route. Any Lovable action that may spend credits requires a separate confirmation immediately before the action.

## Stripe documentation

- [Webhooks](https://docs.stripe.com/webhooks)
- [Event types](https://docs.stripe.com/api/events/types)
- [API keys and webhook secrets](https://docs.stripe.com/keys)
- [Restricted API keys](https://docs.stripe.com/keys/restricted-api-keys)
- [PaymentIntent listing and pagination](https://docs.stripe.com/api/payment_intents/list)
- [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions)
- [Refund listing](https://docs.stripe.com/api/refunds/list)
