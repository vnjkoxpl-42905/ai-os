# Session Desk: the standard for every post-session note

Joshua approved this design on 2026-11-13 as the gold standard: "it should emulate this quality every time ... the interaction, the writing style, the exercises, the notes, every single thing." It replaces the Session Manual as the look. This file is the full specification. Follow it literally. Where it does not cover a case, do not improvise: use the nearest listed piece and put the gap in the run report under "For Joshua to decide".

## Contents

1. Files in this folder
2. Build procedure, step by step
3. Page order of a recap
4. Pieces: markup, when to use, limits
5. What the script adds (never hand-write these)
6. Fixed wording
7. Visual effects and why each exists
8. Writing standard, taken from the model
9. Practice checks standard
10. Primer and reference pages
11. Verification, with commands
12. What must never change without Joshua

## 1. Files in this folder

| File | What it is | Edit it? |
|---|---|---|
| `model-finding-the-conclusion.html` | The approved page (Lanae, 2026-10-29). Open it before every build and keep it beside the draft. | No. Rebuild with `--model`. |
| `model-finding-the-conclusion.src.html` | The model's source: content plus `/*CSS*/` and `/*JS*/` slots. The starting file for every recap. | Only on Joshua's correction to the model. |
| `session-desk.css` | All styling. | Only to add a piece Joshua approved. |
| `session-desk.js` | All behaviour. | Same. |
| `build_session_desk.py` | Builds the pages and runs every check. Writes nothing if a check fails. | Add a check when a problem is seen twice. |
| `SPEC.md` | This file. | Keep in step with the three files above. |

The model's sentences belong to Lanae's session. Copy its structure, pieces and voice. Never copy its teaching sentences or examples into another student's note.

## 2. Build procedure, step by step

Do these in order. Do not skip one because it seems obvious.

1. Open `model-finding-the-conclusion.html` in the browser and read it top to bottom.
2. Make the build folder `brainstorms/YYYY-MM-DD-<student>-post-session/`.
3. Copy `model-finding-the-conclusion.src.html` into it as `recap.src.html`.
4. Change the `<meta name="lsatu-interactive-lesson">` content to `<student>-<YYYY-MM-DD>-<topic-slug>`, and the `<title>` to `<Title> · Session recap`.
5. Replace the content one piece at a time, top to bottom, using section 3 for the order and section 4 for each piece. Delete a piece the session does not call for (section 4 says which are optional). Leave the `/*CSS*/` and `/*JS*/` slots, the progress bar, the rail and the footer exactly as they are.
6. Write the primer and the reference as Markdown in the same folder (section 10).
7. Build:
   ```
   uv run --with markdown python -I <skill>/references/session-desk/build_session_desk.py <folder> "<primer.md>|Before you start · <drill name>|<marker>" "<reference.md>|Reference · Keep it open while you drill|<marker>"
   ```
8. If the builder prints FAILED, fix every listed problem and build again. Never edit a built `.html` by hand; edit the source and rebuild.
9. Run every check in section 11 and report each result.

## 3. Page order of a recap

The model has seven sections. A recap has five to nine. Keep this order and take what the session supports.

| # | Kicker in the model | Job | Pieces used |
|---|---|---|---|
| Hero | `Session recap · October 29` | Name the reasoning. Say how most students go wrong and what works instead. | kicker, h1 on two lines, lede, 3D stage |
| 1 | Read it first | The first thing to do on every question. | intro paragraph, `ol.steps`, one callout |
| 2 | Two kinds of sentences | The distinction the session turned on. | intro, `.kinds`, paragraph, one or two callouts |
| 3 | The check | The rule or test itself. | intro, `ol.steps`, `.gate` if it fits, callout, closing paragraph |
| 4 | Keywords | A common shortcut and its limit. | paragraph, `.flags`, paragraph, `.callout.trap`, paragraph, `.quote` |
| 5 | Try it | Practice. | two or three `.drill` blocks |
| 6 | On every argument | The method as a short checklist. | paragraph, `figure.screen` if it fits, `ol.steps` |
| 7 | Your work | Every assignment and promise. Always last. | `ol.steps.todo` |

