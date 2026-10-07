# Booking Page Responsive Layout: Brainstorm / Discovery Notes
Date: 2026-09-15 · Goal: Define the intended cross-browser booking-page layout before implementation.

## Summary / key decisions

- The booking page currently changes presentation between browsers or viewport sizes.
- Screenshot 1 shows a wide desktop composition with six dates and their slots displayed simultaneously.
- Screenshot 2 shows a month calendar followed by slots only for the selected date.
- Use screenshot 2's selected-date presentation at every screen width, including wide desktop browsers.
- Remove the six-day horizontal schedule rather than switching to it at a desktop breakpoint.
- On desktop, retain the left event-summary sidebar with host, session title, duration, Google Meet, price, divider, and timezone selector.
- The desktop right panel should contain the heading, 12h/24h control, full month calendar, selected-date heading, and that date's full-width time buttons.
- On phones and narrow windows, stack the same event summary and timezone above the calendar, followed by the selected date's time buttons.
- Match the supplied desktop screenshot as the visual source of truth: one selected date uses solid LSAT U burgundy, other bookable dates use a pale burgundy tile, unavailable dates are faded, and only the selected date's times appear below as full-width outlined buttons.
- On first load, automatically select the earliest available date and show its times immediately.

## Q&A log

### Q1 — One layout across every browser width
- Asked: Should screenshot 2's layout be used at every screen size, including wide desktop browsers?
- Captured: “yes exactly.” The month calendar remains visible and only the selected date's time buttons appear beneath it. The six-day horizontal schedule should not appear on desktop.
- Flags: None.

### Q2 — Desktop summary placement
- Asked: Should the event details remain in a left sidebar on desktop, or should everything become one vertical column?
- Captured: Keep the left sidebar on desktop. Joshua supplied a clearer target screenshot showing the sidebar and the month calendar side by side, with only the selected day's times below the calendar.
- Flags: None.

### Q3 — Narrow-screen stacking
- Asked: Should the desktop sidebar content stack above the calendar on phones and narrow browser windows?
- Captured: Yes. Preserve the same information and order in one column: summary, timezone, calendar, then selected-day time buttons.
- Flags: None.

### Q4 — Initial selection and calendar highlighting
- Asked: Should the earliest available date be selected automatically when the page first opens?
- Captured: Joshua identified the latest supplied screenshot as the exact visual target. It shows one selected date in solid burgundy, other available dates in pale burgundy, unavailable dates faded, a selected-date heading, and only that date's time buttons below. Joshua emphasized that no additional elements should be highlighted.
- Flags: Resolved in Q5.

### Q5 — Fresh-load behavior
- Asked: On a fresh page load, should the earliest available date be selected automatically or should the calendar wait for a click?
- Captured: Yes, automatically select the earliest available date and show its times.
- Flags: None.

## Open flags (pending input)

- None.
