---
name: recipe-send-team-announcement
description: "Send a team announcement via both Gmail and a Google Chat space."
metadata:
  version: 0.22.5
  openclaw:
    category: "recipe"
    domain: "communication"
    requires:
      bins:
        - gws
      skills:
        - gws-gmail
        - gws-chat
---


## Local execution contract (2026-10-10)

Use actual approved recipients/content in each channel. Do not claim an attachment unless provided and attached. Draft unless sends are authorized; verify one copy/channel and record authorized send.

## Workflow

# Announce via Gmail and Google Chat

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`, `gws-chat`

Send a team announcement via both Gmail and a Google Chat space.

## Steps

1. Resolve actual target IDs, requested data, date interval/timezone and existing state. Illustrative names, dates and recipients are not user data.
2. Use actual approved recipients/content in each channel. Do not claim an attachment unless provided and attached. Draft unless sends are authorized; verify one copy/channel and record authorized send.
3. Discover the required method using installed `gws <service> --help` and `gws schema <service>.<resource>.<method>`; build parameters from real returned IDs and requested data. For retries reconcile existing output identity first.
4. Execute only the requested authorized operation. Draft email unless send is authorized. Inspect resulting resource/file and report any missing sections or failed items.

## Relevant endpoint references

- `gws chat` (inspect help/schema before invocation)
- `gws gmail` (inspect help/schema before invocation)

