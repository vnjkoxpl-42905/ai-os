---
name: recipe-draft-email-from-doc
description: "Read content from a Google Doc and use it as the body of a Gmail message."
metadata:
  version: 0.22.5
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins:
        - gws
      skills:
        - gws-docs
        - gws-gmail
---


## Local execution contract (2026-10-10)

Extract actual document text and save Gmail draft with --draft. Do not send from a draft request. Use actual recipient/subject and verify exactly one draft with correct text; reuse matching draft on retry.

## Workflow

# Draft a Gmail Message from a Google Doc

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-docs`, `gws-gmail`

Read content from a Google Doc and use it as the body of a Gmail message.

## Steps

1. Resolve actual target IDs, requested data, date interval/timezone and existing state. Illustrative names, dates and recipients are not user data.
2. Extract actual document text and save Gmail draft with --draft. Do not send from a draft request. Use actual recipient/subject and verify exactly one draft with correct text; reuse matching draft on retry.
3. Discover the required method using installed `gws <service> --help` and `gws schema <service>.<resource>.<method>`; build parameters from real returned IDs and requested data. For retries reconcile existing output identity first.
4. Execute only the requested authorized operation. Draft email unless send is authorized. Inspect resulting resource/file and report any missing sections or failed items.

## Relevant endpoint references

- `gws docs documents get --params` (inspect help/schema before invocation)
- `gws gmail` (inspect help/schema before invocation)


Draft helper: `gws gmail +send --draft --to ACTUAL_RECIPIENT --subject ACTUAL_SUBJECT --body ACTUAL_DOCUMENT_TEXT`.
