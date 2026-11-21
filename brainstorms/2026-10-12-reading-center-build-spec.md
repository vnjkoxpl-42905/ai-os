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

## 2026-10-15: Reading Center becomes the activity hub

Joshua confirmed this scope through the grilling workflow:

- `/reading-center` is the home for reading activities, starting with exactly two cards: **Read, Recall, Colour** and **Speed Reading**. RRC is a separate activity, not a Speed Reading mode.
- The collections stay separate. The three imported general-reading passages remain in Speed Reading; RRC retains its existing LR sections.
- Move the existing RRC experience, preserving its read/retell/personal-reaction/full-recall method, recordings, attempts, results and individually assignable sections. No new recall grading or RC passage conversion was requested.
- A Reading Center grant exposes both activity cards. Existing RRC-only assignments remain usable; they do not automatically grant unrelated activities or Speed Reading access.
- Speed Reading library is `/reading-center/speed-reading`; old reader, tags, profile and passage-management URLs stay valid. RRC collection is `/reading-center/rrc`; attempts and reports use `/reading-center/rrc/attempt/:assignmentId`, with validated redirects for old RRC assignment links preserving launch state, query and hash.
- Existing graded attempts and imported passages were opened in the signed-in local preview. Recorder/grading logic and saved identifiers are preserved; no new paid transcription or grading calls were made.

Implementation commit: `b6e09031` in the LSAT U repository. Publication status belongs to the dated verification record in `wiki/log.md`; a commit alone is not proof of live deployment. This dated scope supersedes the older description of Reading Center as only the speed-reader feature.

## 2026-10-15: Side rail redesign interview (in progress)

Joshua requested a revision to the two-card homepage: Speed Reading and RRC should be selectable in a side rail, with the existing RRC experience displayed in the main stage when selected. Reading Center should use a beige background and a palette inspired by the existing RRC experience. Exact visual scope and initial selection remain under discussion through `grill-with-docs`; this is not an implementation approval or a published change.

The previously confirmed separate collections, existing RRC method, saved recordings, attempts, results and separately assignable sections remain requirements.

First interview frontier:

1. Default activity: recommend RRC; alternatives are last activity used or Speed Reading.
2. Visual scope: recommend all Reading Center screens; distinguish library-only from a platform-wide theme change.
3. Contextual tools: recommend Add Text, Tags and Reading Progress under Speed Reading, with RRC retaining its own section and results tools.

Answers pending. Subsequent questions depend on these decisions. No interface changes have been made for this revision.

### 2026-10-16: Dashboard and activity navigation direction

Joshua answered the first frontier:

- The initial tab is **Dashboard**, not RRC. It should give an overview of practice across activities, recent drills, progress and useful visual graphs, with ways to reopen work. Exact metrics and composition remain to be settled.
- The existing LR drill gets its own tab with an explicitly LR-oriented name instead of the acronym RRC. The drill itself remains Read, Recall, Colour; its new navigation name is pending.
- Speed Reading remains a separate tab. A similar RC recall activity inspired by Decaf RC Translation is planned; whether that is built in this release or reserved for a subsequent release remains pending.
- Preserve the existing RRC visual composition while adjusting its palette. Plain beige is rejected. Use the **21st.dev MCP connector** for design exploration. The exact palette and whether “platform” means Reading Center or the wider LSAT U application remain pending.
- Leave Tags as they are. Their broader integration is deferred. Do not infer permission to hide or reorganize Tags from the earlier contextual-tools recommendation. Add Text and Reading Progress placement are not yet settled independently.

21st.dev catalog research found App Dashboard Layout (component 28770), Stats Card (7792) and Mini Chart (9613). These are references, not selected designs or installed dependencies. No interface changes or paid generation were performed.

### 2026-10-16: Second frontier resolved; LR Recall palette comes first

- Confirmed navigation label: **LR Recall**. Keep **Read, Recall, Colour** as the full drill title and method within the page.
- Confirmed Dashboard direction: recent attempts that can reopen or resume, separate LR recall and Speed Reading progress graphs, completed drills and practice time, and honest empty states.
- Confirmed RC activity sequencing: design and build it later; do not add an unusable RC navigation item in this release.
- Joshua changed the immediate sequence: first refine the existing LR Recall/RRC colours through 21st.dev, preserving its visual composition. Integrate the chosen design into Reading Center afterward. Wider application recolouring is not approved by this answer.
- Retrieved real 21st.dev theme CSS for Meridian Blue, Harbor Blue, Powder Blue, Purple Rain and Green Notes. Meridian Blue is the recommended comparison direction (cool grey `#eef0f3`, white panels, muted blue `#3b608f`, restrained terracotta `#b8694a`); Harbor Blue and Purple Rain are alternatives. Theme typography and layout are not selected for adoption. Green Notes retains the rejected beige direction and is not shortlisted.
- Next frontier: preferred palette direction and whether the first palette preview includes the library/instructions only or the complete drill lifecycle. No production styling changes or paid generation have occurred.

### 2026-10-16: Subtle white-background previews supersede theme redesign

Joshua rejected the proposed broader palette comparisons. Preserve the existing RRC layout, typography, accents, visuals and effects. The adjustment is limited to replacing beige background surfaces with white or subtly different whites. Prepare three versions for visual comparison before selecting a production change. Meridian Blue, Harbor Blue and Purple Rain are not approved directions. Immediate scope is local RRC previews, not Reading Center integration or a platform-wide recolour.

Three local previews are available in the existing application worktree on port 8136 at `/reading-center/rrc?palettePreview=white`, `cool` or `neutral`. They override only three neutral surface variables and the two otherwise hardcoded beige demo-panel backgrounds. Preview wiring is development-only. Typecheck and whitespace checks passed; all three were viewed in the signed-in Codex browser and left open. Screenshots are in the application worktree's `verification/rrc-white-previews-2026-10-16/` directory. No version is selected or published yet.

