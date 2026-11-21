# SkillSpector scan, 2026-10-14

Static mode only (`skillspector scan --no-llm`, SkillSpector 2.12.0). Each skill scanned on its own; the recursive mode stops after 32 skills (partial first attempt kept in `first-attempt-recursive/`). Pattern and YARA matches, not verdicts: every HIGH or CRITICAL finding needs a human read before any action. No skill was removed or deactivated.

| Root | Scanned | CRITICAL | HIGH | MEDIUM | LOW |
|---|---|---|---|---|---|
| home-claude | 279 | 18 | 5 | 16 | 240 |
| vault-claude | 114 | 19 | 7 | 19 | 69 |

## Skills rated HIGH or CRITICAL (DO_NOT_INSTALL)

### claude-api (home-claude): CRITICAL 100/100, 129 findings
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:61`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:198`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:201`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:203`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:206`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:207`)
- ... 51 more HIGH/CRITICAL findings in the JSON

### eas-simulator (vault-claude): CRITICAL 100/100, 117 findings
- HIGH PE3 Privilege Escalation: Credential Access (`SKILL.md:34`)
- HIGH PE3 Privilege Escalation: Credential Access (`references/troubleshooting.md:11`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:194`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:226`)
- HIGH AS2 Agent Snooping: MCP Config Access (`references/controllers.md:135`)
- HIGH AS2 Agent Snooping: MCP Config Access (`references/controllers.md:135`)
- ... 3 more HIGH/CRITICAL findings in the JSON

### embedded-captions (vault-claude): CRITICAL 100/100, 115 findings
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:18`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:96`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:155`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:50`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:279`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:280`)
- ... 28 more HIGH/CRITICAL findings in the JSON

### faceless-explainer (vault-claude): CRITICAL 100/100, 21 findings
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:80`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:112`)
- HIGH P2 Prompt Injection: Hidden Instructions (`scripts/assemble-index.mjs:176`)
- HIGH P2 Prompt Injection: Hidden Instructions (`scripts/assemble-index.mjs:176`)
- HIGH P2 Prompt Injection: Hidden Instructions (`scripts/assemble-index.mjs:469`)
- HIGH AR2 Anti-Refusal: Anti-Refusal Statement (`scripts/audio.test.mjs:187`)

### hyperframes-animation (home-claude): CRITICAL 100/100, 64 findings
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:36`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:82`)
- HIGH P2 Prompt Injection: Hidden Instructions (`adapters/html-in-canvas-patterns.md:14`)
- HIGH P2 Prompt Injection: Hidden Instructions (`examples/brand-reveal-assemble-zoom.html:8`)
- HIGH P2 Prompt Injection: Hidden Instructions (`examples/brand-reveal-assemble-zoom.html:8`)
- HIGH P2 Prompt Injection: Hidden Instructions (`examples/comparison-split-cards.html:8`)
- ... 30 more HIGH/CRITICAL findings in the JSON

### hyperframes-animation (vault-claude): CRITICAL 100/100, 64 findings
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:36`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:82`)
- HIGH P2 Prompt Injection: Hidden Instructions (`adapters/html-in-canvas-patterns.md:14`)
- HIGH P2 Prompt Injection: Hidden Instructions (`examples/brand-reveal-assemble-zoom.html:8`)
- HIGH P2 Prompt Injection: Hidden Instructions (`examples/brand-reveal-assemble-zoom.html:8`)
- HIGH P2 Prompt Injection: Hidden Instructions (`examples/comparison-split-cards.html:8`)
- ... 30 more HIGH/CRITICAL findings in the JSON

### hyperframes-creative (home-claude): CRITICAL 100/100, 58 findings
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:54`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:58`)
- HIGH P2 Prompt Injection: Hidden Instructions (`frame-presets/biennale-yellow/caption-skin.html:1`)
- HIGH P2 Prompt Injection: Hidden Instructions (`frame-presets/biennale-yellow/frame-showcase.html:710`)
- HIGH P2 Prompt Injection: Hidden Instructions (`frame-presets/biennale-yellow/frame-showcase.html:799`)
- HIGH P2 Prompt Injection: Hidden Instructions (`frame-presets/biennale-yellow/frame-showcase.html:1040`)
- ... 45 more HIGH/CRITICAL findings in the JSON

### hyperframes-creative (vault-claude): CRITICAL 100/100, 58 findings
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:54`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:58`)
- HIGH P2 Prompt Injection: Hidden Instructions (`frame-presets/biennale-yellow/caption-skin.html:1`)
- HIGH P2 Prompt Injection: Hidden Instructions (`frame-presets/biennale-yellow/frame-showcase.html:710`)
- HIGH P2 Prompt Injection: Hidden Instructions (`frame-presets/biennale-yellow/frame-showcase.html:799`)
- HIGH P2 Prompt Injection: Hidden Instructions (`frame-presets/biennale-yellow/frame-showcase.html:1040`)
- ... 45 more HIGH/CRITICAL findings in the JSON

