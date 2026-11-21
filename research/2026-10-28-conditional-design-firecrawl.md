# Make the Practice centre an inspectable workspace

Date: 2026-10-28. Scope: Firecrawl research for the Conditional Logic Bootcamp. This is research and a proposed adaptation, not an implementation or visual acceptance report.

## Recommend a quiet workbench with precise feedback

The useful advanced pattern is not more decoration. Keep a compact skill/drill navigator beside a contextual setup surface. Use charcoal framing, warm reading surfaces and a cobalt selection accent. Put feedback and data beside the attempt they explain. A selected chart segment should lead to the exact items represented by that segment.

Preserve the resolved flow: **skill → named drill → instructions and supported settings → Start**. No example question in setup. Preserve each activity's existing attempt history. The centre currently has no aggregate performance query, so centre-wide accuracy, mastery scores, trend charts, unlocks and inferred recommendations are not justified by the current data contract.

## Provider and evidence ledger

- Read the installed `C:/Users/Joshu/.agents/skills/firecrawl/SKILL.md`, sibling `firecrawl-agent/SKILL.md`, local `references/firecrawl.md`, and shared `design/README.md`/`design/principles.md` before research.
- Checked earlier `.firecrawl/conditional-design-20261027/` results to avoid repeating Capacities/Rive/Raycast/Brilliant research.
- CLI v1.26.3 authenticated; initial status 1,271 credits remaining, 0/2 jobs.
- Launched two actual Spark2 agent jobs with a 50-credit ceiling each, strict schema, high effort, no Alexandria providers. Both stopped at their credit limits and returned schema-valid partials. Neither is a completed research run.
- Feedback/results job: `01a181ab-c5c3-768f-a91f-46bff9e72e11`; thread `01a181ab-c600-70fd-8091-5acd4e9aefe9`. Payload reports `creditsUsed: 0` despite credit-limit failure. Preserve that inconsistency rather than claiming 50 credits were spent.
- Workspace/data job: `01a181ab-b7ed-73dc-9156-93b95e9abbe2`; thread `01a181ab-b81c-767c-b14f-e6b82de039d2`. No final credits-used field.
- Followed up by directly scraping eight official sources, all HTTP 200. Final account status 1,263 credits remaining, 0/2 jobs. Net eight-credit difference is not per-agent billing proof.
- Raw outputs: `.firecrawl/conditional-design-deep-20261028/firecrawl-*`. No feedback/telemetry calls, authenticated product access, or Alexandria provider calls were made.
- Direct scrapes verify the source text and asset URLs below. **No source image pixels or live product interactions were inspected in this research subtask.** Source pages describe behavior; recommendations below are inferences. Reduced-motion behavior was not established for the referenced products.

## Eight strongest source-backed patterns

