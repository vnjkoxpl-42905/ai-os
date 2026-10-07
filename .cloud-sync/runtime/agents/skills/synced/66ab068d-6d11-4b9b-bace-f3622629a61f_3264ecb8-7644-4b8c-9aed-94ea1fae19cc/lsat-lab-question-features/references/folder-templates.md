# Folder + README templates

Keep everything in one folder named `LSAT Lab - Question Features` so sets accumulate
in a single library. Create it (and the README) only if it doesn't already exist;
otherwise just add the new `PrepTest <n> - Section <n>.md` file alongside the others.

## README.md

```markdown
# LSAT Lab — Question Features

This folder collects question-feature data pulled from my LSAT Lab account.

## Contents

- **Question Features Glossary.md** — The full glossary of all question features
  from LSAT Lab's Logical Reasoning Glossary, each with its complete description.
- **PrepTest <n> - Section <n>.md** — The question features for every question in a
  practice set.

## How this is organized

The Glossary is the reference (what each feature means). Each PrepTest file is a
per-question mapping (which features each question carries).

## Adding more practice tests

One file per section, same format:

- File name: `PrepTest <number> - Section <number>.md`
- Inside: a table with columns Question | Question Features, with PrepTest and
  Section noted at the top.
```

## Per-set file template

```markdown
# PrepTest <N> — Section <N> (<LR or RC>)

Question features for each question in this set, pulled from LSAT Lab's Question
Details panel. <count> questions. Questions marked *(none)* had no Question Features
tags in LSAT Lab.

| Question | Question Features |
|---|---|
| 1 | ... |
```
