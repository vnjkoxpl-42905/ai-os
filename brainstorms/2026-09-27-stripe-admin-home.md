# Stripe integration and admin Home: Brainstorm / Discovery Notes
Date: 2026-09-27 · Goal: Define a complete Stripe-to-LSAT U payment workflow and a teacher-specific admin Home, grounded in the current platform.
Status: in progress
Context sources: `context/work.md`; `decisions/log.md`; `brainstorms/2026-07-19-booking-admin-redesign.md`; `brainstorms/2026-09-23-classroom-home-PLAN.md`; `brainstorms/2026-09-24-lsatu-fit-one-screen.md`; LSAT U code audit in progress.

## Summary / key decisions
- Joshua confirmed on 2026-09-27: every Stripe transaction received should appear automatically on his teacher Home. The Stripe connection is the first design priority; a distinct teacher Home redesign follows. He wants the connection authenticated, immediate, and able to support the actions tied to each payment.
- Joshua answered Q5 on 2026-09-27: show all new activity and backfill it as searchable history, with the past three months as his tentative starting window. At the current date that would begin around 2026-06-27; use the actual activation date for the final import cutoff. New activity continues after the backfill.
- Existing business context: Stripe handles packages; Cal.com is Stripe-linked for paid individual sessions; rare e-transfers exist. Confirmed payment triggers onboarding. A 2026-07-20 decision made booking passes the sole record of sessions owed and explicitly chose no Stripe-to-pass reconciliation. The requested automation may supersede that decision, pending Joshua's answer.
- Recommendations and technical findings will be kept separate from Joshua-confirmed decisions.
- Verified live on `https://lsatprep.study/classroom` in Joshua's signed-in Teacher account on 2026-09-27: the page shows “Nothing is due today. Drill whatever you feel like,” Smart Drill, Timed section, and a student-style Next seven days strip. It shows no payment feed.
- Code audit: `/classroom` renders the student `ClassroomHome` for teachers too. A separate `/teacher/today` exists, but its work queue has no payment source. The Stripe webhook currently handles specific booking/payment-link flows; it does not build a universal Stripe transaction ledger, and the current booking events are sparse. These are repository findings, not a live Stripe reconciliation.
- Code audit: generic invoices, subscriptions, direct Payment Intents, manual Dashboard charges, and unknown payment links are not covered by the current webhook. The Checkout handler currently grants feature access before product classification; this requires a guarded fix before broadening event ingestion. The existing email matching has no durable Stripe customer ID mapping. A live endpoint/deployment check remains necessary.
- Live Stripe account verification attempted 2026-09-27 through the connected Stripe app; the app requires reauthentication. Do not treat repository configuration as proof of live account coverage.
- Live Stripe Dashboard checked 2026-09-27 in the signed-in Aspiring Attorneys account. One active account event destination points to `https://atrcqxpmqrynmtvvyjju.supabase.co/functions/v1/booking-commerce-webhook?provider=stripe`, described as LSAT U booking commerce for packages and single sessions. It listens to five events. Stripe shows 12 deliveries and 3 failed attempts for the dashboard's “This week” view. At least one `checkout.session.completed` attempt returned HTTP 500 with `provider_processing_failed` and was later marked “Delivery recovered,” so failed attempts must not be misreported as permanently lost payments. A 2026-09-23 `checkout.session.completed` returned HTTP 200 with `status: booked`, confirming that one native booking completed end to end. The signing secret was masked; no secret was read or copied. The live status of every payment remains unverified.
- Stripe Dashboard account status has one active task, “Provide information about your business liquidity.” It lists Payments and Payouts as active, with Cartes Bancaires payments paused. This is an account-status task, not evidence that LSAT U's webhook is disconnected. Joshua may need to provide the business information in Stripe; no form was submitted.
- Codex's separate Stripe connector still reports “requires reauthentication” after the Dashboard opened successfully. Dashboard sign-in and the Codex connector are distinct. LSAT U's server-side API key permissions and current environment remain unverified.

