---
type: community
cohesion: 0.05
members: 48
---

# Self-Hosted Gateway and Spend

**Cohesion:** 0.05 - loosely connected
**Members:** 48 nodes

## Members
- [[${ENV_VAR} secret expansion so config can live in version control]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway-config.md
- [[v1organizationsspend_limits admin API]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway-spend-limits.md
- [[Claude Platform on AWS (Anthropic API with AWS auth and Marketplace billing)]] - document - raw/sources/claude-code-docs/en__claude-platform-on-aws.md
- [[Claude apps gateway (self-hosted)]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway.md
- [[Client aborts billed from a conservative floor estimate]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway-spend-limits.md
- [[Cloud session security and isolation layers]] - document - raw/sources/claude-code-docs/en__claude-code-on-the-web.md
- [[Device user-code brute-force resistance]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway-deploy.md
- [[Enable Plugin Suggestions in Managed Settings]] - document - raw/sources/claude-code-docs/en__plugin-relevance.md
- [[Encryption at rest by model provider]] - document - raw/sources/claude-code-docs/en__data-usage.md
- [[Enforce Isolation Across an Organization]] - document - raw/sources/claude-code-docs/en__sandbox-environments.md
- [[Enforce Sandboxing with Managed Settings]] - document - raw/sources/claude-code-docs/en__sandboxing.md
- [[Fail-Closed Startup Enforcement]] - document - raw/sources/claude-code-docs/en__server-managed-settings.md
- [[Gateway deployment container image, Kubernetes, Cloud Run]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway-deploy.md
- [[Gateway on Google Cloud (Cloud Run or GKE, Cloud SQL, Secret Manager)]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway-on-gcp.md
- [[Gateway protocol contract served at GET protocol]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway.md
- [[Gateway threat model summary]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway-deploy.md
- [[GitHub proxy keeping real credentials outside the sandbox]] - document - raw/sources/claude-code-docs/en__claude-code-on-the-web.md
- [[JWT secret rotation and gateway operations]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway-deploy.md
- [[Live enforcement 429 billing_error and the usage meter]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway-spend-limits.md
- [[Managed Marketplace Restrictions]] - document - raw/sources/claude-code-docs/en__plugin-marketplaces.md
- [[Managed Settings and Managed-Only Settings]] - document - raw/sources/claude-code-docs/en__permissions.md
- [[Network access levels None, Trusted, Full, Custom]] - document - raw/sources/claude-code-docs/en__claude-code-on-the-web.md
- [[OIDC identity provider sign-in and IdP group mapping]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway.md
- [[Per-developer spend limits (scope, amount, period)]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway-spend-limits.md
- [[Private-network address requirement at login]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway.md
- [[Provider routing precedence (Bedrock and Foundry win over AWS platform)]] - document - raw/sources/claude-code-docs/en__claude-platform-on-aws.md
- [[Rationale Server-Managed vs Endpoint-Managed Settings]] - document - raw/sources/claude-code-docs/en__server-managed-settings.md
- [[Rationale a trusted gateway can push settings that run commands on developer machines]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway.md
- [[Rationale developer laptops are not trusted, so short-lived JWTs replace raw keys]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway-deploy.md
- [[Rationale one shared upstream credential hides per-developer spend]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway-spend-limits.md
- [[Rationale why run Claude apps gateway (credentials, access control, telemetry, routing)]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway.md
- [[SSRF guard with DNS resolution and IP pinning]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway-deploy.md
- [[Security Approval Dialogs for Delivered Settings]] - document - raw/sources/claude-code-docs/en__server-managed-settings.md
- [[Security proxy and DNS-level audit trail]] - document - raw/sources/claude-code-docs/en__claude-code-on-the-web.md
- [[Server-Managed Settings]] - document - raw/sources/claude-code-docs/en__server-managed-settings.md
- [[Server-Managed Settings Audit Logging]] - document - raw/sources/claude-code-docs/en__server-managed-settings.md
- [[Settings Delivery, Precedence, and Caching]] - document - raw/sources/claude-code-docs/en__server-managed-settings.md
- [[Settings Precedence Order]] - document - raw/sources/claude-code-docs/en__permissions.md
- [[SigV4 credential chain vs workspace API key]] - document - raw/sources/claude-code-docs/en__claude-platform-on-aws.md
- [[Terraform reference for the GCP gateway example]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway-on-gcp.md
- [[Track costs with usage and org dashboards]] - document - raw/sources/claude-code-docs/en__costs.md
- [[Unknown-model fallback pricing tier ($5$25 per million)]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway-spend-limits.md
- [[admin writeread keys, admin_groups, group_limit_mode]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway-config.md
- [[awsAuthRefresh mid-session credential refresh]] - document - raw/sources/claude-code-docs/en__claude-platform-on-aws.md
- [[fail_closed_on_error fail-open vs fail-closed tradeoff]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway-spend-limits.md
- [[gateway.yaml configuration file structure]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway-config.md
- [[store PostgreSQL backing auth state and counters]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway-config.md
- [[upstreams block and multi-provider failover routing]] - document - raw/sources/claude-code-docs/en__claude-apps-gateway-config.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Self-Hosted_Gateway_and_Spend
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Configuration and Environment]]
- 1 edge to [[_COMMUNITY_Auto Mode and Model Providers]]
- 1 edge to [[_COMMUNITY_Plugins and Marketplaces]]
- 1 edge to [[_COMMUNITY_Permissions and Trust Boundaries]]
- 1 edge to [[_COMMUNITY_Code Review and Compliance]]
- 1 edge to [[_COMMUNITY_LLM Gateway and Cost Monitoring]]
- 1 edge to [[_COMMUNITY_Sandboxing and Safety Architecture]]
- 1 edge to [[_COMMUNITY_CLI, Remote Control and Routines]]
- 1 edge to [[_COMMUNITY_Deployment and Rollout]]
- 1 edge to [[_COMMUNITY_Context Window and Compaction]]

## Top bridge nodes
- [[Managed Settings and Managed-Only Settings]] - degree 8, connects to 2 communities
- [[Cloud session security and isolation layers]] - degree 5, connects to 2 communities
- [[Track costs with usage and org dashboards]] - degree 4, connects to 2 communities
- [[Claude apps gateway (self-hosted)]] - degree 13, connects to 1 community
- [[Live enforcement 429 billing_error and the usage meter]] - degree 4, connects to 1 community