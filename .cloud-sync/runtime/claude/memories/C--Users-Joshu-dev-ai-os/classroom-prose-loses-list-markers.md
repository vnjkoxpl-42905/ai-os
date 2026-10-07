---
name: classroom-prose-loses-list-markers
description: "Tailwind preflight strips list markers app-wide, so any hand-rolled prose CSS must re-declare list-style-type."
metadata: 
  node_type: memory
  type: project
  originSessionId: 9a2e34c3-6cc3-41c2-b75a-b0b02f16c2dc
  modified: 2026-09-09T21:26:45.883Z
---

Tailwind's preflight sets `ol, ul, menu { list-style: none }` across LSAT U. Any
hand-written prose stylesheet that sets only `padding-left` gets indented lines with no
bullets, and a numbered list loses its numbers entirely. `.classroom-prose` shipped that
way until 2026-09-09.

**Why:** losing numbers is a change of meaning, not of style — "1, 2, 3" becomes three
lines that no longer say they are in order. It is invisible in review because the CSS
looks complete.

**How to apply:** when writing or auditing prose CSS anywhere in this repo, check
`getComputedStyle(ul).listStyleType` in the browser rather than assuming the browser
default. Declare `disc` / `decimal` explicitly.

Related: [[tailwind-prose-classes-are-inert]]
