# From an audit finding to a small test

Read this after the user chooses an opportunity or asks for setup. A key or successful connection is not proof that the proposed workflow benefits from Jev.

## 1. Make the pilot concrete

Show the existing workflow, exact input, permitted output, downstream action, and comparison. Prefer 10–20 labeled examples, including ambiguous and negative cases. Reserve untouched examples if iterating on criteria. Define what a useful result means: acceptable missed items, wrong choices, latency, and total cost. A tiny pilot proves feasibility, not production reliability.

Prepare the implementation before requesting any final approval needed for new data transmission or paid calls. Reuse authorization already given for that specific data, provider, and scope. Audit-only consent is not consent to send private transcripts to a new provider or change the user's live workflow.

## 2. Choose a supported provider

Read [providers-and-examples.md](providers-and-examples.md) and verify the selected provider's current official documentation. OpenRouter's documented route uses a Decisions API, not chat completions. Existing TypeSafe integrations may need an adapter.

Let the user enter a key through a hidden local prompt or their environment/secret manager, not into the conversation or a committed file. Do not print, paste into source code, or save credentials in the report. Help with account navigation if asked; account access and billing actions remain subject to the host's permissions.

## 3. Test connectivity with fixed synthetic data

The bundled helper requires Python 3.10+ and only the standard library. Resolve its location from this skill's directory. The following paths assume the repository root; adjust to the installed skill path as needed.

Preview only, no key or network needed:

```sh
python skills/jev-audit/scripts/check_connection.py --provider openrouter
```

After the user authorizes a single small paid connection check and has supplied the matching environment variable:

```sh
python skills/jev-audit/scripts/check_connection.py --provider openrouter --live
# Or, for an existing direct TypeSafe account:
python skills/jev-audit/scripts/check_connection.py --provider typesafe --live
```

The helper sends one fixed synthetic support message, never reads history, never retries, rejects redirects, limits response size, and validates the returned probability. It reports request wall time and usage if supplied. `--prompt-key` uses a hidden terminal prompt when the environment variable is absent; use it only in an interactive terminal the user controls. Do not open a visible terminal window without the user's request.

It exits on missing credentials or provider/validation errors. Fix the cause before another call; do not automatically probe multiple models, gateways, or account keys. A correct probability on this easy message establishes a working response shape, not real task accuracy.

## 4. Evaluate the selected workflow

Run the original approach and the Jev candidate on the same labeled sample. Keep existing execution/approval rules in place; start with recommendations or shadow decisions where appropriate. Record errors, abstentions, fallback work, measured timings, and reported billed usage. For screening, inspect both kept and rejected items. For compaction, verify continued task quality. For code checks, run the real tests as well.

Do not treat a model's self-confidence as test accuracy. Compare with ordinary rules or a cheaper existing model where appropriate. State missing billing information rather than assuming zero cost. Include the audit/implementation effort when judging whether the integration is worthwhile.

End with the observed result: adopt the narrow pilot, revise and retest, or keep the original approach. Offer a separate concrete implementation step if the evidence supports it. Do not enable a persistent hook, global routing change, or unattended automation merely because the connection check passed.
