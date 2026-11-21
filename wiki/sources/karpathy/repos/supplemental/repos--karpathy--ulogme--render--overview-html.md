---
type: source
subject: "repos/karpathy/ulogme/render/overview.html"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, github, source]
semantic-status: complete-preserved-text-read
---

# repos/karpathy/ulogme/render/overview.html

Captured repository text; ownership does not establish individual authorship. Original date: 2014-05-13T02:16:30Z (created); pushed 2020-09-17T23:08:59Z. Captured: 2026-10-08T09:35:44.650708Z.

[Immutable raw file](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/ulogme/render/overview.html). SHA-256 `cd84c78e555cda79cb458d5abd3f7ce5b4a66c676e1a71878ca7dc5e36afd1e1`. Manifest hash match: True.

## Reviewed content

Multi-day dashboard loads all day JSON files, maps window groups, aggregates durations/key counts and displays stacked daily bars, per-window totals, 10-minute key-frequency heatmaps anchored at 7 AM, and click-through daily views. Filtering changes visible categories. Like single-day view, first category occurrence initializes count to zero and last event duration is assumed one second, so exact aggregate correctness is not asserted. Promise loading catches errors but proceeds to analysis, a historical failure-handling limitation. No personal event logs or dashboard were executed.

> div.append('p').text('total keys pressed: ' + sum_kevents_global + ' in ' + events.length + ' days (' + Math.floor(sum_kevents_global/events.length) + ' per day average)');

## Limits

Complete preserved text read, lines 1-497. No captured code executed or linked sources inspected. Static source review does not establish current correctness, performance or compatibility.
