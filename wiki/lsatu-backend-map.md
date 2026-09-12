---
type: operating-layer
subject: LSAT U backend map (live database structure)
updated: 2026-07-19
aliases: []
---

# LSAT U backend map (live database structure)

Captured 2026-07-19 via the Lovable Cloud SQL editor (source CSV: `query-results-export-2026-07-19_03-00-03.csv` in Joshua's downloads; introspection query in [[log]]). This is the **structural** truth of the live DB — 82 tables, all RLS policies, functions, triggers, cron. Edge-function code lives in the repo (`projects/lsatu/supabase/functions/`). See [[lovable-cloud]] for platform capabilities.

**Data snapshot exists**: full pg_dump (custom format, pg 17.6) exported 2026-07-19 → `raw/lsatu_260719.backup.zip` (26 MB, sha256 `eb9c9e6c…d84d771`). Ingested same day; row counts below updated from the dump. Reading it needs a zstd-capable pg_restore (`/usr/local/opt/postgresql@17/bin/pg_restore`; Homebrew `libpq` build lacks zstd). 840 MB uncompressed, but ~99% of rows are `cron.job_run_details` history (936k rows) — real app data is small. Storage **file bytes are NOT in the dump** (only `storage.objects` metadata: 16 objects, all in `message-attachments`; 4 buckets) — files download separately from Cloud tab → Storage (still deferred).

## Domains and their tables (rows @ capture)

- **Practice engine**: attempts (180), sessions, section_history (2), blind_review_sessions, question_usage (58), question_views (698), daily_stats, settings, flagged_questions (8), question_type_strategies, reasoning_type_guidance, tactical_patterns, concept_library
- **Wrong Answer Journal**: wrong_answer_journal (67), wrong_answer_journal_notes, journal_pages/databases/views (Notion-style)
- **Gamification**: achievements, user_achievements, profiles (21; holds all has_*_access flags + XP/streaks), events, session_replays (320)
- **Bootcamps**: bootcamp_kv (9; generic KV store), intro_lr_attempts, chapter_progress, abstract_* (5 tables: lesson_progress, drill/gauntlet/translator_attempts, final_set), flashcard_reviews
- **Teaching/admin**: guided_drills (108) + guided_drill_assignments, homework_sets/assignments, activities + activity_assignments + activity_item_responses, classroom_items (29), weekly_plans + weekly_plan_items, teaching_assets, ta_interactions/ta_assignments/ai_ta_drafts, smartboard_sessions, student_context, student_sessions, session_ingestions, teacher_todo_dismissals, teacher_message_templates
- **Students**: students (23), students_safe (view-ish safe copy), user_roles, external_work_uploads + student_external_metrics + student_analytics_sources (external-work pipeline ALREADY EXISTS — reuse for the booking upload feature)
- **Messaging**: conversations (16), conversation_participants, messages (75), message_attachments (16), notifications, tutor_conversations (AI tutor), operator_conversations/messages (admin AI operator)
- **Booking**: booking_passes (4), booking_pass_redemptions, booking_availability + config, booking_link_hits (rate limiting), schedule_events (131), gcal_sync_state
- **Email**: email_send_log, email_send_state, suppressed_emails, email_unsubscribe_tokens (queue: enqueue_email / email_queue_dispatch / read_email_batch / move_to_dlq)
- **Content/RAG**: lsatu_content_index (119, pgvector embeddings), lsatu_content_staging, lsat_knowledge_sources, drive_files

## Moving parts

- **Cron**: one job — `gcal-sync-pull-every-5-min` (`*/5 * * * *`).
- **Key RPCs** (beyond pgvector/btree_gist extension noise): redeem_booking_pass_v2, resolve_booking_link_full, regenerate_booking_link, grant_booking_access, is_slot_bookable, booking_buffered_range, get_booking_availability/set_booking_availability, has_role, match_lsatu_content (RAG), retrieve_lsat_knowledge, get_or_create_joshua_conversation, notify_admins_on_signup, email queue functions.
- **Triggers**: updated_at touchers everywhere + immutability guards (homework/activity/TA/notification/profile-admin-fields) — student writes can't tamper with admin-set fields.
- **RLS posture**: every table has RLS on. Pattern: students own-rows only; admins via `has_role(auth.uid(),'admin')`; public read only for knowledge/strategy reference tables; service-role-only for email infrastructure.

## Reuse flags

- `external_work_uploads` (+ storage path, processing_status, source_platform columns) is a ready-made home for the booking-time student uploads feature ([[../brainstorms/2026-07-19-booking-student-uploads|brainstorm]]) — extend rather than new table. **Empty at the 2026-07-19 snapshot (0 rows)**, so schema changes to it carry no data-migration risk.
- `message_attachments` already handles files (storage_path, drive integration) — second reuse candidate.
