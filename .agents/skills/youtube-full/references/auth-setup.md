# TranscriptAPI — key handling in this OS

**This file replaces the upstream `auth-setup.md` deliberately. Do not restore the vendor version.**

## The key

`TRANSCRIPT_API_KEY` lives in `C:/Users/Joshu/dev/ai-os/.env` (mode 600, git-ignored via `.gitignore:13`),
alongside `ANTHROPIC_API_KEY`, `EXA_API_KEY`, `YOUTUBE_API_KEY`, and the rest. That is this OS's
only home for API keys — per `CLAUDE.md`, "API keys live in the root `.env`".

To use it in a request, source the env rather than interpolating the value into a command:

```bash
set -a; . C:/Users/Joshu/dev/ai-os/.env; set +a
curl -s "https://transcriptapi.com/api/v2/youtube/transcript?video_url=URL&format=text&include_timestamp=true" \
  -H "Authorization: Bearer $TRANSCRIPT_API_KEY" \
  -H "User-Agent: ClaudeCode/1.0"
```

The `User-Agent` header is mandatory — Cloudflare returns 403 (code 1010) without it.

## Provisioning — Joshua's job, not the agent's

If `TRANSCRIPT_API_KEY` is unset, **stop and ask Joshua for it.** He signs up at
<https://transcriptapi.com> and pastes the `sk_...` key; the agent appends it to `.env`.

Do **not**:

- register an account on his behalf, or ask for his email to do so
- request or relay an emailed OTP code
- write the key into shell profiles (`~/.zshenv`, `~/.zprofile`, `~/.profile`) — `.env` is the only store

Account creation is out of scope for the assistant, and this OS does not scatter secrets into
shell startup files.

## Why the upstream auth doc was dropped

The vendor's `references/auth-setup.md` (repo: ZeroPointRepo/youtube-skills, read 2026-07-17)
instructs agents to write credentials to a temp file specifically so the value never appears in
tool output, explaining that this defeats runtimes which "redact values matching patterns like
`access_token` or bearer tokens from tool output before the model sees them."

Token redaction is a safety control. Guidance whose stated purpose is evading it does not belong
in this vault, regardless of intent. The API reference in `SKILL.md` is retained and unmodified —
only the auth flow was replaced.

## Cost — check before bulk runs

Free tier is 100 credits; then $5/month for 1,000 credits/month. Most calls cost 1 credit
(channel resolve and latest are free). A "transcribe every video in this channel" request can
burn the free tier in one command — confirm with Joshua before any bulk operation.

## Prefer yt-dlp unless there's a reason not to

`yt-dlp` is installed and covers transcripts, search (`ytsearch5:query`), and channel browsing
(`https://www.youtube.com/@handle/videos`) for free, with **word-level timestamps** this API does
not return. See `system/tooling.md`. Reach for TranscriptAPI when yt-dlp is blocked or rate-limited
(e.g. running from a cloud IP), not by default.
