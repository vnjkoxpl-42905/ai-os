---
title: Note formula
type: rules
status: derived 2026-11-14 from Joshua's Lanae note and the notes he assigned 2026-10-25 to 2026-11-13; his corrections win
---

# Note formula: how a note is built and how it reads

Sources: the Lanae note (`model-note/Lanae - Finding the Conclusion by Asking Why.html`, 1,526 words, 7 sections) and the live notes for Charles, Sofia, Celia, Zeina, Ore and Yahunathan in `notes-archive/`. Zeina's 2026-11-13 notes are the only posted ones that already use the Lanae shell. Charles's and Sofia's November notes use an older, plainer shell.

To build a note: copy [model-note/note-shell.html](model-note/note-shell.html), fill the `{{slots}}`, delete components you do not need, and do not edit the CSS or script. The shell is the Lanae page with the body turned into one example of every component.

## The two kinds of note

Vocabulary is settled in `CONTEXT.md` (Joshua, 2026-11-14). There are two kinds of note. A guided drill already carries its own intro, so a short note beside a drill is an exception, not a kind.

| Kind | When | Words | Kicker | Sections |
|---|---|---|---|---|
| **Teaching note** | One idea the student has not had a note on, or needs again | 1,000 to 2,100 (Lanae 1,526) | `Session recap · <Month D>` | hero, then 5 to 7 sections, ending with "What to do next" |
| **Warm-Up** | A standing set that gets her into LSAT mode before a section; not built from a session | about 730 for the picker, 410 to 450 per version | `Before test day · The warm-up` | a picker, then one note per version; no session recap |

A post-session note is a teaching note with this session's recap inside it. An **adapted note** reuses an earlier teaching note's teaching and always gets a fresh recap.

**Short notes beside a drill.** Observed before the vocabulary was settled and posted under the names "Before you start" (about 300 words), "Reference" (270 to 650) and "Follow-up" (600 to 720, Charles 2026-11-03 to 05). Those names are retired. Write one only when a drill has no intro of its own, or when the note teaches the idea the drill practises. Keep it to the same quality bar.

## The teaching note, section by section

The Lanae order. Each section has a small-caps kicker and an h2 that states the idea.

1. **Hero.** Kicker. Title in two lines, a plain phrase for what the student learns. A lede of 3 to 4 sentences: what most students do, why it fails, then the check that always works. Three floating cards: two checks and the result.
2. **Read it first** (steps). The process, 3 to 4 numbered steps, each a bold instruction plus one or two sentences and a quoted example. Ends with a callout: the lesson is the process, not the one answer.
3. **Two kinds** (two-card contrast). The either/or the student must tell apart: definition, "looks like", "test". Then a callout naming a trap with a concrete case.
4. **The check** (steps, optionally the switch gate). The test in two questions. A callout: one check is not enough.
5. **Keywords or the trap** (flags, trap callout, quote). What the signal words do and do not tell you. A trap callout. Then the student's own words from the session, quoted back: "You said it yourself... That's the right question."
6. **Try it** (tap-to-check). 3 to 5 real sentences or answers from the session. Each reveals a label and one sentence of reasoning.
7. **On every question** (the screen). Left side is the work, right is the answers. 4 to 5 steps. Then **What to do next**: tasks named as they are on the platform, and "Send me a message on the platform if you have a question."

## How it reads

- **Open on the mistake.** "Most students find the conclusion by hunting for a word like but or therefore. Those words help when they show up, but plenty of conclusions don't have one."
- **Teach the reasoning, not the verdict.** "A fact isn't something you prove. It's something you use as proof." "The root of evidently is evidence: the author is reading it, not just reporting it."
- **Second person, short sentences, plain verbs.** "Say it in your own words." "Question it like a lawyer would." One idea per sentence. A term gets defined the first time it appears.
- **Everyday scenes for examples.** The bus route, the cafe, the pool, Maya's desk, Lena at the gate. Then the LSAT version.
- **Name the trap out loud.** "The trap that costs the most." Say what students do, then what to do.
- **Say what is unclear.** "Not always. The LSAT is never black and white." "Judge the idea, not the word."
- **Charles-style short notes** drop the hero cards for a routine and a table: "Nothing here is new. What you add is a routine that holds up across ten questions." "Spend your effort on the stimulus, and let the conclusions do the cutting."
- **Labels are one line:** "Fact. You can look it up." "Not this one. Nila's shop could qualify even if most shops did not file."
- **Banned in anything a student reads:** em-dashes, "delve", "unlock", "seamless", "robust", "game-changer", "Great question", "Certainly", and a paragraph that opens with Moreover, Furthermore or Additionally. A note is a "note". Never "conceptual note", never "session recap page".

## The recap lives inside the note

The recap is two things in the teaching note: the kicker (`Session recap · October 29`) and the quote of what the student said or asked. The "Try it" items are the real sentences and answers from that session. Nothing else in the note is about the session; the rest teaches the idea.

## Gaps against the Lanae look

| Gap | State |
|---|---|
| **Fraunces headings** | Embedded in the shell on 2026-11-14 (latin roman 67 KB and italic 81 KB, from Google Fonts, SIL Open Font License, files in `model-note/fonts/`). The Lanae file itself still loads Fraunces from Google Fonts, which the LSAT U lesson validator rejects, so it cannot be posted as it stands. Zeina's 2026-11-13 note names Fraunces but embeds nothing, so she sees Palatino or Georgia. Her notes would need rebuilding from the shell to match. |
| **Outfit body** | Embedded in the shell (32 KB, from the vault's design prototypes). |
| **JetBrains Mono labels** | Not embedded; falls back to Cascadia Mono or Consolas. The only local copies are Nerd Font builds, too heavy. |
| **Paper grain** | Kept in the shell. The nested `url(%23n)` is percent-encoded so the validator does not read it as a file. |
| **Real platform question** | Not in the Lanae note. Its "screen" is a schematic. Embedding the real drill question is unbuilt. |
| **Zeina's grain** | Her note dropped the grain texture to pass the validator. |
