---
title: Spreeder feature inventory
date: 2026-10-12
source: https://spreeder.ereflect.com (Joshua's logged-in account, inspected live in Chrome)
purpose: Reference spec for replicating Spreeder in a skill / LSAT U reading tool with predetermined passages
---

# Spreeder feature inventory

Verified live unless marked *(code only)*. "Code only" means the name exists in the app's main bundle
(`resources.ereflect.com/Spreeder/webApp/main.21893fdef5a7593c.js`) but no screen for it was reachable
from this account.

## 1. Library (`/library`)

- Shelves: **Recent**, **Added By Me** (with "View All").
- Card: cover image (generic document icon for user text), title, author line.
- Card ⋮ menu: **View/Location**, **Edit Image**, **Edit Text**, **Tag**, **Delete**, **Hide from Recent**.
- Global search: "Searching 20504 books.." (built-in catalogue) plus a book-search icon.
- Routes: `library`, `library/:name`, `library/tags/:name`.

## 2. Adding text (Add Text button)

| Option | Behaviour |
|---|---|
| Paste Text | Full-screen "Add To Library": Enter Title field, Add Text Here box, Cancel / Save (Save disabled until filled). |
| Import Document | Opens a file picker (accepted types not exposed). |
| AI Book Summary | Uses AI credits; generates a cover step, falls back to text only if the cover fails. |
| AI Generate | Uses AI credits. |

Profile shows the credit balance ("0 AI Credits").

## 3. Reader (`/spreed`)

### Chrome around the text
- Top: Back, title, **Search** (e-Reader only), **Fullscreen**, **Bookmarks**, **Settings (gear)**.
- Bottom: **Keyboard shortcuts** button, **WPM button** (shows current speed), **View**, progress ("1% - 3 minutes remaining").
- Transport: previous chunk ◁, play/pause, next chunk ▷.

### Speed (WPM) dialog
- "Reading Speed (WPM)" with **−100, −10, +10, +100** buttons, Cancel / Save. Default 200.

### View panel
- Full passage overlay with "User added" badge, **Search this text**, current word boxed, click any word to jump,
  play button, footer "3 minutes to go - 200 WPM".

### Bookmarks
- Empty state: "To create a bookmark, simply pause Spreeder while you're reading and long press or click on any word."

### Keyboard shortcuts
| Keys | Action |
|---|---|
| ↑ / ↓ or + / − | increase / decrease speed |
| P or Space | pause / resume |
| → | section forward |
| ← | section back |
| R | restart |
| S | settings |

## 4. Preferences dialog ("<name>'s preferences")

Tabs: **Spreed · Appearance · Advanced**, plus **Restore Defaults**. Saved per user, server-side.

### Spreed tab: Reading Mode and its per-mode settings
| Mode | What it looks like | Settings (ranges) |
|---|---|---|
| **Serial** | One chunk flashed in a fixed spot | Number of Lines (1–6), Words Per Line (1–6), Center Text (toggle, default on) |
| **Flow** | Chunk flashes, positioned where it sits in the line | Words Per Line (1–6) |
| **Highlight** | Whole text visible, current chunk bright, rest dimmed | Words Per Line (1–6), Number of Lines (1–6) |
| **Scroll** | Text scrolls past | Words Per Line (1–6) |
| **e-Reader** | Normal paginated reading ("1 / 6"), page slider, prev/next page, in-text search | Theme, Font, Size, Line Spacing (1.0–2.0, step 0.1) |

### Appearance tab (all modes)
- **Theme:** Light, Dark, High Contrast, System.
- **Font (19):** Arial, Times New Roman, Verdana, Calibri, Microsoft Sans Serif, Impact, Lucida Console,
  Comic Sans MS, Georgia, Palatino Linotype, Tahoma, Trebuchet MS, Courier New, Open Dyslexic Font, Antikor,
  Code New Roman, CQ Mono, Pointfree, Fira Mono.
- **Size:** 8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 28, 32, 36, 40, 44, 50, 56, 62, 68, 74 (default 36).
- Live "Sample Text" preview.
- Note: in speed modes this tab renders blank (Spreeder bug); the controls exist in the DOM and show
  correctly in e-Reader mode and under Profile → Settings.

### Advanced tab
- **Punctuation Pauses** (default on): "Slight pause at end of sentences and punctuation marks. Only works for group size of 1."
- **Speed Variability** (default off): no help text shown. *Inference:* varies display time per chunk (e.g. by word length).

## 5. Profile (`/profile`)

