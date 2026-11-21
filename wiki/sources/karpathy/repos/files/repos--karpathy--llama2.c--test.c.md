---
type: source
subject: "GitHub source repos/karpathy/llama2.c/test.c"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llama2.c/test.c]
semantic-status: complete-named-text-read
---

# repos/karpathy/llama2.c/test.c

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llama2.c/test.c), SHA-256 `ea6d3b4368147d5aea36024e2294f4b69709fa44bff2c7b70aed86682de4f76a`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
#define TESTING #include "run.c" void assert_eq(int a, int b) { if (a != b) {
```

Four llama2.c sampling/tests/TinyStories sources fully read. Sample resolves checkpoint-specific tokenizer, strips compile prefix, seeds CPU/CUDA, optional autocast/compile, file prompt, runs model.generate without EOS exit. C tokenizer tests empty/BOS, trailing spaces, newline formatting and French UTF8 against exact debugger-derived Meta tokens. Python tests compare C and PyTorch greedy200step outputs to one fixed260K reference; external downloads lack hashes, subprocess return code unchecked. TinyStories stages download/cache, inspect first example, train BPE on ten shards, parallel pretok BOS-separated uint16 arrays, report average sequence length, memmap chunks+one next-token target, deterministic rank/worker seeds and shard0 heldout. Loader workers reshuffle whole shared datasets rather than exclusive partition. Download lacks raise_for_status/atomic integrity; process executor.map iterator unconsumed can hide worker exceptions; uint16 implicitly assumes vocab fits. Keeps raw-versus-derived distinctions and optional temp deletion confirmation. Tests read, not executed.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
#define TESTING
#include "run.c"

void assert_eq(int a, int b) {
    if (a != b) {
        printf("Assertion failed: %d != %d\n", a, b);
        exit(EXIT_FAILURE);
    }
}

void test_prompt_encoding(Tokenizer* tokenizer, char* prompt, int* expected_tokens, int num_expected_tokens) {
    // encode
    int* prompt_tokens = (int*)malloc((strlen(prompt)+3) * sizeof(int));
    int num_prompt_tokens = 0; // the total number of prompt tokens
    encode(tokenizer, prompt, 1, 0, prompt_tokens, &num_prompt_tokens);

    #if VERBOSITY == 1
    // print maybe
    printf("expected tokens:\n");
    for (int i = 0; i < num_expected_tokens; i++) printf("%d ", expected_tokens[i]);
    printf("\n");
    printf("actual tokens:\n");
    for (int i = 0; i < num_prompt_tokens; i++) printf("%d ", prompt_tokens[i]);
    printf("\n");
    #endif

    // verify
    assert_eq(num_prompt_tokens, num_expected_tokens);
    for (int i = 0; i < num_prompt_tokens; i++) {
        assert_eq(prompt_tokens[i], expected_tokens[i]);
    }

    #if VERBOSITY == 1
    printf("OK\n");
    printf("---\n");
    #endif
    free(prompt_tokens);
}

void test_prompt_encodings() {
    // let's verify that the Tokenizer works as expected

    char *tokenizer_path = "tokenizer.bin";
    int vocab_size = 32000;
    Tokenizer tokenizer;
    build_tokenizer(&tokenizer, tokenizer_path, vocab_size);

    // test 0 (test the empty string) (I added this as a simple case)
    char *prompt0 = "";
    int expected_tokens0[] = {1};
    test_prompt_encoding(&tokenizer, prompt0, expected_tokens0, sizeof(expected_tokens0) / sizeof(int));

    // the tests below are taken from the Meta Llama 2 repo example code
    // https://github.com/facebookresearch/llama/blob/main/example_text_completion.py
    // and the expected tokens come from me breaking in the debugger in Python

    // test 1
    char *prompt = "I believe the meaning of life is";
    int expected_tokens[] = {1, 306, 4658, 278, 6593, 310, 2834, 338};
    test_prompt_encoding(&tokenizer, prompt, expected_tokens, sizeof(expected_tokens) / sizeof(int));

    // test 2
    char* prompt2 = "Simply put, the theory of relativity states that ";
    int expected_tokens2[] = {1, 3439, 17632, 1925, 29892, 278, 6368, 310, 14215, 537, 5922, 393, 29871};
    test_prompt_encoding(&tokenizer, prompt2, expected_tokens2, sizeof(expected_tokens2) / sizeof(int));

    // test 3
    char* prompt3 = "A brief message congratulating the team on the launch:\n\n        Hi everyone,\n\n        I just ";
    int expected_tokens3[] = {1, 319, 11473, 2643, 378, 629, 271, 18099, 278, 3815, 373, 278, 6826, 29901, 13, 13, 4706, 6324, 14332, 29892, 13, 13, 4706, 306, 925, 29871};
    test_prompt_encoding(&tokenizer, prompt3, expected_tokens3, sizeof(expected_tokens3) / sizeof(int));

    // test 4
    char* prompt4 = "Translate English to French:\n\n        sea otter => loutre de mer\n        peppermint => menthe poivrée\n        plush girafe => girafe peluche\n        cheese =>";
    int expected_tokens4[] = {1, 4103, 9632, 4223, 304, 5176, 29901, 13, 13, 4706, 7205, 4932, 357, 1149, 301, 449, 276, 316, 2778, 13, 4706, 1236, 407, 837, 524, 1149, 6042, 354, 772, 440, 29878, 1318, 13, 4706, 715, 1878, 330, 3055, 1725, 1149, 330, 3055, 1725, 4639, 28754, 13, 4706, 923, 968, 1149};
    test_prompt_encoding(&tokenizer, prompt4, expected_tokens4, sizeof(expected_tokens4) / sizeof(int));

    // memory and file handles cleanup
    free_tokenizer(&tokenizer);
}

int main(int argc, char *argv[]) {
    test_prompt_encodings();
    printf("ALL OK\n");
}

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
