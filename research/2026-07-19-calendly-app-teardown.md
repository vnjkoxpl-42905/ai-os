---
type: research
subject: Site Teardown Calendly (logged-in app shell)
updated: 2026-07-19
aliases: []
---

# Site Teardown: Calendly (logged-in app shell)

**URL:** calendly.com app (authenticated dashboard, "mf-publisher" micro-frontend)
**Built by:** Calendly in-house
**Platform:** Ruby on Rails host page (csrf `authenticity_token` meta) serving a client-rendered React SPA via a micro-frontend publisher (`assets.calendly.com/mfe/mf-publisher/`)
**Date analyzed:** 2026-07-19

## What this page actually is

The pasted HTML contains **zero UI markup** — the body is `<div id='popup-region'></div><div id='root'></div>`. Everything you see in the Calendly dashboard is rendered client-side by React into `#root` (modals/popovers portal into `#popup-region`). So the teardown value here is not page structure; it is (a) the architecture pattern and (b) the design system, which I pulled from the real CSS bundles (confirmed from source, not inferred).

## Tech Stack (Confirmed from Source)

| Technology | Evidence | Purpose |
|---|---|---|
| React SPA | `react-*.js` bundles, empty `#root` | entire dashboard UI |
| Webpack module federation ("MFE") | `window.WEBPACK_PUBLIC_PATH = '//assets.calendly.com/mfe/mf-publisher/'` | micro-frontend loader; ~190 split chunks (react, ui-libs, moment, vendors, main) |
| Rails host | `csrf-param: authenticity_token` meta | serves the shell + session/CSRF |
| Moment.js | 5 dedicated `moment-*.js` chunks | date/timezone math (legacy choice; they ship the whole tz database) |
| SimpleBar | `app-styles-main` CSS is almost entirely simplebar rules | custom styled scrollbars |
| Optimizely | inline `optimizelyUserData` (user_id, tier, trial, org) | A/B testing / feature flags |
| FullStory | inline snippet, `FS.identify(...)` | session replay analytics |
| Icon sprite chunk | `icons-*.js` (single 1 chunk) | JS-bundled icon set |

Notable: fonts are **embedded as base64 data URIs inside the CSS** (Proxima Nova 400/600/700 + italics, Calendly Sans 400/500) — zero extra font requests, at the cost of a ~1.6MB base stylesheet.

## Design System (extracted from `calendly-ui-base` CSS)

Three-layer token architecture — the main lesson worth stealing:

1. **Core palette:** `--coreColorBlue600`, `--coreColorNeutral050`, … (25→975 numeric scales for blue, neutral, red, green, yellow, teal/aqua, plus grayscale aliases)
2. **Semantic layer:** `--colorSurfaceActionStrong: var(--coreColorBlue600)`, `--colorTextSecondary: var(--coreColorNeutral600)`, `--colorStrokeDestructive: var(--coreColorRed600)` — components never touch raw hex. Multiple values per token = theming (light/dark/inverse) by re-mapping the semantic layer only.
3. **Component layer:** `--button-background-color: var(--colorSurfaceActionStrong, var(--coreColorBlue600))` — every var has a fallback chain.

### Colors (key values)
| Name/Usage | Value |
|---|---|
| Primary action (Calendly blue) | `--coreColorBlue600: #006bff` (`Blue500: #09f` in one theme) |
| Blue tints (hover/selected surfaces) | Blue050 `#edf5ff` · Blue100 `#d5e8fe` · Blue150 `#c1defe` |
| Neutral 0 / 025 / 050 | `#fff` / `#f8f9f9` / `#f5f5f7` (page + card surfaces) |
| Neutral 100–300 (borders → muted text) | `#e4e6e9` · `#d8dce0` · `#c6ccd2` · `#a4aeb7` |
| Success green | Green600 `#14aa51`, Green500 `#00db75` |
| Backgrounds via semantic | `--colorSurfaceSecondary: var(--coreColorNeutral025)` |

