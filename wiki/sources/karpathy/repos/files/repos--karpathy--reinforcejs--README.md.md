---
type: source
subject: "GitHub source repos/karpathy/reinforcejs/README.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/reinforcejs/README.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/reinforcejs/README.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/reinforcejs/README.md), SHA-256 `28c323f2068abab7cb3fab53c1cba9f8ac68da5305fbfd88483026059dc3b709`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "# REINFORCEjs **REINFORCEjs** is a Reinforcement Learning library that implements several common RL algorithms, all".

PyTorch MADE reimplements a paper with masked autoregressive dependencies, contrasts cheap likelihood with sequential sampling and admits failure to reproduce claimed single-pass multi-mask gains; averaged multiple passes improve reported loss at added cost. Normalizing-flows README lists GPU/high-dimensional/image support and stable-update work as TODO, not implemented capability. Matlab Random Forest explicitly restricts itself to learning and recommends mature alternatives for serious use. Randomfun Rust notes are learning notes and broad claims about language safety need qualifications before practical reuse. Reader3 is a chapter-oriented EPUB-to-local-library/LLM co-reading illustration, explicitly mostly vibe-coded and unsupported. RecurrentJS exposes values/derivatives, expression graphs and optimizers but warns beta users must understand backprop; its example variable inconsistencies are not certified executable code. ReinforceJS marks continuous policy/actor-critic work very alpha and reuses RecurrentJS, so these are not independent implementation evidence. Researchlei separates citation acquisition and visual library while admitting sparse indexes and aggressive external throttling. RustBPE aims at a small fast training component interoperating with tiktoken inference; it explicitly discloses LLM-assisted Rust and compares equality against an author-understood Python reference rather than treating passing tests as proof of idiomatic Rust design.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

````text
# REINFORCEjs

**REINFORCEjs** is a Reinforcement Learning library that implements several common RL algorithms, all with web demos. In particular, the library currently includes:

- **Dynamic Programming** methods
- (Tabular) **Temporal Difference Learning** (SARSA/Q-Learning)
- **Deep Q-Learning** for Q-Learning with function approximation with Neural Networks
- **Stochastic/Deterministic Policy Gradients** and Actor Critic architectures for dealing with continuous action spaces. (*very alpha, likely buggy or at the very least finicky and inconsistent*)

See the [main webpage](http://cs.stanford.edu/people/karpathy/reinforcejs) for many more details, documentation and demos.

# Code Sketch

The library exports two global variables: `R`, and `RL`. The former contains various kinds of utilities for building expression graphs (e.g. LSTMs) and performing automatic backpropagation, and is a fork of my other project [recurrentjs](https://github.com/karpathy/recurrentjs). The `RL` object contains the current implementations:

- `RL.DPAgent` for finite state/action spaces with environment dynamics
- `RL.TDAgent` for finite state/action spaces
- `RL.DQNAgent` for continuous state features but discrete actions

A typical usage might look something like:

```javascript
// create an environment object
var env = {};
env.getNumStates = function() { return 8; }
env.getMaxNumActions = function() { return 4; }

// create the DQN agent
var spec = { alpha: 0.01 } // see full options on DQN page
agent = new RL.DQNAgent(env, spec); 

setInterval(function(){ // start the learning loop
  var action = agent.act(s); // s is an array of length 8
  //... execute action in environment and get the reward
  agent.learn(reward); // the agent improves its Q,policy,model, etc. reward is a float
}, 0);
```

The full documentation and demos are on the [main webpage](http://cs.stanford.edu/people/karpathy/reinforcejs).

# License

MIT.

````

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