Every section is `<section><div class="wrap">`, then `<div class="sec-kicker">` (two to four plain words), then an `<h2>` that says something ("Pivot words turn the direction, nothing more", not "Keywords"), then content. The section number, the rail entry and the progress bar come from the script.

## 4. Pieces: markup, when to use, limits

Copy markup from the model source, never from memory. The builder rejects inline `style=`, images, iframes and outside scripts.

### Hero and 3D stage (required)

```html
<header class="hero">
  <div class="wrap">
    <div class="kicker">Session recap · October 29</div>
    <h1>Finding the Conclusion<br>by Asking Why</h1>
    <p class="lede">...</p>
  </div>
  <div class="stage" aria-hidden="true">
    <div class="stack" data-tilt="10">
      <div class="slab base"><i>PASSES BOTH</i><b>The conclusion</b></div>
      <div class="slab c2"><i>CHECK 2</i><b>Does another sentence tell me why to believe it?</b></div>
      <div class="slab c1"><i>CHECK 1</i><b>Is this sentence an opinion?</b></div>
    </div>
  </div>
</header>
```

- Kicker: `Session recap · <Month day>`, no year.
- h1: the reasoning taught, broken once with `<br>` so each line is two to four words.
- Lede: three to five sentences. How most students do it, why that fails, what works on every question.
- Stage: two light cards resting above one dark slab. The two cards are the two things the student does or asks. The slab is what they produce. `c1` is the top card, `c2` the middle, `base` the dark one. Each card's `<b>` is at most 50 characters. The slab's `<b>` is at most three words. Each `<i>` label is at most 12 characters, in capitals. Take the words from the lede or the section headings. If the session's method has more than two parts, use the first two and name the result. The stage is hidden from screen readers because it repeats the lede, so it must never carry anything the text does not.

### Numbered steps: `ol.steps` (required at least once)

```html
<ol class="steps">
  <li><b>Say it in your own words, like a short story.</b> Who did what, and why? ...</li>
</ol>
```

For any procedure. Two to six items. Each item opens with a bold instruction that ends in a full stop or question mark, then one to four sentences. Include a tiny worked example inside the item when the step is abstract ("X" becomes "Y").

### The student's work: `ol.steps.todo` (required, last section, exactly one)

Same markup with `class="steps todo"`. The script turns each number into a tick box and remembers ticks on that device. One item per assignment or promise from the transcript, with its real certainty. Nothing here that the transcript does not support.

### Key rule note: `.callout` and `.callout.trap`

```html
<div class="callout"><span class="tag">One check isn't enough</span>
  An opinion with no reason behind it is only an opinion. <strong>It has to pass both.</strong>
</div>
```

- The tag is the rule itself as a short sentence, not a category. "Why someone did something is never a fact", not "Note".
- Body: one to five sentences. At most one `<strong>` run, on the sentence the student must keep.
- `.callout.trap` (red) is for the single most costly mistake of the session. At most one per recap. Its tag in the model is "The trap that costs the most".
- At most six callouts in a recap, at most two in a row.

### Taxonomy cards: `.kinds` (optional)

```html
<div class="kinds">
  <div class="kind apply" data-tilt="5">
    <span class="bar"></span>
    <div class="name">Fact</div>
    <p class="what">Something you can measure or check. ...</p>
    <div class="words"><b>Looks like</b><span>The painting sold for $20,000.</span></div>
    <div class="test"><b>Test</b>Could I measure it or look it up?</div>
  </div>
  ...
</div>
```

Use only when the session taught two or three real categories. Never invent categories to fill the piece. Each card has a name, a one or two sentence `what`, one example line under "Looks like" or "Sounds like", and one question under "Test" or "Use it". Paired cards use the same example subject so the contrast is visible (the painting sold for a price; the painting is beautiful).

| Class | Colour | Edge detail | Use for |
|---|---|---|---|
| `apply` | green | ruler ticks | something measurable or checkable |
| `describe` | green | plain | a green card where a ruler would mean nothing |
| `link` | brass | quote mark in the paper | something a person says or interprets |
| `assume` | brass | plain | a brass card where a quote mark would mean nothing |
| `warn` / `object` | red | plain | the category to be careful with |

### Two switches and a lamp: `.gate` (optional, at most one)

Use only when the session taught a rule with exactly two conditions that must both hold. Copy the block from the model. Change only the `<h3>`, the hint, the two switch labels and the four verdict sentences.