### Typography
| Role | Font Family | Notes |
|---|---|---|
| Body / UI | `Proxima Nova, sans-serif` (400/600/700 + italics) | embedded woff/woff2 data URIs |
| Display / eyebrow | `Calendly Sans` (400/500) | brand display face |
| Editorial secondary | `STIX Two Text, Times New Roman, serif` | marketing-style headlines |
| Newer theme | `Geist` | appears as body/label family in the refreshed theme |

Type scale (rem): Body S/M/L = 0.75 / 0.875 / 1 · Headline 3/2/1 = 1.5 / 1.75 / 2.

### Spacing, radius, shadows
- Spacing: `--spacing-{n}x` where 1x = 1rem, in steps 0.0625x → 6x, each with a `-negative` twin.
- Radius: `--border-radius-{0.125…1.5}x`, `-pill: 9999px`, `-circle: 50%`; buttons are `0.5rem` (or pill in the newer theme); there's even a `squircle-multiplier`.
- Shadow: `--shadowModal: 0 32px 96px rgb(25 72 112/8%), 0 0 24px rgb(25 72 112/8%)` — soft, blue-tinted, very Calendly.

### Motion
- Durations: instant 70ms · faster 110ms · fast 150ms · moderate 240ms · slow 400ms · slower 700ms
- Easings: `simple: cubic-bezier(0.2,0,0.38,0.9)` and `expressive: cubic-bezier(0.4,0.14,0.3,1)`, each with enter/exit variants
- Keyframes are small utility fades/slides (`fade-in`, `dropdown-in`, `slide-up`, `shimmer`, `pulse-inner/outer`) — no scroll-driven theatrics in the app; polish comes from consistent duration/easing tokens.

### Responsive approach
App-shell breakpoints are minimal: `max-width: 895px` (nav collapse) plus `max-height: 560px` / `500px` guards. It is a desktop-first dashboard, not a fluid marketing page.

## Effects Breakdown

| Effect | Implementation | Complexity | Cloneable? |
|---|---|---|---|
| Sidebar expand/collapse | width transition using `--base-nav-transition-*` tokens (240ms expressive easing) | Low | Yes |
| Dropdown/popover entrances | `dropdown-in` keyframes into `#popup-region` portal | Low | Yes |
| Loading shimmer | `shimmer` / `rotate-shimmer` keyframes on skeletons | Low | Yes |
| Custom scrollbars | SimpleBar | Low | Yes (`npm i simplebar-react`) |
| Bulk-action bar slide | `--bulk-actions-animation-speed: 120ms` inset transitions | Low | Yes |
| Theming (light/dark/brand) | re-map semantic tokens only | Med | Yes |

## What LSAT U should steal (build plan)

Your `CalendlyBookingCard` already clones the booking surface. The transferable wins are system-level:

1. **Semantic token layer.** You already have bronze/glass tokens in `tailwind.config.ts`; the upgrade is Calendly's discipline — components consume `surface/text/stroke/action` roles, never scale steps directly.
2. **Motion tokens.** Add the 6 durations + 2 easings as Tailwind `transitionDuration`/`transitionTimingFunction` entries and use them everywhere — this is most of Calendly's "polished" feel.
3. **Modal shadow.** Their tinted `shadowModal` reads premium; a bronze-tinted equivalent would suit LSAT U.
4. **Portal region for popups** (`#popup-region` sibling of `#root`) — clean stacking-context management; Radix already does this for you.
5. **Skip:** Moment.js (use date-fns you already have), base64-inline fonts (1.6MB CSS), micro-frontends (single-team overkill).

## Notes
- Proxima Nova and Calendly Sans are licensed fonts — don't reuse; Geist is free (Vercel).
- No GSAP/Lenis/scroll libraries in the app shell — the dashboard's feel is 100% token-driven CSS transitions.
- Confirmed vs inferred: everything in Design System and Effects is confirmed from the fetched CSS; JS behavior details (handlers, configs) were not extractable — ~190 minified chunks with no meaningful reverse-engineering value.
