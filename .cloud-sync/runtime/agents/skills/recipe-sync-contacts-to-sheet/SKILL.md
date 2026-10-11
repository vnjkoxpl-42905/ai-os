---
name: recipe-sync-contacts-to-sheet
description: "Export Google Contacts directory to a Google Sheets spreadsheet."
metadata:
  version: 0.22.5
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins:
        - gws
      skills:
        - gws-people
        - gws-sheets
---


## Local execution contract (2026-10-10)

Use Google People personal connections when the task is Contacts; directory profiles are a separate organizational source. Map actual contact fields and stable resource IDs, reconcile existing rows and verify real sync. Never append placeholder records.

## Workflow

# Export Google Contacts to Sheets

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-people`, `gws-sheets`

Export Google Contacts directory to a Google Sheets spreadsheet.

## Steps

1. Resolve actual target IDs, requested data, date interval/timezone and existing state. Illustrative names, dates and recipients are not user data.
2. Use Google People personal connections when the task is Contacts; directory profiles are a separate organizational source. Map actual contact fields and stable resource IDs, reconcile existing rows and verify real sync. Never append placeholder records.
3. Discover the required method using installed `gws <service> --help` and `gws schema <service>.<resource>.<method>`; build parameters from real returned IDs and requested data. For retries reconcile existing output identity first.
4. Execute only the requested authorized operation. Draft email unless send is authorized. Inspect resulting resource/file and report any missing sections or failed items.

## Relevant endpoint references

- `gws people people listDirectoryPeople --params` (inspect help/schema before invocation)
- `gws sheets` (inspect help/schema before invocation)

