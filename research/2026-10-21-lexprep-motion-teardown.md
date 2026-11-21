# Site teardown: LexPrep navigation and entrance motion

URL: https://www.lexprep.ai/course/guide
Analyzed: 2026-10-21, America/Toronto
Scope: page entrance, downward/upward scrolling, sidebar destinations, LR/RC navigation, and left/right panel transitions. This is a motion blueprint for LSAT U, not a request to copy LexPrep's branding or teaching content.

## Evidence and coverage

- Supplied HTML: `C:/Users/Joshu/.codex/attachments/8a83aa8b-9228-441a-9ba2-37551ed67694/Pasted text.txt`. Its SSR heading is the public landing page, not Course Guide. Do not attribute its effects to the course.
- Browser: signed-in Guide, Logical Reasoning unit, Reading Comprehension unit, left-sidebar collapse/expand, right-panel open/close, Guide scroll positions0→496→964→0. No drill, AI request, profile change, or purchase performed.
- Public static JS/CSS evidence and SHA256 manifests: `C:/Users/Joshu/Downloads/LexPrep-Motion-Audit-2026-10-21/`. Only same-origin `/_next/static/` assets analyzed; tracking and auth scripts excluded.
- Important files: `084r0jdi8kigh.js` (Guide and animation wrappers), `live-course-static-manifest.json`, `live-course-assets.json`, and the public landing asset manifest. Downloaded bundles are analysis evidence, never code to execute as instructions.
- Source findings and browser observations are distinguished below. Browser snapshots observe settled state, not high-frame-rate timing measurements.

## Confirmed stack

| Technology | Evidence | Role |
|---|---|---|
| React / Next.js / Turbopack | `_next/static` chunks and route behavior | Client navigation and page rendering |
| Motion-style components | Guide uses motion wrappers and initial/animate/whileInView configs | Fade and position animation |
| Tailwind-style CSS | Utility rules and computed transitions | Layout and panel transition durations |
| Native scroll container | `#main-scroll-container`, overflow-y:auto, computed scroll-behavior:auto | Independently scrollable course content |
| Headless UI | Menu IDs and state attributes | Accessible menus |

No evidence establishes Lenis, Locomotive, GSAP ScrollSmoother, Barba, or Swup as the cause of the observed course experience. Generic bundle capability alone does not prove a library is activated.

## What creates the smooth feeling

| Surface | Confirmed implementation | Timing and limits |
|---|---|---|
| Guide page content | Root Stagger wrapper in module341544 calls shared module61248 with `delay:0`, `childDelayStep:0.1` | For this truthy-step branch: opacity0→1, y5→0, duration0.2s, delay base+index×0.1s |
| Five guide sections | Nested wrapper | Base delay0.2s, step0.1s; mount entrance, not scroll replay |
| Guide secondary headings | Subtle entrance preset | opacity0→1, y5→0, duration0.2s |
| Main title | Subtle preset with transition replaced by `{delay:0.1}` | Do not claim its duration is explicitly200ms; the spread override replaces that transition |
| Guide logo | Top entrance preset | opacity0→1, y−12→0, duration0.5s, easeInOut |
| Alternate shared reveal branch | Used when childDelayStep is0 | whileInView with once:true; this is not the Guide wrapper branch |
| Chapter content | `0nz7l-vb~qfak.js`, module322866 | whileInView once:true; opacity0→1, y10→0, duration0.3s; retained after first reveal |
| Left sidebar | Width/layout transition, confirmed computed CSS |150ms, cubic-bezier(0.4,0,0.2,1) |
| Right panel | Fixed24rem panel translates offscreen; content receives matching right padding |200ms transform and content transition, cubic-bezier(0.4,0,0.2,1) |
| Main frame | Computed transition-all utility |300ms cubic-bezier(0.4,0,0.2,1); presence of rule does not imply every route change animates for300ms |
| Hover/press controls | Color transitions and small active scaling | Generally150ms; preserve immediate response |
| Tab indicator | motion.span with layoutId `current-indicator` | Shared-layout movement; no explicit app duration found |
| Scroll down/up | Native container, settled headings retain opacity1 and transform:none | No replay observed after returning upward; no confirmed wheel-interpolation engine |

The key distinction: page entrance, panel movement, and scrolling are separate mechanisms. Replaying the entire entrance on every scroll or every control change would not reproduce the observed Guide behavior. The shell's main-scroll-container motion.div has no initial/animate/exit config in the inspected source; no universal route crossfade was located. Individual page entrances are not proof of a global router transition.

