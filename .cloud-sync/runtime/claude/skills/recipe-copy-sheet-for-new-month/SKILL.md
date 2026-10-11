---
name: recipe-copy-sheet-for-new-month
description: "Duplicate a Google Sheets template tab for a new month of tracking."
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
---


## Local execution contract (2026-10-10)

Use the copyTo response new sheetId for rename, never hardcoded 123. Check existing requested-month tab before copy, retain template, and verify returned tab identity/title.

## Workflow

# Copy a Google Sheet for a New Month

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-sheets`

Duplicate a Google Sheets template tab for a new month of tracking.

## Steps

1. Resolve actual target IDs, requested data, date interval/timezone and existing state. Illustrative names, dates and recipients are not user data.
2. Use the copyTo response new sheetId for rename, never hardcoded 123. Check existing requested-month tab before copy, retain template, and verify returned tab identity/title.
3. Discover the required method using installed `gws <service> --help` and `gws schema <service>.<resource>.<method>`; build parameters from real returned IDs and requested data. For retries reconcile existing output identity first.
4. Execute only the requested authorized operation. Draft email unless send is authorized. Inspect resulting resource/file and report any missing sections or failed items.

## Relevant endpoint references

- `gws sheets spreadsheets batchUpdate --params` (inspect help/schema before invocation)
- `gws sheets spreadsheets get --params` (inspect help/schema before invocation)
- `gws sheets spreadsheets sheets copyTo --params` (inspect help/schema before invocation)