### impeccable (home-claude): CRITICAL 100/100, 41 findings
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:55`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:150`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:161`)
- HIGH P2 Prompt Injection: Hidden Instructions (`reference/document.md:74`)
- HIGH P2 Prompt Injection: Hidden Instructions (`reference/live.md:214`)
- HIGH P2 Prompt Injection: Hidden Instructions (`reference/live.md:214`)
- ... 5 more HIGH/CRITICAL findings in the JSON

### jev-audit (home-claude): CRITICAL 100/100, 6 findings
- CRITICAL TT3 Data Flow: Tainted flow: 'request' from os.environ.get (line 84, credential/environment) → urllib.request.build_opener.open (network output) (`scripts/check_connection.py:88`)
- HIGH P3 Prompt Injection: Exfiltration Commands (`SKILL.md:59`)

### jev-audit (vault-claude): CRITICAL 100/100, 6 findings
- CRITICAL TT3 Data Flow: Tainted flow: 'request' from os.environ.get (line 84, credential/environment) → urllib.request.build_opener.open (network output) (`scripts/check_connection.py:88`)
- HIGH P3 Prompt Injection: Exfiltration Commands (`SKILL.md:59`)

### mcp-builder (home-claude): CRITICAL 100/100, 17 findings
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:62`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:83`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:223`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:66`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:84`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:216`)
- ... 2 more HIGH/CRITICAL findings in the JSON

### media-use (home-claude): CRITICAL 100/100, 132 findings
- HIGH PE3 Privilege Escalation: Credential Access (`audio/references/tts.md:74`)
- HIGH PE3 Privilege Escalation: Credential Access (`audio/scripts/lib/heygen.mjs:6`)
- HIGH PE3 Privilege Escalation: Credential Access (`audio/scripts/lib/heygen.mjs:67`)
- HIGH PE3 Privilege Escalation: Credential Access (`audio/scripts/lib/heygen.mjs:71`)
- HIGH PE3 Privilege Escalation: Credential Access (`audio/scripts/lib/heygen.test.mjs:138`)
- HIGH PE3 Privilege Escalation: Credential Access (`audio/scripts/lib/heygen.test.mjs:138`)
- ... 12 more HIGH/CRITICAL findings in the JSON

### media-use (vault-claude): CRITICAL 100/100, 132 findings
- HIGH PE3 Privilege Escalation: Credential Access (`audio/references/tts.md:74`)
- HIGH PE3 Privilege Escalation: Credential Access (`audio/scripts/lib/heygen.mjs:6`)
- HIGH PE3 Privilege Escalation: Credential Access (`audio/scripts/lib/heygen.mjs:67`)
- HIGH PE3 Privilege Escalation: Credential Access (`audio/scripts/lib/heygen.mjs:71`)
- HIGH PE3 Privilege Escalation: Credential Access (`audio/scripts/lib/heygen.test.mjs:138`)
- HIGH PE3 Privilege Escalation: Credential Access (`audio/scripts/lib/heygen.test.mjs:138`)
- ... 12 more HIGH/CRITICAL findings in the JSON

### notebooklm (home-claude): CRITICAL 100/100, 155 findings
- HIGH YR1 YARA Match: YARA rule 'agent_skill_remote_bootstrap_execution': Remote script or code download followed by execution/bootstrap installation [agent_skill (`README.md:105`)
- HIGH YR1 YARA Match: YARA rule 'agent_skill_remote_bootstrap_execution': Remote script or code download followed by execution/bootstrap installation [agent_skill (`SKILL.md:31`)
- HIGH RA1 Rogue Agent: Self-Modification (`docs/cli-reference.md:695`)
- HIGH RA1 Rogue Agent: Self-Modification (`src/notebooklm/cli/download.py:150`)
- HIGH RA1 Rogue Agent: Self-Modification (`src/notebooklm/cli/download.py:480`)
- HIGH RA1 Rogue Agent: Self-Modification (`src/notebooklm/cli/download.py:516`)
- ... 56 more HIGH/CRITICAL findings in the JSON

### pr-to-video (vault-claude): CRITICAL 100/100, 29 findings
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:66`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:88`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:66`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:88`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:108`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:140`)
- ... 4 more HIGH/CRITICAL findings in the JSON

### product-launch-video (vault-claude): CRITICAL 100/100, 23 findings
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:103`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:135`)
- HIGH P2 Prompt Injection: Hidden Instructions (`scripts/assemble-index.mjs:238`)
- HIGH P2 Prompt Injection: Hidden Instructions (`scripts/assemble-index.mjs:238`)
- HIGH P2 Prompt Injection: Hidden Instructions (`scripts/assemble-index.mjs:617`)
- HIGH PE3 Privilege Escalation: Credential Access (`scripts/audio.test.mjs:27`)
- ... 1 more HIGH/CRITICAL findings in the JSON

### scroll-craft (vault-claude): CRITICAL 100/100, 16 findings
- HIGH LP1 MCP Least Privilege: Code capability 'network' detected in engine/scrollcraft.js but not covered by declared permissions. (`engine/scrollcraft.js:1`)
- HIGH AR2 Anti-Refusal: Anti-Refusal Statement (`references/approved-collection.md:88`)
- HIGH AR1 Anti-Refusal: Anti-Refusal Statement (`references/assets.md:111`)
- HIGH P2 Prompt Injection: Hidden Instructions (`references/device-diag.html:2`)
- HIGH P2 Prompt Injection: Hidden Instructions (`references/template.html:2`)
- HIGH P2 Prompt Injection: Hidden Instructions (`references/template.html:50`)
- ... 7 more HIGH/CRITICAL findings in the JSON

### security-and-hardening (vault-claude): CRITICAL 100/100, 21 findings
- HIGH YR4 YARA Match: YARA rule 'agent_skill_prompt_injection_hidden_instructions': Prompt injection or hidden instructions embedded in AI agent skill text [agent (`SKILL.md:21`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:77`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:85`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:92`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:100`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:107`)
- ... 14 more HIGH/CRITICAL findings in the JSON

### shadcn (home-claude): CRITICAL 100/100, 102 findings
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:55`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:258`)
- HIGH MP3 Memory Poisoning: Memory Manipulation (`SKILL.md:220`)
- HIGH RA1 Rogue Agent: Self-Modification (`cli.md:34`)
- HIGH RA1 Rogue Agent: Self-Modification (`cli.md:76`)
- HIGH AS1 Agent Snooping: Agent Config Directory Access (`mcp.md:22`)

### skill-creator (home-claude): CRITICAL 100/100, 9 findings
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:371`)
- HIGH E2 Data Exfiltration: Env Variable Harvesting (`scripts/improve_description.py:33`)
- HIGH E2 Data Exfiltration: Env Variable Harvesting (`scripts/run_eval.py:83`)
- HIGH AS1 Agent Snooping: Agent Config Directory Access (`scripts/run_eval.py:23`)

### watch (home-claude): CRITICAL 100/100, 21 findings
- CRITICAL TT3 Data Flow: Tainted flow: 'request' from os.environ.get (line 175, credential/environment) → urllib.request.urlopen (network output) (`scripts/whisper.py:177`)
- HIGH PE3 Privilege Escalation: Credential Access (`SKILL.md:16`)
- HIGH PE3 Privilege Escalation: Credential Access (`SKILL.md:112`)
- HIGH PE3 Privilege Escalation: Credential Access (`scripts/setup.py:63`)
- HIGH SC8 Supply Chain: Skill ships a __pycache__ directory that normal discovery skips (`scripts/__pycache__/:1`)
- HIGH SC8 Supply Chain: Skill ships Python bytecode (.pyc/.pyo) that normal analysis skips (`scripts/__pycache__/setup.cpython-312.pyc:1`)
- ... 7 more HIGH/CRITICAL findings in the JSON

### motion-graphics (vault-claude): CRITICAL 96/100, 42 findings
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:54`)
- HIGH P2 Prompt Injection: Hidden Instructions (`samples/asset-fusion/_ref-circle-highlight.html:6`)
- HIGH P2 Prompt Injection: Hidden Instructions (`samples/asset-fusion/_ref-circle-highlight.html:6`)

