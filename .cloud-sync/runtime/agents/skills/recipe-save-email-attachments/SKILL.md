---
name: recipe-save-email-attachments
description: "Find Gmail messages with attachments and save them to a Google Drive folder."
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
        - gws-drive
---


## Local execution contract (2026-10-10)

Resolve message and attachment IDs, decode Gmail base64url bytes, write a physical task-owned local file and verify size/hash before upload. Use actual filename/MIME, preserve source, and do not claim extraction from metadata alone.

## Workflow

# Save Gmail Attachments to Google Drive

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`, `gws-drive`

Find Gmail messages with attachments and save them to a Google Drive folder.

## Steps

1. Resolve actual target IDs, requested data, date interval/timezone and existing state. Illustrative names, dates and recipients are not user data.
2. Resolve message and attachment IDs, decode Gmail base64url bytes, write a physical task-owned local file and verify size/hash before upload. Use actual filename/MIME, preserve source, and do not claim extraction from metadata alone.
3. Discover the required method using installed `gws <service> --help` and `gws schema <service>.<resource>.<method>`; build parameters from real returned IDs and requested data. For retries reconcile existing output identity first.
4. Execute only the requested authorized operation. Draft email unless send is authorized. Inspect resulting resource/file and report any missing sections or failed items.

## Relevant endpoint references

- `gws drive` (inspect help/schema before invocation)
- `gws gmail users messages attachments get` (inspect help/schema before invocation)
- `gws gmail users messages get --params` (inspect help/schema before invocation)
- `gws gmail users messages list --params` (inspect help/schema before invocation)

