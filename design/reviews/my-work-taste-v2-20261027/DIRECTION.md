# My Work notes: proposed visual direction

2026-10-27. Approval pending. No application source changed, committed, pushed or published.

## Verified workflow

- Loaded C:/Users/Joshu/dev/ai-os/.agents/skills/design-taste-frontend/SKILL.md, heading tasteskill v2.
- UPSTREAM.md identifies 12af471f627f866411b4bd785b19646d3672784c. Scripts, references and library exist.
- Read the full main skill, full app-screen workflow and critique guide, plus typography, colour and relevant interaction/reduced-motion guidance.
- App library offered achromatic-ledger and editorial-greeting. Selected editorial-greeting, seed 1136768603, keeping palette and type. Adapt its editorial hierarchy and tonal structure to the existing My Work noun title, without introducing a greeting or marketing sections.
- Product question: Which teaching note or recap should I return to now?
- Product face: warm study paper, charcoal ink, Fraunces note titles and Outfit controls.
- Product signature: a chronological teaching archive with exact type/date, meaningful unread state, and direct return to an explanation.

## Evidence actually inspected

Live signed-in notes page: desktop and phone captures. This account has four Notes and zero unread teaching notes, so the Type control is correctly absent. Do not fabricate categories to expose it.

Local actual-component fixture: 16 synthetic notes across types/months, three unread. Ran inspect.mjs at 1440, 768 and 390; opened all six fold/full-page image sheets. This fixture uses a representative shell, not the full authenticated classroom shell. It is served in development mode, not a production acceptance build.

21st.dev free metadata search returned Basic Select, Select and HeroUI Select alternatives. No external component code retrieved or dependency installed. Existing installed Radix Select is the recommended base.

Source inventory includes archive, personal note list/editor, detail return, loading/error/empty states and installed Select integration. Non-default states have source coverage at this phase, not fresh rendered acceptance.

## Proposed changes after approval

1. Make search, All/Unread and Type one coherent toolbar: shared height, baseline, radius, label size and focus treatment. On phone use full-width search followed by one compact filter row where content fits; reflow rather than clip at zoom or with long labels.
2. Replace native Type select with the existing accessible Radix Select. Opaque warm paper popup, modest radius, fine edge, contact plus ambient elevation, charcoal text, pale selected/hovered option and a checkmark. Distinguish selected, pointer hover and keyboard focus. Portal receives explicit scoped light/dark palette ownership.
3. Keep the paper/charcoal identity and layered material hierarchy. Quiet the resting archive shadow rather than flattening everything to white. Reserve pronounced elevation for real overlays.
4. Tighten title-to-navigation-to-archive spacing, with an app-sized heading and a consistent serif title/sans utility scale. Reduce competing border weights and retain readable metadata.
5. Keep notes primary and Personal notes subordinate. Align type, title, excerpt, date and Read note action consistently across the lead and regular rows. Preserve useful excerpts, honest dates and existing month groups.
6. Carry this language into detail/Back, Personal notes list/editor, save/conflict/error states and all empty/loading/filtered states. Use short menu/press feedback and disable travel/scale under reduced motion.

## Baseline critique

ROUND 0
Seen in one second: My Work, then the teaching archive.
Idea: a warm paper archive for returning to precise LSAT teaching.
Live thing: search/filter real teaching notes and open one with preserved return context.
Layout: page heading / ruled destination navigation / paper archive / chronological rows.
Top three problems:
1. Mixed control language. Native popup in the supplied image breaks the material treatment; toolbar controls also use competing borders/underlines.
2. Mobile vertical cost. In the mixed-type fixture, the first note begins around y585 on an 844px viewport. Compress chrome and filter layout without reducing touch targets.
3. Unbalanced hierarchy. Desktop h1 is 43px and the archive shadow is too assertive for a resting plane. Make the title more compact and express depth through coherent tones and quieter shadow.

Inspector: one FAIL, heavy-shadow; three WARN, micro-label, dev-server and app-title-size. Lint: zero FAIL, two shadow warnings. These are baseline findings, not a pass. Existing warm palette and two role-specific font families are deliberate product constraints and take precedence over generic house preferences.

## Functional contracts and final checks

Preserve URL whitelist and q/filter/type/shown return state; no empty Radix item value; preserve account ownership, accurate unread counts, read-on-open behavior, search across complete safe bodies, draft recovery and conflict guards. Do not alter production read state during visual review.

After approval: implement locally; verify keyboard arrows/typeahead/Enter/Escape and focus return; test popup collision/scroll, narrow widths, 200 percent text zoom, long labels, dark/forced colours and reduced motion; run relevant regression checks and production build. Inspect and open production-rendered desktop/tablet/phone screenshots and state variants; critique and fix the weakest three issues for up to three rounds. No commit, push or publish.
