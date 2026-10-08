# Audit of all 17 official Karpathy uploads

Audited 2026-10-08. All dates; sources remain unchanged.

**15 timestamped transcripts are saved. Two uploads have no transcript file.**

Every saved transcript was compared cue-for-cue against its local caption JSON. Saved cues are not independently verified as every spoken word. Automatic captions may contain errors or repeated text.

| Video | Upload date | Status | Cues | Caption words | Gaps >15s | Exact MD/cue match |
|---|---|---|---:|---:|---:|---|
| [How I use LLMs](https://www.youtube.com/watch?v=EWvNQjAaOHw) | 20250227 | saved_timestamped | 3475 | 25287 | 0 | True |
| [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) | 20250205 | saved_timestamped | 5761 | 41116 | 0 | True |
| [Let's reproduce GPT-2 (124M)](https://www.youtube.com/watch?v=l8pRSuU81PU) | 20240609 | saved_timestamped | 6049 | 43388 | 0 | True |
| [Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) | 20240220 | saved_timestamped | 3422 | 24679 | 0 | True |
| [[1hr Talk] Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) | 20231123 | saved_timestamped | 1704 | 12151 | 0 | True |
| [Let's build GPT: from scratch, in code, spelled out.](https://www.youtube.com/watch?v=kCc8FmEb1nY) | 20230117 | saved_timestamped | 2955 | 21030 | 0 | True |
| [Building makemore Part 5: Building a WaveNet](https://www.youtube.com/watch?v=t3YJ5hKiMQ0) | 20221121 | saved_timestamped | 1559 | 10385 | 0 | True |
| [Building makemore Part 4: Becoming a Backprop Ninja](https://www.youtube.com/watch?v=q8SA3rM6ckI) | 20221011 | saved_timestamped | 3097 | 20776 | 0 | True |
| [Building makemore Part 3: Activations & Gradients, BatchNorm](https://www.youtube.com/watch?v=P6sfmUTpUmc) | 20221004 | saved_timestamped | 3051 | 21386 | 0 | True |
| [Building makemore Part 2: MLP](https://www.youtube.com/watch?v=TCH_1BHY58I) | 20220912 | saved_timestamped | 2147 | 12731 | 1 | True |
| [The spelled-out intro to language modeling: building makemore](https://www.youtube.com/watch?v=PaCmpygFfXo) | 20220907 | saved_timestamped | 3332 | 19445 | 0 | True |
| [Stable diffusion dreams of psychedelic faces](https://www.youtube.com/watch?v=kVpDARqZdrQ) | 20220819 | saved_timestamped | 16 | 16 | 0 | True |
| [Stable diffusion dreams of steampunk brains](https://www.youtube.com/watch?v=2oKjtvYslMY) | 20220817 | saved_timestamped | 147 | 147 | 0 | True |
| [Stable diffusion dreams of tattoos](https://www.youtube.com/watch?v=sM9bozW295Q) | 20220816 | saved_timestamped | 11 | 11 | 0 | True |
| [The spelled-out intro to neural networks and backpropagation: building micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0) | 20220816 | saved_timestamped | 4183 | 24352 | 0 | True |
| [Stable diffusion dreams of "blueberry spaghetti" for one night](https://www.youtube.com/watch?v=vEnetcj_728) | 20220816 | missing_transcript |  |  | unknown |  |
| [Stable diffusion dreams of steam punk neural networks](https://www.youtube.com/watch?v=Jv1ayv-04H4) | 20220816 | missing_transcript |  |  | unknown |  |

## Two uploads have no available caption track

The parent independently checked both with installed yt-dlp `--list-subs` on 2026-10-08: no automatic captions and no subtitles. The earlier collector describes these as music/instrumental-only animations. This audit did not listen to their audio and does not claim that absence of speech is independently verified.
- `vEnetcj_728`: Stable diffusion dreams of "blueberry spaghetti" for one night.
- `Jv1ayv-04H4`: Stable diffusion dreams of steam punk neural networks.

## Existing manifest hashes need care

The old manifest hashes LF-normalized text rather than physical Windows CRLF bytes. This audit records physical and normalized SHA-256 separately. No sources were repaired or overwritten.

## Exact file evidence

[audit.json](audit.json) records all 17 entries, full source paths, physical hashes, cue counts, temporal bounds, gaps, metadata identity checks and collection provenance. The source collection is `raw/sources/karpathy-brain/raw/youtube/`.
