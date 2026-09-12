# LSAT U home dashboard: five prototypes, no limits

This is the first screen a student of LSAT U (lsatprep.study) sees after logging in. I have attached the exact production source, full-page screenshots of the current design in four states, and inspiration images. Read them so you know what exists. Then forget that it has to look anything like this.

I want the best dashboard you can make. Not a refresh, not a cleanup. Something a student opens and feels they are inside a serious, beautiful, expensive piece of software built for them. Take it as far as your taste and your tools will go. You have complete creative freedom over layout, hierarchy, typography, colour, motion, materials, metaphor, and information architecture. Nothing on the current page is sacred.

## Deliver five prototypes

**Prototype 1.** The current design, rebuilt faithfully from the source and screenshots, so we have a baseline on the canvas. Beside it, a blunt critique: what is weak, what is dated, what is merely fine.

**Prototypes 2 to 5.** Four genuinely different answers, not four variations. Each should feel like a different studio made it. Name each direction in one line before you build. At least one should be something I would not have thought to ask for.

For each: desktop in light and dark, a phone version, and the empty state (nothing assigned, no message, nothing booked). Make them interactive wherever it matters: the primary action, opening a piece of work, hover and press states, any motion you propose. I want to feel them, not just look at them.

Use the fixture data in `preview-harness/classroomHomePreview.tsx` so all five show the same student on the same Friday and can be compared honestly.

## The bar

Top-tier, pristine, elite. Judge your own work against the best product design shipping today: Linear, Arc, Things, Vercel, Apple's first-party apps, Stripe's dashboard, Family, Amie, Cron, the Rauno Freiberg and Emil Kowalski school of interaction detail. Principles I care about:

- **Hierarchy you can feel in half a second.** One thing is clearly first. Everything else earns its place.
- **Typography as the design.** Optical sizes, real weights, tight tracking on display, generous measure on body. Tabular numerals wherever a number sits.
- **Materials, not flat rectangles.** Light, depth, grain, glass, paper, shadow that comes from somewhere. Surfaces that feel like they have a physical property.
- **Motion with intent.** Spring physics, staggered entrances, shared-element transitions, hover that anticipates. Never decoration for its own sake; every movement tells the student what just happened or what will.
- **Density that adapts.** Calm when there is little to do, tight and instrument-like when there is a lot.
- **Restraint in colour.** One accent used with discipline beats five used loosely. Dark mode designed, not inverted.
- **Craft at the edges.** Focus rings, empty states, loading, the 320px phone, the 1920px monitor, reduced motion. The details nobody notices until they are wrong.

## Tools and techniques to reach for

You are not limited to static layouts. Claude Design can build code-powered prototypes with shaders, 3D, voice, video, and built-in AI. Use whatever raises the ceiling. Ideas, none mandatory:

- **Shaders and generative backgrounds.** A slow WebGL gradient or noise field that shifts with time of day, or with how much work is due. Ambient, never loud.
- **3D and depth.** A hero that tilts on cursor, cards with real parallax layers, a progress object rendered as a physical thing rather than a bar.
- **Variable fonts.** Weight and optical size animating on hover, on scroll, on state change.
- **Scroll-driven and view transitions.** The page choreographing itself as the student moves through it; the hero morphing into the work it opens.
- **Spring and gesture physics.** Rows that drag, swipe, snap. Pills that squash on press. A week band that scrubs.
- **Data as sculpture.** The next seven days as a horizon line, a ring, a strip of light. Progress as a filling vessel, a stacked deck, a lit path.
- **Sound and haptics.** A single considered tone on completing work. Optional, off by default, but design it.
- **Time and light awareness.** The page knowing it is 11 p.m. and behaving differently than at 8 a.m.
- **Built-in AI.** A one-line "what should I do first?" that answers from the student's own assigned work, rendered as part of the design rather than a chat box.
- **Micro-illustration or iconography** drawn for this product rather than pulled from a library.
- **Adjustment knobs.** Give me sliders on the canvas for density, warmth, and motion intensity on your strongest prototype so I can tune it live.

If a prototype wants data that does not exist yet, draw it anyway and label it "would need: X". I want the idea.

## Context you need, kept short

- The student works one-to-one with a single tutor. The page shows what to pick up now, assigned work, the tutor's latest message, the next session, the week ahead, a "find a question" search, and a "Read, Recall, Colour" card. How you present, group, hide, or reweight those is yours.
- It renders inside a shell with a left navigation rail. Draw the rail in desktop versions so the page is judged in context; you may restyle it to match your direction.
- Copy is plain and adult. No exclamation marks, no emoji, no cheerleading. If you write new words, keep that register.
- Current type is Fraunces, Outfit, JetBrains Mono. Current accent is orange `#ff8906`. Keep, replace, or reinvent.

## When you are done

Rank the five. Say which you would ship, which you would ship if you were braver, and what you would steal from the others to make the winner better. Then tell me what you would build next if I gave you the whole app.

Do not ask clarifying questions before the first pass. Make the calls, note the assumptions, show me five things.

## Attached

- `screenshots/` · current design: light full, light empty, dark full, mobile
- `source/dashboard/` · the exact page (`ClassroomHomeView.tsx` markup, `home.css` tokens and rules, `homeModel.ts` data shape)
- `source/shell/` · the shell and rail
- `source/tokens/` · app-wide tokens and Tailwind config
- `source/preview-harness/` · the fixture behind the screenshots
- `source/TEACHING-VOICE.md` · copy voice
- Inspiration images: mood, not template
- Repo, if useful: GitHub `vnjkoxpl-42905/lsatu-684d89db`, `src/components/classroom/home/`
