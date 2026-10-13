---
title: Reading Center step-by-step build plan
date: 2026-10-13
builder: Gemini 3.8 Flash
reviewer: Claude (reviews and fixes after the build)
spec: brainstorms/2026-10-12-reading-center-build-spec.md (the "what"; this file is the "how")
reference: research/2026-10-12-spreeder-feature-inventory.md
---

# Reading Center: step-by-step build plan

Read this whole file once before you start. Then do the steps **in order**. Do not skip a step. Do not
combine steps. After each step, run its **Check** and only continue when the check passes. If a check
fails twice, stop and write what failed into the PR description under "Blocked"; do not invent a
workaround.

Repo: `C:\Users\Joshu\dev\ai-os-projects\lsatu`. You work in a separate worktree created in Step 0,
`C:\Users\Joshu\dev\ai-os-projects\lsatu-reading-center`; all paths after Step 0 are relative to it.

---

## Rules you must follow the whole time

1. **Branch, never `main`.** Step 0 creates the branch. Never run `git push origin main`, never
   `git reset --hard`, never `git push --force`.
2. **Touch only the files this plan names.** The one exception: a test file next to a file you created.
   Do not reformat, rename or "clean up" any other file.
3. **Do not edit** `src/integrations/supabase/types.ts`, `src/integrations/supabase/client.ts`,
   `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, or any existing migration file.
4. **Do not apply database migrations.** Write the `.sql` file only. Do not run `supabase db push`,
   do not call any Lovable tool, do not send Lovable any message. The reviewer applies the migration.
5. **No new npm packages.** Everything needed is already installed (React, react-router-dom,
   @tanstack/react-query, recharts, shadcn/ui in `src/components/ui/`, lucide-react, vitest).
6. **No em dashes (—) in any text a user sees.** Use a comma, a colon or a period instead.
   (The seed passage in step 2 is the one exception: it is source text, copy it exactly.)
7. **Because the database types are not regenerated yet**, every Supabase call to a `reading_center_*`
   table must go through the helper `rcDb()` from step 4. Never write `supabase.from("reading_center_...")`
   anywhere else.
8. **Imports** use the `@/` alias, e.g. `import { Button } from "@/components/ui/button";`.
9. TypeScript strict mode is off in this repo. Still give every exported function explicit parameter and
   return types.
10. Commit after every step with the exact message given. Run `npm run typecheck` before every commit;
    if it fails, fix only errors in files you created.

---

## Supervisor: ask Claude, headless

A Claude supervisor oversees this build. It is the same Claude chat that wrote this plan, so it already
knows everything. You talk to it by running the `claude` command in your terminal. The command must run
**from `C:\Users\Joshu\dev\ai-os`** (that is where the chat lives), so it always starts with `cd`.

Use this exact command every time, changing only the message in the last quotes:

```bash
cd C:\Users\Joshu\dev\ai-os && claude -p --resume 70b72262-5c64-4c94-b8d5-90f16a760c0b --add-dir C:\Users\Joshu\dev\ai-os-projects\lsatu-reading-center "[Gemini] <your message>"
```

Always start your message with `[Gemini]` and include the step number, what you did, and the exact
question or the exact error (last 40 lines). Your first message, right after Step 0, must be:
`[Gemini] Starting. Step 0 done, worktree at C:\Users\Joshu\dev\ai-os-projects\lsatu-reading-center on feat/reading-center. Ready for supervision.`

If the command errors (for example the session is busy), wait 60 seconds and retry once. If it fails
again, stop and tell Joshua.

When you **must** call it:
1. **Before you ask Joshua any question.** Ask the supervisor first. Only ask Joshua if the supervisor
   says "ask Joshua".
2. **When a Check fails twice.** Send the step number, the command, and the last 40 lines of output.
3. **After Steps 5, 10, 12 and 16** (checkpoint reviews). Message:
   `[Gemini] Checkpoint: Step N done. Review the diff for this step against the plan. Reply APPROVED or list exact fixes.`
   If it lists fixes, make exactly those fixes, commit, and send the checkpoint message again until it
   replies APPROVED.
4. **Before Step 19** (final review). Message: `[Gemini] Final review before PR. Review the full diff.`

Rules for the supervisor's answers:
- Its instructions override your own judgement, but never these: do not push to `main`, do not apply the
  migration, do not use Lovable, do not delete files outside the worktree.
- If it says "STOP", stop and report to Joshua.
- Paste every supervisor reply into the PR description under a heading "Supervisor log" (latest last).

---

## Step 0: Create the branch

The main checkout (`C:\Users\Joshu\dev\ai-os-projects\lsatu`) is shared with other sessions and often
has uncommitted changes that are not yours. **Never** stash, restore, discard, commit or switch branches
there. Build in a separate worktree instead. Run, one command at a time:

```bash
git -C C:\Users\Joshu\dev\ai-os-projects\lsatu fetch origin
git -C C:\Users\Joshu\dev\ai-os-projects\lsatu worktree add C:\Users\Joshu\dev\ai-os-projects\lsatu-reading-center -b feat/reading-center origin/main
cd C:\Users\Joshu\dev\ai-os-projects\lsatu-reading-center
npm install
```

From now on, **every path in this plan is relative to `C:\Users\Joshu\dev\ai-os-projects\lsatu-reading-center`**.

**Check:** `git branch --show-current` prints `feat/reading-center` and `git status` shows a clean tree.

---

## Step 1: Create the folder structure

Create these empty folders (add each file in later steps):

```
src/features/reading-center/
src/features/reading-center/lib/
src/features/reading-center/hooks/
src/features/reading-center/components/
src/features/reading-center/components/modes/
src/features/reading-center/pages/
```

Create `src/features/reading-center/CONTEXT.md` with exactly:

```md
# Reading Center

Speed-reading tool for general articles (not LSAT RC). Spec: ai-os
brainstorms/2026-10-12-reading-center-build-spec.md.

- lib/: pure logic (tokenize, timing, constants, types). No React, no Supabase. Unit tested.
- hooks/: data access (react-query) and the reading clock.
- components/: UI. components/modes/ holds one renderer per reading mode.
- pages/: route components (library, reader, stats, admin).

Word lists (next phase) will link to (passage_id, word_index). Word indexes come from
lib/tokenize.ts and must stay stable for a given passage body.
```

**Check:** the six folders exist. Commit: `reading-center: scaffold feature folder`.

---

## Step 2: Write the database migration

Create `supabase/migrations/20261013120000_reading_center_v1.sql`. Copy this **exactly**, then paste
the seed passage where marked.

```sql
-- Reading Center v1: passages, preferences, progress, bookmarks, sessions.
-- Additive only. No existing table is altered.