### 2026-10-16: Integration authorized

Joshua asked to choose the best preview and integrate it into Reading Center. Selected **Pure White** because it removes beige with the least change to the existing RRC identity. Implement the already-confirmed Dashboard, LR Recall and Speed Reading navigation, preserve Tags, separate collections, assignment access, saved attempts and results. Keep the existing RRC landscape, effects, accent colours, typography and instructional content. RC Recall remains a later activity. Publication and acceptance results will be recorded separately after verification.

### 2026-10-16: Compact LR Recall and consolidate detailed analytics

Joshua requested removing redundant analytics from the LR Recall activity page. Detailed LR progress and graded-run history belong in **Reading Progress**. Dashboard retains its compact cross-activity summaries. LR Recall should focus on choosing/doing a section and accessing its instructions, with a more compact introduction that preserves the existing artwork, demonstration, typography and effects. Keep all saved attempts and report routes. Reading Progress separates LR Recall details from existing Speed Reading analytics and settings; its data remains account-scoped.

### 2026-10-16: LR Recall entry audit and proposed hierarchy

Status: audit and documentation completed; replacement layout is proposed, not implemented or published. Joshua requested an audit after five browser annotations and asked for second-brain guidance plus Humanizer. This is a new hierarchy correction following the earlier compact release, not a claim that release failed its previous checks.

#### Evidence and diagnosis

Read-only live inspection at `/reading-center/rrc`, 1285 by 873 viewport: the hero occupies 705px. The section list follows for 794px. Recorded examples begin at document position 2319px; the comparison section begins at 3062px. These are one captured desktop state, not universal viewport measurements. The synthetic hero demonstration plays separately from the three real recorded examples. Four illustrated step tabs repeat their selected description in another panel. Full instructions open a longer essay.

Source readback: SectionLaunchFrame makes Choose a section scroll/focus the list; Read the full instructions selects the briefing panel and scrolls. SectionLibrary labels any previously started section Run it again, including when its earlier attempt is unfinished. That action creates a new attempt unless an unused assignment can be started. It does not resume the unfinished recording. Completed reports remain openable.

The existing scoped design brief still describes the original standalone door as Persuade at the top and Operate below. The primary failure is a mismatch between that landing-page hierarchy and the Reading Center's operational purpose. The palette itself is not the cause.

#### Audit priorities

1. **High: clarify the task.** Put section selection and its actual Start action near the top. Keep Instructions & examples equally easy to find but visually secondary. Do not label a scroll action Start drill or promise Resume where unsupported.
2. **High: consolidate teaching.** Put the four steps beside one real video player, with Example 1, Example 2 and Example 3 selectors. On a phone, place the player immediately after the steps. Avoid making students traverse the section list and a synthetic demo to find the recorded tutorial.
3. **Medium: remove competing repetition.** Remove the marked hero tagline and standalone Your own words, every detail comparison block. Keep own-words recall, details and argument relationships in the instructions. Move the synthetic demo out of the primary entry hierarchy, or offer it only as optional help. This placement is a proposal; existing illustration and effects are preserved until the layout is adopted.
4. **Medium: make teaching copy fair and concrete.** Coverage looks perfect and nothing was understood asserts an unobservable mental state. Everybody does, That lasts about a week and speed arriving automatically overstate what the page can establish. Replace those claims with the actual task or qualified guidance in a later instructional-copy pass. Do not shorten away method conditions.

#### Wording proposed for the five annotations

| Marked element | Proposed treatment |
|---|---|
| Hero tagline | Remove. Its method belongs in the four steps. |
| Question 1 to Question 3 selectors | Example 1, Example 2, Example 3. Retain duration; make source citation secondary. Match accessible names and player labels. |
| Your own words, every detail block | Remove the standalone block. Preserve the required distinctions in instructions. |
| Long recorded-example introduction | Watch the four steps in practice. |
| Watch it done | Video examples. |

#### Recommended layout

Compact LR Recall heading, with Read, Recall, Colour as the method name. Choose a section is the dominant action and Instructions & examples is the clear secondary action. Section choice is immediately available. Its rows distinguish Start section, Start new attempt and completed report links by real behavior. Instructions & examples contains the four steps and the recorded video together, followed by an optional Full instructions disclosure. Do not create another dashboard or repeat detailed analytics here. Keep the white ground, indigo/lavender and illustration identity, but let artwork support the controls rather than dominate the first screen.

The exact arrangement and treatment of the synthetic animation remain proposals for Joshua to adopt. No new tab structure, resume behavior, grading change or palette change is assumed.

#### Acceptance gates for a later implementation

- At desktop, phone and sidecar widths, find section choice, instructions and Example 3 without hunting through unrelated panels. A timed five-second findability check is a proposed usability target, not a test already passed.
- Keep one dominant action in each state. Section selection does not create an attempt. Starting creates or starts the intended assignment only once. Unfinished rows do not imply unsupported resume.
- Written steps, recorded examples, visible selector names and accessible names agree. Video selection does not autoplay audio. Reduced motion leaves complete usable instructions.
- Preserve microphone/recording expectations, pause semantics, the inability to return to earlier stimuli, saved attempts, account scoping and report routes. No paid calls are needed to verify entry-page navigation.
- Check contrast, focus, keyboard navigation and small-screen video/step order in the rendered page. Unit tests alone do not establish instructional clarity.

#### Sources and filing

