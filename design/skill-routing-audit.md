---
type: reference
subject: Full design skill routing and runtime coverage
created: 2026-10-24
updated: 2026-10-27
aliases: [Design skill audit]
tags: [design, skills, claude, codex, llm-wiki]
sources: []
---

# Every design skill has a route## Emil collection refresh (2026-10-29)The later targeted inventory refresh adds all 16 `emil-upstream-*` skills to the [generated skill registry](skills.generated.md), with one verified path each for the Claude and Codex project activations and catalogs. The four entrypoint copies for each skill matched by SHA-256 at this check. The historical counts and table below describe the 2026-10-24 audit and do not include that later collection; this refresh did not rescan all other roots or test invocation.

Start at [the design hub](README.md). This register covers design-primary skills and direct visual, component, research, browser and motion support. Metadata was read across all nine existing Claude/Codex catalog, project, home and plugin roots. Generic API/module design, database schema design, billing contract design and unrelated operational workflows were examined but kept out of the design subset.

## Current routing verification on 2026-10-27

The [current generated registry](skills.generated.md) contains 536 design/supporting skill paths. All 536 entry points exist after repairing four replaced plugin-version paths. Seven Taste Skill v2 copies again include the shared design-hub route; their full v2 bodies remain intact. The older counts below describe the original 2026-10-24 audit, not the current generated registry.