create table if not exists public.reading_center_passages (
  id uuid primary key default gen_random_uuid(),
  slug text unique not null,
  title text not null,
  author text,
  body text not null,
  cover_url text,
  word_count int not null default 0,
  sort_order int not null default 0,
  is_published boolean not null default true,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.reading_center_preferences (
  user_id uuid primary key references auth.users(id) on delete cascade,
  wpm int not null default 200 check (wpm between 50 and 5000),
  reading_mode text not null default 'serial'
    check (reading_mode in ('serial','flow','highlight','scroll','ereader')),
  number_of_lines int not null default 1 check (number_of_lines between 1 and 6),
  words_per_line int not null default 1 check (words_per_line between 1 and 6),
  center_text boolean not null default true,
  theme text not null default 'system'
    check (theme in ('light','dark','high_contrast','system')),
  font_family text not null default 'Arial',
  font_size int not null default 36,
  line_spacing numeric(2,1) not null default 1.0 check (line_spacing between 1.0 and 2.0),
  punctuation_pauses boolean not null default true,
  speed_variability boolean not null default false,
  goal_wpm int not null default 600 check (goal_wpm between 50 and 5000),
  updated_at timestamptz not null default now()
);

create table if not exists public.reading_center_progress (
  user_id uuid not null references auth.users(id) on delete cascade,
  passage_id uuid not null references public.reading_center_passages(id) on delete cascade,
  word_index int not null default 0,
  completed_at timestamptz,
  last_opened_at timestamptz not null default now(),
  hidden_from_recent boolean not null default false,
  primary key (user_id, passage_id)
);

create table if not exists public.reading_center_bookmarks (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  passage_id uuid not null references public.reading_center_passages(id) on delete cascade,
  word_index int not null,
  created_at timestamptz not null default now()
);
create index if not exists reading_center_bookmarks_user_passage_idx
  on public.reading_center_bookmarks (user_id, passage_id);

create table if not exists public.reading_center_sessions (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  passage_id uuid not null references public.reading_center_passages(id) on delete cascade,
  reading_mode text not null,
  wpm int not null,
  words_read int not null,
  active_ms int not null,
  paused_ms int not null default 0,
  started_at timestamptz not null,
  ended_at timestamptz not null
);
create index if not exists reading_center_sessions_user_started_idx
  on public.reading_center_sessions (user_id, started_at desc);

alter table public.reading_center_passages    enable row level security;
alter table public.reading_center_preferences enable row level security;
alter table public.reading_center_progress    enable row level security;
alter table public.reading_center_bookmarks   enable row level security;
alter table public.reading_center_sessions    enable row level security;

-- Passages: signed-in users read published rows; admins read and write everything.
create policy "rc passages read published" on public.reading_center_passages
  for select to authenticated using (is_published or public.has_role(auth.uid(), 'admin'));
create policy "rc passages admin insert" on public.reading_center_passages
  for insert to authenticated with check (public.has_role(auth.uid(), 'admin'));
create policy "rc passages admin update" on public.reading_center_passages
  for update to authenticated using (public.has_role(auth.uid(), 'admin'))
  with check (public.has_role(auth.uid(), 'admin'));
create policy "rc passages admin delete" on public.reading_center_passages
  for delete to authenticated using (public.has_role(auth.uid(), 'admin'));

-- Per-user tables: owner full access, admins read.
create policy "rc prefs own" on public.reading_center_preferences
  for all to authenticated using (user_id = auth.uid()) with check (user_id = auth.uid());
create policy "rc prefs admin read" on public.reading_center_preferences
  for select to authenticated using (public.has_role(auth.uid(), 'admin'));

create policy "rc progress own" on public.reading_center_progress
  for all to authenticated using (user_id = auth.uid()) with check (user_id = auth.uid());
create policy "rc progress admin read" on public.reading_center_progress
  for select to authenticated using (public.has_role(auth.uid(), 'admin'));

create policy "rc bookmarks own" on public.reading_center_bookmarks
  for all to authenticated using (user_id = auth.uid()) with check (user_id = auth.uid());
create policy "rc bookmarks admin read" on public.reading_center_bookmarks
  for select to authenticated using (public.has_role(auth.uid(), 'admin'));

create policy "rc sessions own" on public.reading_center_sessions
  for all to authenticated using (user_id = auth.uid()) with check (user_id = auth.uid());
create policy "rc sessions admin read" on public.reading_center_sessions
  for select to authenticated using (public.has_role(auth.uid(), 'admin'));

-- Seed passage 1. Body uses $rc$ quoting so apostrophes need no escaping.
insert into public.reading_center_passages (slug, title, author, body, word_count, sort_order)
values (
  'living-in-a-rational-society',
  'Living in a rational society',
  null,
  $rc$PASTE_PASSAGE_HERE$rc$,
  0,
  1
)
on conflict (slug) do nothing;

-- word_count for the seed: count whitespace-separated words.
update public.reading_center_passages
set word_count = array_length(regexp_split_to_array(trim(body), '\s+'), 1)
where slug = 'living-in-a-rational-society';
```

Replace `PASTE_PASSAGE_HERE` with the three paragraphs from
`C:\Users\Joshu\dev\ai-os\research\2026-10-12-spreeder-feature-inventory.md`, section 9, starting at
"The rationalizing of society" and ending at "increasingly routinized lives." Keep the **blank line
between paragraphs** (one empty line). Copy characters exactly, including `’` and `—`. Do not include
the final line "Paragraph breaks are inferred...".

**Check:** the file contains no `PASTE_PASSAGE_HERE`; it contains exactly two blank lines inside the
`$rc$...$rc$` block (the two paragraph breaks). Commit: `reading-center: v1 migration and seed passage`.

---

## Step 3: Constants and types (`lib/constants.ts`, `lib/types.ts`)

Create `src/features/reading-center/lib/types.ts`:

```ts
export type ReadingMode = "serial" | "flow" | "highlight" | "scroll" | "ereader";
export type ReaderTheme = "light" | "dark" | "high_contrast" | "system";

export interface Passage {
  id: string;
  slug: string;
  title: string;
  author: string | null;
  body: string;
  cover_url: string | null;
  word_count: number;
  sort_order: number;
  is_published: boolean;
  created_at: string;
  updated_at: string;
}

export interface Preferences {
  wpm: number;
  reading_mode: ReadingMode;
  number_of_lines: number;
  words_per_line: number;
  center_text: boolean;
  theme: ReaderTheme;
  font_family: string;
  font_size: number;
  line_spacing: number;
  punctuation_pauses: boolean;
  speed_variability: boolean;
  goal_wpm: number;
}

export interface Progress {
  passage_id: string;
  word_index: number;
  completed_at: string | null;
  last_opened_at: string;
  hidden_from_recent: boolean;
}

export interface Bookmark {
  id: string;
  passage_id: string;
  word_index: number;
  created_at: string;
}

export interface ReadingSession {
  id: string;
  passage_id: string;
  reading_mode: ReadingMode;
  wpm: number;
  words_read: number;
  active_ms: number;
  paused_ms: number;
  started_at: string;
  ended_at: string;
}

export interface Token {
  index: number;          // position in the whole passage, starting at 0
  text: string;           // the word with its punctuation attached
  paragraphIndex: number; // starting at 0
  endsSentence: boolean;
  hasPunctuation: boolean;
  endsParagraph: boolean;
}

export interface Chunk {
  index: number;          // chunk number, starting at 0
  startWord: number;      // token index of the first word
  endWord: number;        // token index of the last word (inclusive)
  rows: Token[][];        // numberOfLines rows, each up to wordsPerLine tokens
}
```

Create `src/features/reading-center/lib/constants.ts`:

```ts
import type { Preferences, ReadingMode, ReaderTheme } from "./types";

export const DEFAULT_PREFERENCES: Preferences = {
  wpm: 200,
  reading_mode: "serial",
  number_of_lines: 1,
  words_per_line: 1,
  center_text: true,
  theme: "system",
  font_family: "Arial",
  font_size: 36,
  line_spacing: 1.0,
  punctuation_pauses: true,
  speed_variability: false,
  goal_wpm: 600,
};

export const WPM_MIN = 50;
export const WPM_MAX = 5000;
export const LINES_MIN = 1;
export const LINES_MAX = 6;
export const WORDS_PER_LINE_MIN = 1;
export const WORDS_PER_LINE_MAX = 6;
export const LINE_SPACING_MIN = 1.0;
export const LINE_SPACING_MAX = 2.0;
export const LINE_SPACING_STEP = 0.1;

export const READING_MODES: { value: ReadingMode; label: string }[] = [
  { value: "serial", label: "Serial" },
  { value: "flow", label: "Flow" },
  { value: "highlight", label: "Highlight" },
  { value: "scroll", label: "Scroll" },
  { value: "ereader", label: "e-Reader" },
];

export const THEMES: { value: ReaderTheme; label: string }[] = [
  { value: "light", label: "Light" },
  { value: "dark", label: "Dark" },
  { value: "high_contrast", label: "High Contrast" },
  { value: "system", label: "System" },
];

/** Font label shown in the menu -> CSS font-family stack. */
export const FONTS: { label: string; stack: string }[] = [
  { label: "Arial", stack: "Arial, Helvetica, sans-serif" },
  { label: "Times New Roman", stack: "'Times New Roman', Times, serif" },
  { label: "Verdana", stack: "Verdana, Geneva, sans-serif" },
  { label: "Calibri", stack: "Calibri, Carlito, sans-serif" },
  { label: "Microsoft Sans Serif", stack: "'Microsoft Sans Serif', Tahoma, sans-serif" },
  { label: "Impact", stack: "Impact, 'Arial Black', sans-serif" },
  { label: "Lucida Console", stack: "'Lucida Console', Monaco, monospace" },
  { label: "Comic Sans MS", stack: "'Comic Sans MS', 'Comic Sans', cursive" },
  { label: "Georgia", stack: "Georgia, serif" },
  { label: "Palatino Linotype", stack: "'Palatino Linotype', Palatino, 'Book Antiqua', serif" },
  { label: "Tahoma", stack: "Tahoma, Geneva, sans-serif" },
  { label: "Trebuchet MS", stack: "'Trebuchet MS', Helvetica, sans-serif" },
  { label: "Courier New", stack: "'Courier New', Courier, monospace" },
  { label: "OpenDyslexic", stack: "OpenDyslexic, 'Comic Sans MS', sans-serif" },
  { label: "Antikor", stack: "Antikor, Georgia, serif" },
  { label: "Code New Roman", stack: "'Code New Roman', 'Courier New', monospace" },
  { label: "CQ Mono", stack: "'CQ Mono', 'Courier New', monospace" },
  { label: "Pointfree", stack: "Pointfree, 'Courier New', monospace" },
  { label: "Fira Mono", stack: "'Fira Mono', 'Courier New', monospace" },
];

export const FONT_SIZES = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 28, 32, 36, 40, 44, 50, 56, 62, 68, 74];

