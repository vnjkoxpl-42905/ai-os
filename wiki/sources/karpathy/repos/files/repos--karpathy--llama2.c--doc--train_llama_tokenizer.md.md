---
type: source
subject: "GitHub source repos/karpathy/llama2.c/doc/train_llama_tokenizer.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llama2.c/doc/train_llama_tokenizer.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/llama2.c/doc/train_llama_tokenizer.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llama2.c/doc/train_llama_tokenizer.md), SHA-256 `6b8525e1aadc772ee1a49e23fa73da0c91b0a61c5e03c0f4fc7ecd549782549a`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
# training llama tokenizer How does Meta train their sentencepiece tokenizer? You can print the
```

Five llama2.c CI/config/document sources fully read. CI builds Ubuntu and macOS, MSVC amd64/x86/arm64 matrix and MinGW, runs pytest except crosscompiled ARM64 and tolerates only brew update failure; configuration expresses coverage not proof current runs pass. MSVC batch uses optimized fast FP and OpenMP. Configurator explicitly dislikes complexity, executes trusted config files into globals then literal-evaluates known exact-type CLI overrides, rejects unknown keys; arbitrary config execution is not safe for untrusted input. Stories260K documents custom512token vocab, grouped shared KV heads, tiny baseline loss1.2968, uncertain ten-minute time, poor greedy sample and exact Python/C comparison with manual257 token bound due termination mismatch. Tokenizer note inspects actual Meta protobuf settings, recommends coverage1, digit split, whitespace pieces, byte fallback and identity normalization, explicitly approximate reproduction and newline/max-sentence assumptions.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

````text
# training llama tokenizer

How does Meta train their sentencepiece tokenizer? You can print the config as follows:

```python
import sentencepiece.sentencepiece_model_pb2
mp = sentencepiece.sentencepiece_model_pb2.ModelProto()
mp.ParseFromString(open("tokenizer.model", "rb").read())
print(mp.trainer_spec)
print(mp.normalizer_spec)
```

this gives:

```
trainer_spec {
  input: "/large_experiments/theorem/datasets/MERGED/all.test1.merged"
  model_prefix: "spm_model_32k_200M_charcov099995_allowWSO__v2"
  model_type: BPE
  vocab_size: 32000
  self_test_sample_size: 0
  input_format: "text"
  character_coverage: 0.9999499917030334
  input_sentence_size: 200000000
  seed_sentencepiece_size: 1000000
  shrinking_factor: 0.75
  num_threads: 80
  num_sub_iterations: 2
  max_sentence_length: 4192
  shuffle_input_sentence: true
  max_sentencepiece_length: 16
  split_by_unicode_script: true
  split_by_whitespace: true
  split_by_number: true
  treat_whitespace_as_suffix: false
  split_digits: true
  allow_whitespace_only_pieces: true
  vocabulary_output_piece_score: true
  hard_vocab_limit: true
  use_all_vocab: false
  byte_fallback: true
  required_chars: ""
  unk_id: 0
  bos_id: 1
  eos_id: 2
  pad_id: -1
  unk_surface: " \342\201\207 "
  unk_piece: "<unk>"
  bos_piece: "<s>"
  eos_piece: "</s>"
  pad_piece: "<pad>"
  train_extremely_large_corpus: false
  enable_differential_privacy: false
  differential_privacy_noise_level: 0.0
  differential_privacy_clipping_threshold: 0
}
normalizer_spec {
  name: "identity"
  precompiled_charsmap: ""
  add_dummy_prefix: true
  remove_extra_whitespaces: false
  normalization_rule_tsv: ""
}
```

We can use the sentencepiece spm_train to train the same models, but optionally smaller. Here are their [options docs](https://github.com/google/sentencepiece/blob/master/doc/options.md) we can refer to. It's not much but it helps.

We'll depart on one setting, I recommend changing `character_coverage` -> 1.0. We also want to make sure to note the following important settings that come up in the paper and are not necessarily the default sentencepiece settings:

```
--split-digits = true
--allow_whitespace_only_pieces = true
--byte_fallback = true
--normalization_rule_name = identity
```

With this in mind we can train a sentencepiece vocab in what I believe is probably the same to how Meta trained theirs as:

```
spm_train --input="$input" \
          --model_prefix="$model_prefix" \
          --model_type=bpe \
          --vocab_size="$vocab_size" \
          --self_test_sample_size=0 \
          --input_format="text" \
          --character_coverage=1.0 \
          --num_threads="$(nproc)" \
          --split_digits=true \
          --allow_whitespace_only_pieces=true \
          --byte_fallback=true \
          --unk_surface=" \342\201\207 " \
          --normalization_rule_name=identity \
```

Where $input is the input file, $model_prefix is the output path prefix, vocab_size is the desired vocab, and we're by default taking over the CPU resources of the machine.

Lastly note that sentencepiece is weird and expects "sentences" delimited by newlines as the input. You can't just put in a massive block of text. And they have a hyperparameter that constols the maximum size of a "sentence". Fwiw I really dislike this design choice around a weird concept of a "sentence". It should just be block of text with no assumptions. But here we are.

Look into the file `tinystories.py` where we train the vocab in the same way, but using Python bindings instead.

````

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
