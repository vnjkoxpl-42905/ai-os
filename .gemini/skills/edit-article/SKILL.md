---
name: edit-article
description: Edit and improve articles by restructuring sections, improving clarity, and tightening prose. Use when user wants to edit, revise, or improve an article draft.
disable-model-invocation: true
---

## Current AI OS execution contract

Use paragraph length as a readability heuristic, not a 240-character truncation rule. Preserve complete reasoning and existing approved scope; do not impose a new approval question for each section already authorized.

1. First, divide the article into sections based on its headings. Think about the main points you want to make during those sections.

Consider that information is a directed acyclic graph, and that pieces of information can depend on other pieces of information. Make sure that the order of the sections and their contents respects these dependencies.

Confirm the sections with the user.

2. For each section:

2a. Rewrite the section to improve clarity, coherence, and flow. Use readable paragraph lengths without truncating complete explanations.
