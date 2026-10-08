# Run the video method in Codex

Joshua selected Codex on 2026-10-08. This supersedes the requirement to resume the Claude replay. Original video prompt files remain unchanged. Existing X files are the authorized Prompt 1 acquisition exception; no TwitterAPI.io recollection is needed. The saved collection is already compiled.

Only Prompt 4 changes its runtime name from Claude Code to Codex. Prompt 5 uses the Codex project-hook interface while retaining the exact blocking message. These are authorized runtime adaptations, not claims that the video used Codex.


## Prompt 1

```text
Go get everything Andrej Karpathy has put out publicly. His blog and his repos straight from GitHub. The caption transcripts of his YouTube lectures with youtube-transcript-api and yt-dlp. His X posts with the TwitterAPI.io key in my .env file. Run one agent per source so they work in parallel. Save all of it raw into a folder called karpathy-brain/raw, one subfolder per source, and write a manifest in each one listing every file with its word count and anything that failed. Don't summarize anything yet.
```


## Prompt 2

```text
Here's Karpathy's LLM wiki gist.
gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
Use it as the framework and compile everything in karpathy-brain/raw into a wiki of his brain. I want an index, a log, one page per source, pages for his principles and his methods, and a hot page under 500 words that answers most questions about how he thinks. Every claim about him needs a quote from the raw files. Never edit anything in raw.
```


## Prompt 3

```text
Read the wiki and write his rules for how he builds and how he teaches. Only keep a rule if it shows up in at least two different places, like his blog and a lecture. Every rule needs an exact quote from him with the source it came from. Give me the seven strongest ones.
```


## Prompt 4

```text
Turn these seven rules into a Codex subagent called karpathy. It reads the wiki's hot page first, never reads more than five wiki pages, follows the seven rules on every task, cites the wiki page for anything it says about him, and ends every answer with what it ran, what came out, and what it changed. Then make a skill called karpathy-teach that hands any task to that agent and grades the answer against the seven rules before showing it to me.
```


## Prompt 5

```text
Add a Stop hook to this project. When a turn used the karpathy agent or the karpathy-teach skill, and a code file was written or edited but nothing was run afterward, block the stop and send it back with the message: Karpathy rule, run it before you say it works. Leave every other session alone.
```


## Prompt 6

```text
/karpathy-teach build me a tiny byte-pair tokenizer from scratch and teach me what it does
```
