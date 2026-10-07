---
name: web-research-uses-firecrawl-credits
description: Whenever searching or reading the web, use Firecrawl (CLI / firecrawl-* skills), never WebSearch/WebFetch; spend Firecrawl credits, not Claude credits.
metadata:
  type: feedback
---

For any live-web task (searching, reading a page, finding a repo, checking docs), use the Firecrawl CLI via the `firecrawl` / `firecrawl-search` / `firecrawl-scrape` skills. Do not reach for the built-in WebSearch or WebFetch tools.

**Why:** Joshua said so on 2026-09-11. He pays for Firecrawl credits separately and wants web work billed there rather than against his Claude usage. Firecrawl also returns cleaner markdown than WebFetch.

**How to apply:** Before any web lookup, route through `firecrawl search` / `firecrawl scrape` in Bash. Local CLIs that are not web fetches (`gh`, `gws`) are fine to use directly. Related: [[firecrawl-via-cli-not-mcp]].

**Auth note (2026-09-11):** the CLI is not logged in on this machine; `firecrawl --status` says "Not authenticated". The key is `FIRECRAWL_API_KEY` in `dev/ai-os/.env`. Export it for the command (`export FIRECRAWL_API_KEY="$(grep '^FIRECRAWL_API_KEY=' .env | cut -d= -f2-)"`) and never print it. Balance was 10,457 credits.