## Technical recommendation (tentative, not approved)
1. Correct the current webhook so payment classification and live-mode checks precede any student access grant. Preserve the existing native single-session path while broadening account coverage.
2. Receive signed Stripe events server-side and persist each event ID once. Normalize related Checkout, PaymentIntent, charge, invoice, refund, and dispute events to a single payment record per underlying transaction, so one sale cannot create several grants. Track event receipt and processing separately, with retries and an error queue. Stripe's webhook guide: https://docs.stripe.com/webhooks.
3. Backfill Stripe history through authenticated API reads if Joshua confirms history scope. Reconcile regularly against Stripe because webhooks alone can be missed or delayed. Keep secrets server-side; grant only the API permissions required for verified reads and approved actions. Stripe key guide: https://docs.stripe.com/keys.
4. Map Stripe customer IDs and payment metadata to LSAT U users. Show unmatched or ambiguous money on admin Home immediately, while holding any access change until the identity and offer are verified, subject to Joshua's answer.
5. Drive package passes, single-session booking status, onboarding, and exceptions from the canonical payment state. Make every downstream action idempotent and auditable. The precise action rules remain Joshua's decision.
6. Feed a distinct teacher Home from the payment ledger, teacher schedule, messages, and work queue. Students retain the student Home. Confirm the section order with Joshua.

## Q&A log

### Round 1
#### Q1 - Payment coverage
- Asked: whether all successful Stripe payments, including unknown or historical ones, should appear on the admin Home.
- Recommended: show all account payments, queue unknown matches for review, and grant access only after buyer and product verification.
- Captured: “any transaction that happens, or anything I get, should automatically go to my teacher's homepage.” All new Stripe account transactions should be visible. The original historical-backfill gap is superseded by Q5.
- Flags: non-payment Stripe events -> Joshua; historical depth is now tentatively three months (Q5).

#### Q2 - Package booking passes
- Asked: whether package payments should automatically create or top up a booking pass, superseding the 2026-07-20 manual-pass decision.
- Recommended: automate verified package passes with duplicate protection and an exception queue.
- Captured: no direct answer yet. Joshua reiterated that a payment should automatically have an appropriate action.
- Flags: exact package entitlement action -> Joshua.

#### Q3 - Ambiguous payer identity
- Asked: what to do when a payer does not clearly match one LSAT U account.
- Recommended: show Needs matching immediately and wait for review before access or credits change.
- Captured: no direct answer yet.
- Flags: identity matching policy -> Joshua.

#### Q4 - Teacher Home shape
- Asked: whether Teacher gets a distinct dashboard, with a priority among payments, sessions, and work.
- Recommended: teacher-specific Home, with students keeping their current Home.
- Captured: “Teacher's homepage should be very different because right now it makes no sense.” Joshua wants Stripe connection first, then the teacher Home redesign. He did not rank the Home sections beyond requiring automatic transaction visibility.
- Flags: Home content and ordering -> Joshua.

### Round 2 (partial answer received)
#### Q5 - New activity and history
- Asked: show every new payment, refund and dispute, and whether to import older activity; recommended all new financial activity plus searchable history, with payouts and fees in a financial view.
- Recommended: all new financial activity plus a searchable historical backfill.
- Captured: “show all new activity and back fil it as searchable history and maybe for m past 3 months.” The three-month depth is tentative (“maybe”).
- Flags: whether “all new activity” includes payouts and fees, or only payment-related activity -> Joshua. Exact historical cutoff -> confirm before import.

#### Q6 - Package pass automation
- Asked: automatic booking pass versus task versus manual grant.
- Recommended: one automatic pass grant per verified purchase.
- Captured: awaiting answer.

#### Q7 - Ambiguous payer identity
- Asked: show payment immediately and hold access versus automatic email match or immediate grant.
- Recommended: show and hold access pending review.
- Captured: awaiting answer.

#### Q8 - Connection permission scope
- Asked: full Stripe visibility with scoped server-side actions versus unrestricted Stripe write access or visibility only.
- Recommended: full visibility and only the permissions needed for approved actions.
- Captured: awaiting answer.

## Open flags (pending input)
- Three-month historical backfill depth is tentative; confirm final cutoff before import -> Joshua.
- Whether payouts and fees belong in “all new activity” -> Joshua.
- Exact action for each verified payment type -> Joshua.
- Admin Home priorities beyond payment activity -> Joshua.
- Whether to supersede the 2026-07-20 booking-pass decision -> Joshua.
- Meaning of “maximum amount of permissions” for the platform connection -> Joshua; recommend the smallest server-side permissions that still cover every required Stripe read and payment action.
