---
name: calcom-pending-bookings-are-unpaid
description: Paid event types only (not free consultations). A cal.com booking stuck at status "pending" means the student's 30-minute Stripe payment hold expired; the link is dead, unrecoverable, and the stale booking keeps blocking the slot.
metadata:
  type: project
---

Applies to **paid** event types only. The free **consultation** event type takes no payment and
never lands in `pending` — do not raise this failure mode about a consultation booking.

`session-link` (event type 4753558) charges Stripe `ON_BOOKING`, $45 USD, `refundPolicy: never`.
The flow is: pick slot -> form -> **"Pay to book"** -> `https://cal.com/payment/<payment-uuid>`
which loads Stripe Elements and holds the slot for **30 minutes only**:

> "This slot is held for you for 29:54 — after that, someone else may book it."

Miss that window and the payment page is dead. The link is a random uuid, is **not** in the
booking record, and API v2 exposes **no** payments endpoint (`/v2/payments`,
`/v2/bookings/<uid>/payments` are all 404) — so an expired link cannot be recovered or re-sent.

Worse, `https://cal.com/booking/<uid>` then shows "Your meeting is awaiting payment — $45.00"
with only *Add to calendar* and *Cancel*. **There is no Pay button** — verified against a
control booking, so this is cal.com's behavior for any unpaid booking, not a per-student glitch.
cal.com also sends Joshua **no host notification** for an unpaid booking, so it is invisible.

The stale `pending` booking still **holds the slot**, hiding it from every other student.

Find them (`CALCOM_API_KEY` in `.env`; **API v2 only — v1 is decommissioned**):

```
curl -H "Authorization: Bearer $CALCOM_API_KEY" -H "cal-api-version: 2024-08-13" \
  "https://api.cal.com/v2/bookings?status=upcoming&take=100"
```

**Why:** "Scheduling isn't working" almost always means this. Payment itself is fine — Stripe
Elements load and other students pay normally.
**How to apply:** The only fix is to cancel the stale pending booking and have the student book
again, which issues a fresh 30-minute link. Sweep for `pending` bookings periodically; they
accumulate and silently eat availability. See [[calcom-rolling-window-hides-saturdays]].