/** Pause multipliers, applied only when a chunk is exactly one word. */
export const PAUSE_SENTENCE = 2.0;
export const PAUSE_PUNCTUATION = 1.5;
export const PAUSE_PARAGRAPH = 2.5;

/** Speed variability clamp. */
export const VARIABILITY_MIN = 0.75;
export const VARIABILITY_MAX = 1.5;

export const STAT_PERIODS = [
  { value: "24h", label: "24 Hours", ms: 24 * 3600_000 },
  { value: "7d", label: "7 Days", ms: 7 * 86400_000 },
  { value: "14d", label: "14 Days", ms: 14 * 86400_000 },
  { value: "30d", label: "30 Days", ms: 30 * 86400_000 },
  { value: "6m", label: "6 Months", ms: 182 * 86400_000 },
] as const;

/** Theme colours. High Contrast is fixed; the others use app tokens via classes. */
export const THEME_CLASSES: Record<Exclude<ReaderTheme, "system">, string> = {
  light: "bg-white text-zinc-900",
  dark: "bg-black text-white",
  high_contrast: "bg-black text-[#FFFF00]",
};
```

Do not add webfont files. Fonts not installed on the device fall back to the stack. (The reviewer may add
webfonts later.)

**Check:** `npm run typecheck` passes. Commit: `reading-center: types and constants`.

---

## Step 4: Database helper (`lib/db.ts`)

Create `src/features/reading-center/lib/db.ts`:

```ts
import { supabase } from "@/integrations/supabase/client";

/**
 * The generated Supabase types do not include reading_center_* tables yet.
 * This helper is the ONLY place that casts. Remove it after types are regenerated.
 */
// eslint-disable-next-line @typescript-eslint/no-explicit-any
export const rcDb = (table: string) => (supabase as any).from(table);
```

**Check:** typecheck passes. Commit: `reading-center: db helper`.

---

## Step 5: Tokenizer (`lib/tokenize.ts`) and its tests

Create `src/features/reading-center/lib/tokenize.ts` exactly:

```ts
import type { Chunk, Token } from "./types";

