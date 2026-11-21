# Prompt 1 for Antigravity: collect Karpathy's sources only

This adapts the video's first prompt to Joshua's logged-in X browser and existing free tools. It does not run the wiki, rules, agent or hook stages.

```text
I am reproducing the source-collection stage of Nate Herk's video:
https://www.youtube.com/watch?v=bvGptCLDhyo

Your job is ONLY to gather Andrej Karpathy's public source material into actual
local files. Claude/Codex will compile and use it afterward. Do not summarize,
derive rules, build a wiki, install agents/skills/hooks, or alter my AI OS setup.

I have X logged in in Chrome. Use that existing browser session to read public
Karpathy posts. Do not use paid TwitterAPI.io, paid APIs, paid scraping proxies,
or paid transcription. Do not export cookies, tokens, passwords or browser sessions.

Write everything under this exact collection root:
C:\Users\Joshu\dev\ai-os\raw\sources\karpathy-brain\raw

Subfolders:
blog\
github\
youtube\
x\

First inspect any existing collection at that root. Resume without overwriting
or deleting existing source files. Keep other vault folders and source collections
untouched. Store any temporary software environments outside the Obsidian vault.

If available, use one independent worker per source type, in parallel. Assign each
worker its own subfolder and do not let workers edit the same file. If parallel
workers are unavailable, do the same collection sequentially and record that.

1. BLOG AND WRITING
Identify Karpathy's official personal site/blog and publicly authored writings.
Start from his official pages and follow their publication indexes and links.
Save complete article text, headings, code blocks and relevant captions, not
snippets or an agent-generated summary. Preserve original HTML when practical
alongside the readable Markdown. Record links to original assets. Collect linked
first-party writing hosted on other platforms where accessible. Distinguish
Karpathy's writing from third-party commentary and do not attribute others' words
to him.

2. GITHUB
Start from https://github.com/karpathy and enumerate public repositories and gists.
Also inspect officially linked Karpathy projects and educational organizations.
Save actual readable source files, READMEs, documentation and notebooks preserving
their repository paths, plus repository/gist URLs and the commit/revision captured.
Capture first-party explanations referenced by those projects. Record licenses.
Do not substitute README summaries for the repository contents. Do not execute
downloaded code or install repository dependencies. Exclude only generated caches,
dependency/build folders and Git object databases, and explicitly log exclusions.
For unusually large binaries or inaccessible assets, list each omission and why.

3. YOUTUBE
Identify his official channel and enumerate available videos/playlists. Also find
public talks/interviews linked by his official pages. Collect full timestamped
caption transcripts, titles, descriptions, URLs, video IDs, durations and chapter
information. Use existing yt-dlp and youtube-transcript-api where they work.
Preserve human-provided versus automatic-caption provenance. Save raw VTT/SRT or
JSON plus a readable Markdown transcript. Do not silently clean up quotations or
invent missing speech. If captions are missing, record the gap. A local transcription
fallback may be used if already available, but label it machine-transcribed rather
than claiming it is verified verbatim. Avoid paid services. A 429/rate limit means
record the failure and resume responsibly; do not hammer the endpoint.
Do not download entire video collections when transcripts suffice for this task.

4. X
Read public posts by https://x.com/karpathy using my existing logged-in Chrome
session. Target all accessible author posts from 2023-01-01 through the collection
date, including replies, threads, quote-post commentary and long-form articles.
If earlier public posts are accessible, collect them too and record the wider range.
Use date-bounded searches and profile/thread navigation to improve coverage.
Save exact visible post text, post ID, permanent URL, timestamp and relevant thread
relationships. Expand long posts and follow thread continuations. Retain the post's
links and code. Keep quoted/replied-to third-party text separately attributed.
For important images, preserve an accessible image or screenshot and any separately
labeled OCR; do not claim OCR is the author's exact text. Record inaccessible media.
Deduplicate by post ID, not by approximate text similarity. Do not collect my private
messages, bookmarks, account history or unrelated personal data. Do not like, follow,
post, reply, message or change account settings. If browser/search limits prevent
complete history, record exactly what ranges were checked and what remains unknown.

DELIVERABLES
Save physical local files containing the source content, not just links.
Use stable descriptive filenames and preserve meaningful source folder structure.
Each source subfolder must contain MANIFEST.json and MANIFEST.md with:
- local relative path, source title, source URL, source ID;
- author, original date if available, retrieval timestamp;
- source type, caption/transcription method or captured commit as appropriate;
- word count, byte count, SHA-256 hash;
- collection status and any incomplete/truncated sections.

Each source subfolder must also contain FAILURES.md and COVERAGE.md listing:
- sources discovered, successfully saved and failed;
- explicit exclusions with individual source URLs/paths and reasons;
- date ranges/searches/playlists/repository pagination checked;
- earliest/latest captured dates and coverage limitations;
- where to resume, without storing authentication material.

At the collection root write COLLECTION-REPORT.md with per-source counts, word
counts, completion status, exact collection location and outstanding gaps.
Treat duplicate statements from different original sources as separate evidence;
only skip identical copies of the same source, and record the duplicate.

Do not say “everything collected” merely because scrolling stopped or a search
returned no results. Separate verified completeness from best-effort coverage.
Do not use the video's approximate 700,000-word result as a target to pad or a
required success count. Preserve the real sources and report the real totals.

When finished, give me the collection path, per-source counts, failures and remaining
coverage gaps. Stop there. The next wiki/rules/agent stages belong to Claude/Codex.
```
