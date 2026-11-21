# Student-first visual design comparison

## Scope

UI design only: no score deductions for sample-data accuracy, missing backend integration or simulated actions. Baseline: original corrected student handoff, desktop and390px images. Current production redirected the review browser to auth, so this is not a verified signed-in live-site comparison. Prototype controls are excluded from design scores.

Codex scores were saved before reading Claude's response. Claude used a fresh session9c67ea43-db73-4fea-b6d3-254500178942, with explicit model claude-opus-5-5 and effort medium. Returned modelUsage confirmed claude-opus-5-5. Claude was not given Codex's scores or audit. It inspected all3 student desktop/mobile full-page renders, baseline2images, three desktop motion contact sheets, then fresh6student viewport captures and2phone sheets. Detailed reports: CLAUDE-VISUAL-REVIEW.md and CLAUDE-VISUAL-ADDENDUM.md. The latter corrects limited mobile observations in the first report.

## Codex rubric

Hierarchy25: task/CTA dominance and secondary visual weight. Typography20: readable scale, contrast, type relationships. Composition20: proportions, spacing, density and depth. Identity15: originality and coherent visual language. Motion10: purposeful entrance/feedback, based on sparse natural-frame sheets with limited pacing evidence. Mobile10: actual390px composition and motif adaptation. These are structured judgments, not objective measured quality.

| Direction | Hierarchy25 | Type20 | Composition20 | Identity15 | Motion10 | Mobile10 | Total |
|---|---|---|---|---|---|---|---|
| Lamplight |20|17|16|14|8|6|81|
| Marginalia |17|18|17|13|7|7|79|
| Carrel |18|16|15|14|8|6|77|

Original static baseline72/90, motion unscored. Corresponding static-only new scores: Lamplight73/90, Marginalia72/90, Carrel69/90. Do not compare baseline72 directly with totals out100.

## Independent scores

| Direction | Codex | Claude Opus5.5 Medium, final |
|---|---|---|
| Lamplight |81|80|
| Marginalia |79|78|
| Carrel |77|67|

Claude's weighting differs: hierarchy25, type20, composition15, identity20, motion10, mobile10. Its scores aren't the same instrument; identical ranking is more meaningful than a one-point difference. Main disagreement: Codex gives Carrel more credit for material craft; Claude sees excessive competing objects as a larger compositional problem. Both see Lamplight as strongest to develop, not a finished premium result.

## Lamplight

Keep: one cream lit task against navy, warm amber as a controlled focal accent, moving a chosen queue item into the main slot, twelve-unit progress rhythm, clear separation between primary and secondary action. The week windows are genuinely worth exploration, with improved empty-day contrast and compact dimensions.

Improve/reject: oversized greeting beside the work title, substantial dead left-column space under the hero, long hanging-wire space on mobile, dim secondary captions, generic outlined action pills and generic boxed personal message. Countdown consumes an entire wide section for little visual information. Calendar/practice sit far down a3907px mobile page. Current phone CTA is above the fold, but only near the lower edge; no claim it is absent.

Versus original: meaningful improvement in distinctive hierarchy and atmosphere. Original wins at compact supporting information and restrained overall page length. This is the best full creative direction, but not a reason to discard the original's calm structure.

## Marginalia

Keep: readable serif, small-cap run-ins used selectively, paper/ink restraint, fine rules, controlled blue CTA, gutter labels, contextual numbered notes, compact tick ruler. Phone tap-to-expand notes preserve context without permanently occupying space. The original study-centered tone benefits from this editorial character.

Improve/reject: turning every status and task into prose, repeated underlined nouns at similar weight, using main text and sidenotes to say similar things, very large greeting, nearly flat hierarchy outside the main blue button. Week contents list is elegant but slower to scan than the original date strip. Don't transplant the complete literary structure merely for novelty. Initial near-blank motion frame should be investigated before calling entrance behavior refined; sparse frames do not establish duration.

Versus original: stronger typographic identity and editorial composition; weaker immediate task grouping and at-a-glance overview. Borrow typography and contextual annotation, not the entire page architecture.

## Carrel

Keep: convincing paper-edge layering, stamped due date, restrained lift/tilt interaction feedback, readable event chips and day numbers. A session ticket is a clear way to differentiate a booking from work. Swipe/card exchange is a useful idea where the content genuinely benefits from serial navigation. The palette is deliberate and distinct.

Improve/reject: simultaneously using card file, lined paper, envelope, postage stamp, flip clock, ticket, spiral binding and stopwatch. Each object is individually crafted, but too many create equal visual claims. Blank ruled lines dominate the primary card; tabs truncate; mobile Continue falls below the first viewport. A large envelope for a short message consumes disproportionate space. Avoid transplanting the whole desk.

Versus original: more tactile and memorable, weaker restraint and task overview. Most valuable as a source of a few interaction/material details rather than the dashboard template. Claude grades it ten points below Codex; neither would use it wholesale.

## Baseline takeaways

Retain near-white/ink clarity, dominant dark due-work card, compact supporting rail, consistent navigation and small seven-day calendar. Main visual deficit is generic surfaces and modest identity, not poor basic hierarchy. A coherent new design may legitimately depart from it, but should earn those departures visually.

## Recommendation

Develop Lamplight as one coherent direction. Selectively borrow Marginalia's type treatment/contextual notes if they fit that language; Carrel's feedback craft is worth considering without importing all its objects. Do not combine every successful fragment. Highest-value improvements: rebalance hero and queue, reduce greeting prominence, redesign secondary captions/message presentation, compact countdown and calendar, and reduce phone whitespace before adding more decoration.

## Evidence repair

The first Claude fresh-capture command used the previous server-root path and overwrote audit-owned viewport PNGs with404captures. Host corrected the URL, added an HTTP-status assertion before screenshots and restored all12successfulcaptures. No prototype files were changed. Claude then inspected corrected6studentviewport images in a follow-up to the same fresh independent review. Do not use the first report's capture-failure observation as an unresolved issue.
