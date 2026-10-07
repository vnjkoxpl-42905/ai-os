# Compile one preserved source into linked knowledge

This is the internal wiki-writing procedure for `ingest`. Read the current
vault's `system/schema/llm-wiki.md` first; its conventions win. Discovery,
SHA-256 duplicate checks, archive copying, and routing belong to the parent
skill and are not repeated here.

1. Read the complete source, inspecting important referenced images separately.
   If it is too large, process a bounded section and record coverage; never claim
   complete ingestion of unread material. Use available format-reading tools.
2. Read `wiki/index.md` and relevant domain indexes, then follow their links.
   Search for existing subject/source pages before creating anything. Do not
   dump the whole raw collection or wiki into context.
3. State the important takeaways and any evidence conflict. Follow the user's
   stated focus. Ask only when a consequential ambiguity remains; an explicit
   instruction to ingest and file authorizes routine completion.
4. Create or update one factual source summary in `wiki/sources/`. Use the
   schema's metadata and an unambiguous link to preserved source bytes, with
   title, origin, hash, capture/publication dates when known, date ingested,
   source type, key claims, limitations, and links to related pages. Unknown
   values remain unknown. Attribute what the source says; do not promote it
   automatically to a verified fact or Joshua's decision.
5. Update the relevant entity, concept, domain, or synthesis pages. Follow the
   schema and keep existing authoritative paths, including student and corpus
   records. New entity/concept pages go to the schema's designated locations.
   Separate source facts from interpretation and recommendations. Cite the
   evidence beside important claims. Keep disagreements explicit with both
   sources linked until Joshua adjudicates them. Respect backend authority for
   current operational state and date any checked snapshot.
6. Link related existing pages in both useful directions. Use unambiguous vault
   wikilinks or relative Markdown links in saved pages and clickable absolute
   Markdown file links in chat.
   Do not create a page for every noun or force 10-15 pages per source. Create
   only distinct, useful subjects and link them from an index or related page.
7. Update `wiki/index.md` for every created or materially changed page, preserving
   existing categories and domain index links. Each entry has a resolvable link
   and a one-line content description. Follow the owning generator for generated
   sections rather than hand-editing them. In ai-os run
   `py system/scripts/wiki-maintenance.py --index` for the generated catalog.
   Update human-maintained domain indexes when needed.
8. Append `## [YYYY-MM-DD] ingest | Source title` to `wiki/log.md` with source
   identity/hash, pages created or updated, gaps, conflicts, and verification.
   Preserve prior entries. Use the user's date/time context.
9. Verify original source hash is unchanged, archived copy matches, referenced
   paths resolve, modified pages appear in the index, and the log entry exists.
   Run `py system/scripts/wiki-maintenance.py --lint` in ai-os for structural
   links/index checks, then review claims semantically. Read back changed pages.
   Report the preserved source and finished pages with
   links, plus any unread coverage, unresolved conflict, or skipped work.

Generated sections require compare-and-swap. Read expected target bytes, prepare
the replacement, and confirm the target still has that hash before writing.
Human-owned content and unrelated concurrent edits must be preserved.
