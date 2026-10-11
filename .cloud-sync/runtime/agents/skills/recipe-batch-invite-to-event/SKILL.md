---
name: recipe-batch-invite-to-event
description: "Add a list of attendees to an existing Google Calendar event and send notifications."
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

Read actual selected event; merge requested guests into existing attendees preserving their fields/status, deduplicate by email, then patch. Do not replace existing guests with the sample array. sendUpdates notifications require invitation/send authorization and readback.

## Workflow

# Add Multiple Attendees to a Calendar Event

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-calendar`

Add a list of attendees to an existing Google Calendar event and send notifications.

## Steps

1. Resolve actual target IDs, requested data, date interval/timezone and existing state. Illustrative names, dates and recipients are not user data.
2. Read actual selected event; merge requested guests into existing attendees preserving their fields/status, deduplicate by email, then patch. Do not replace existing guests with the sample array. sendUpdates notifications require invitation/send authorization and readback.
3. Discover the required method using installed `gws <service> --help` and `gws schema <service>.<resource>.<method>`; build parameters from real returned IDs and requested data. For retries reconcile existing output identity first.
4. Execute only the requested authorized operation. Draft email unless send is authorized. Inspect resulting resource/file and report any missing sections or failed items.

## Relevant endpoint references

- `gws calendar events get --params` (inspect help/schema before invocation)
- `gws calendar events patch --params` (inspect help/schema before invocation)

