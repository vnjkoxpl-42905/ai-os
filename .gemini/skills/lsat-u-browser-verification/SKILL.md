---
name: lsat-u-browser-verification
description: Control and verify the dedicated LSAT U persistent browser environment on port 9223 for visual inspection, DOM analysis, console checking, multi-viewport testing, and pulling platform messages on https://lsatprep.study and localhost:8080. Trigger on "pull LSAT U messages", "check lsatprep.study messages", "access lsatprep.study", "check platform messages", or visual testing requests.
---

# LSAT U Browser Verification Skill

This skill controls the dedicated, persistent Chrome verification instance configured for Joshua and Antigravity. It connects over Chrome DevTools Protocol (CDP) to port `9223` with the dedicated authenticated profile at `C:\Users\Joshu\AppData\Local\LSATU-Agent-Chrome`.

## Trigger Phrases
Activate this skill whenever Joshua asks to:
- "pull LSAT U messages"
- "check lsatprep.study messages"
- "access lsatprep.study"
- "check platform messages"
- "inspect LSAT U"
- Take screenshots across standard viewports (1440x900, 1366x768, 1280x800, 1024x768, 390x844)
- Check DOM layout, element spacing, or console errors on LSAT U
- Verify student views, drills, testing centre, or dashboard changes
- Check if the agent browser connection is healthy

## Architecture and Endpoints
- **Dedicated Debugging Port**: `9223`
- **CDP URL**: `http://127.0.0.1:9223`
- **Profile Directory**: `C:\Users\Joshu\AppData\Local\LSATU-Agent-Chrome`
- **Tooling Directory**: `C:\Users\Joshu\Tools\LSATU-Agent\`
- **Antigravity MCP Server**: `chrome-devtools` (registered in `~/.gemini/config/mcp_config.json`)
- **Key Platform Surfaces**:
  - Messages / Teacher Inbox: `https://lsatprep.study/teacher?ws=messages`
  - Student Roster & Submissions: `https://lsatprep.study/teacher?ws=students`
  - Classroom & Drills: `https://lsatprep.study/classroom`
  - Local Dev Server: `http://localhost:8080`

## Step-by-Step Execution Path: "Pull LSAT U Messages"

When Joshua asks to "pull LSAT U messages" or check platform messages:

1. **Run the Automated Extractor**:
   Execute the dedicated platform extractor via PowerShell:
   ```powershell
   node C:\Users\Joshu\Tools\LSATU-Agent\pull_platform_messages.mjs
   ```
   This script automatically:
   - Verifies if Chrome is running on port 9223 (launches it automatically if not).
   - Connects over CDP to `http://127.0.0.1:9223`.
   - Navigates to `https://lsatprep.study/teacher?ws=messages`.
   - Checks authentication state:
     - If redirected to `/auth`, reports that login is needed and captures a screenshot to `latest_messages.png`.
     - If authenticated, extracts student conversation threads, unread counts, and recent message snippets.
   - Saves a viewport snapshot to `C:\Users\Joshu\Tools\LSATU-Agent\latest_messages.png`.
   - Returns structured JSON to the console.

2. **Present the Findings**:
   - Report whether the session is authenticated.
   - List active student conversations, unread alerts, and the latest messages.

3. **Platform Action Routing**:
   - For administrative actions (assigning drills, grading, posting notes), coordinate with the `lsat-u-platform-actions` skill.

## Additional Quick Commands

### Check Connection and Auth Status
```powershell
node C:\Users\Joshu\Tools\LSATU-Agent\agent-browser.mjs status
```

### Capture a Viewport Screenshot
```powershell
node C:\Users\Joshu\Tools\LSATU-Agent\agent-browser.mjs screenshot "C:/Users/Joshu/Tools/LSATU-Agent/current.png" 1440 900
```

### Run the 5-Viewport Sweep
Runs standard viewports (desktop, laptop, tablet, mobile) and saves diagnostic screenshots:
```powershell
node C:\Users\Joshu\Tools\LSATU-Agent\verify-viewports.mjs "https://lsatprep.study/classroom/drill?section=lr"
```

### Launch / Health Check
```powershell
pwsh -File C:\Users\Joshu\Tools\LSATU-Agent\start-dev-session.ps1
```
Or launch via the desktop shortcut: `LSAT U Agent Browser.lnk`.
