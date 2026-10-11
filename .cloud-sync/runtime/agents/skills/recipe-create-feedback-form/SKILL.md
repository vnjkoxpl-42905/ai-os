---
name: recipe-create-feedback-form
description: "Create a Google Form for feedback and share it via Gmail."
metadata:
  version: 0.22.5
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins:
        - gws
      skills:
        - gws-forms
        - gws-gmail
---


## Local execution contract (2026-10-10)

After title creation, use forms.batchUpdate with requested questions and response settings, then verify actual items and respondent usability. Prepare email as draft; send only authorized recipient/content. A titled empty form is incomplete.

## Workflow

# Create and Share a Google Form

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-forms`, `gws-gmail`

Create a Google Form for feedback and share it via Gmail.

## Steps

1. Resolve actual target IDs, requested data, date interval/timezone and existing state. Illustrative names, dates and recipients are not user data.
2. After title creation, use forms.batchUpdate with requested questions and response settings, then verify actual items and respondent usability. Prepare email as draft; send only authorized recipient/content. A titled empty form is incomplete.
3. Discover the required method using installed `gws <service> --help` and `gws schema <service>.<resource>.<method>`; build parameters from real returned IDs and requested data. For retries reconcile existing output identity first.
4. Execute only the requested authorized operation. Draft email unless send is authorized. Inspect resulting resource/file and report any missing sections or failed items.

## Relevant endpoint references

- `gws forms forms create --json` (inspect help/schema before invocation)
- `gws gmail` (inspect help/schema before invocation)


Use `gws forms forms batchUpdate` to add questions after create; inspect `gws forms forms get` before sharing the respondent URL.
