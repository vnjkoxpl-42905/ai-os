---
type: source
subject: "GitHub source repos/karpathy/nanochat/tasks/arc.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/tasks/arc.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/nanochat/tasks/arc.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/tasks/arc.py), SHA-256 `f00642888b36ddff8524603f63d417cd39fc36c3c206922cd676df51c10f1b19`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
""" The ARC dataset from Allen AI. https://huggingface.co/datasets/allenai/ai2_arc """ from tasks.common import Task, load_hub_dataset, render_mc
```

Tokenizer training bounds total text and per-document length, sanity-checks Unicode roundtrip, stores raw token byte lengths rather than individually decoded UTF8 strings and zeros special-token byte counts for evaluation. Task utilities cache parquet with completion manifest and file lock, expose seeded row permutations, explicitly sliced tasks, shuffled oversampling mixtures and curriculum sequences. Multiple-choice rendering keeps answer-letter token identity by eliminating delimiter whitespace and placing labels after choices. ARC validates answer membership. GSM8K separates calculator expressions/results from prose, extracts marked numeric answers and reuses reward; malformed reference and prediction both None can compare equal. HumanEval extracts first fenced code block plus prompt imports, runs actual tests and returns execution success, subject to explicitly limited subprocess security. Dataset example prose is foreign benchmark content, not persona claims.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""
The ARC dataset from Allen AI.
https://huggingface.co/datasets/allenai/ai2_arc
"""

from tasks.common import Task, load_hub_dataset, render_mc

class ARC(Task):

    def __init__(self, subset, split, **kwargs):
        super().__init__(**kwargs)
        assert subset in ["ARC-Easy", "ARC-Challenge"], "ARC subset must be ARC-Easy or ARC-Challenge"
        assert split in ["train", "validation", "test"], "ARC split must be train|validation|test"
        self.ds = load_hub_dataset("allenai/ai2_arc", subset, split=split).shuffle(seed=42)

    @property
    def eval_type(self):
        return 'categorical'

    def num_examples(self):
        return len(self.ds)

    def get_example(self, index):
        row = self.ds[index]
        question = row["question"] # the question text
        choices = row["choices"]["text"] # the text of each choice
        answer_string = row["answerKey"] # e.g. "A", "B", "C", "D"
        letters = row["choices"]["label"] # e.g. ["A", "B", "C", "D"]
        assert answer_string in letters, f"ARC answer {answer_string} must be one of {letters}" # sanity check
        # create and return the Conversation object
        user_message = render_mc(question, letters, choices)
        messages = [
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": answer_string}
        ]
        conversation = {
            "messages": messages,
            "letters": letters, # useful during evaluation, so we can narrow and clamp the assistant prediction to one of the letters
        }
        return conversation

    def evaluate(self, conversation, assistant_response):
        # the assert here is not strictly speaking needed, but currently the way we eval, we expect this to be true
        # I'm going to leave the assert here to prevent footguns, but possibly in the future can remove it.
        assert assistant_response in conversation['letters'], f"ARC answer {assistant_response} is expected to be one of {conversation['letters']}"
        assistant_message = conversation['messages'][-1]['content'] # e.g. "A"
        return assistant_response == assistant_message

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
