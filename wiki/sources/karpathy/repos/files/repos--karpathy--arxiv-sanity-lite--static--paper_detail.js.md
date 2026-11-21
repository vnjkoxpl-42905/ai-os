---
type: source
subject: "GitHub source repos/karpathy/arxiv-sanity-lite/static/paper_detail.js"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/static/paper_detail.js]
semantic-status: complete-named-text-read
---

# repos/karpathy/arxiv-sanity-lite/static/paper_detail.js

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-lite/static/paper_detail.js), SHA-256 `7beaa30594770514071f97794f293db933b9bbf1c0fc1ce6e120ac58b26941b8`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
'use strict'; const PaperLite = props => { const p = props.paper; return ( <div
```

Arxiv-sanity-lite backend exposes random/time/text/tag/exemplar ranking, pagination, inspection of TF-IDF and SVM weights, and user-tag/email preferences through lazy per-request database handles. Inspection makes feature contributions visible rather than hiding ranking behind a score. The source uses username-only sessions and a fallback dev signing key, GET mutations and limited old email validation; this is a historical prototype, not a hardened authentication model to adopt. React paper/detail/tag components render scores and links and send prompt-driven add/remove requests, but report responses only to console without refreshing state or explicit error UI. This code was read, not deployed or interacted with.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
'use strict';

const PaperLite = props => {
    const p = props.paper;
    return (
    <div class='rel_paper'>
        <div class='rel_title'><a href={'http://arxiv.org/abs/' + p.id}>{p.title}</a></div>
        <div class='rel_authors'>{p.authors}</div>
        <div class="rel_time">{p.time}</div>
        <div class='rel_tags'>{p.tags}</div>
        <div class='rel_abs'>{p.summary}</div>
    </div>
    )
}

ReactDOM.render(<PaperLite paper={paper} />, document.getElementById('wrap'))

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
