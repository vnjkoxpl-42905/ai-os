---
type: reference
subject: Design connector access and current verification
created: 2026-10-24
updated: 2026-10-24
aliases: [Design MCP health, Design tool connections]
tags: [design, tools, claude, codex]
sources: []
---

# Choose a working design connection

Shared route for Claude Code and Codex. Read [the design hub](README.md) first. This is a dated health snapshot, not a promise that authentication persists. Configured, exposed in the current session, authenticated and successfully tested are different states.

| Tool | Claude Code route | Codex route | Verified 2026-10-24 |
|---|---|---|---|
| Firecrawl | Shared CLI and installed skills | Shared CLI and installed skills | Authenticated CLI 1.26.3; a one-result search succeeded, using 2 credits. Use `py system/scripts/firecrawl-local.py` from the vault to load its saved credential into the child process. Hosted MCP is deliberately not installed. |
| Tavily | Shared `tvly` CLI and installed skills | Shared `tvly` CLI and installed skills | CLI 0.1.8 authenticated; one-result search succeeded. The executable is `tvly`, not `tavily`. |
| 21st.dev | Registered in project `.mcp.json` | Not registered in the inspected home config and not exposed in this Codex session; direct SDK route available | Authenticated direct MCP handshake listed 51 tools; metadata search returned five components. No paid source-code retrieval or generation was attempted. |
| Godly | Project MCP | Home MCP; exposed in this session | Call completed, but dashboard search returned zero results with collection 404 and size-limit warnings. Treat as degraded coverage, not a healthy complete catalogue. |
| MotionSites | Project MCP | Home MCP; exposed in this session | Search metadata returned one dashboard preview. Full prompt retrieval and plan entitlement were not tested. |
| Pinterest | Project MCP | Home MCP; exposed in this session | Blocked: server reports no authenticated Pinterest token. Public browsing is a separate access route and does not establish API authentication. |
| shadcn | Project MCP | Home MCP; exposed in this session | Audit checklist call succeeded. Component registry search depends on the selected project's `components.json`; do not initialize unrelated projects just to pass a probe. |
| Mobbin | Not present in inspected project/global MCP registrations | Home HTTP registration; not exposed in this session | Configured only; authentication and provider request were not tested. A configured URL is not proof of usable access. |
| Kling | No direct entry in inspected Claude project/global MCP registrations; plugin access may differ | Home MCP; exposed in this session | Identity/capability call succeeded, MCP 1.3.3. No image/video job was submitted. Generation is charged and needs the task's specific authorization. |
| REA browser analysis | Global MCP registration | Home MCP; exposed in this session | Registration/exposure confirmed only. Browser inspection requires a known loopback CDP endpoint; not probed against unrelated running browser processes. |
| Playwright + Edge | Local library accessible to shell | Local library accessible to shell | Headless Edge 156.0.4314.42 rendered an in-memory page and its heading was read. This confirms the browser harness launches, not that a dashboard has been visually reviewed. |
| Codex browser panel | Not a Claude tool | `open_in_codex` | Opens a page for Joshua. Merely opening a panel is not screenshot inspection or motion verification. |

## Safe next steps when a connection is unavailable

- Pinterest needs an access token in the environment used to launch its MCP server. Do not paste credentials into chat, notes or this page. Follow the central credential policy and verify the narrow account call after configuring it.
- If 21st is required in Codex's native MCP list, add the supported authenticated registration deliberately; the current working direct SDK probe is evidence of API access, not native registration. The evidence script contains no embedded key and reads the central store at runtime.
- For Mobbin, first refresh/discover the registered connector in the intended runtime, then test a read-only call. Do not infer that a paid subscription or OAuth grant exists from a config entry.
- Reuse existing CLI/browser installations. Check status and one small real call before reinstalling or starting a login flow.

## Evidence and related routes

- [Safe health results](../research/2026-10-24-design-skill-doctor/connections.json)
- [21st direct metadata probe](../research/2026-10-24-design-skill-doctor/connections-21st-probe.mjs) and [result](../research/2026-10-24-design-skill-doctor/connections-21st.json)
- [Libraries and repositories](repositories.md), [design skills](skill-routing-audit.md), [main system connection registry](../connections.md)
- Browser library: `C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/playwright`; use channel `msedge` when appropriate.

Configuration was read without exposing command arguments, headers, URLs containing credentials or environment values. No configuration, authentication grant, application or executable repository was changed by this audit.
