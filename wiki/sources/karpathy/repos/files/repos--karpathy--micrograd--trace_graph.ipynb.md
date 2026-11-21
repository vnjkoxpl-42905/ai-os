---
type: source
subject: "GitHub source repos/karpathy/micrograd/trace_graph.ipynb"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/micrograd/trace_graph.ipynb]
semantic-status: complete-named-text-read
---

# repos/karpathy/micrograd/trace_graph.ipynb

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/micrograd/trace_graph.ipynb), SHA-256 `e75fc7682da23d0e6a87dbc6ab2efaa21b95e109dc4db516b89eff3a28193300`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
{ "cells": \[ { "cell_type": "code", "execution_count": null, "metadata": {}, "outputs": \[\], "source": \[ "#
```

Four micrograd artifacts fully text read. Generated Graphviz SVG encodes simple2D neuron weighted products/additions/ReLU with data and gradients visible, not a new authored essay. Package init empty. Engine tests mirror nonlinear branching, repeated-node accumulation, powers/division/negative operations against PyTorch double forward and backward outputs, one exact and one1e-6 tolerance, read not run. Trace notebook recursively records unique value nodes and dependency edges, labels intermediate data/grad and operations, asserts graph direction, demonstrates tiny scalar and seeded2D neuron then renders gout. Mechanism visibility plus trusted-reference comparison evidence, no pixel interpretation required for textual SVG labels.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# brew install graphviz\n",
    "# pip install graphviz\n",
    "from graphviz import Digraph"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from micrograd.engine import Value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def trace(root):\n",
    "    nodes, edges = set(), set()\n",
    "    def build(v):\n",
    "        if v not in nodes:\n",
    "            nodes.add(v)\n",
    "            for child in v._prev:\n",
    "                edges.add((child, v))\n",
    "                build(child)\n",
    "    build(root)\n",
    "    return nodes, edges\n",
    "\n",
    "def draw_dot(root, format='svg', rankdir='LR'):\n",
    "    \"\"\"\n",
    "    format: png | svg | ...\n",
    "    rankdir: TB (top to bottom graph) | LR (left to right)\n",
    "    \"\"\"\n",
    "    assert rankdir in ['LR', 'TB']\n",
    "    nodes, edges = trace(root)\n",
    "    dot = Digraph(format=format, graph_attr={'rankdir': rankdir}) #, node_attr={'rankdir': 'TB'})\n",
    "    \n",
    "    for n in nodes:\n",
    "        dot.node(name=str(id(n)), label = \"{ data %.4f | grad %.4f }\" % (n.data, n.grad), shape='record')\n",
    "        if n._op:\n",
    "            dot.node(name=str(id(n)) + n._op, label=n._op)\n",
    "            dot.edge(str(id(n)) + n._op, str(id(n)))\n",
    "    \n",
    "    for n1, n2 in edges:\n",
    "        dot.edge(str(id(n1)), str(id(n2)) + n2._op)\n",
    "    \n",
    "    return dot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# a very simple example\n",
    "x = Value(1.0)\n",
    "y = (x * 2 + 1).relu()\n",
    "y.backward()\n",
    "draw_dot(y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# a simple 2D neuron\n",
    "import random\n",
    "from micrograd import nn\n",
    "\n",
    "random.seed(1337)\n",
    "n = nn.Neuron(2)\n",
    "x = [Value(1.0), Value(-2.0)]\n",
    "y = n(x)\n",
    "y.backward()\n",
    "\n",
    "dot = draw_dot(y)\n",
    "dot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "dot.render('gout')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
