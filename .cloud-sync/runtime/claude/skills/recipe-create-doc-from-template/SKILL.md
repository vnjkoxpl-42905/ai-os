---
name: recipe-create-doc-from-template
description: "Copy a Google Docs template, fill in content, and share with collaborators."
metadata:
  version: 0.22.5
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins:
        - gws
      skills:
        - gws-drive
        - gws-docs
---


## Local execution contract (2026-10-10)

Use returned copy document ID and gws docs +write --document, not --document. Preserve template source and existing formatting; apply actual replacements using supported batchUpdate where appropriate and read back.

## Workflow

# Create a Google Doc from a Template

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`, `gws-docs`

Copy a Google Docs template, fill in content, and share with collaborators.

## Steps

1. Resolve actual target IDs, requested data, date interval/timezone and existing state. Illustrative names, dates and recipients are not user data.
2. Use returned copy document ID and gws docs +write --document, not --document-id. Preserve template source and existing formatting; apply actual replacements using supported batchUpdate where appropriate and read back.
3. Discover the required method using installed `gws <service> --help` and `gws schema <service>.<resource>.<method>`; build parameters from real returned IDs and requested data. For retries reconcile existing output identity first.
4. Execute only the requested authorized operation. Draft email unless send is authorized. Inspect resulting resource/file and report any missing sections or failed items.

## Relevant endpoint references

- `gws docs` (inspect help/schema before invocation)
- `gws drive files copy --params` (inspect help/schema before invocation)
- `gws drive permissions create --params` (inspect help/schema before invocation)


Write helper: `gws docs +write --document ACTUAL_DOCUMENT_ID --text ACTUAL_TEXT`. Create titles through `gws docs documents create`, not +write --title/--body.