The existing [teaching voice](../wiki/teaching-voice.md) supplies plain, specific copy; [copy corrections](../wiki/COPY-CORRECTIONS.md) already says to state things once where they matter and to avoid teaching the method twice. The [2026-09-08 RRC critique](../wiki/RRC-BRIEFING-CRITIQUE-2026-09-08.md) supplies historical hierarchy findings, not current pause behavior. The [website planning method](../references/website-design-planning.md) and its linked Nate Herk source summaries support designing for the person's decision before choosing effects. Humanizer supplied the prose review lens, not an AI-authorship verdict.

Classification: partially new synthesis. Existing principles are retained; this audit adds their application to the current LR Recall entry. Updated the application's existing DESIGN.md and scoped Activity Centre surface brief with the reusable constraints and a dated correction. Tokens and the machine-readable global palette sidecar are unchanged. No application code, backend records or published UI changed during this audit.

### 2026-10-16: Clarification interview, one decision at a time

Joshua requested no implementation of the audit suggestions until they have been explained in simple terms and discussed individually. The preceding replacement layout remains a proposal, not an approved package.

- Requested removals, held for later implementation: the sentence beneath Read, Recall, Colour and the Before you start box beside the section list.
- Confirmed: keep the large white animated example beneath the top buttons in its current location. This supersedes the audit proposal to move that animation into the instructions/examples area or remove it. The animated example is distinct from the three recorded tutorial videos farther down.
- Confirmed instruction destination: clicking Read the full instructions replaces the contents of the entire large purple introduction box, including its title, buttons, landscape and inner white animated panel, with the existing four step boxes: Read it, Tell it back, Colour it and The Recall. Preserve their existing wording. The sidebar and section list stay outside the changing area. This supersedes the proposed jump to a separate lower teaching section and the mistaken interpretation that only the inner white panel would switch.
- Requested interaction: smooth transitions within that area, with a Watch video option that switches to the tutorial there. Exact step presentation, return controls and selection among the three recorded examples remain to be clarified. No component choice or paid connector action has been approved.
- Confirmed step presentation: show all four step boxes and their existing instruction text together, stacked on smaller screens. Do not retain the separate panel repeating the selected step.
- Confirmed video presentation: Watch video replaces the four steps within the same large area with one player, Example 1 / Example 2 / Example 3 selectors and Back to instructions. Open Example 1 paused; the student starts playback. Preserve the existing three recordings.
- Confirmed primary action: Choose a section stays visible in the animated introduction, instructions and video views. It continues to take the student to the section list below, without creating an attempt or requiring a return to the introduction first.
- Confirmed content location: remove the original lower-page copies of the four steps and recorded examples once they are available inside the purple area. Preserve the content and recordings there; do not duplicate them farther down the page.
- Confirmed removal: remove the entire Your own words, every detail section with Retelling / Reciting / Listing cards. Preserve the existing own-words and detail requirements in the four steps.
- Confirmed longer instructions: preserve the existing longer written explanation under Read more in the instructions view, closed initially. Keep the four steps visible.
- New planned asset: Joshua wants to generate a video explaining these instructions in a separate step. Its script, production and relationship to the existing three worked-example videos are not settled. Do not generate it or add an unavailable video control during this clarification interview.
- Confirmed new video scope: the generated video is specifically for the full written instructions, not for the examples. The existing three recordings are distinct worked examples. Whether Watch video should now open the new full-instructions video, with a separate route to examples, remains to be clarified.
- Interview preference, superseded by the full grill-me correction below: use regular chat questions, one at a time. Do not use pop-up question controls for the remainder of this grilling.
- Open next: instruction-video versus example navigation, return navigation to the animated introduction, and remaining audit suggestions. No interface changes have been made during this interview.

### 2026-10-16: Full grill-me checkpoint and resumed rounds

Date: 2026-10-16. Goal: agree on LR Recall's introduction, instructions and video views before implementation. Status: in progress. Capture continues in this existing interview/spec file at Joshua's request. Context: the dated audit and clarification notes above; global grill-me and grilling skills; existing Reading Center and Activity Centre terminology.

#### Summary and interview correction

Use the explicitly selected `~/.agents/skills/grill-me/SKILL.md`. Ask all currently answerable unresolved decisions in a numbered round directly in chat, with recommendations, then wait. This supersedes the one-question-at-a-time preference above. Do not use pop-ups, re-ask settled requirements or implement before shared understanding is confirmed. Save each answer and read it back before the next round. The original answers below remain traceable; earlier recommendations are not user decisions.

Design branches: introduction (animation retained), instructions (four boxes and optional longer text), media (full-instructions video distinct from worked examples), navigation (section choice always available), section actions (new attempts versus reports), transition behavior, and final acceptance. The original audit package is not adopted wholesale.

#### Q&A log: recovered checkpoint of answered Q1 to Q11

Each item below corresponds to one earlier answered round. This is a recovery checkpoint from the conversation and prior saved bullets, not a claim that structured entries were written at those earlier moments.

**Q1: Animated example location**
- Asked/recommended: move the white animated panel beside the instructions and recorded examples.
- Captured: "Keep it where it is." Recommendation rejected. Initial animation remains in its current introduction location.

**Q2: Instructions destination**
- Asked/recommended: show the steps and recorded videos together instead of opening the longer essay first.
- Captured: preserve the instructions; switch content within the same card with smooth transitions; four steps and a Watch video option.
- Flag resolved by Q3/Q4: which card switches. Do not treat the question's proposed separate learning area as approved.

**Q3: Inner white panel interpretation**
- Asked: whether only the inner white animated panel would switch.
- Captured: "the purple bigger box" and "the whole purple; box, you swap it." The inner-panel interpretation was rejected, not approved.

