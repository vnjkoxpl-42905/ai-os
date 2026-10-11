---
name: recipe-collect-form-responses
description: "Retrieve and review responses from a Google Form."
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
---


## Local execution contract (2026-10-10)

Require actual form ID; gws forms forms list is unavailable. Discover forms.responses.list via installed schema, paginate, map real responses and verify saved rows. Resolve form through supplied ID or actual Drive metadata.

## Workflow

# Check Form Responses

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-forms`

Retrieve and review responses from a Google Form.

## Steps

1. Resolve actual target IDs, requested data, date interval/timezone and existing state. Illustrative names, dates and recipients are not user data.
2. Require actual form ID; gws forms forms list is unavailable. Discover forms.responses.list via installed schema, paginate, map real responses and verify saved rows. Resolve form through supplied ID or actual Drive metadata.
3. Discover the required method using installed `gws <service> --help` and `gws schema <service>.<resource>.<method>`; build parameters from real returned IDs and requested data. For retries reconcile existing output identity first.
4. Execute only the requested authorized operation. Draft email unless send is authorized. Inspect resulting resource/file and report any missing sections or failed items.

## Relevant endpoint references

- `gws forms forms get --params` (inspect help/schema before invocation)
- `gws forms forms responses list` (inspect help/schema before invocation)
- `gws forms forms list is unavailable` (inspect help/schema before invocation)
- `gws forms forms responses list --params` (inspect help/schema before invocation)

