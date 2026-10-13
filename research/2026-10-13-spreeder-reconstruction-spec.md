---
title: Spreeder reconstruction spec (visual + behaviour)
date: 2026-10-13
sources:
  - Live capture of spreeder.ereflect.com in Joshua's logged-in Chrome (account "mk"), 1536x695 viewport, 2026-10-13
  - Static code: main.21893fdef5a7593c.js + 219 lazy chunks from resources.ereflect.com/Spreeder/webApp/ (REA analyze-javascript-application, 222 files, 2804 modules, 0 parse failures)
supersedes: visual guesses in brainstorms/2026-10-12-reading-center-build-spec.md (that spec said "use the app's design tokens"; Joshua wants Spreeder matched identically)
target: dev/ai-os-projects/reading-center (standalone first, LSAT U later)
---

# Spreeder reconstruction spec

Observed = seen live or read in shipped code. Inferred = marked. Brand assets (Spreeder logo, cover art,
eReflect icon fonts `iconNewui`/`iconSpreed`) are **not** copied; equivalents are named.

## 1. Global

- UI font **Poppins** (Google Fonts, OFL). Reading text uses the chosen reading font (default Arial).
- Icons: reader header uses **Ionicons** (MIT): `arrow-back-outline`, `search`, `expand-outline`, `bookmark`, `settings`.
  Dialogs/menus use **Material Icons** (Apache 2.0): `close`, `arrow_drop_down`, `more_vert`, `navigate_next`, `keyboard_arrow_left/right`.
  Speed gauge / view-text / keyboard / list glyphs are eReflect's own font: substitute Ionicons `speedometer`, `reader`/`list`, `keypad`.
- Themes (whole app, not just reader): Light, Dark, High Contrast, System.

| Token | Light | Dark | High Contrast |
|---|---|---|---|
| page bg | #ffffff | #000000 | #121212 |
| reading surface | #ffffff | #000000 | #1e1e1e |
| primary text | #424242 (chrome), #000 (reading) | #ffffff | #ffffff |
| secondary text | #757575 | #ffffff | #e0e0e0 |
| card (profile) | n/c | #252525 | inferred #242424 |
| dialog bg | #ffffff | #000000 | #242424, border .8px #6c6c6c |
| dialog shadow | rgba(0,0,0,.2) 0 11px 15px -7px … | rgba(255,255,255,.4) -1px 4px 29px 0 | same as dark |
| backdrop | rgba(0,0,0,.55) | rgba(110,118,125,.4) | rgba(110,118,125,.4) |
| outline borders | #cccccc | #cccccc (dropdown), #444 (secondary btn) | #444444 |
| bottom bar | rgba(255,255,255,.85), top .8px #ccc | rgba(0,0,0,.8), top .8px #121313 | #1a1a1a, top .8px #6c6c6c |
| unhighlighted words (Highlight) | #cbcbcb | #444 | #444 |
| accent green (active tab, Save) | #34ad07 | #34ad07 text, ink #71f141 @15% | — |
| accent blue (speed/view) | #0a85ff | #0a85ff | — |
| slider / toggle blue | #3e92d7 knob, track tint | same | same |

## 2. Shell (library / profile)

- Left sidenav 230px, bg rgba(0,0,0,.85) (dark). Hamburger top-left, product logo (substitute: wordmark "Reading Center").
- "Add Text" button 189x55 at (20,70): bg #073555, text #009cdb Poppins 14/500, radius 12, blue ⊕ icon left. Opens menu: Paste Text, Import Document, AI Book Summary, AI Generate (icons left, dark panel #252525-ish).
- Nav rows 56px apart, icon x44, label x71, Poppins 14/500 white: Spreed (book icon), Tags (tag), Courses (mortarboard), Profile (person).
- Active row: 189x52 pill radius 8, bg #1a3b13, label/icon #3aab1f, 4px green left bar. Hover: bg #2c2c2c-ish.
- Top bar right: book-search icon, search box 232x32 bg #252525 radius 8 ".8px" border, placeholder "Searching N books..", magnifier; apps grid; account icon + caret.

## 3. Library (/library)

