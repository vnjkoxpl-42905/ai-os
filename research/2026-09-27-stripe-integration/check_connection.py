"""Read-only Stripe API connectivity check. Never prints credentials or payment data."""

import json
import pathlib
import urllib.error
import urllib.request


root = pathlib.Path(__file__).resolve().parents[2]
secret = None
for line in (root / ".env").read_text(encoding="utf-8").splitlines():
    if line.startswith("STRIPE_SECRET_KEY="):
[REDACTED CREDENTIAL]
        break

if not secret:
    raise SystemExit("STRIPE_SECRET_KEY missing")

for label, path in (
    ("account", "/v1/account"),
    ("payment_intents_read", "/v1/payment_intents?limit=1"),
):
    request = urllib.request.Request(
        "https://api.stripe.com" + path,
        headers={"Authorization": "Bearer " + secret},
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            payload = json.load(response)
            print(json.dumps({"check": label, "http_status": response.status, "account_id": payload.get("id") if label == "account" else None, "livemode": payload.get("livemode") if label == "payment_intents_read" else None}))
    except urllib.error.HTTPError as error:
        body = json.loads(error.read().decode("utf-8"))
        print(json.dumps({"check": label, "http_status": error.code, "error_type": body.get("error", {}).get("type"), "error_code": body.get("error", {}).get("code")}))
