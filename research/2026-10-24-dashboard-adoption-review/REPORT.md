# What to bring forward from the LSAT U prototypes

Prepared 2026-10-24. Read-only design review, followed by this report and the accompanying comparison gallery. No application, production, wiki or prototype files were changed by this review.

Keep the existing LSAT U navigation and compact Home structure. Bring the strongest visual details and useful interactions into their existing destinations. The prototypes are a collection of ideas to recover, not a competition in which choosing one means discarding the others.

The most coherent combination is the neutral editorial hierarchy of Margin, Refined and Refined Studio; Lumen's quiet calendar and supporting surfaces; Marginalia's contextual notes; Lamplight's clear next action; Carrel's restrained material detail; and Atmosphere's paper landscape used within the existing compact assignment card. Studio's question search and reference console belong in existing Practice / Find a question; recent-practice ideas belong in Review. Library remains the curriculum destination.

## Preserve the structure while adopting the details

The latest brief asks to mine positives across Claude Code and Codex versions. Earlier handoff constraints preserve the existing sidebar, destinations, compact assignment card and Home section placement. This review therefore separates a reusable treatment from the alternative page layout in which it first appeared.

For example, a charcoal card can give Continue clear priority without becoming a full-width landing-page hero. A reference console can improve Find a question within Practice without putting the whole console on Home. A searchable student roster can help the teacher workspace without changing student navigation.

The referenced implementation checkout contains unpublished Home work. It has not been established as a clean production baseline. This report makes adoption recommendations; it does not certify the checkout or the current live interface.

## What each family contributes

| Family or version | Positive to recover | Best destination | Specific treatment to limit |
|---|---|---|---|
| Earliest Dashboard, 2026-10-22 | Compact, practical student and teacher composition; clear everyday work areas | Current Home and teacher structure | Screenshots alone do not establish interactions or backend behavior |
| Dashboard Handoff, 2026-10-22 | Distinct student and teacher responsibilities; original structure as the anchor | Existing role-specific destinations | Do not import a prototype's alternative navigation merely to obtain its visual polish |
| Broadsheet / The Brief | Editorial rules, decisive titles and orderly information hierarchy | Home headings, assignment rows, teacher lists | Avoid large newspaper-like mastheads consuming task space |
| Meridian | Precise, scannable progress presentation | Progress and compact task status | Use real counts; do not infer mastery or improvement from decorative indicators |
| Therefore | One concise reason for the recommended next action | Home resume context, Review next action | Avoid repeated slogans or motivational text replacing an explanation |
| Claude Code v2 Lamplight | Strong contrast around one task and a clear primary action | Compact Home assignment/resume card | Literal lamp or oversized stage is unnecessary |
| Claude Code v2 Carrel | Subtle paper/material depth; organized message anatomy; searchable teacher roster concept | Messages, teacher roster, small card accents | Limit literal desk props, tickets, envelopes and ornamental clutter |
| Claude Code v2 Marginalia | Contextual notes and identifiable underlined links | Task guidance, messages, lessons and Review explanations | Avoid a large quotation column when a short task-linked note works |
| New Directions 01 Lumen | Quiet near-white surfaces, readable note column, rounded selected-day calendar and progress blocks | Home supporting surfaces and calendar | Its original phone calendar wraps 4+3; copy the principle, not that layout automatically |
| New Directions 02 Margin | Strong next-action contrast, serif hierarchy, numbered rows, task-linked teacher note and fine dividers | Home, My Work and instructional headings | Giant saved-place numerals and a broad hero can overwhelm ordinary work |
| New Directions 03 Studio | Slight paper edge, saved-place wording, clear status, discreet task tabs and preparation cue | My Work, resume surfaces and session preparation | Large folio and task swapping must not make Continue ambiguous |
| New Directions 04 Refined | Balanced neutral system; contextual note; practical next-session card; rounded selectable calendar with linked agenda | Home calendar, session preparation, compact resume card | Phone hero remains tall; adapt its details to current card dimensions |
| New Directions 05 Studio | Search, reference lookup, LR/RC selection, saved/recent questions, work-type distinction, useful recent-practice entry and prominent session time | Practice / Find a question, Review, My Work and session details | Do not assume its cobalt/coral/yellow/lavender composition, sculpture or slogan stack must accompany those functions |
| New Directions 06 Refined Studio | Strong neutral synthesis; aligned rows; inset reference console; indexed reference slips; per-question results and a revisit action | Practice / Find a question, Review, Progress summaries and My Work | Large question sculpture and watermark are optional; sample counts are not production data |
| New Directions 07 Atmosphere | Original paper-strata image, charcoal highlights, restrained surface depth and accessible small-screen search | Compact assignment artwork and shared visual polish | Keep dense content opaque and readable; scenery must not compete with labels or actions |
| Motion Studies 01 Scroll / 02 Interface | Bounded transitions, static navigation, selected-tab clarity, draft settings with Apply/Cancel and reduced-motion alternatives | Existing content changes, practice setup, drawers and dialogs | Avoid whole-page motion; verify cancellation, saving and focus behavior separately |
| LexPrep motion refinements | Bounded content-only motion, stable navigation, no repeated heading entrance and reduced-motion safeguards | Existing page content | A still image does not establish animation timing or current runtime behavior |

