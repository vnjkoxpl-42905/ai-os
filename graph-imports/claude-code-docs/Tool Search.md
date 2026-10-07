---
source_file: "raw/sources/claude-code-docs/en__agent-sdk__tool-search.md"
type: "document"
community: "Subagents and Agent Teams"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Subagents_and_Agent_Teams
---

# Tool Search

## Connections
- [[ENABLE_TOOL_SEARCH Environment Variable]] - `implements` [EXTRACTED]
- [[McpServerConfig]] - `references` [EXTRACTED]
- [[Rationale tool definitions eat context and selection accuracy degrades past 30-50 tools, so definitions are deferred and loaded on demand]] - `rationale_for` [EXTRACTED]
- [[Rationale tool search costs one extra round-trip, so loading everything upfront is faster under ~10 tools]] - `rationale_for` [EXTRACTED]
- [[tool_reference Content Block  defer_loading]] - `references` [EXTRACTED]


## Source
- Full document: [[en__agent-sdk__tool-search]]
- Live docs: https://code.claude.com/docs/en/agent-sdk/tool-search

#graphify/document #graphify/EXTRACTED #community/Subagents_and_Agent_Teams
