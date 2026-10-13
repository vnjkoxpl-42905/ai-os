---
title: Reading Center build spec
date: 2026-10-12
status: ready for build
owner: Joshua
reference: research/2026-10-12-spreeder-feature-inventory.md (the observed Spreeder behaviour this replicates)
target: LSAT U (repo vnjkoxpl-42905/lsatu-684d89db; React + Vite + TS + Tailwind + shadcn, Supabase)
---

# Reading Center: build spec

## 1. Goal

The feature is called the **Reading Center**. Use that name in the nav, page titles, routes
(`/reading-center`), tables (`reading_center_*`) and the feature flag (`reading_center`).

The builder is a Claude model; a stronger Claude model reviews the PR against this spec, section by
section, and against the acceptance checks in section 12. Build so the review is easy: one PR, small
focused commits, and a PR description that maps each spec section to the files that implement it.

Build a speed-reading tool inside LSAT U that replicates every verified Spreeder reader feature, running
on a **predetermined list of passages** Joshua controls. Students pick a passage from the list and read it
in any of five modes, with full control over speed, chunking, appearance, and pauses. Their settings,
progress, bookmarks and reading stats persist.

The passages are general reading passages and real articles, **not LSAT RC passages**. Joshua will
supply a large set of articles that ship pre-loaded, so the library must handle dozens to hundreds of
passages comfortably (search, sorting, a bulk import script; see section 11).

## 2. Ground rules for the builder

- Work on a branch off `main` and open a PR. Never commit to `main`.
- Read the repo's `CLAUDE.md` / `AGENTS.md` first and follow its conventions, tokens and component picks.
- Student data is never destroyed: additive migrations only, nullable or defaulted columns.
- Passage text lives in Postgres (seeded by migration), not in a static JSON file, so Joshua can add
  passages without a code deploy.
- No Lovable-credit-spending actions. Database changes go in a SQL migration file.
- Copy rules: no em dashes in any UI string.
- Gate the whole feature behind a feature flag (`reading_center`), off by default, so it can ship dark.

## 3. Scope

### In scope (v1)
1. Passage library (predetermined list, admin-managed).
2. Reader with five modes: Serial, Flow, Highlight, Scroll, e-Reader.
3. Speed control, transport controls, keyboard shortcuts, progress/time remaining.
4. Preferences dialog (Spreed / Appearance / Advanced) persisted per user.
5. View panel (full text, search, click-to-jump).
6. Bookmarks.
7. Fullscreen.
8. Reading stats and speed goal on a profile/stats page.
9. Admin passage management (add, edit, reorder, hide, delete).

### Out of scope (v1), listed so nothing is forgotten
- Student-pasted text and document import (Spreeder has them; Joshua wants a fixed list). Leave the
  data model able to support `source = 'user'` later.
- AI Book Summary / AI Generate.
- Quizzes and flashcards: **not a focus**. Do not build them and do not design around them.
- Training games, courses, text-to-speech, streaks (present in Spreeder's code but never observed
  working; see inventory section 7).

### Next phase, design for it now
- **Word lists** will become very important. Do not build the word-list UI in v1, but keep the design
  ready for it: tokens carry stable `index` values per passage (section 5), and passages are stable rows
  with ids, so a later `reading_center_word_lists` / `reading_center_word_list_items
  (word, passage_id, word_index)` can link a saved word back to the exact spot in an article. Leave a
  short note in the PR describing where word lists would plug in.
- Built-in book catalogue search.

## 4. Data model (Supabase / Postgres)

