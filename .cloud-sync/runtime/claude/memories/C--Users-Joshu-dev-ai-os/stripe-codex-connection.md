---
name: Stripe Codex connection
description: The Codex Stripe app is connected to the Aspiring Attorneys Stripe account in live mode, verified by account listing on 2026-09-14. This does not verify Stripe CLI login or a local API key.
type: reference
---

On 2026-09-14, the Stripe app connection in Codex successfully listed the **Aspiring Attorneys** account (`acct_1PJnXRIULVCj6rqq`) with `livemode: true`. This confirms the OAuth connection is working for that account.

This is separate from the Stripe CLI and any API key in `.env`; neither was verified by this check. Available actions remain subject to the app's granted scopes and Codex permissions.