### music-to-video (vault-claude): CRITICAL 96/100, 17 findings
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:103`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:105`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:186`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:138`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:186`)
- HIGH P2 Prompt Injection: Hidden Instructions (`references/templates/logo-split-lockup-pulse/index.html:21`)

### remotion-to-hyperframes (vault-claude): CRITICAL 96/100, 45 findings
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:58`)
- HIGH P2 Prompt Injection: Hidden Instructions (`references/sequencing.md:36`)

### 3d-brain (home-claude): CRITICAL 92/100, 47 findings
- HIGH AS1 Agent Snooping: Agent Config Directory Access (`SKILL.md:23`)
- HIGH P2 Prompt Injection: Hidden Instructions (`assets/template/index.html:22`)
- HIGH P2 Prompt Injection: Hidden Instructions (`assets/template/index.html:22`)
- HIGH P2 Prompt Injection: Hidden Instructions (`assets/template/index.html:79`)
- HIGH P2 Prompt Injection: Hidden Instructions (`assets/template/index.html:79`)
- HIGH PE3 Privilege Escalation: Credential Access (`scripts/test-package.mjs:39`)

### hyperframes-cli (home-claude): CRITICAL 91/100, 245 findings
- HIGH P2 Prompt Injection: Hidden Instructions (`SKILL.md:31`)
- HIGH TM1 Tool Misuse: Tool Parameter Abuse (`references/cloud.md:148`)
- HIGH PE3 Privilege Escalation: Credential Access (`references/lambda.md:35`)

### hyperframes-cli (vault-claude): CRITICAL 91/100, 245 findings
- HIGH P2 Prompt Injection: Hidden Instructions (`SKILL.md:31`)
- HIGH TM1 Tool Misuse: Tool Parameter Abuse (`references/cloud.md:148`)
- HIGH PE3 Privilege Escalation: Credential Access (`references/lambda.md:35`)

### docx (home-claude): CRITICAL 86/100, 11 findings
- HIGH TM1 Tool Misuse: Tool Parameter Abuse (`SKILL.md:56`)
- HIGH TM2 Tool Misuse: Chaining Abuse (`SKILL.md:56`)
- HIGH E2 Data Exfiltration: Env Variable Harvesting (`scripts/office/soffice.py:28`)

### expo-data-fetching (vault-claude): CRITICAL 85/100, 20 findings
- HIGH PE3 Privilege Escalation: Credential Access (`SKILL.md:298`)
- HIGH PE3 Privilege Escalation: Credential Access (`SKILL.md:410`)
- HIGH PE3 Privilege Escalation: Credential Access (`SKILL.md:314`)
- HIGH PE3 Privilege Escalation: Credential Access (`SKILL.md:465`)
- HIGH PE3 Privilege Escalation: Credential Access (`SKILL.md:317`)
- HIGH PE3 Privilege Escalation: Credential Access (`SKILL.md:412`)
- ... 4 more HIGH/CRITICAL findings in the JSON

### hyperframes-core (home-claude): CRITICAL 85/100, 24 findings
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:27`)
- HIGH P2 Prompt Injection: Hidden Instructions (`references/sub-compositions.md:45`)

### hyperframes-core (vault-claude): CRITICAL 85/100, 24 findings
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:27`)
- HIGH P2 Prompt Injection: Hidden Instructions (`references/sub-compositions.md:45`)

### skill-doctor (home-claude): CRITICAL 85/100, 7 findings
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:76`)
- HIGH PE3 Privilege Escalation: Credential Access (`scripts/collect_sessions.py:559`)

### hyperframes (home-claude): CRITICAL 84/100, 32 findings
- HIGH P2 Prompt Injection: Hidden Instructions (`SKILL.md:40`)
- HIGH AR2 Anti-Refusal: Anti-Refusal Statement (`SKILL.md:50`)

### hyperframes (vault-claude): CRITICAL 84/100, 32 findings
- HIGH P2 Prompt Injection: Hidden Instructions (`SKILL.md:40`)
- HIGH AR2 Anti-Refusal: Anti-Refusal Statement (`SKILL.md:50`)

### supabase (vault-claude): CRITICAL 83/100, 12 findings
- HIGH YR1 YARA Match: YARA rule 'info_stealer': Information stealer patterns (credential harvesting, browser data theft) [malware] (`SKILL.md:3`)
- HIGH PE3 Privilege Escalation: Credential Access (`SKILL.md:38`)
- HIGH PE3 Privilege Escalation: Credential Access (`SKILL.md:43`)
- HIGH PE3 Privilege Escalation: Credential Access (`SKILL.md:43`)
- HIGH PE3 Privilege Escalation: Credential Access (`SKILL.md:115`)
- HIGH PE3 Privilege Escalation: Credential Access (`SKILL.md:43`)
- ... 4 more HIGH/CRITICAL findings in the JSON

### pptx (home-claude): CRITICAL 82/100, 9 findings
- HIGH TM1 Tool Misuse: Tool Parameter Abuse (`SKILL.md:66`)
- HIGH TM2 Tool Misuse: Chaining Abuse (`SKILL.md:66`)
- HIGH E2 Data Exfiltration: Env Variable Harvesting (`scripts/office/soffice.py:28`)

### playwright-cli (vault-claude): HIGH 80/100, 19 findings
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:476`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:488`)
- HIGH MP3 Memory Poisoning: Memory Manipulation (`references/storage-state.md:273`)

### slideshow (vault-claude): HIGH 80/100, 11 findings
- HIGH P2 Prompt Injection: Hidden Instructions (`SKILL.md:61`)
- HIGH P2 Prompt Injection: Hidden Instructions (`SKILL.md:61`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:434`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:475`)
- HIGH P2 Prompt Injection: Hidden Instructions (`references/standalone-harness.md:33`)

### graphify (home-claude): HIGH 75/100, 8 findings
- HIGH TM1 Tool Misuse: Tool Parameter Abuse (`SKILL.md:404`)
- HIGH TM1 Tool Misuse: Tool Parameter Abuse (`SKILL.md:806`)
- HIGH TM1 Tool Misuse: Tool Parameter Abuse (`SKILL.md:807`)
- HIGH TM1 Tool Misuse: Tool Parameter Abuse (`SKILL.md:974`)
- HIGH AR2 Anti-Refusal: Anti-Refusal Statement (`SKILL.md:1384`)

### browser-testing-with-devtools (vault-claude): HIGH 65/100, 4 findings
- HIGH YR1 YARA Match: YARA rule 'info_stealer': Information stealer patterns (credential harvesting, browser data theft) [malware] (`SKILL.md:64`)
- HIGH P1 Prompt Injection: Instruction Override (`SKILL.md:77`)
- HIGH YR4 YARA Match: YARA rule 'agent_skill_prompt_injection_hidden_instructions': Prompt injection or hidden instructions embedded in AI agent skill text [agent (`SKILL.md:77`)

### hyperframes-audio (home-claude): HIGH 63/100, 8 findings
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:77`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:285`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:291`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:366`)

### hyperframes-audio (vault-claude): HIGH 63/100, 8 findings
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:77`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:285`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:291`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:366`)

### git-guardrails-claude-code (home-claude): HIGH 62/100, 4 findings
- HIGH AS1 Agent Snooping: Agent Config Directory Access (`SKILL.md:24`)
- HIGH AS1 Agent Snooping: Agent Config Directory Access (`SKILL.md:61`)
- HIGH TM1 Tool Misuse: Tool Parameter Abuse (`SKILL.md:13`)
- HIGH TM1 Tool Misuse: Tool Parameter Abuse (`scripts/block-dangerous-git.sh:8`)

### expo-brownfield (vault-claude): HIGH 61/100, 32 findings
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:36`)
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:37`)

### talking-head-recut (vault-claude): HIGH 61/100, 24 findings
- HIGH P2 Prompt Injection: Hidden Instructions (`references/frames/hairline.html:1`)
- HIGH P2 Prompt Injection: Hidden Instructions (`references/frames/polaroid.html:1`)
- HIGH P2 Prompt Injection: Hidden Instructions (`references/layouts/overlay.html:1`)
- HIGH P2 Prompt Injection: Hidden Instructions (`references/layouts/overlay.html:1`)
- HIGH P2 Prompt Injection: Hidden Instructions (`references/layouts/pip.html:1`)
- HIGH P2 Prompt Injection: Hidden Instructions (`references/layouts/pip.html:1`)
- ... 7 more HIGH/CRITICAL findings in the JSON

### hyperframes-registry (home-claude): HIGH 57/100, 28 findings
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:143`)
- HIGH AR2 Anti-Refusal: Anti-Refusal Statement (`references/component-quality-bar.md:33`)