const SENTENCE_END = /[.!?]["'’”)\]]*$/;
const OTHER_PUNCT = /[,;:—–)\]]["'’”]*$/;

/** Split text into paragraphs: one or more blank lines separate paragraphs. */
export function splitParagraphs(body: string): string[] {
  return body
    .replace(/\r\n/g, "\n")
    .split(/\n\s*\n/)
    .map((p) => p.trim())
    .filter((p) => p.length > 0);
}

export function tokenize(body: string): Token[] {
  const tokens: Token[] = [];
  const paragraphs = splitParagraphs(body);
  paragraphs.forEach((para, paragraphIndex) => {
    const words = para.split(/\s+/).filter((w) => w.length > 0);
    words.forEach((text, i) => {
      const endsSentence = SENTENCE_END.test(text);
      tokens.push({
        index: tokens.length,
        text,
        paragraphIndex,
        endsSentence,
        hasPunctuation: !endsSentence && OTHER_PUNCT.test(text),
        endsParagraph: i === words.length - 1,
      });
    });
  });
  return tokens;
}

export function countWords(body: string): number {
  return tokenize(body).length;
}

/**
 * Group tokens into chunks of up to wordsPerLine * numberOfLines words.
 * A chunk never crosses a paragraph boundary.
 */
export function chunkTokens(tokens: Token[], wordsPerLine: number, numberOfLines: number): Chunk[] {
  const size = Math.max(1, wordsPerLine) * Math.max(1, numberOfLines);
  const chunks: Chunk[] = [];
  let current: Token[] = [];
  const flush = () => {
    if (current.length === 0) return;
    const rows: Token[][] = [];
    for (let i = 0; i < current.length; i += wordsPerLine) rows.push(current.slice(i, i + wordsPerLine));
    chunks.push({
      index: chunks.length,
      startWord: current[0].index,
      endWord: current[current.length - 1].index,
      rows,
    });
    current = [];
  };
  for (const t of tokens) {
    current.push(t);
    if (current.length === size || t.endsParagraph) flush();
  }
  flush();
  return chunks;
}

/** Index of the chunk that contains wordIndex. Returns 0 if not found. */
export function chunkIndexForWord(chunks: Chunk[], wordIndex: number): number {
  const i = chunks.findIndex((c) => wordIndex >= c.startWord && wordIndex <= c.endWord);
  return i === -1 ? 0 : i;
}

/** Normalise a passage title into a URL slug. */
export function slugify(title: string): string {
  return title
    .toLowerCase()
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}
```

Create `src/features/reading-center/lib/tokenize.test.ts`:

```ts
import { describe, expect, it } from "vitest";
import { chunkIndexForWord, chunkTokens, slugify, splitParagraphs, tokenize } from "./tokenize";

const BODY = "One two, three. Four?\n\nFive six seven.";

describe("tokenize", () => {
  it("splits paragraphs on blank lines", () => {
    expect(splitParagraphs(BODY)).toEqual(["One two, three. Four?", "Five six seven."]);
  });
  it("numbers words across the whole passage", () => {
    const t = tokenize(BODY);
    expect(t.map((x) => x.index)).toEqual([0, 1, 2, 3, 4, 5, 6]);
    expect(t[4].paragraphIndex).toBe(1);
  });
  it("flags punctuation", () => {
    const t = tokenize(BODY);
    expect(t[1].hasPunctuation).toBe(true);   // two,
    expect(t[2].endsSentence).toBe(true);     // three.
    expect(t[3].endsSentence).toBe(true);     // Four?
    expect(t[3].endsParagraph).toBe(true);
    expect(t[0].hasPunctuation).toBe(false);
  });
  it("treats a closing quote or bracket after a full stop as a sentence end", () => {
    expect(tokenize("He left.)")[1].endsSentence).toBe(true);
    expect(tokenize("home.’")[0].endsSentence).toBe(true);
  });
});

describe("chunkTokens", () => {
  it("never crosses a paragraph", () => {
    const c = chunkTokens(tokenize(BODY), 3, 1);
    expect(c.map((x) => [x.startWord, x.endWord])).toEqual([[0, 2], [3, 3], [4, 6]]);
  });
  it("lays a chunk out in rows", () => {
    const c = chunkTokens(tokenize(BODY), 2, 2);
    expect(c[0].rows.map((r) => r.map((t) => t.text))).toEqual([["One", "two,"], ["three.", "Four?"]]);
  });
  it("finds the chunk for a word", () => {
    const c = chunkTokens(tokenize(BODY), 3, 1);
    expect(chunkIndexForWord(c, 5)).toBe(2);
    expect(chunkIndexForWord(c, 99)).toBe(0);
  });
});

describe("slugify", () => {
  it("makes URL-safe slugs", () => {
    expect(slugify("Living in a rational society")).toBe("living-in-a-rational-society");
    expect(slugify("  Café: Notes!! ")).toBe("cafe-notes");
  });
});
```

**Check:** `npx vitest run src/features/reading-center/lib/tokenize.test.ts` passes (all green).
Commit: `reading-center: tokenizer with tests`.

---

## Step 6: Timing (`lib/timing.ts`) and its tests

Create `src/features/reading-center/lib/timing.ts` exactly:

```ts
import type { Chunk, Preferences } from "./types";
import {
  PAUSE_PARAGRAPH, PAUSE_PUNCTUATION, PAUSE_SENTENCE, VARIABILITY_MAX, VARIABILITY_MIN,
} from "./constants";

export function msPerWord(wpm: number): number {
  return 60000 / wpm;
}

/** Pause multiplier for a one-word chunk. Returns 1 for multi-word chunks or when pauses are off. */
function pauseFactor(chunk: Chunk, pausesOn: boolean): number {
  const words = chunk.endWord - chunk.startWord + 1;
  if (!pausesOn || words !== 1) return 1;
  const t = chunk.rows[0][0];
  if (t.endsParagraph) return PAUSE_PARAGRAPH;
  if (t.endsSentence) return PAUSE_SENTENCE;
  if (t.hasPunctuation) return PAUSE_PUNCTUATION;
  return 1;
}

function chunkChars(chunk: Chunk): number {
  return chunk.rows.flat().reduce((n, t) => n + t.text.replace(/[^\p{L}\p{N}]/gu, "").length, 0);
}

/**
 * Display duration (ms) for every chunk, in order.
 * Speed variability: longer chunks get more time, shorter get less, clamped, then rescaled so the
 * total equals the no-variability total.
 */
export function chunkDurations(
  chunks: Chunk[],
  prefs: Pick<Preferences, "wpm" | "punctuation_pauses" | "speed_variability">,
): number[] {
  const base = msPerWord(prefs.wpm);
  const plain = chunks.map((c) => (c.endWord - c.startWord + 1) * base * pauseFactor(c, prefs.punctuation_pauses));
  if (!prefs.speed_variability || chunks.length === 0) return plain;

  const totalWords = chunks.reduce((n, c) => n + (c.endWord - c.startWord + 1), 0);
  const totalChars = chunks.reduce((n, c) => n + chunkChars(c), 0);
  const avgChars = totalChars / Math.max(1, totalWords);
  const varied = chunks.map((c, i) => {
    const words = c.endWord - c.startWord + 1;
    const raw = avgChars > 0 ? chunkChars(c) / (words * avgChars) : 1;
    const factor = Math.min(VARIABILITY_MAX, Math.max(VARIABILITY_MIN, raw));
    return plain[i] * factor;
  });
  const plainTotal = plain.reduce((a, b) => a + b, 0);
  const variedTotal = varied.reduce((a, b) => a + b, 0);
  const scale = variedTotal > 0 ? plainTotal / variedTotal : 1;
  return varied.map((d) => d * scale);
}

/** Milliseconds left from the start of chunk `fromChunk` to the end. */
export function remainingMs(durations: number[], fromChunk: number): number {
  let sum = 0;
  for (let i = Math.max(0, fromChunk); i < durations.length; i++) sum += durations[i];
  return sum;
}

/** "N minutes remaining", "1 minute remaining" or "Less than a minute remaining". */
export function formatRemaining(ms: number): string {
  if (ms < 60000) return "Less than a minute remaining";
  const m = Math.ceil(ms / 60000);
  return m === 1 ? "1 minute remaining" : `${m} minutes remaining`;
}

/** Whole-number percent of words read, 0 to 100. */
export function percentRead(wordIndex: number, totalWords: number): number {
  if (totalWords <= 0) return 0;
  return Math.min(100, Math.max(0, Math.floor((wordIndex / totalWords) * 100)));
}

/** Effective WPM for a session. Returns 0 if no active time. */
export function effectiveWpm(wordsRead: number, activeMs: number): number {
  if (activeMs <= 0) return 0;
  return Math.round(wordsRead / (activeMs / 60000));
}

/** Estimated whole minutes to read `words` at `wpm`, at least 1. */
export function estimateMinutes(words: number, wpm: number): number {
  return Math.max(1, Math.round(words / wpm));
}
```

Create `src/features/reading-center/lib/timing.test.ts`:

```ts
import { describe, expect, it } from "vitest";
import { tokenize, chunkTokens } from "./tokenize";
import { chunkDurations, effectiveWpm, formatRemaining, percentRead, remainingMs } from "./timing";

const words300 = Array.from({ length: 300 }, (_, i) => `word${i}`).join(" ");

describe("chunkDurations", () => {
  it("300 words at 300 WPM, no pauses, takes 60 seconds", () => {
    const c = chunkTokens(tokenize(words300), 1, 1);
    const d = chunkDurations(c, { wpm: 300, punctuation_pauses: false, speed_variability: false });
    expect(d.reduce((a, b) => a + b, 0)).toBeCloseTo(60000, 0);
  });
  it("adds pauses only for one-word chunks", () => {
    const body = "Stop. Go now";
    const one = chunkDurations(chunkTokens(tokenize(body), 1, 1), { wpm: 60, punctuation_pauses: true, speed_variability: false });
    expect(one[0]).toBe(2000); // sentence end x2 at 1000 ms/word
    const two = chunkDurations(chunkTokens(tokenize(body), 2, 1), { wpm: 60, punctuation_pauses: true, speed_variability: false });
    expect(two[0]).toBe(2000); // two words, no pause multiplier
  });
  it("variability keeps the same total within 1%", () => {
    const body = "a extraordinarily b incomprehensibility c d e f";
    const c = chunkTokens(tokenize(body), 1, 1);
    const off = chunkDurations(c, { wpm: 200, punctuation_pauses: false, speed_variability: false });
    const on = chunkDurations(c, { wpm: 200, punctuation_pauses: false, speed_variability: true });
    const sum = (x: number[]) => x.reduce((a, b) => a + b, 0);
    expect(Math.abs(sum(on) - sum(off)) / sum(off)).toBeLessThan(0.01);
    expect(on[1]).toBeGreaterThan(on[0]); // long word gets more time
  });
});

describe("helpers", () => {
  it("formats remaining time", () => {
    expect(formatRemaining(30000)).toBe("Less than a minute remaining");
    expect(formatRemaining(60000)).toBe("1 minute remaining");
    expect(formatRemaining(150000)).toBe("3 minutes remaining");
  });
  it("percent and remaining", () => {
    expect(percentRead(55, 550)).toBe(10);
    expect(remainingMs([100, 200, 300], 1)).toBe(500);
  });
  it("effective wpm", () => {
    expect(effectiveWpm(300, 60000)).toBe(300);
    expect(effectiveWpm(10, 0)).toBe(0);
  });
});
```

**Check:** `npx vitest run src/features/reading-center/lib` passes. Commit:
`reading-center: timing engine with tests`.

---

## Step 7: Data hooks (`hooks/useReadingCenterData.ts`)

Create `src/features/reading-center/hooks/useReadingCenterData.ts`. Use `@tanstack/react-query` and
`useAuth` from `@/contexts/AuthContext` (it returns `{ user }`; `user.id` is the user id).

Write these exports. Every query key starts with `"reading-center"`. Every function that writes must
call `queryClient.invalidateQueries({ queryKey: [...] })` for the keys it changes.

| Export | Kind | Does |
|---|---|---|
| `usePassages()` | query `["reading-center","passages"]` | `rcDb("reading_center_passages").select("*").order("sort_order").order("title")`. Returns `Passage[]`. |
| `usePassageBySlug(slug)` | query `["reading-center","passage",slug]` | select `*` where `slug = slug`, `.maybeSingle()`. |
| `usePreferences()` | query `["reading-center","prefs",userId]` | select `*` where `user_id = userId`, `.maybeSingle()`. If no row, return `DEFAULT_PREFERENCES`. Otherwise merge: `{ ...DEFAULT_PREFERENCES, ...row, line_spacing: Number(row.line_spacing) }`. |
| `useSavePreferences()` | mutation | input `Partial<Preferences>`. Upsert `{ user_id, ...current, ...input, updated_at: new Date().toISOString() }` with `onConflict: "user_id"`. Before the request, set the query cache to the merged value so the UI updates instantly (`queryClient.setQueryData`). |
| `useProgressList()` | query `["reading-center","progress",userId]` | select `*` where `user_id = userId`. |
| `useSaveProgress()` | mutation | input `{ passage_id, word_index, completed?: boolean, hidden_from_recent?: boolean }`. Upsert with `onConflict: "user_id,passage_id"`, always set `last_opened_at` to now; set `completed_at` to now only when `completed === true`. |
| `useBookmarks(passageId)` | query `["reading-center","bookmarks",userId,passageId]` | select `*` where user and passage, order `created_at` desc. |
| `useAddBookmark()` / `useDeleteBookmark()` | mutations | insert `{ user_id, passage_id, word_index }` / delete by `id`. |
| `useSessions(sinceIso)` | query `["reading-center","sessions",userId,sinceIso]` | select `*` where user and `started_at >= sinceIso`, order `started_at` asc. |
| `useRecordSession()` | mutation | insert one `reading_center_sessions` row (all columns except id). |
| `useUpsertPassage()` / `useDeletePassage()` / `useReorderPassages()` | mutations (admin) | upsert by `id` (or insert when no id), with `word_count = countWords(body)` and `updated_at = now`; delete by id; reorder = for each `{id, sort_order}` run an update. |

Rules:
- Every query: `enabled: !!userId` (except passages, which need only a signed-in user, same rule).
- If a Supabase call returns `error`, `throw error`. Do not swallow errors.
- Never call `supabase.from` directly. Use `rcDb("table_name")`.

**Check:** typecheck passes. Commit: `reading-center: data hooks`.

---

## Step 8: Reading clock (`hooks/useReadingClock.ts`)

Create `src/features/reading-center/hooks/useReadingClock.ts`.

Signature:
```ts
export function useReadingClock(args: {
  durations: number[];        // from chunkDurations
  chunkCount: number;
  initialChunk: number;
  onChunkChange: (chunk: number) => void;
  onFinish: () => void;
}): {
  playing: boolean;
  chunk: number;
  play: () => void;
  pause: () => void;
  toggle: () => void;
  goTo: (chunk: number) => void;   // clamps to 0..chunkCount-1, keeps playing state
  next: () => void;
  prev: () => void;
  restart: () => void;             // goTo(0) and pause
  activeMs: () => number;          // total ms spent playing since mount
  pausedMs: () => number;          // total ms spent paused since the first play
};
```

Implementation rules (follow exactly):
1. Keep `chunk` in `useState` **and** mirror it in a `useRef` (`chunkRef`). Keep `durations`,
   `onChunkChange`, `onFinish` in refs updated by a `useEffect` each render. The animation loop reads
   only refs, never state, so it never restarts because of a re-render.
2. Use `requestAnimationFrame`. Store `elapsedInChunk` (ms) in a ref. Each frame: `delta = now - lastFrame`;
   add `delta` to `elapsedInChunk` and to the active-time ref; while `elapsedInChunk >= durations[chunk]`,
   subtract that duration and advance one chunk. If the chunk passes the last one, stop playing, call
   `onFinish()`, and leave `chunk` on the last chunk.
3. Cap `delta` at 1000 ms so returning to a background tab does not jump far ahead.
4. `pause` cancels the frame and records when the pause started (for `pausedMs`). `play` sets `lastFrame`
   to `performance.now()` before requesting the first frame.
5. `goTo` sets `elapsedInChunk = 0`.
6. Cancel the animation frame on unmount.
7. Call `onChunkChange(newChunk)` every time the chunk changes, from any cause.

**Check:** typecheck passes. Commit: `reading-center: reading clock`.

---

## Step 9: Theme wrapper (`components/ReaderSurface.tsx`)

Create a component `ReaderSurface({ prefs, children, className })` that:
- Resolves `theme === "system"` with `window.matchMedia("(prefers-color-scheme: dark)").matches`
  ("dark" if true, else "light"); listen for changes with `addEventListener("change", ...)` and clean up.
- Renders a `div` with `min-h-screen w-full` plus `THEME_CLASSES[resolved]` plus `className`.
- Sets inline style `fontFamily` to the matching `FONTS` stack (fallback to the Arial stack if not found),
  `fontSize: prefs.font_size`, `lineHeight: prefs.line_spacing`.
- Exposes the resolved theme through a `data-theme` attribute (`light`, `dark`, `high_contrast`).

**Check:** typecheck passes. Commit: `reading-center: reader surface theming`.

---

## Step 10: The five mode renderers (`components/modes/`)

Every mode component receives the same props:

```ts
export interface ModeProps {
  tokens: Token[];
  chunks: Chunk[];
  chunk: number;              // current chunk index
  prefs: Preferences;
  playing: boolean;
  onWordClick: (wordIndex: number) => void; // used for jump and bookmarks
}
```

Put `ModeProps` in `components/modes/types.ts`.

**Font rule (applies to every mode, the View panel body and the Sample Text preview):** the passage text
element must use `style={READING_TEXT_STYLE}` (import from `../ReaderSurface`). Never set the reading font
size anywhere else, and never apply it to the top bar, bottom bar, buttons or dialogs. For the Sample Text
preview in the preferences dialog, set the inline style from the chosen font stack and size directly.

Then create:

### 10a. `SerialMode.tsx`
- Show only `chunks[chunk].rows`. Each row is one line: the words joined by a space.
- Container: flex column, vertically centred in the stage (`flex-1 flex items-center`).
- If `prefs.center_text` then `text-center justify-center items-center`, else left-aligned with
  `pl-[15%]`.
- When `playing` is false, each word is a `<button>` (no visible button styling, `cursor-pointer`)
  that calls `onWordClick(token.index)`.

### 10b. `FlowMode.tsx`
- Build "lines": group all tokens into rows of `prefs.words_per_line` tokens, never crossing a
  paragraph (reuse `chunkTokens(tokens, prefs.words_per_line, 1)`; each chunk is one line).
- Show only the current line's words at the position they would sit: render the **whole current line**
  but give every word outside the current chunk `opacity-0` (invisible, still takes space). The current
  chunk's words are fully visible. Left-aligned with `pl-[15%]`.
- Clickable words when paused, same as Serial.

### 10c. `HighlightMode.tsx`
- Render the whole passage. Group tokens into rows of `prefs.words_per_line` words (same grouping as
  Flow). Each row is a block line.
- Words with `index` between `chunks[chunk].startWord` and `chunks[chunk].endWord` (inclusive) have
  full opacity and `font-semibold`; every other word has `opacity-35` (use `style={{ opacity: 0.35 }}`).
- Paragraphs are separated by a gap (`mb-6` on the last row of each paragraph).
- Keep the current chunk vertically centred: give the first word of the current chunk a ref and, when
  `chunk` changes, call `ref.scrollIntoView({ block: "center", behavior: prefs.wpm > 600 ? "auto" : "smooth" })`.
- All words clickable at all times when paused.

### 10d. `ScrollMode.tsx`
- Same row layout as Highlight, inside a container with `overflow-hidden` and a fixed height (`h-[70vh]`).
- Draw a thin horizontal guide line at 40% of the container height (absolute positioned,
  `border-t border-current opacity-30`).
- Translate the inner column with CSS `transform: translateY(...)` so the row containing the current
  chunk's first word sits on the guide line. Use `transition: transform 150ms linear`. Measure the row's
  `offsetTop` with a ref on the row element.
- The current chunk's words are full opacity; others `0.6`.
- Clickable words when paused.

### 10e. `EReaderMode.tsx`
- No timer. Props additionally: `page: number`, `onPageCountChange(n)`, `onPageChange(n)`,
  `searchQuery: string`.
- Render paragraphs as normal `<p>` elements inside a column `max-w-[46rem] mx-auto px-6`.
- Pagination: put the text in a container with fixed height `calc(100vh - 140px)` and CSS columns:
  `columnWidth` = container width, `columnGap: 48px`, `height` fixed. Measure `scrollWidth / (width + 48)`
  rounded up = page count; call `onPageCountChange`. Show page `p` by setting
  `scrollLeft = p * (width + 48)` on the container (overflow hidden). Re-measure on resize and when
  font, size or spacing change.
- If `searchQuery` is non-empty: wrap matching text (case-insensitive) in `<mark>`; when the query
  changes, jump to the page containing the first match (find the first `<mark>` element, compute its
  `offsetLeft`, page = `Math.floor(offsetLeft / (width + 48))`).
- Words are clickable (for bookmarks): wrap each token in a `<span data-word={index}>` and handle
  clicks on the paragraph with event delegation reading `data-word`.

Create `components/modes/index.tsx` exporting a `ModeRenderer` that switches on `prefs.reading_mode`
and renders the matching component.

**Check:** typecheck passes. Commit: `reading-center: five reading modes`.

---

## Step 11: Reader dialogs and panels (`components/`)

Use shadcn `Dialog`, `Tabs`, `Select`, `Slider`, `Switch`, `Tooltip`, `Popover`, `Input`, `Button` from
`@/components/ui/*`. Open each file in `src/components/ui/` first to see its exact export names.

### 11a. `WpmDialog.tsx`
Props: `open, onOpenChange, value, onSave(v)`. Title "Reading Speed (WPM)". Local state starts at
`value` whenever the dialog opens. Big centred number. Left column buttons "-10", "-100"; right column
"+10", "+100". Each clamps to `WPM_MIN..WPM_MAX`. Footer: "Cancel" (closes, discards) and "Save"
(calls `onSave(local)` then closes).

### 11b. `PreferencesDialog.tsx`
Props: `open, onOpenChange, prefs, onChange(partial)`. Title "Preferences".
- If `prefs.reading_mode === "ereader"`: **no tabs**. Show: Reading Mode select, Theme select, Font select
  + Size select on one row, a "Sample Text" preview (rendered in the chosen font and size), and a
  Line Spacing slider (1.0 to 2.0, step 0.1, value shown at right).
- Otherwise tabs **Spreed**, **Appearance**, **Advanced**:
  - Spreed: Reading Mode select, then by mode:
    - serial: "Number of Lines" slider 1–6, "Words Per Line" slider 1–6, "Center Text" switch.
    - flow: "Words Per Line" slider 1–6.
    - highlight: "Words Per Line" slider 1–6, "Number of Lines" slider 1–6.
    - scroll: "Words Per Line" slider 1–6.
  - Appearance: Theme select, Font select + Size select, "Sample Text" preview. This tab must show its
    controls in every mode.
  - Advanced: "Punctuation Pauses" switch with a "?" tooltip: "Slight pause at the end of sentences and
    punctuation marks. Only works with one word at a time." "Speed Variability" switch with tooltip:
    "Gives longer words a little more time and shorter words a little less, at the same overall speed."
- Each slider shows its label at the bottom left and the current value at the bottom right.
- Each font option in the Font select renders in its own font (`style={{ fontFamily: stack }}`).
- Footer button "Restore Defaults": opens a confirm (`AlertDialog`) "Restore all reading settings to
  their defaults?" with "Cancel" / "Restore". On Restore call `onChange({ ...DEFAULT_PREFERENCES,
  goal_wpm: prefs.goal_wpm })` (keep the goal).
- Every change calls `onChange` immediately (live preview). The parent debounces saving (step 12).

### 11c. `ViewPanel.tsx`
Props: `open, onOpenChange, title, tokens, currentWord, wpm, remainingText, onJump(wordIndex), onPlay()`.
Full-screen overlay (Dialog with `max-w-none w-screen h-screen`). Shows: title, a small badge
"Passage", a search input "Search this text...". Body: paragraphs of clickable words; the current word
has a 2px outline in the primary colour; words matching the search (case-insensitive, punctuation
ignored) get a yellow background. Clicking a word calls `onJump(index)` and closes. A round play button
calls `onPlay()` and closes. Footer text: `${remainingText} - ${wpm} WPM` but replace "remaining" with
"to go" (e.g. "3 minutes to go - 200 WPM"). Esc closes.

### 11d. `BookmarksDialog.tsx`
Props: `open, onOpenChange, bookmarks, tokens, onJump(wordIndex), onDelete(id)`. Title "Bookmarks".
Each row: a snippet of up to 6 words before and 6 after the bookmarked word with that word bold, the
date (`toLocaleDateString()`), a jump on click, and a trash icon button (`aria-label="Delete bookmark"`)
that calls `onDelete`. Empty state: a list icon, heading "No bookmarks yet", text "To add one, pause
and click any word."

### 11e. `ShortcutsPopover.tsx`
A `Popover` triggered by a keyboard icon button (`aria-label="Keyboard shortcuts"`). Content title
"Keyboard Shortcuts" and this table:

| Keys | Label |
|---|---|
| ↑ / ↓ or + / − | increase or decrease speed |
| P or Space | pause / resume |
| → | section forward |
| ← | section back |
| R | restart |
| S | settings |

### 11f. `CompletionCard.tsx`
Props: `wordsRead, activeMs, onReadAgain, onBack`. Shows "Passage complete", words read, time
(m:ss from activeMs), effective WPM (`effectiveWpm`), buttons "Read again" and "Back to library".

### 11g. `ResumePrompt.tsx`
Small dialog: "Pick up where you left off?" Buttons "Resume" and "Start over".

**Check:** typecheck passes. Commit: `reading-center: reader dialogs and panels`.

---

## Step 12: Reader page (`pages/ReaderPage.tsx`)

Route param `slug` (`useParams`). Steps inside the component, in this order:

1. Load `usePassageBySlug(slug)`, `usePreferences()`, `useProgressList()`, `useBookmarks(passage?.id)`.
   While loading show a centred spinner. If the passage is not found show "Passage not found" and a
   link back to `/reading-center`.
2. `tokens = useMemo(() => tokenize(passage.body), [passage.body])`.
3. Keep `prefs` in local state initialised from the query. `updatePrefs(partial)` sets local state
   immediately and calls `useSavePreferences().mutate(partial)` debounced by 500 ms (use a ref holding a
   `setTimeout` id; merge pending partials).
4. Keep the current **word index** in a ref and state (`wordIndex`). This is the single source of truth
   for position.
5. `chunks = useMemo(() => chunkTokens(tokens, prefs.words_per_line, prefs.reading_mode === "serial" ||
   prefs.reading_mode === "highlight" ? prefs.number_of_lines : 1), [...])`.
6. `durations = useMemo(() => chunkDurations(chunks, prefs), [chunks, prefs.wpm,
   prefs.punctuation_pauses, prefs.speed_variability])`.
7. `useReadingClock({ durations, chunkCount: chunks.length, initialChunk: chunkIndexForWord(chunks,
   wordIndex), onChunkChange: c => setWordIndex(chunks[c].startWord), onFinish })`.
   When `chunks` changes (settings change), call `clock.goTo(chunkIndexForWord(chunks, wordIndexRef.current))`
   so the reader keeps their place.
8. Resume: on first load, if saved progress for this passage has `word_index > 0` and no `completed_at`,
   show `ResumePrompt`. Resume sets the word index to the saved value; Start over sets 0.
9. Save progress: debounce 2 s after every `wordIndex` change, and immediately on pause, on finish and on
   unmount: `useSaveProgress().mutate({ passage_id, word_index })`.
10. Record a session (`useRecordSession`) when: the user pauses after at least 5000 ms of active time
    since the last recorded session, on finish, and on unmount if active time ≥ 5000 ms. Fields:
    `words_read` = words advanced during that stretch, `active_ms`, `paused_ms`, `wpm`, `reading_mode`,
    `started_at`, `ended_at`. Reset the stretch counters after recording.
11. `onFinish`: pause, save progress with `completed: true`, record the session, show `CompletionCard`.
    "Read again" sets word 0 and hides the card; "Back to library" navigates to `/reading-center`.
12. Layout:
    - Wrap everything in `ReaderSurface`.
    - Top bar (`h-14 flex items-center px-4`): left a "Back" button (arrow icon + "Back") to
      `/reading-center`; centre the passage title; right icon buttons in this order: Search (only in
      e-Reader; toggles an input in the top bar that sets `searchQuery`), Fullscreen, Bookmarks, Settings.
      Every icon button has an `aria-label`.
    - Stage: `ModeRenderer` (flex-1).
    - Transport (hidden in e-Reader): previous-chunk button (`aria-label="Previous"`), a large round
      play/pause button (`aria-label` "Play" or "Pause"), next-chunk button (`aria-label="Next"`).
    - Bottom bar (`h-12 border-t`): left `ShortcutsPopover`; centre a WPM button showing a gauge icon and
      the number (opens `WpmDialog`) and a "View" button (opens `ViewPanel`); right the text
      `${percentRead}% - ${formatRemaining(remainingMs(durations, clock.chunk))}`.
    - e-Reader bottom bar instead: a page `Slider` (0..pageCount-1), "n / total", previous/next page
      buttons.
13. Fullscreen: `document.documentElement.requestFullscreen()` / `document.exitFullscreen()`; track
    `document.fullscreenElement` with a `fullscreenchange` listener; swap the icon (Maximize / Minimize
    from lucide-react).
14. Bookmarks: `onWordClick(index)` from a mode: if playing, do nothing in Serial/Flow and jump in
    Highlight/Scroll. If paused, add a bookmark at that index and show a toast "Bookmark added" (use the
    app's existing toast: search `src/components/ui/` for `sonner` or `use-toast` and use whichever
    exists). In e-Reader, clicking a word adds a bookmark.
15. Keyboard: one `keydown` listener on `window`. Ignore events when `event.target` is an `input`,
    `textarea`, `select` or has `contenteditable`. Also ignore when any dialog is open. Map:
    - `ArrowUp` or `+` or `=`: wpm +10 (clamped), save.
    - `ArrowDown` or `-`: wpm −10 (clamped), save.
    - `p`/`P` or `" "` (Space): toggle play; call `event.preventDefault()` for Space.
    - `ArrowRight`: next chunk (e-Reader: next page). `ArrowLeft`: previous chunk (e-Reader: previous page).
    - `r`/`R`: restart. `s`/`S`: open settings.
16. Mode switch keeps the word: changing `reading_mode` only changes `prefs`; step 7 re-snaps the chunk.

**Check:** typecheck passes. Commit: `reading-center: reader page`.

---

## Step 13: Library page (`pages/LibraryPage.tsx`)

1. Title "Reading Center" (h1) and a search `Input` placeholder "Search passages" that filters by title
   and author (case-insensitive).
2. Load `usePassages()`, `useProgressList()`, `usePreferences()`.
3. Section **Continue reading**: passages with progress `word_index > 0`, no `completed_at`,
   `hidden_from_recent` false, sorted by `last_opened_at` newest first. Hide the section if empty.
4. Section **All passages**: every published passage in `sort_order`.
5. Card (`components/PassageCard.tsx`): a 3:4 cover tile (image if `cover_url`, else a coloured tile
   with a `FileText` icon), title (2 lines max, `line-clamp-2`), author if present, a meta line
   `${word_count} words · ${estimateMinutes(word_count, prefs.wpm)} min`, a progress bar if started,
   a check icon if completed. Whole card links to `/reading-center/${slug}`.
6. Card ⋮ menu (`DropdownMenu`): "Open", "View text" (opens `ViewPanel` read-only, jump disabled),
   "Hide from Continue reading" (only when shown in that section; calls `useSaveProgress` with
   `hidden_from_recent: true`).
7. Grid: `grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-4`.
8. A link/button "Stats" in the header to `/reading-center/stats`. For admins (`useUserPermissions().is_admin`)
   also a "Manage passages" link to `/admin/reading-center`.
9. Empty state when no passages: "No passages yet."

**Check:** typecheck passes. Commit: `reading-center: library page`.

---

## Step 14: Stats page (`pages/StatsPage.tsx`)

1. Header "Your reading" and a "Set goal" button.
2. Period select using `STAT_PERIODS` (default 30 Days). `sinceIso = new Date(Date.now() - ms).toISOString()`.
3. Load `useSessions(sinceIso)` and `usePreferences()`.
4. **Vital stats**: two semicircle gauges built with recharts `PieChart` (startAngle 180, endAngle 0,
   range 0–2000): "Current Speed" = median `effectiveWpm` of the last 5 sessions (0 if none), and
   "Target Speed" = `prefs.goal_wpm`. Show the number under each gauge.
5. Metric select: "Reading Speed", "Reading Focus", "Training Time". One recharts `ResponsiveContainer`
   chart below:
   - Reading Speed: `LineChart`, x = session date, y = effective WPM.
   - Reading Focus: `BarChart`, x = day, y = `active_ms / (active_ms + paused_ms) * 100` averaged per day (%).
   - Training Time: `BarChart`, x = day, y = sum of `active_ms` per day in minutes.
6. Empty state when there are no sessions: a chart icon, "Not enough data yet", "Read a few passages and
   come back."
7. **Goal dialog** (`components/GoalDialog.tsx`): slider 50–5000 step 50, value shown, text "The average
   reader manages about 200 words per minute. A good first goal is 600." Buttons "Cancel", "Recommend"
   (sets the slider to `max(300, round50(3 × currentSpeed))`, or 600 when currentSpeed is 0), "Set"
   (saves `goal_wpm`).

**Check:** typecheck passes. Commit: `reading-center: stats and goal`.

---

## Step 15: Admin page (`pages/AdminPassagesPage.tsx`)

1. Title "Reading Center passages", button "New passage".
2. Table: drag handle, title, word count, Published switch, Edit, Delete. Rows sortable with
   `@dnd-kit/sortable` (already installed; copy the usage pattern from an existing file: run
   `grep -rln "useSortable" src` and open the first result). On drop, call `useReorderPassages` with new
   `sort_order` values `1..n`.
3. Editor dialog (`components/PassageEditor.tsx`): fields Title (required), Author (optional), Cover URL
   (optional text input; no upload in v1), Body (`Textarea`, `min-h-[50vh]`, helper text "Leave a blank
   line between paragraphs."). Live line under the body: `${countWords(body)} words · about
   ${estimateMinutes(countWords(body), 200)} min at 200 WPM`. Slug = `slugify(title)` on create; do not
   change the slug on edit. "Save" calls `useUpsertPassage`. Show the Supabase error text if it fails.
4. Delete: `AlertDialog`. Load how many progress rows exist for that passage
   (`rcDb("reading_center_progress").select("user_id", { count: "exact", head: true }).eq("passage_id", id)`).
   If count > 0, show "N students have progress on this passage. Type the title to confirm." and only
   enable "Delete" when the typed text equals the title exactly.

**Check:** typecheck passes. Commit: `reading-center: admin passages page`.

---

## Step 16: Routes (`src/App.tsx`)

This is the only existing file you edit in this step. Make exactly these changes:

1. Next to the other `React.lazy` page imports near the top, add:
```ts
const ReadingCenterLibrary = React.lazy(() => import("./features/reading-center/pages/LibraryPage"));
const ReadingCenterReader = React.lazy(() => import("./features/reading-center/pages/ReaderPage"));
const ReadingCenterStats = React.lazy(() => import("./features/reading-center/pages/StatsPage"));
const ReadingCenterAdmin = React.lazy(() => import("./features/reading-center/pages/AdminPassagesPage"));
```
   Each page file must have a `default export`.
2. Find the line `<Route path="/admin/drive-files" element={`. Directly **above** it, add:
```tsx
<Route path="/admin/reading-center" element={
  <ProtectedRoute requireAdmin>
    <React.Suspense fallback={<div className="min-h-screen" />}>
      <ReadingCenterAdmin />
    </React.Suspense>
  </ProtectedRoute>
} />
<Route path="/reading-center" element={
  <ProtectedRoute requireAdmin>
    <React.Suspense fallback={<div className="min-h-screen" />}>
      <ReadingCenterLibrary />
    </React.Suspense>
  </ProtectedRoute>
} />
<Route path="/reading-center/stats" element={
  <ProtectedRoute requireAdmin>
    <React.Suspense fallback={<div className="min-h-screen" />}>
      <ReadingCenterStats />
    </React.Suspense>
  </ProtectedRoute>
} />
<Route path="/reading-center/:slug" element={
  <ProtectedRoute requireAdmin>
    <React.Suspense fallback={<div className="min-h-screen" />}>
      <ReadingCenterReader />
    </React.Suspense>
  </ProtectedRoute>
} />
```

Why `requireAdmin`: v1 ships dark. Only Joshua (admin) can see the Reading Center until he decides to
open it to students. This replaces the "feature flag" in the spec. **Do not** add a new column to
`profiles`, and **do not** edit `useUserPermissions.ts`, `adminUsers.ts` or `ProtectedRoute.tsx`.

**Do not add any navigation link** to the Foyer or sidebar. Joshua reaches it by URL until launch.

**Check:** `npm run typecheck` and `npm run build` both pass. Commit: `reading-center: admin-only routes`.

---

## Step 17: Bulk import script (`scripts/reading-center-import.ts`)

1. Open `scripts/assign.ts` and copy **exactly** how it reads Supabase credentials and creates its
   client (it reads them from the ai-os `.env`, not this repo's `.env`). Use the same approach. Never
   print a key.
2. Usage: `npx vite-node scripts/reading-center-import.ts -- <folder> [--apply]`. Without `--apply` it is a
   dry run that changes nothing.
3. For each `.md` or `.txt` file in the folder (not recursive), sorted by filename:
   - Optional front matter between `---` lines at the top: keys `title`, `author`, `sort_order`, `cover`.
   - Title = front matter `title`, else the first line starting with `# ` (strip the `# `), else the
     filename without extension.
   - Body = the rest of the file, with the `# title` line removed and trimmed.
   - Slug = `slugify(title)` (import from `../src/features/reading-center/lib/tokenize`).
   - word_count = `countWords(body)`.
4. Fetch existing passages by slug. Print one line per file: `NEW`, `CHANGED` (body, title, author, cover
   or sort_order differ) or `SAME`, with title and word count. At the end print totals.
5. With `--apply`, upsert `NEW` and `CHANGED` rows `onConflict: "slug"`. New rows get `sort_order` from
   front matter, else (current max sort_order + 1, incrementing).
6. Never delete passages.
7. Add to `package.json` `scripts`, right after the `"student-work"` line:
   `"reading-center:import": "vite-node scripts/reading-center-import.ts --",`

**Check:** create a temp folder in your scratch space with one test file and run the script **without**
`--apply`; it must print one `NEW` line and change nothing. Do not run with `--apply`. Commit:
`reading-center: bulk import script`.

---

## Step 18: Final verification

Run each command and paste the last 20 lines of each output into the PR description:

```bash
npm run typecheck
npx vitest run src/features/reading-center
npm run lint -- src/features/reading-center scripts/reading-center-import.ts
npm run build
```

All four must pass. Fix only problems in files you created or the lines you added to `App.tsx` and
`package.json`.

Then check by reading your own code (the reviewer will run the app):
- [ ] No `supabase.from("reading_center` outside `lib/db.ts`.
- [ ] No em dash `—` in any `.tsx` string (search: `grep -rn "—" src/features/reading-center`; the only
      allowed hits are inside regexes in `tokenize.ts`).
- [ ] Every icon-only button has an `aria-label`.
- [ ] Appearance tab shows controls in every mode.
- [ ] Keyboard handler ignores inputs and open dialogs.
- [ ] `git diff --stat origin/main` lists only: files under `src/features/reading-center/`, the
      migration file, `scripts/reading-center-import.ts`, `src/App.tsx`, `package.json`.

---

## Step 19: Push and open the PR

```bash
git push -u origin feat/reading-center
gh pr create --base main --head feat/reading-center --title "Reading Center v1 (admin-only)" --body-file PR_BODY.md
```

Write `PR_BODY.md` in your scratch space (not in the repo) with these headings:

1. **Summary**: what was built in 3 sentences.
2. **Spec map**: a table: spec section number → files that implement it.
3. **Steps**: steps 0–18, each "done" or "blocked: reason".
4. **Verification output**: the outputs from step 18.
5. **Not done / deviations**: anything you skipped or did differently, and why. Write "None" if none.
6. **Migration**: "Not applied. Reviewer applies `supabase/migrations/20261013120000_reading_center_v1.sql`."
7. **Word lists**: 2–3 sentences on where word lists will plug in (tables linking
   `(passage_id, word_index)`; `tokenize.ts` keeps indexes stable).

End the PR body with:

🤖 Generated with Gemini 3.8 Flash; to be reviewed by Claude.

Do not merge the PR. Stop here.
