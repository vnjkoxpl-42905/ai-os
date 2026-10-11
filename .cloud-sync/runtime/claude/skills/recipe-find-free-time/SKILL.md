---
name: recipe-find-free-time
description: "Query Google Calendar free/busy status for multiple users to find a meeting slot."
metadata:
  version: 0.22.5
  openclaw:
    category: "recipe"
    domain: "scheduling"
    requires:
      bins:
        - gws
      skills:
        - gws-calendar
---


## Local execution contract (2026-10-10)

Find-only mode returns candidate slots from the requested interval/timezone and freebusy result, with no event creation. Book only when explicitly requested, recheck availability and deduplicate. Do not run the event-insert example for availability inspection.

## Workflow

# Find Free Time Across Calendars

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-calendar`

Query Google Calendar free/busy status for multiple users to find a meeting slot.

## Steps

1. Resolve actual target IDs, requested data, date interval/timezone and existing state. Illustrative names, dates and recipients are not user data.
2. Find-only mode returns candidate slots from the requested interval/timezone and freebusy result, with no event creation. Book only when explicitly requested, recheck availability and deduplicate. Do not run the event-insert example for availability inspection.
3. Discover the required method using installed `gws <service> --help` and `gws schema <service>.<resource>.<method>`; build parameters from real returned IDs and requested data. For retries reconcile existing output identity first.
4. Execute only the requested authorized operation. Draft email unless send is authorized. Inspect resulting resource/file and report any missing sections or failed items.

## Relevant endpoint references

- `gws calendar` (inspect help/schema before invocation)
- `gws calendar freebusy query --json` (inspect help/schema before invocation)