**Q4: Entire purple area's contents**
- Asked/recommended: replace the entire purple area's contents with instructions.
- Captured: "replace the whole purple box contents" with the existing Step 1 to Step 4 boxes. Sidebar and section list stay outside the changing area. Exact return controls were not independently adopted by this answer.

**Q5: All four steps together**
- Asked/recommended: show every step's existing text together without a repeated selected-step panel.
- Captured: "Yes, show all four steps and their text together." Stack them on smaller screens.

**Q6: Existing example player**
- Asked/recommended: one player, Example 1 to Example 3 buttons, Back to instructions; Example 1 opens paused.
- Captured: "Yes, one player with three example buttons and a back button."
- Later correction: Q10/Q11 adds a distinct full-instructions video. The agreed example-player arrangement remains, but the original assumption that Watch video necessarily opens examples is pending Q12.

**Q7: Section choice in every view**
- Asked/recommended: keep Choose a section available in all three views.
- Captured: "Yes, keep Choose a section visible in all three views." It takes the student to the section list; it does not itself start an attempt.

**Q8: Lower-page duplicates**
- Asked/recommended: remove the old lower-page instructions and video sections once the content is available within the purple area.
- Captured: "Yes, remove the old copies farther down." Preserve their content in the new location.

**Q9: Comparison cards**
- Asked/recommended: remove Your own words, every detail and its Retelling / Reciting / Listing cards.
- Captured: "Yes, remove that comparison section." Existing method requirements remain in the steps.

**Q10: Longer explanation**
- Asked/recommended: retain the exact longer explanation under Read more, closed initially.
- Captured: "keep longer explanations under 'Read more'." Joshua also plans a generated video for the instructions. Generation is a separate future task, not authorized to begin during this interview.

**Q11: New video versus examples**
- Asked/recommended: distinguish a new instructional tutorial from the three existing recordings.
- Captured: "the video shouldnt be for the examples" and "specifically for thefull instructions". The new video covers the full written instructions. Exact navigation remains pending; do not imply approval of the offered labels. Joshua requested direct-chat questions, then subsequently corrected the round size to the full grilling method.

#### Open flags (pending input)

- Q12 resolved below: use Watch instructions for the full-instructions video and Watch examples for the existing recordings.
- Q13 resolved below: use Back to home for the local introduction view, without leaving the page.
- Q14 resolved below: use Start section / Start new attempt, preserving current behavior.
- Smooth-transition implementation and connector/component choice -> agent after navigation decisions; respect reduced motion and do not spend credits without applicable authorization.
- New instruction-video script, production and readiness -> separate future task with Joshua.
- Final shared-understanding confirmation -> Joshua; implementation remains on hold.

#### Resumed round: Q12 to Q14 (answered)

**Q12: Separate instruction video from examples**
- Asked: should Watch video open the new full-instructions video, while Watch examples opens the existing three recordings?
- Recommended: yes, keep these purposes separate within the same changing purple area.
- Captured: Joshua corrected the label to "watch instructions" and paired it with "watch examples". Use Watch instructions for the full written-instructions video and Watch examples for the three existing recordings. This supersedes Watch video as the label. The new video's production remains a separate future task.

**Q13: Return to introduction**
- Asked: should Back to introduction restore the original title and animation, while video views use Back to instructions?
- Recommended: yes, offer an obvious route back without leaving the page.
- Captured: "it should say back to home" and agreement that students move between views without leaving the page. Back to home restores the original introduction within the changing purple area, not Reading Center Dashboard. This supersedes the proposed Back to introduction label. Existing Back to instructions on media views remains the prior agreed return path unless later changed.

**Q14: Truthful section-start labels**
- Asked: should section-row buttons say Start section when there is no previous attempt and Start new attempt otherwise, replacing Run it again without changing behavior?
- Recommended: yes, make it clear this starts new work rather than resuming the earlier recording.
- Captured: "go with your recommendation." Use Start section when there is no previous attempt and Start new attempt otherwise, preserving the actual attempt behavior. No resume feature is requested.

#### Remaining frontier: Q15 to Q16 (answered)

**Q15: Written versus video entry controls**
- Asked: should the opening Read the full instructions control still show the four written steps, with Watch instructions and Watch examples available inside that instructions view?
- Recommended: yes, distinguish reading the method from watching either video type.
- Captured: "Yes to both." The opening Read the full instructions control shows the four written steps. Watch instructions and Watch examples belong inside that instructions view, with Watch instructions subject to video readiness below.

**Q16: Release before the new instruction video exists**
- Asked: should the redesigned page be able to ship with the written instructions and existing examples, adding Watch instructions only when the generated full-instructions video is ready?
- Recommended: yes, avoid an empty or disabled video control; keep production of the new video separate.
- Captured: "Yes to both. Keep watch instructions hidden until the video is ready." The redesigned page can use the existing written instructions and examples before the generated full-instructions video is ready. Add Watch instructions only when the real video is available. This resolves sequencing, not final implementation approval.

Next: after these answers, present the complete design for shared-understanding confirmation and ask whether anything was missed. No implementation during clarification.

#### Consolidated design for final confirmation

Status: interview decisions settled; final shared-understanding confirmation pending. No implementation has begun.

