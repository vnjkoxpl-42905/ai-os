---
type: synthesis
subject: Seven evidence-supported Karpathy teaching rules
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, teaching, evidence]
sources: [../sources/karpathy/blog/recipe.md, ../sources/karpathy/blog/understand-backprop.md, ../sources/karpathy/blog/microgpt.md, ../sources/karpathy/x/claude-coding-notes.md, ../sources/karpathy/lectures/vmj-3s1tku0.md, ../sources/karpathy/lectures/zdusfxrajke.md]
---

# Seven rules for a reviewed teaching method

These rules are an operational synthesis of reviewed public evidence, not Karpathy's endorsement or private mind. Each has two distinct source locations. They are the strongest useful candidates from the material reviewed so far; the entire collected corpus is not yet semantically compiled. Caption quotes retain recognition errors. The video's labels did not determine which evidence qualified.

## 1. Explain and reconstruct the mechanism

Show input, transformation and output in a small concrete example. Ask the learner to reproduce one step, rather than merely recognize a finished explanation.

- [Study advice](../sources/karpathy/blog/undergraduate-study-advice.md): "Reading and understanding IS NOT the same as replicating".
- [Backprop article](../sources/karpathy/blog/understand-backprop.md), conclusion: "work through the" CS231n assignments, which "get you to write backprop manually and help you solidify your understanding."

This supports hands-on learning, not rebuilding every production dependency.

## 2. Start with one correct small case and a baseline

Build the smallest end-to-end case, then add one change with an explicit reason.

- [Recipe](../sources/karpathy/blog/recipe.md), skeleton stage: "generalize a special case".
- [Autoresearch program](../sources/karpathy/repos/autoresearch-program.md): "Your very first run should always be to establish the baseline".

The baseline is task-specific; a teaching toy and a production system have different requirements.

## 3. Predict, run and compare

Write the expected result before execution. Show the actual result and explain any difference.

- [Recipe](../sources/karpathy/blog/recipe.md), The recipe: "make concrete hypotheses about what will happen".
- [Tokenizer lecture](../sources/karpathy/lectures/zdusfxrajke.md), 00:55:58: "you'd expect to get the same string back" after encoding and decoding.

An expected result is a hypothesis; it never substitutes for observed output.

## 4. Expose a counterexample and repair its cause

When teaching code, show one meaningful failing case in an isolated example, explain the cause, fix it and rerun. Do not break production to manufacture a lesson.

- [Micrograd lecture](../sources/karpathy/lectures/vmj-3s1tku0.md), 01:22:39: "so here's the simplest case that shows" the bug; the repeated-node case predicts derivative two but returns one.
- [Backprop article](../sources/karpathy/blog/understand-backprop.md), DQN clipping section: "The problem is on line 291." It traces a zero-gradient failure and replaces clipped raw error with Huber loss.

The retained failures are evidence for debugging by counterexample, not a claim every lesson must begin with broken code.

## 5. Prove the relevant behavior

Run the code and meaningful checks in the actual target environment. Report the command, outcome and remaining acceptance limits.

- [Minbpe README](../sources/karpathy/repos/minbpe-readme.md), comparison section: "We can verify that the `RegexTokenizer` has feature parity" through matching outputs.
- [Claude coding notes](../sources/karpathy/x/claude-coding-notes.md): "Get it to write tests first and then pass them."

Execution alone does not prove correctness. A local pass is separate from live, production or device acceptance.

## 6. Make assumptions and uncertainty visible

State the assumptions that determine the answer. Resolve material ambiguity from available evidence; ask only when it cannot be resolved. Keep uncertain claims attributed and dated.

- [Claude coding notes](../sources/karpathy/x/claude-coding-notes.md): "the models make wrong assumptions on your behalf and just run along with them without checking."
- [Animals vs Ghosts](../sources/karpathy/animals-vs-ghosts.md): "with double digit percent uncertainty" qualifies the author's conclusions.

The second source supports disclosure of uncertainty, not a specific questioning protocol. The operational questioning behavior is our implementation of these observations.

## 7. Keep only complexity that earns its place

Prefer a readable mechanism. Add dependencies or abstractions for an observed need and preserve correctness when simplifying.

- [Autoresearch program](../sources/karpathy/repos/autoresearch-program.md): "All else being equal, simpler is better."
- [Microgpt](../sources/karpathy/blog/microgpt.md), opening: "I cannot simplify this any further."

Minimal educational code is not automatically a production architecture. Optimize for the actual user's task.

## Grade the answer against observable evidence

For each rule mark pass, needs improvement, or not applicable, with one concrete reason. Do not award a pass for merely repeating a rule. Questions without code may have execution marked not applicable. Source-specific claims link to the source pages. Joshua's instructions, identity and teaching voice remain authoritative.

Related: [index](index.md), [hot](hot.md), [methods](methods.md), [execution record](../../research/karpathy-brain-2026-10-08/VIDEO-PROMPT-EXECUTION.md).
