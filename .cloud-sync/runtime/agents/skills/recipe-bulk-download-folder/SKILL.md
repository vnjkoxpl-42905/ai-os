---
name: recipe-bulk-download-folder
description: "List and download all files from a Google Drive folder."
metadata:
  version: 0.22.5
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      bins:
        - gws
      skills:
        - gws-drive
---


## Local execution contract (2026-10-10)

Page through complete Drive list and recurse requested subfolders with exact relative structure. Handle native Docs export versus binary download, save physical local files and verify sizes/hashes. Report permission/failure gaps rather than claiming all from one list.

## Workflow

# Bulk Download Drive Folder

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`

List and download all files from a Google Drive folder.

## Steps

1. Resolve actual target IDs, requested data, date interval/timezone and existing state. Illustrative names, dates and recipients are not user data.
2. Page through complete Drive list and recurse requested subfolders with exact relative structure. Handle native Docs export versus binary download, save physical local files and verify sizes/hashes. Report permission/failure gaps rather than claiming all from one list.
3. Discover the required method using installed `gws <service> --help` and `gws schema <service>.<resource>.<method>`; build parameters from real returned IDs and requested data. For retries reconcile existing output identity first.
4. Execute only the requested authorized operation. Draft email unless send is authorized. Inspect resulting resource/file and report any missing sections or failed items.

## Relevant endpoint references

- `gws drive files export --params` (inspect help/schema before invocation)
- `gws drive files get --params` (inspect help/schema before invocation)
- `gws drive files list --params` (inspect help/schema before invocation)

