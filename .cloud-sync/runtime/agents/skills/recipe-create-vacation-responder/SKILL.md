---
name: recipe-create-vacation-responder
description: "Enable a Gmail out-of-office auto-reply with a custom message and date range."
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
---


## Local execution contract (2026-10-10)

Set actual requested startTime/endTime epoch bounds and requested audience, preserve prior settings and read back. Disable-when-back is manual unless separately configured scheduling was requested. Do not enable indefinitely from a bounded vacation request.

## Workflow

# Set Up a Gmail Vacation Responder

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`

Enable a Gmail out-of-office auto-reply with a custom message and date range.

## Steps

1. Resolve actual target IDs, requested data, date interval/timezone and existing state. Illustrative names, dates and recipients are not user data.
2. Set actual requested startTime/endTime epoch bounds and requested audience, preserve prior settings and read back. Disable-when-back is manual unless separately configured scheduling was requested. Do not enable indefinitely from a bounded vacation request.
3. Discover the required method using installed `gws <service> --help` and `gws schema <service>.<resource>.<method>`; build parameters from real returned IDs and requested data. For retries reconcile existing output identity first.
4. Execute only the requested authorized operation. Draft email unless send is authorized. Inspect resulting resource/file and report any missing sections or failed items.

## Relevant endpoint references

- `gws gmail users settings getVacation --params` (inspect help/schema before invocation)
- `gws gmail users settings updateVacation --params` (inspect help/schema before invocation)

