---
name: recipe-create-events-from-sheet
description: "Read event data from a Google Sheets spreadsheet and create Google Calendar entries for each row."
metadata:
  version: 0.22.5
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins:
        - gws
      skills:
        - gws-sheets
        - gws-calendar
---


## Local execution contract (2026-10-10)

Map actual rows/columns and validate timezone/dates with dry-run first. Persist stable row-to-event identity, reconcile existing events on retry and consume real attendees. Do not turn sample rows into obligations.

## Workflow

# Create Google Calendar Events from a Sheet

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-sheets`, `gws-calendar`

Read event data from a Google Sheets spreadsheet and create Google Calendar entries for each row.

## Steps

1. Resolve actual target IDs, requested data, date interval/timezone and existing state. Illustrative names, dates and recipients are not user data.
2. Map actual rows/columns and validate timezone/dates with dry-run first. Persist stable row-to-event identity, reconcile existing events on retry and consume real attendees. Do not turn sample rows into obligations.
3. Discover the required method using installed `gws <service> --help` and `gws schema <service>.<resource>.<method>`; build parameters from real returned IDs and requested data. For retries reconcile existing output identity first.
4. Execute only the requested authorized operation. Draft email unless send is authorized. Inspect resulting resource/file and report any missing sections or failed items.

## Relevant endpoint references

- `gws calendar` (inspect help/schema before invocation)
- `gws sheets` (inspect help/schema before invocation)

