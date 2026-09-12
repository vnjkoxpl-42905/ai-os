# Graph Report - /Users/joshuaf/ai-os/raw/sources/claude-code-docs  (2026-07-20)

## Corpus Check
- Large corpus: 170 files · ~684,188 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder, or use --no-semantic to run AST-only.

## Summary
- 963 nodes · 1239 edges · 21 communities detected
- Extraction: 81% EXTRACTED · 18% INFERRED · 1% AMBIGUOUS · INFERRED: 228 edges (avg confidence: 0.77)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Agent Loop and Context|Agent Loop and Context]]
- [[_COMMUNITY_Core Concepts and Glossary|Core Concepts and Glossary]]
- [[_COMMUNITY_Configuration and Environment|Configuration and Environment]]
- [[_COMMUNITY_Subagents and Agent Teams|Subagents and Agent Teams]]
- [[_COMMUNITY_Deployment and Rollout|Deployment and Rollout]]
- [[_COMMUNITY_Workflows and Worktree Isolation|Workflows and Worktree Isolation]]
- [[_COMMUNITY_Permissions and Trust Boundaries|Permissions and Trust Boundaries]]
- [[_COMMUNITY_Self-Hosted Gateway and Spend|Self-Hosted Gateway and Spend]]
- [[_COMMUNITY_Context Window and Compaction|Context Window and Compaction]]
- [[_COMMUNITY_Auto Mode and Model Providers|Auto Mode and Model Providers]]
- [[_COMMUNITY_CLI, Remote Control and Routines|CLI, Remote Control and Routines]]
- [[_COMMUNITY_MCP and Channels|MCP and Channels]]
- [[_COMMUNITY_Hooks and Memory Files|Hooks and Memory Files]]
- [[_COMMUNITY_Plugins and Marketplaces|Plugins and Marketplaces]]
- [[_COMMUNITY_Skills and Tool Catalog|Skills and Tool Catalog]]
- [[_COMMUNITY_SDK Tools and Data Retention|SDK Tools and Data Retention]]
- [[_COMMUNITY_Sandboxing and Safety Architecture|Sandboxing and Safety Architecture]]
- [[_COMMUNITY_LLM Gateway and Cost Monitoring|LLM Gateway and Cost Monitoring]]
- [[_COMMUNITY_Code Review and Compliance|Code Review and Compliance]]
- [[_COMMUNITY_SDK Skills and Slash Commands|SDK Skills and Slash Commands]]
- [[_COMMUNITY_IDE Integrations and Sessions|IDE Integrations and Sessions]]

## God Nodes (most connected - your core abstractions)
1. `Claude Code Glossary` - 23 edges
2. `Auto Mode` - 18 edges
3. `Model Context Protocol (MCP)` - 17 edges
4. `Subagent` - 15 edges
5. `Plugin` - 15 edges
6. `Desktop Code Tab` - 14 edges
7. `Claude apps gateway (self-hosted)` - 13 edges
8. `Permission Mode` - 13 edges
9. `Subagents in the SDK` - 12 edges
10. `Agent Teams` - 12 edges

## Surprising Connections (you probably didn't know these)
- `Boundaries Stated in Conversation` --semantically_similar_to--> `Allow / Ask / Deny Rules`  [INFERRED] [semantically similar]
  raw/sources/claude-code-docs/en__permission-modes.md → raw/sources/claude-code-docs/en__permissions.md
- `PostToolUse Hook` --semantically_similar_to--> `OpenTelemetry Export`  [INFERRED] [semantically similar]
  raw/sources/claude-code-docs/en__agent-sdk__hooks.md → raw/sources/claude-code-docs/en__agent-sdk__observability.md
- `Hook Matchers` --semantically_similar_to--> `Allow and Deny Rules`  [INFERRED] [semantically similar]
  raw/sources/claude-code-docs/en__agent-sdk__hooks.md → raw/sources/claude-code-docs/en__agent-sdk__permissions.md
- `Add an Adversarial Review Step` --semantically_similar_to--> `Agent Teams`  [INFERRED] [semantically similar]
  raw/sources/claude-code-docs/en__best-practices.md → raw/sources/claude-code-docs/en__agent-teams.md
- `/goal Command` --conceptually_related_to--> `Agent View`  [AMBIGUOUS]
  raw/sources/claude-code-docs/en__goal.md → raw/sources/claude-code-docs/en__agent-view.md

