---
name: pull-submissions
description: Pull booking-time student submissions (files + comments) from the LSAT U backend into students/<name>/submissions/. Use when Joshua says "pull submissions", "get the booking uploads", "sync student submissions", or as part of /pickup. On-demand only — no cron, no watcher.
---


## Local execution contract (2026-10-10)

Resolve actual skills/claude or skills/codex helper and sibling app root. Credentials come from central project .env/current approved auth, never exposed. Preserve source identity, deduplicate repeated collection and verify resulting physical artifacts.

## Workflow

# Pull Submissions

When a student books a session through their `/book/<slug>` link, the confirm step lets them optionally attach work (any file, up to 5) and leave a comment. Those land in the LSAT U backend (Supabase storage + `external_work_uploads`, comment on `booking_pass_redemptions.student_note`) and are surfaced in the Bookings admin tab and the booking confirmation email to Joshua.

This skill is the **on-demand pull** that mirrors those submissions into the ai-os brain, so a student's work lives alongside their transcripts.

## What it does

1. Logs in with the admin creds in `~/ai-os/.env` (`LSATPREP_ADMIN_*`) against GoTrue, exactly as the admin UI authenticates.
2. Calls `booking-pass-admin` → `list_bookings`, keeps every booking that has a note or attached files.
3. For each new one, downloads the files (via short-lived signed URLs from `get_booking_uploads`) and writes the comment, into `students/<name>/submissions/`.
4. Records each pulled redemption in a per-student `.pulled.json` manifest so re-running only fetches what's new (idempotent).

## Run it

```bash
bash ~/ai-os/skills/claude/pull-submissions/pull-submissions.sh            # pull everything new
bash ~/ai-os/skills/claude/pull-submissions/pull-submissions.sh --dry-run  # list only, write nothing
```

Requires `curl` and `jq`. Reads `VITE_SUPABASE_URL` / `VITE_SUPABASE_PUBLISHABLE_KEY` from `../ai-os-projects/lsatu/.env` and the admin creds from the root `.env` (both sourced with absolute paths — cwd is unreliable).

## Output layout

```
students/<name>/submissions/
  .pulled.json                       # manifest of redemption ids already pulled
  2026-07-19_a1b2c3d4_note.md        # the student's comment (if any)
  2026-07-19_a1b2c3d4_PT155.pdf      # each attached file, prefixed date_redemption
```

Student name → folder slug is derived from the pass name (lowercased, hyphenated). If the folder doesn't exist yet it's created; reconcile a new folder against `students/README.md` naming if the student already has a record under a different slug.

## Notes

- On-demand by design. Do not add a cron or launchd watcher — Joshua decided the pull is manual (can run inside `/pickup`).
- The backend is the source of truth; this is a mirror. Never delete backend rows from here.
- Files download through 10-minute signed URLs; if a download 403s, just re-run (a fresh URL is minted each call).
