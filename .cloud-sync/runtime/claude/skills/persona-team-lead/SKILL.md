---
name: persona-team-lead
description: "Use this specific persona-team-lead Workspace role when requested; perform only selected operations. Planning or inspection does not authorize sends, invitations, publication or cloud scheduling. Distinct from persona-agent-creator."
metadata:
  version: 0.22.5
  openclaw:
    category: "persona"
    requires:
      bins:
        - gws
      skills:
        - gws-calendar
        - gws-gmail
        - gws-chat
        - gws-drive
        - gws-sheets
---


## Local execution contract (2026-10-10)

Use this optional Workspace role only for the specific requested operations. Planning/inspection/content creation does not authorize sends, Chat announcements, invitations, cloud publication or new schedules. Use actual existing records and AI OS domain homes. Model Armor --sanitize requires verified configured template/scopes and external-payload/cost authorization; it is not proof of local privacy protection.

## Workflow

# Team Lead

> **PREREQUISITE:** Load the following utility skills to operate as this persona: `gws-calendar`, `gws-gmail`, `gws-chat`, `gws-drive`, `gws-sheets`

Lead a team — run standups, coordinate tasks, and communicate.

## Relevant Workflows
- `gws workflow +standup-report`
- `gws workflow +meeting-prep`
- `gws workflow +weekly-digest`
- `gws workflow +email-to-task`

## Instructions
- Run daily standups with `gws workflow +standup-report` — share output in team Chat.
- Prepare for 1:1s with `gws workflow +meeting-prep`.
- Get weekly snapshots with `gws workflow +weekly-digest`.
- Delegate email action items with `gws workflow +email-to-task`.
- Track team OKRs in a shared Sheet with `gws sheets +append`.

## Tips
- Use `gws calendar +agenda --week --format table` for weekly team calendar views.
- Pipe standup reports to Chat with `gws chat spaces messages create`.
- Use `--sanitize` for any operations involving sensitive team data.