- Header: name, AI credit balance, share button.
- **Dashboard:** Vital Stats gauges (Current Speed, Target Speed, 0–2000 scale), Reading Focus, Training Time,
  Reading Speed charts, each with refresh and a period picker.
- **Stats:** metric picker (Reading Speed, Reading Focus, Training Time) × period (24 Hours, 7 Days, 14 Days, 30 Days, 6 Months).
- **Options:** Theme (submenu), Edit Profile, **Goals** (Reading Speed Goal slider 50–5000 WPM, default 600,
  with Recommend button; copy: "An average person reads at 200 words per minute. We recommend starting with a
  goal of 600 WPM."), Settings (same Appearance + Advanced dialog), Sign Out.

## 6. Courses (`/courses`)

- Empty for this account: "No curriculums or courses assigned to your class yet."
- *(code only)* curricula → courses → steps with replay and preview; Nearpod activities; class invites; admin.

## 7. Present in code, not reachable here *(code only)*

- Training games: Speed Builder, Focus, Catch, Falling Words, Rising Words, Sinking Words, Letter Train I/II,
  Key Memory, Key React, Quick Trainer; Typesy-imported games.
- Word work: word lists with learn, review, edit, word-scroll; flashcards; quizzes.
- Text-to-speech: voices and voice rate (browser speechSynthesis), voice control.
- Streaks.

## 8. Not inspected

- Fullscreen (standard browser fullscreen assumed), Edit Profile form, Import Document accepted file types,
  AI Book Summary / AI Generate dialogs (both need credits; account has 0), Tags page contents, eReflect app grid.

## 9. First predetermined passage

**Living in a rational society** (user added, ~550 words, ~3 min at 200 WPM)

The rationalizing of society can be conceptualized as the pursuit of efficiency, predictability, calculability, and control through technology. But rational systems inevitably spawn a series of irrationalities that result in the compromising and perhaps even the undermining of their rationality. Fast-food restaurants, which epitomize the rational model, proffer the fastest means of getting from a hungry state to a sated one, without surprises, at low cost, in a carnival-like setting suggesting that fun awaits the consumer at each visit. The wholesomeness of the food seems an insignificant consideration. Whereas in the past, working people were prepared to spend up to an hour preparing dinner, they now are impatient if a meal is not on the table within ten minutes. (For their part, some fast-food restaurants have developed chairs that become uncomfortable after about twenty minutes, to ensure that diners do not stay long.) Fast-food restaurants have preferentially recruited adolescent help, at least until recently, because this age group adjusts more easily than adults do to surrendering their autonomy to machines, rules, and procedures. Few skills are required on the job, so workers are asked to use only a minute portion of their abilities. This policy is irrational from the standpoint of the organization, since it could obtain much more from its employees for the money (however negligible) it pays them. These minimal skill demands are also irrational from the perspective of the employees, who are not allowed to think or to respond creatively to the demands of the work. These restrictions lead to high levels of resentment, job dissatisfaction, alienation, absenteeism, and turnover among workers in fast-food franchises. In fact, these businesses have the highest turnover rate of any industry in the U.S. The entire workforce of the fast-food industry turns over three times in a year. Although the simple, repetitive nature of the work makes it easy to replace those who leave, the organization would clearly benefit from keeping employees longer. The costs of hiring and training are magnified when the turnover rate is extraordinarily high.

The application of the rational model to the house-building process in the 1950s and ’60s led to suburban communities consisting of nearly identical structures. Indeed, it was possible to wander into the residence of someone else and not to realize immediately that one was not at home. The more expensive developments were superficially more diversified, but their interior layouts assumed residents who were indistinguishable in their requirements. Furthermore, the planned communities themselves look very similar. Established trees are bulldozed to facilitate construction. In their place, a number of saplings, held up by posts and wire, are planted. Streets are laid out in symmetrical grid patterns. With such uniformity, suburbanites may well enter the wrong subdivision or become lost in their own.

Many of Steven Spielberg’s films are set in such suburbs. Spielberg’s strategy is to lure the viewer into this highly repetitive world and then to have a completely unexpected event occur. For example, the film Poltergeist takes place in a conventional suburban household in which evil spirits ultimately disrupt the sameness. (The spirits first manifest themselves through another key element of the homogeneous society—the television set.) The great success of Spielberg’s films may be traceable to a longing for some unpredictability, even if it is bizarre and menacing, in increasingly routinized lives.

Paragraph breaks are inferred; Spreeder's word view does not preserve them.
