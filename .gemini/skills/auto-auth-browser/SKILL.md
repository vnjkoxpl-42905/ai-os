---
name: auto-auth-browser
description: Automatically authenticate and manage session persistence for Loophole Online and LSAT platforms using Playwright CDP and .env credentials, eliminating manual login barriers.
---

# Auto-Auth Browser

Automate authentication and session state management for protected web applications (such as Loophole Online, LSAT U, and TutorOcean). This skill ensures that whenever Joshua or an agent requests a protected lesson, video, or drill, authentication is handled silently and automatically without user intervention.

## When to Use

Activate this skill when Joshua says:
- "Log into Loophole" / "Sign into my Loophole account"
- "Auto-login to the browser"
- "Open this link and make sure I am logged in"
- "Session expired, re-authenticate"
- "Find the lesson link for [topic]"

## Prerequisites & Credential Model

Credentials must be stored in the repository root `.env` file (which is git-ignored and never tracked):
```env
LOOPHOLE_EMAIL=your-email@example.com
LOOPHOLE_PASSWORD=your-password
```

## Quick Recipes

All scripts reside in:
`.gemini/skills/auto-auth-browser/scripts/`

### 1. Verify Session & Auto-Login
Check if the current browser session is authenticated. If not, automatically submit the sign-in form and navigate to the requested target:
```powershell
node .gemini/skills/auto-auth-browser/scripts/auto-login.mjs --target "https://new.theloophole.com/training-camp/browse/stage/learn/video/conditional-sufficient-assumption-sa-strategy"
```

### 2. Reconnaissance & Link Discovery via Firecrawl
Search course maps and training camp playlists for target lesson URLs using Firecrawl:
```powershell
node .gemini/skills/auto-auth-browser/scripts/firecrawl-recon.mjs "conditional-sufficient-assumption"
```

## Security & Resilience Protocol

1. **Zero Exposure:** Passwords and tokens are never printed to terminal output, transcripts, or committed to Git.
2. **Session Persistence:** Once authenticated, cookies and session tokens are saved to `~/.edge-live-profile/storageState.json` so subsequent executions run without repeating form submissions.
3. **Graceful Fallback:** If credentials are missing in `.env`, the script halts immediately with an explicit notification instructing Joshua to populate `.env`.
