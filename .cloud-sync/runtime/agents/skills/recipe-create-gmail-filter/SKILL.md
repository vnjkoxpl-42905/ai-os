---
name: recipe-create-gmail-filter
description: "Create a Gmail filter to automatically label, star, or categorize incoming messages."
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

Apply only requested criteria/actions. Do not remove INBOX for generic labeling/star/category requests; archival must be explicit. Reuse existing labels/filters and read back resulting action/criteria.

## Workflow

# Create a Gmail Filter

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`

Create a Gmail filter to automatically label, star, or categorize incoming messages.

## Steps

1. Resolve actual target IDs, requested data, date interval/timezone and existing state. Illustrative names, dates and recipients are not user data.
2. Apply only requested criteria/actions. Do not remove INBOX for generic labeling/star/category requests; archival must be explicit. Reuse existing labels/filters and read back resulting action/criteria.
3. Discover the required method using installed `gws <service> --help` and `gws schema <service>.<resource>.<method>`; build parameters from real returned IDs and requested data. For retries reconcile existing output identity first.
4. Execute only the requested authorized operation. Draft email unless send is authorized. Inspect resulting resource/file and report any missing sections or failed items.

## Relevant endpoint references

- `gws gmail users labels create --params` (inspect help/schema before invocation)
- `gws gmail users labels list --params` (inspect help/schema before invocation)
- `gws gmail users settings filters create` (inspect help/schema before invocation)
- `gws gmail users settings filters list` (inspect help/schema before invocation)