- Opening view: retain the existing purple introduction, artwork and animated demonstration in place. Remove only the marked sentence beneath the title. Keep Choose a section and Read the full instructions.
- Switching area: replace the contents of the entire purple box when changing views, not just the inner white animated panel. Use smooth transitions without leaving the page; retain accessible reduced-motion behavior. Sidebar and section list remain outside the changing area.
- Written instructions: show the four existing step boxes and all their existing text together: Read it, Tell it back, Colour it, The Recall. Stack appropriately on smaller screens. Remove the repeated selected-step detail panel. Keep the exact longer explanation under Read more, closed initially.
- Navigation: Choose a section remains visible in every view and takes the student to the existing section list. Back to home restores the opening introduction locally. Media views retain Back to instructions.
- Media: Watch examples opens one paused player with Example 1 / Example 2 / Example 3 selectors and the existing recordings. Watch instructions is reserved for the planned generated video of the full written instructions and stays hidden until that video is ready. Its production remains a separate task.
- Cleanup: remove the old lower-page copies of the steps and videos, the Before you start box and the entire Your own words, every detail comparison section. Preserve necessary method requirements and the relocated content.
- Section controls: Start section for no previous attempt; Start new attempt otherwise. Preserve current attempt behavior, completed reports, recordings and account access. No resume feature or grading change.
- Scope: preserve current typography, colours and visual identity. No broader palette redesign, replacement instructional wording, dashboard changes or new analytics. Implementation starts only after Joshua confirms this consolidated understanding.

Open flag: final confirmation and any omitted requirement -> Joshua. Video production -> separate future task. Routine component/transition implementation -> agent after confirmation.

#### 2026-10-16: Shared understanding confirmed; implementation authorized

Joshua confirmed the consolidated design: "Yes, that's everything. Go ahead and implement the LR Recall changes as agreed, keep the transitions smooth". Interview status: complete. Implement the consolidated design above. His closing phrase about Watch instructions is interpreted consistently with the explicit preceding agreement: hide it until the full-instructions video is ready. No such video exists yet; do not render its control or substitute the example videos for it. Production of that video remains separate. Verification and publication results will be recorded after the implementation is checked.

#### 2026-10-16: Implemented, published and live verified

Commit b7557bf16a25456dffaf9278384df2ef1cadcfa0 implements the agreed Reading Center-only view changes and clearer section-start labels. Safe-push typecheck, production build/content guard, scoped ESLint and 148 focused tests passed. The broader run has 14 pre-existing failures reproduced exactly on a pristine pre-change checkout; these unrelated activity-test failures were not repaired or represented as passing.

The free Lovable publication request 1bb8945b-2579-412f-897f-7ff6092a3bd0 completed: the custom domain serves changed asset /assets/index-De-rZ_Pg.js, and Lovable reports the exact commit. Signed-in live readback verified all four complete step bodies, closed/expandable Read more, Example 3 paused, return navigation within the same route, retained home animation, removed duplicates/marked copy and absent Watch instructions. No console errors. Responsive/reduced-motion and visual-clipping checks passed locally at 320/600/768/1024/1440. No new attempt, microphone/provider call or student impersonation. Existing attempts, recordings and grading behavior are unchanged. The live instructions view was left open in Codex. The full-instructions video remains a separate future task.


#### 2026-10-16: Smaller instruction cards published; presenter video prepared

Joshua requested a slight card-size reduction and a new full-instructions video with a realistic on-screen presenter and a different, natural voice. Commit 91935fa8f6138286e56cb44f82f7d6fd6ba8a286 reduces illustration height to 132px, padding to 16px and headings to 26px while retaining all four complete instruction bodies. Build/content guard and safe-push typecheck passed. Responsive checks at 320/600/768/1024/1440 found no clipped text or horizontal overflow. Free Lovable publication 5ed764d0-2ac4-423a-887f-b566f37507a7 completed; signed-in live verification found asset /assets/index-J_VfSnE6.js and the exact new sizing, with no clipped instruction text.

Video packet: C:/Users/Joshu/dev/ai-os-projects/lr-recall-instructions-video. SCRIPT.md contains 814 words, approximately six minutes, sourced from all six instruction sections and four steps. source-instructions.json is a hash-verified copy. No presenter or voice has been selected or generated. HeyGen remains signed out in browser and CLI; the sign-in tab is open. Watch instructions remains hidden. No provider credits spent.

Setup side effect: HyperFrames init refreshed six pre-existing global helper skills in .agents and .claude and added ten Gemini skill directories. Canonical vault copies remain unchanged. Current refreshed copies were hash-verified into C:/Users/Joshu/.codex/backups/hyperframes-init-20261016-055702. This is a post-install backup, not an exact pre-install rollback; no global files were deleted or restored without evidence.


#### 2026-10-16: Reference recordings and grader audit, not yet a scoring-policy change

Joshua requested comparison of existing recordings/transcripts to their questions, reference listening in LR Recall review, and grader evaluation. He then requested the Translation workout and prior RRC standards as the basis. Read the full Loophole Translation + CLIR Drill and Translation Marathon captured procedures, and current app-owned read-recall-colour-section.instructions.json. Loophole prescribes chunk translation, quip, then exact-idea CLIR checking, with an out-loud 20-minute goal and complete conditions. RRC explicitly adds a hidden-text final recall, says this part is scored, preserves own words/free order/details, and uses a separate captured-key Read criterion. These are related procedures, not identical scoring contracts.

Source audit found current grade-rrc-section combines working retell and final recall for numeric detail coverage, while final recall also has a separate qualitative verdict. Report playback prioritizes the final recall window but WHAT YOU SAID displays combined speech. This conflicts with a simple reading of the current learner-facing final-recall scoring instruction. Evaluate and resolve before changing production scores; historical grades remain unchanged.

The current judge model in source is gemini-3.1-flash-lite; the documented coverage floor calibration refers to another model. Source is not proof of deployed function version or present judge accuracy. Deepgram Nova-3 supplies ASR. Existing rrc-census performs paid judge calls without a dry-run/max-call gate; it was not run.

