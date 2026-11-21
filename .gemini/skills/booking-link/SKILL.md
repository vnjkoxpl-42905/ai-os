---
name: booking-link
description: Use whenever Joshua wants a one-off booking link for LSAT U — "make me a link for Dakota at 7:15 tomorrow", "send her a link to book tonight", "one-off link, $60", "short notice link", "I need a link she can schedule herself with". Mints a single-use URL that sells exactly one session at a price you set, optionally pinned to one exact time, and closes after she books. Also covers listing and revoking existing links.
---

## Current AI OS execution contract

Resolve this repository root from AGENTS.md and the application from its registered sibling project. Read credentials only through the central private .env loader. Legacy home-relative application or secret paths below are examples, not current authorities. Draft/send authority is unchanged.

# One-off booking links

A URL Joshua sends to one person. She opens it, books one session, pays, and
gets the Google Meet invite from the ordinary booking flow. Then the link
closes.

## Authorization

Minting a link is pre-authorized. Joshua asking for a link means make it now —
do not ask permission, ask only for the facts you actually need.

**Never send the link anywhere.** Print it and hand it to Joshua. He decides who
gets it. A link is a bearer credential: whoever holds it can book that slot.

## What you need before running

Only two things are required, and one has a default:

- **Price** in dollars. Required — links always charge, and the standard rate is
  $45 but a given person may pay something else. Ask if it was not said.
- **Who it is for.** Used only for the admin-side note, never in the URL. If
  Joshua did not say, use a short description.

Everything else is optional. Ask for nothing you were not given.

## Running it

From the LSAT U app checkout, `../ai-os-projects/lsatu` relative to the AI OS root:

```bash
npm run booking:link -- --for "Dakota" --price 45 --at "2026-09-10 19:15"
```

Times in `--at` are wall-clock in Joshua's booking timezone (`America/Toronto`),
format `YYYY-MM-DD HH:mm`, 24-hour. Convert "7:15pm tomorrow" yourself — resolve
relative dates against today before running, and never pass a relative word
through.

It prints the URL, the price, the time, and how many times the link can sell.
Give Joshua the URL exactly as printed.

### The flags

| Flag | Default | What it does |
|---|---|---|
| `--for` | — | Who the link is for. Note only, never in the URL. |
| `--price` | — | Dollars. Required. |
| `--at` | none | Pin one exact time. See below. |
| `--minutes` | 70 | Session length. |
| `--notice` | 1440, or 0 with `--at` | Minimum notice in minutes. `0` means "bookable right now". |
| `--window` | 6 | How many business days ahead the picker reaches. |
| `--label` | "LSAT Session" | The title she sees on the page. |
| `--note` | auto | Admin reminder of who and why. |

### Pinned versus picker

**`--at` pins one time.** She sees only that time and confirms it. The minimum
notice, the rolling window and the weekly hours are all skipped, because Joshua
choosing the time *is* that decision. This is the right shape for "I have a gap
at 7:15 tonight, let her take it."

**Without `--at` she gets a calendar** of open times, still inside the weekly
hours. Use `--notice 0` for a short-notice link she can book today, and
`--window` to control how far ahead it reaches.

Double-booking is never skipped either way. A pinned time that clashes with
something already on the calendar is refused at mint time — the script deletes
the link and tells you what it hit — and refused again inside the booking
transaction.

## Listing and revoking

```bash
npm run booking:link -- --list
npm run booking:link -- --revoke <slug>
```

`--list` shows every one-off link with its state: `open`, `used`, or `revoked`.
Revoking is immediate and the URL stops resolving.

## Reading the outcome honestly

- **"clashes with something already on your calendar"** — the time is taken. No
  link was created. Tell Joshua what he asked for is not free and offer to pick
  another time; do not silently mint a different one.
- **"would have no open times at all"** — a picker link whose window and weekly
  hours produce nothing. Usually `--window` is too small or the hours are empty.
- **A time in the past** is refused. If Joshua asks for a time that has already
  gone by today, say so rather than rolling it to tomorrow on your own.

## How it works, so you can debug it

A one-off link is a row in `booking_event_types` with a random 10-character slug
and `single_use` set. That is the same table defining the ordinary session and
the consultation, and every layer beneath — the page, the `single-session` edge
function, the SQL slot policy, the claim transaction — is already keyed by event
slug. So the link books through exactly the code a normal session books through.
There is no second booking path to keep in sync.

Single use is enforced by the `enforce_booking_event_shape` trigger under a
per-slug advisory lock, so two people opening the same link at the same moment
cannot both get through. A hold holds the link; letting the checkout expire
releases it; a cancelled or refunded booking stays spent, and a replacement
needs a fresh link.

Relevant files:

- `scripts/booking-link.ts` — the CLI
- `src/pages/OneOffBooking.tsx` and the `/book/x/:slug` route in `src/App.tsx`
- `supabase/migrations/20260908120000_one_off_booking_links.sql`
- `supabase/functions/single-session/index.ts`

## Credentials

`LSATPREP_ADMIN_EMAIL` / `LSATPREP_ADMIN_PASSWORD` from the AI OS root `.env`, which is
git-ignored. This repo's `.env` is tracked in git — never put a credential
there.
