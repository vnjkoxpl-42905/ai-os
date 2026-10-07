---
name: in-app-browser-scales-css-widths
description: getComputedStyle in the Claude in-app browser reports outline/border widths at 0.8x, so width thresholds always "fail".
metadata:
  type: feedback
---

In the in-app Browser pane, `getComputedStyle` reports `outline-width`, `outline-offset`
and `border-width` scaled by 0.8. A `div` created on the spot with `border: 2px solid`
reads back `1.6px`, while its `height: 20px` reads back exactly 20. Box geometry
(`getBoundingClientRect`, heights, widths) is correct; only these stroke widths are scaled.

**Why:** any audit script with a rule like `parseFloat(cs.outlineWidth) >= 2` can never
pass there, so it reports every control on the page as having no focus ring. Confirmed
2026-09-09 on the LSAT U drill hub, where it flagged 14 of 16 controls that all had
correct 2px rings.

**How to apply:** read `outline-style` and `box-shadow` to prove a ring *exists*, and take
its *width* from the CSS source, never from the browser. Separately, `:focus-visible` only
matches after real keyboard input, so press Tab once with the `computer` tool before any
programmatic `.focus()` sweep, or every element reports unstyled. Related:
[[no-fake-urls-on-his-servers]].