Exact local mapping audit: 12 section files, 283 stimulus items, 303 citations all match archived current citations. 274 stimulus items have at least one audio; 294 citation-linked audio records, 275 distinct audio hashes. Instructor transcripts contain reading, translation, reactions and CLIR, not isolated final recall. They are comparison evidence, not a verbatim gold learner answer. Preserve grouped citations and audio exceptions. No uploads, provider calls, regrades or source/grader edits performed during this audit.

Recommended evaluation cases: good paraphrase and reordered ideas; all/most and modality changes; lost negatives; reversed relationships; correct working retell with failed final recall; verbatim reading; silence; ASR errors. Human-label expected detail and reasoning judgments before a capped provider evaluation. Keep working translation feedback, final-recall coverage and CLIR accuracy distinct; this remains a recommendation pending the source-contract review.


#### 2026-10-16: Historical scoring intent found; correction to initial audit interpretation

Accepted app ADR0013 explicitly counts working retelling, colouring and final recall together for per-stimulus coverage; the 2026-09-01 grader specification agrees. Combined coverage is therefore intentional historical policy, not an established backend defect. Current step-four learner copy saying this is the part that gets scored is incomplete/conflicting with that accepted policy. Do not silently switch numeric scoring to final-recall-only. ADR0025 supersedes earlier no-analysis language and makes The Read a separate given/matched judgment; ADR0030 reinforces retention versus understanding. The earlier final-only recommendation above remains unadopted and must not be treated as a locked decision.

ADR0035 requires recalibration before displaying grades from a changed judge. Current source uses gemini-3.1-flash-lite while calibration documentation names gemini-3.8-flash; evidence of current-model calibration is not established. Actual deployed model remains unverified. Resolve the learner-copy/scoring-contract disagreement and evaluate the current judge with reviewed samples before production changes. No model evaluation or live regrade has occurred.


#### 2026-10-16: Cheaper model and material-meaning grading proposal

Joshua requested a cheaper appropriate judge and grading that prioritizes important meaning and differences that matter. This does not yet settle how to change the accepted full-detail coverage policy. Source audit: grade-rrc-section selects gemini-3.1-flash-lite; shared gemini-proxy overrides every requested chat model with the same ID. A grader-only model-name edit through that proxy would not establish a model change. No production model was changed. Avoid changing the shared proxy for one activity; use an explicit isolated allowlisted evaluation route if comparing models.

Official Google pricing checked 2026-10-16: Gemini3.1Flash-Lite text input/output USD0.25/1.50 per million tokens; Gemini2.5Flash-Lite USD0.10/0.40. https://ai.google.dev/gemini-api/docs/pricing . These are direct standard provider token rates, not a verified Lovable gateway bill or complete per-attempt cost. Candidate2.5 is cheaper, not proven adequate for this rubric.

Recommendation: test current cheap model with revised evidence-based feedback first, alongside2.5Flash-Lite in a bounded evaluation if budget approved. Keep existing meaning/word-order tolerance. Distinguish changed core claim/relationship/negation/qualification from omitted detail and harmless paraphrase. Require short cited learner evidence and the source proposition for each deduction; never invent missing speech or use instructor commentary as learner evidence. Keep full-detail retention measurable separately from material reasoning errors, so gist-only does not pass and one small omission does not receive the same explanation as a reversed argument. This is proposed evaluation policy, not a deployed rubric change.

Use reviewed faithful paraphrases, harmless name substitutions, all/most, possible/certain, lostnegation, reversedcausality, missingnecessarycondition, gist-only and ASR-error cases. Record false deductions, missed meaning changes, repeat-run agreement and measured token costs. Current judge has no explicit dollar/token spending cap, and gatewayfailure may add a direct fallback call. Add a call/token/cost ceiling to an isolated harness before executing; do not run uncapped rrc-census. No paid model tests or historical regrades performed.


#### 2026-10-16: Saved instructor references selected for grader calibration

Joshua authorized using saved Loophole explanations and homepage worked examples as standard-setting inspiration. Created six-question calibration-candidates.md/json under app verification/lr-recall-reference-audit-2026-10-16. Each contains exact authored stimulus/chunks, written CLIR, complete-transcript source paths, bounded evidence excerpts and text hashes. These are candidate calibration references, not automatically full-credit gold responses. Transcript inspection found ASR/meaning faults including no-reason-to-think-harm versus no-harm, remote-work narrowing and explosion/implosion confusion. Preserve these as adjudication flags and negative test opportunities rather than silently feeding them as truth. No independent listening claim, paidcalls, benchmarkresults, regrades or productiongraderchanges. Current buildJudgePrompt already includes an optional same-question modelRun solely for calibration, with student-speech-only evidence rules. Model analogies/jokes/order must not become mandatory answer details.

Homepage example source recovery completed: 17 text files from private lsatu-films commit6357e00 saved under app verification/lr-recall-reference-audit-2026-10-16/homepage-example-sources/, with git blob identities and SHA256 provenance. recall/scripts.json contains the three authored whole-stimulus recalls; instruction cue/script/timing files separate read, retell, colour and final recall. These are stronger phase-specific calibration candidates than full mixed Loophole transcripts. Source recovery does not independently establish exact rendered MP4 audio correspondence. No provider evaluation or production change performed.



#### 2026-10-16: Joshua designates instructor recordings as 10/10 standards

Joshua explicitly clarified that her recorded responses are the golden standard, 10/10. Treat those instructor performances as the owner-selected positive calibration standard, including her natural paraphrase, emphasis, level of detail and analytical response. Do not impose a stricter invented ideal and then penalize these designated examples for failing it. This supersedes the earlier framing that the recorded performances themselves await Joshua's approval. The extracted transcripts and phase boundaries remain independently fallible: an ASR difference is not a defect in her performance; the original recording takes priority. Authored factual sources still identify what is being discussed, and instructor analogies/jokes are not mandatory wording for students. No claim of direct auditory review, completed provider evaluation or deployed grading change is made by this decision record.


