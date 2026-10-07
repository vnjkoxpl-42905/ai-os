# External tooling

Programs this OS shells out to. They are **not** in the skill DB and **not** git-tracked here —
they are system software, installed the way this machine installs software. A skill is text an
agent reads; these are binaries an agent runs. The distinction is why `yt-dlp` and `opencli` live
in `/usr/local` and not in `skills/`: they are machine-local, would not survive a clone of this
vault, and tracking them would push dead references to every checkout.

Last verified: 2026-07-17.

| Tool | Installed at | Install/update | Health check |
|---|---|---|---|
| `yt-dlp` | `/usr/local/bin/yt-dlp` (2026.07.04) | `brew install yt-dlp` | `yt-dlp --version` |
| `gh` | `/usr/local/bin/gh` | `brew install gh` | `gh auth status` |
| `opencli` | `/usr/local/bin/opencli` → `/usr/local/lib/node_modules/@jackwener/opencli` (1.8.6) | `npm install -g @jackwener/opencli` | `opencli doctor` |
| `node` / `npm` | `/usr/local/bin` (v26.0.0 / 11.12.1) | `brew install node` | `node --version` |
| `ffmpeg` | not installed | `brew install ffmpeg` | needed only for audio transcription |

## YouTube — yt-dlp is the default

Covers all three of transcripts, search, and channel browsing, free, with no key:

```bash
yt-dlp --skip-download --write-auto-sub --write-info-json --sub-lang en URL   # captions + chapters
yt-dlp "ytsearch5:query" --flat-playlist --print "%(id)s | %(title)s"          # search
yt-dlp "https://www.youtube.com/@handle/videos" --flat-playlist --playlist-end 10 --print "%(id)s | %(title)s"
```

Captions are YouTube's **ASR**, served with a punctuation layer, and carry **word-level timestamps**.
Technical jargon is unreliable (`Claude`→`cloud`, `Anthropic`→`enthropic`, `CLAUDE.md` never spelled) —
see `raw/sources/youtube/jdbOVepEtUE/PROVENANCE.md`. Reliable for locating a timecode; verify before
quoting.

`YOUTUBE_API_KEY` (`.env`) is good for search, metadata, comments, and chapters. It **cannot** fetch
transcripts: `captions.download` rejects API keys (401) and, even with OAuth, only returns captions
for videos you own.

## Web, search, GitHub

- **Web → text:** `curl -s "https://r.jina.ai/URL"` (Jina Reader). No key.
- **Semantic web search:** Exa. `EXA_API_KEY` in `.env`.
- **GitHub:** `gh` CLI, already authenticated (scopes: `gist`, `read:org`, `repo`).

## OpenCLI — drives real Chrome, reuses live logins

Daemon on port 19825 + Chrome Web Store extension (v1.0.22). Reddit / Facebook / Instagram /
Twitter / Xiaohongshu read access works because it reuses **Joshua's own logged-in browser
sessions** — no separate tokens, no cookies handed to the agent.

**It is not read-only.** Confirmed write commands exist (source read 2026-07-17):

- **Reddit:** `comment`, `reply`, `upvote`/downvote, `save`, `subscribe`. No new-post command.
- **Facebook:** `add-friend`, `join-group`. No post/comment. **No Messenger support at all** —
  `marketplace-inbox` is read-only and cannot reply.
- **Instagram:** full write surface — `post`, `reel`, `story`, `comment`, `like`, `follow`, `note`.

Every write action is Joshua's real account. **Never invoke one without showing him the exact
content and target and getting an explicit yes, per action.** Reading is normal work; writing is not.

## Skills that wrap paid services

`skills/claude/youtube-full` (TranscriptAPI) is installed but needs `TRANSCRIPT_API_KEY`, which
Joshua must provision himself — see that skill's `references/auth-setup.md`. Free tier is 100
credits, then $5/mo. Prefer `yt-dlp`; reach for it only when yt-dlp is blocked.

## Evaluated and rejected

- **IA-Programming/Youtube-MCP** — abandoned (last push 2025-03-26), pins
  `youtube-transcript-api==0.6.3` against current 1.2.4, README references a `requirements.txt`
  that does not exist. Returns flat text, no timestamps. Strictly worse than yt-dlp.
- **Panniantong/Agent-Reach full install** — actively maintained and well-built, but the full
  flow installs system packages and bulk-extracts cookies from Chrome for Twitter/Xiaohongshu/
  Xueqiu. Its own README warns this risks account bans and advises a burner account. Only its
  Whisper transcription piece is interesting; not installed.