## Hyperedges (group relationships)
- **Permission Decision Pipeline** — en_agent_sdk_hooks_pretooluse, en_agent_sdk_permissions_allow_deny_rules, en_agent_sdk_permissions_permission_modes, en_agent_sdk_permissions_can_use_tool_callback, en_agent_sdk_permissions_permission_evaluation_order [EXTRACTED 1.00]
- **Context Window Budget Management** — en_agent_sdk_agent_loop_context_window, en_agent_sdk_agent_loop_automatic_compaction, en_agent_sdk_mcp_tool_search, en_agent_sdk_claude_code_features_claude_md, en_agent_sdk_agent_loop_effort_level [INFERRED 0.85]
- **Session Durability on Stateless Hosts** — en_agent_sdk_hosting_subprocess_model, en_agent_sdk_hosting_local_disk_state, en_agent_sdk_session_storage_session_store, en_agent_sdk_session_storage_dual_write_architecture, en_agent_sdk_sessions_resume_by_id [INFERRED 0.88]
- **Four ways Claude Code parallelizes work** — en_agents_run_agents_in_parallel, en_agent_sdk_subagents_subagents, en_agent_view_agent_view, en_agent_teams_agent_teams, en_agents_dynamic_workflows, en_agents_worktrees [EXTRACTED 1.00]
- **Context-budget discipline across SDK features** — en_best_practices_context_window_constraint, en_agent_sdk_tool_search_tool_search, en_agent_sdk_subagents_context_isolation, en_agent_sdk_slash_commands_compact, en_agent_sdk_skills_skills_option [INFERRED 0.82]
- **Permission and trust layer governing autonomous runs** — en_auto_mode_config_classifier, en_auto_mode_config_human_checkpoint, en_agent_sdk_typescript_permission_mode, en_agent_sdk_user_input_tool_approval_requests, en_changelog_permission_check_hardening [INFERRED 0.85]
- **Gateway control plane: config, identity, storage, spend enforcement, telemetry** — en_claude_apps_gateway_gateway, en_claude_apps_gateway_config_gateway_yaml, en_claude_apps_gateway_oidc_sso, en_claude_apps_gateway_config_store_postgres, en_claude_apps_gateway_spend_limits_enforcement, en_claude_apps_gateway_config_telemetry [EXTRACTED 0.95]
- **Managing the context budget across compaction, checkpoints, skills, and cost controls** — en_context_window_context_window, en_context_window_compaction, en_checkpointing_restore_vs_summarize, en_costs_claude_md_to_skills, en_common_workflows_delegate_research_subagents, en_chrome_rationale_default_context_cost [INFERRED 0.80]
- **Defending the session against untrusted external input** — en_channels_reference_sender_gating, en_channels_reference_untrusted_field_sanitization, en_computer_use_rationale_terminal_excluded, en_claude_code_on_the_web_security_proxy, en_data_usage_webfetch_safety_check [INFERRED 0.75]
- **Configuration Diagnosis Flow** — en_debug_your_config_context_command, en_debug_your_config_doctor_command, en_debug_your_config_safe_mode, en_debug_your_config_settings_precedence, en_glossary_settings_layers [EXTRACTED 1.00]
- **Ways to Keep Claude Working Unattended** — en_goal_command, en_desktop_scheduled_tasks_local_task, en_desktop_scheduled_tasks_comparison, en_auto_mode_config_auto_mode, en_glossary_verification_loop [INFERRED 0.82]
- **Enterprise Routing, Credentials, and Policy Delivery** — en_gateways_concept, en_gateways_claude_apps_gateway, en_devcontainer_managed_settings, en_feature_availability_by_provider, en_env_vars_anthropic_base_url, en_google_vertex_ai_setup [INFERRED 0.80]
- **Hook decision pipeline: event fires, matcher/if filters, script returns exit code or JSON, permission layer adjudicates** — en_hooks_hook_lifecycle, en_agent_sdk_hooks_hook_matchers, en_hooks_guide_if_field, en_hooks_guide_exit_codes, en_hooks_guide_structured_json_output, en_hooks_guide_permission_mode_interaction [EXTRACTED 1.00]
- **Cross-session knowledge stack: CLAUDE.md, rules, auto memory, and compaction jointly determine what Claude knows at session start** — en_memory_claude_md, en_memory_claude_rules, en_glossary_auto_memory, en_context_window_context_window, en_agent_sdk_agent_loop_automatic_compaction [EXTRACTED 1.00]
- **Enterprise routing and governance: gateway, network config, model restrictions, managed MCP, and telemetry form the org control plane** — en_llm_gateway_gateway, en_llm_gateway_rollout_steps, en_network_config_proxy, en_model_config_model_restrictions, en_managed_mcp_managed_mcp_json, en_monitoring_usage_otel_telemetry [INFERRED 0.80]
- **Layered Agent Safety: Permission Rules, Modes, Classifier, and Isolation** — en_permissions_allow_ask_deny_rules, en_glossary_permission_mode, en_permission_modes_classifier, en_sandboxing_sandboxed_bash_tool, en_security_permission_based_architecture [INFERRED 0.85]
- **Plugin Distribution Pipeline: Manifest, Dependencies, Marketplace, Relevance, Hints** — en_plugins_reference_plugin_manifest, en_plugin_dependencies_dependency_constraint, en_plugin_marketplaces_marketplace, en_plugin_relevance_relevance, en_plugin_hints_plugin_hint [EXTRACTED 1.00]
- **Organization-Wide Configuration Control** — en_permissions_managed_settings, en_server_managed_settings_server_managed_settings, en_sandboxing_managed_enforcement, en_plugin_marketplaces_managed_restrictions, en_sandbox_environments_org_enforcement [INFERRED 0.80]
- **Forked skill execution in a subagent** — en_skills_skill, en_skills_context_fork, en_sub_agents_builtin_subagents, en_sub_agents_preload_skills, en_tools_reference_agent_tool [EXTRACTED 0.90]
- **Configuration precedence stack across scopes** — en_settings_configuration_scopes, en_settings_settings_files, en_settings_managed_settings, en_settings_settings_precedence, en_skills_where_skills_live [EXTRACTED 0.85]
- **Non-terminal surfaces for running Claude Code** — en_web_quickstart_claude_code_on_web, en_slack_claude_code_in_slack, en_vs_code_extension, en_ultraplan_ultraplan, en_ultrareview_ultrareview [INFERRED 0.80]
- **Worktree Lifecycle: Create, Isolate, Clean Up** — en_worktrees_worktree_flag, en_worktrees_worktreeinclude, en_worktrees_baseref, en_worktrees_worktree_cleanup, en_worktrees_worktree_lock [EXTRACTED 1.00]
- **Workflow Authoring Loop: Trigger, Approve, Run, Save** — en_workflows_ultracode_keyword, en_workflows_workflow_approval, en_workflows_workflows_command, en_workflows_saved_workflow, en_workflows_workflow_args [EXTRACTED 1.00]
- **ZDR Enterprise Control Surface** — en_zero_data_retention_zdr, en_zero_data_retention_force_login, en_zero_data_retention_disabled_features, en_zero_data_retention_fable_5_unavailable [EXTRACTED 1.00]

