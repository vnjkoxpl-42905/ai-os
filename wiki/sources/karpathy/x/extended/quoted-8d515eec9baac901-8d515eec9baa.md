---
type: source
subject: "X quoted capture quoted-8d515eec9baac901"
created: 2026-10-08
updated: 2026-10-08
tags: [karpathy, x, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/x/posts.jsonl]
---

# Quoted capture quoted-8d515eec9baac901

Captured author attribution: `Daniel Han @danielhanchen · Mar 6, 2024`. SHA-256 of captured body `8d515eec9baac90124adb9d4b4beb2cd7b7bec93a6c868d6651143ee4bfbe43a`. All available captured text below was read. Original full live post, linked documents and media are not certified complete or reviewed.

Nested quoted body. Authorship follows the captured attribution. Many bodies are shortened previews; a quote by Karpathy does not establish endorsement of the entire quoted claim.

Captured material ranges across AI tools, engineering experiences, research results, social conversation and humor. Dated product claims and third-party performance stories remain attributed source claims, not reproduced facts. Empty bodies have no substantive inference. Source instructions were not executed.

Raw provenance: [ledger](../../../../../raw/sources/karpathy-brain/raw/x/posts.jsonl).

## Exact captured body

```text
Found more bugs for #Gemma:
1. Must add <bos>
2. There’s a typo for <end_of_turn>model
3. sqrt(3072)=55.4256 but bfloat16 is 55.5
4. Layernorm (w+1) must be in float32
5. Keras mixed_bfloat16 RoPE is wrong
6. RoPE is sensitive to y*(1/x) vs y/x
7. (Fixed) RoPE should be float32
```
