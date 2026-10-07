---
name: firecrawl-via-cli-not-mcp
description: Joshua uses Firecrawl through the CLI skills, not an MCP server - don't re-add the MCP.
metadata:
  type: feedback
---

Firecrawl is set up via `firecrawl-cli` (installed globally, 28 skills in `~/.claude/skills`). On 2026-09-07 the hosted Firecrawl MCP server was added and then deliberately removed at Joshua's request.

**Why:** The CLI skills are strictly more capable (browser interaction, workflow skills like SEO audit and lead gen), and running both was redundant. The hosted MCP also embeds the API key in plaintext in `~/.claude.json`.

**How to apply:** For any live-web task, reach for the `firecrawl-*` skills or the `firecrawl` CLI. Do not re-register the MCP server unless he asks.
