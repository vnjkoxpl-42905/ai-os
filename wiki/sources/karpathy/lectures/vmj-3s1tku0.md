---
type: source
subject: "Karpathy video VMj-3S1tku0"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, youtube]
sources: ["../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/VMj-3S1tku0.md"]
semantic-status: complete-preserved-text-no-media-review
---

# The spelled-out intro to neural networks and backpropagation: building micrograd

Original: [VMj-3S1tku0](https://www.youtube.com/watch?v=VMj-3S1tku0); channel Andrej Karpathy. Upload date 2022-08-16. Captured 2026-10-08, compilation 2026-10-08. Automatic English captions, not verified against audio.

[Physical raw Markdown](../../../../raw/sources/karpathy-brain/raw/youtube/transcripts/VMj-3S1tku0.md). SHA-256: `359016a0d9045af81fc9622ad3f23fca3e65e8d15fc056a93ed20ac55043746f`. Physical byte hash differs from the older manifest. CRLF-to-LF normalized SHA-256 matches its hash `45d112a1b2de93c10e80269e93dc110c06480ceb4e31f4a6c4362cef711833e3` exactly. Raw bytes were preserved; normalized matching does not make the physical byte hashes identical.

## Reviewed evidence

Karpathy begins with an executable scalar autograd engine to expose the mechanism before tensor efficiency. In the reviewed bug section, a repeated node (a+a) gives an incorrect gradient of one instead of two because assignments overwrite contributions; gradient accumulation is the proposed fix. This is pedagogical simplification, not a recommendation to deploy scalar neural networks.

> [00:06:44] the fundamental level and then you can

> [00:06:46] speed it up later okay so here's the fun

The repeated-node derivative should be two, and the fix accumulates contributions rather than overwriting them:

> [01:23:24] should be uh two

> [01:25:26] have to accumulate these gradients these

> [01:25:28] gradients add

## Sequential compilation of the full preserved transcript

At 00:08-00:19, the derivative is introduced as local sensitivity. Karpathy plots a simple quadratic, perturbs one input by a small h, asks for the predicted sign, runs the calculation, and checks the numerical result against the analytic derivative. Very small h has floating-point limitations. The same method extends to a three-input expression, predicting how each input changes the result before measuring it.

At 00:19-00:32, Value first wraps a scalar, then supports addition and multiplication. The expected arithmetic result is checked before adding parent pointers, operation labels, and a graph visualization. Visualization nodes for operations are explicitly distinguished from actual Value objects. The grad field stores the derivative of the final output with respect to each intermediate value, preparing for a backward pass.

At 00:32-00:53, he manually derives gradients for a small expression and repeatedly checks them using finite differences. A simple dependency explanation of the chain rule replaces a confusing symbolic presentation. Local derivatives multiply the downstream derivative; an addition distributes it unchanged. A small step in the gradient direction raises the selected output, demonstrating why gradients can guide optimization. This is an ascent demonstration, not a prescription to increase a training loss.

At 00:53-01:09, the same reasoning is applied to a two-input neuron with weights, bias and tanh. Inputs are chosen to make intermediate results understandable. A zero input gives its corresponding weight a zero gradient, explained by its lack of influence on the output. An operation can sit at an arbitrary abstraction level if its local derivative is known; the lecture does not demand atomizing every operation forever.

At 01:09-01:22, manual calculations become backward closures, then a reverse topological traversal, then one public backward method. He leaves an actual None-returning callback mistake in the lesson, fixes storing the function instead of calling it, and checks that automated gradients match the earlier manual values. Topological ordering ensures dependencies contribute before processing a node.

At 01:22-01:27, the initially successful single-neuron example is challenged with a repeated variable. The a+a counterexample exposes assignment overwriting; accumulation with += fixes both aliasing and contributions from separate branches. He checks the corrected derivative of two, then cleans intermediate demonstration code. The next portion decomposes tanh into smaller operations to show equivalent outputs and gradients.

At 01:28-01:44, supporting ordinary numbers requires wrapping non-Value operands and reflected multiplication. The lecture prompts learners to pause and derive backward expressions for exponentiation and scalar powers. Division and subtraction reuse existing operations. Replacing one tanh node with equivalent smaller operations must preserve both output and leaf gradients, and the lesson checks both. A PyTorch comparison uses double precision to match Python floats, explicitly enables gradients for leaf tensors, and reproduces the manual outputs and derivatives. This comparison is shown in the lecture; it was not rerun during this compilation.

At 01:44-02:10, a neuron becomes a layer and then a multi-layer perceptron. Each layer independently evaluates its neurons, while layers compose sequentially. Four labeled examples provide target values. The loss is described as mean squared error but the displayed explanation sums the squared differences; the transcript should not be treated as a precision specification of reduction settings. Parameters are collected explicitly and adjusted against the gradient to decrease the loss. Predicted outputs and actual loss are inspected after updates. Too-small learning rates converge slowly; too-large steps can become unstable because derivatives provide local information.

At 02:10-02:14, a second bug changes how to interpret the earlier rapid convergence: gradients were never reset between optimization steps. The += accumulation needed within one backward pass also carries contributions across passes unless cleared. He resets every parameter gradient before backward, reinitializes, and reruns. The simple dataset had let buggy code appear successful. Thus a low loss alone is not enough to establish correct training semantics.

At 02:14-end, the lecture connects expressions, targets, loss, backpropagation and repeated optimization, then walks the contemporaneous micrograd repository. Differences include ReLU rather than the lesson's tanh, a shared Module with zero_grad, and tests comparing forward and backward values against PyTorch. A larger classification demo introduces batching, a different loss, regularization and learning-rate decay; some of these are explicitly deferred rather than fully taught. The production PyTorch kernel search exposes additional device and dtype complexity while retaining the same local derivative. A custom autograd function needs a forward implementation and local backward gradients. The outtakes are also read; no additional method is inferred from them.

## Coverage and interpretation

Status: **complete-preserved-text-no-media-review**. Reviewed line ranges: 1-4259, covering all metadata and all preserved timestamped caption cues sequentially. Full file remains local and linked. This is complete reading of the preserved text, not verification of caption accuracy, audio, visuals or missing speech.

The quoted passages support local teaching/building methods only within their stated scope. Captions contain recognition errors; quotations preserve those errors rather than silently correcting them. No linked code, papers, diagrams or media was independently executed or inspected. Source upload dates do not establish current tool capabilities.

Related: [Karpathy index](../../../karpathy/index.md), [principles](../../../karpathy/principles.md), [methods](../../../karpathy/methods.md).
