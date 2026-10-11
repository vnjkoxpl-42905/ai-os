---
name: recipe-create-presentation
description: "Create a new Google Slides presentation and add initial slides."
metadata:
  version: 0.22.5
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins:
        - gws
      skills:
        - gws-slides
        - gws-drive
---


## Local execution contract (2026-10-10)

Create presentation, then slides.batchUpdate to add requested slides and content; read back actual slide/page IDs and content. Resolve gws-drive for the optional permissions step. Share only with authorized actual collaborators; blank presentation is incomplete.

## Workflow

# Create a Google Slides Presentation

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-slides`

Create a new Google Slides presentation and add initial slides.

## Steps

1. Resolve actual target IDs, requested data, date interval/timezone and existing state. Illustrative names, dates and recipients are not user data.
2. Create presentation, then slides.batchUpdate to add requested slides and content; read back actual slide/page IDs and content. Resolve gws-drive for the optional permissions step. Share only with authorized actual collaborators; blank presentation is incomplete.
3. Discover the required method using installed `gws <service> --help` and `gws schema <service>.<resource>.<method>`; build parameters from real returned IDs and requested data. For retries reconcile existing output identity first.
4. Execute only the requested authorized operation. Draft email unless send is authorized. Inspect resulting resource/file and report any missing sections or failed items.

## Relevant endpoint references

- `gws drive permissions create --params` (inspect help/schema before invocation)
- `gws slides presentations create --json` (inspect help/schema before invocation)


Use `gws slides presentations batchUpdate` to add requested slides/content before optional `gws drive permissions create`.