## Communities

### Community 0 - "Agent Loop and Context"
Cohesion: 0.03
Nodes (89): Rationale: Consult at Decision Points Rather Than Every Turn, advisorModel Setting, Advisor Tool, Advisor vs opusplan vs Subagents vs /model, Advisor Model Pairing Capability Check, Advisor Impact on Prompt Caching, The Agent Loop, Automatic Compaction (+81 more)

### Community 1 - "Core Concepts and Glossary"
Cohesion: 0.03
Nodes (85): Rationale: CLAUDE.md Guides, Permissions Guarantee, Common Configuration Failure Causes, /context Command, /doctor Setup Checkup, Hook Inspection with /hooks, MCP Server Check with /mcp, Debug Your Configuration, claude-cli:// URL Scheme (+77 more)

### Community 2 - "Configuration and Environment"
Cohesion: 0.04
Nodes (67): Safe Mode Clean-Configuration Test, Resolved Settings Precedence, Desktop Enterprise Configuration, Scheduled Task SKILL.md on Disk, Claude Code Dev Container Feature, Container Egress Firewall, Managed Settings in a Dev Container, Persist ~/.claude Across Rebuilds (+59 more)

### Community 3 - "Subagents and Agent Teams"
Cohesion: 0.03
Nodes (65): Streaming Message Flow, StreamEvent, Streaming Output (real-time responses), Streaming UI Pattern, Context Persistence Across Turns, Rationale: streaming input is preferred because the agent lives as a long-lived process handling interrupts, permissions, and session state, Single Message Input, Streaming Input Mode (+57 more)

### Community 4 - "Deployment and Rollout"
Cohesion: 0.04
Nodes (56): Prompt recipes for common tasks, Champion recruitment and pilot group variants, Rollout launch announcement templates, Tips and tricks enablement campaign, Manage Context (/clear, /compact, /context), /export Rendered Transcript, Rationale: Transcript Entry Format Is Internal and Unstable, Script Access Interfaces to Conversations (+48 more)

