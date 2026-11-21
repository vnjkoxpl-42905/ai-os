# Student-home visual references, 2026-10-23

## Evidence and scope

Read the original creative brief in `C:/Users/Joshu/.codex/attachments/614486b3-1ac4-49fb-848c-b0e275f72813/Pasted text.txt`. It calls for coherent artistic identities rather than a checklist of effects. Current steering prefers the existing near-white/ink palette, Lamplight's top rail, and alternatives to exam-day countdowns.

Used Firecrawl search plus Sunsama documentation scrape, web search/open, and real headless Edge captures. Actually inspected `reference-sunsama.png`, `reference-recent.png`, `reference-21st-tabs.png`, and `reference-pinterest.png` in this folder. These are rendered site captures, not authenticated product walkthroughs. No motion smoothness claim is established by these stills.

## Eight concrete patterns worth testing

1. **A top rail with one moving active marker.** Keep LSAT U, six labelled sections, inbox and avatar on one steady baseline. Use a slim underline or small travelling dot, not six pill backgrounds. [21st Tabs](https://preview.21st.dev/@ddoemonn/components/tabs) explicitly provides a sliding indicator and directional transitions. Its public preview was visible; the component source requires a free account. Do not import the boxed tab-panel styling into global navigation. GSAP can implement the principle without component dependency.

2. **Today's study budget in place of an exam countdown.** A compact `35 min planned · 1 of 3 complete` display ties a quiet segmented bar to today's actual work. Sunsama's visible product screenshot places time estimates beside tasks and divides days into clear columns. [Sunsama](https://www.sunsama.com/). Adapt the time-estimate hierarchy, not its busy multicolour scheduling board.

3. **A narrow next-session / preparation module.** Show `Tomorrow, 6:00 pm`, teacher name, and one relevant preparation action. This is a useful right-column anchor with less visual bulk than a flip clock. [Morgen](https://www.morgen.so/) unifies tasks and scheduled events; its planning concepts were read, not directly captured or operated. The LSAT-specific preparation cue is our synthesis.

4. **One task card, a quieter up-next queue.** Maintain one high-contrast continuation surface and visually subordinate remaining work with numbered rows, duration and one divider. Sunsama's screenshot uses discrete task cards with internally grouped subtasks; the valuable principle is grouping by work unit. Avoid making every task equally large or hiding the entire queue in a card stack.

5. **Daily intention rather than a distant deadline.** A small editable line, `Today I am working on…`, can pair with a teacher-selected focus such as `Finding the conclusion`. [Sunsama daily highlights](https://help.sunsama.com/docs/usage-guides/daily-highlights) is listed in its documentation; full page was not opened. This idea is a study adaptation, not a verified exact product control. Keep it secondary to Continue.

6. **Filter chips as section-local tools.** The visually inspected [Recent / former Godly](https://recent.design/) header has a calm row of rounded category filters above content. Adapt to `All work / LR / RC` within the work queue, not as a second global navigation rail. Selected state should share the same ink/surface tokens as the top rail.

7. **Asymmetric editorial composition with deliberate alignment.** Recent's varied-height cards remain harmonious because gutter, radius and column edges repeat. For LSAT U, use one generous task region plus a narrow next-session/message column, then a full-width seven-day strip. Do not import a masonry feed: students need stable locations. Add depth to the dominant surface only.

8. **Quiet status, not a rainbow dashboard.** The inspected [University Dashboard pin](https://www.pinterest.com/pin/107664247337864365/) uses a pale summary panel and small status labels in subordinate cards. Its hierarchy is useful but the design is ordinary; it is not a flagship reference. Borrow subtle status emphasis only. Keep near-white, ink, one muted accent, common type scale and common control heights across all modules.

## What not to take

- No wholesale Pinterest education-dashboard layout: this specific inspected pin is generic and data-heavy.
- No animated shader, 3D ornament or decorative large exam counter merely because component libraries offer one.
- No indiscriminate component mixing. One navigation state style, one card-edge vocabulary, one icon stroke weight and one motion family should govern the page.
- No literal desk, lamp or letter metaphor required. Originality can come from typography, spatial rhythm, task focus and interactions.

## Motion synthesis to prototype

Persistent rail remains still. New content enters by 8–14px with a short opacity reveal, roughly 40–60ms stagger among 3–4 meaningful groups. Swapping the primary task should preserve the card's shell and crossfade/translate its interior. An expanded preparation/message panel can grow from its source row. These numbers are starting hypotheses to inspect in natural playback, not facts copied from source websites.

## Access observations

`https://godly.website` redirects to `https://recent.design/?ref=godly`; direct `https://recent.design/` loaded correctly in Edge. Pinterest's public pin loaded visually while signed out. 21st's public page and preview rendered while signed out; no installation or MCP was necessary. Do not confuse these public references with API/authenticated access.

## Local source records

- Firecrawl search output: `C:/Users/Joshu/dev/ai-os/.firecrawl/dashboard-next-products.json`
- Firecrawl Sunsama navigation scrape: `C:/Users/Joshu/dev/ai-os/.firecrawl/dashboard-next-sunsama.md`
- Screenshots: this folder, `reference-*.png`.
