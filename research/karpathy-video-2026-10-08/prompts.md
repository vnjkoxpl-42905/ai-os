# Karpathy video: prompts and execution sequence

Source: [I Built Another Andrej Karpathy Using Claude](https://www.youtube.com/watch?v=bvGptCLDhyo), Nate Herk. Inspected 2026-10-08.

The [full timestamped caption transcript](transcript.md) contains 393 segments, ending at 10:43.8. [Machine-readable captions](transcript.json) preserve timing. yt-dlp was used with the installed Deno runtime, retrieved video metadata, but its English subtitle download returned HTTP 429. The existing youtube-transcript-api retrieved the captions successfully. Automatic captions can contain mistakes; they are not verified biographical facts.

Prompts 1 through 5 below were read directly from the numbered on-screen cards. The sixth entry is the actual test command visibly shown at 8:15. The narrator announces six prompts, but a separate numbered 06 card has not been verified. This distinction is deliberate: do not invent a longer sixth prompt. Original wording is separate from the adapted Antigravity collection brief.

No Karpathy corpus collection, wiki compilation, agent installation, skill installation or hook change has been completed by this extraction task. Collection is delegated to Antigravity by Joshua; later stages await its source files.

## 1. The crawl, on-screen card at 3:35

```text
Go get everything Andrej Karpathy has put out publicly. His blog and his repos straight from GitHub. The caption transcripts of his YouTube lectures with youtube-transcript-api and yt-dlp. His X posts with the TwitterAPI.io key in my .env file. Run one agent per source so they work in parallel. Save all of it raw into a folder called karpathy-brain/raw, one subfolder per source, and write a manifest in each one listing every file with its word count and anything that failed. Don't summarize anything yet.
```

For Joshua, substitute the logged-in X browser for the paid TwitterAPI.io acquisition method. Antigravity does collection only. The full adapted brief is [antigravity-collection-prompt.md](antigravity-collection-prompt.md).

## 2. The wiki, on-screen card at 4:45

```text
Here's Karpathy's LLM wiki gist.
gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
Use it as the framework and compile everything in karpathy-brain/raw into a wiki of his brain. I want an index, a log, one page per source, pages for his principles and his methods, and a hot page under 500 words that answers most questions about how he thinks. Every claim about him needs a quote from the raw files. Never edit anything in raw.
```

The [actual gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) was opened and verified. For implementation, map the collection path to our registered source archive, and follow existing AI OS routing/schema. Preserve the existing LSAT and student domain homes.

## 3. The rules, on-screen card at 5:45

```text
Read the wiki and write his rules for how he builds and how he teaches. Only keep a rule if it shows up in at least two different places, like his blog and a lecture. Every rule needs an exact quote from him with the source it came from. Give me the seven strongest ones.
```

Do not start with the video's seven labels as predetermined truth. Derive supported rules from collected evidence. Report if seven do not meet the two-source threshold. Syndicated copies of one statement are not two independent sources.

## 4. Two files, on-screen card at 6:50

```text
Turn these seven rules into a Claude Code subagent called karpathy. It reads the wiki's hot page first, never reads more than five wiki pages, follows the seven rules on every task, cites the wiki page for anything it says about him, and ends every answer with what it ran, what came out, and what it changed. Then make a skill called karpathy-teach that hands any task to that agent and grades the answer against the seven rules before showing it to me.
```

Implement within the repository's project activation/catalog conventions. Claude and Codex configurations differ; a Claude subagent file is not automatically a Codex agent. Neither agent impersonates Karpathy or claims his endorsement.

## 5. Run gate, on-screen card at 7:45

```text
Add a Stop hook to this project. When a turn used the karpathy agent or the karpathy-teach skill, and a code file was written or edited but nothing was run afterward, block the stop and send it back with the message: Karpathy rule, run it before you say it works. Leave every other session alone.
```

Implementation requires current Claude hook documentation and tests for scope, execution evidence, retries and unrelated sessions. Running an unrelated command is not proof edited code works. Do not assume Codex supports the same hook mechanism or install a global gate.

## 6. Actual teaching test command shown at 8:15

```text
/karpathy-teach build me a tiny byte-pair tokenizer from scratch and teach me what it does
```

This is a visible demonstration command, not a verified numbered 06 card. Execute only after the preceding stages exist. Check the success criterion, prediction, real output, deliberately broken case, fix, cited rules and seven-rule grading. Preserve the video's literal invocation as source text; activate through the skill mechanism supported by our runtime.

## Additional demonstrations, separate from the six-entry sequence

- Around 8:55: the video asks whether the client would accept an implementation and what they would want to delete. The visible blue text says “What would he want it to lead?” while the narration/captions say “want to delete.” Do not silently treat that mismatch as exact prompt text.
- Around 9:35 onward: the video demonstrates karpathy-ingest with a new source link and updates to source, principle, index, hot and log pages. This is an ongoing intake demonstration, not evidence that an ingest skill has already been installed here.

## Run these one at a time

1. Joshua gives Antigravity the collection brief. Its deliverable is physical source files, hashes, manifests, coverage and failure records.
2. We verify those delivered files and then execute the wiki compilation prompt.
3. Derive the seven supported rules.
4. Build and validate the project agent and teaching skill.
5. Build and test the scoped execution gate.
6. Run the tokenizer teaching test and inspect its actual evidence.

The video transcript and prompts are now saved. The remaining stages are pending, not claimed complete.
