# Margin refinement reference research

Date: 2026-10-24. Scope: public reference research only, no prototype edits or component installs.

## What was actually checked

- Firecrawl: three searches succeeded, student dashboard/planner, 21st activity/calendar patterns, and public Pinterest monochrome dashboard pins. Six search credits reported in saved results. Two scrapes succeeded: 21st activity catalogue and Tutor LMS dashboard article. Pinterest scrape rejected the site as unsupported. No Firecrawl agent job or bulk crawl was needed.
- Tavily: one four-result search succeeded through `tvly`. Earlier claims that its launcher is broken are outdated for this run.
- 21st MCP: authenticated HTTP transport, tools/list and TWO real component searches succeeded. Nine metadata results total. Old catalogue failure is no longer current. No paid code retrieval and no component install were invoked. Saved result JSONs contain only metadata and literal API-key placeholders, not credentials.
- Pinterest MCP: account probe explicitly returned unauthenticated. A fresh headless browser could open the exact requested public pin, but its login modal obstructed part of the preview. Escape/outside click did not dismiss it. This is limited visual coverage, not a signed-in search.
- Visual inspection: opened and read `21st-activity.png`, `21st-card.png`, `pinterest.png`, `pinterest-visible.png`, and `tutorlms-resume.png` with the image viewer. These are genuine browser screenshots captured on live pages. No claims of interaction/motion inspection on third-party references.

## Five useful patterns, ranked

1. **Coach feedback that leads to a concrete next step.** A quiet white panel with avatar, short insight, expandable explanation and one relevant practice link. Not a decorative quote or new chatbot. Activity-card reference gives spacing, divider and avatar treatment. Keep subordinate to charcoal hero.
2. **Next session preparation.** A date/time, topic, a two-item preparation list, and a place to note a question. Useful replacement for the test countdown. Tutor LMS demonstrates separating ongoing work from upcoming live lessons. Do not pretend prototype details are a real booking integration.
3. **Seven-day calendar plus selected-day detail.** Preserve the user-approved rounded strip from Lumen. Selected day uses charcoal; clicking changes one compact line/panel of sessions/work beneath, rather than introducing a second full calendar. The visual strip is already stronger for this page than generic monthly calendar imports.
4. **A restrained All / LR / RC filter over work rows.** Small segmented control, visible selected state, keyboard navigation. Borrow the tab pattern rather than the whole notification centre. Helps students find work without adding competing modules.
5. **Exact-place resume/activity rows.** Show title, what changed, last saved position and one small affordance. Tutor LMS Continue Learning is a direct product reference. Avoid a social feed with five decorative avatars and generic 'completed lesson' filler.

## Concrete references and observed visual takeaways

### Recent Activity Card, Oliver / 7ovr
https://21st.dev/@olewandowski1/components/activity-1
- Confirmed on page: React + Tailwind; MIT licence; registry source `7ovr.com/r/activity-1.json`.
- Screenshot: `21st-card.png`.
- Actual composition: five compact avatar rows, actor/action as primary, small right-aligned relative time, hairline separators, light raised container. Useful for coach feedback or a compact update row.
- Do not copy the developer activity wording, crowded row count, or enclose every homepage section in another generic rounded card.

### Activity Tabs With Unread, Oliver / 7ovr
https://21st.dev/@olewandowski1/components/activity-4
- Actual MCP result id 28490. All/Mentions/Comments tabs, unread badge and dot, timestamps. Framework React/Tailwind inferred from catalogue category; individual licence not independently opened in this run. Do not reuse code until licence/source read.
- Transfer: one focused filter above the work queue. No need for unread badges on LR/RC themselves.

### Notification Center Tabs, Oliver / 7ovr
https://21st.dev/@olewandowski1/components/notifications-3
- Actual MCP result id 28432; includes All/Unread/Mentions and caught-up state. Licence not separately verified here.
- Transfer: quiet empty state and compact update disclosure. Not a full inbox replacement in this refinement.

### Calendar [React-Area], Origin UI
https://21st.dev/@originui/components/calendar-rac
- Actual MCP result id 458. Metadata/preview URL only, no code retrieved and individual licence not independently verified.
- Consider for future keyboard-accessible date picker; not superior to the user-approved seven-day strip for the current homepage.

### Tutor LMS Continue Learning / Upcoming Lessons
https://tutorlms.com/blog/tutor-lms-learner-dashboard-the-most-complete-student-portal
- Primary product article, saved `tutorlms.md`, visual screenshot `tutorlms-resume.png`.
- Continue rows have clear thumbnail/title/progress/Resume, with upcoming lessons as a separate region. Useful information architecture.
- Reject its many summary metric tiles, saturated blue framing and green progress styling. Match accepted near-white and charcoal instead.

### Exact Pinterest pin supplied by user
https://ca.pinterest.com/pin/363736107411612086/
- Title: Free Online Courses Dashboard for Figma, Theme-UI, attributed in page text to Boguslaw Podhalicz.
- Visible behind modal: black vertical rail, white primary workspace, compact Continue card, course list left and analytics right. This supports compact work rows but does not offer a stronger navigation choice than the user's top rail.
- No source file downloaded, no licence inferred, no new login performed. The modal significantly limits confidence in fine details. Do not force a takeaway from an obstructed reference.

## Palette and harmony

Keep accepted near-white #f8f9fb and charcoal #17191d; the exact existing Margin charcoal hero rendering and rounded Lumen strip are primary references, ahead of external templates. Depth from subtle directional hero light, one soft card shadow, fine divider and clearly separated surfaces. No sage, beige, coloured heatmap, new accent rainbow or test countdown. External components should fit this language, not bring their own conflicting corner radii/type scales.

## Avoid adding

- Heatmap/streak widgets, KPI grids and exam countdowns only to make the page look busier.
- A second monthly calendar next to the selected strip.
- Animated background shader behind reading content.
- Multiple equal-weight calls to action in every supporting module.
- Any wholesale component install until stack/licence/source is checked.

Research is inspiration and product reasoning. It is not evidence of learning efficacy or final implementation quality.
