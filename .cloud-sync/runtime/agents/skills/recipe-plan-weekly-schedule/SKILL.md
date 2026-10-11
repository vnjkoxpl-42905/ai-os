---
name: recipe-plan-weekly-schedule
description: "Review your Google Calendar week, identify gaps, and add events to fill them."
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

Use one actual requested/current date interval and timezone consistently for freebusy and every proposed event. Plan-only is read-only. Calendar insertion requires requested booking scope and existing-event reconciliation; illustrative dates are not current data.

## Workflow

# Plan Your Weekly Google Calendar Schedule

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-calendar`

Review your Google Calendar week, identify gaps, and add events to fill them.

## Steps

1. Resolve actual target IDs, requested data, date interval/timezone and existing state. Illustrative names, dates and recipients are not user data.
2. Use one actual requested/current date interval and timezone consistently for freebusy and every proposed event. Plan-only is read-only. Calendar insertion requires requested booking scope and existing-event reconciliation; illustrative dates are not current data.
3. Discover the required method using installed `gws <service> --help` and `gws schema <service>.<resource>.<method>`; build parameters from real returned IDs and requested data. For retries reconcile existing output identity first.
4. Execute only the requested authorized operation. Draft email unless send is authorized. Inspect resulting resource/file and report any missing sections or failed items.

## Relevant endpoint references

- `gws calendar` (inspect help/schema before invocation)
- `gws calendar freebusy query --json` (inspect help/schema before invocation)