```sql
create table reading_center_passages (
  id uuid primary key default gen_random_uuid(),
  slug text unique not null,
  title text not null,
  author text,
  body text not null,             -- plain text; paragraphs separated by a blank line
  cover_url text,                 -- optional; fall back to a generic document icon
  word_count int not null,        -- computed on write
  sort_order int not null default 0,
  is_published boolean not null default true,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table reading_center_preferences (
  user_id uuid primary key references auth.users(id) on delete cascade,
  wpm int not null default 200 check (wpm between 50 and 5000),
  reading_mode text not null default 'serial'
    check (reading_mode in ('serial','flow','highlight','scroll','ereader')),
  number_of_lines int not null default 1 check (number_of_lines between 1 and 6),
  words_per_line int not null default 1 check (words_per_line between 1 and 6),
  center_text boolean not null default true,
  theme text not null default 'system' check (theme in ('light','dark','high_contrast','system')),
  font_family text not null default 'Arial',
  font_size int not null default 36,
  line_spacing numeric(2,1) not null default 1.0 check (line_spacing between 1.0 and 2.0),
  punctuation_pauses boolean not null default true,
  speed_variability boolean not null default false,
  goal_wpm int not null default 600 check (goal_wpm between 50 and 5000),
  updated_at timestamptz not null default now()
);

create table reading_center_progress (
  user_id uuid references auth.users(id) on delete cascade,
  passage_id uuid references reading_center_passages(id) on delete cascade,
  word_index int not null default 0,
  completed_at timestamptz,
  last_opened_at timestamptz not null default now(),
  hidden_from_recent boolean not null default false,
  primary key (user_id, passage_id)
);

create table reading_center_bookmarks (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references auth.users(id) on delete cascade,
  passage_id uuid references reading_center_passages(id) on delete cascade,
  word_index int not null,
  created_at timestamptz not null default now()
);

create table reading_center_sessions (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references auth.users(id) on delete cascade,
  passage_id uuid references reading_center_passages(id) on delete cascade,
  reading_mode text not null,
  wpm int not null,                 -- setting at the time
  words_read int not null,
  active_ms int not null,           -- time actually playing, pauses excluded
  started_at timestamptz not null,
  ended_at timestamptz not null
);
```

RLS: passages readable by any authenticated user where `is_published`; writable by admins only.
All other tables: a user reads and writes only their own rows; admins read all.

Seed migration: insert passage 1 (section 11).

## 5. Text processing (shared by every mode)

Write one pure, unit-tested module `readingCenter/tokenize.ts`:

- Split `body` into paragraphs on blank lines, paragraphs into words on whitespace. Keep punctuation
  attached to its word. Each token: `{ index, text, paragraphIndex, endsSentence, hasPunctuation }`.
  - `endsSentence`: word ends with `.`, `!`, `?` (allowing a trailing `)` `"` `’`).
  - `hasPunctuation`: word ends with `,` `;` `:` `—` `)`.
- `chunk(tokens, wordsPerLine, numberOfLines)` groups tokens into display chunks. Chunk size =
  `wordsPerLine × numberOfLines` words, laid out as `numberOfLines` rows of `wordsPerLine` words.
  Chunks never cross a paragraph boundary.
- Position everywhere is a **word index**, never a chunk index, so changing chunk size mid-read
  keeps the reader's place (snap to the chunk containing that word).

## 6. Timing engine

One hook, `useReadingCenterClock`, drives every timed mode. Do not depend on a context object that is
recreated every tick; keep mutable state in refs.

- Base time per word = `60000 / wpm` ms. Chunk duration = base × words in chunk.
- **Punctuation pauses** (only when chunk size is exactly 1 word, matching Spreeder):
  sentence end ×2.0, other punctuation ×1.5, paragraph end ×2.5. Make the multipliers constants.
- **Speed variability** (Spreeder gives no description; this is our definition, keep it isolated so it
  can be changed): scale each chunk by its length relative to the passage average,
  `factor = clamp(0.75, 1.5, avgCharsPerWord ? chunkChars / (words × avgCharsPerWord) : 1)`, then
  renormalise so total passage time still equals `wordCount × 60000 / wpm`.
- Use `requestAnimationFrame` with elapsed-time accounting so tab throttling does not drift the speed.
- Time remaining = remaining words × base time (with pauses), rounded up to whole minutes:
  "N minutes remaining" / "Less than a minute remaining".
- Record a `reading_center_sessions` row on pause (if ≥ 5 s active), on completion and on exit.

## 7. Reader screen (`/reading-center/:slug`)

### Layout
- Top bar: Back (to library), passage title (centred), and on the right: Search (e-Reader only),
  Fullscreen, Bookmarks, Settings.
- Stage (centre): mode renderer.
- Transport (timed modes): ◁ previous chunk, ▶/❚❚ play/pause (large circle), ▷ next chunk.
- Bottom bar: keyboard-shortcuts button (left), WPM button showing current WPM, View button (centre),
  progress text "P% - N minutes remaining" (right).
