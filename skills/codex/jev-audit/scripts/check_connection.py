#!/usr/bin/env python3
"""Preview, or explicitly send, one synthetic Jev connection check. No retries."""

import argparse
import getpass
import json
import math
import os
import sys
import time
import urllib.error
import urllib.request


PROVIDERS = {
    "openrouter": ("https://openrouter.ai/api/alpha/decisions", "OPENROUTER_API_KEY", "typesafe/jev-1.13"),
    "typesafe": ("https://api.typesafe.ai/v1/systemone", "TYPESAFE_API_KEY", "jev-latest"),
}
MAX_RESPONSE_BYTES = 262144


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def request_body(model):
    return {
        "model": model,
        "state": {"message": "My package arrived damaged. Please help me replace it."},
        "questions": {
            "support_request": {
                "type": "noul",
                "instructions": "The message asks for customer support about a damaged package.",
            }
        },
    }


def validate_response(data):
    if not isinstance(data, dict):
        raise ValueError("Expected a JSON object.")
    answers = data.get("answers")
    answer = answers.get("support_request") if isinstance(answers, dict) else None
    if not isinstance(answer, dict) or answer.get("type") != "noul":
        raise ValueError("Missing or incompatible support_request answer.")
    value = answer.get("noul")
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or not 0 <= value <= 1:
        raise ValueError("Expected a finite probability from 0 to 1.")
    result = {"support_request_probability": value}
    usage = data.get("usage")
    if isinstance(usage, dict):
        # Only expose known numeric billing fields, never arbitrary provider text.
        result["usage"] = {
            key: usage[key] for key in ("input_tokens", "output_tokens", "cost")
            if isinstance(usage.get(key), (int, float)) and not isinstance(usage[key], bool)
            and math.isfinite(usage[key]) and usage[key] >= 0
        }
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider", choices=PROVIDERS, default="openrouter")
    parser.add_argument("--model", help="Override only after checking current official provider docs.")
    parser.add_argument("--live", action="store_true", help="Send one request; provider usage may be billed.")
    parser.add_argument("--prompt-key", action="store_true", help="Use a hidden prompt if no environment key exists; requires an interactive terminal.")
    args = parser.parse_args(argv)
    endpoint, key_name, default_model = PROVIDERS[args.provider]
    body = request_body(args.model or default_model)
    if not args.live:
        print(json.dumps({"mode": "preview", "network_requests": 0, "endpoint": endpoint,
                          "key_environment_variable": key_name, "body": body}, indent=2))
        return 0
    key = os.environ.get(key_name, "").strip()
    if not key and args.prompt_key:
        if not sys.stdin.isatty():
            print("A hidden key prompt requires an interactive terminal.", file=sys.stderr)
            return 2
        key = getpass.getpass(f"{key_name} (hidden): ").strip()
    if not key:
        print(f"Set {key_name} in your environment, or use --prompt-key in an interactive terminal. Do not paste the key into chat.", file=sys.stderr)
        return 2
    request = urllib.request.Request(endpoint, data=json.dumps(body).encode("utf-8"), method="POST",
                                     headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    start = time.monotonic()
    try:
        with urllib.request.build_opener(NoRedirect()).open(request, timeout=20) as response:
            raw = response.read(MAX_RESPONSE_BYTES + 1)
        if len(raw) > MAX_RESPONSE_BYTES:
            raise ValueError("Provider response exceeded the size limit.")
        result = validate_response(json.loads(raw))
    except urllib.error.HTTPError as error:
        print(f"Provider returned HTTP {error.code}. No retry was made. Check account access, credits, model and endpoint. Response body omitted.", file=sys.stderr)
        return 1
    except (urllib.error.URLError, TimeoutError, OSError):
        print("Connection failed or timed out. No retry was made.", file=sys.stderr)
        return 1
    except (ValueError, UnicodeError):
        print("Provider returned an invalid or incompatible response. No retry was made. Check the current API documentation.", file=sys.stderr)
        return 1
    print(json.dumps({"mode": "live", "requests_attempted": 1,
                      "elapsed_ms": round((time.monotonic() - start) * 1000, 1), **result,
                      "note": "Connection check only; not a task-accuracy or production benchmark."}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
