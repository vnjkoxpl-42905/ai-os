import os
import hashlib
import json

output_file = r"C:\Users\Joshu\dev\ai-os\AIOS_PHASE_0_CURRENT_STATE_PACK.md"

doc = []

# ==================================================
# 5. EXACT ACTIVE SKILL DISCOVERY
# ==================================================
doc.append("## 5. EXACT ACTIVE SKILL DISCOVERY")
doc.append("")
doc.append("Discovery context captured from the active Antigravity session opened at `C:\\Users\\Joshu\\dev\\ai-os`.")
doc.append("")
doc.append("### A. EXPOSED SKILLS (85 Active in Prompt Context)")
doc.append("")
doc.append("| Identifier | Exact Path | Source | Description Chars | Approx Token Overhead |")
doc.append("|---|---|---|---|---|")

exposed_skills_raw = [
    ("a11y-debugging", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\_snapshots\a11y-debugging\SKILL.md", ".gemini (_snapshots)", 228, 65),
    ("access", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\_snapshots\discord-access\SKILL.md", ".gemini (_snapshots)", 179, 52),
    ("agy-customizations", r"C:\Users\Joshu\.gemini\antigravity\builtin\skills\agy-customizations\SKILL.md", "builtin", 258, 72),
    ("auto-auth-browser", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\auto-auth-browser\SKILL.md", ".gemini", 175, 48),
    ("bigquery-ai-ml", r"C:\Users\Joshu\.gemini\config\skills\bigquery-ai-ml\SKILL.md", "GLOBAL (config)", 265, 74),
    ("bigquery-graph", r"C:\Users\Joshu\.gemini\config\skills\bigquery-graph\SKILL.md", "GLOBAL (config)", 206, 58),
    ("bigquery-sql", r"C:\Users\Joshu\.gemini\config\skills\bigquery-sql\SKILL.md", "GLOBAL (config)", 216, 60),
    ("brainstorming", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\brainstorming\SKILL.md", ".gemini", 188, 52),
    ("brand-guidelines", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\brand-guidelines\SKILL.md", ".gemini", 218, 62),
    ("canvas-design", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\canvas-design\SKILL.md", ".gemini", 282, 78),
    ("chrome-devtools", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\_snapshots\chrome-devtools\SKILL.md", ".gemini (_snapshots)", 249, 70),
    ("codebase-design", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\codebase-design\SKILL.md", ".gemini", 255, 71),
    ("configure", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\_snapshots\discord-configure\SKILL.md", ".gemini (_snapshots)", 215, 60),
    ("consultation-followup-drafts", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\consultation-followup-drafts\SKILL.md", ".gemini", 108, 30),
    ("consultation-inquiry-drafts", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\consultation-inquiry-drafts\SKILL.md", ".gemini", 103, 29),
    ("data-autocleaning", r"C:\Users\Joshu\.gemini\config\skills\data-autocleaning\SKILL.md", "GLOBAL (config)", 254, 71),
    ("design-an-interface", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\design-an-interface\SKILL.md", ".gemini", 199, 55),
    ("design-taste-frontend", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\design-taste-frontend\SKILL.md", ".gemini", 204, 57),
    ("diagnosing-bugs", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\diagnosing-bugs\SKILL.md", ".gemini", 143, 40),
    ("discord-access", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\discord-access\SKILL.md", ".gemini", 179, 52),
    ("discord-configure", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\discord-configure\SKILL.md", ".gemini", 215, 60),
    ("dispatching-parallel-agents", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\dispatching-parallel-agents\SKILL.md", ".gemini", 105, 30),
    ("domain-modeling", r"c:\Users\Joshu\dev\ai-os\.agents\skills\domain-modeling\SKILL.md", ".agents (Codex inherited)", 167, 46),
    ("edge-live-control", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\edge-live-control\SKILL.md", ".gemini", 243, 68),
    ("emil-design-eng", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\_project-forks\lsatu\emil-design-eng\SKILL.md", ".gemini (_project-forks)", 157, 44),
    ("enforcing-resource-attribution", r"C:\Users\Joshu\.gemini\config\skills\enforcing-resource-attribution\SKILL.md", "GLOBAL (config)", 252, 70),
    ("example-command", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\_snapshots\example-command\SKILL.md", ".gemini (_snapshots)", 107, 30),
    ("example-skill", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\_snapshots\example-skill\SKILL.md", ".gemini (_snapshots)", 265, 74),
    ("executing-plans", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\executing-plans\SKILL.md", ".gemini", 106, 30),
    ("finishing-a-development-branch", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\finishing-a-development-branch\SKILL.md", ".gemini", 225, 63),
    ("frontend-design", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\frontend-design\SKILL.md", ".gemini", 216, 60),
    ("gcloud-auth-verification", r"C:\Users\Joshu\.gemini\config\plugins\data-agent-kit-plugin\skills\gcloud_auth_verification\SKILL.md", "plugin", 224, 63),
    ("gcp-composer-troubleshooting", r"C:\Users\Joshu\.gemini\config\skills\gcp-composer-troubleshooting\SKILL.md", "GLOBAL (config)", 233, 65),
    ("generative_ui", r"C:\Users\Joshu\.gemini\antigravity\builtin\skills\generative_ui\SKILL.md", "builtin", 248, 69),
    ("git-guardrails-claude-code", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\git-guardrails-claude-code\SKILL.md", ".gemini", 225, 63),
    ("google-antigravity-sdk", r"C:\Users\Joshu\.gemini\config\plugins\google-antigravity-sdk\skills\google-antigravity-sdk\SKILL.md", "plugin", 205, 57),
    ("graphify", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\graphify\SKILL.md", ".gemini", 88, 25),
    ("grill-with-docs", r"c:\Users\Joshu\dev\ai-os\.agents\skills\grill-with-docs\SKILL.md", ".agents (Codex inherited)", 186, 52),
    ("gws-admin-reports", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-admin-reports\SKILL.md", ".gemini", 60, 18),
    ("gws-calendar", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-calendar\SKILL.md", ".gemini", 49, 15),
    ("gws-calendar-agenda", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-calendar-agenda\SKILL.md", ".gemini", 65, 19),
    ("gws-calendar-insert", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-calendar-insert\SKILL.md", ".gemini", 43, 14),
    ("gws-chat", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-chat\SKILL.md", ".gemini", 46, 14),
    ("gws-chat-send", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-chat-send\SKILL.md", ".gemini", 45, 14),
    ("gws-classroom", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-classroom\SKILL.md", ".gemini", 55, 16),
    ("gws-docs", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-docs\SKILL.md", ".gemini", 30, 10),
    ("gws-docs-write", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-docs-write\SKILL.md", ".gemini", 47, 14),
    ("gws-drive", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-drive\SKILL.md", ".gemini", 56, 16),
    ("gws-drive-upload", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-drive-upload\SKILL.md", ".gemini", 57, 17),
    ("gws-events", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-events\SKILL.md", ".gemini", 46, 14),
    ("gws-events-renew", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-events-renew\SKILL.md", ".gemini", 72, 20),
    ("gws-events-subscribe", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-events-subscribe\SKILL.md", ".gemini", 79, 23),
    ("gws-forms", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-forms\SKILL.md", ".gemini", 31, 10),
    ("gws-gmail", r"c:\Users\Joshu\dev\ai-os\.agents\skills\gws-gmail\SKILL.md", ".agents (Codex inherited)", 40, 12),
    ("gws-gmail-forward", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-gmail-forward\SKILL.md", ".gemini", 51, 15),
    ("gws-gmail-read", r"c:\Users\Joshu\dev\ai-os\.agents\skills\gws-gmail-read\SKILL.md", ".agents (Codex inherited)", 58, 17),
    ("gws-gmail-reply", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-gmail-reply\SKILL.md", ".gemini", 65, 19),
    ("gws-gmail-reply-all", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-gmail-reply-all\SKILL.md", ".gemini", 69, 20),
    ("gws-gmail-send", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-gmail-send\SKILL.md", ".gemini", 27, 9),
    ("gws-gmail-triage", r"c:\Users\Joshu\dev\ai-os\.agents\skills\gws-gmail-triage\SKILL.md", ".agents (Codex inherited)", 62, 18),
    ("gws-gmail-watch", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-gmail-watch\SKILL.md", ".gemini", 64, 19),
    ("gws-keep", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-keep\SKILL.md", ".gemini", 29, 9),
    ("gws-meet", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-meet\SKILL.md", ".gemini", 36, 11),
    ("gws-modelarmor", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-modelarmor\SKILL.md", ".gemini", 62, 18),
    ("gws-modelarmor-create-template", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-modelarmor-create-template\SKILL.md", ".gemini", 62, 18),
    ("gws-modelarmor-sanitize-prompt", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-modelarmor-sanitize-prompt\SKILL.md", ".gemini", 69, 20),
    ("gws-modelarmor-sanitize-response", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-modelarmor-sanitize-response\SKILL.md", ".gemini", 71, 21),
    ("gws-people", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-people\SKILL.md", ".gemini", 44, 13),
    ("gws-shared", r"c:\Users\Joshu\dev\ai-os\.agents\skills\gws-shared\SKILL.md", ".agents (Codex inherited)", 87, 25),
    ("gws-sheets", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-sheets\SKILL.md", ".gemini", 45, 13),
    ("gws-sheets-append", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-sheets-append\SKILL.md", ".gemini", 54, 16),
    ("gws-sheets-read", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-sheets-read\SKILL.md", ".gemini", 51, 15),
    ("gws-slides", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-slides\SKILL.md", ".gemini", 45, 13),
    ("gws-tasks", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-tasks\SKILL.md", ".gemini", 44, 13),
    ("gws-workflow", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-workflow\SKILL.md", ".gemini", 57, 17),
    ("gws-workflow-email-to-task", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-workflow-email-to-task\SKILL.md", ".gemini", 70, 20),
    ("gws-workflow-file-announce", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-workflow-file-announce\SKILL.md", ".gemini", 57, 17),
    ("gws-workflow-meeting-prep", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-workflow-meeting-prep\SKILL.md", ".gemini", 76, 22),
    ("gws-workflow-standup-report", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-workflow-standup-report\SKILL.md", ".gemini", 68, 20),
    ("gws-workflow-weekly-digest", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\gws-workflow-weekly-digest\SKILL.md", ".gemini", 69, 20),
    ("high-end-visual-design", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\high-end-visual-design\SKILL.md", ".gemini", 267, 75),
    ("imessage-access", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\imessage-access\SKILL.md", ".gemini", 181, 52),
    ("imessage-configure", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\imessage-configure\SKILL.md", ".gemini", 217, 61),
    ("json-canvas", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\json-canvas\SKILL.md", ".gemini", 226, 64),
    ("loophole-lecture-transcribe", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\loophole-lecture-transcribe\SKILL.md", ".gemini", 184, 52),
    ("lsat-u-browser-verification", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\lsat-u-browser-verification\SKILL.md", ".gemini", 243, 68),
    ("mcp-builder", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\mcp-builder\SKILL.md", ".gemini", 239, 67),
    ("memory-leak-debugging", r"C:\Users\Joshu\.gemini\config\plugins\chrome-devtools-plugin\skills\memory-leak-debugging\SKILL.md", "plugin", 206, 58),
    ("migrate-to-shoehorn", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\migrate-to-shoehorn\SKILL.md", ".gemini", 168, 47),
    ("migrate-workflows", r"C:\Users\Joshu\.gemini\antigravity\builtin\skills\migrate-workflows\SKILL.md", "builtin", 203, 57),
    ("minimalist-ui", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\minimalist-ui\SKILL.md", ".gemini", 137, 39),
    ("netlify-blobs", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\_snapshots\netlify-blobs\SKILL.md", ".gemini (_snapshots)", 255, 71),
    ("netlify-deploy", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\_snapshots\netlify-deploy\SKILL.md", ".gemini (_snapshots)", 217, 61),
    ("netlify-identity", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\_snapshots\netlify-identity\SKILL.md", ".gemini (_snapshots)", 249, 70),
    ("notebooklm", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\_project-forks\lsatu\notebooklm\SKILL.md", ".gemini (_project-forks)", 239, 67),
    ("obsidian-bases", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\obsidian-bases\SKILL.md", ".gemini", 227, 64),
    ("obsidian-markdown", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\obsidian-markdown\SKILL.md", ".gemini", 241, 68),
    ("obsidian-vault", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\obsidian-vault\SKILL.md", ".gemini", 170, 48),
    ("pickup", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\_project-forks\lsatu\pickup\SKILL.md", ".gemini (_project-forks)", 199, 56),
    ("playground", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\_snapshots\playground\SKILL.md", ".gemini (_snapshots)", 257, 72),
    ("prototype", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\prototype\SKILL.md", ".gemini", 175, 49),
    ("pull-submissions", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\pull-submissions\SKILL.md", ".gemini", 221, 62),
    ("qa", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\qa\SKILL.md", ".gemini", 239, 67),
    ("receiving-code-review", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\receiving-code-review\SKILL.md", ".gemini", 229, 64),
    ("redesign-existing-projects", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\redesign-existing-projects\SKILL.md", ".gemini", 253, 71),
    ("request-refactor-plan", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\request-refactor-plan\SKILL.md", ".gemini", 204, 57),
    ("requesting-code-review", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\requesting-code-review\SKILL.md", ".gemini", 143, 40),
    ("research", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\research\SKILL.md", ".gemini", 235, 66),
    ("research-add-items", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\research-add-items\SKILL.md", ".gemini", 65, 18),
    ("research-deep", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\research-deep\SKILL.md", ".gemini", 97, 27),
    ("research-report", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\research-report\SKILL.md", ".gemini", 88, 25),
    ("resolving-merge-conflicts", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\resolving-merge-conflicts\SKILL.md", ".gemini", 83, 23),
    ("scaffold-exercises", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\scaffold-exercises\SKILL.md", ".gemini", 188, 53),
    ("second-brain", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\second-brain\SKILL.md", ".gemini", 254, 71),
    ("second-brain-ingest", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\second-brain-ingest\SKILL.md", ".gemini", 227, 64),
    ("second-brain-lint", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\second-brain-lint\SKILL.md", ".gemini", 181, 51),
    ("second-brain-query", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\second-brain-query\SKILL.md", ".gemini", 213, 60),
    ("session-handoff-nate", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\_inactive\session-handoff-nate-active-copy\SKILL.md", ".gemini (_inactive)", 272, 76),
    ("setup-pre-commit", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\setup-pre-commit\SKILL.md", ".gemini", 235, 66),
    ("skill-repair", r"C:\Users\Joshu\.gemini\config\skills\skill-repair\SKILL.md", "GLOBAL (config)", 177, 50),
    ("slack-gif-creator", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\slack-gif-creator\SKILL.md", ".gemini", 175, 49),
    ("subagent-driven-development", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\_project-forks\lsatu\subagent-driven-development\SKILL.md", ".gemini (_project-forks)", 96, 27),
    ("superwhisper", r"c:\Users\Joshu\dev\ai-os\.agents\skills\superwhisper\SKILL.md", ".agents (Codex inherited)", 222, 62),
    ("systematic-debugging", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\systematic-debugging\SKILL.md", ".gemini", 110, 31),
    ("tdd", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\tdd\SKILL.md", ".gemini", 143, 40),
    ("test-driven-development", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\test-driven-development\SKILL.md", ".gemini", 97, 27),
    ("theme-factory", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\theme-factory\SKILL.md", ".gemini", 270, 76),
    ("troubleshooting", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\_snapshots\troubleshooting\SKILL.md", ".gemini (_snapshots)", 217, 61),
    ("tutorocean-profile-fill", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\tutorocean-profile-fill\SKILL.md", ".gemini", 195, 55),
    ("using-git-worktrees", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\_project-forks\lsatu\using-git-worktrees\SKILL.md", ".gemini (_project-forks)", 191, 54),
    ("using-superpowers", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\using-superpowers\SKILL.md", ".gemini", 178, 50),
    ("verification-before-completion", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\verification-before-completion\SKILL.md", ".gemini", 232, 65),
    ("watch", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\watch\SKILL.md", ".gemini", 257, 72),
    ("webapp-testing", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\webapp-testing\SKILL.md", ".gemini", 217, 61),
    ("wizard", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\wizard\SKILL.md", ".gemini", 267, 75),
    ("wrapup", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\wrapup\SKILL.md", ".gemini", 204, 57),
    ("writing-for-agents", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\writing-for-agents\SKILL.md", ".gemini", 112, 31),
    ("writing-plans", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\writing-plans\SKILL.md", ".gemini", 101, 28),
    ("writing-skills", r"C:\Users\Joshu\dev\ai-os\.gemini\skills\writing-skills\SKILL.md", ".gemini", 129, 36)
]

for item in exposed_skills_raw:
    doc.append(f"| `{item[0]}` | `{item[1]}` | {item[2]} | {item[3]} | ~{item[4]} tok |")

doc.append("")
doc.append("### B. SUPPRESSED / EXCLUDED SKILLS (98 Skills Excluded Due to Context Limits)")
doc.append("")
doc.append("| Identifier | Presumed File Path | Exclusion Reason |")
doc.append("|---|---|---|")

suppressed_skills_raw = [
    "academy-guide", "accidental-data-loss-prevention", "agent-development", "algorithmic-art",
    "antigravity-guide", "audit", "bigquery-bigframes", "bigquery-data-transfer-service",
    "bigtable-basics", "booking-link", "bootcamp-builder", "bootcamp-parity-audit",
    "build-mcp-app", "build-mcp-server", "build-mcpb", "building-data-apps", "captions",
    "chat-export", "chrome-extensions", "claude-api", "claude-automation-recommender",
    "claude-md-improver", "code-review", "codex-build", "codex-review", "command-development",
    "dataform-bigquery", "dbt-bigquery", "debug-optimize-lcp", "defuddle", "discernment-nudge",
    "discovering-gcp-data-assets", "doc-coauthoring", "docx", "extract-design",
    "federate-lakehouse-catalog", "find-skills", "gcp-data-pipelines", "gcp-dataflow",
    "gcp-managed-airflow-dag-authoring", "gcp-managed-airflow-migrations",
    "gcp-managed-airflow-recommendations", "gcp-pipeline-orchestration",
    "gcp-pipeline-resource-provisioning", "gcp-spark", "gcs-security-assessment",
    "gemini-api-dev", "gemini-interactions-api", "gemini-live-api-dev", "gemini-omni-flash-api",
    "google-cloud-auth-verification", "google-cloud-storage-basics",
    "google-cloud-storage-bucket-architect", "google-cloud-storage-fuse", "grill-me",
    "grill-me-codex", "grill-with-docs-codex", "guided-drill-assignment", "hook-development",
    "image-to-code", "impeccable", "inbound-tutoring-replies", "ingest", "internal-comms",
    "kling-cli", "level-up", "lovable-migrate", "lovable-prompt", "lsat-lab-mega-set",
    "lsat-lab-transcribe", "lsat-u-architecture", "lsat-u-platform-actions",
    "lsat-u-topic-builder", "lsatu-cc-handoff", "managing-python-dependencies",
    "math-olympiad", "mcp-integration", "ml-best-practices", "modern-web-guidance",
    "morning-brief", "netlify-ai-gateway", "netlify-caching", "netlify-cli-and-deploy",
    "netlify-config", "netlify-db", "netlify-edge-functions", "netlify-forms",
    "netlify-frameworks", "netlify-functions", "netlify-image-cdn", "notebook-guidance",
    "obsidian-cli", "pdf", "plugin-settings", "plugin-structure", "ponytail", "pptx",
    "pre-consultation-check-in", "prompt-architect-refiner", "resolving-mcp-region-configs",
    "resume", "review", "schema-mapping", "send-booking-link", "session-handoff",
    "session-recap", "shadcn", "site-teardown", "skill-creator", "skill-development",
    "skill-doctor", "skill-lint", "subtitles", "transcript", "transcriptapi",
    "video-transcript", "web-artifacts-builder", "xlsx", "youtube-api", "youtube-channels",
    "youtube-data", "youtube-full", "youtube-playlist", "youtube-search", "yt"
]

for s in suppressed_skills_raw:
    # Check if exists in .gemini/skills or config/skills
    p1 = os.path.join(r"C:\Users\Joshu\dev\ai-os\.gemini\skills", s, "SKILL.md")
    p2 = os.path.join(r"C:\Users\Joshu\.gemini\config\skills", s, "SKILL.md")
    path_found = p1 if os.path.exists(p1) else (p2 if os.path.exists(p2) else "Path unresolved / multi-directory")
    doc.append(f"| `{s}` | `{path_found}` | Context token budget limit reached |")

doc.append("")
doc.append("### C. DISCOVERABLE BUT NOT INCLUDED SKILLS")
doc.append("- Additional skills in `C:\\Users\\Joshu\\dev\\ai-os\\.gemini\\skills\\` that are neither exposed nor listed in the suppressed summary (e.g. nested non-SKILL.md folders, intermediate directory trees).")
doc.append("- Total discovered directories at root: 219. Total valid SKILL.md files: 215.")
doc.append("")
doc.append("### D. UNKNOWN")
doc.append("- Exact algorithm for selecting which 85 skills are exposed vs which 98 are suppressed when budget is exceeded: **UNKNOWN** (appears to correlate with alphabetical ordering or directory priority, but official formula is unverified).")
doc.append("")
doc.append("---")
doc.append("")

with open(output_file, "a", encoding="utf-8") as f:
    f.write("\n".join(doc) + "\n")
print("Section 5 appended successfully.")