- Black background by default (follows theme).

### The five modes
| Mode | Render | Settings shown on Spreed tab |
|---|---|---|
| Serial | Current chunk only, in a fixed box. Centred if Center Text on, else left-aligned. | Number of Lines, Words Per Line, Center Text |
| Flow | Current chunk only, placed at the horizontal position it would occupy in the flowing line, so the eye travels left to right then returns. | Words Per Line |
| Highlight | Whole passage visible, laid out `wordsPerLine` words per row. Current chunk full brightness, all else ~35% opacity. Auto-scroll keeps the current chunk vertically centred. | Words Per Line, Number of Lines |
| Scroll | Passage laid out `wordsPerLine` words per row and scrolled upward continuously at the WPM rate through a fixed reading line; the word at the line is emphasised. | Words Per Line |
| e-Reader | Normal paginated text sized to the viewport. No timer. Page indicator "n / total", page slider, prev/next page arrows, keyboard ← →. Search icon in the top bar searches the passage and jumps to the page of the hit. | Theme, Font, Size, Line Spacing (replaces the Spreed/Appearance split in this mode) |

Switching mode keeps the current word index.

### Controls
- **WPM dialog** "Reading Speed (WPM)": current value large, buttons −10, −100 (left) and +10, +100 (right),
  Cancel / Save. Clamp 50–5000. Saving persists to preferences.
- **View panel**: full-screen overlay. Title, small "Passage" badge, "Search this text" input that
  highlights matches, full text with current word outlined, click any word to set position, play button,
  footer "N minutes to go - W WPM". Close with ✕ or Esc.
- **Bookmarks**: while paused, click or long-press a word (in Highlight, Scroll, View panel or e-Reader;
  in Serial/Flow, the bookmark button on the paused stage bookmarks the current word) to add a bookmark.
  Bookmarks dialog lists them as a text snippet around the word with date; click to jump, trash to delete.
  Empty state: "No bookmarks yet. To add one, pause and click any word."
- **Fullscreen**: browser Fullscreen API toggle; icon swaps.
- **Keyboard shortcuts** (popover from the keyboard button, and active globally on this page):

| Keys | Action |
|---|---|
| ↑ or + | speed +10 WPM |
| ↓ or − | speed −10 WPM |
| P or Space | pause / resume |
| → | next chunk (e-Reader: next page) |
| ← | previous chunk (e-Reader: previous page) |
| R | restart from the beginning |
| S | open settings |

Ignore shortcuts while focus is in a text input.

- On reaching the end: stop, mark `completed_at`, show a completion card with words read, active time,
  effective WPM, and buttons Read again / Back to library.
