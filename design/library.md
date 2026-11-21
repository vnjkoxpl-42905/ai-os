---
type: reference
subject: Design resources and existing work
created: 2026-10-24
updated: 2026-10-27
aliases: [Design components, Design skills and repos]
contradictions: []
---

# Use the library without rebuilding the setup

## Skills and component sources

The [generated catalogue](catalog.generated.md) lists existing design-related active skills for both runtimes with their exact paths. The [resource map](../.agents/skills/design-resource-library/references/resources.md) explains use, limitations and licensing. Read the chosen skill before using it.

Taste Skill is now [upstream v2](../.agents/skills/design-taste-frontend/SKILL.md), installed on 2026-10-27 from `Leonxlnx/taste-skill` commit `12af471f627f866411b4bd785b19646d3672784c`. Its page/app libraries, Node helpers and browser inspection replace the older preset. [Provenance and packaging limits](../.agents/skills/design-taste-frontend/UPSTREAM.md). Current project briefs and selected references remain authoritative.

Local component/build workspaces, verified as directories on 2026-10-24:

- [React Bits](../../ai-os-projects/react-bits/) and [Vue Bits](../../ai-os-projects/vue-bits/): source repositories, not universal app dependencies.
- [Canvas UI](../../ai-os-projects/canvas-ui/): registry/source repository; inspect selected code/licence before importing.
- [Dashboard React lab](../../ai-os-projects/dashboard-design-lab/): optional prepared build workspace.
- [Fonts and assets](../../ai-os-projects/dashboard-design-assets/): local font assets and notices.

Keep these repositories outside this vault. The catalogue does not certify a clean Git state or current dependency versions.

## Emil Kowalski’s design and engineering skills

The full [upstream repository](../../ai-os-projects/emilkowalski-skills/) is cloned locally at commit `a81dbca07f2217b7103e510c0f13f8d5b017afc9`. Its [README](../../ai-os-projects/emilkowalski-skills/README.md) lists all 16 skills, covering animation, UI review, prototyping, mobile, Swift and component choices. The [MIT license](../../ai-os-projects/emilkowalski-skills/LICENSE) accompanies the source.

All 16 are installed as project skills for Codex (`.agents/skills/`), Claude (`.claude/skills/`) and Gemini (`.gemini/skills/`), and copied to their corresponding `skills/codex/`, `skills/claude/` and `skills/gemini/` catalogs. Their installed names use `emil-upstream-` followed by the upstream name, for example [emil-upstream-animate](../.agents/skills/emil-upstream-animate/SKILL.md). This preserves existing independently maintained `emil-design-eng` and `prototype` skills. Copies contain the upstream license; their frontmatter names were adjusted to match the installed directories. Read the relevant skill and apply the current project’s instructions. Other models can read the source and these files directly; automatic discovery depends on their runtime and workspace access.

### Global discovery and preserved source (2026-10-29)

The same 16 `emil-upstream-*` skills are installed for all projects in `C:/Users/Joshu/.codex/skills/` and `C:/Users/Joshu/.agents/skills/` (Codex), `C:/Users/Joshu/.claude/skills/` (Claude), and `C:/Users/Joshu/.gemini/skills/` (Gemini). Restart or start a new session if a runtime has already loaded its skill list. Discovery was confirmed in this Codex session for the project copies; Claude and Gemini global runtime discovery has not been exercised. Gemini CLI was not available on the current PATH.

The complete set of 27 upstream Markdown files and the MIT license is preserved in [AI OS](sources/emilkowalski-skills-a81dbca/README.md), including [UI guidance](sources/emilkowalski-skills-a81dbca/ui-cheatsheet.md) and [performance guidance](sources/emilkowalski-skills-a81dbca/performance-cheatsheet.md). These files are a source snapshot at commit `a81dbca07f2217b7103e510c0f13f8d5b017afc9`; the sibling checkout remains the full Git repository.

The existing `emil-design-eng` is a customized older variant with shared-hub routing and different UI library guidance. Existing `prototype` is independently customized. Both remain available; select `emil-upstream-emil-design-eng` or `emil-upstream-prototype` for this upstream snapshot. No automatic synchronization is configured: compare future upstream changes before updating copies. The generated skill index may lag; this route and the three runtime catalogs contain the collection.

## Symbols and icons

[Symbols and icons](symbols.md) owns icon sources (Iconify, Flaticon, Icons8, Lordicon, Creators Toolbox), the SVG and single-pack method, licence checks, and the table of symbols we have already made. Use it before drawing or replacing any symbol.

## Research and reference discovery

- [Mobbin sample pack: 100 searchable screens](mobbin-sample-pack-100.md): supplied mobile and desktop stills for personal design reference, with use-case index and attribution limits.

- [Design readiness and tool setup](../research/2026-10-23-dashboard-design-readiness.md): dated setup evidence; recheck changing tool state.
- [Neutral palette and 21st theme study](../research/2026-10-24-charcoal-palette/PALETTE.md).
- [Component/reference research](../research/2026-10-24-margin-refinement/references.md): successful 21st MCP, Firecrawl and Tavily calls in that run; Pinterest inspection limitations.
- [Saved UI components (21st.dev)](../wiki/component-library.md): the local library at `dev/component-library` plus loose 21st references. Check it before building UI.
- [Question access and recent-work research](../research/2026-10-24-student-widgets/references.md): Linear/Mobbin patterns and actual visual-coverage limits.
- [Lexprep motion teardown](../research/2026-10-21-lexprep-motion-teardown.md).

