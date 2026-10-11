---
name: recipe-save-email-to-doc
description: "Save a Gmail message body into a Google Doc for archival or reference."
metadata:
  version: 0.22.5
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins:
        - gws
      skills:
        - gws-gmail
        - gws-docs
---


## Local execution contract (2026-10-10)

Use installed gws docs +write --document, not --document-id; decode actual email body, preserve sender/date/message identity, consume created document ID and read back saved content.

## Workflow

# Save a Gmail Message to Google Docs

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`, `gws-docs`

Save a Gmail message body into a Google Doc for archival or reference.

## Steps

1. Resolve actual target IDs, requested data, date interval/timezone and existing state. Illustrative names, dates and recipients are not user data.
2. Use installed gws docs +write --document, not --document-id; decode actual email body, preserve sender/date/message identity, consume created document ID and read back saved content.
3. Discover the required method using installed `gws <service> --help` and `gws schema <service>.<resource>.<method>`; build parameters from real returned IDs and requested data. For retries reconcile existing output identity first.
4. Execute only the requested authorized operation. Draft email unless send is authorized. Inspect resulting resource/file and report any missing sections or failed items.

## Relevant endpoint references

- `gws docs` (inspect help/schema before invocation)
- `gws docs documents create --json` (inspect help/schema before invocation)
- `gws gmail users messages get --params` (inspect help/schema before invocation)
- `gws gmail users messages list --params` (inspect help/schema before invocation)


Write helper: `gws docs +write --document ACTUAL_DOCUMENT_ID --text ACTUAL_TEXT`. Create titles through `gws docs documents create`, not +write --title/--body.
