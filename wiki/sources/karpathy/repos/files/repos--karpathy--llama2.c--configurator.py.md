---
type: source
subject: "GitHub source repos/karpathy/llama2.c/configurator.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llama2.c/configurator.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/llama2.c/configurator.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llama2.c/configurator.py), SHA-256 `5cc23aca26b4ab3c0d9e5f82740f4781f9444f42718c15abcee70d93c5aabe8f`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
""" Poor Man's Configurator. Probably a terrible idea. Example usage: $ python train.py config/override_file.py --batch_size=32
```

Five llama2.c CI/config/document sources fully read. CI builds Ubuntu and macOS, MSVC amd64/x86/arm64 matrix and MinGW, runs pytest except crosscompiled ARM64 and tolerates only brew update failure; configuration expresses coverage not proof current runs pass. MSVC batch uses optimized fast FP and OpenMP. Configurator explicitly dislikes complexity, executes trusted config files into globals then literal-evaluates known exact-type CLI overrides, rejects unknown keys; arbitrary config execution is not safe for untrusted input. Stories260K documents custom512token vocab, grouped shared KV heads, tiny baseline loss1.2968, uncertain ten-minute time, poor greedy sample and exact Python/C comparison with manual257 token bound due termination mismatch. Tokenizer note inspects actual Meta protobuf settings, recommends coverage1, digit split, whitespace pieces, byte fallback and identity normalization, explicitly approximate reproduction and newline/max-sentence assumptions.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""
Poor Man's Configurator. Probably a terrible idea. Example usage:
$ python train.py config/override_file.py --batch_size=32
this will first run config/override_file.py, then override batch_size to 32

The code in this file will be run as follows from e.g. train.py:
>>> exec(open('configurator.py').read())

So it's not a Python module, it's just shuttling this code away from train.py
The code in this script then overrides the globals()

I know people are not going to love this, I just really dislike configuration
complexity and having to prepend config. to every single variable. If someone
comes up with a better simple Python solution I am all ears.
"""

import sys
from ast import literal_eval

for arg in sys.argv[1:]:
    if '=' not in arg:
        # assume it's the name of a config file
        assert not arg.startswith('--')
        config_file = arg
        print(f"Overriding config with {config_file}:")
        with open(config_file) as f:
            print(f.read())
        exec(open(config_file).read())
    else:
        # assume it's a --key=value argument
        assert arg.startswith('--')
        key, val = arg.split('=')
        key = key[2:]
        if key in globals():
            try:
                # attempt to eval it it (e.g. if bool, number, or etc)
                attempt = literal_eval(val)
            except (SyntaxError, ValueError):
                # if that goes wrong, just use the string
                attempt = val
            # ensure the types match ok
            assert type(attempt) == type(globals()[key])
            # cross fingers
            print(f"Overriding: {key} = {attempt}")
            globals()[key] = attempt
        else:
            raise ValueError(f"Unknown config key: {key}")

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
