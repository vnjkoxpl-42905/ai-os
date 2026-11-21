# Jev capabilities, sources, and examples

Reference check: September 20, 2026. Recheck current official documentation before implementation. If browsing is unavailable, use these as a dated starting point and label access/pricing as unverified today.

## What qualifies as a Jev opportunity

Jev is TypeSafe's structured decision model. An application supplies state and typed questions. **Choice** selects among supplied options, **Score** evaluates supplied ordered levels, and **Noul** evaluates a yes/no proposition. Code consumes the returned values. It does not browse, execute a tool, generate a full article, or invent the application's missing data. An LLM can also classify; the question is whether this specialized component improves the user's actual workflow.

- [System One concepts](https://docs.typesafe.ai/concepts/system-one)
- [Introduction](https://docs.typesafe.ai/introduction)
- [Choice](https://docs.typesafe.ai/primitives/choice)
- [Confidence](https://docs.typesafe.ai/confidence)

Defined outputs do not guarantee correct decisions. Confidence is not a calibrated correctness percentage for an untested task. Avoid classifying an entire open-ended workflow when only one small decision within it fits. Use ordinary code for exact checks and arithmetic.

## Provider options

**OpenRouter:** its [official Jev recipe](https://openrouter.ai/docs/cookbook/building-agents/gate-tool-calls-with-jev) documents model `typesafe/jev-1.13`, an `OPENROUTER_API_KEY`, credits, and `POST https://openrouter.ai/api/alpha/decisions` with `{model, state, questions}`. This is a Decisions request, not an ordinary chat-completions call. Confirm the current model and endpoint when configuring it. The model catalog was visible during the reference check; its versioned model detail page returned 404, while the official recipe documented access. A real connection test determines whether the user's account can call it.

**TypeSafe directly:** [official introduction](https://docs.typesafe.ai/introduction). The reference integration uses `TYPESAFE_API_KEY`, `jev-latest`, and `https://api.typesafe.ai/v1/systemone`. Follow current onboarding/access instructions; do not assume every account is approved.

**Vercel AI Gateway:** [Jev model page](https://vercel.com/ai-gateway/models/jev). Useful if already in the user's stack. Confirm its evaluation API and credentials separately; a temporary price promotion is not permanent pricing.

Keys are provider-specific. A repository expecting `TYPESAFE_API_KEY` cannot use an OpenRouter key unless its transport is adapted. Prefer the user's existing supported provider; OpenRouter is a documented starting option when they have no preference. Do not silently change a working integration or create accounts, purchase credits, or install a global hook during the audit.

For estimates, obtain current provider pricing. Include input state repeated across batches, retries, fallback LLM calls, and downstream work retained unnecessarily. Show cash cost, token use, latency, and subscription limits separately.

## Real implementations to inspect selectively

Read only examples matching an observed workflow. These are community projects, not evidence of a universal benefit or official endorsement.

| Project | Narrow Jev decision | Rest of the workflow / limitations |
|---|---|---|
| [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) | Choose browser operations and targets from supplied page context. | Browser tools act; a text model fills generative gaps. One fast demo is not a general browser benchmark. |
| [Fast Jev Compaction](https://github.com/tamaratran/fast-jev-compaction) | Retain, truncate, or discard historical tool calls/results. | Retained text stays verbatim; it can still lose important context. The reviewed Claude integration requires early-access function hooks. Its animated macOS demo is scripted. |
| [Newsjack](https://github.com/elvisun/newsjack) | Keep, monitor, or reject candidate stories. | A separate agent investigates and writes. Check discarded stories and total downstream cost. The visual demo has a simulated mode; use real output for measurements. |
| [Commit Sentry](https://github.com/dabit3/jev-experiments/tree/main/commit-sentry) | Judge staged diff hunks for specific risks. | Code applies warning/blocking policy. Does not run tests or establish code correctness. Supports manual checks and Git hooks for existing repositories. |
| [Judge Sheets](https://github.com/dabit3/jev-experiments/tree/main/judge-sheets) | Classify or score rows of text against column questions. | Standalone spreadsheet app, not a Google Sheets integration. Verify the user's input/export path; the supplied dataset is synthetic. |

Do not describe independent alternatives such as NanoJev, Jevlike, SemIf, or Laya as TypeSafe Jev, or imply TypeSafe's model weights are open source. The repositories above illustrate possible integrations; use the user's own evidence to decide whether any is worth trying.
