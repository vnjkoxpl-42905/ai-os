# Combined local LSAT U preview

User authorization: On 2026-10-24 Joshua asked to build a local version combining the best parts identified in the adoption review. Earlier decisions retain the current sidebar and separate Home, My Work, Practice, Review, Progress and Library. No deployment authorized.

Scene: a coached student checks their next assignment in an ordinary daylight study room, then returns for a longer reading block. Paper light surfaces, charcoal priority, readable black text, semantic restrained accents.

Primary action: continue the actual selected resumed task, independently of browsing another assignment.

Visual contract: current supplied compact Home screenshot is the layout anchor; Refined supplies Newsreader/Manrope hierarchy and aligned rows; Lamplight supplies one-action contrast; Marginalia supplies short task-linked notes; Carrel supplies restrained material edges and message anatomy; 07 supplies a quiet landscape crop inside the compact card. No large hero, quote column, top nav replacement, full lookup/results panels on Home or test countdown.

Scope: a self-contained interactive local HTML/CSS/JS prototype. Student first, with a clearly labelled teacher preview for searchable students. Home, My Work, Practice/finder, Review, Progress and Library each have their own hash route. Synthetic fixtures, local-only storage with honest errors, no network writes and no production account connection. Library stays lessons/activities/bootcamps; question lookup stays Practice.

Flows: sidebar/mobile navigation; assignment preview versus preserved resume identity; LR/RC work filters; calendar selection with agenda; messages mark-read and reply drafts; next-session preparation note save/cancel; keyboard question search, supported/unsupported references, bookmarks and recents; sample answer feedback and revisit; teacher student lookup; empty/error states where relevant. No outbound sending or destructive reset.

Reference files: adoption report in ai-os/research/2026-10-24-dashboard-adoption-review/REPORT.md; supplied live-layout screenshot; 02/04/06/07 studies; local source route mapping recorded in report. PRODUCT.md and DESIGN.md copied from reference checkout only for product context, with later scoped user brief taking precedence over older aesthetic declarations.

Image probe/mock decision: skip new generation because the user has selected an established visual family and fixed layout after reviewing the existing rendered references. Existing generated 07 landscape supplies the selected image asset. Implementation adapts approved details rather than exploring a new direction.

Key states: default, filtered empty, unknown reference, bookmarked/unbookmarked, saved/unsaved note, unavailable local storage, selected calendar day, read/unread messages, role-specific navigation. Respect reduced motion at runtime and first-frame content visibility. Native dialogs trap focus and restore triggers.

Acceptance: actual rendered narrow/mobile/mid/wide views, readable component captures, keyboard/focus, local persistence/failure, menu and route behavior, natural/reduced motion checked separately. No production integration or live verification claim.
