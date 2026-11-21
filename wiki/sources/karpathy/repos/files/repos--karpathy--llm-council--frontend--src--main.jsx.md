---
type: source
subject: "GitHub source repos/karpathy/llm-council/frontend/src/main.jsx"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm-council/frontend/src/main.jsx]
semantic-status: complete-named-text-read
---

# repos/karpathy/llm-council/frontend/src/main.jsx

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm-council/frontend/src/main.jsx), SHA-256 `4b4b864dbe45253425d0c925337180ec07e204295179f80f59551216f466f618`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
import { StrictMode } from 'react' import { createRoot } from 'react-dom/client' import './index.css' import
```

Fifteen council UI/style/bootstrap files fully read. Chat input visible only for empty conversation, Enter submits ShiftEnter newline, stage loaders and raw Markdown show each response, ranking and final chair. Stage2 client de-anonymizes labels with disclosure, preserves parsed ranking and aggregate mean plus vote counts for inspection. CSS light scheme, stage colors, code/list spacing and fixed260px sidebar; no responsive or accessibility guarantee, sidebar items are click-only divs and tabs lack tab semantics. React/Vite/main Hello scaffolds not authored epistemic content. Start.sh launches backend and Vite with two-second delay, prints running before health evidence, trap terminates recorded child processes. All source text read, no launch or paid calls.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
