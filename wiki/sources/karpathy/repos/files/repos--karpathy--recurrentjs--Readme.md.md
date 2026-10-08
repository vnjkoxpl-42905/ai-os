---
type: source
subject: "GitHub source repos/karpathy/recurrentjs/Readme.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/recurrentjs/Readme.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/recurrentjs/Readme.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/recurrentjs/Readme.md), SHA-256 `acb60d3ab87ebd07b197d20fe6879201ac9f7b23f8646526c16229f65475a5e3`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "# RecurrentJS RecurrentJS is a Javascript library that implements: - Deep **Recurrent Neural Networks** (RNN)".

PyTorch MADE reimplements a paper with masked autoregressive dependencies, contrasts cheap likelihood with sequential sampling and admits failure to reproduce claimed single-pass multi-mask gains; averaged multiple passes improve reported loss at added cost. Normalizing-flows README lists GPU/high-dimensional/image support and stable-update work as TODO, not implemented capability. Matlab Random Forest explicitly restricts itself to learning and recommends mature alternatives for serious use. Randomfun Rust notes are learning notes and broad claims about language safety need qualifications before practical reuse. Reader3 is a chapter-oriented EPUB-to-local-library/LLM co-reading illustration, explicitly mostly vibe-coded and unsupported. RecurrentJS exposes values/derivatives, expression graphs and optimizers but warns beta users must understand backprop; its example variable inconsistencies are not certified executable code. ReinforceJS marks continuous policy/actor-critic work very alpha and reuses RecurrentJS, so these are not independent implementation evidence. Researchlei separates citation acquisition and visual library while admitting sparse indexes and aggressive external throttling. RustBPE aims at a small fast training component interoperating with tiktoken inference; it explicitly discloses LLM-assisted Rust and compares equality against an author-understood Python reference rather than treating passing tests as proof of idiomatic Rust design.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

````text

# RecurrentJS

RecurrentJS is a Javascript library that implements: 

- Deep **Recurrent Neural Networks** (RNN) 
- **Long Short-Term Memory networks** (LSTM) 
- In fact, the library is more general because it has functionality to construct arbitrary **expression graphs** over which the library can perform **automatic differentiation** similar to what you may find in Theano for Python, or in Torch etc. Currently, the code uses this very general functionality to implement RNN/LSTM, but one can build arbitrary Neural Networks and do automatic backprop.

## Online demo

An online demo that memorizes character sequences can be found below. Sentences are input data and the networks are trained to predict the next character in a sentence. Thus, they learn English from scratch character by character and eventually after some training generate entirely new sentences that sometimes make some sense :)

[Character Sequence Memorization Demo](http://cs.stanford.edu/people/karpathy/recurrentjs)

## Example code

The core of the library is a **Graph** structure which maintains the links between matrices and how they are related through transformations. Another important building block is the **Mat** class which represents a 2-dimensional `N x D` matrix, its values in field `.w` and its derivates in field `.dw`. Here is how you would implement a simple Neural Network layer:

```javascript

var W = new R.RandMat(10, 4); // weights Mat
var x = new R.RandMat(4, 1); // random input Mat
var b = new R.RandMat(10, 1); // bias vector

// matrix multiply followed by bias offset. h is a Mat
var G = new R.Graph();
var h = G.add(G.mul(W, x), b); 
// the Graph structure keeps track of the connectivities between Mats

// we can now set the loss on h
h.dw[0] = 1.0; // say we want the first value to be lower

// propagate all gradients backwards through the graph
// starting with h, all the way down to W,x,b
// i.e. this sets .dw field for W,x,b with the gradients
G.backward();

// do a parameter update on W,b:
var s = new R.Solver(); // the Solver uses RMSProp
// update W and b, use learning rate of 0.01, 
// regularization strength of 0.0001 and clip gradient magnitudes at 5.0
var model = {'W':W, 'b':b};
s.step(model, 0.01, 0.0001, 5.0)
```

To construct and train an LSTM for example, you would proceed as follows:

```javascript

// takes as input Mat of 10x1, contains 2 hidden layers of
// 20 neurons each, and outputs a Mat of size 2x1
var hidden_sizes = [20, 20];
var lstm_model = R.initLSTM(10, hidden_sizes, 2);
var x1 = new R.RandMat(10, 1); // example input #1
var x2 = new R.RandMat(10, 1); // example input #2
var x3 = new R.RandMat(10, 1); // example input #3

// pass 3 examples through the LSTM
var G = new R.Graph();
var out1 = R.forwardLSTM(G, lstm_model, hidden_sizes, x1, {});
var out2 = R.forwardLSTM(G, lstm_model, hidden_sizes, x2, out1);
var out3 = R.forwardLSTM(G, lstm_model, hidden_sizes, x3, out2);

// the field .o contains the output Mats:
// e.g. x1.o is a 2x1 Mat
// for example lets assume we have binary classification problem
// so the output of the LSTM are the log probabilities of the
// two classes. Lets first get the probabilities:
var prob1 = R.softmax(out1.o);
var target1 = 0; // suppose first input has class 0
cost += -Math.log(probs.w[ix_target]); // softmax cost function

// cross-entropy loss for softmax is simply the probabilities:
out1.dw = prob1.w;
// but the correct class gets an extra -1:
out1.dw[ix_target] -= 1;

// in real application you'd probably have a desired class
// for every input, so you'd iteratively se the .dw loss on each
// one. In the example provided demo we are, for example, 
// predicting the index of the next letter in an input sentence.

// update the LSTM parameters
G.backward();
var s = new R.Solver();

// perform RMSprop update with
// step size of 0.01
// L2 regularization of 0.00001
// and clipping the gradients at 5.0 elementwise
s.step(lstm_model, 0.01, 0.00001, 5.0);
```

You'll notice that the Softmax and so on isn't folded very neatly into the library yet and you have to understand backpropagation. I'll fix this soon.

## Warning: Beta

This code works fine, but it's a bit rough around the edges - you have to understand Neural Nets well if you want to use it and it isn't beautifully modularized. I thought I would still make the code available now and work on polishing it further later, since I hope that even in this state it can be useful to others who may want to browse around and get their feet wet with training these models or learning about them.

## License
MIT




````

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
