---
name: lsat-drill-builder
description: Generate a new LSAT "argument dissection" drill in the same interactive style as the First Sentence vs Rebuttal drill, for any LR topic. Use when Joshua asks to build, create, or generate a drill, a dissection lab, an argument-parts practice set, or a "drill like the rebuttal one" for a new topic (assumptions, flaws, strengthen/weaken, parallel reasoning, conclusion ID, etc.). Produces a standalone single-file HTML drill with all the same features.
---

# LSAT Drill Builder

This skill regenerates the interactive argument-dissection drill for a new topic by reusing a finished template and swapping only the content. Every interaction, animation, color rule, and scoring behavior carries over automatically because you do not rewrite the engine. You replace two data blocks.

## What you are building

A standalone, single-file HTML drill (no dependencies, runs offline, persists to localStorage) where a student dissects ~20 LSAT stimuli step by step: identify indicator words, select the main conclusion, classify the structure, then select the supporting/opposing parts. It ends with a session review and an interactive answer key.

## The template

`assets/drill-template.html` is the complete, working drill. Treat it as the engine. Do NOT touch the CSS, the JavaScript functions, the step flow, the animations, or the review/answer-key code. You only edit content.

## The only two things you change

1. **`const drillsData = [ ... ];`** the array of questions.
2. **`const drillExplanations = { ... };`** the per-question coaching text.

Both are near the middle of the file. Find them by searching for `const drillsData = [` and `const drillExplanations = {`.

### drillsData item shape

```js
{ id: 1, type: 'first', parts: [
    {id: 'p1', text: "Sentence with <i-w t=\"Opinion Indicator\">should</i-w> tagged.", isC: true},
    {id: 'p2', text: "A supporting sentence.", isS: true},
    {id: 'p3', text: "Another supporting sentence.", isS: true}
], feedback: "One short paragraph explaining the dissection." }
```

- `id`: 1-based, sequential.
- `type`: the structure the student must classify. Use `'first'` or `'rebuttal'` for this drill family. If a NEW topic needs different categories, see "Adapting the classification step".
- `parts`: each sentence/clause of the stimulus, in order. Flags:
  - `isC: true` = main conclusion (exactly one per question).
  - `isS: true` = support / premise (zero or more).
  - `isO: true` = opposing viewpoint (zero or more). A part can be both `isO` and `isS`.
- `text`: the sentence. Wrap indicator words inline as `<i-w t="Type">word</i-w>`. Escape quotes inside JS strings: `<i-w t=\"Premise Indicator\">because</i-w>`.

### Indicator word types (the `t="..."` values)

Use exactly these so colors map correctly:

- `"Conclusion Indicator"`: so, thus, hence, therefore, it follows, as a result, consequently, this shows that, conclude
- `"Premise Indicator"`: for, after all, because, since (do NOT tag "and")
- `"Pivot"`: but, yet, however
- `"Opposing Viewpoint"`: some people say, it is commonly believed, some economists believe, etc.
- `"Concession Indicator"`: although, while, despite, granted, naturally
- `"Opinion Indicator"`: clearly, obviously, evidently, ought, must, should

Colors are driven by type: Premise/Support = orange, Opposing = red, Pivot = purple, Concession = grey. Don't invent new type strings without also adding a color in `parseIndicators`.

### drillExplanations item shape

```js
1: {
    title: "Short scannable title",
    why_conclusion: "Why that sentence is the conclusion.",
    why_structure: "Why this structure classification.",
    why_follow_up: "Why those are the supports / opposing view.",
    takeaway: "One or two tight sentences naming the identifying signal."
}
```

- Keys must match the `id`s in `drillsData`.
- Write `title` and `takeaway` in Joshua's LSAT U voice. If the `lsat-u-voice` skill is available, use it. Voice in one line: concrete, confident, no hedging, no em dashes, a short punchy landing. The `takeaway` should point at the actual tell (the indicator word or the structural move), not vague encouragement.

## Step-by-step procedure

1. **Get the topic and the stimuli.** Ask Joshua which LR topic and whether he's providing the 20 stimuli or wants you to draft them. Never invent LSAT questions silently; confirm source.
2. **Read `assets/drill-template.html`** so you know the exact current formatting.
3. **Write the new `drillsData`**: tag every indicator word, set isC/isS/isO on every part, write a short `feedback` per question.
4. **Write the new `drillExplanations`** with matching ids, in voice.
5. **Replace only those two blocks** in a copy of the template. Leave everything else byte-for-byte.
6. **Update the homepage title** (search for `First Sentence vs Rebuttal Drill`) and the drill context label if the topic name should change.
7. **Verify** (see below).
8. **Save** as `<Topic Name> (drill).html` in Joshua's selected folder and present it.

## Adapting the classification step (only if the new topic needs it)

Step 3 offers two buttons: "First-Sentence Conclusion" and "Rebuttal", validated against `type`. If the new topic classifies something else, change the two button labels in `renderDrillControls` (search for `selectStructure('first')`) and the `type` values in `drillsData`. Keep the two-option pattern unless Joshua asks for more. If a topic doesn't need a classification step at all, ask Joshua before removing it, since it touches the step flow.

## Verification (always run before delivering)

- Syntax-check the inline JS: extract the `<script>` block and `new Function(it)` in Node. Must parse.
- Every `drillExplanations` id has a matching `drillsData` id and vice versa.
- Each question has exactly one `isC`; every `'first'` has at least one `isS`; every `'rebuttal'` has a selectable step-4 target.
- No `<i-w>` tag wraps the word "and".
- Walk it mentally: homepage to drill to review to answer key.

## Features that must keep working

Indicator-word breathing pulse (reduced-motion aware), wrong-answer shake/flash, selected-phrase glow, step feedback banners, staggered entrance animations, skeleton loaders, toasts, hover tooltip on revealed indicators, multi-select supports/opposing with lenient wrong-clicks, clean/recovered/assisted scoring, collapsed per-question breakdown, interactive answer key with clickable jump-back, Prev/Next nav, percentage-only progress, localStorage autosave, full keyboard/ARIA support. All live in the untouched engine, so they survive as long as you only edit the two data blocks.