### hyperframes-registry (vault-claude): HIGH 57/100, 28 findings
- HIGH AE1 analysis-evasion: Incomplete referenced artifact analysis (`SKILL.md:143`)
- HIGH AR2 Anti-Refusal: Anti-Refusal Statement (`references/component-quality-bar.md:33`)

### pull-submissions (home-claude): HIGH 54/100, 7 findings
- HIGH PE3 Privilege Escalation: Credential Access (`pull-submissions.sh:6`)
- HIGH PE3 Privilege Escalation: Credential Access (`pull-submissions.sh:33`)
- HIGH PE3 Privilege Escalation: Credential Access (`pull-submissions.sh:36`)
- HIGH PE3 Privilege Escalation: Credential Access (`pull-submissions.sh:50`)

## All scores

| Skill | Root | Severity | Score | Findings | Coverage |
|---|---|---|---|---|---|
| claude-api | home-claude | CRITICAL | 100 | 129 | partial |
| eas-simulator | vault-claude | CRITICAL | 100 | 117 | partial |
| embedded-captions | vault-claude | CRITICAL | 100 | 115 | partial |
| faceless-explainer | vault-claude | CRITICAL | 100 | 21 | partial |
| hyperframes-animation | home-claude | CRITICAL | 100 | 64 | partial |
| hyperframes-animation | vault-claude | CRITICAL | 100 | 64 | partial |
| hyperframes-creative | home-claude | CRITICAL | 100 | 58 | partial |
| hyperframes-creative | vault-claude | CRITICAL | 100 | 58 | partial |
| impeccable | home-claude | CRITICAL | 100 | 41 | partial |
| jev-audit | home-claude | CRITICAL | 100 | 6 | complete |
| jev-audit | vault-claude | CRITICAL | 100 | 6 | complete |
| mcp-builder | home-claude | CRITICAL | 100 | 17 | partial |
| media-use | home-claude | CRITICAL | 100 | 132 | partial |
| media-use | vault-claude | CRITICAL | 100 | 132 | partial |
| notebooklm | home-claude | CRITICAL | 100 | 155 | partial |
| pr-to-video | vault-claude | CRITICAL | 100 | 29 | partial |
| product-launch-video | vault-claude | CRITICAL | 100 | 23 | partial |
| scroll-craft | vault-claude | CRITICAL | 100 | 16 | partial |
| security-and-hardening | vault-claude | CRITICAL | 100 | 21 | partial |
| shadcn | home-claude | CRITICAL | 100 | 102 | partial |
| skill-creator | home-claude | CRITICAL | 100 | 9 | partial |
| watch | home-claude | CRITICAL | 100 | 21 | partial |
| motion-graphics | vault-claude | CRITICAL | 96 | 42 | partial |
| music-to-video | vault-claude | CRITICAL | 96 | 17 | partial |
| remotion-to-hyperframes | vault-claude | CRITICAL | 96 | 45 | partial |
| 3d-brain | home-claude | CRITICAL | 92 | 47 | partial |
| hyperframes-cli | home-claude | CRITICAL | 91 | 245 | partial |
| hyperframes-cli | vault-claude | CRITICAL | 91 | 245 | partial |
| docx | home-claude | CRITICAL | 86 | 11 | partial |
| expo-data-fetching | vault-claude | CRITICAL | 85 | 20 | partial |
| hyperframes-core | home-claude | CRITICAL | 85 | 24 | partial |
| hyperframes-core | vault-claude | CRITICAL | 85 | 24 | partial |
| skill-doctor | home-claude | CRITICAL | 85 | 7 | partial |
| hyperframes | home-claude | CRITICAL | 84 | 32 | partial |
| hyperframes | vault-claude | CRITICAL | 84 | 32 | partial |
| supabase | vault-claude | CRITICAL | 83 | 12 | partial |
| pptx | home-claude | CRITICAL | 82 | 9 | partial |
| playwright-cli | vault-claude | HIGH | 80 | 19 | partial |
| slideshow | vault-claude | HIGH | 80 | 11 | partial |
| graphify | home-claude | HIGH | 75 | 8 | partial |
| browser-testing-with-devtools | vault-claude | HIGH | 65 | 4 | partial |
| hyperframes-audio | home-claude | HIGH | 63 | 8 | partial |
| hyperframes-audio | vault-claude | HIGH | 63 | 8 | partial |
| git-guardrails-claude-code | home-claude | HIGH | 62 | 4 | partial |
| expo-brownfield | vault-claude | HIGH | 61 | 32 | partial |
| talking-head-recut | vault-claude | HIGH | 61 | 24 | partial |
| hyperframes-registry | home-claude | HIGH | 57 | 28 | partial |
| hyperframes-registry | vault-claude | HIGH | 57 | 28 | partial |
| pull-submissions | home-claude | HIGH | 54 | 7 | partial |
| webapp-testing | home-claude | MEDIUM | 49 | 4 | complete |
| source-driven-development | vault-claude | MEDIUM | 47 | 3 | partial |
| audit | home-claude | MEDIUM | 45 | 3 | partial |
| claudex-loop | home-claude | MEDIUM | 45 | 8 | partial |
| claudex-loop | vault-claude | MEDIUM | 45 | 8 | partial |
| post-session-recap | vault-claude | MEDIUM | 45 | 3 | partial |
| firecrawl-monitor | home-claude | MEDIUM | 44 | 4 | partial |
| eas-workflows | vault-claude | MEDIUM | 43 | 5 | partial |
| xlsx | home-claude | MEDIUM | 42 | 8 | partial |
| consultation-followup-drafts | home-claude | MEDIUM | 39 | 3 | partial |
| figma | vault-claude | MEDIUM | 38 | 5 | partial |
| constraint-driven-development | vault-claude | MEDIUM | 37 | 2 | partial |
| humanizer | vault-claude | MEDIUM | 37 | 3 | partial |
| obsidian-bases | home-claude | MEDIUM | 37 | 2 | partial |
| theme-factory | home-claude | MEDIUM | 37 | 2 | partial |
| web-artifacts-builder | home-claude | MEDIUM | 37 | 2 | partial |
| accommodations-email | home-claude | MEDIUM | 33 | 2 | partial |
| accommodations-email | vault-claude | MEDIUM | 33 | 2 | partial |
| context-engineering | vault-claude | MEDIUM | 33 | 4 | partial |
| eas-app-stores | vault-claude | MEDIUM | 30 | 29 | partial |
| lsat-u-architecture | home-claude | MEDIUM | 29 | 2 | partial |
| ci-cd-and-automation | vault-claude | MEDIUM | 27 | 8 | partial |
| diagnosing-bugs | home-claude | MEDIUM | 27 | 1 | partial |
| assign-lsatu-work | home-claude | MEDIUM | 26 | 4 | partial |
| wizard | home-claude | MEDIUM | 26 | 2 | partial |
| algorithmic-art | home-claude | MEDIUM | 25 | 1 | partial |
| expo-app-clip | vault-claude | MEDIUM | 23 | 6 | partial |
| expo-module | vault-claude | MEDIUM | 23 | 11 | partial |
| git-workflow-and-versioning | vault-claude | MEDIUM | 23 | 2 | partial |
| doubt-driven-development | vault-claude | MEDIUM | 22 | 1 | complete |
| eas-hosting | vault-claude | MEDIUM | 22 | 10 | partial |
| code-simplification | vault-claude | MEDIUM | 21 | 2 | complete |
| lsat-lab-transcribe | home-claude | MEDIUM | 21 | 1 | partial |
| persona-agent-creator | vault-claude | MEDIUM | 21 | 1 | partial |
| spec-driven-development | vault-claude | MEDIUM | 21 | 4 | partial |
| api-and-interface-design | vault-claude | LOW | 20 | 1 | partial |
| general-video | vault-claude | LOW | 20 | 9 | partial |
| reverse-engineer-anything | home-claude | LOW | 20 | 6 | complete |
| shipping-and-launch | vault-claude | LOW | 20 | 1 | partial |
| expo-native-ui | vault-claude | LOW | 19 | 7 | partial |
| expo-skill-feedback | vault-claude | LOW | 19 | 7 | complete |
| discernment-nudge | home-claude | LOW | 17 | 1 | complete |
| to-questionnaire | home-claude | LOW | 17 | 1 | complete |
| to-tickets | home-claude | LOW | 17 | 1 | complete |
| research-deep | home-claude | LOW | 16 | 2 | partial |
| booking-link | home-claude | LOW | 15 | 1 | partial |
| design-taste-frontend | home-claude | LOW | 15 | 2 | partial |
| stripe-best-practices | vault-claude | LOW | 15 | 2 | partial |
| expo-router | vault-claude | LOW | 14 | 2 | partial |
| hyperframes-studio | home-claude | LOW | 14 | 5 | partial |
| hyperframes-studio | vault-claude | LOW | 14 | 5 | partial |
| frontend-design | home-claude | LOW | 13 | 1 | complete |
| second-brain-ingest | vault-claude | LOW | 13 | 4 | partial |
| using-git-worktrees | home-claude | LOW | 13 | 3 | partial |
| eas-observe | vault-claude | LOW | 12 | 7 | partial |
| eas-update | vault-claude | LOW | 12 | 7 | partial |
| expo-animation | vault-claude | LOW | 12 | 5 | partial |
| expo-examples | vault-claude | LOW | 12 | 11 | partial |
| expo-overview | vault-claude | LOW | 12 | 3 | partial |
| expo-upgrade | vault-claude | LOW | 12 | 15 | partial |
| expo-web-to-native | vault-claude | LOW | 12 | 3 | partial |
| extract-design | home-claude | LOW | 12 | 6 | partial |
| find-skills | home-claude | LOW | 12 | 13 | partial |
| firecrawl | home-claude | LOW | 12 | 4 | partial |
| gws-gmail-read | home-claude | LOW | 12 | 2 | complete |
| hyperframes-keyframes | home-claude | LOW | 12 | 8 | partial |
| hyperframes-keyframes | vault-claude | LOW | 12 | 8 | partial |
| setup-pre-commit | home-claude | LOW | 12 | 3 | partial |
| lsat-u-topic-builder | home-claude | LOW | 11 | 2 | partial |
| planning-and-task-breakdown | vault-claude | LOW | 11 | 2 | partial |
| using-agent-skills | vault-claude | LOW | 11 | 2 | complete |
| verification-before-completion | home-claude | LOW | 11 | 2 | complete |
| expo-dev-client | vault-claude | LOW | 10 | 2 | partial |
| expo-ui | vault-claude | LOW | 10 | 2 | partial |
| firecrawl-agent | home-claude | LOW | 10 | 2 | partial |
| firecrawl-crawl | home-claude | LOW | 10 | 2 | partial |
| firecrawl-download | home-claude | LOW | 10 | 2 | complete |
| firecrawl-interact | home-claude | LOW | 10 | 2 | complete |
| firecrawl-map | home-claude | LOW | 10 | 2 | partial |
| firecrawl-parse | home-claude | LOW | 10 | 2 | partial |
| firecrawl-scrape | home-claude | LOW | 10 | 2 | partial |
| firecrawl-search | home-claude | LOW | 10 | 2 | partial |
| kling-cli | vault-claude | LOW | 10 | 2 | partial |
| performance-optimization | vault-claude | LOW | 10 | 2 | partial |
| grill-me | home-claude | LOW | 8 | 1 | partial |
| grilling | home-claude | LOW | 8 | 1 | complete |
| grilling | vault-claude | LOW | 8 | 1 | complete |
| lovable-prompt | home-claude | LOW | 8 | 1 | partial |
| pr | home-claude | LOW | 8 | 1 | partial |
| second-brain-query | vault-claude | LOW | 8 | 1 | partial |
| superwhisper | home-claude | LOW | 8 | 1 | partial |
| bootcamp-builder | home-claude | LOW | 7 | 1 | partial |
| bootcamp-builder | vault-claude | LOW | 7 | 1 | partial |
| deprecation-and-migration | vault-claude | LOW | 7 | 1 | complete |
| eas-update-insights | vault-claude | LOW | 7 | 1 | partial |
| expo-design-system | vault-claude | LOW | 7 | 1 | partial |
| expo-dom | vault-claude | LOW | 7 | 1 | partial |
| expo-project-structure | vault-claude | LOW | 7 | 1 | partial |
| incremental-implementation | vault-claude | LOW | 7 | 1 | partial |
| level-up | home-claude | LOW | 7 | 1 | partial |
| loop-me | home-claude | LOW | 7 | 1 | partial |
| lsat-lab-lecture-transcribe | vault-claude | LOW | 7 | 1 | partial |
| pdf | home-claude | LOW | 7 | 1 | partial |
| second-brain-lint | vault-claude | LOW | 7 | 1 | partial |
| setup-matt-pocock-skills | home-claude | LOW | 7 | 1 | partial |
| skill-lint | home-claude | LOW | 7 | 1 | complete |
| slack-gif-creator | home-claude | LOW | 7 | 6 | partial |
| transcript-intake | vault-claude | LOW | 7 | 1 | partial |
| wrapup | home-claude | LOW | 7 | 1 | partial |
| youtube-full | home-claude | LOW | 6 | 1 | partial |
| firecrawl-developer-index | home-claude | LOW | 5 | 1 | complete |
| prompt-architect-refiner | home-claude | LOW | 3 | 1 | complete |
| academy-guide | home-claude | LOW | 0 | 0 | partial |
| ai-prompt-research | vault-claude | LOW | 0 | 0 | partial |
| ai-visibility-audit | vault-claude | LOW | 0 | 0 | partial |
| ask-matt | home-claude | LOW | 0 | 0 | partial |
| bootcamp-parity-audit | home-claude | LOW | 0 | 0 | partial |
| brand-guidelines | home-claude | LOW | 0 | 0 | complete |
| browser-harness | home-claude | LOW | 0 | 0 | partial |
| canvas-design | home-claude | LOW | 0 | 0 | partial |
| chat-export | home-claude | LOW | 0 | 0 | partial |
| chief-of-staff | home-claude | LOW | 0 | 0 | complete |
| chief-of-staff | vault-claude | LOW | 0 | 0 | complete |
| claude-handoff | home-claude | LOW | 0 | 0 | complete |
| claudex-route | home-claude | LOW | 0 | 0 | complete |
| claudex-route | vault-claude | LOW | 0 | 0 | complete |
| code-review | home-claude | LOW | 0 | 0 | partial |
| code-review-and-quality | vault-claude | LOW | 0 | 0 | partial |
| codebase-design | home-claude | LOW | 0 | 0 | complete |
| codex-build | home-claude | LOW | 0 | 0 | complete |
| codex-build | vault-claude | LOW | 0 | 0 | complete |
| codex-review | home-claude | LOW | 0 | 0 | complete |
| codex-review | vault-claude | LOW | 0 | 0 | complete |
| competitive-landscape | vault-claude | LOW | 0 | 0 | complete |
| competitor-analysis | vault-claude | LOW | 0 | 0 | complete |
| consultation-inquiry-drafts | home-claude | LOW | 0 | 0 | partial |
| debugging-and-error-recovery | vault-claude | LOW | 0 | 0 | complete |
| decision-mapping | home-claude | LOW | 0 | 0 | complete |
| defuddle | home-claude | LOW | 0 | 0 | complete |
| design-an-interface | home-claude | LOW | 0 | 0 | complete |
| doc-coauthoring | home-claude | LOW | 0 | 0 | partial |
| documentation-and-adrs | vault-claude | LOW | 0 | 0 | partial |
| domain-modeling | home-claude | LOW | 0 | 0 | partial |
| domain-modeling | vault-claude | LOW | 0 | 0 | partial |
| edit-article | home-claude | LOW | 0 | 0 | complete |
| emil-design-eng | home-claude | LOW | 0 | 0 | partial |
| firecrawl-company-directories | home-claude | LOW | 0 | 0 | partial |
| firecrawl-competitive-intel | home-claude | LOW | 0 | 0 | partial |
| firecrawl-dashboard-reporting | home-claude | LOW | 0 | 0 | partial |
| firecrawl-deep-research | home-claude | LOW | 0 | 0 | partial |
| firecrawl-demo-walkthrough | home-claude | LOW | 0 | 0 | partial |
| firecrawl-knowledge-base | home-claude | LOW | 0 | 0 | partial |
| firecrawl-knowledge-ingest | home-claude | LOW | 0 | 0 | partial |
| firecrawl-lead-gen | home-claude | LOW | 0 | 0 | partial |
| firecrawl-lead-research | home-claude | LOW | 0 | 0 | partial |
| firecrawl-market-research | home-claude | LOW | 0 | 0 | partial |
| firecrawl-qa | home-claude | LOW | 0 | 0 | partial |
| firecrawl-research-index | home-claude | LOW | 0 | 0 | partial |
| firecrawl-research-papers | home-claude | LOW | 0 | 0 | partial |
| firecrawl-seo-audit | home-claude | LOW | 0 | 0 | partial |
| firecrawl-shop | home-claude | LOW | 0 | 0 | partial |
| firecrawl-website-design-clone | home-claude | LOW | 0 | 0 | partial |
| firecrawl-workflows | home-claude | LOW | 0 | 0 | partial |
| frontend-ui-engineering | vault-claude | LOW | 0 | 0 | complete |
| grill-by-claude | home-claude | LOW | 0 | 0 | complete |
| grill-by-claude | vault-claude | LOW | 0 | 0 | complete |
| grill-me-codex | home-claude | LOW | 0 | 0 | complete |
| grill-me-codex | vault-claude | LOW | 0 | 0 | complete |
| grill-with-docs | home-claude | LOW | 0 | 0 | complete |
| grill-with-docs | vault-claude | LOW | 0 | 0 | complete |
| grill-with-docs-codex | home-claude | LOW | 0 | 0 | complete |
| grill-with-docs-codex | vault-claude | LOW | 0 | 0 | complete |
| guided-drill-assignment | home-claude | LOW | 0 | 0 | partial |
| gws-admin-reports | home-claude | LOW | 0 | 0 | complete |
| gws-calendar | home-claude | LOW | 0 | 0 | complete |
| gws-calendar-agenda | home-claude | LOW | 0 | 0 | complete |
| gws-calendar-insert | home-claude | LOW | 0 | 0 | complete |
| gws-chat | home-claude | LOW | 0 | 0 | partial |
| gws-chat-send | home-claude | LOW | 0 | 0 | complete |
| gws-classroom | home-claude | LOW | 0 | 0 | complete |
| gws-docs | home-claude | LOW | 0 | 0 | complete |
| gws-docs-write | home-claude | LOW | 0 | 0 | complete |
| gws-drive | home-claude | LOW | 0 | 0 | partial |
| gws-drive-upload | home-claude | LOW | 0 | 0 | partial |
| gws-events | home-claude | LOW | 0 | 0 | complete |
| gws-events-renew | home-claude | LOW | 0 | 0 | complete |
| gws-events-subscribe | home-claude | LOW | 0 | 0 | partial |
| gws-forms | home-claude | LOW | 0 | 0 | complete |
| gws-gmail | home-claude | LOW | 0 | 0 | complete |
| gws-gmail-forward | home-claude | LOW | 0 | 0 | complete |
| gws-gmail-reply | home-claude | LOW | 0 | 0 | complete |
| gws-gmail-reply-all | home-claude | LOW | 0 | 0 | complete |
| gws-gmail-send | home-claude | LOW | 0 | 0 | complete |
| gws-gmail-triage | home-claude | LOW | 0 | 0 | complete |
| gws-gmail-watch | home-claude | LOW | 0 | 0 | partial |
| gws-keep | home-claude | LOW | 0 | 0 | complete |
| gws-meet | home-claude | LOW | 0 | 0 | complete |
| gws-modelarmor | home-claude | LOW | 0 | 0 | complete |
| gws-modelarmor-create-template | home-claude | LOW | 0 | 0 | complete |
| gws-modelarmor-sanitize-prompt | home-claude | LOW | 0 | 0 | complete |
| gws-modelarmor-sanitize-response | home-claude | LOW | 0 | 0 | complete |
| gws-people | home-claude | LOW | 0 | 0 | partial |
| gws-script | home-claude | LOW | 0 | 0 | complete |
| gws-script-push | home-claude | LOW | 0 | 0 | partial |
| gws-shared | home-claude | LOW | 0 | 0 | partial |
| gws-sheets | home-claude | LOW | 0 | 0 | complete |
| gws-sheets-append | home-claude | LOW | 0 | 0 | complete |
| gws-sheets-read | home-claude | LOW | 0 | 0 | complete |
| gws-slides | home-claude | LOW | 0 | 0 | complete |
| gws-tasks | home-claude | LOW | 0 | 0 | complete |
| gws-workflow | home-claude | LOW | 0 | 0 | complete |
| gws-workflow-email-to-task | home-claude | LOW | 0 | 0 | complete |
| gws-workflow-file-announce | home-claude | LOW | 0 | 0 | complete |
| gws-workflow-meeting-prep | home-claude | LOW | 0 | 0 | complete |
| gws-workflow-standup-report | home-claude | LOW | 0 | 0 | complete |
| gws-workflow-weekly-digest | home-claude | LOW | 0 | 0 | complete |
| handoff | home-claude | LOW | 0 | 0 | complete |
| herdr | home-claude | LOW | 0 | 0 | partial |
| high-end-visual-design | home-claude | LOW | 0 | 0 | partial |
| idea-refine | vault-claude | LOW | 0 | 0 | partial |
| image-to-code | home-claude | LOW | 0 | 0 | complete |
| implement | home-claude | LOW | 0 | 0 | complete |
| implement-spec | home-claude | LOW | 0 | 0 | complete |
| improve-codebase-architecture | home-claude | LOW | 0 | 0 | partial |
| inbound-tutoring-replies | home-claude | LOW | 0 | 0 | partial |
| internal-comms | home-claude | LOW | 0 | 0 | complete |
| interview-me | vault-claude | LOW | 0 | 0 | complete |
| json-canvas | home-claude | LOW | 0 | 0 | partial |
| karpathy-teach | vault-claude | LOW | 0 | 0 | partial |
| keyword-clustering | vault-claude | LOW | 0 | 0 | complete |
| keyword-research | vault-claude | LOW | 0 | 0 | complete |
| link | home-claude | LOW | 0 | 0 | partial |
| link-prospecting | vault-claude | LOW | 0 | 0 | complete |
| local-seo | vault-claude | LOW | 0 | 0 | complete |
| lovable-migrate | home-claude | LOW | 0 | 0 | partial |
| lsat-lab-mega-set | home-claude | LOW | 0 | 0 | partial |
| lsat-lab-sync | vault-claude | LOW | 0 | 0 | partial |
| lsat-u-platform-actions | home-claude | LOW | 0 | 0 | partial |
| lsat-u-voice | vault-claude | LOW | 0 | 0 | complete |
| lsatu-cc-handoff | home-claude | LOW | 0 | 0 | partial |
| migrate-to-shoehorn | home-claude | LOW | 0 | 0 | complete |
| minimalist-ui | home-claude | LOW | 0 | 0 | partial |
| morning-brief | home-claude | LOW | 0 | 0 | partial |
| observability-and-instrumentation | vault-claude | LOW | 0 | 0 | partial |
| obsidian-cli | home-claude | LOW | 0 | 0 | partial |
| obsidian-markdown | home-claude | LOW | 0 | 0 | partial |
| obsidian-vault | home-claude | LOW | 0 | 0 | complete |
| onboard | home-claude | LOW | 0 | 0 | partial |
| orca-cli | home-claude | LOW | 0 | 0 | complete |
| orchestration | home-claude | LOW | 0 | 0 | complete |
| persona-content-creator | home-claude | LOW | 0 | 0 | complete |
| persona-customer-support | home-claude | LOW | 0 | 0 | complete |
| persona-event-coordinator | home-claude | LOW | 0 | 0 | complete |
| persona-exec-assistant | home-claude | LOW | 0 | 0 | complete |
| persona-hr-coordinator | home-claude | LOW | 0 | 0 | complete |
| persona-it-admin | home-claude | LOW | 0 | 0 | complete |
| persona-project-manager | home-claude | LOW | 0 | 0 | complete |
| persona-researcher | home-claude | LOW | 0 | 0 | complete |
| persona-sales-ops | home-claude | LOW | 0 | 0 | complete |
| persona-team-lead | home-claude | LOW | 0 | 0 | complete |
| pickup | home-claude | LOW | 0 | 0 | partial |
| ponytail | home-claude | LOW | 0 | 0 | complete |
| prototype | home-claude | LOW | 0 | 0 | complete |
| qa | home-claude | LOW | 0 | 0 | complete |
| recipe-backup-sheet-as-csv | home-claude | LOW | 0 | 0 | complete |
| recipe-batch-invite-to-event | home-claude | LOW | 0 | 0 | complete |
| recipe-block-focus-time | home-claude | LOW | 0 | 0 | complete |
| recipe-bulk-download-folder | home-claude | LOW | 0 | 0 | complete |
| recipe-collect-form-responses | home-claude | LOW | 0 | 0 | complete |
| recipe-compare-sheet-tabs | home-claude | LOW | 0 | 0 | complete |
| recipe-copy-sheet-for-new-month | home-claude | LOW | 0 | 0 | complete |
| recipe-create-classroom-course | home-claude | LOW | 0 | 0 | complete |
| recipe-create-doc-from-template | home-claude | LOW | 0 | 0 | complete |
| recipe-create-events-from-sheet | home-claude | LOW | 0 | 0 | complete |
| recipe-create-expense-tracker | home-claude | LOW | 0 | 0 | complete |
| recipe-create-feedback-form | home-claude | LOW | 0 | 0 | complete |
| recipe-create-gmail-filter | home-claude | LOW | 0 | 0 | complete |
| recipe-create-meet-space | home-claude | LOW | 0 | 0 | complete |
| recipe-create-presentation | home-claude | LOW | 0 | 0 | complete |
| recipe-create-shared-drive | home-claude | LOW | 0 | 0 | complete |
| recipe-create-task-list | home-claude | LOW | 0 | 0 | complete |
| recipe-create-vacation-responder | home-claude | LOW | 0 | 0 | complete |
| recipe-draft-email-from-doc | home-claude | LOW | 0 | 0 | complete |
| recipe-email-drive-link | home-claude | LOW | 0 | 0 | complete |
| recipe-find-free-time | home-claude | LOW | 0 | 0 | complete |
| recipe-find-large-files | home-claude | LOW | 0 | 0 | complete |
| recipe-forward-labeled-emails | home-claude | LOW | 0 | 0 | complete |
| recipe-generate-report-from-sheet | home-claude | LOW | 0 | 0 | complete |
| recipe-label-and-archive-emails | home-claude | LOW | 0 | 0 | complete |
| recipe-log-deal-update | home-claude | LOW | 0 | 0 | partial |
| recipe-organize-drive-folder | home-claude | LOW | 0 | 0 | partial |
| recipe-plan-weekly-schedule | home-claude | LOW | 0 | 0 | complete |
| recipe-post-mortem-setup | home-claude | LOW | 0 | 0 | complete |
| recipe-reschedule-meeting | home-claude | LOW | 0 | 0 | complete |
| recipe-review-meet-participants | home-claude | LOW | 0 | 0 | complete |
| recipe-review-overdue-tasks | home-claude | LOW | 0 | 0 | complete |
| recipe-save-email-attachments | home-claude | LOW | 0 | 0 | complete |
| recipe-save-email-to-doc | home-claude | LOW | 0 | 0 | complete |
| recipe-schedule-recurring-event | home-claude | LOW | 0 | 0 | complete |
| recipe-send-team-announcement | home-claude | LOW | 0 | 0 | complete |
| recipe-share-doc-and-notify | home-claude | LOW | 0 | 0 | partial |
| recipe-share-event-materials | home-claude | LOW | 0 | 0 | complete |
| recipe-share-folder-with-team | home-claude | LOW | 0 | 0 | partial |
| recipe-sync-contacts-to-sheet | home-claude | LOW | 0 | 0 | complete |
| recipe-watch-drive-changes | home-claude | LOW | 0 | 0 | partial |
| redesign-existing-projects | home-claude | LOW | 0 | 0 | partial |
| request-refactor-plan | home-claude | LOW | 0 | 0 | complete |
| research | home-claude | LOW | 0 | 0 | complete |
| research-add-items | home-claude | LOW | 0 | 0 | complete |
| research-report | home-claude | LOW | 0 | 0 | partial |
| resolving-merge-conflicts | home-claude | LOW | 0 | 0 | complete |
| resume | home-claude | LOW | 0 | 0 | partial |
| retro | home-claude | LOW | 0 | 0 | partial |
| review | home-claude | LOW | 0 | 0 | partial |
| scaffold-exercises | home-claude | LOW | 0 | 0 | partial |
| second-brain | home-claude | LOW | 0 | 0 | partial |
| second-brain-ingest | home-claude | LOW | 0 | 0 | partial |
| second-brain-lint | home-claude | LOW | 0 | 0 | partial |
| second-brain-query | home-claude | LOW | 0 | 0 | partial |
| second-brain-task | vault-claude | LOW | 0 | 0 | partial |
| send-booking-link | home-claude | LOW | 0 | 0 | partial |
| seo-audit | vault-claude | LOW | 0 | 0 | partial |
| seo-coach | vault-claude | LOW | 0 | 0 | complete |
| seo-project-setup | vault-claude | LOW | 0 | 0 | partial |
| seo-report | vault-claude | LOW | 0 | 0 | partial |
| session-handoff | home-claude | LOW | 0 | 0 | partial |
| session-handoff | vault-claude | LOW | 0 | 0 | partial |
| setup-ts-deep-modules | home-claude | LOW | 0 | 0 | partial |
| site-teardown | home-claude | LOW | 0 | 0 | partial |
| supabase-postgres-best-practices | vault-claude | LOW | 0 | 0 | partial |
| tdd | home-claude | LOW | 0 | 0 | partial |
| teach | home-claude | LOW | 0 | 0 | partial |
| to-issues | home-claude | LOW | 0 | 0 | complete |
| to-spec | home-claude | LOW | 0 | 0 | complete |
| triage | home-claude | LOW | 0 | 0 | partial |
| tutorocean-profile-fill | home-claude | LOW | 0 | 0 | partial |
| ubiquitous-language | home-claude | LOW | 0 | 0 | partial |
| wait-what | home-claude | LOW | 0 | 0 | partial |
| wayfinder | home-claude | LOW | 0 | 0 | partial |
| writing-beats | home-claude | LOW | 0 | 0 | complete |
| writing-for-agents | home-claude | LOW | 0 | 0 | partial |
| writing-fragments | home-claude | LOW | 0 | 0 | complete |
| writing-great-skills | home-claude | LOW | 0 | 0 | complete |
| writing-shape | home-claude | LOW | 0 | 0 | complete |