Standalone Refined saved from 04, and the saved charcoal Studio derived from 03, are snapshots in these lineages. They are useful evidence of the evolution, not independent new design families. Intermediate v2 `_research/backup-pass3-*` sources were inventoried but were not separately visually verified.

## Adopt these first

| Priority | Proposed adoption | Reason | Implementation boundary |
|---|---|---|---|
| 1 | Shared serif heading hierarchy with readable supporting text, consistent spacing and aligned rows/arrows | Improves the existing interface across destinations without moving it | Visual work; inspect desktop and phone in the actual host wrapper |
| 1 | Compact charcoal resume card with one clear Continue action, exact saved place and a task-specific note | Combines Lamplight, Margin and Refined's clearest hierarchy | Preserve actual resume semantics and existing task identity |
| 1 | Calendar selected state, obvious focus/hover, day-linked agenda and readable event markers | Makes the existing calendar easier to use | Bind only to real schedule data and existing routes |
| 1 | Cleaner message anatomy and tighter spacing | Recovers Carrel and Lumen's personal support without duplicating teacher content | Preserve inbox state, identity and account scoping |
| 2 | Restrained paper landscape within the current assignment card | Recovers Atmosphere's depth without replacing Home composition | Check actual crop, contrast, load cost and reduced motion |
| 2 | Clear next-session time and a short preparation question | Recovers practical session support from 03, 04 and 05 | Browser-local prototype notes do not establish cross-device/account persistence |
| 2 | Reference lookup, LR/RC controls and saved/recent questions in existing Practice / Find a question | Reduces retrieval steps | Requires existing question-bank and saved-question contracts; no sample bank substitution |
| 2 | Review rows with exact counts, dated attempts, answer strips and a direct revisit action | Turns history into a useful next step | Requires accurate attempt/question linkage and accessible text equivalents |
| 2 | Searchable teacher roster using the existing teacher architecture | Recovers a useful Carrel concept | Requires real authorized student scope and existing teacher data |
| 3 | Limited material accents, work-type icons and short content transitions | Adds distinction after hierarchy and behavior are sound | Adopt selectively; no decorative quota, perpetual idle animation or new navigation |

Priority indicates recommendation, not approval to modify or publish the app. The next concrete design should be a local before/after adaptation of these details within the current production structure.

## Put the ideas in the destinations they serve

**Home:** compact next assignment, clear Continue, task-linked teacher note, short assignment rows, calendar/agenda, session time and tidy messages. Keep the current section order and navigation.

**My Work:** LR/RC filtering, obvious work type, aligned metadata, honest due/planned distinctions and clear completion/resume state. Selecting another assignment must not overwrite the task that Continue resumes.

**Practice / Find a question:** clear drill entry points, reference lookup, LR/RC controls, saved/recent questions and keyboard search. Practice owns drills, saved drill sets and exams; the existing Find a question action opens its finder within Practice. Preserve that route and return behavior. The sample guided negation and paragraph-recall workflows are design demonstrations, not proof of new production drills.