### Community 5 - "Workflows and Worktree Isolation"
Cohesion: 0.04
Nodes (48): Resume by PR URL, History Search Across All Projects, Safer Automatic Edits, Move a Session With /cd, Subagents Can Spawn Subagents, Set Any Setting From the Prompt, Subagents Run in the Background by Default, Adversarial Cross-Check Quality Pattern (+40 more)

### Community 6 - "Permissions and Trust Boundaries"
Cohesion: 0.05
Nodes (48): Permission relay to a remote channel, Rationale: an ungated channel is a prompt injection vector, Five-letter request_id alphabet without 'l', Gate inbound messages on sender identity, Sanitizing description and input_preview as untrusted, Machine-wide computer use lock (one session at a time), Per-session app approval and sentinel warnings, Rationale: terminal excluded from screenshots to block feedback injection (+40 more)

### Community 7 - "Self-Hosted Gateway and Spend"
Cohesion: 0.05
Nodes (48): admin: write/read keys, admin_groups, group_limit_mode, gateway.yaml configuration file structure, ${ENV_VAR} secret expansion so config can live in version control, store: PostgreSQL backing auth state and counters, upstreams block and multi-provider failover routing, Gateway deployment: container image, Kubernetes, Cloud Run, JWT secret rotation and gateway operations, Rationale: developer laptops are not trusted, so short-lived JWTs replace raw keys (+40 more)

### Community 8 - "Context Window and Compaction"
Cohesion: 0.05
Nodes (47): Checkpoint (pre-prompt code snapshot), Checkpoint limitations: bash and external changes untracked, Rationale: checkpoints are local undo, Git is permanent history, Restore vs. summarize semantics, /rewind menu: restore and summarize actions, Browser tools in plan mode: read-only vs state-changing, Browser file upload restrictions (permissions, 10MB, hard links), Claude Code Chrome integration (+39 more)

### Community 9 - "Auto Mode and Model Providers"
Cohesion: 0.05
Nodes (44): PermissionMode and CanUseTool, Tool Approval Requests, Claude Code on Amazon Bedrock, AWS Guardrails, Bedrock IAM Configuration, Bedrock Inference Profiles and Model Pinning, Mantle Endpoint, 1M Token Context Window (+36 more)

### Community 10 - "CLI, Remote Control and Routines"
Cohesion: 0.05
Nodes (43): Move tasks between web and terminal (--cloud and --teleport), CLI commands (claude, -p, --continue, --resume, update), CLI flags reference, Pipe Claude into scripts (non-interactive -p), Claude Code (Agentic Coding Tool), Customization via CLAUDE.md, Skills, and Hooks, Installation Methods (native, Homebrew, WinGet, apt/dnf/apk), Model Context Protocol Integration (+35 more)

### Community 11 - "MCP and Channels"
Cohesion: 0.06
Nodes (40): Channel (MCP server that pushes events), claude/channel capability declaration, --dangerously-load-development-channels, Model Context Protocol (MCP) and stdio transport, notifications/claude/channel event payload format, Channel reply tool (two-way channels), Webhook receiver channel walkthrough, Channels research preview and Anthropic-curated allowlist (+32 more)

### Community 12 - "Hooks and Memory Files"
Cohesion: 0.07
Nodes (38): Hook Matchers, Background task termination at exit, Bare mode (--bare), Rationale: bare mode gives identical results on every machine, CLAUDE_ENV_FILE script preamble, ConfigChange hook event, CwdChanged hook event, FileChanged hook event (+30 more)

### Community 13 - "Plugins and Marketplaces"
Cohesion: 0.06
Nodes (38): channelsEnabled / allowedChannelPlugins enterprise controls, Package a channel as a plugin and publish to a marketplace, Community Marketplace, Plugin Marketplace Concept, Team Marketplaces via extraKnownMarketplaces, Plugin Marketplaces on GHES, Plugin, Plugin Dependency Version Constraint (+30 more)

### Community 14 - "Skills and Tool Catalog"
Cohesion: 0.06
Nodes (38): Exclude Sensitive Files, Permission Settings, Sandbox Settings and Path Prefixes, Agent Skills Open Standard (agentskills.io), Pre-approve Tools for a Skill (allowed-tools), Bundled Skills, Dynamic Context Injection (!`command`), Skill Frontmatter Reference (+30 more)

