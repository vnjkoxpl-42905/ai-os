# Conditional practice design: Tavily coverage and design constraints

Date: 2026-10-28. Scope: a conditional-logic practice workspace, skill selection, drill setup, tactile feedback and honest performance displays.

## Tavily research did not run

Windows Application Control blocked the installed `tvly.exe` before the first search reached the provider. There is no Tavily MCP connector in this session. The denial was not bypassed. Authentication, quota and credits remain unverified.

Exact command and failure: [provider execution receipt](../.tavily/conditional-design-20261028/PROVIDER-STATUS.md).

This report supplies product-design deductions from the user-provided screenshot and task constraints. It does **not** claim a live source investigation, reviewed source imagery, six validated references or successful Tavily calls. The host's parallel Firecrawl research should own source-backed visual recommendations.

## What the screenshot shows

The supplied 988 by 835 screenshot shows a four-item flat skill switcher, a left activity list and a right instructions/setup card. `Recall` and `Apply` do not explain their content. `Conditional Rephrase` and its description repeat across the list and setup surface. `Timing: Original progression` mixes two concepts. The existing palette uses muted green and beige. The bottom comparison controls and prototype notices occupy a large amount of otherwise quiet space.

These observations concern the image only. No runtime interaction, keyboard state, performance query or actual drill configuration was inspected in this research subtask.

## Three concrete directions for the builder

1. **Editor workspace.** Use a dark graphite structural rail, warm reading surface and a non-green blue-violet selected accent. Keep explicit skill names and named drills together in a navigable hierarchy. Give setup a separate header and compact settings strip. Mobile should become a clear choose-then-configure progression with a persistent selected activity label and Change control. Preserve instructions and real settings before Start. No question sample.
2. **A compact attempt ledger.** Where the engine actually exposes a completed run, display the most recent attempt as a small sequence of response markers. An outlined circle denotes unanswered, a checked disc denotes correct and a crossed disc denotes missed, with visible text or accessible labels. A retry can have its own corner mark. Do not recolor an earlier miss into a correct first attempt. The sequence is more useful than a synthetic readiness score.
3. **A post-run comparison strip.** When comparable attempt history exists, show current correct/answered beside the previous attempt using two aligned horizontal marks. Include run size and date. When question sets, modes or scoring differ, show a history list rather than a trend suggesting improvement. Use a plain empty state until genuine data exists.

## What tactile means here

Feedback should be immediate, discrete and easy to read: a 100-160ms press response, a short icon transition, and a stable final status. Shape and text carry meaning; color reinforces it. An error should not shake the whole reading surface. Reduced motion removes movement while keeping the status change. Avoid confetti, flashing glows, animated counters and constant ambient particles in sustained reading.

## Data contract needed before graphs

Do not invent fields or claim the centre can aggregate them. First verify each existing engine's data, identity and persistence boundary:

| Display | Required real fields | Failure or empty behavior |
|---|---|---|
| Session markers | Ordered response ids, answered status and outcome | Omit if only a final score exists |
| Correct and missed counts | Scored response count, correct count, scoring semantics | Do not treat skipped or revealed answers as correct |
| Last attempt | Activity id, student id, mode/topic filters, attempt timestamp | Show No previous attempt when absent |
| Previous/current comparison | Two comparable runs and their denominators | Show separate history rows when not comparable |
| Resume | Existing run identity and supported resume target | Offer another attempt only when resume is unsupported |

Do not convert completed work to mastery, use a pooled percentage across incompatible drills, penalize ungraded lesson checks, or mix local-browser prototype state with signed-in student history.

## Validation priorities

- Use actual long activity names and descriptions, the largest legitimate settings set, empty histories, partial runs and a student with only one assigned activity.
- Skill selection must not make an unassigned drill discoverable or launchable.
- Place hint/retry before reveal where the drill supports that teaching model; visualization must not expose answers early.
- Verify 390px, 768px and desktop; keyboard, focus-visible and reduced motion; and diagram symbols at high zoom.
- Evaluate whether each chart answers an actual learner decision. Remove it if a concise sentence or count is clearer.

No application code, configuration, dependency, architecture or data writes were changed by this subtask. No messages or telemetry were sent externally.