| Verdict | Shown when | Lamp | In the model |
|---|---|---|---|
| `v0` | neither switch on | dark | Neither check passes. Not the conclusion. |
| `v1` | first only | amber | Only an opinion. It still needs a reason. |
| `v2` | second only | amber | Not the conclusion yet. It has to pass both. |
| `v3` | both | green, glowing | It passes both. This is the conclusion. |

Each verdict is at most two short sentences and must be true under a counterexample check. If the transcript does not settle what one of the four states means, do not ship the gate; list it for Joshua.

### Warning words: `.flags`

```html
<div class="flags"><span class="flag">but</span><span class="flag">yet</span><span class="flag">however</span></div>
```

Two to five single words or short phrases the session named. The script adds the turn arrow. They are tags, not buttons: do not make them clickable.

### Credit line: `.quote` (required, one or two)

```html
<div class="quote">You said it yourself: pivot words don't always lead to the conclusion. ...</div>
```

Second person. Names something the student actually did or said in the session, with a transcript timestamp in the private source map. Two to four sentences. Never an error framed as "your mistake". Place it at the end of the section it relates to.

### Practice check: `.drill` (required, two or three)

```html
<div class="drill">
  <div class="drill-head"><div>
    <h3>Say it out loud, then tap to check</h3>
    <p class="hint">Can you measure it or look it up, or is someone interpreting?</p>
  </div></div>
  <p class="passage"><em>Short original argument, only when the check needs one.</em></p>
  <div class="chips">
    <div class="chip" data-k="describe" role="button" tabindex="0" aria-expanded="false"><span>The bus leaves at 8:15.</span><span class="stamp" aria-hidden="true">Fact</span><span class="ans">Fact. You can look it up.</span></div>
  </div>
</div>
```

- A chip is a `<div>` holding exactly three spans in this order: the sentence, the stamp, the answer. No nested `<div>`.
- `data-k` sets the stamp and pressed colour: `describe` green, `assume` brass, `object` red, `neutral` grey.
- The stamp is the verdict in one to three words, 2 to 14 characters. It must match the first words of the answer.
- The answer starts with the verdict as its own sentence, then gives the reason in one or two sentences. No leading dot.
- `.passage` is optional and holds a two to four sentence original argument. See section 9.

### Left-then-right screen: `figure.screen` (optional)

Use only when the session taught doing the work in the stimulus before reading the choices. Copy the block unchanged. The caption is one line of at most eight words.

### Pieces carried over for primers and references

`table.t` inside `.table-wrap`, `.rule` (one conditional written as a sentence with `<span class="ar">` arrow), `.opposite` (two-sided comparison) and plain `<ul>`. Styled in the same look. Available in a recap when the content needs them.

## 5. What the script adds (never hand-write these)

| Added | Where | Source |
|---|---|---|
| Section number chip (01, 02 ...) | before each kicker | CSS counter |
| Left rail of section links (screens 1280px and wider) | `.rail ol` | each section's kicker, or its h2 when the kicker is empty |
| Reading progress bar | `.progress i` | scroll position |
| "Tap" cue on each chip | before the stamp | script |
| Counter "N of M checked" with dots | `.drill-head` | script |
| Turn arrow on each flag | start of `.flag` | script |
| Tick boxes on `ol.todo` | start of each item | script; saved per device under the lesson marker |
| Section fade-in on scroll | `section` | script; off when the reader asks for reduced motion |
| Tilt toward the pointer | any `[data-tilt]` | script; mouse only, off for reduced motion |

Because the tick boxes save under the lesson marker, two pages must never share a marker.

## 6. Fixed wording

These strings are part of the design. Do not reword them per student.

| String | Where |
|---|---|
| `Session recap · <Month day>` | recap kicker |
| `Before you start · <drill name>` | primer kicker |
| `Reference · Keep it open while you drill` | reference kicker |
| `Tap` | chip cue |
| `N of M checked` | drill counter |
| `Step N done` | tick box label for screen readers |
| `LSAT U` | footer mark |
| `Not this one` | stamp for a wrong pick in a "which one" check |

