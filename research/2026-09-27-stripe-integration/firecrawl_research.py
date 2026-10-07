"""Run two bounded Firecrawl agents against official Stripe documentation.

Raw results stay in the git-ignored .firecrawl directory. The findings are
distilled into the dated research plan in this directory.
"""

import json
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "references" / "firecrawl"))
from runner import get_api_key  # noqa: E402


SCHEMA = {
    "type": "object",
    "properties": {
        "summary": {"type": "string"},
        "findings": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "claim": {"type": "string"},
                    "source_url": {"type": "string"},
                    "evidence_excerpt": {"type": "string"},
                    "implementation_implication": {"type": "string"},
                },
                "required": ["claim", "source_url", "evidence_excerpt", "implementation_implication"],
            },
        },
        "open_questions": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["summary", "findings", "open_questions"],
}


JOBS = [
    (
        "webhooks",
        "https://docs.stripe.com/webhooks,https://docs.stripe.com/api/events/types",
        "Extract Stripe's current official rules for verifying webhook signatures, "
        "selecting payment event types, duplicate and unordered delivery, retries, and "
        "manual recovery. Include source URLs and short evidence excerpts. Explain why "
        "Checkout, PaymentIntent and invoice events can overlap for one purchase.",
    ),
    (
        "backfill-auth",
        "https://docs.stripe.com/keys,https://docs.stripe.com/api/payment_intents/list,https://docs.stripe.com/api/refunds/list",
        "Extract Stripe's current official rules for restricted API keys and "
        "server-side read access, plus created-date filtering and pagination for "
        "three-month PaymentIntent and refund backfills. Include source URLs and "
        "short evidence excerpts. State what still needs live account verification.",
    ),
]


def main():
    output_dir = ROOT / ".firecrawl"
    output_dir.mkdir(exist_ok=True)
    schema_path = output_dir / "stripe-research-schema.json"
    schema_path.write_text(json.dumps(SCHEMA), encoding="utf-8")
    env = dict(os.environ, FIRECRAWL_API_KEY=get_api_key())
    firecrawl_cmd = str(Path(os.environ["APPDATA"]) / "npm" / "firecrawl.cmd")
    for name, urls, prompt in JOBS:
        path = output_dir / f"stripe-{name}-agent.json"
        command = [
            firecrawl_cmd, "agent", prompt, "--urls", urls,
            "--model", "spark-1-mini", "--schema-file", str(schema_path),
            "--max-credits", "15", "--wait", "--timeout", "180",
            "--json", "--output", str(path),
        ]
        print(f"[Firecrawl] Launching {name} agent", flush=True)
        result = subprocess.run(command, env=env, capture_output=True, text=True)
        print(json.dumps({"job": name, "exit_code": result.returncode, "output": str(path), "message": (result.stdout + result.stderr)[-800:]}), flush=True)


if __name__ == "__main__":
    main()