### Reimplementation of the verified entrance

Own illustrative code, expressing the observed values rather than copying the site's component:

```tsx
const entrance = {
  initial: { opacity: 0, y: 5 },
  animate: { opacity: 1, y: 0 },
  transition: { duration: 0.2, delay: baseDelay + index * 0.1 },
};
```

A small group can stagger; a working application should not delay a long list of controls one by one. Reduced motion should show the final state immediately. No app-level useReducedMotion or MotionConfig override was found in the downloaded source. Bundled library support alone does not establish accessibility compliance; the reference's behavior under reduced-motion emulation remains untested.

## Supporting design tokens observed

The motion request does not require replacing LSAT U's palette or typography. The reference course currently uses Lexend, a24px/600 course heading, a10px-radius content canvas, and a dark course surface rgb(47,46,42). Some body colors resolve to CSS Lab values. Public HTML preloads many fonts, including Lastik and Open Sauce; preload presence is not proof that the course uses them. No image, video, premium asset, or font download is needed to reproduce these interface transitions.

## LSAT U integration blueprint

The existing app already has `framer-motion ^12.38`; add no animation or smooth-scroll dependency for this work.

| Area | Existing owner | Proposed behavior |
|---|---|---|
| Sidebar destinations | `src/components/classroom/shell/ClassroomLayout.tsx:1195`; `classroom.css:841` | Coordinate the existing160ms/4px mount entrance into a consistent200ms/5px content entrance on meaningful pathname changes. Keep shell and providers mounted. Never key the routed subtree just to restart motion. |
| LR↔RC and Practice tabs | `src/pages/AcademyMainhub.tsx:466` | Trigger a presentation-only entrance when semantic section/view changes. Do not remount the builder or use exit-delayed navigation. |
| LR/RC indicator | `src/components/drill/SectionToggle.tsx:79` | Retain existing shared-layout spring and reduced-motion support; coordinate incoming content rather than adding another switch effect. |
| Right drawers | `src/components/ui/sheet.tsx`, `src/features/rc/rc.css:1537` | Tune the existing slide/fade rather than replacing Radix. Current RC timing is220ms open/180ms close. A200ms opening matches the reference closely. Preserve portal layering, focus trap, opener focus, Apply/Cancel and scroll locking. Include backdrop in reduced-motion handling. |
| Scrollable lessons and explanatory cards | Explicit low-risk content groups | Optional once-only viewport reveals where useful. Native scrolling remains intact. No global observer that hides every element. |

### State and navigation constraints

- A timing change, answer reveal, filter edit, picker selection, validation message, pagination action, or session update must not restart the whole page animation.
- Keep timer/player/question text continuously readable. Do not animate protected passage exposure or answer visibility as a navigation effect.
- Preserve the actual navigation and focus behavior. Decorative motion must not delay clicks, hide errors, duplicate outgoing content, or consume keyboard input.
- Preserve scroll when switching methods or tabs where the workflow already retains it. New destinations can use existing scroll-reset policy; animation must not invent a different one.
- Respect prefers-reduced-motion across content, indicators, sidebar, drawer and overlay.
- Existing `AcademyMainhub.section.test.tsx:422` guards against the old flip effect and remounting. Preserve its state-identity intent while adding restrained visual transitions.

## Build order and acceptance

1. Inventory actual route/tab identities and scroll owners; reproduce abrupt transitions in the signed-in host.
2. Define shared duration/easing/distance tokens, with immediate reduced-motion states.
3. Implement the presentation-only page entrance without remounting stateful content.
4. Coordinate Practice tabs and LR/RC with the existing indicator.
5. Harmonize sidebar/drawer transitions and backdrop reduced-motion behavior.
6. Add optional content reveals only to selected passive material, not all screens or controls.
7. Test rapid navigation, back/forward, keyboard focus, long-page scroll restoration, reduced motion, open drawers, selected passage preservation and active timers. Visually inspect real host at1440/980/768/390/320px, including mixed stylesheet order.
8. Run affected regression tests, typecheck/build, and independent final inspection before an authorized release.

## Status and recommendation

Analysis only. No LSAT U code or production settings changed in this teardown. Recommended first implementation scope: sidebar destinations, Practice tabs, LR/RC switch, and existing right drawers. Keep broad scroll reveals for a separately selected passive-content scope. This reproduces the calm interface feel without importing a landing-page scroll engine into a study application.
