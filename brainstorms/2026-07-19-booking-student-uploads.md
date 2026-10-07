---
type: brainstorm
subject: Booking student uploads comments Brainstorm / Discovery Notes
updated: 2026-07-19
aliases: []
---

# Booking student uploads + comments: Brainstorm / Discovery Notes

Date: 2026-07-19 · Goal: Design an optional, sleek step where students submit work (sections/PTs/files) and comments/updates, and where it surfaces for Joshua.

## Summary / key decisions

1. **Placement:** optional card ON the slot-confirmation form of /book/:slug (not a separate page or post-booking step). Drag-drop/tap upload zone + one comment box, skippable. Copy in Joshua's voice asks for work AND "any other updates." Confirmation screen shows what was attached.
2. **Destinations (two):** upload lands in the Lovable/Supabase backend storage tied to student + booking (source of truth), and flows into the student's existing ai-os folder (`students/<name>/submissions/`) with the comment saved alongside as a note file.
3. **ai-os sync:** on-demand "pull submissions" command (can also run inside /pickup). No cron/watcher. No Google Drive.
4. **Files:** any file type, up to 5 files per booking. (Defaults pending confirmation: 20MB/file cap, ~2000-char comment.)
5. **Notification:** folded into the existing booking notification email — includes comment + file names. No separate per-upload emails.
6. **Admin UI:** paperclip badge on Bookings-tab rows and student-detail session lists, expanding to comment + downloadable files.
7. **Scope:** same upload card for everyone — account-linked and manual/token passes alike; submission ties to pass + booking, not account.

## Q&A log

### Q1 — Placement in the flow

- Asked: Where does the upload/comment step live? (booking-time step vs standalone page vs both)
- Captured: **Option 1 — booking-time step only.** Attached to that specific booking. No standalone add-more surface.

### Q2 — Where submissions surface for Joshua

- Asked: Admin surfacing — inline in Booking workspace vs Inbox vs separate tab
- Captured: Joshua wants copies in: (1) a folder, (2) his ai-os brain, (3) the LSAT U database for the student. Emphasis on copies landing where he works.

### Q3 — Pipeline / the "folder"

- Asked: Drive vs local ai-os folder; proposed Supabase Storage as source of truth + ai-os sync
- Captured: **No Drive.** Lovable/Supabase backend storage for that student + automatic flow into the student's ai-os folder. Two destinations total.

### Q4 — ai-os sync mechanism

- Asked: pickup-time + on-demand pull vs cron/launchd polling
- Captured: **"Pull submissions" on demand does it** (can run as part of /pickup). No cron. Files land in `students/<name>/submissions/` with the comment as a note file.

### Q5 — File constraints

- Asked: file types / count / size (proposed PDF+images, 5 files, 20MB, 2000-char comment)
- Captured: **Any file type, up to 5 files per booking. That's it.** Size cap unstated — defaulting to 20MB/file and ~2000-char comment unless corrected.

### Q6 — Student-facing UX shape

- Asked: optional card on the slot-confirmation form vs separate post-booking step
- Captured: **Not a separate page.** One optional card on the confirm form; skippable; Joshua's voice; confirmation screen echoes attachments.

### Q7 — Notification

- Asked: none vs fold into existing booking email vs separate ping
- Captured: **Fold into the existing booking notification email** (comment + file names). No separate emails.
- Flags: verify what booking email currently exists and where it's sent from → build phase

### Q8 — Admin UI viewing

- Asked: confirm inline viewing in the Booking workspace
- Captured: **Yes** — paperclip badges in Bookings tab + student detail, expandable.

### Q9 — Who gets the upload card

- Asked: account-linked students only, or manual/token passes too
- Captured: **Same upload card for everyone.** Ties to pass + booking; ai-os filing uses the name on the pass.

## Post-interview build notes (added later on 2026-07-19)

- **Reuse, don't create:** the live DB already has `external_work_uploads` (storage_path, processing_status, source_platform, student_id, uploaded_by) and `message_attachments` — the upload feature extends `external_work_uploads` + adds a booking link column rather than a new table. See wiki/lsatu-backend-map.md.
- **Migration path unblocked:** migrations now apply instantly via Cloud tab → SQL editor (Jay 2 writes SQL, Joshua pastes and runs). No more waiting on Lovable's agent.

## Open flags (pending input)

- Size cap 20MB/file + ~2000-char comment: assumed defaults, confirm or adjust. → Joshua
- Backstop items not discussed (assumed defaults unless Joshua objects): student can remove/replace files up to session start from the confirmation view; submissions kept indefinitely; no student-facing history of past submissions. → Joshua
- Existing booking notification email: locate/verify sender path in edge functions before wiring the fold-in. → build phase
