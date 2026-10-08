# Stripe access without depending on the connected app

Verified 2026-10-08: the existing central `STRIPE_SECRET_KEY` successfully read the live **Aspiring Attorneys** account. The Codex Stripe connected app separately returned reauthentication required. Those are different authentication routes; use the working API route for read-only verification while the app connection is unavailable.

From the current vault, run:

```powershell
py system/scripts/stripe-account-read.py
```

The helper reads `.env` directly, uses only `GET /v1/account`, bounds its request to 30 seconds and prints a small metadata whitelist. It never prints keys, request headers, full error responses, customer records or payment instruments. Missing credentials, API errors and invalid responses exit nonzero; no cached success is substituted.

The successful account response was `acct_1PJnXRIULVCj6rqq`, display/business name Aspiring Attorneys, country CA, with a live credential. Confirm this identity before financial queries. An account read does not prove every restricted endpoint is authorized or establish a customer's current payment status.

For a payment question, query the exact customer/payment/link through the [official Stripe API](https://docs.stripe.com/api), with a bounded date/range and pagination. Treat all actual financial state as live authority. No charge, refund, subscription change, permission modification or message is authorized merely by an audit or read-only request. Preserve the existing action-specific approval requirements.

If restoring the connected app, Joshua must complete its account sign-in/reconnection in Codex. API access does not silently repair that OAuth session. Keep credentials in the existing central store, not in this reference or chat.