Use [the task-to-skill guide and prompt](README.md#use-this-folder-to-improve-a-design) to start work. The core website/app design, reference, component, motion and browser skill routes have activated project/home copies. `build-mcp-app`, `playground` and `watch` remain catalogue-only options. `captions` and `subtitles` are intentionally under the inactive Claude catalogue. These five are not promised as automatically callable runtime skills. Reading their catalogue entry is possible where the runtime permits local instructions; activation or installation is a separate decision.

A broader fresh metadata scan found 2,039 path records and 175 relevant directory names. The generated registry retains its reviewed 536-record design classification rather than blindly promoting every new metadata match. Plugin availability and provider authentication must still be checked for the selected task. File and link checks do not execute every skill or validate all external dependencies.

## Verified coverage on 2026-10-24

- 2,021 SKILL.md path records examined, including duplicate runtime copies and plugin versions.
- 523 relevant path records: 364 primary and 159 supporting.
- 174 distinct directory names, which are not guaranteed to be distinct capabilities because vendor namespaces can reuse names.
- 431 editable relevant copies now contain a hub link. All appended bytes preserve the original file prefix, metadata and custom instructions.
- 92 plugin, bundled system or managed synced copies are read-only in this audit. Their companion routes appear below. Shared root/home instructions supply the incoming hub route without altering vendor packages.
- No missing editable design routes after live readback. No new global activation or replacement skill copies were created.
- Coverage excludes frozen `_snapshots`, dependency trees and Git internals. These are archives or implementation dependencies, not active or canonical skill entry points.
- This audit establishes routing and discoverability, not that every skill was executed, every tool authenticated, or every plugin present in both runtimes.

The [machine-readable full inventory](../research/2026-10-24-design-completeness/skills.json) records every considered path, metadata, classification reason, editability, routing result and verification hash, including the general skills excluded from the design subset.

| Root | Primary | Supporting | General |
|---|---:|---:|---:|
| `catalog-claude` | 65 | 18 | 249 |
| `catalog-codex` | 69 | 13 | 233 |
| `project-codex` | 44 | 9 | 101 |
| `project-claude` | 43 | 8 | 77 |
| `home-agents` | 39 | 30 | 260 |
| `home-codex` | 23 | 16 | 114 |
| `home-claude` | 39 | 33 | 250 |
| `plugin-codex` | 35 | 16 | 209 |
| `plugin-claude` | 7 | 16 | 5 |


## Design and directly supporting capabilities

Each row links a real installed/catalogued copy. Use its owning runtime path; a catalogue copy does not activate a skill. Namespace-specific and all duplicate paths remain in the full JSON register.

| Skill directory name | Classification | Existing homes |
|---|---|---|
| [21st-ui](<../../../.claude/plugins/cache/21st-dev/21st/1.0.1/skills/21st-ui/SKILL.md>) | primary | plugin-claude, plugin-codex |
| [a11y-debugging](<../skills/claude/a11y-debugging/SKILL.md>) | supporting | catalog-claude, plugin-claude |
| [accessibility-review](<../../../.codex/plugins/cache/claude-cowork/design/1.2.0/skills/accessibility-review/SKILL.md>) | primary | plugin-codex |
| [algorithmic-art](<../skills/claude/algorithmic-art/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude |
| [appkit-interop](<../../../.codex/plugins/cache/openai-curated-remote/build-macos-apps/0.1.4/skills/appkit-interop/SKILL.md>) | supporting | plugin-codex |
| [artifact-template-simple-dark-mode](<../../../.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-simple-dark-mode/SKILL.md>) | primary | plugin-codex |
| [artifact-template-simple-light-mode](<../../../.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-simple-light-mode/SKILL.md>) | primary | plugin-codex |
| [audit](<../../../.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/audit/SKILL.md>) | primary | plugin-codex |
| [bootcamp-parity-audit](<../skills/claude/bootcamp-parity-audit/SKILL.md>) | primary | catalog-claude, home-agents, home-claude |
| [brand-guidelines](<../skills/claude/brand-guidelines/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude |
| [browser](<../../../.agents/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/browser/SKILL.md>) | supporting | home-agents, home-claude, plugin-codex |
| [browser-harness](<../../../.agents/skills/browser-harness/SKILL.md>) | supporting | home-agents, home-claude |
| [browser-testing-with-devtools](<../.agents/skills/browser-testing-with-devtools/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [build-chatgpt-app](<../../../.codex/plugins/cache/openai-curated/openai-developers/1dc19589/skills/build-chatgpt-app/SKILL.md>) | primary | plugin-codex |
| [build-mcp-app](<../skills/claude/build-mcp-app/SKILL.md>) | supporting | catalog-claude |
| [built-in-browser](<../../../.claude/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/built-in-browser/SKILL.md>) | supporting | home-claude |
| [canvas-design](<../skills/claude/canvas-design/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude |
| [captions](<../skills/claude/_inactive/captions/SKILL.md>) | supporting | catalog-claude |
| [chrome-browser](<../../../.claude/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/chrome-browser/SKILL.md>) | supporting | home-claude |
| [chrome-devtools](<../skills/claude/chrome-devtools/SKILL.md>) | supporting | catalog-claude, plugin-claude |
| [chrome-devtools-cli](<../../../.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.11.0/skills/chrome-devtools-cli/SKILL.md>) | supporting | plugin-claude |
| [chrome-extensions](<../.agents/skills/chrome-extensions/SKILL.md>) | supporting | project-codex |
| [computer-use](<../../../.claude/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/computer-use/SKILL.md>) | supporting | home-claude |
| [constraint-driven-development](<../.agents/skills/constraint-driven-development/SKILL.md>) | supporting | catalog-claude, catalog-codex, project-claude, project-codex |
| [cookie-debugging](<../../../.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.11.0/skills/cookie-debugging/SKILL.md>) | supporting | plugin-claude |
| [create-pet](<../../../.codex/plugins/cache/openai-curated-remote/work-pets/0.1.6/skills/create-pet/SKILL.md>) | primary | plugin-codex |
| [debug-optimize-lcp](<../skills/claude/debug-optimize-lcp/SKILL.md>) | supporting | catalog-claude, plugin-claude |
| [design-critique](<../../../.codex/plugins/cache/claude-cowork/design/1.2.0/skills/design-critique/SKILL.md>) | primary | plugin-codex |
| [design-handoff](<../../../.codex/plugins/cache/claude-cowork/design/1.2.0/skills/design-handoff/SKILL.md>) | primary | plugin-codex |
| [design-qa](<../../../.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/design-qa/SKILL.md>) | primary | plugin-codex |
| [design-resource-library](<../.agents/skills/design-resource-library/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [design-system](<../../../.codex/plugins/cache/claude-cowork/design/1.2.0/skills/design-system/SKILL.md>) | primary | plugin-codex |
| [design-taste-frontend](<../.agents/skills/design-taste-frontend/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude, home-codex, project-claude, project-codex |
| [documents](<../../../.codex/plugins/cache/openai-primary-runtime/documents/26.1026.10807/skills/documents/SKILL.md>) | primary | plugin-codex |
| [docx](<../skills/claude/docx/SKILL.md>) | supporting | catalog-claude, catalog-codex, home-agents, home-claude, plugin-codex |
| [eas-simulator](<../.agents/skills/eas-simulator/SKILL.md>) | supporting | catalog-claude, catalog-codex, project-claude, project-codex |
| [embedded-captions](<../.agents/skills/embedded-captions/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [emil-design-eng](<../skills/claude/_project-forks/lsatu/emil-design-eng/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude, home-codex |
| [expo-animation](<../.agents/skills/expo-animation/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [expo-design-system](<../.agents/skills/expo-design-system/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [expo-dom](<../.agents/skills/expo-dom/SKILL.md>) | supporting | catalog-claude, catalog-codex, project-claude, project-codex |
| [expo-native-ui](<../.agents/skills/expo-native-ui/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [expo-overview](<../.agents/skills/expo-overview/SKILL.md>) | supporting | catalog-claude, catalog-codex, project-claude, project-codex |
| [expo-router](<../.agents/skills/expo-router/SKILL.md>) | supporting | catalog-claude, catalog-codex, project-claude, project-codex |
| [expo-ui](<../.agents/skills/expo-ui/SKILL.md>) | supporting | catalog-claude, catalog-codex, project-claude, project-codex |
| [expo-web-to-native](<../.agents/skills/expo-web-to-native/SKILL.md>) | supporting | catalog-claude, catalog-codex, project-claude, project-codex |
| [extract-design](<../.agents/skills/extract-design/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude, home-codex, project-claude, project-codex |
| [faceless-explainer](<../.agents/skills/faceless-explainer/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [figma](<../.agents/skills/figma/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [firecrawl](<../../../.agents/skills/firecrawl/SKILL.md>) | supporting | home-agents, home-claude, home-codex |
| [firecrawl-agent](<../../../.agents/skills/firecrawl-agent/SKILL.md>) | supporting | home-agents, home-claude, home-codex |
| [firecrawl-crawl](<../../../.agents/skills/firecrawl-crawl/SKILL.md>) | supporting | home-agents, home-claude, home-codex |
| [firecrawl-deep-research](<../../../.agents/skills/firecrawl-deep-research/SKILL.md>) | supporting | home-agents, home-claude, home-codex |
| [firecrawl-demo-walkthrough](<../../../.agents/skills/firecrawl-demo-walkthrough/SKILL.md>) | supporting | home-agents, home-claude, home-codex |
| [firecrawl-developer-index](<../../../.agents/skills/firecrawl-developer-index/SKILL.md>) | supporting | home-agents, home-claude, home-codex |
| [firecrawl-download](<../../../.agents/skills/firecrawl-download/SKILL.md>) | supporting | home-agents, home-claude, home-codex |
| [firecrawl-interact](<../../../.agents/skills/firecrawl-interact/SKILL.md>) | primary | home-agents, home-claude, home-codex |
| [firecrawl-map](<../../../.agents/skills/firecrawl-map/SKILL.md>) | supporting | home-agents, home-claude, home-codex |
| [firecrawl-parse](<../../../.agents/skills/firecrawl-parse/SKILL.md>) | supporting | home-agents, home-claude, home-codex |
| [firecrawl-qa](<../../../.agents/skills/firecrawl-qa/SKILL.md>) | supporting | home-agents, home-claude, home-codex |
| [firecrawl-research-index](<../../../.agents/skills/firecrawl-research-index/SKILL.md>) | supporting | home-agents, home-claude, home-codex |
| [firecrawl-scrape](<../../../.agents/skills/firecrawl-scrape/SKILL.md>) | supporting | home-agents, home-claude, home-codex |
| [firecrawl-search](<../../../.agents/skills/firecrawl-search/SKILL.md>) | supporting | home-agents, home-claude, home-codex |
| [firecrawl-website-design-clone](<../../../.agents/skills/firecrawl-website-design-clone/SKILL.md>) | primary | home-agents, home-claude, home-codex |
| [firecrawl-workflows](<../../../.agents/skills/firecrawl-workflows/SKILL.md>) | primary | home-agents, home-claude, home-codex |
| [frontend-app-builder](<../../../.codex/plugins/cache/openai-curated/build-web-apps/1dc19589/skills/frontend-app-builder/SKILL.md>) | primary | plugin-codex |
| [frontend-design](<../skills/claude/frontend-design/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude, home-codex, plugin-codex |
| [frontend-testing-debugging](<../../../.codex/plugins/cache/openai-curated/build-web-apps/1dc19589/skills/frontend-testing-debugging/SKILL.md>) | primary | plugin-codex |
| [frontend-ui-engineering](<../.agents/skills/frontend-ui-engineering/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [general-video](<../.agents/skills/general-video/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude, project-claude, project-codex |
| [get-context](<../../../.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/get-context/SKILL.md>) | primary | plugin-codex |
| [google-slides](<../../../.codex/plugins/cache/openai-curated-remote/google-drive/0.1.22/skills/google-slides/SKILL.md>) | supporting | plugin-codex |
| [gsap](<../../../.codex/plugins/cache/openai-curated/hyperframes/1dc19589/skills/gsap/SKILL.md>) | primary | plugin-codex |
| [gsap-core](<../.agents/skills/gsap-core/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [gsap-frameworks](<../.agents/skills/gsap-frameworks/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [gsap-performance](<../.agents/skills/gsap-performance/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [gsap-plugins](<../.agents/skills/gsap-plugins/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [gsap-react](<../.agents/skills/gsap-react/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [gsap-scrolltrigger](<../.agents/skills/gsap-scrolltrigger/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [gsap-timeline](<../.agents/skills/gsap-timeline/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [gsap-utils](<../.agents/skills/gsap-utils/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [gws-slides](<../skills/claude/gws-slides/SKILL.md>) | supporting | catalog-claude, catalog-codex, home-agents, home-claude, home-codex |
| [hatch-pet](<../../../.codex/skills/hatch-pet/SKILL.md>) | primary | home-codex |
| [higgsfield-generate](<../skills/codex/higgsfield-generate/SKILL.md>) | primary | catalog-codex, home-codex |
| [higgsfield-marketplace-cards](<../skills/codex/higgsfield-marketplace-cards/SKILL.md>) | primary | catalog-codex, home-codex |
| [higgsfield-product-photoshoot](<../skills/codex/higgsfield-product-photoshoot/SKILL.md>) | primary | catalog-codex, home-codex |
| [higgsfield-soul-id](<../skills/codex/higgsfield-soul-id/SKILL.md>) | primary | catalog-codex, home-codex |
| [higgsfield-websites](<../skills/codex/higgsfield-websites/SKILL.md>) | primary | catalog-codex, home-codex |
| [high-end-visual-design](<../skills/claude/high-end-visual-design/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude, home-codex |
| [html-handoff](<../.agents/skills/html-handoff/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [hyperframes](<../.agents/skills/hyperframes/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude, plugin-codex, project-claude, project-codex |
| [hyperframes-animation](<../.agents/skills/hyperframes-animation/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude, project-claude, project-codex |
| [hyperframes-audio](<../.agents/skills/hyperframes-audio/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude, project-claude, project-codex |
| [hyperframes-cli](<../.agents/skills/hyperframes-cli/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude, plugin-codex, project-claude, project-codex |
| [hyperframes-core](<../.agents/skills/hyperframes-core/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude, project-claude, project-codex |
| [hyperframes-creative](<../.agents/skills/hyperframes-creative/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude, project-claude, project-codex |
| [hyperframes-keyframes](<../.agents/skills/hyperframes-keyframes/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude, project-claude, project-codex |
| [hyperframes-registry](<../.agents/skills/hyperframes-registry/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude, plugin-codex, project-claude, project-codex |
| [hyperframes-studio](<../.agents/skills/hyperframes-studio/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude, project-claude, project-codex |
| [ideate](<../../../.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/ideate/SKILL.md>) | primary | plugin-codex |
| [image-to-code](<../skills/claude/image-to-code/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude, home-codex, plugin-codex |
| [imagegen](<../skills/codex/imagegen/SKILL.md>) | primary | catalog-codex, home-codex |
| [impeccable](<../.agents/skills/impeccable/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude, home-codex, project-claude, project-codex |
| [index](<../../../.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/index/SKILL.md>) | primary | plugin-codex |
| [json-canvas](<../skills/claude/json-canvas/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude, home-codex |
| [kling-cli](<../.agents/skills/kling-cli/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [liquid-glass](<../../../.codex/plugins/cache/openai-curated-remote/build-macos-apps/0.1.4/skills/liquid-glass/SKILL.md>) | supporting | plugin-codex |
| [lovable-prompt](<../skills/claude/lovable-prompt/SKILL.md>) | supporting | catalog-claude, catalog-codex, home-agents, home-claude, home-codex |
| [media-use](<../.agents/skills/media-use/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude, project-claude, project-codex |
| [minimalist-ui](<../skills/claude/minimalist-ui/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude, home-codex |
| [modern-web-guidance](<../.agents/skills/modern-web-guidance/SKILL.md>) | primary | project-codex |
| [motion-graphics](<../.agents/skills/motion-graphics/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [music-to-video](<../.agents/skills/music-to-video/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [orca-cli](<../../../.agents/skills/orca-cli/SKILL.md>) | supporting | home-agents, home-claude |
| [pdf](<../../../.codex/plugins/cache/openai-primary-runtime/pdf/26.1026.10807/skills/pdf/SKILL.md>) | primary | plugin-codex |
| [performance-optimization](<../.agents/skills/performance-optimization/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [playground](<../skills/claude/playground/SKILL.md>) | primary | catalog-claude |
| [playwright](<../skills/codex/playwright/SKILL.md>) | supporting | catalog-codex, home-codex |
| [playwright-cli](<../.agents/skills/playwright-cli/SKILL.md>) | supporting | catalog-claude, catalog-codex, project-claude, project-codex |
| [pptx](<../skills/claude/pptx/SKILL.md>) | supporting | catalog-claude, catalog-codex, home-agents, home-claude, plugin-codex |
| [pr-to-video](<../.agents/skills/pr-to-video/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [presentations](<../../../.codex/plugins/cache/openai-primary-runtime/presentations/26.1026.10807/skills/presentations/SKILL.md>) | supporting | plugin-codex |
| [product-launch-video](<../.agents/skills/product-launch-video/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [prototype](<../skills/claude/prototype/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude |
| [react-best-practices](<../../../.codex/plugins/cache/openai-curated/build-web-apps/1dc19589/skills/react-best-practices/SKILL.md>) | supporting | plugin-codex |
| [react-bits](<../.agents/skills/react-bits/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [redesign-existing-projects](<../skills/claude/redesign-existing-projects/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude, home-codex |
| [remotion-best-practices](<../../../.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-best-practices/SKILL.md>) | supporting | plugin-claude |
| [remotion-captions](<../../../.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-captions/SKILL.md>) | primary | plugin-claude |
| [remotion-create](<../../../.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-create/SKILL.md>) | supporting | plugin-claude |
| [remotion-docs](<../../../.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-docs/SKILL.md>) | supporting | plugin-claude |
| [remotion-interactivity](<../../../.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-interactivity/SKILL.md>) | primary | plugin-claude |
| [remotion-maps](<../../../.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-maps/SKILL.md>) | primary | plugin-claude |
| [remotion-markup](<../../../.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-markup/SKILL.md>) | primary | plugin-claude |
| [remotion-multimedia](<../../../.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-multimedia/SKILL.md>) | primary | plugin-claude |
| [remotion-render](<../../../.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-render/SKILL.md>) | supporting | plugin-claude |
| [remotion-saas](<../../../.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-saas/SKILL.md>) | primary | plugin-claude |
| [remotion-studio](<../../../.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-studio/SKILL.md>) | supporting | plugin-claude |
| [remotion-to-hyperframes](<../.agents/skills/remotion-to-hyperframes/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [remotion-upgrade](<../../../.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-upgrade/SKILL.md>) | supporting | plugin-claude |
| [research](<../../../.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/research/SKILL.md>) | supporting | plugin-codex |
| [research-synthesis](<../../../.codex/plugins/cache/claude-cowork/design/1.2.0/skills/research-synthesis/SKILL.md>) | supporting | plugin-codex |
| [scroll-craft](<../.agents/skills/scroll-craft/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [shadcn](<../skills/claude/shadcn/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude, home-codex |
| [shadcn-best-practices](<../../../.codex/plugins/cache/openai-curated/build-web-apps/1dc19589/skills/shadcn-best-practices/SKILL.md>) | primary | plugin-codex |
| [site-teardown](<../skills/claude/site-teardown/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude, home-codex, plugin-codex |
| [sites](<../../../.codex/plugins/cache/openai-curated-remote/sites/1.1.2/skills/sites/SKILL.md>) | primary | plugin-codex |
| [sites-remix](<../../../.codex/plugins/cache/openai-curated-remote/sites/1.1.2/skills/sites-remix/SKILL.md>) | primary | plugin-codex |
| [slack-gif-creator](<../skills/claude/slack-gif-creator/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude |
| [slideshow](<../.agents/skills/slideshow/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [stripe-apps](<../../../.codex/plugins/cache/openai-curated-remote/stripe/8.0.1/skills/stripe-apps/SKILL.md>) | supporting | plugin-codex; updated 2026-10-29 from 8.0.0 |
| [subtitles](<../skills/claude/_inactive/subtitles/SKILL.md>) | supporting | catalog-claude |
| [swiftui-patterns](<../../../.codex/plugins/cache/openai-curated-remote/build-macos-apps/0.1.4/skills/swiftui-patterns/SKILL.md>) | supporting | plugin-codex |
| [talking-head-recut](<../.agents/skills/talking-head-recut/SKILL.md>) | primary | catalog-claude, catalog-codex, project-claude, project-codex |
| [tavily-best-practices](<../../../.agents/skills/tavily-best-practices/SKILL.md>) | supporting | home-agents, home-claude |
| [tavily-cli](<../../../.agents/skills/tavily-cli/SKILL.md>) | supporting | home-agents, home-claude |
| [tavily-crawl](<../../../.agents/skills/tavily-crawl/SKILL.md>) | supporting | home-agents, home-claude |
| [tavily-dynamic-search](<../../../.agents/skills/tavily-dynamic-search/SKILL.md>) | supporting | home-agents, home-claude |
| [tavily-extract](<../../../.agents/skills/tavily-extract/SKILL.md>) | supporting | home-agents, home-claude |
| [tavily-map](<../../../.agents/skills/tavily-map/SKILL.md>) | supporting | home-agents, home-claude |
| [tavily-research](<../../../.agents/skills/tavily-research/SKILL.md>) | supporting | home-agents, home-claude |
| [tavily-search](<../../../.agents/skills/tavily-search/SKILL.md>) | supporting | home-agents, home-claude |
| [template-creator](<../../../.codex/plugins/cache/openai-primary-runtime/template-creator/26.1026.10807/skills/template-creator/SKILL.md>) | supporting | plugin-codex |
| [theme-factory](<../skills/claude/theme-factory/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude |
| [url-to-code](<../../../.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/url-to-code/SKILL.md>) | primary | plugin-codex |
| [user-context](<../../../.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/user-context/SKILL.md>) | primary | plugin-codex |
| [user-research](<../../../.codex/plugins/cache/claude-cowork/design/1.2.0/skills/user-research/SKILL.md>) | primary | plugin-codex |
| [ux-copy](<../../../.codex/plugins/cache/claude-cowork/design/1.2.0/skills/ux-copy/SKILL.md>) | supporting | plugin-codex |
| [view-refactor](<../../../.codex/plugins/cache/openai-curated-remote/build-macos-apps/0.1.4/skills/view-refactor/SKILL.md>) | supporting | plugin-codex |
| [visualize](<../../../.codex/plugins/cache/openai-bundled/visualize/1.0.57/skills/visualize/SKILL.md>) | primary | plugin-codex; updated 2026-10-29 from 1.0.55 |
| [watch](<../skills/claude/watch/SKILL.md>) | primary | catalog-claude, catalog-codex |
| [web-artifacts-builder](<../skills/claude/web-artifacts-builder/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude, plugin-codex |
| [webapp-testing](<../skills/claude/webapp-testing/SKILL.md>) | primary | catalog-claude, catalog-codex, home-agents, home-claude, home-codex, plugin-codex |
| [website-to-hyperframes](<../../../.codex/plugins/cache/openai-curated/hyperframes/1dc19589/skills/website-to-hyperframes/SKILL.md>) | primary | plugin-codex |


## Read-only companion registry

These exact entry points connect vendor and managed skills to this hub without editing their installed packages. A package update may replace vendor instructions; refresh this audit when new skills are installed.

| Installed entry point | Class | Reason kept read-only |
|---|---|---|
| [C:/Users/Joshu/.agents/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/browser/SKILL.md](<../../../.agents/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/browser/SKILL.md>) | supporting | Managed synced copy |
| [C:/Users/Joshu/.agents/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/docx/SKILL.md](<../../../.agents/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/docx/SKILL.md>) | supporting | Managed synced copy |
| [C:/Users/Joshu/.agents/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/frontend-design/SKILL.md](<../../../.agents/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/frontend-design/SKILL.md>) | primary | Managed synced copy |
| [C:/Users/Joshu/.agents/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/pptx/SKILL.md](<../../../.agents/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/pptx/SKILL.md>) | supporting | Managed synced copy |
| [C:/Users/Joshu/.agents/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/site-teardown/SKILL.md](<../../../.agents/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/site-teardown/SKILL.md>) | primary | Managed synced copy |
| [C:/Users/Joshu/.agents/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/web-artifacts-builder/SKILL.md](<../../../.agents/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/web-artifacts-builder/SKILL.md>) | primary | Managed synced copy |
| [C:/Users/Joshu/.agents/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/webapp-testing/SKILL.md](<../../../.agents/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/webapp-testing/SKILL.md>) | primary | Managed synced copy |
| [C:/Users/Joshu/.claude/plugins/cache/21st-dev/21st/1.0.1/skills/21st-ui/SKILL.md](<../../../.claude/plugins/cache/21st-dev/21st/1.0.1/skills/21st-ui/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.11.0/skills/a11y-debugging/SKILL.md](<../../../.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.11.0/skills/a11y-debugging/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.11.0/skills/chrome-devtools-cli/SKILL.md](<../../../.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.11.0/skills/chrome-devtools-cli/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.11.0/skills/chrome-devtools/SKILL.md](<../../../.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.11.0/skills/chrome-devtools/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.11.0/skills/cookie-debugging/SKILL.md](<../../../.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.11.0/skills/cookie-debugging/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.11.0/skills/debug-optimize-lcp/SKILL.md](<../../../.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.11.0/skills/debug-optimize-lcp/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.9.0/skills/a11y-debugging/SKILL.md](<../../../.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.9.0/skills/a11y-debugging/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.9.0/skills/chrome-devtools-cli/SKILL.md](<../../../.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.9.0/skills/chrome-devtools-cli/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.9.0/skills/chrome-devtools/SKILL.md](<../../../.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.9.0/skills/chrome-devtools/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.9.0/skills/cookie-debugging/SKILL.md](<../../../.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.9.0/skills/cookie-debugging/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.9.0/skills/debug-optimize-lcp/SKILL.md](<../../../.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.9.0/skills/debug-optimize-lcp/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-best-practices/SKILL.md](<../../../.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-best-practices/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-captions/SKILL.md](<../../../.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-captions/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-create/SKILL.md](<../../../.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-create/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-docs/SKILL.md](<../../../.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-docs/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-interactivity/SKILL.md](<../../../.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-interactivity/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-maps/SKILL.md](<../../../.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-maps/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-markup/SKILL.md](<../../../.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-markup/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-multimedia/SKILL.md](<../../../.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-multimedia/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-render/SKILL.md](<../../../.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-render/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-saas/SKILL.md](<../../../.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-saas/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-studio/SKILL.md](<../../../.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-studio/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-upgrade/SKILL.md](<../../../.claude/plugins/cache/remotion/remotion/4.0.523/skills/remotion-upgrade/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.claude/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/browser/SKILL.md](<../../../.claude/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/browser/SKILL.md>) | supporting | Managed synced copy |
| [C:/Users/Joshu/.claude/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/built-in-browser/SKILL.md](<../../../.claude/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/built-in-browser/SKILL.md>) | supporting | Managed synced copy |
| [C:/Users/Joshu/.claude/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/chrome-browser/SKILL.md](<../../../.claude/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/chrome-browser/SKILL.md>) | supporting | Managed synced copy |
| [C:/Users/Joshu/.claude/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/computer-use/SKILL.md](<../../../.claude/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/computer-use/SKILL.md>) | supporting | Managed synced copy |
| [C:/Users/Joshu/.claude/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/docx/SKILL.md](<../../../.claude/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/docx/SKILL.md>) | supporting | Managed synced copy |
| [C:/Users/Joshu/.claude/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/frontend-design/SKILL.md](<../../../.claude/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/frontend-design/SKILL.md>) | primary | Managed synced copy |
| [C:/Users/Joshu/.claude/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/pptx/SKILL.md](<../../../.claude/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/pptx/SKILL.md>) | supporting | Managed synced copy |
| [C:/Users/Joshu/.claude/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/site-teardown/SKILL.md](<../../../.claude/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/site-teardown/SKILL.md>) | primary | Managed synced copy |
| [C:/Users/Joshu/.claude/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/web-artifacts-builder/SKILL.md](<../../../.claude/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/web-artifacts-builder/SKILL.md>) | primary | Managed synced copy |
| [C:/Users/Joshu/.claude/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/webapp-testing/SKILL.md](<../../../.claude/skills/synced/66ab068d-6d11-4b9b-bace-f3622629a61f_3264ecb8-7644-4b8c-9aed-94ea1fae19cc/webapp-testing/SKILL.md>) | primary | Managed synced copy |
| [C:/Users/Joshu/.codex/plugins/cache/21st-dev/21st/1.0.1/skills/21st-ui/SKILL.md](<../../../.codex/plugins/cache/21st-dev/21st/1.0.1/skills/21st-ui/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/claude-cowork/anthropic-skills/1.0.0/skills/browser/SKILL.md](<../../../.codex/plugins/cache/claude-cowork/anthropic-skills/1.0.0/skills/browser/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/claude-cowork/anthropic-skills/1.0.0/skills/docx/SKILL.md](<../../../.codex/plugins/cache/claude-cowork/anthropic-skills/1.0.0/skills/docx/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/claude-cowork/anthropic-skills/1.0.0/skills/frontend-design/SKILL.md](<../../../.codex/plugins/cache/claude-cowork/anthropic-skills/1.0.0/skills/frontend-design/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/claude-cowork/anthropic-skills/1.0.0/skills/pptx/SKILL.md](<../../../.codex/plugins/cache/claude-cowork/anthropic-skills/1.0.0/skills/pptx/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/claude-cowork/anthropic-skills/1.0.0/skills/site-teardown/SKILL.md](<../../../.codex/plugins/cache/claude-cowork/anthropic-skills/1.0.0/skills/site-teardown/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/claude-cowork/anthropic-skills/1.0.0/skills/web-artifacts-builder/SKILL.md](<../../../.codex/plugins/cache/claude-cowork/anthropic-skills/1.0.0/skills/web-artifacts-builder/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/claude-cowork/anthropic-skills/1.0.0/skills/webapp-testing/SKILL.md](<../../../.codex/plugins/cache/claude-cowork/anthropic-skills/1.0.0/skills/webapp-testing/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/claude-cowork/design/1.2.0/skills/accessibility-review/SKILL.md](<../../../.codex/plugins/cache/claude-cowork/design/1.2.0/skills/accessibility-review/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/claude-cowork/design/1.2.0/skills/design-critique/SKILL.md](<../../../.codex/plugins/cache/claude-cowork/design/1.2.0/skills/design-critique/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/claude-cowork/design/1.2.0/skills/design-handoff/SKILL.md](<../../../.codex/plugins/cache/claude-cowork/design/1.2.0/skills/design-handoff/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/claude-cowork/design/1.2.0/skills/design-system/SKILL.md](<../../../.codex/plugins/cache/claude-cowork/design/1.2.0/skills/design-system/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/claude-cowork/design/1.2.0/skills/research-synthesis/SKILL.md](<../../../.codex/plugins/cache/claude-cowork/design/1.2.0/skills/research-synthesis/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/claude-cowork/design/1.2.0/skills/user-research/SKILL.md](<../../../.codex/plugins/cache/claude-cowork/design/1.2.0/skills/user-research/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/claude-cowork/design/1.2.0/skills/ux-copy/SKILL.md](<../../../.codex/plugins/cache/claude-cowork/design/1.2.0/skills/ux-copy/SKILL.md>) | supporting | Plugin package |
| [visualize 1.0.57](<../../../.codex/plugins/cache/openai-bundled/visualize/1.0.57/skills/visualize/SKILL.md>) | primary | Plugin package; 1.0.55 entrypoint hash matched |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated-remote/build-macos-apps/0.1.4/skills/appkit-interop/SKILL.md](<../../../.codex/plugins/cache/openai-curated-remote/build-macos-apps/0.1.4/skills/appkit-interop/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated-remote/build-macos-apps/0.1.4/skills/liquid-glass/SKILL.md](<../../../.codex/plugins/cache/openai-curated-remote/build-macos-apps/0.1.4/skills/liquid-glass/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated-remote/build-macos-apps/0.1.4/skills/swiftui-patterns/SKILL.md](<../../../.codex/plugins/cache/openai-curated-remote/build-macos-apps/0.1.4/skills/swiftui-patterns/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated-remote/build-macos-apps/0.1.4/skills/view-refactor/SKILL.md](<../../../.codex/plugins/cache/openai-curated-remote/build-macos-apps/0.1.4/skills/view-refactor/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated-remote/google-drive/0.1.22/skills/google-slides/SKILL.md](<../../../.codex/plugins/cache/openai-curated-remote/google-drive/0.1.22/skills/google-slides/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-simple-dark-mode/SKILL.md](<../../../.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-simple-dark-mode/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-simple-light-mode/SKILL.md](<../../../.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-simple-light-mode/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/audit/SKILL.md](<../../../.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/audit/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/design-qa/SKILL.md](<../../../.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/design-qa/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/get-context/SKILL.md](<../../../.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/get-context/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/ideate/SKILL.md](<../../../.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/ideate/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/image-to-code/SKILL.md](<../../../.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/image-to-code/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/index/SKILL.md](<../../../.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/index/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/research/SKILL.md](<../../../.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/research/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/url-to-code/SKILL.md](<../../../.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/url-to-code/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/user-context/SKILL.md](<../../../.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/user-context/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated-remote/sites/1.1.2/skills/sites-remix/SKILL.md](<../../../.codex/plugins/cache/openai-curated-remote/sites/1.1.2/skills/sites-remix/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated-remote/sites/1.1.2/skills/sites/SKILL.md](<../../../.codex/plugins/cache/openai-curated-remote/sites/1.1.2/skills/sites/SKILL.md>) | primary | Plugin package |
| [stripe-apps 8.0.1](<../../../.codex/plugins/cache/openai-curated-remote/stripe/8.0.1/skills/stripe-apps/SKILL.md>) | supporting | Plugin package; 8.0.1 entrypoint reviewed |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated-remote/work-pets/0.1.6/skills/create-pet/SKILL.md](<../../../.codex/plugins/cache/openai-curated-remote/work-pets/0.1.6/skills/create-pet/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated/build-web-apps/1dc19589/skills/frontend-app-builder/SKILL.md](<../../../.codex/plugins/cache/openai-curated/build-web-apps/1dc19589/skills/frontend-app-builder/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated/build-web-apps/1dc19589/skills/frontend-testing-debugging/SKILL.md](<../../../.codex/plugins/cache/openai-curated/build-web-apps/1dc19589/skills/frontend-testing-debugging/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated/build-web-apps/1dc19589/skills/react-best-practices/SKILL.md](<../../../.codex/plugins/cache/openai-curated/build-web-apps/1dc19589/skills/react-best-practices/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated/build-web-apps/1dc19589/skills/shadcn-best-practices/SKILL.md](<../../../.codex/plugins/cache/openai-curated/build-web-apps/1dc19589/skills/shadcn-best-practices/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated/hyperframes/1dc19589/skills/gsap/SKILL.md](<../../../.codex/plugins/cache/openai-curated/hyperframes/1dc19589/skills/gsap/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated/hyperframes/1dc19589/skills/hyperframes-cli/SKILL.md](<../../../.codex/plugins/cache/openai-curated/hyperframes/1dc19589/skills/hyperframes-cli/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated/hyperframes/1dc19589/skills/hyperframes-registry/SKILL.md](<../../../.codex/plugins/cache/openai-curated/hyperframes/1dc19589/skills/hyperframes-registry/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated/hyperframes/1dc19589/skills/hyperframes/SKILL.md](<../../../.codex/plugins/cache/openai-curated/hyperframes/1dc19589/skills/hyperframes/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated/hyperframes/1dc19589/skills/website-to-hyperframes/SKILL.md](<../../../.codex/plugins/cache/openai-curated/hyperframes/1dc19589/skills/website-to-hyperframes/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated/openai-developers/1dc19589/skills/build-chatgpt-app/SKILL.md](<../../../.codex/plugins/cache/openai-curated/openai-developers/1dc19589/skills/build-chatgpt-app/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-curated/stripe/1dc19589/skills/stripe-apps/SKILL.md](<../../../.codex/plugins/cache/openai-curated/stripe/1dc19589/skills/stripe-apps/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-primary-runtime/documents/26.1026.10807/skills/documents/SKILL.md](<../../../.codex/plugins/cache/openai-primary-runtime/documents/26.1026.10807/skills/documents/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-primary-runtime/pdf/26.1026.10807/skills/pdf/SKILL.md](<../../../.codex/plugins/cache/openai-primary-runtime/pdf/26.1026.10807/skills/pdf/SKILL.md>) | primary | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-primary-runtime/presentations/26.1026.10807/skills/presentations/SKILL.md](<../../../.codex/plugins/cache/openai-primary-runtime/presentations/26.1026.10807/skills/presentations/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.codex/plugins/cache/openai-primary-runtime/template-creator/26.1026.10807/skills/template-creator/SKILL.md](<../../../.codex/plugins/cache/openai-primary-runtime/template-creator/26.1026.10807/skills/template-creator/SKILL.md>) | supporting | Plugin package |
| [C:/Users/Joshu/.codex/skills/.system/imagegen/SKILL.md](<../../../.codex/skills/.system/imagegen/SKILL.md>) | primary | Bundled system skill or symlink |


## How to keep this accurate

When adding or changing a design skill, route its canonical and already-existing activated custom copies back to [README.md](README.md), without replacing customizations. Register vendor-owned skills here instead of editing package caches. Use the inventory runner to inspect newly discovered metadata, then review classifications before applying pointers. The inventory is a dated audit, not a background watcher.

The sole compare-and-swap skip was a shared `orca-cli` copy whose other path had already received the block; a fresh read verified that it also contained the hub pointer. All other eligible edits were appended after their expected hash matched.
