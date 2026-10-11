---
name: recipe-create-expense-tracker
description: "Set up a Google Sheets spreadsheet for tracking expenses with headers and initial entries."
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
        - gws-drive
---


## Local execution contract (2026-10-10)

Create requested structure only unless real expense entries are supplied. Do not append illustrative expense data or share with an example manager. Consume returned spreadsheet ID, use actual authorized recipients and verify sheet headers/entries.

## Workflow

# Create a Google Sheets Expense Tracker

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-sheets`, `gws-drive`

Set up a Google Sheets spreadsheet for tracking expenses with headers and initial entries.

## Steps

1. Resolve actual target IDs, requested data, date interval/timezone and existing state. Illustrative names, dates and recipients are not user data.
2. Create requested structure only unless real expense entries are supplied. Do not append illustrative expense data or share with an example manager. Consume returned spreadsheet ID, use actual authorized recipients and verify sheet headers/entries.
3. Discover the required method using installed `gws <service> --help` and `gws schema <service>.<resource>.<method>`; build parameters from real returned IDs and requested data. For retries reconcile existing output identity first.
4. Execute only the requested authorized operation. Draft email unless send is authorized. Inspect resulting resource/file and report any missing sections or failed items.

## Relevant endpoint references

- `gws drive files create --json` (inspect help/schema before invocation)
- `gws drive permissions create --params` (inspect help/schema before invocation)
- `gws sheets` (inspect help/schema before invocation)

