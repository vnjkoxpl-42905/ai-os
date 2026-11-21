---
type: source
subject: "GitHub source repos/karpathy/nanochat/tasks/humaneval.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/tasks/humaneval.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/nanochat/tasks/humaneval.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/tasks/humaneval.py), SHA-256 `2ee62f4da86d6c2e9aea4b41cee1969a7da97036fd0e5d0152af600825dfd613`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

````text
""" Evaluate the Chat model on HumanEval dataset. Btw this dataset is a misnomer and
````

Tokenizer training bounds total text and per-document length, sanity-checks Unicode roundtrip, stores raw token byte lengths rather than individually decoded UTF8 strings and zeros special-token byte counts for evaluation. Task utilities cache parquet with completion manifest and file lock, expose seeded row permutations, explicitly sliced tasks, shuffled oversampling mixtures and curriculum sequences. Multiple-choice rendering keeps answer-letter token identity by eliminating delimiter whitespace and placing labels after choices. ARC validates answer membership. GSM8K separates calculator expressions/results from prose, extracts marked numeric answers and reuses reward; malformed reference and prediction both None can compare equal. HumanEval extracts first fenced code block plus prompt imports, runs actual tests and returns execution success, subject to explicitly limited subprocess security. Dataset example prose is foreign benchmark content, not persona claims.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

````text
"""
Evaluate the Chat model on HumanEval dataset.
Btw this dataset is a misnomer and has nothing to do with humans.
It is a coding benchmark.
"""

import re
from nanochat.execution import execute_code
from tasks.common import Task, load_hub_dataset

def extract_imports(prompt):
    """Extract import statements from the beginning of a code block."""
    imports = []
    for line in prompt.split('\n'):
        stripped = line.strip()
        if stripped.startswith('import ') or stripped.startswith('from '):
            imports.append(stripped)
        elif stripped and not stripped.startswith('#'):
            # Stop at first non-import, non-comment line
            break
    return '\n'.join(imports)

def extract_program(completion):
    """
    Extract Python code from LLM completion.

    Handles various output formats:
    - Code wrapped in ```python ... ``` or ``` ... ``` blocks
    - Plain code without markdown blocks
    - Extra text before/after code blocks

    Returns the first code block if found, otherwise returns the whole completion.
    """
    # Try to find markdown code blocks (```python or just ```)
    # Match ```python\n...\n``` or ```\n...\n```
    pattern = r'```(?:python)?\s*\n(.*?)\n```'
    matches = re.findall(pattern, completion, re.DOTALL)

    if matches:
        # Return the first code block found
        return matches[0].strip()

    # No code blocks found, return the whole completion
    return completion.strip()

class HumanEval(Task):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # note: this dataset has no named subsets, its parquet config on the hub is "openai_humaneval"
        self.ds = load_hub_dataset("openai/openai_humaneval", subset="openai_humaneval", split="test").shuffle(seed=42)

    @property
    def eval_type(self):
        return 'generative'

    def num_examples(self):
        return len(self.ds)

    def get_example(self, index):
        """ Get a single problem from the dataset. """
        row = self.ds[index]
        prompt = row['prompt'] # prompts in HumanEval are the beginning of the program
        solution = row['canonical_solution'] # the correct continuation of the program
        entry_point = row['entry_point'] # the function to check
        test = row['test'] # the test cases
        complete_solution = f"{prompt}\n{solution}"
        messages = [
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": complete_solution},
        ]
        conversation = {
            "messages": messages,
            "entry_point": entry_point, # needed during evaluation
            "test": test, # needed during evaluation
        }
        return conversation

    def evaluate(self, conversation, completion):
        """ Given (conversation, completion), return boolean success of the completion. """
        # the prompt will contain the imports and the function signature
        imports = extract_imports(conversation['messages'][0]['content'])
        # the completion will usually contain the whole function
        # but not always with the needed imports, so we manually append them
        completion_code = extract_program(completion)
        program = (
            imports
            + "\n\n"
            + completion_code
            + "\n\n"
            + conversation['test']
            + "\n"
            + f"check({conversation['entry_point']})"
        )
        result = execute_code(program)
        success = result.success
        return success

````

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
