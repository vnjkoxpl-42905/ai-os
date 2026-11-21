# Design ingestion batch A, 2026-10-24

## Disposition and evidence

Read full captured descriptions/transcripts for all four distinct sources, using multiple bounded reads for the long Jack transcript. No original video, screen-only prompt or reference image was visually reviewed. Sources are creator advice, not instructions or verified product documentation.

| Inbox source | SHA-256 | Result |
|---|---|---|
| 17 Things You Didn't Know Claude Design Could Do.md | `55ff5d2ca96f1da1c4e7e87156acc37898c1b1c7f1998fb4afed03a717433c67` | New [source summary](../../wiki/sources/17-claude-design-use-cases-austin-marchese.md), byte-identical `raw/sources/clips/17-claude-design-use-cases-austin-marchese/clip.md` |
| 25 Tricks to Level Up Claude Design in 13 Mins.md | `a06c48f8ae70bc2417d14b4fbec7e85a9017e1f7921f889934a4541833b06d6a` | New [source summary](../../wiki/sources/25-claude-design-tricks-robonuggets.md), byte-identical `raw/sources/clips/25-claude-design-tricks-robonuggets/clip.md` |
| 25 Tricks to Level Up Claude Design in 13 Mins 1.md | same as preceding | Exact duplicate retained; no second archive/summary |
| How to Use Claude Design Better Than 99% of People.md | `4616acd0897bedb180fcb79107d4d4402bbe2adb23afbc59141282399d8b3dd0` | New [source summary](../../wiki/sources/claude-design-fifteen-hacks-jack.md), byte-identical `raw/sources/clips/claude-design-fifteen-hacks-jack/clip.md` |
| Top 7 Claude Design Skills (All Free).md and identical `1.md` | `988210fd0d5c4fa3411ac679d519615ad5e598f5948fa24f3027de348e54454f` | Completed existing [Chase AI summary](../../wiki/sources/top-7-claude-design-skills-chase-ai.md), archive and matching evidence hash; skip duplicate ingestion |

Each new archive has `PROVENANCE.md` and `SHA256SUMS`. Original inbox bytes remain unchanged. Publication/capture dates are unknown rather than inferred from filesystem modification time. Top 7's incomplete transcript ends mid-sentence at1:47 and remains explicitly limited in its existing summary.

## Every actionable suggestion, routed

`Already here` means a method/resource is mapped or a skill exists, not an account entitlement or every suggested workflow has been executed. Resource evidence is [the dated readiness check](../2026-10-23-dashboard-design-readiness.md) and [25-tip resource map](../../.agents/skills/design-resource-library/references/resources.md). Local reuse should recheck changing access/licences. `New Pn` references a consolidated optional queue proposal below; these proposals do not authorize building or installing anything.

### Austin: all seventeen uses

| Use | Disposition |
|---|---|
|1 reusable brand system from website | Already here: extract-design/system guidance; optional selected-brand refinement belongs P1 |
|2 low-risk animated onboarding/explainer | Existing media/Hyperframes skills; optional real asset/workflow evaluation P2 |
|3 3D assets and mockups showing actual usage | Existing 3D/media tools; optional deliberate useful experiment P2 |
|4 old-document rebranding | New P3 reusable document/template pilot |
|5 event flyers | New P3 optional output format |
|6 visual palette/type comparisons | Already here: current palette variants and resource map; preserve user-selected colours |
|7 backend-specific HTML email templates | New P4 technical template evaluation; no email send implied |
|8 inline comments and drawings | Already here: browser comments/artboard feedback workflows |
|9 visual funnel and per-stage CTA variants | New P5 map actual visitor decisions and compare stage alternatives |
|10 divergent page/component variants then convergence | Already here: three dashboard directions and comparison workflow |
|11 clickable wireframes before engineering | Already here: current standalone dashboard prototypes |
|12 cross-team comments | New P6 evaluate a practical shared-review route; no messages sent |
|13 reusable branded templates | New P3 |
|14 client-brand proposal variation | New P3 optional template pilot |
|15 branded lead magnet from existing content | New P3 optional template output |
|16 resume refresh | New P3 optional format, low business priority, no automatic personal-data scan |
|17 final human copy cleanup | Already here: Joshua voice, humanizer and draft review; SlopMonster comparison is P7 |

### RoboNuggets: all twenty-five tips