**Review:** dated sets, correct/total counts, answer-level indicators and a direct return to the question. A small sample of attempts does not justify a trend or mastery claim.

**Progress:** actual counts and grounded next steps. Meridian's precision and 06's compact result vocabulary are more valuable than arbitrary dashboard metrics.

**Library:** written lessons and exercises, with existing Lessons, Activities and Bootcamps tabs. Adopt contextual lesson notes, readable instructional typography and useful links here. The prototype section labelled Question library does not establish this application's Library route as a question bank.

**Teacher:** retain the existing role architecture. Carrel's searchable roster and message anatomy are useful candidates. The seven New Directions variants are student prototypes and do not validate teacher workflows.

The route mapping above was verified against checkout source, not the live site: [Library curriculum destinations](C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/src/lib/destinationAccess.ts:75), [Find a question action and return route](C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/src/components/classroom/shell/ClassroomLayout.tsx:350), and [Practice drill/set/exam routes](C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/src/App.tsx:637). In particular, Library uses `/library/lessons`, `/library/activities` and `/library/bootcamps`; Find a question opens `/practice/drills?finder=open&finderReturnTo=...`.

## Earlier passes contain useful improvements too

In 05 Studio, pass 1 gives the session card a huge date and a general slogan. Later passes foreground **7:15 PM and the session duration**, which is more useful to a returning student. The progress line becomes a countable strip. The preparation action becomes visually secondary to Continue. The sculpture becomes smoother, but its artistic improvement does not require adopting it into the compact Home card.

In 07 Atmosphere, the final pass removes a decorative circle from the session card. The useful principle is directional light and subtle texture rather than an unrelated object. Readme records describe enlarged metadata/touch targets, reachable phone search and a runtime reduced-motion repair. Those are historical implementation claims, not fresh runtime findings from this review.

The 06 review record documents a previously corrupted resumed-task state when selecting another assignment, transform conflicts in the sculpture, tablet overlap, wrong navigation targets and inconsistent dates. Its README records fixes. Preserve these behavioral lessons whether or not the sculpture is retained.

## Visual polish and new functionality need different evidence

Typography, spacing, row alignment, dividers, surface depth, restrained artwork and calendar state styling are visual adaptations. They still require rendered inspection in the actual Classroom/Home wrapper because host colors, dimensions and responsive behavior affect the result.

Search, bookmarks, question lookup, saved session preparation, roster filtering and review actions are functionality. They require real account/data integration and failure handling. A button with a working prototype dialog does not prove its production destination or persistence.

All New Directions samples use synthetic schedules/results and original demonstration questions. They are not connected to the live LSAT U question bank. Local storage in a prototype does not establish signed-in persistence, cross-device storage, authorization or recovery after a failed write. Counts and labels must come from the existing production model.

The motion implementation should keep navigation stable, animate only the content that changes, settle promptly and provide a static reduced-motion equivalent. Draft configuration should apply only on Apply and discard on Cancel. Those contracts require runtime tests when implemented; a screenshot cannot prove them.

## Sources and review coverage

Absolute source roots:

- [Earliest dashboard](C:/Users/Joshu/Downloads/LSAT-U-Dashboard-2026-10-22/)
- [Role handoff](C:/Users/Joshu/Downloads/LSAT-U-Dashboard-Handoff-2026-10-22/)
- [Three Directions](C:/Users/Joshu/Downloads/LSAT-U-Dashboard-Three-Directions/index.html)
- [Claude Code v2 directions](C:/Users/Joshu/Downloads/LSAT-U-Dashboard-Three-Directions-v2/index.html)
- [New Directions comparison](C:/Users/Joshu/Downloads/LSAT-U-Dashboard-New-Directions/index.html)
- [New Directions historical review](C:/Users/Joshu/Downloads/LSAT-U-Dashboard-New-Directions/REVIEW.md)
- [Motion Studies](C:/Users/Joshu/Downloads/LSAT-U-Motion-Studies-2026-10-22/)
- [LexPrep motion work](C:/Users/Joshu/Downloads/LSAT-U-LexPrep-Motion-2026-10-22/)
- [Shared design router](C:/Users/Joshu/dev/ai-os/design/README.md)