- Content x=250. Shelves: **Recent**; **Added By Me** `View All >`; **In Progress** `View All >`. Heading Poppins bold ~18px.
- Card: cover 148x209 radius ~4 (user text: solid #009cdb tile with white document glyph). Title Poppins 13 white 2 lines, author grey small, ⋮ (more_vert) right of title.
- ⋮ menu: View/Location (eye), Edit Image (image), Edit Text (edit), Tag (tag), Delete (trash), Hide from Recent (eye-off). Dark panel, Poppins 15.
- Paste Text: full-screen "Add To Library" (Poppins 24), X top-right, underline field "Enter Title", bordered box "Add Text Here", bottom-right Cancel (outlined) + Save (disabled until valid).

## 4. Reader (/spreed)

- Header 56px: back arrow 24px at (32,14) + "Back" Poppins 14/500 ls .28px; centred title Poppins 18/400 ls .72px; right icons 26px at x 1405/1450/1496 (expand, bookmark, settings); e-Reader adds search at x 1359.
- Reading card: width 72% (100% under 1380px), radius 10, padding 20px 0, full height, canvas inside. Stage padding 20 left/right.
- Transport (hidden while playing): prev ◁ and next ▷ outlined triangles 50x50 at ±100px of centre, circle play ~60px. Hover: light grey circle behind.
- Clicking the reading area toggles play/pause. Window blur pauses. Resize pauses and relays out.
- Bottom bar 40px: keyboard button left (~x251); centre two 80x30 buttons radius 4 border .8px: gauge icon + WPM, list icon + "View", colour #0a85ff Poppins 13/500; right "#readingTimespan" Poppins 14/400 `${pct}% - ${time} remaining`.
- Speed change toast: "N WPM" pill bg #323232 white 14px padding 8 radius 4, top 10px centred, fades in .5s, holds 2s, fades out 2s.

### Text model (shipped code)
- Whitespace collapsed to single spaces; em dash → "-"; **no paragraphs**.
- Sections: sentences (regex `[^.!?]+([.!?"”]+|$)`) accumulated until ~2000 chars; a sentence that would push past 2400 is split at a word boundary. Sentence ends after "Dr/Mr/Mrs/Ms" or a single letter do not close a section.
- Words = split(" "); id 1-based; charPosition.
- Progress % = round((sectionIndex + posInSection/sectionLen) / sections * 100) (1 when on the last word of a section).
- Remaining = time from current word to end: "N hour(s) and M minute(s)", "Less than a minute".

### Layout (Serial / Flow / Highlight / Scroll)
- Words are measured in the font; a line takes words while `x + width + space <= stageWidth - 40` **and** words < Words Per Line.
- Serial: slide = Number of Lines lines, block vertically centred; Center Text centres each line, else x=20.
- Flow: forced 1 line, spacing 1, left-aligned x=20; each chunk revealed by a bg-coloured mask sweeping left→right across the window over the chunk's duration (blank when paused at chunk start).
- Highlight: page = floor((height-20)/fontSize) lines, left x=20, all visible in unhighlighted colour; current group (Number of Lines lines) drawn in font colour, not bold.
- Scroll: same page, only current group visible at its own y; previous group hidden; new page starts at top.
- Font size clamp 8..74. Line spacing multiplies fontSize.

### Timing (shipped code)
- Section total T = round(words / wpm * 60000). Chunks n. Even delay = T / (n - 1 + f), last = even*f where f = min(lastChunkLines / numberOfLines, 1).
- Speed Variability: delay = round(T/n) * (chunkChars + (notLast?1:0)) / (sectionChars/n).
- Punctuation Pauses: delay *= 2 if chunk text contains any of `. ? ! : ; - – ,` (any group size).
- WPM clamp 50..5000, step 10 (keys ↑/+ and ↓/-), rounded to 10.

### Dialogs
- Preferences: 550x599 centred, radius 15, padding 14. Title "<first name>'s preferences" Poppins 24/400 (dark white / light #424242), close X.
  - Tabs Spreed/Appearance/Advanced Poppins 14 (active 500 #34ad07 on pill 100x30 radius 99 bg accent @15%; idle #757575 light / white dark).
  - Spreed: "Reading Mode:" 13/400 ls .52px + dropdown (93x36, border .8 #ccc, radius 4, "Serial" 14/500 + arrow_drop_down). Sliders with tick dots, label below-left 12/400, value below-right. Serial: Number of Lines, Words Per Line, Center Text toggle. Flow/Scroll: Words Per Line. Highlight: Words Per Line, Number of Lines.
  - Appearance: Theme dropdown; Font dropdown (wide, filled #eee in light) + Size dropdown; large "Sample Text" centred in chosen font/size.
  - Advanced: Punctuation Pauses (default on) "Slight pause at end of sentences and punctuation marks. Only works for group size of 1."; Speed Variability (default off) "Slow down for larger chunks and speed up for smaller chunks so average wpm stays the same". White round "?" icons.
  - e-Reader mode: no tabs; Reading Mode, Theme, Font+Size, Sample Text, Line Spacing slider (1.0–2.0, 10 ticks).
  - Restore Defaults: bottom-left, 149x38 outlined. Only X closes (Escape does not).
  - Dropdown menus: white (light) / #252525 (dark) panel, items Poppins 15, hover grey.
- Reading Speed (WPM): 528x363, radius 15. Title Poppins 24 #424242. Value 45px/400 #424242 centred. Left column -10 above -100, right column +10 above +100: 75x55, radius 15, bg #d5e7fb, text #0a85ff 18/500. Footer right: Cancel (outlined #ccc) + Save (bg #34ad07 white).
- View: full screen sheet. Title Poppins ~24 #424242 top-left, X top-right. Chip "User added" grey pill. Pill search "Search this text..." top-right; on Enter shows X, "i of n", ▼ ▲; whole-word match; current hit #fab95d, others #fae55d, radius 4. Text Poppins 16/400 #212121 lh 33; current word outlined 1.6px #34ad07 radius 5; click word to jump. Grey round play button bottom-centre. Thin rule then footer "3 minutes to go - 200 WPM" Poppins 14 #757575.
- Bookmarks: dialog ~850 wide radius 15; title "Bookmarks"; empty state grey 150px circle with list glyph, "No Bookmarks Yet" Poppins ~28 #616161, text "To create a bookmark, simply pause Spreeder while you're reading and long press or click on any word." Bookmark rows have optional notes ("Enter Notes (Optional)...", "Go to location") — from code, not seen filled.
- Keyboard Shortcuts popover: white card radius ~12 with pointer to the keyboard button; grey keycaps with bottom shadow: ↑ / ↓ or + - "increase or decrease speed"; P or SPACE BAR "pause / resume"; → "section forward", R "restart"; ← "section back", S "settings".
- Finish: "You have successfully completed <strong>title</strong>. It will now be moved to your finished section on the Home Screen."

### e-Reader
- Column ~734px centred, reading font/size, lh = font size × spacing; text fills page height and clips. Hover word → #3e92d7.
- Bottom: ion-range full width (bar 4px rgba(100,100,100,.4), active + knob 25px #3e92d7), "n / N" #424242cc, chevrons.
- Search: right panel card "Search" + X; underline field "Search in this book"; "N results in book"; results grouped "Page p (k results)" with snippet, match bold; selected group bg light blue; matches highlighted #ffff00 in text.

## 5. Profile (/profile)

- Header card #252525 radius 15: avatar circle, "<name>'s Spreeder" Poppins 25/300, pill "✦ 0 AI Credits"; tabs Dashboard / Stats (active = green pill) / Options ▾ / share.
- Dashboard: 2x2 cards #252525 radius 15: Vital Stats (Current Speed, Target Speed speedometer dials), Reading Focus (↻ 30 Days ▾), Training Time (↻ 6 months ▾), Reading Speed (↻ 30 Days ▾). Empty: "Nothing just yet. Your results will appear here later 🙂".
- Stats: "Reading Speed ▾" metric + "30 Days ▾"; empty: dark circle with bar-chart tile, "Not Enough Data", "We don't have enough data to display your stats yet. Use the app for a while and come back soon."
- Options menu: Theme: Dark ▸, Edit Profile, Goals, Settings, Sign Out.
- Goals dialog (black, radius 15): slider; "Reading Speed Goal (WPM):" bold + value right; text "Please enter your goal reading speed in words per minute (WPM). An average person reads at 200 words per minute. We recommend starting with a goal of 600 WPM."; Cancel, Recommend, Set (green).
- Recommend → full-screen "Goal Recommendation Test": blue checkered flag, "Recommend Goals" (blue ~40px), "Please complete the following test and Spreeder will recommend your ideal goals.", green Start. (Test content not inspected; would record results.)

## 6. Not reproduced / out of scope (decide later)
- 20,504-book catalogue, AI Book Summary / AI Generate (credits), Import Document parsing, Courses (empty for this account), eReflect app grid, share, Wordela word actions in e-Reader ("Add to Wordela Wordlist", "Look Up Word").

## 7. Build status (2026-10-13, dev/ai-os-projects/reading-center @ 441536b)

Built to this spec and checked in the browser: library shell and shelves, reader Serial / Highlight / e-Reader
(Light and Dark), preferences dialog, View panel, e-Reader search, play timing (about 310 ms a word at 200 WPM,
punctuated chunks doubled).

Deliberate departures:
- Flow: Spreeder's shipped wipe multiplies by the per-frame delta (`y.timeDiff/m`) instead of elapsed time, so the
  mask barely moves and Flow shows almost nothing. Built as the intended left-to-right reveal over the chunk time.
- e-Reader search snippet keeps the space Spreeder drops ("technology.But").
- No Spreeder logo, cover art or eReflect icon font; Ionicons / Material Icons stand in.

Not built (need a service or were not observable):
- Look Up Word and Add to Wordela Word List (word action sheet), AI Book Summary, AI Generate, the 20,504-book
  catalogue, Courses content, share, Sign Out, AI credits.
- Not observed live, so built from inference: filled Bookmarks list, Tag dialog, Edit Image dialog, Delete confirm,
  Edit Profile, the reading-test text picker, charts with data, light-theme sidenav colours, speedometer artwork.
