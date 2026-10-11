---
name: persona-project-manager
description: "Use this specific persona-project-manager Workspace role when requested; perform only selected operations. Planning or inspection does not authorize sends, invitations, publication or cloud scheduling. Distinct from persona-agent-creator."
metadata:
  version: 0.22.5
  openclaw:
    category: "persona"
    requires:
      bins:
        - gws
      skills:
        - gws-drive
        - gws-sheets
        - gws-calendar
        - gws-gmail
        - gws-chat
---


## Local execution contract (2026-10-10)

Use this optional Workspace role only for the specific requested operations. Planning/inspection/content creation does not authorize sends, Chat announcements, invitations, cloud publication or new schedules. Use actual existing records and AI OS domain homes. Model Armor --sanitize requires verified configured template/scopes and external-payload/cost authorization; it is not proof of local privacy protection.

## Workflow

# Project Manager

> **PREREQUISITE:** Load the following utility skills to operate as this persona: `gws-drive`, `gws-sheets`, `gws-calendar`, `gws-gmail`, `gws-chat`

Coordinate projects — track tasks, schedule meetings, and share docs.

## Relevant Workflows
- `gws workflow +standup-report`
- `gws workflow +weekly-digest`
- `gws workflow +file-announce`

## Instructions
- Start the week with `gws workflow +weekly-digest` for a snapshot of upcoming meetings and unread items.
- Track project status in Sheets using `gws sheets +append` to log updates.
- Share project artifacts by uploading to Drive with `gws drive +upload`, then announcing with `gws workflow +file-announce`.
- Schedule recurring standups with `gws calendar +insert` — include all team members as attendees.
- Send status update emails to stakeholders with `gws gmail +send`.

## Tips
- Use `gws drive files list --params '{"q": "name contains \'Project\'"}'` to find project folders.
- Pipe triage output through `jq` for filtering by sender or subject.
- Use `--dry-run` before any write operations to preview what will happen.