#### 2026-10-16: Meaning-based grading fixes implemented; live AI benchmark blocked

Joshua authorized fixing unreasonable deductions, keeping the cheaper model and using her recorded responses as the designated 10/10 standard. App commit c128c71e implements meaning-equivalent/contextual paraphrase rules; per-detail learner quotes and reasons retained in saved grade JSON; strict evidence parsing refuses missing/duplicate/malformed judgments rather than fabricating student deductions. Explicit reviewed country-sweden coverage grouping prevents duplicate counting in PT102.S3.Q24, including legacy snapshots via exact question/text allowlist. Combined retelling/final-recall policy and separate Read remain unchanged. Gemini3.1Flash-Lite remains configured. Grader version2/build2026-10-16-meaning-evidence and8192output-token cap identify the new code. Historical grades were not regraded.

Verification:71focusedtests passed, productionbuild/contentguard passed, independentreview parserfindings fixed, evaluatorTScheck passed. scripts/rrc-eval contains15source-verified cases including3homepageauthoredrecalls and3actualsavedS1instructortranscripts (exactproductionreadstripper), plusparaphrase/materialchangecontrols. Offlinevalidation passed; originalaudio/transcriptbytes hashchecked for selectedreferences, no independent listening claimed. Modelbenchmarks were NOTexecuted: --run stoppedbeforeprovider with missingexistingGEMINI_API_KEY. Zero provider calls and no testcharges. AdminJWT cannotinvokeinternal-onlyAIproxy; noauthenticationbypassadded. Test runner has15sequentialcalls/no retries/$0.50conservativebatchreservationcap and savedprompt/sourcehashes. It doesnotwriteor regrade studentrecords.

Not deployed: backendfunctionchange. LovableCloudbackenddeploymentrequiresseparate explicitroute/creditconfirmation underrootAGENTS, and actualmodelcalibrationstillpending legitimatecredentialaccess. Do not report offlinefixtures/unitchecks as proofherrecordingsscore10/10. Maincodepush/typecheckstatus recorded separately aftercompletion.


2026-10-16 final follow-up: commit0e332460 removes the remaining exact-label and uncertainty-as-failure prompt conflicts. Same entity expressed through a unique contextual role and equivalent quantities count; unresolved ASR meaning uses uncertain_details and is refused as ungraded. Strict malformed uncertainty payloads are also rejected. Finalfocusedtests76/76passed; final15caseofflinevalidationpassed with source/prompt hashes. No live model tests could run without an existingGEMINI_API_KEY; allrequestsblockedbeforeprovider. Codecommitc128c71e merged safely through6e45c88e onto main; finalfollowuppush/typecheckpending at this logcheckpoint. Backenddeploymentandrecording-basedAIqualityconfirmationremainpending; nothingwasregraded.

#### 2026-10-16: Lovable-backed deployment and three actual reference tests

Joshua approved Lovable credits and the deployment route. Lovable deployed only grade-rrc-section with bundled shared source, reporting 0.8 credits. Independent admin census no-transcript probe read the new BUILD 2026-10-16-meaning-evidence from the live backend. Gemini 3.1 Flash-Lite remains configured; no new local Gemini API key is necessary for this server-backed test route. No student records or historical grades changed.

Three saved PT105.S2 instructor transcripts were tested once each. Q1 and Q2 returned Detail 1 has no evidence audit and were refused as ungraded. Q3 scored 100% (11/11), with matching Read and no missed details or decoy credit. All three requests completed, but only one returned a valid grade. Do not report the grader calibrated or all instructor standards passing. Provider raw replies were not retained by the census response, so the missing evidence-versus-reason field is unknown. Further response-contract hardening and another explicitly capped evaluation remain required. Receipt: C:/Users/Joshu/dev/ai-os-projects/lsatu-reading-hub-20261015/verification/rrc-meaning-eval/2026-10-17T00-13-25-968Z-live-census/.

#### 2026-10-16: Grounded evidence and explicit meaning grading

Joshua authorized further Lovable credits, fixing output failures and rerunning the three references, with important meaning rather than incidental wording as the grading criterion. The first structured-schema rerun (live BUILD 2026-10-16-structured-evidence) yielded PT105.S2.Q1 88% factual coverage, Q2 ungraded for an edited quotation, Q3 100%. Q1 also exposed a source-leaking credit for large based on the prompt alone. These were not reported as three passing standards.

Follow-up commit 4b14b2bb makes evidence selections numbered units of the stripped learner transcript; the server reconstructs genuine quotations and retains strict validation. Generic calibration examples preserve source claims, relationships and qualifications, distinguish hypothetical reactions from source assertions, and contain no target reference answers or forced scores. Meaning preservation is now explicitly separate from exhaustive factual coverage. Important actors, relationships, negation, conditions, relevant quantities and modality remain material. Incidental details can be omitted or differ without reducing meaning, but remain truthful factual misses; zero material facts never produces an automatic 100%. Original factual percent/bands remain available and historical grades are not reinterpreted.

Read-stripping regressions identified and fixed boundary shifts that cut adjacent words or left fragments. Independent review blocked unsafe combined spans twice until guards preserved punctuated, unpunctuated and common-vocabulary learner asides. Final 29 read tests, 89 grading tests and 84 report/library tests passed, totaling 202. New and historical report variants were inspected in the running local browser; screenshots are in app verification/rrc-meaning-eval/. Final production build passed. Main push, Lovable deployment and final reference/control results are recorded afterward; this checkpoint is not a passing live calibration claim.

