# House look for LSAT U notes

Set on 2026-11-17 from Joshua's corrections to Sara Altuwaijri's note (about twenty rounds of visual and wording fixes that a first draft in this look would have avoided). Use it as the starting point for the visual treatment. It does not replace the [lesson quality bar](lesson-quality-bar.md) or the shell at `wiki/homework-assigning/model-note/note-shell.html`; it says what to do with them.

A working example is [the Sara builder](examples/sara-2026-11-16-note-builder.py). It renders any number of notes from one set of block renderers and writes the HTML and a Markdown fallback together, so the two cannot drift. Copy it, replace the content blocks, keep the renderers and the palette.

## Palette: no beige

Joshua rejected the shell's dark beige ("not as dark beige, off-white like 7Sage, high contrast, sleek"). The shell file stays untouched. The builder overrides its color variables and swaps its warm brown shadows for neutral ones:

- Page `#F4F4F1`, cards and sections pure white, text near-black `#101010`, thin neutral rings instead of 3D bottom edges.
- Accents stay: green for evidence, brass for conclusion, red for the unstated assumption, each as a light tint over white.
- No paper-grain background image.

## What reads as cheap, so leave it out

- A dark box with a giant quote glyph for what the student said.
- Ruler ticks and giant decorative glyphs on cards, and hover tilt (`data-tilt`) on content cards.
- Warm brown drop shadows. Decorative motion. Labels that name the tool or the draft.

## Components, and when to use each

| Need | Component | Rule |
|---|---|---|
| An argument, in any example | Equation card: evidence row, a "+" and an Assumption row when one is missing, a rule line with "so", then the conclusion row | Evidence green, assumption red dashed, conclusion brass. A failing argument strikes the conclusion and labels it "Falls" or "Doesn't follow" |
| The same three ideas named in a sentence | Inline marks `[[ev:...]]`, `[[co:...]]`, `[[as:...]]` | One fixed color per idea across the whole note, so the reader learns the code once |
| A graded set of options (required or enough, strong or weak) | Ladder: one row per option, two labeled yes/no pills | Every row answers both questions. Never a bullet list that implies the answer |
| Two or three things to tell apart | Kind cards: definition, looks like, test | Flat card, no decoration |
| Two directions of one idea | Opposite panels | Name them with the teacher's words (Linking, Defender) |
| The test the student runs | Switch gate, then numbered steps, then one worked example | Show the example as an equation card |
| What the student said in the session | "What you said" block | Small label, her words in plain quotes, then a takeaway in normal text. Clean garbled speech with an ellipsis, never invent words. Quotes are optional; drop one that confuses |
| A routine to run on every question | The shell's screen figure with 4 numbered steps | Steps restate what the note taught |

## Writing rules that were violated and corrected

- State the concept in the teacher's terms. A necessary assumption is an idea the author **has to agree with**. The trap is an answer the author only **might** agree with. A first draft said "agreeing isn't the test" and was wrong.
- Use the teacher's own labels and the platform's: floor, main assumption, linking, defender, and the drill card's "missing idea" and "rule out an objection".
- One scope per note. A scope shift in the session becomes a second, shorter note with its own lesson id. Strict word count (hidden answers included) stays at or under 2,100.
- Ask what each example is for. A cash register example is the evidence, the gap and the conclusion; show it as an equation card, then ladder the amounts.

## Rendering and tooling gotchas

- Avoid `color-mix()`: the in-app browser pane painted a row blank with it. Use plain hex or rgba.
- Do not reuse the shell's class names (`.rule`, `.chip`, `.quote`, `.kind`) for new parts. A new `.rule` inherited the shell's rounded box. Give new parts their own names.
- The shell reveals sections on scroll. For a screenshot, scroll with real ticks, then wait two seconds; jumping with `scrollTo` can leave sections faded.
- Check three widths (375, 820, 1280) and the real Chrome tab as well as the pane. Test taps with a real click; a scripted `.click()` does not open the tap-to-check rows.
- Serve the preview folder with a static server on a fixed port, open it for Joshua yourself as soon as the first full draft exists, and keep it running.
- In Bash heredocs a backslash collapses. Write helper scripts to the scratchpad and run them by path.