- Resume: opening a passage starts at the saved `word_index` (with a one-time "Resume from where you
  left off? / Start over" prompt if index > 0).

## 8. Preferences dialog

Title "Preferences". Tabs **Spreed · Appearance · Advanced**. Footer button **Restore Defaults**
(restores the defaults in section 4 after a confirm). Changes apply live and save on change (debounced).

- **Spreed**: Reading Mode select (Serial, Flow, Highlight, Scroll, e-Reader), then the per-mode controls
  from the table above. Sliders show their current value at the right end and have discrete steps.
- **Appearance**:
  - Theme: Light, Dark, High Contrast, System.
  - Font (19): Arial, Times New Roman, Verdana, Calibri, Microsoft Sans Serif, Impact, Lucida Console,
    Comic Sans MS, Georgia, Palatino Linotype, Tahoma, Trebuchet MS, Courier New, OpenDyslexic, Antikor,
    Code New Roman, CQ Mono, Pointfree, Fira Mono. Each option rendered in its own face. Self-host the
    non-system fonts (OpenDyslexic, Fira Mono, etc.) with a fallback stack; if a licence is unclear, ship
    it with a fallback and flag it in the PR.
  - Size: 8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 28, 32, 36, 40, 44, 50, 56, 62, 68, 74.
  - Live "Sample Text" preview.
  - Must actually render in every mode (Spreeder's version is blank in speed modes; do not copy that bug).
- **Advanced**: Punctuation Pauses toggle with help "Slight pause at the end of sentences and punctuation
  marks. Only works with one word at a time." Speed Variability toggle with help "Gives longer words a
  little more time and shorter words a little less, at the same overall speed." Both help texts on a ? tooltip.

Theme values: Light (white bg, near-black text), Dark (black bg, white text), High Contrast (black bg,
yellow `#FFFF00` text, white highlight outline), System (follows OS). Use the app's design tokens for
everything except High Contrast.

## 9. Library (`/reading-center`)

- Shelves: **Continue reading** (progress > 0 and not complete, newest first, excludes hidden), then
  **All passages** (admin `sort_order`).
- Card: cover (or generic document icon on a coloured tile), title, author, word count, estimated minutes
  at the student's WPM, a progress bar if started, a check if completed.
- Card ⋮ menu: Open, View text, Hide from Continue reading.
- Search box filters by title and author.
- Empty state if no passages are published.

## 10. Stats and goal (`/reading-center/stats`)

- Header: student name, a share-free layout.
- **Vital stats**: two gauges 0–2000 WPM, Current Speed (median effective WPM over the last 5 sessions)
  and Target Speed (goal).
- Charts (Recharts or the app's chart lib): Reading Speed (effective WPM per session), Reading Focus
  (share of session time spent playing vs paused), Training Time (active minutes per day). Each with
  period picker 24 Hours, 7 Days, 14 Days, 30 Days, 6 Months, and an empty state "Not enough data yet.
  Read a few passages and come back."
- **Goal** dialog: slider 50–5000 WPM, default 600, copy "The average reader manages about 200 words per
  minute. A good first goal is 600." Buttons Cancel, Recommend (sets 3× current speed, rounded to 50,
  min 300), Set.
- Effective WPM for a session = `words_read / (active_ms / 60000)`.

## 11. Admin (`/admin/reading-center`)

- Table of passages: drag to reorder, title, word count, published toggle, edit, delete (confirm).
- Editor: title, author, optional cover upload (Supabase storage), body textarea (blank line = new
  paragraph), live word count and reading-time estimate at 200 WPM, Save.
- Deleting a passage with student progress requires typing the title to confirm and warns how many
  students have progress on it.

### Bulk import

Add `scripts/reading-center-import.ts`: reads a folder of `.md` or `.txt` files (first `# ` line or
filename = title; optional front matter `author`, `sort_order`, `cover`), computes word counts, and
upserts by slug. Dry-run flag prints what would change. This is how Joshua's article set gets loaded.

### Seed passage 1: "Living in a rational society"

Use the exact text in `research/2026-10-12-spreeder-feature-inventory.md` section 9 (three paragraphs,
about 550 words). Keep its original punctuation, including the em dash, which is source text.

## 12. Acceptance checks

The builder must verify each of these in the running app and report results in the PR:

1. Library lists the seeded passage with correct word count and estimated time.
2. Each of the five modes renders and, for timed modes, plays; mode switch mid-read keeps the word.
3. At 300 WPM, 1 word per chunk, pauses off, 300 words take 60 s ±2 % (measure with a test clock).
4. Punctuation pauses lengthen sentence ends only when chunk size is 1.
5. Speed variability on vs off: same total passage time within 1 %.
6. Every slider honours its range; every Appearance option changes the stage in every mode.
7. All seven shortcuts work, and do nothing while typing in the View search.
8. WPM dialog buttons and clamping; value persists after reload.
9. View panel search highlights matches; clicking a word moves the position.
10. Bookmarks add, list, jump, delete; persist after reload.
11. Closing mid-passage and reopening offers resume at the same word.
12. Completion card appears; a session row is written; stats page shows it.
13. Goal dialog Recommend and Set work; Target gauge updates.
14. A non-admin cannot reach admin routes or write passages (RLS test).
15. Feature flag off hides every route and nav entry.
16. Mobile width (375 px): reader usable, controls reachable, tap a word to bookmark.
17. Unit tests for `tokenize.ts` and the timing engine pass.

## 13. Open questions for Joshua (do not block the build)

- The rest of the passage list: Joshua attaches the articles later; v1 ships with passage 1 and the
  import script.
- Nav placement: own sidebar item "Reading Center", or under an existing practice area.
