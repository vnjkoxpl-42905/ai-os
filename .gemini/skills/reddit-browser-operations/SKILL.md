---
name: reddit-browser-operations
description: Control and verify the dedicated Reddit persistent browser environment on port 9224 for Reddit research, community monitoring, DOM analysis, and session management. Trigger on "pull Reddit messages", "check Reddit messages", "who messaged me on Reddit", "Reddit inbox", "Reddit chat", or any Reddit browser task.
---

# Reddit Browser Operations Skill

This skill controls the dedicated, persistent Chrome instance configured for Joshua and Antigravity Command Center operations on Reddit. It connects over Chrome DevTools Protocol (CDP) to port `9224` with the dedicated authenticated profile at `C:\Users\Joshu\AppData\Local\Reddit-Agent-Chrome`.

## Trigger Phrases
Activate this skill whenever Joshua says:
- "pull Reddit messages"
- "check Reddit messages"
- "who messaged me on Reddit"
- "look at my Reddit inbox"
- "check Reddit chat"
- "inspect Reddit"
- Any request regarding Reddit communications, threads, or visual checks

## Architecture and Endpoints
- **Dedicated Debugging Port**: `9224`
- **CDP URL**: `http://127.0.0.1:9224`
- **Profile Directory**: `C:\Users\Joshu\AppData\Local\Reddit-Agent-Chrome`
- **Tooling Directory**: `C:\Users\Joshu\Tools\Reddit-Agent\`
- **Target URLs**:
  - Reddit Chat: `https://chat.reddit.com` (redirects to `https://www.reddit.com/chat/room/...`)
  - Reddit Inbox: `https://www.reddit.com/message/inbox`

## Step-by-Step Execution Path: "Pull Reddit Messages"

When Joshua asks to "pull Reddit messages":

1. **Run the Automated Extractor**:
   Execute the dedicated message extractor via PowerShell:
   ```powershell
   node C:\Users\Joshu\Tools\Reddit-Agent\pull_reddit_messages.mjs
   ```
   This script automatically:
   - Verifies if Chrome is running on port 9224 (launches it automatically if not).
   - Connects to Chrome over CDP at `http://127.0.0.1:9224`.
   - Navigates to Reddit Chat (`https://chat.reddit.com`).
   - Pierces Reddit's web-component Shadow DOM to extract all 1:1 chat threads with sender names, timestamps, and message previews.
   - Saves a clean visual screenshot to `C:\Users\Joshu\Tools\Reddit-Agent\latest_chat.png`.
   - Navigates to Legacy Inbox (`https://www.reddit.com/message/inbox`) and captures legacy PMs/replies.
   - Returns structured JSON to the console.

2. **Present the Findings**:
   - State the most recent sender, timestamp, and message text clearly.
   - List other recent active conversation threads (sender, date, snippet).
   - If visual context is helpful, inspect `C:\Users\Joshu\Tools\Reddit-Agent\latest_chat.png`.

3. **Drafting Policy**:
   - **Never auto-send replies.**
   - All correspondence intended for a prospective student or user must route through `wiki/teaching-voice.md`.
   - Present the drafted reply in chat and wait for Joshua's explicit approval or instructions.

## Additional Operational Commands

### Check Browser and Login Status
```powershell
node C:\Users\Joshu\Tools\Reddit-Agent\agent-browser.mjs status
```

### Check Active CDP Targets
```powershell
python C:\Users\Joshu\Tools\Reddit-Agent\check_session.py
```

### Capture Viewport Screenshot
```powershell
node C:\Users\Joshu\Tools\Reddit-Agent\agent-browser.mjs screenshot "C:/Users/Joshu/Tools/Reddit-Agent/current.png" 1440 900
```

### Launch / Health Check
```powershell
pwsh -File C:\Users\Joshu\Tools\Reddit-Agent\start-reddit-session.ps1
```
Or launch via desktop shortcut: `Reddit Agent Browser.lnk`.
