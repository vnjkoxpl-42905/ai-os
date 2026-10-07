---
name: no-fake-urls-on-his-servers
description: "Never leave Joshua watching a temporary or invented localhost route; close or redirect the tab before removing the route."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e582e2d1-1471-4789-a38c-fd697aa8fe17
  modified: 2026-09-09T07:39:34.323Z
---

Do not navigate Joshua's running servers to made-up URLs. On 2026-09-09 a deliberately
nonexistent path (`/zzz-control-route`) was used on `localhost:4173` as a measurement
control; it rendered the app's 404 page and he told me to stop and to just use
`localhost:4173`.

**Why:** he watches the browser pane live. A 404 on his own app reads as something
broken, and he has no way to tell an intentional control from a real failure. The
address bar is part of what he is reading.

**How to apply:** navigate to the plain origin, or to a route that actually exists. If a
"route not on the allowlist" control is genuinely needed, use a real route that qualifies
and say beforehand which one and why. Never leave a fabricated URL sitting in the address
bar — navigate away as soon as the reading is taken.

The same rule applies to temporary routes that briefly exist. On 2026-09-13 I added
`/dev-drill-hub` for a browser verification, removed the route while its tab was still
open, and hot reload replaced the page with the app's 404. Before removing any temporary
verification route, first close its agent-created tab or navigate that tab to a known-good
route. Cleanup is not complete while Joshua is still looking at a URL the cleanup will
invalidate.

Related: [[ai-os-safety-rules]], [[lsatu-content-lives-in-postgres]].