Lovable's structured-evidence deployment cost 1.8 credits and also changed unrelated MCP/email packaging source despite the deployment-only request. These changes are preserved, explicitly surfaced to Joshua, and their functions were not deployed according to the Lovable report. Existing generated MCP local work was preserved in exact-hash verification copies and Git stashes during merge. No student grade writes or historical regrades were requested.

#### 2026-10-16: Provider format repaired and live grading controls verified

Main 537a58e3 was deployed through Lovable after Joshua approved dismissing the outdated plan. Live build `2026-10-16-grounded-meaning-2` was independently verified. All three reference responses parsed, and their numbered evidence reconstructed genuine learner quotations. PT105.S2.Q1 returned 90% meaning and 83% detail coverage; Q2 and Q3 returned 100% on both. All Read and colour checks passed, with no reciting or listing flags. All three altered-source controls rejected the changed essential claim. Exactly six jobs ran without retries or student-record writes. One Q1 control retained an original read-aloud sentence, but its actual retelling independently supported the deduction. Saved transcript testing does not establish independent listening to the recordings.

The next general prompt refinement, main 5ee1fdff and live build `2026-10-16-grounded-meaning-3`, still produced Q1 91% meaning and 83% detail coverage. Q2 and Q3 remained 100% on both. All three controls remained valid and rejected their altered claims. Q1 still marked salinity and a precise formation footprint as material merely because they were specific details. Prompt wording alone did not fix the underlying scoring instability.

The durable correction fixes essential meaning before seeing a learner response. Source-only reviewed keys classify all 54 authored facts across the three reference questions, with written reasons. They bind the exact source and ordered fact text, lines and kinds. Unknown or changed snapshots fall back to every fact counting as essential. The model still judges factual preservation and must select grounded learner evidence; it cannot choose the denominator. Incidental errors remain in exhaustive detail coverage and feedback. No expected score or learner transcript is stored in a reviewed key.

An independent source review approved the classifications. The final implementation passed 104 focused tests, 15 offline fixtures and typecheck. Commit 354c8140 was safely merged and pushed as main aa8b79f0. Live build `2026-10-16-grounded-meaning-4` and grader version 4 were requested through Lovable; final deployment and test results are recorded afterward. Only the three reference sources have reviewed materiality keys so far. The synthetic altered-source controls test conservative stale-key handling and contradiction detection; unit tests separately cover wrong responses under a fixed reviewed denominator.

The frontend was published through the free control. Public bundles `index-BkH9Siqj.js` and `SectionReportCard-DAnEPxb7.js` include separate Meaning preserved and Detail coverage metrics. Signed-in live report acceptance was unavailable; local new and historical report browser checks passed.

Lovable also performed unrelated preview packaging work despite deployment-only requests. These changes were surfaced, preserved and distinguished from the grader. Its latest preview-local package install was untracked, but Git readback also found a two-line deno.lock addition in 4752374e. No unrelated functions were requested for deployment. The original dirty generated MCP working copy remains preserved with SHA-256 C436D33DF2E99CCA3C80893ED27985F5DF6E3B7DCA6FA93E4749F80D2A55996C.


#### 2026-10-17: LR Recall grading fix deployed and final references pass

Final live BUILD `2026-10-16-grounded-meaning-5`, grader version 5, was verified independently. Gemini 3.1 Flash-Lite remains the configured cheap model through Lovable gateway with direct fallback. The response schema is provider-compatible; numbered learner evidence is validated and reconstructed by the server. Source-only reviewed keys fix the essential-meaning criteria before seeing any learner response. A valid source-consistent alternative Read is now accepted rather than requiring the authored example's particular gap. These are rubric and evaluation improvements, not model-weight fine-tuning.

Final saved-transcript reference tests: PT105.S2.Q1 100% operative meaning (16/16) and 83% exhaustive detail coverage (20/24); Q2 100% (18/18) and 100% detail coverage (19/19); Q3 100% (11/11) and 100% detail coverage (11/11). All three Read and method checks passed. Q2's alternative critique of sales volume versus profit per dose was explicitly accepted. Every reconstructed quotation was grounded in stripped learner speech.

The final three altered-source controls scored 79%, 95% and 91%; each contradictory target was rejected, with zero credited decoys or invalid quoted units. These controls invalidate the exact reviewed source keys and exercise conservative all-essential fallback. They are not live wrong-answer tests under an unchanged reviewed key; unit tests cover fixed-denominator behavior. Exactly six final jobs ran without retries. Saved transcript tests do not establish independent listening or perfect ASR alignment. Reviewed materiality keys currently cover only the three reference sources; unknown or changed sources remain conservative.

Final verification: 109 focused tests, 15 offline fixtures, production build with the 758-file canonical-content guard, and safe-push typecheck passed. Read fix 5ffab1b9 is deployed. Unsolicited Lovable dependency/config changes were independently reviewed, then exactly reversed across five preexisting files with new commit 96bc7af1. GitHub main was read back at 96bc7af195db002a6bc4c2c1d7ef9bf628b1c9d5. No history rollback, file deletion, historical regrades or student-record writes. The unrelated dirty generated MCP working copy remains byte-identical to its preserved C436...996C backup. No further Lovable agent was invoked after dependency restoration.

Known Lovable credits across this repair's deployment/debugging requests total 11.9, excluding the earlier 0.8-credit initial deployment. Gateway token usage and inference costs were not returned. The final scoped deployment cost 0.4 credits and made no edits.

Full report: `C:/Users/Joshu/dev/ai-os-projects/lsatu-reading-hub-20261015/verification/rrc-meaning-eval/REPORT.md`. Final reference receipt: `2026-10-17T04-56-54-447Z-live-census`; final control receipt: `2026-10-17T04-57-40-237Z-live-controls`. Earlier failed/intermediate receipts remain preserved.
