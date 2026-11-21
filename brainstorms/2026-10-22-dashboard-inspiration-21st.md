# LSAT U dashboard: 21st.dev research

Date: 2026-10-22. Research only. No app changes or component installation.

## Actual MCP result

Used the official installed plugin's documented HTTP JSON-RPC transport at `https://21st.dev/api/mcp`, authenticating with the existing `API_KEY_21ST` process environment variable. No credential was printed, stored in this note, or sent to another destination.

- `initialize`: HTTP 200; negotiated protocol `2024-11-05`; server `21st`, version `0.1.1`.
- `tools/list`: HTTP 200; confirmed `search`, `get_inspiration`, `get_component`, and `get_usage` schemas.
- `get_usage`: free tier, hosted AI disabled, zero AI credits, two of two free component-code retrievals available.
- `get_inspiration` for refined neutral teacher/student workspaces: server returned `isError: true`, `21st get_inspiration failed: catalog search failed`.
- `search` for `calendar agenda` and `task list dashboard`: both returned `isError: true`, `21st search failed: catalog search failed`.
- No hosted generation, paid action, code retrieval, install, account change, or permission change attempted. This is an authenticated catalog-service failure, not an authentication failure. Do not claim that MCP returned working component candidates.

## Public catalog metadata fallback

Primary 21st.dev pages were discoverable through web search despite the MCP catalog failure. These are metadata references, not fetched/installed source code or visually inspected previews.

1. **Task List**, Ravi Katiyar. Table-like task rows accepting a title and task array, with staggered list animation. Useful structure for a restrained teacher attention queue. Its listed Framer Motion dependency should not be imported into LSAT U's existing GSAP reveal tree.
   Source: https://mcp.21st.dev/%40ravikatiyar162/components/task-list
2. **Calendar Planner**, Ruixen UI. Monochrome calendar with notes under dates and a two-month arrangement. Useful idea: directly readable schedule context rather than colored decorative dots. A full two-month planner is excessive for Home; prefer an existing-data chronological agenda.
   Source: https://contact_2a72bbaa.21st.dev/%40ruixen.ui/components/calendar-planner
3. **Inbox Calendar**, Ruixen UI. Events arranged chronologically under date headings, expandable details. Best adaptation for Home is a compact date rail and a few real upcoming entries, linking to the existing scheduling destination. Do not add a new event editor or local-only calendar persistence.
   Source: https://preview.21st.dev/%40ruixen.ui/components/inbox-calendar
4. **Fullscreen Calendar**, Ahmed Mayara. Responsive spacious calendar with current-date highlighting. Useful spacing and date emphasis reference, but a full grid would consume too much Home space and compete with the primary teacher/student action.
   Source: https://21st.dev/%40ahmedmayara/components/fullscreen-calendar

## Recommended adaptation

- Use a paper-white working canvas and deep ink, preserving the approved LSAT U tokens. Existing editorial serif can remain in the greeting only; task text, labels, controls and numbers use the established interface sans family. Do not transplant the Taste preset's generic font/palette wholesale.
- Teacher Home should read like an instructor's desk: concise masthead, one dominant attention list, a quieter schedule/utility rail, and direct student/assignment actions. Distinguish unread conversations from items needing a response. Never show student-assigned work to an admin.
- Student Home should prioritize one actual next step, then a readable queue. Avoid duplicating the hero assignment as the first row of an identical list. Give the remaining queue its own clear role or label the full inventory explicitly.
- Prefer ruled rows, typography and negative space over a grid of equally weighted metric cards. Reserve the deep-ink surface for the next useful action, not every region.
- Keep status visible in text, with color as a secondary cue. Use installed Radix icons. No fake analytics, invented activity heatmaps, AI prompts, generated stock portraits, decorative charts, or automatic rearranging lists.
- Motion should be one short coherent entrance using existing GSAP ownership, then quiet updates. Do not re-blur the whole dashboard when counters change. Support reduced motion and stable loading dimensions.
- Agenda and task ideas are conditional on existing real data sources and permission-safe routes. A polished empty or unavailable state is preferable to fabricated events, counts or buttons.

## Limits

No component code was obtained. Public metadata does not establish accessibility, licensing of copied code, production quality, or backend readiness. No visual preview was opened in this subtask. Parent agent owns Pinterest visual research and browser verification of the implementation.