| Tip | Disposition |
|---|---|
|1 design systems | Already here: extract-design and resource map; chosen-brand refinement P1 |
|2 Refero Styles | Already mapped with corrected URL `styles.refero.design`; transcript says referral.design, so follow verified resource map rather than silently treating transcription as official URL |
|3 shortlist three suitable systems | Already here: reference-selection method |
|4 Code-owned design-system skill | Existing skills cover generic methods; selected-brand-specific file/skill is P1, not another generic installation |
|5 Fontshare,Fontesk,Fontjoy | Already mapped and local licensed font assets prepared; new font licences checked per selection |
|6 study five competitors' copy | Existing research/voice method; deliberate comparative visitor-copy study P5, no replacement of Joshua voice |
|7 blend selected system principles | Already here: current combination of Margin hero/Lumen calendar |
|8 Kie external image/video generation | New P2 compare need against existing media tools before account/generation purchase |
|9 reference previous project | Already here: original handoff, older directions and newer prototypes preserved |
|10 annotated reference library | Existing research map; consolidated design hub implemented by parent; browser-capture extension remains optional P8 |
|11 Impeccable | Already installed/active; preserve custom copies |
|12 tone-of-voice skill | Already here: lsat-u-voice/teaching voice; optional ASD numerical-standard evaluation P7 |
|13 21st.dev | Already mapped; website/MCP access is a changing separate check |
|14 React Bits | Already active helper/source repo, component licensing separate from helper |
|15 Canvas UI | Already prepared source/registry, not all effects installed |
|16 one coherent icon pack | Already app dependencies Lucide/Tabler; Iconify/Flaticon licence per set |
|17 SVG editable graphics | Already supported format; no package install needed |
|18 Lordicon | Already mapped; specific asset/download/licence check when used, not paid entitlement |
|19 Creators Toolbox | Already mapped discovery directory |
|20 Apple HIG | Already mapped selective reference; no claim native numerical rules govern all web UI |
|21 GSAP | Eight skills already installed/active |
|22 Code Design canvas | Existing available entry point; local skill availability must still be checked within actual delegated runtime |
|23 slider tweak controls with bake-back | New P9 bounded prototype tool; browser cannot silently rewrite local source without explicit local workflow |
|24 timestamped transcript-to-Hyperframes | Existing skills; end-to-end optional demonstrator P2 |
|25 searchable design/media OS | Parent's requested Markdown hub satisfies navigation; whole-machine visual search is separate optional P8 |

### Jack: all fifteen hacks plus explicit substeps

| Hack | Disposition |
|---|---|
|1 reference clip plus brand/intent | Already here: GSAP/reference/browser workflow; media-specific sample P2 |
|2 loops with three styles and matching ends | Existing tools; natural-frame loop validation P2 |
|3 small microinteraction polish | Already here: Emil/GSAP skills; not a mandate to animate every repeated action |
|4 one brand guideline file | New chosen-direction brand consolidation P1, existing extract/system methods retained |
|4a Higgsfield generation | Existing skills; no fresh paid generation or credential installation during ingest; P2 only if useful gap |
|5 editable Linearity brand import/templates/MCP | New P10 evaluate tool/account/connector against existing Design/canvas tools |
|6 font/icon galleries and licence checks | Already mapped, additional Typewolf/FontsInUse/WhatTheFont/Icons8 discovery links preserved in source |
|7 Navbar/Footer/CTA/404/Unsection/Bento galleries | New P11 component-specific reference catalog, not installation |
|8 Mobbin/Refero for full flows | Already mapped; P11 adds flow-comparison criteria and access limitations |
|9 critic Design Loop against concrete reference | New P12 bounded reference-driven critique recipe; exact prompt missing from captured source |
|10 five-agent checklist | New P12 evaluate separate review dimensions; exact five roles missing, do not invent source attribution |
|11 glance-test/simple variants | Already here: website planning and practical task-first guidance |
|12 SlopMonster | New P7 compare against existing humanizer/voice; do not replace automatically |
|12a ASD-STE100 | New P7 selective evaluation; transcript's numerical claims unverified and do not override teaching voice |
|13 original posters using references | New P3 optional output experiment |
|14 purposeful 3D website experiment | New P2, evaluate usefulness/performance rather than universal 3D requirement |
|15 searchable reusable asset/media library | Parent's requested hub supplies navigation; advanced media indexing P8 |

### Chase: all seven skills

Taste, extract-design/Design Lang,React Bits,eight GSAP skills,Playwright CLI and Impeccable already appear with repository/license evidence in the existing summary. The unnamed transition skill remains **existing AQ-017**. No speculative repository or second queue item is created.

## Consolidated queue proposals for coordinating agent