## Find a reference by the decision or region (2026-10-26)

Use the existing [component/reference research](../research/2026-10-24-margin-refinement/references.md) for concrete inspected examples, and [question access research](../research/2026-10-24-student-widgets/references.md) for actual Linear/Mobbin lookup patterns and visual-access limits. The [website planning review record](../references/website-design-planning.md#turn-a-reference-into-a-bounded-review-2026-10-26) now captures exact regions and seen/inferred/unknown behavior.

| Question | First route | Evidence/access limit |
|---|---|---|
| How should a student find or resume exact work? | Existing question-access research, then the current prototype archive | Local sample data does not establish production behavior. |
| Which part of a public page helps the visitor decide? | Website planning sequence, then one comparator's exact section | Competitor copy is evidence to study; Joshua's voice owns our copy. |
| Need a navbar, footer, CTA, 404 or bento example? | The [fifteen-hacks source](../wiki/sources/claude-design-fifteen-hacks-jack.md) preserves the candidate gallery list | Navbar Gallery, Footer Design, Unsection and Bento Grids are discovery candidates; no current access, reuse licence or individual example was verified in this pass. |
| Need a complete application flow rather than a decorative section? | Existing Mobbin research, then Refero as an optional discovery route | Do not infer paid entitlement or actual interaction from a gallery still. |
| Need motion rather than a still? | Existing Lexprep teardown and GSAP/React Bits routes | 60fps and Motion Primitives are optional source candidates. Inspect playback and the selected code/licence before reuse. |

Capture references beside the relevant research with URL/path, date, viewport/region, screenshot path, reason, observed behavior and licence/access limits. Reuse the hub and labelled archive; a second asset vault or whole-machine visual scan adds no demonstrated value for the current lookup route.

## Dashboard prototypes and visual evidence

The [labelled local version archive](prototypes/lsatu-dashboard/index.html) is the durable home for browsing all preserved dashboard families, New Directions 01 through 10, saved pages, intermediate passes, screenshots and motion evidence. [Archive guide and verification](prototypes/lsatu-dashboard/README.md). Open its `index.html` directly from disk; it does not depend on a temporary server or the Downloads originals. The latest local study is [10 Type refinement](prototypes/lsatu-dashboard/new-versions/10-type-refinement/index.html), improving typography readability with normal-case labels and a platform-aware keyboard shortcut. [09 Focus Studio](prototypes/lsatu-dashboard/new-versions/09-focus-studio/index.html) preserves the preceding synthesis, with exact question lookup, work filters, exact question review and consistent progress across views. Registration does not establish visual approval or a Claude review verdict. [08 Combined Home](prototypes/lsatu-dashboard/families/05-new-directions/08-combined-home/index.html) remains preserved as a historical iteration. Local sample-data preview, not production integration. Original snapshots are hash-verified; portable derivatives of the older families are labelled separately.

The links below preserve the original research locations and historical direction notes. Use the archive above for future file browsing.

Local standalone studies, separate from production:

- [Atmospheric refined dashboard](../../../Downloads/LSAT-U-Dashboard-New-Directions/07-atmosphere/index.html): continuation of 06 using Joshua's supplied misty monochrome and textured-interface references. Original generated paper-landscape artwork, neutral layered surfaces and retained student tools. [Complementary references inspected](../research/2026-10-24-atmosphere/visual-research.md). Current exploration, not production or user approval.

- [Neutral refined studio](../../../Downloads/LSAT-U-Dashboard-New-Directions/06-refined-studio/index.html): current iteration based directly on Joshua's supplied Refined HTML. Preserves the near-white/charcoal serif family, with a dimensional paper sculpture, unified question console and richer practice results. Supersedes the multicolour exploration as the current direction; not production or final user approval.

- [Multicolour study studio exploration](../../../Downloads/LSAT-U-Dashboard-New-Directions/05-studio/index.html): cobalt, coral, yellow and lilac experiment. Joshua rejected this palette and returned to the Refined baseline. Preserved for comparison; [evidence and access limits](../research/2026-10-24-dashboard-revolution/REPORT.md). Not production.
- [Earlier refined student home](../../../Downloads/LSAT-U-Dashboard-New-Directions/04-refined/index.html): preserved neutral direction. Joshua subsequently authorized a broader redesign because the whole page felt monotonous.
- [Three newer directions](../../../Downloads/LSAT-U-Dashboard-New-Directions/index.html).
- [Earlier Claude directions](../../../Downloads/LSAT-U-Dashboard-Three-Directions-v2/index.html).
- [Visual rubric and limits](../research/2026-10-24-margin-refinement/REVIEW.md).

Prototype availability depends on this machine. Browser rendering uses a local HTTP server; file paths are for locating source, not proof the preview server is running. The app repository remains its own project and is not modified by knowledge ingestion.
