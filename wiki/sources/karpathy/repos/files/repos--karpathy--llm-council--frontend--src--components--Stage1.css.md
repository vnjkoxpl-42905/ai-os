---
type: source
subject: "GitHub source repos/karpathy/llm-council/frontend/src/components/Stage1.css"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm-council/frontend/src/components/Stage1.css]
semantic-status: complete-named-text-read
---

# repos/karpathy/llm-council/frontend/src/components/Stage1.css

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm-council/frontend/src/components/Stage1.css), SHA-256 `333b1ad7c77708fd7aa180ddfb411dadc175e8b93792aa3b90c950171e71f803`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
.stage { margin: 24px 0; padding: 20px; background: #fafafa; border-radius: 8px; border: 1px solid #e0e0e0;
```

Fifteen council UI/style/bootstrap files fully read. Chat input visible only for empty conversation, Enter submits ShiftEnter newline, stage loaders and raw Markdown show each response, ranking and final chair. Stage2 client de-anonymizes labels with disclosure, preserves parsed ranking and aggregate mean plus vote counts for inspection. CSS light scheme, stage colors, code/list spacing and fixed260px sidebar; no responsive or accessibility guarantee, sidebar items are click-only divs and tabs lack tab semantics. React/Vite/main Hello scaffolds not authored epistemic content. Start.sh launches backend and Vite with two-second delay, prints running before health evidence, trap terminates recorded child processes. All source text read, no launch or paid calls.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
.stage {
  margin: 24px 0;
  padding: 20px;
  background: #fafafa;
  border-radius: 8px;
  border: 1px solid #e0e0e0;
}

.stage-title {
  margin: 0 0 16px 0;
  color: #333;
  font-size: 16px;
  font-weight: 600;
}

.tabs {
  display: flex;
  gap: 8px;
  margin-bottom: 16px;
  flex-wrap: wrap;
}

.tab {
  padding: 8px 16px;
  background: #ffffff;
  border: 1px solid #d0d0d0;
  border-radius: 6px 6px 0 0;
  color: #666;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}

.tab:hover {
  background: #f0f0f0;
  color: #333;
  border-color: #4a90e2;
}

.tab.active {
  background: #ffffff;
  color: #4a90e2;
  border-color: #4a90e2;
  border-bottom-color: #ffffff;
  font-weight: 600;
}

.tab-content {
  background: #ffffff;
  padding: 16px;
  border-radius: 6px;
  border: 1px solid #e0e0e0;
}

.model-name {
  color: #888;
  font-size: 12px;
  margin-bottom: 12px;
  font-family: monospace;
}

.response-text {
  color: #333;
  line-height: 1.6;
}

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
