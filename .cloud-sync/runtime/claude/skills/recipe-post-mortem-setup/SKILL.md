---
name: recipe-post-mortem-setup
description: "Create a Google Docs post-mortem, schedule a Google Calendar review, and notify via Chat."
metadata:
  version: 0.22.5
  openclaw:
    category: "recipe"
    domain: "engineering"
    requires:
      bins:
        - gws
      skills:
        - gws-docs
        - gws-calendar
        - gws-chat
---


## Local execution contract (2026-10-10)

Create with gws docs documents create using title JSON, consume returned documentId, then gws docs +write --document ID --text TEXT. Do not use unsupported +write --title/--body. Use actual incident facts and draft-only announcements.

## Workflow

# Set Up Post-Mortem

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-docs`, `gws-calendar`, `gws-chat`

Create a Google Docs post-mortem, schedule a Google Calendar review, and notify via Chat.

## Steps

1. Resolve actual target IDs, requested data, date interval/timezone and existing state. Illustrative names, dates and recipients are not user data.
2. Create with gws docs documents create using title JSON, consume returned documentId, then gws docs +write --document ID --text TEXT. Do not use unsupported +write --title/--body. Use actual incident facts and draft-only announcements.
3. Discover the required method using installed `gws <service> --help` and `gws schema <service>.<resource>.<method>`; build parameters from real returned IDs and requested data. For retries reconcile existing output identity first.
4. Execute only the requested authorized operation. Draft email unless send is authorized. Inspect resulting resource/file and report any missing sections or failed items.

## Relevant endpoint references

- `gws calendar` (inspect help/schema before invocation)
- `gws chat` (inspect help/schema before invocation)
- `gws docs` (inspect help/schema before invocation)
- `gws docs documents create using title` (inspect help/schema before invocation)


Write helper: `gws docs +write --document ACTUAL_DOCUMENT_ID --text ACTUAL_TEXT`. Create titles through `gws docs documents create`, not +write --title/--body.