| Primary source and screen | Documented mechanism, verified in direct scrape | Adaptation for LSAT U | Real data required and limits |
|---|---|---|---|
| [Linear Insights](https://linear.app/docs/insights): chart and table | Bars/segments temporarily filter the issue view; hover/selection highlights related table records. Parameters depend on the actual records in view. | After a completed round, selecting **Missed · 3** filters the exact three items in that round. Keep the list and summary synchronized. | Stable attempt/item IDs, a clearly defined outcome, total answered/total round counts. Must distinguish first-try misses from eventual completion. Do not equate resolved with correct. |
| [Codewars kata trainer](https://docs.codewars.com/references/kata-trainer/): instructions, output, past solutions | Instructions and result output have distinct jobs; past solutions appear only when a previous completion exists. Running tests exposes output. | Setup stays about the task and settings. After checking, a contained result inspector becomes available beside or below the answer. Show existing attempts only when present. | Existing attempt identity and responses. Do not import its sample-test editor into setup; Joshua explicitly rejected sample questions there. |
| [Anki statistics](https://docs.ankiweb.net/manual/stats): card info, review history, scoped graphs | Card Info exposes review history. Stats can be scoped to a deck/search/history period. The docs explicitly warn that one day's correct percentage is not an overall progress indicator. | Show a modest activity history with explicit scope, such as **This attempt**, **Previous attempts**. An item can expose its prior work without a fictional mastery score. | Real timestamped reviews/attempts, item IDs, and outcomes. Self-ratings must be labelled self-ratings. Repeated attempts are not unique questions. |
| [GitHub Primer ProgressBar accessibility](https://primer.style/product/components/progress-bar/accessibility/): segmented progress | Communicate exact counts in adjacent text, do not use color alone, preserve contrast/reflow, and keep a passive progress bar out of keyboard focus. | Use symbol plus **Correct**, **Missed**, **Not answered** and exact counts. A passive strip needs no tab stop; any segment that filters must be an actual named button with keyboard support. | Correct count, missed count, unanswered count and denominator must reconcile. Outcome distribution is not course completion. Provide a text/list equivalent. |
| [Duolingo Explain My Answer](https://blog.duolingo.com/explain-my-answer-now-free/): answer-specific explanation | Optional feedback relates to the submitted error and underlying rule. Published UI images show answer state then an explanation entry point. | On a miss, provide the existing authored hint/reasoning beside the submitted answer, then a meaningful retry. Do not replace hint-first teaching with immediate answer disclosure. | Actual submitted answer, accepted answer/equivalence and existing authored rationale. Source does not justify introducing an LLM explanation service. |
| [Grafana data links](https://grafana.com/docs/grafana/latest/visualizations/panels-visualizations/configure-data-links/): chart to contextual detail | Links can carry series/value/time range; panel-to-panel filtering preserves selected context when explicitly included. | Clicking a result or history entry opens the relevant drill/attempt with topic/mode context intact; Back restores the same skill/drill selection. | Existing route/run identifiers and supported query state. Avoid read-only chart interactions accidentally creating attempts or changing assignment membership. |
| [Vercel Observability](https://vercel.com/docs/observability): graph, ranked routes, detailed records | Choose a time range, narrow the graph, rank related routes, inspect one route, follow its source logs. | Aggregate-to-record drilldown is useful only when the dataset exists. Prefer exact in-round item review today; richer cross-attempt comparisons require a separate data contract. | Timestamped comparable records and reliable scope. Duration/speed views require actual timing and pedagogical intent; speed is not a proxy for conditional understanding. |
| [Observable Plot interactions](https://observablehq.com/plot/features/interactions): tips and crosshair | Pointer transform shows nearest datum; tips expose exact fields; crosshair puts values at edges rather than covering marks. Docs still call direct point selection under development and do not promise animated incremental views. | If later implementing response-time history, reveal exact values on demand and keep text/table equivalent. A tiny native SVG strip may suffice for current bounded attempts. | Ordered records and honest labels. Do not install Plot expecting built-in accessible click selection or animated transitions. Keyboard/touch alternatives need independent implementation. |

## Public source assets for the host's visual inspection

These URLs were extracted from directly fetched primary pages. They are available leads, not visually reviewed evidence.

- [Linear chart/table screenshot](https://webassets.linear.app/images/ornj730p/production/c845c78338ca581e6794e8aa2731d02bdd5b058f-2160x1327.png?w=1440&q=95&auto=format&dpr=2)
- [Codewars light trainer](https://docs.codewars.com/assets/images/kata-trainer-light-865e36a6e86df907b936736484db81f2.png)
- [Codewars dark trainer](https://docs.codewars.com/assets/images/kata-trainer-dark-6a7ff8380e9e366daa144b917f70a267.png)
- [Anki statistics](https://mintcdn.com/anki/4yLyWj6_UVW-sSDI/media/Statistics.png?fit=max&auto=format&n=4yLyWj6_UVW-sSDI&q=85&s=3bf89a735c59f150e62714bda9c80c40)
- [Duolingo incorrect answer state](https://storage.ghost.io/c/7a/33/7a33d0f4-927d-4fe8-a6bf-96131b5e76d4/content/images/2025/12/EN_Reverse-Translate.png)
- [Duolingo explanation state](https://storage.ghost.io/c/7a/33/7a33d0f4-927d-4fe8-a6bf-96131b5e76d4/content/images/2025/12/EN_Reverse-Translate-EMA.png)
- [Grafana data point link](https://grafana.com/media/docs/grafana/panels-visualizations/screenshot-time-series-data-link-v10.3.png)
- [Vercel error-rate screen](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fobservability%2Ferror-rate-light.png&w=1080&q=75)

## Concrete implementation recommendations

1. **Selection is a persistent relationship.** A selected skill exposes its named drills in a compact navigator. The selected drill controls the adjacent instruction/settings inspector. Keep title, category and Start visible together. On phone collapse the navigator after an explicit selection and offer a clear Change activity action; preserve context on return.
2. **Make status feel pressable only when it is.** Use a small inset medallion with a crisp check or cross, a visible text label and precise count. An actionable status may lower its contact shadow on press and expose focus independently. Passive feedback must not mimic a button. Cobalt can carry correct/selected information, amber missed/retry, neutral unfinished. Color is redundant to the symbol and label.
3. **Animate cause and effect.** A 120–180ms local state transition, tiny compression and short icon draw can confirm an action. Do not shake missed answers, hide reading during animation, run ambient loops or replay the page on filtering. Reduced motion uses immediate state changes with the same information. These timings are proposed implementation choices, not measurements from the sources.
4. **Use a result strip only when it has an action.** A segmented strip or item mosaic can lead to the exact missed items. Show correct/missed/unanswered counts and total in text. No radar mastery chart, trend curve, heatmap or score projection based on absent data. Keep small charts secondary to reading and retrying the actual items.
5. **Treat self-report honestly.** Flashcard Again/Needs work/Got it history represents the learner's rating, not machine-scored correctness. Do not silently merge that with objective diagram results.
6. **Prove all state paths.** Keyboard select/start/change/back, touch widths, 200% zoom, reduced motion, forced colors, no history, partial attempt, completed attempt, item retry and load/error states. Compare exact records behind every displayed count. Do not infer pedagogical quality from CSS or test success.

## Rejected or insufficient leads

- Monkeytype's extracted result text was suggestive, but the agent reported CSS/server failures. Not promoted to a verified screen reference.
- Radix and Zed returned weak source evidence in these partials. Do not claim their particular state contracts or preview behaviors were independently checked here.
- No marketing hero, particle field, futuristic dashboard mockup or decorative chart is evidence of a useful learning interaction.
- No app code, dependencies, assignment membership, backend schema or historical data changed in this subtask.