The parent review covered earlier families, saved snapshots and motion studies; its findings are synthesized above. A local Claude log ties an artifact family to the work by its naming, but exact authorship of every version is unknown. Labels such as Claude Code v2 describe the discovered family; they are not a verified author-by-author attribution.

The parent's earlier images, recorded by exact source path in [inventory.json](C:/Users/Joshu/dev/ai-os/research/2026-10-24-dashboard-adoption-review/inventory.json), were:

- `C:/Users/Joshu/Downloads/LSAT-U-Dashboard-2026-10-22/teacher-before-1440.png`
- `C:/Users/Joshu/Downloads/LSAT-U-Dashboard-Handoff-2026-10-22/student-dashboard.png`
- `C:/Users/Joshu/Downloads/LSAT-U-Dashboard-Handoff-2026-10-22/teacher-dashboard.png`
- `C:/Users/Joshu/Downloads/LSAT-U-Dashboard-Three-Directions/screenshots/broadsheet-student-1440-top.jpg`
- `C:/Users/Joshu/Downloads/LSAT-U-Dashboard-Three-Directions/screenshots/meridian-student-1440-top.jpg`
- `C:/Users/Joshu/Downloads/LSAT-U-Dashboard-Three-Directions/screenshots/therefore-student-1440-top.jpg`
- `C:/Users/Joshu/Downloads/LSAT-U-Dashboard-Three-Directions-v2/screenshots/lamplight-student-1440.png`
- `C:/Users/Joshu/Downloads/LSAT-U-Dashboard-Three-Directions-v2/screenshots/carrel-student-1440.png`
- `C:/Users/Joshu/Downloads/LSAT-U-Dashboard-Three-Directions-v2/screenshots/marginalia-student-1440.png`
- `C:/Users/Joshu/Downloads/LSAT-U-Dashboard-Three-Directions-v2/screenshots/thumbs/carrel-teacher-1440.jpg`
- `C:/Users/Joshu/Downloads/LSAT-U-Motion-Studies-2026-10-22/01-desktop.jpg`
- `C:/Users/Joshu/Downloads/LSAT-U-Motion-Studies-2026-10-22/02-desktop.jpg`
- `C:/Users/Joshu/Downloads/LSAT-U-LexPrep-Motion-2026-10-22/home-desktop.png`

The New Directions reviewer directly read the available README files, 03's design notes, 05's product brief, the comparison review and HTML structure across 01 through 07. That reviewer opened these existing images:

| Version | Images actually opened |
|---|---|
| 01 | `artifacts/student-1440.png` |
| 02 | `artifacts/margin-1440.png` |
| 03 | `studio-1440.png` |
| 04 | `artifacts/refined-1440.png`, `artifacts/refined-390.png` |
| 05 | `artifacts/pass-final-1440.png`, `artifacts/pass-1-hero-1440.png`, `artifacts/pass-2-hero-1440.png`, `artifacts/pass-3-hero-1440.png` |
| 06 | `artifacts/final-desktop.png` |
| 07 | `artifacts/atmosphere-pass-1-1440.png`, `artifacts/atmosphere-pass-2-1440.png`, `artifacts/atmosphere-pass-3-1440.png`, `artifacts/atmosphere-final-phone.png` |

All image paths in this table are relative to the matching version directory under `C:/Users/Joshu/Downloads/LSAT-U-Dashboard-New-Directions/`. This is 14 directly viewed captures for that set. Full-page desktop captures support composition review; they do not replace detailed phone, keyboard or signed-in workflow testing.

07 includes copied historical 06 artifacts. Files without the `atmosphere` prefix cannot automatically be presented as fresh 07 visual evidence. The root comparison index is also incomplete as an inventory because it primarily links the initial three and 04; the directory inventory establishes the later versions.

No fresh runtime, interaction, performance, screen-reader, production walkthrough or live-backend acceptance was performed for this report. Existing verification reports and README assertions remain historical evidence. No commit, push, merge, deployment or Lovable credit use occurred.