### Community 15 - "SDK Tools and Data Retention"
Cohesion: 0.06
Nodes (37): Accessibility Settings Beyond Screen Reader Mode, Screen Reader Mode, API Provider Choice, Managed Settings Distribution to Devices, Organization Setup for Claude Code, Organization Policy Enforcement, Custom Tools, Structured Data Tool Returns (+29 more)

### Community 16 - "Sandboxing and Safety Architecture"
Cohesion: 0.06
Nodes (33): Classifier Allowed-by-Default Categories, Classifier Blocked-by-Default Categories, Auto Mode Safety Classifier, Boundaries Stated in Conversation, Three-Point Subagent Classifier Check, Rationale: Transcripts Are Session State, Not Working Files, Rationale: additionalDirectories Grant File Access, Not Configuration, Rationale: Rules Are Enforced by Claude Code, Not by the Model (+25 more)

### Community 17 - "LLM Gateway and Cost Monitoring"
Cohesion: 0.07
Nodes (29): Structured output with --json-schema, Output formats (text, json, stream-json), Streaming stream-json event protocol, system/init session metadata event, Healthcare compliance (BAA), Usage policy and credential use, apiKeyHelper credential rotation, Gateway credential variable (+21 more)

### Community 18 - "Code Review and Compliance"
Cohesion: 0.07
Nodes (27): How channels compare to web, Slack, MCP, Remote Control, Rationale: channels fill the push-into-open-session gap, telemetry: OTLP metrics, logs, and traces destinations, Data residency as the gateway's driving requirement, Gateway compliance posture, Gateway data flow table (what reaches Anthropic), Auto-fix pull requests from PR webhooks, Claude Code on the web cloud session (+19 more)

### Community 19 - "SDK Skills and Slash Commands"
Cohesion: 0.08
Nodes (25): Agent Skills in the SDK, allowed-tools Frontmatter (CLI only), Rationale: Skills are model-invoked filesystem artifacts, not a programmatic API, settingSources / setting_sources Option, Skill Locations (project, user, plugin), SKILL.md File, skills Option (context filter), Command Arguments and Placeholders (+17 more)

### Community 20 - "IDE Integrations and Sessions"
Cohesion: 0.12
Nodes (18): Execution environments (local, cloud, remote control), Built-in IDE MCP server, JetBrains IDE plugin, Claude Code mobile app, Remote Control from mobile, Branch a Session (/branch, --fork-session), Rationale: Name Sessions for Parallel Work, Resume a Session (+10 more)

## Ambiguous Edges - Review These
- `Screen Reader Mode` → `Managed Settings Distribution to Devices`  [AMBIGUOUS]
  raw/sources/claude-code-docs/en__accessibility.md · relation: conceptually_related_to
- `Agent View` → `/goal Command`  [AMBIGUOUS]
  raw/sources/claude-code-docs/en__whats-new__2026-w20.md · relation: conceptually_related_to
- `Auto Mode` → `Common Failure Patterns`  [AMBIGUOUS]
  raw/sources/claude-code-docs/en__auto-mode-config.md · relation: conceptually_related_to
- `Rollout launch announcement templates` → `Track costs with /usage and org dashboards`  [AMBIGUOUS]
  raw/sources/claude-code-docs/en__communications-kit.md · relation: references
- `Healthcare compliance (BAA)` → `Audit security events / send to SIEM`  [AMBIGUOUS]
  raw/sources/claude-code-docs/en__legal-and-compliance.md · relation: conceptually_related_to
- `Usage policy and credential use` → `Gateway credential variable`  [AMBIGUOUS]
  raw/sources/claude-code-docs/en__legal-and-compliance.md · relation: conceptually_related_to
- `Shell Mode Responds to Command Output` → `/radio`  [AMBIGUOUS]
  raw/sources/claude-code-docs/en__whats-new__2026-w26.md · relation: conceptually_related_to

## Knowledge Gaps
- **354 isolated node(s):** `Accessibility Settings Beyond Screen Reader Mode`, `advisorModel Setting`, `Rationale: Consult at Decision Points Rather Than Every Turn`, `Advisor vs opusplan vs Subagents vs /model`, `Turn` (+349 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Screen Reader Mode` and `Managed Settings Distribution to Devices`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Agent View` and `/goal Command`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Auto Mode` and `Common Failure Patterns`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Rollout launch announcement templates` and `Track costs with /usage and org dashboards`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `Healthcare compliance (BAA)` and `Audit security events / send to SIEM`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Usage policy and credential use` and `Gateway credential variable`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Shell Mode Responds to Command Output` and `/radio`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._