---
type: source
subject: "GitHub source repos/karpathy/nanochat/tasks/mmlu.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/tasks/mmlu.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/nanochat/tasks/mmlu.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/tasks/mmlu.py), SHA-256 `0b00ada4ad4bc7675f6e36a1e8770b19ae17c12daedbf7c88965228902421a66`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
""" The MMLU dataset. https://huggingface.co/datasets/cais/mmlu """ from tasks.common import Task, load_hub_dataset, render_mc class MMLU(Task): letters
```

MMLU adapter retains subject provenance, enforces four choices and valid restricted-letter responses. SmolTalk validates optional system prefix, user-assistant alternation and string messages before rendering. Attention fallback tests compare actual outputs and gradients with hardware-qualified tolerances across full/sliding context, GQA, cached prefill and decode; a regression test specifically catches single-token decode ignoring window limits. SDPA-only tests verify shape, finite values, gradients and cache advancement. All tests are source-inspected not run. Auto override test assumes availability equals selection, which is stale when available FA3 is rejected by compute dtype. MPS support is stated but SDPA test class selects only CUDA or CPU.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""
The MMLU dataset.
https://huggingface.co/datasets/cais/mmlu
"""

from tasks.common import Task, load_hub_dataset, render_mc

class MMLU(Task):

    letters = ('A', 'B', 'C', 'D')
    groups = ('abstract_algebra', 'anatomy', 'astronomy', 'business_ethics', 'clinical_knowledge', 'college_biology', 'college_chemistry', 'college_computer_science', 'college_mathematics', 'college_medicine', 'college_physics', 'computer_security', 'conceptual_physics', 'econometrics', 'electrical_engineering', 'elementary_mathematics', 'formal_logic', 'global_facts', 'high_school_biology', 'high_school_chemistry', 'high_school_computer_science', 'high_school_european_history', 'high_school_geography', 'high_school_government_and_politics', 'high_school_macroeconomics', 'high_school_mathematics', 'high_school_microeconomics', 'high_school_physics', 'high_school_psychology', 'high_school_statistics', 'high_school_us_history', 'high_school_world_history', 'human_aging', 'human_sexuality', 'international_law', 'jurisprudence', 'logical_fallacies', 'machine_learning', 'management', 'marketing', 'medical_genetics', 'miscellaneous', 'moral_disputes', 'moral_scenarios', 'nutrition', 'philosophy', 'prehistory', 'professional_accounting', 'professional_law', 'professional_medicine', 'professional_psychology', 'public_relations', 'security_studies', 'sociology', 'us_foreign_policy', 'virology', 'world_religions')

    def __init__(self, subset, split, **kwargs):
        super().__init__(**kwargs)
        assert subset in ["all"], f"subset {subset} must be all"
        assert split in ["auxiliary_train", "validation", "dev", "test"], f"split {split} must be auxiliary_train|validation|dev|test"
        self.subset = subset
        self.split = split
        self.ds = load_hub_dataset("cais/mmlu", subset, split=split).shuffle(seed=42)

    @property
    def eval_type(self):
        return 'categorical'

    def num_examples(self):
        return len(self.ds)

    def get_example(self, index):
        row = self.ds[index]
        question = row["question"] # the question text
        choices = row["choices"] # the text of each choice
        answer = row["answer"] # index of the answer, e.g. 0,1,2,3 (for A,B,C,D)
        subject = row["subject"] # e.g. "college_biology", "college_chemistry", etc.
        assert len(choices) == 4, "MMLU should have 4 choices"
        # create and return the Conversation object
        user_message = render_mc(question, self.letters, choices)
        assistant_message = self.letters[answer]
        messages = [
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": assistant_message}
        ]
        conversation = {
            "messages": messages,
            "subject": subject, # might be useful later for grouping metrics by subject
            "letters": self.letters, # useful during evaluation, so we can narrow and clamp the assistant prediction to one of the letters
        }
        return conversation

    def evaluate(self, conversation, assistant_response):
        # the assert here is not strictly speaking needed, but currently the way we eval, we expect this to be true
        # I'm going to leave the assert here to prevent footguns, but possibly in the future can remove it.
        assert assistant_response in self.letters, f"MMLU answer {assistant_response} is expected to be one of {self.letters}"
        assistant_message = conversation['messages'][-1]['content'] # e.g. "A"
        return assistant_response == assistant_message

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
