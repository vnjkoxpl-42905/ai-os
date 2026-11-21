---
type: reference
subject: Design repositories, assets and prototype routing
created: 2026-10-24
updated: 2026-10-24
aliases: [Design repo registry, Component repos, Design workspaces]
contradictions: []
---

# Find the right source before rebuilding it

This is the shared Claude Code and Codex route to local repositories, source libraries, design tools and prototypes. Follow the [design hub](README.md) for principles and skills. Repository source remains outside this Obsidian vault. Local availability does not prove a component is installed in the target app, a tool is authenticated, or a preview is running.

## Reusable resources and the prepared lab

### emilkowalski-skills

Emil Kowalski’s 16 design and engineering skills, including animation, UI review and prototyping. [Source repository](<../../ai-os-projects/emilkowalski-skills>), [README](<../../ai-os-projects/emilkowalski-skills/README.md>) and [MIT license](<../../ai-os-projects/emilkowalski-skills/LICENSE>). Installed runtime copies and collision handling are described in the [library](library.md#emil-kowalskis-design-and-engineering-skills).

### react-bits

Animated React components and effects. Read README, choose a component and its JS/TS + CSS/Tailwind variant, then inspect dependencies before copying.

- Source: [react-bits](<../../ai-os-projects/react-bits>).
- Instructions: [README](<../../ai-os-projects/react-bits/README.md>).
- License: MIT + Commons Clause; read local restrictions before reuse.
- Terms: [local LICENSE.md](<../../ai-os-projects/react-bits/LICENSE.md>).

### vue-bits

Vue/Nuxt component alternatives. Do not copy Vue code directly into the React LSAT U app.

- Source: [vue-bits](<../../ai-os-projects/vue-bits>).
- Instructions: [README](<../../ai-os-projects/vue-bits/README.md>).
- License: MIT + Commons Clause; read local restrictions before reuse.
- Terms: [local LICENSE.md](<../../ai-os-projects/vue-bits/LICENSE.md>).

### canvas-ui

Framework-agnostic GPU/canvas effects. Components can wrap live DOM; test fallback, performance and reduced motion before adoption.

- Source: [canvas-ui](<../../ai-os-projects/canvas-ui>).
- Instructions: [README](<../../ai-os-projects/canvas-ui/README.md>).
- License: MIT + Commons Clause; read local restrictions before reuse.
- Terms: [local LICENSE.md](<../../ai-os-projects/canvas-ui/LICENSE.md>).

### taste-vault

Reference gallery, design vocabulary and Reference to Design workflow. Browse actual screenshots; vendor House DNA is reference material, not Joshua's approved palette. The custom Python server is required for Add reference persistence.

- Source: [taste-vault](<../../ai-os-projects/taste-vault>).
- Instructions: [README](<../../ai-os-projects/taste-vault/README.md>).
- License: MIT; third-party reference screenshot rights excluded.
- Terms: [local LICENSE](<../../ai-os-projects/taste-vault/LICENSE>).
- Repo-owned skill and prompts: [Reference to Design](<../../ai-os-projects/taste-vault/skills/reference-to-design/SKILL.md>) and [prompt pack](<../../ai-os-projects/taste-vault/skills/reference-to-design/references/prompts.md>). These files are available to read; this audit does not claim runtime activation.

### dashboard-design-assets

Offline fonts and assets. Newsreader, Manrope, Space Grotesk and IBM Plex Mono have local OFL notices in their font subfolders.

- Source: [dashboard-design-assets](<../../ai-os-projects/dashboard-design-assets>).
- License: No top-level license found; do not assume redistribution rights.
- Font terms: [ibmplexmono OFL](<../../ai-os-projects/dashboard-design-assets/fonts/ibmplexmono/OFL.txt>).
- Font terms: [manrope OFL](<../../ai-os-projects/dashboard-design-assets/fonts/manrope/OFL.txt>).
- Font terms: [newsreader OFL](<../../ai-os-projects/dashboard-design-assets/fonts/newsreader/OFL.txt>).
- Font terms: [spacegrotesk OFL](<../../ai-os-projects/dashboard-design-assets/fonts/spacegrotesk/OFL.txt>).

### godly-mcp-server

Read-only public design-discovery MCP implementation. Its README describes intended tools, not evidence of current successful queries.

- Source: [godly-mcp-server](<../../ai-os-projects/godly-mcp-server>).
- Instructions: [README](<../../ai-os-projects/godly-mcp-server/README.md>).
- License: No top-level license found; do not assume redistribution rights.

### pinterest-mcp-server

Read-only Pinterest API discovery. Authentication and beta public-search entitlement are separate requirements. Credentials stay in the central ignored .env.

- Source: [pinterest-mcp-server](<../../ai-os-projects/pinterest-mcp-server>).
- Instructions: [README](<../../ai-os-projects/pinterest-mcp-server/README.md>).
- License: No top-level license found; do not assume redistribution rights.

### dashboard-design-lab

Prepared React/Vite/TypeScript harness with GSAP, Motion, Tailwind, Lucide and Tabler. Its README gives build/browser commands; it is separate from production.

- Source: [dashboard-design-lab](<../../ai-os-projects/dashboard-design-lab>).
- Instructions: [README](<../../ai-os-projects/dashboard-design-lab/README.md>).
- License: No top-level license found; do not assume redistribution rights.

## Both runtimes use the same hub

From the AI OS workspace, both root operating instruction files route design work to this folder. From another checkout, explicitly open `C:/Users/Joshu/dev/ai-os/design/README.md`, then this registry and the relevant skill. An external app checkout does not automatically inherit AI OS instructions. Follow that checkout's own AGENTS.md/CLAUDE.md before editing. Protected LSAT U operating instructions were not changed by this inventory.

A repository being reachable from both tools does not grant browser login sessions or authenticate its MCP. Keep tool credentials in their existing secret store and verify a real provider call when using the tool. Use the existing [resource guidance](../.agents/skills/design-resource-library/references/resources.md) and [readiness record](../research/2026-10-23-dashboard-design-readiness.md) for setup context, with dated evidence limits.

## Standalone studies and handoffs

These are local prototype artifacts, separate from app source and production. Preview-server health was not tested for this registry.

- [LSAT-U-Dashboard-2026-10-22](<../../../Downloads/LSAT-U-Dashboard-2026-10-22>).
- [LSAT-U-Dashboard-Handoff-2026-10-22](<../../../Downloads/LSAT-U-Dashboard-Handoff-2026-10-22>).
- [LSAT-U-Dashboard-New-Directions](<../../../Downloads/LSAT-U-Dashboard-New-Directions>).
- [LSAT-U-Dashboard-Three-Directions](<../../../Downloads/LSAT-U-Dashboard-Three-Directions>).
- [LSAT-U-Dashboard-Three-Directions-v2](<../../../Downloads/LSAT-U-Dashboard-Three-Directions-v2>).
- [LSAT-U-LexPrep-Motion-2026-10-22](<../../../Downloads/LSAT-U-LexPrep-Motion-2026-10-22>).
- [LSAT-U-Motion-Studies-2026-10-22](<../../../Downloads/LSAT-U-Motion-Studies-2026-10-22>).
- [RC-Direct-Design-Audit-2026-10-21](<../../../Downloads/RC-Direct-Design-Audit-2026-10-21>).

## Application and visual-production checkouts

These are project context or examples, not a global component library. Every listed sibling directory was checked for root README, package metadata, license files and operating-instruction presence. This is metadata coverage, not a review of every application source file.

| Workspace | Root instructions found | README |
|---|---|---|
| [conditional-and-or-video-20261019](<../../ai-os-projects/conditional-and-or-video-20261019>) | [AGENTS.md](<../../ai-os-projects/conditional-and-or-video-20261019/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/conditional-and-or-video-20261019/CLAUDE.md>) | [README](<../../ai-os-projects/conditional-and-or-video-20261019/README.md>) |
| [contrapositive-video](<../../ai-os-projects/contrapositive-video>) | None at this root | [README](<../../ai-os-projects/contrapositive-video/README.md>) |
| [lr-recall-instructions-video](<../../ai-os-projects/lr-recall-instructions-video>) | [AGENTS.md](<../../ai-os-projects/lr-recall-instructions-video/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lr-recall-instructions-video/CLAUDE.md>) | No root README |
| [lsatu](<../../ai-os-projects/lsatu>) | [AGENTS.md](<../../ai-os-projects/lsatu/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu/DESIGN.md>) | [README](<../../ai-os-projects/lsatu/README.md>) |
| [lsatu-abstract](<../../ai-os-projects/lsatu-abstract>) | [AGENTS.md](<../../ai-os-projects/lsatu-abstract/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-abstract/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-abstract/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-abstract/README.md>) |
| [lsatu-and-or-20261019](<../../ai-os-projects/lsatu-and-or-20261019>) | [AGENTS.md](<../../ai-os-projects/lsatu-and-or-20261019/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-and-or-20261019/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-and-or-20261019/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-and-or-20261019/README.md>) |
| [lsatu-and-or-baseline-20261019](<../../ai-os-projects/lsatu-and-or-baseline-20261019>) | [AGENTS.md](<../../ai-os-projects/lsatu-and-or-baseline-20261019/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-and-or-baseline-20261019/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-and-or-baseline-20261019/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-and-or-baseline-20261019/README.md>) |
| [lsatu-conditional-bootcamp](<../../ai-os-projects/lsatu-conditional-bootcamp>) | [AGENTS.md](<../../ai-os-projects/lsatu-conditional-bootcamp/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-conditional-bootcamp/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-conditional-bootcamp/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-conditional-bootcamp/README.md>) |
| [lsatu-conditional-merge](<../../ai-os-projects/lsatu-conditional-merge>) | [AGENTS.md](<../../ai-os-projects/lsatu-conditional-merge/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-conditional-merge/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-conditional-merge/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-conditional-merge/README.md>) |
| [lsatu-conditional-reconcile](<../../ai-os-projects/lsatu-conditional-reconcile>) | [AGENTS.md](<../../ai-os-projects/lsatu-conditional-reconcile/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-conditional-reconcile/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-conditional-reconcile/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-conditional-reconcile/README.md>) |
| [lsatu-conditional-takeover](<../../ai-os-projects/lsatu-conditional-takeover>) | [AGENTS.md](<../../ai-os-projects/lsatu-conditional-takeover/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-conditional-takeover/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-conditional-takeover/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-conditional-takeover/README.md>) |
| [lsatu-drill-focus](<../../ai-os-projects/lsatu-drill-focus>) | [AGENTS.md](<../../ai-os-projects/lsatu-drill-focus/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-drill-focus/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-drill-focus/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-drill-focus/README.md>) |
| [lsatu-fix-overrides](<../../ai-os-projects/lsatu-fix-overrides>) | [AGENTS.md](<../../ai-os-projects/lsatu-fix-overrides/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-fix-overrides/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-fix-overrides/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-fix-overrides/README.md>) |
| [lsatu-four-situations](<../../ai-os-projects/lsatu-four-situations>) | [AGENTS.md](<../../ai-os-projects/lsatu-four-situations/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-four-situations/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-four-situations/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-four-situations/README.md>) |
| [lsatu-lr-baseline-20261016](<../../ai-os-projects/lsatu-lr-baseline-20261016>) | [AGENTS.md](<../../ai-os-projects/lsatu-lr-baseline-20261016/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-lr-baseline-20261016/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-lr-baseline-20261016/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-lr-baseline-20261016/README.md>) |
| [lsatu-merge-tmp](<../../ai-os-projects/lsatu-merge-tmp>) | [AGENTS.md](<../../ai-os-projects/lsatu-merge-tmp/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-merge-tmp/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-merge-tmp/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-merge-tmp/README.md>) |
| [lsatu-missed-session-credit](<../../ai-os-projects/lsatu-missed-session-credit>) | [AGENTS.md](<../../ai-os-projects/lsatu-missed-session-credit/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-missed-session-credit/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-missed-session-credit/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-missed-session-credit/README.md>) |
| [lsatu-nav-168](<../../ai-os-projects/lsatu-nav-168>) | [AGENTS.md](<../../ai-os-projects/lsatu-nav-168/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-nav-168/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-nav-168/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-nav-168/README.md>) |
| [lsatu-rc-builder-layout](<../../ai-os-projects/lsatu-rc-builder-layout>) | [AGENTS.md](<../../ai-os-projects/lsatu-rc-builder-layout/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-rc-builder-layout/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-rc-builder-layout/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-rc-builder-layout/README.md>) |
| [lsatu-rc-create](<../../ai-os-projects/lsatu-rc-create>) | [AGENTS.md](<../../ai-os-projects/lsatu-rc-create/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-rc-create/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-rc-create/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-rc-create/README.md>) |
| [lsatu-rc-final-release-20261021](<../../ai-os-projects/lsatu-rc-final-release-20261021>) | [AGENTS.md](<../../ai-os-projects/lsatu-rc-final-release-20261021/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-rc-final-release-20261021/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-rc-final-release-20261021/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-rc-final-release-20261021/README.md>) |
| [lsatu-rc-finished](<../../ai-os-projects/lsatu-rc-finished>) | [AGENTS.md](<../../ai-os-projects/lsatu-rc-finished/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-rc-finished/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-rc-finished/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-rc-finished/README.md>) |
| [lsatu-rc-focus-release](<../../ai-os-projects/lsatu-rc-focus-release>) | [AGENTS.md](<../../ai-os-projects/lsatu-rc-focus-release/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-rc-focus-release/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-rc-focus-release/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-rc-focus-release/README.md>) |
| [lsatu-rc-prelight-20261020](<../../ai-os-projects/lsatu-rc-prelight-20261020>) | [AGENTS.md](<../../ai-os-projects/lsatu-rc-prelight-20261020/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-rc-prelight-20261020/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-rc-prelight-20261020/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-rc-prelight-20261020/README.md>) |
| [lsatu-rc-september-20261020](<../../ai-os-projects/lsatu-rc-september-20261020>) | [AGENTS.md](<../../ai-os-projects/lsatu-rc-september-20261020/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-rc-september-20261020/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-rc-september-20261020/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-rc-september-20261020/README.md>) |
| [lsatu-rc-sonnet-build](<../../ai-os-projects/lsatu-rc-sonnet-build>) | [AGENTS.md](<../../ai-os-projects/lsatu-rc-sonnet-build/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-rc-sonnet-build/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-rc-sonnet-build/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-rc-sonnet-build/README.md>) |
| [lsatu-reading-center](<../../ai-os-projects/lsatu-reading-center>) | [AGENTS.md](<../../ai-os-projects/lsatu-reading-center/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-reading-center/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-reading-center/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-reading-center/README.md>) |
| [lsatu-reading-center-rc-recall](<../../ai-os-projects/lsatu-reading-center-rc-recall>) | [AGENTS.md](<../../ai-os-projects/lsatu-reading-center-rc-recall/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-reading-center-rc-recall/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-reading-center-rc-recall/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-reading-center-rc-recall/README.md>) |
| [lsatu-reading-center-sidebar](<../../ai-os-projects/lsatu-reading-center-sidebar>) | [AGENTS.md](<../../ai-os-projects/lsatu-reading-center-sidebar/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-reading-center-sidebar/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-reading-center-sidebar/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-reading-center-sidebar/README.md>) |
| [lsatu-reading-hub-20261015](<../../ai-os-projects/lsatu-reading-hub-20261015>) | [AGENTS.md](<../../ai-os-projects/lsatu-reading-hub-20261015/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-reading-hub-20261015/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-reading-hub-20261015/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-reading-hub-20261015/README.md>) |
| [lsatu-relationship-ui](<../../ai-os-projects/lsatu-relationship-ui>) | [AGENTS.md](<../../ai-os-projects/lsatu-relationship-ui/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-relationship-ui/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-relationship-ui/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-relationship-ui/README.md>) |
| [lsatu-role-home-20261022](<../../ai-os-projects/lsatu-role-home-20261022>) | [AGENTS.md](<../../ai-os-projects/lsatu-role-home-20261022/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-role-home-20261022/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-role-home-20261022/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-role-home-20261022/README.md>) |
| [lsatu-str](<../../ai-os-projects/lsatu-str>) | [AGENTS.md](<../../ai-os-projects/lsatu-str/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-str/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-str/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-str/README.md>) |
| [lsatu-str-backend](<../../ai-os-projects/lsatu-str-backend>) | [AGENTS.md](<../../ai-os-projects/lsatu-str-backend/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-str-backend/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-str-backend/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-str-backend/README.md>) |
| [lsatu-unless](<../../ai-os-projects/lsatu-unless>) | [AGENTS.md](<../../ai-os-projects/lsatu-unless/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-unless/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-unless/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-unless/README.md>) |
| [lsatu-wt-frozen](<../../ai-os-projects/lsatu-wt-frozen>) | [AGENTS.md](<../../ai-os-projects/lsatu-wt-frozen/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/lsatu-wt-frozen/CLAUDE.md>), [DESIGN.md](<../../ai-os-projects/lsatu-wt-frozen/DESIGN.md>) | [README](<../../ai-os-projects/lsatu-wt-frozen/README.md>) |
| [rc-training-demo](<../../ai-os-projects/rc-training-demo>) | [AGENTS.md](<../../ai-os-projects/rc-training-demo/AGENTS.md>), [CLAUDE.md](<../../ai-os-projects/rc-training-demo/CLAUDE.md>) | [README](<../../ai-os-projects/rc-training-demo/README.md>) |
| [reading-center](<../../ai-os-projects/reading-center>) | [CLAUDE.md](<../../ai-os-projects/reading-center/CLAUDE.md>) | No root README |

## General tools and excluded operational folders

These were counted in the complete sibling inventory. They are not being presented as design component repositories.

| Directory | Classification | Reason |
|---|---|---|
| [.conditional-reconcile-runtime](<../../ai-os-projects/.conditional-reconcile-runtime>) | excluded | Operational scratch/runtime checkout; not a reusable design library. Top-level metadata inventoried only. |
| [.lsatu-booking-messages-20261014](<../../ai-os-projects/.lsatu-booking-messages-20261014>) | excluded | Operational scratch/runtime checkout; not a reusable design library. Top-level metadata inventoried only. |
| [.lsatu-ops](<../../ai-os-projects/.lsatu-ops>) | excluded | Operational scratch/runtime checkout; not a reusable design library. Top-level metadata inventoried only. |
| [.lsatu-ops-gianna](<../../ai-os-projects/.lsatu-ops-gianna>) | excluded | Operational scratch/runtime checkout; not a reusable design library. Top-level metadata inventoried only. |
| [.lsatu-ops-sandra](<../../ai-os-projects/.lsatu-ops-sandra>) | excluded | Operational scratch/runtime checkout; not a reusable design library. Top-level metadata inventoried only. |
| [.lsatu-publish-rule](<../../ai-os-projects/.lsatu-publish-rule>) | excluded | Operational scratch/runtime checkout; not a reusable design library. Top-level metadata inventoried only. |
| [antigravity-sdk-python](<../../ai-os-projects/antigravity-sdk-python>) | general | General tooling or source retrieval; relevant when needed but outside design library scope. |
| [claudex-loop](<../../ai-os-projects/claudex-loop>) | general | General tooling or source retrieval; relevant when needed but outside design library scope. |
| [karpathy-method-tools](<../../ai-os-projects/karpathy-method-tools>) | general | General tooling or source retrieval; relevant when needed but outside design library scope. |
| [skill-dependency-tests](<../../ai-os-projects/skill-dependency-tests>) | general | General tooling or source retrieval; relevant when needed but outside design library scope. |
| [x-archive-collector](<../../ai-os-projects/x-archive-collector>) | general | General tooling or source retrieval; relevant when needed but outside design library scope. |
| [youtube-transcripts](<../../ai-os-projects/youtube-transcripts>) | general | General tooling or source retrieval; relevant when needed but outside design library scope. |

## Coverage and limits

- Checked **58 sibling project directories** and **8 matching Downloads folders**, for **66 records**.
- Classification: 7 reusable design resources, 47 design/application/prototype projects, 6 general tools and 6 excluded operational scratch folders. The prepared lab is counted as a project.
- Read available top-level README/package/license metadata. Relevant library README and license bodies were read to explain intended use and licensing.
- Did not traverse node_modules, .git internals, secrets, private data or nested dependency copies. Did not inspect every file on the computer or claim blanket ingestion.
- Did not change app code, repository configuration, skills, credentials or protected project operating instructions.
- Machine-readable provenance and root metadata: [complete repository inventory](<../research/2026-10-24-design-completeness/repos.json>).


## Reference to Design activation update (2026-10-24)

The earlier repository audit only established read access. Joshua subsequently authorized activation: [Reference to Design](../.agents/skills/reference-to-design/SKILL.md) is now an active skill in Claude Code and Codex, including global discovery roots, supporting guides and MIT notice. See [activation receipt](../research/2026-10-24-reference-to-design-activation/receipt.json).