Never visible to a student: "manual", "desk", "template", "Recognition drill", "Step zero", "The finalist", and every phrase in `wiki/COPY-CORRECTIONS.md`. The builder rejects em dashes, en dashes, "~", "concept lesson" and "establish".

## 7. Visual effects and why each exists

All of these live in `session-desk.css` and `session-desk.js`. This table is so a later edit keeps them, and so nobody adds decoration that has no job.

| Effect | How it is made | Its job |
|---|---|---|
| Paper ground with grain | warm `--ground` plus an inline SVG noise tile | one material for the whole page, per `design/principles.md` |
| Section sheets | `--plane`, 28px corners, a fine top highlight, a tight contact shadow and a soft lower shadow | each idea is one sheet on the desk |
| Small surface scale | ground, plane, card, well (pressed in), charcoal (focal) | depth without more boxes |
| 3D hero stack | CSS `perspective`, `preserve-3d`, `translate3d`; stacked 1px shadows give the cards thickness; slow bob; pointer tilt | shows the method as two things resting on a result |
| Step tokens on a thread | charcoal discs with a 3px base, joined by a dotted line | a procedure reads as a sequence |
| Thick tilting kind cards | stacked edge shadows, pointer tilt of 5 degrees | categories feel like cards you can pick up |
| Ruler ticks, quote mark | gradients on `.bar`; a large serif mark at 13% opacity | the edge detail carries the category's meaning |
| Switches and lamp | inset track, raised knob, radial-gradient lamp with a glow | a two-condition rule you can feel |
| Tilted paper tags | 1 to 2 degree rotation, red italic serif, turn arrow | warning words stand apart from running text |
| Charcoal credit panel | dark gradient, 4px base, brass quote mark | the one dark surface in a section draws the eye to the student's own win |
| Pressable rows | raised 3px; on press they drop 3px and lose the shadow | pressing gives the answer, like a key |
| Rubber stamp | bordered capitals at -5 degrees, scaling in from 1.9x | the verdict lands with weight |
| Taped passage | off-white sheet rotated half a degree with a tape strip | the stimulus is an object separate from the questions |
| Tilted screen | charcoal bezel in perspective, lit left pane, dim right pane | where to look first |

Limits that keep it tasteful: one dark focal surface per section; rotation never more than 2 degrees on anything holding a sentence; accent colours only carry meaning (green measurable or correct, brass interpretation or key rule, red trap or warning); every motion stops under reduced motion; text stays crisp, so no blur or texture sits behind a paragraph.

## 8. Writing standard, taken from the model

Authority order stays as SKILL.md sets it: Joshua's current instruction and dated corrections, then `wiki/teaching-voice.md` and `references/lsat-teaching-voice-standard.md`, then this model. The model shows what those rules sound like when followed. Check each draft against these patterns, with the model open.

| Pattern in the model | Example from the model | Check on your draft |
|---|---|---|
| Open on what most students do, then the better process | "Most students find the conclusion by hunting for a word like *but* or *therefore*." | The lede names a real habit and says why it fails. |
| Short declarative sentences | "Often it is. Not always." | No sentence carries more than one idea. Read it aloud. |
| Plain definitions before use | "Fact: Something you can measure or check." | Every term is defined in everyday words where it first appears. |
| A small everyday example beside each claim | the painting, Maya's desk, the bus route, the café menus | Each rule has a fresh example within two sentences. No test stimulus reproduced. |
| The reason, not only the rule | "That's an interpretation, because you can't measure a motive." | Every rule sentence is followed by why. |
| A test the student can ask themselves | "Could I measure it or look it up?" | Each category or step gives a question to ask. |
| Limits stated honestly | "It doesn't have to be a good one. The author has to be trying." | Overstated rules are narrowed, not dropped. |
| Process over result | "On test day you can't repeat a result. You can repeat a process." | The note teaches what to do, not what the answer was. |
| Credit that is specific | "You asked whether the sentence with the *but* was a premise." | The credit line could only be about this student. |
| Headings that say something | "Pivot words turn the direction, nothing more" | No heading is a bare category label. |
| Contractions and second person | "you haven't read it yet" | It reads like Joshua talking to one student. |

Length: the model's recap is about 1,400 words, practice answers included. Stay between 1,100 and 1,600 for a recap. A primer is 150 to 250 words. A reference is 350 to 600.

