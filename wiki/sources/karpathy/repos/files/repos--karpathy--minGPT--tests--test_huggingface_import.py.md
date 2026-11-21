---
type: source
subject: "GitHub source repos/karpathy/minGPT/tests/test_huggingface_import.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/minGPT/tests/test_huggingface_import.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/minGPT/tests/test_huggingface_import.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/minGPT/tests/test_huggingface_import.py), SHA-256 `4839ac2314fba2b7b842927a716259a306eaf637cb6647c6a1cb809e63ec6621`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
""" Ensure that we can load huggingface/transformer GPTs into minGPT """ import unittest import torch
```

Adder reverses output digits to align addition with carry order, masks input loss and uses a seeded finite train/test split; greedy predictions are compared with exact addition and up to five mistakes are printed. Selecting checkpoints using train plus test correctness reuses test information. CharGPT trains character windows and samples periodically; its comment about evaluating train and test is inaccurate because no held-out evaluation is implemented. Import test compares minGPT and Hugging Face logits, exact generated IDs and decoded strings on a Unicode prompt, but was read rather than run. Nanochat arxiv skill prefers recursively reading cached TeX source and relating papers to concrete repository code, keeping reusable downloads separate from project-specific summaries; these source instructions were not activated.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""
Ensure that we can load huggingface/transformer GPTs into minGPT
"""

import unittest
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from mingpt.model import GPT
from mingpt.bpe import BPETokenizer
# -----------------------------------------------------------------------------

class TestHuggingFaceImport(unittest.TestCase):

    def test_gpt2(self):
        model_type = 'gpt2'
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        prompt = "Hello!!!!!!!!!? 🤗, my dog is a little"

        # create a minGPT and a huggingface/transformers model
        model = GPT.from_pretrained(model_type)
        model_hf = GPT2LMHeadModel.from_pretrained(model_type) # init a HF model too

        # ship both to device
        model.to(device)
        model_hf.to(device)

        # set both to eval mode
        model.eval()
        model_hf.eval()

        # tokenize input prompt
        # ... with mingpt
        tokenizer = BPETokenizer()
        x1 = tokenizer(prompt).to(device)
        # ... with huggingface/transformers
        tokenizer_hf = GPT2Tokenizer.from_pretrained(model_type)
        model_hf.config.pad_token_id = model_hf.config.eos_token_id # suppress a warning
        encoded_input = tokenizer_hf(prompt, return_tensors='pt').to(device)
        x2 = encoded_input['input_ids']

        # ensure the logits match exactly
        logits1, loss = model(x1)
        logits2 = model_hf(x2).logits
        self.assertTrue(torch.allclose(logits1, logits2))

        # now draw the argmax samples from each
        y1 = model.generate(x1, max_new_tokens=20, do_sample=False)[0]
        y2 = model_hf.generate(x2, max_new_tokens=20, do_sample=False)[0]
        self.assertTrue(torch.equal(y1, y2)) # compare the raw sampled indices

        # convert indices to strings
        out1 = tokenizer.decode(y1.cpu().squeeze())
        out2 = tokenizer_hf.decode(y2.cpu().squeeze())
        self.assertTrue(out1 == out2) # compare the exact output strings too

if __name__ == '__main__':
    unittest.main()

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