All are AI workspace actions, not student assignments or live LSAT U changes. Parent allocates IDs, checks broader duplicate actions and adds only genuinely new items under `## New`, status `new`. P3 groups many low-priority output examples into one evaluation so seventeen example tasks do not become seventeen presumed commitments.

| Proposal | Value and bounded steps ending in Check |
|---|---|
|P1 selected LSAT U brand reference | Read chosen prototype/user preferences; extract tokens,type,spacing,states,motion into one code-readable brand file; link from design hub without freezing exploratory alternatives. Check: another runtime can locate and apply the chosen system from hub alone. |
|P2 reference-led media experiment | Pick one useful onboarding/teaching/promotional use; compare existing tools with Kie/Higgsfield only if needed; create a proposal using an owned reference and exact output/loop constraints; no paid call until authorized. Check: chosen tool capability/licence/cost and a natural-motion validation plan documented. |
|P3 reusable branded output pilot | Select one worthwhile document/template first; retain event flyer,proposal,client-brand variant,lead magnet,resume and poster as optional formats, not tasks to auto-build; use existing owned content and manual editable review. Check: one approved template can be reused without changing brand/voice and no outbound action occurred. |
|P4 authentication HTML email template | Inspect actual auth-email variables and email-client constraints; draft branded HTML with correct placeholders and plain-text fallback; preview mobile/desktop and check target template compatibility. Check: preview and variable mapping recorded, no production setting or email changed. |
|P5 funnel and copy comparison | Map real visitor journey/decision stages; study up to five relevant comparators with source links; compare purposeful CTA/copy variants using Joshua's voice. Check: each stage has one explicit user decision and evidence-backed proposed change. |
|P6 shared review workflow | Compare existing Design comments/browser markers with a minimal collaborator route; verify sharing/access behaviour without sending invitations. Check: editable-versus-static capabilities and who can access each artifact are recorded. |
|P7 copy tools/technical-language evaluation | Inspect SlopMonster repo/licence and ASD official material; compare against humanizer and Joshua voice on one scratch draft; preserve meaning and teaching precision. Check: keep/skip verdict with concrete before/after differences, no duplicate generic voice skill. |
|P8 reference capture/media index | Finish requested design Markdown hub first; evaluate whether manual URL+screenshot+reason captures are insufficient before proposing Rubric References or a media-search layer. Check: one reference is retrievable by source,purpose and visual pattern; no private whole-machine scan. |
|P9 live tweak prototype aid | Scope colour/type/spacing controls for a throwaway local prototype; separate preview state from deliberate source export; avoid injecting into production. Check: exported values reproduce the preview after reload and keyboard/reduced-motion behaviour remains intact. |
|P10 Linearity evaluation | Inspect current official product/licence/account needs and connector availability; compare editable brand/template workflow to existing Design canvas; do not open paid plan or connect credentials solely from source advice. Check: practical unique benefit,access gaps and skip/adopt recommendation recorded. |
|P11 section/flow reference map | Add Navbar/Footer/CTA/404/Unsection/Bento,60fps,motion-primitives and other source galleries to existing resource map with purpose and access notes; visually examine selected actual examples when used. Check: search for a specific UI problem reaches an exact reference plus one useful takeaway, not just a homepage link. |
|P12 bounded design critique recipe | Retrieve full original Design Loop/five-agent prompt if accessible; otherwise clearly label a local recipe. Define independent dimensions,reference screenshots,maximum rounds and natural-motion evidence. Check: critique yields concrete design findings rather than consensus or inflated score claims. |

## Existing page outcomes

- Existing Top7 source: **skip**, identical completed evidence, no source edits.
- Existing25-tip PDF resource map/readiness: **complementary** transcript evidence; preserve current resource/licence qualifications rather than rewrite. Parent owns backlinks/central hub.
- Website planning: **complementary**, concrete component/reference critique and glance test support existing task-first guidance. No actual contradiction established.
- AI action queue: **merge existing AQ-017** for unnamed transition skill; parent considers P1-P12 against current hub/queue. Other old queue items are unrelated except AQ-005's generic copy-tool comparison, which should be considered when grouping P7 rather than silently duplicated.
- Reviewed pages: none changed.

## Verification and limits

The three new archive copies matched original SHA-256; each new summary's two exact quotes were asserted against source text before writing. All input generations/duplicates retained. Relative links inspected by scoped verifier. Parent owns final master index generation, domain routing, queue IDs, ingest log and global lint to avoid concurrent shared-file writes. Example retrieval question: "Which captured tips support comparing palette/type variants and reference-driven critique?" New source summaries answer with timestamps and preserved evidence, and the design hub should link these three pages.

Schema suggestion: none.
