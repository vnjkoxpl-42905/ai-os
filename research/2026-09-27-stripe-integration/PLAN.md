# Stripe connection and teacher Home, 2026-09-27

## Goal and definition of done

LSAT U uses the existing authenticated live Stripe account as its source of payment truth. Every new Stripe financial event is visible to Joshua on a teacher-specific Home within seconds of normal webhook delivery, with its actual status and a link to the underlying Stripe record. The previous three months are searchable. The ledger reconciles against Stripe, never counts one sale twice, and makes failed or unmatched processing visible. Only recognized session/package payments can enable platform access; package booking passes require Joshua's one-click approval.

“Full capability” means complete visibility and the approved downstream actions. It does not mean an unrestricted API key or automatically granting a benefit for every charge.

## Verified connection state

- A read-only call using the locally stored `STRIPE_SECRET_KEY` returned HTTP 200 from `GET /v1/account` for `acct_1PJnXRIULVCj6rqq` and HTTP 200 from `GET /v1/payment_intents?limit=1`. No key or payment data was copied into this report.
- The live Stripe event destination points to LSAT U's `booking-commerce-webhook`. A completed Checkout event returned 200 on 2026-09-23. A completed Checkout event on 2026-09-21 had a 500 attempt and was marked recovered after retry. The precise exception behind that 500 still needs a Lovable Cloud log lookup.
- The Codex Stripe connector independently requires reauthentication. This does not invalidate the server API key or existing Stripe webhook.
- The current webhook handles booking Checkout completion/expiration and refunds. It is not a complete transaction feed. The teacher's `/classroom` Home is still the student Home.
- A fresh Stripe Dashboard view on 2026-09-27 showed the destination subscribed to 15 event types: eight `charge.*` and `charge.dispute.*` types, two asynchronous Checkout outcomes, `checkout.session.completed`, `checkout.session.expired`, and three `refund.*` types. The current handler processes only the final five and returns success for the other ten. An older open tab still showed five, so use the fresh 15-event view as the current setting and recheck before changing subscriptions.
- Stripe Account status showed an unstarted business-liquidity information request for a routine credit review. Payments and payouts were active; Cartes Bancaires payments were paused. This is an account status matter separate from webhook delivery.

## Fastest implementation path

1. **Baseline and repair.** Read the Lovable Cloud log for the 2026-09-21 recovered 500. Inventory the live destination, payment channels, product/payment links, and current secret scopes. Reconcile that event against the resulting booking/pass state. Do not replace the working booking path blindly.
2. **Durable ingest.** Add a signature-verified Stripe receiver and an event inbox keyed by Stripe event ID. Persist receipt and processing state before responding. Process asynchronously, with retries, dead-letter/exception visibility, and idempotent updates. Keep webhook responses fast. Record every subscribed type or deliberately mark it ignored with a reason; never return 200 for a relevant event without traceability.
3. **Canonical financial ledger.** Normalize Checkout Sessions, PaymentIntents/charges, invoices/subscriptions, refunds, disputes, balance transactions, fees, and payouts into linked records. Use underlying object IDs to deduplicate one payment represented by several events. Track gross amount, refund, fee/net where available, currency, status, source object, timestamps, payer identity, and product classification. Keep customer-facing payment events distinct from internal balance movements so totals are not double-counted.
4. **Coverage.** Handle the ten currently subscribed event types that the existing booking function ignores, especially delayed Checkout outcomes and charge/dispute changes. After the receiver is ready, add only the missing event types required for actual invoice, subscription, PaymentIntent, payout, or balance flows. Audit active Stripe products and payment methods before choosing subscriptions. Do not subscribe to `*` merely to claim broad coverage.
5. **Three-month backfill.** Read Stripe objects with a server-side read key, created-time filters, and cursor pagination for the three months before activation. Import historical activity as ledger records without retroactive pass/access grants. Run reconciliation against Stripe totals and identify gaps/ambiguous records. Continue periodic reconciliation after launch to recover missed webhooks.
6. **Identity and actions.** Put the LSAT U user ID and offer/booking ID in new Checkout `client_reference_id` or metadata; save Stripe customer ID when available. For old Payment Links, use the mapped link and verified email as fallback. Unmatched payments go to a teacher review queue. Recognized session/package payments can enable platform access; package purchases create a proposed “Grant N passes” action that Joshua confirms once. All other charges are logged only. This follows the locked 2026-09-27 decision.
7. **Teacher Home.** Route teacher/admin `/classroom` to a separate Home. Lead with new money and exceptions, then upcoming sessions and actions. Show searchable history with filters for date, payer/student, product, type, status, and amount. Each row shows source, matching confidence, and the next action. Keep student Home unchanged.
8. **Rollout and proof.** Exercise new payments, delayed success/failure, refunds, partial refunds, disputes, unmatched payers, duplicate and out-of-order events, retries, package approval, and three-month import in Stripe sandbox. Deploy Lovable Cloud functions through the confirmed Lovable path. Change live event subscriptions only after the receiver is ready. Verify a production payment appears on teacher Home and reconcile the imported range against Stripe.

## Acceptance checks

- A new Stripe payment or status change appears on teacher Home within one minute of normal webhook delivery; any processing delay or failure is visible.
- Every Stripe activity record in the selected three-month period is searchable, with no duplicate sale rows or duplicate booking actions. Exceptions are counted and reviewable.
- A payment with no confident student/offer match never grants access or passes. A recognized package presents one approval action and cannot be granted twice.
- Payments, refunds, disputes, payouts, and fees remain distinguishable. Stripe remains the authority if totals disagree.
- Only teacher/admin roles can see financial activity. Stripe keys and signing secrets stay server-side; no card details are stored in the teacher ledger.

## Stripe-side configuration

- The existing webhook signing secret and server API key are present in configuration; verify their Lovable Cloud secret values without exposing them.
- Create a restricted **read** key for the activity/backfill reader with only the resources it needs. Keep any write authority in a separate server-side key. The webhook signing secret is separate from API keys.
- Add the new event types to the existing live destination only when its receiver is ready. Stripe may deliver out of order and retry failed deliveries, so ingestion must be idempotent.
- The Codex Stripe connector can be reauthenticated separately to make administrative inspection easier. It is not required for LSAT U runtime payments.

## Current blockers and decisions

- The 2026-09-27 decision in `decisions/log.md` resolves the entitlement rules: package passes need teacher confirmation, unmatched payers wait for review, and unrelated charges are logged without access. Do not ask Joshua to decide these again.
- The exact three-month cutoff is tied to the actual import/activation date. Three months is the working scope from Joshua's request.
- Lovable Cloud deployment requires confirmation of that route. Any Lovable action that may spend credits requires a separate confirmation immediately before the action.

## Stripe documentation

- [Webhooks](https://docs.stripe.com/webhooks)
- [Event types](https://docs.stripe.com/api/events/types)
- [API keys and webhook secrets](https://docs.stripe.com/keys)
- [Restricted API keys](https://docs.stripe.com/keys/restricted-api-keys)
- [PaymentIntent listing and pagination](https://docs.stripe.com/api/payment_intents/list)
- [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions)
- [Refund listing](https://docs.stripe.com/api/refunds/list)
