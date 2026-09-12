---
type: research
subject: Site Teardown Calendly Booking Widget
updated: 2026-07-18
aliases: []
---

# Site Teardown: Calendly Booking Widget

**URL:** https://calendly.com/joshua-fisseha01/30min
**Platform:** Client-side React SPA (`<div id="root">` hydrated by hashed bundles)
**Date analyzed:** 2026-07-18
**Scope:** Only the date/time picker widget (the goal is to match its look in LSAT U's `BookSessionPanel`, NOT to clone Calendly).

## Tech Stack (from source)
| Technology | Evidence | Purpose |
|---|---|---|
| React SPA | empty `#root`, `booking-*.js` bundle hydrates it | renders the whole widget client-side |
| Proxima Nova | `font-family` in booking CSS | Calendly's brand typeface |
| Custom CSS design tokens | `--coreColorBlue700`, `--colorTextSecondary`, etc. | themable design system |

Note: the JS is a single minified/hashed bundle (`booking-022d58336.js`). Decoding it yields obfuscated class names and an internal state machine — NOT useful for matching the look. The visible design comes entirely from the CSS tokens below + the known layout, so the JS decode was intentionally skipped.

## Design System (confirmed from CSS)

### Colors
| Usage | Value |
|---|---|
| Primary blue | `#0069FF` (rgb 0,105,255) |
| Blue hover | `#005FE6` |
| Blue active/selected day | `#004AB3` (coreColorBlue700) |
| Heading text | `#1A1A1A` (neutral900) |
| Secondary/muted text | `rgba(26,26,26,0.6)` |
| Time-slot default text | `#797C7F` |
| Slot hover bg | `#D8D8D8` |
| Panel border | `#ECECEC` |
| Disabled day | neutral300 |

### Typography
| Role | Font | Weight | Size / line-height |
|---|---|---|---|
| Heading ("30 Minute Meeting") | Proxima Nova | 700 | 1.375rem / 1.75rem |
| Body | Proxima Nova | 400 | 0.875rem / 1.4 |

### Calendar day cell
- Min height `1.5rem`; rendered as a **circle** (~40px) in the live UI.
- Border-radius `0.375rem` on the token, but visually **fully rounded** (pill/circle) for day buttons.
- Available day: white bg, light-blue tint fill, blue number.
- Selected day: solid blue (`#004AB3`) fill, white number.
- Today: small dot indicator under the number.
- Disabled/no-availability day: muted grey, not clickable.

### Time-slot button
- Border-radius `0.5rem` (8px).
- Padding `8px 12px` (tall in live UI ~ `12px 0`, full-width).
- Default: white bg, **blue border**, blue bold text.
- Hover: light grey bg (`#D8D8D8`) / subtle.
- Selected: dark/blue fill, white text.
- Stacked in a **vertical scrolling column** on the right.

### Card / panel
- Border `1px solid #ECECEC`, radius `0.5rem`, shadow `0 2px 15px rgba(0,0,0,.1)`.
- Two-column split: left = meeting info + month calendar; right = "Select a Date & Time" / time column.

### Spacing
- Token scale: `8px, 12px, 16px, 24px`. Panels padded `24px`.

## Layout (the widget shape you want)
```
┌──────────────────────────┬───────────────────────────┐
│ Host · "30 Minute Meeting"│ Select a Date & Time      │
│ ⏱ 30 min                  │  ‹  July 2026  ›          │
│ 📹 Web conferencing        │  Su Mo Tu We Th Fr Sa     │
│                           │        (month grid, avail  │
│                           │         days = blue tint)  │
│                           │  Time zone ▾               │
│                           │                            │
│  (after day click →)      │  Monday, July 20           │
│                           │   [ 9:00am ]  ← column of   │
│                           │   [ 9:30am ]     full-width │
│                           │   [10:00am ]     slot btns  │
└──────────────────────────┴───────────────────────────┘
```

## Mapping to LSAT U `BookSessionPanel` (what to change)
Our panel is React + Tailwind + shadcn, dark-theme aware (uses `--primary`, `--border`, `--card`, `--muted-foreground` tokens). The current rebuild already matches the LAYOUT (month day-picker left, time column right). To match Calendly's LOOK, the deltas are:

1. **Day cells → circular, blue-tinted when available.** We already use `rounded-full` + `bg-primary/10` for available, solid `bg-primary` for selected. ✅ Matches Calendly's "tint vs solid" pattern (using our brand primary instead of Calendly blue — keep our brand, don't hardcode `#0069FF`).
2. **Time-slot buttons → full-width, bordered, brand-colored, bold, in a scrolling column.** We already do `w-full rounded-lg border border-primary/40 text-primary` + `max-h-[320px] overflow-y-auto`. ✅
3. **Selected slot → solid fill + a Confirm button** (Calendly shows "Next"; we show "Confirm 9:00am"). ✅
4. **Panel → card with border + subtle shadow, header row split.** We use `rounded-2xl border bg-card shadow-sm` with a bordered header. ✅
5. **Typography:** Calendly uses Proxima Nova; we should NOT import it (licensing + our design system). Use LSAT U's existing type scale. The visual weight (bold headings, muted sub-labels) already matches.

### Verdict
The teardown confirms our rebuilt `BookSessionPanel` already reproduces Calendly's structure and interaction model. The only brand difference is color (their `#0069FF` vs our `--primary` bronze/accent) and font (Proxima Nova vs our stack) — both of which we intentionally keep as LSAT U's own, per the design-system rule (never hardcode hex, reuse tokens). No further code change is required to "match the clean look"; it matches by pattern while staying on-brand.

## Notes
- Do NOT hardcode Calendly's `#0069FF` — LSAT U is a premium editorial design system; use `--primary` tokens (per `lsatu-design-system` memory).
- Proxima Nova is a licensed font; not worth importing to mimic. Our stack reads as premium already.
- The only thing blocking the student from SEEING our version right now is the backend redeploy (the `get_student_booking` VOLATILE fix), not the styling.
