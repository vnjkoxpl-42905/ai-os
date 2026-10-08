# Karpathy channel transcripts: 2024-10-08 through 2026-10-08

Checked the official @AndrejKarpathy channel on 2026-10-08 using yt-dlp. All 17 upload dates were checked individually. Exactly two uploads fall inside the inclusive date window. YouTube reported no Shorts or Streams tab.

## Both requested transcripts are local Markdown files

| Video | Upload date | Length | Caption cues | Caption words | Local file |
|---|---|---|---:|---:|---|
| How I use LLMs | 2025-02-27 | 2:11:12 | 3,475 | 25,287 | [Full transcript](C:/Users/Joshu/dev/ai-os/raw/sources/karpathy-brain/raw/youtube/transcripts/EWvNQjAaOHw.md) |
| Deep Dive into LLMs like ChatGPT | 2025-02-05 | 3:31:23 | 5,761 | 41,116 | [Full transcript](C:/Users/Joshu/dev/ai-os/raw/sources/karpathy-brain/raw/youtube/transcripts/7xTGNNLPyMI.md) |

These files already existed in the collected corpus. Each timestamped Markdown transcript row was compared with its caption JSON and matches exactly. The batch script was executed successfully for both videos, then rerun using its cache. The temporary verification output is recorded in the saved run manifest; the original corpus files are the durable transcript copies linked above.

## Coverage and limitations

- Every locally available caption cue is retained, without summarization.
- Neither selected video has a caption gap longer than 15 seconds. No missing section was detected by this timing check. Spoken completeness and caption accuracy were not verified by listening to the audio.
- The final cues extend 1.319 seconds (Deep Dive) and 1.76 seconds (How I use LLMs) beyond the metadata duration. They were preserved rather than clipped.
- Direct caption retrieval currently returns IP blocking / HTTP 429. Existing local captions were reused; no paid service or repeated bypass attempts were needed.
- Correction from the full-channel audit on 2026-10-08: the previous encoding-artifact claim was caused by the audit script decoding UTF-8 with the Windows cp1252 default. The source itself is not corrupted. Explicit UTF-8 decoding reproduces the previous manifest checksum for both videos after normalizing CRLF to LF. Fresh physical-file hashes are recorded in verification.json and SHA256SUMS. Original sources were never changed.
- Guest appearances on other channels are outside this channel-only request.

## The remaining 15 channel uploads are outside the date window

- 2024-06-09: Let's reproduce GPT-2 (124M) (`l8pRSuU81PU`).
- 2024-02-20: Let's build the GPT Tokenizer (`zduSFxRajkE`).
- 2023-11-23: [1hr Talk] Intro to Large Language Models (`zjkBMFhNj_g`).
- 2023-01-17: Let's build GPT: from scratch, in code, spelled out. (`kCc8FmEb1nY`).
- 2022-11-21: Building makemore Part 5: Building a WaveNet (`t3YJ5hKiMQ0`).
- 2022-10-11: Building makemore Part 4: Becoming a Backprop Ninja (`q8SA3rM6ckI`).
- 2022-10-04: Building makemore Part 3: Activations & Gradients, BatchNorm (`P6sfmUTpUmc`).
- 2022-09-12: Building makemore Part 2: MLP (`TCH_1BHY58I`).
- 2022-09-07: The spelled-out intro to language modeling: building makemore (`PaCmpygFfXo`).
- 2022-08-19: Stable diffusion dreams of psychedelic faces (`kVpDARqZdrQ`).
- 2022-08-17: Stable diffusion dreams of steampunk brains (`2oKjtvYslMY`).
- 2022-08-16: Stable diffusion dreams of tattoos (`sM9bozW295Q`).
- 2022-08-16: The spelled-out intro to neural networks and backpropagation: building micrograd (`VMj-3S1tku0`).
- 2022-08-16: Stable diffusion dreams of "blueberry spaghetti" for one night (`vEnetcj_728`).
- 2022-08-16: Stable diffusion dreams of steam punk neural networks (`Jv1ayv-04H4`).

## Reuse the script

The inventory includes durable local caption caches. Code and dependencies live outside the Obsidian vault.

```powershell
& "C:\Users\Joshu\AppData\Local\Programs\Python\Python312\python.exe" "C:\Users\Joshu\dev\ai-os-projects\youtube-transcripts\batch.py" --inventory "C:\Users\Joshu\dev\ai-os\research\karpathy-channel-2024-10-08-to-2026-10-08\channel-inventory.json" --since 2024-10-08 --until 2026-10-08 --out "C:\Users\Joshu\Downloads\karpathy-transcripts-2024-2026"
```


## Verification correction

An earlier audit decoded the source using the Windows default code page. Its generated adaptations and run are superseded by the explicit UTF-8 cache and manifest-20261008T110010747979Z-472abdaeae97.json. Original source files were always intact. The all-17 audit is at ../karpathy-channel-all-17-2026-10-08/report.md.