Every claim, example, hidden answer, stamp and gate verdict gets a counterexample attempt before handoff. The look being approved does not approve the reasoning in a new note.

## 9. Practice checks standard

- Two or three checks, at least five rows in total. The model has a five-row sort and a three-row "which one".
- The first check drills the session's core distinction on single sentences. The last check runs the full method on one short original argument in a `.passage`.
- At least one row must be the trap the recap warned about, so the student meets it (the model's "too few riders" row and its fact after *but*).
- Rows reuse the recap's own examples where possible, then add one or two new ones.
- Each check's `<h3>` is the instruction. The `.hint` is the question to ask.
- Mix the verdicts so the answer cannot be guessed from position.

## 10. Primer and reference pages

Written in Markdown and built by the same command. They carry the same paper, sheets, type and tables. They have no 3D stage or practice checks, because the approved samples are short reading pages. If Joshua asks for more on these pages, add the piece to this spec first.

| Markdown | Becomes |
|---|---|
| `# Title` | h1 |
| first paragraph | the lede in the hero |
| other paragraphs before the first `##` | one opening sheet labelled with the page role |
| `## Heading` | a numbered sheet |
| numbered list | step tokens |
| bullet list | brass diamond bullets |
| table | card table that scrolls sideways on a phone |
| `> **Tag sentence** body` | callout with that tag |

Primer content, in this order: the task exactly as the real drill presents it (check the live drill, never infer from its name), how it is scored, the rule from the session, the trap it catches, one habit, what to do after a miss.

Reference content: what you are looking for, the method as a table or steps, where to look first, how to choose the answer, and a pointer back to the recap. Check any step count it cites against the recap as built.

## 11. Verification, with commands

Report each line as done, failed or not done. A builder pass is not a visual check.

1. **Builder:** all pages print `ok`.
2. **Model rebuild still passes:** `uv run --with markdown python -I build_session_desk.py --model`.
3. **Desktop render of each page.** The in-app browser pane is too narrow for this, so use headless Chrome, then open the PNG:
   ```
   "/c/Program Files/Google/Chrome/Application/chrome.exe" --headless=new --disable-gpu --hide-scrollbars --user-data-dir="<scratchpad>/prof" --virtual-time-budget=4000 --window-size=1400,7600 --screenshot="<scratchpad>/recap.png" "file:///<folder>/recap.html"
   ```
   Look at every section, top to bottom, beside the model. Headless Chrome cannot go narrower than about 500px, so it is not a phone check.
4. **Phone width, in the browser pane:** set the mobile preset (375 wide), reload, then confirm `document.documentElement.scrollWidth === innerWidth` and that no element's right edge passes the viewport. Screenshot the hero, one kind card, the gate, one opened chip and the screen figure.
5. **Interactions, every one:** each chip opens by click and by Enter and Space, sets `aria-expanded`, shows its stamp and moves the counter; both switches reach all four gate states and the visible verdict matches section 4; each tick box toggles. Undo any tick you set so the page opens clean.
6. **Console:** no errors.
7. **Keyboard:** Tab reaches every chip, switch and tick box with a visible focus ring.
8. **Fonts:** Fraunces, Outfit and JetBrains Mono report as loaded. They come from Google Fonts with system fallbacks. Whether LSAT U's lesson frame allows that request has not been confirmed (see section 12).
9. **Copy:** the rejected-phrase table in `wiki/COPY-CORRECTIONS.md` checked across all pages, hidden answers included.
10. **Source sync:** the primary Markdown in `students/<slug>/recaps/` matches the built wording, stamps and verdicts included.

## 12. What must never change without Joshua

- The tokens in `:root`, the type stacks and the surface scale.
- The piece markup in section 4 and the fixed wording in section 6.
- Adding a new piece, a new colour or a new effect. Propose it, get approval, then add it to the CSS, this spec and the builder checks together.

Open items as of 2026-11-13, to settle before the first post in this look:

- Whether LSAT U's interactive-lesson frame loads Google Fonts. If it does not, the page still works in system fonts, but the fonts should then be embedded. Not yet tested on the platform.
- Whether saved tick boxes work inside the lesson frame. The script fails safe if storage is blocked.
- The gate verdict wording in the model depends on Joshua's open call about the fact rule in Lanae's note.
