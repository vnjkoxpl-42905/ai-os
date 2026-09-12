---
type: community
cohesion: 0.07
members: 27
---

# Code Review and Compliance

**Cohesion:** 0.07 - loosely connected
**Members:** 27 nodes

## Members
- [[code-review local diff review]] - document - raw/sources/claude-code-docs/en__code-review.md
- [[Auto-fix pull requests from PR webhooks]] - document - raw/sources/claude-code-docs/en__claude-code-on-the-web.md
- [[CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC and per-provider defaults]] - document - raw/sources/claude-code-docs/en__data-usage.md
- [[Claude Code on the web cloud session]] - document - raw/sources/claude-code-docs/en__claude-code-on-the-web.md
- [[Code Review (managed multi-agent PR review)]] - document - raw/sources/claude-code-docs/en__code-review.md
- [[Commands across a typical workflow (setup, task, parallel, ship, between)]] - document - raw/sources/claude-code-docs/en__commands.md
- [[Data residency as the gateway's driving requirement]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway.md
- [[Data retention periods and zero data retention]] - document - raw/sources/claude-code-docs/en__data-usage.md
- [[Data training policy by plan type]] - document - raw/sources/claude-code-docs/en__data-usage.md
- [[Finding severity levels Important, Nit, Pre-existing]] - document - raw/sources/claude-code-docs/en__code-review.md
- [[Gateway compliance posture]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway-deploy.md
- [[Gateway data flow table (what reaches Anthropic)]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway-deploy.md
- [[GitHub App vs web-setup authentication]] - document - raw/sources/claude-code-docs/en__claude-code-on-the-web.md
- [[How channels compare to web, Slack, MCP, Remote Control]] - document - raw/sources/claude-code-docs/en__channels.md
- [[Plaintext local storage and cleanupPeriodDays]] - document - raw/sources/claude-code-docs/en__claude-directory.md
- [[REVIEW.md and CLAUDE.md review customization]] - document - raw/sources/claude-code-docs/en__code-review.md
- [[Rationale channels fill the push-into-open-session gap]] - document - raw/sources/claude-code-docs/en__channels.md
- [[Rationale findings don't approve or block so existing workflows stay intact]] - document - raw/sources/claude-code-docs/en__code-review.md
- [[Rationale setup scripts belong to the environment, SessionStart hooks to the repo]] - document - raw/sources/claude-code-docs/en__claude-code-on-the-web.md
- [[Run parallel sessions with git worktrees]] - document - raw/sources/claude-code-docs/en__common-workflows.md
- [[Session quality surveys and transcript-share follow-up]] - document - raw/sources/claude-code-docs/en__data-usage.md
- [[Setup scripts and environment caching]] - document - raw/sources/claude-code-docs/en__claude-code-on-the-web.md
- [[Slash commands catalog]] - document - raw/sources/claude-code-docs/en__commands.md
- [[Telemetry services metrics and error reports]] - document - raw/sources/claude-code-docs/en__data-usage.md
- [[Verification step filtering false positives]] - document - raw/sources/claude-code-docs/en__code-review.md
- [[WebFetch domain safety check]] - document - raw/sources/claude-code-docs/en__data-usage.md
- [[telemetry OTLP metrics, logs, and traces destinations]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway-config.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Code_Review_and_Compliance
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Context Window and Compaction]]
- 1 edge to [[_COMMUNITY_Self-Hosted Gateway and Spend]]

## Top bridge nodes
- [[Commands across a typical workflow (setup, task, parallel, ship, between)]] - degree 4, connects to 1 community
- [[Data residency as the gateway's driving requirement]] - degree 2, connects to 1 community
- [[Plaintext local storage and cleanupPeriodDays]] - degree 2, connects to 1 community