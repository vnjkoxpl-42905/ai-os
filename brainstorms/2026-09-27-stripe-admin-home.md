# Stripe integration and admin Home: Brainstorm / Discovery Notes
Date: 2026-09-27 · Goal: Define a complete Stripe-to-LSAT U payment workflow and a teacher-specific admin Home, grounded in the current platform.
Status: in progress
Context sources: `context/work.md`; `decisions/log.md`; `brainstorms/2026-07-19-booking-admin-redesign.md`; `brainstorms/2026-09-23-classroom-home-PLAN.md`; `brainstorms/2026-09-24-lsatu-fit-one-screen.md`; LSAT U code audit in progress.

## Summary / key decisions
- User intent, pending detailed decisions: Stripe payments should be visible in the admin account and drive appropriate actions for tutoring sessions and packages without manual detection. Admin Home should reflect Joshua's teacher work rather than student assignments, drilling, or due dates.
- Existing business context: Stripe handles packages; Cal.com is Stripe-linked for paid individual sessions; rare e-transfers exist. Confirmed payment triggers onboarding. A 2026-07-20 decision made booking passes the sole record of sessions owed and explicitly chose no Stripe-to-pass reconciliation. The requested automation may supersede that decision, pending Joshua's answer.
- Recommendations and technical findings will be kept separate from Joshua-confirmed decisions.
- Verified live on `https://lsatprep.study/classroom` in Joshua's signed-in Teacher account on 2026-09-27: the page shows “Nothing is due today. Drill whatever you feel like,” Smart Drill, Timed section, and a student-style Next seven days strip. It shows no payment feed.
- Code audit: `/classroom` renders the student `ClassroomHome` for teachers too. A separate `/teacher/today` exists, but its work queue has no payment source. The Stripe webhook currently handles specific booking/payment-link flows; it does not build a universal Stripe transaction ledger, and the current booking events are sparse. These are repository findings, not a live Stripe reconciliation.
- Code audit: generic invoices, subscriptions, direct Payment Intents, manual Dashboard charges, and unknown payment links are not covered by the current webhook. The Checkout handler currently grants feature access before product classification; this requires a guarded fix before broadening event ingestion. The existing email matching has no durable Stripe customer ID mapping. A live endpoint/deployment check remains necessary.
- Live Stripe account verification attempted 2026-09-27 through the connected Stripe app; the app requires reauthentication. Do not treat repository configuration as proof of live account coverage.

## Q&A log

## Open flags (pending input)
- Definition of which Stripe payments enter LSAT U and what each payment should trigger -> Joshua.
- Admin Home priorities and payment visibility requirements -> Joshua.
- Whether to supersede the 2026-07-20 booking-pass decision -> Joshua.
