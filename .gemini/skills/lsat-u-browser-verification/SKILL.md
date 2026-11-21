---
name: lsat-u-browser-verification
description: Control and verify the dedicated LSAT U persistent browser environment on port 9223 for visual inspection, DOM analysis, console checking, and multi-viewport testing on https://lsatprep.study and localhost:8080.
---

# LSAT U Browser Verification Skill

This skill controls the dedicated, persistent Chrome verification instance configured for Joshua and Antigravity. It connects over Chrome DevTools Protocol (CDP) to port `9223` with the dedicated authenticated profile at `C:\Users\Joshu\AppData\Local\LSATU-Agent-Chrome`.

## When to Use
Activate this skill whenever Joshua asks to:
- Inspect, test, or visually verify pages on `https://lsatprep.study` or `http://localhost:8080`
- Take screenshots across standard viewports (1440x900, 1366x768, 1280x800, 1024x768, 390x844)
- Check DOM layout, element spacing, or console errors on LSAT U
- Verify student views, drills, testing centre, or dashboard changes
- Check if the agent browser connection is healthy

## Architecture and Endpoints
- **Dedicated Debugging Port**: `9223`
- **CDP URL**: `http://127.0.0.1:9223`
- **Profile Directory**: `C:\Users\Joshu\AppData\Local\LSATU-Agent-Chrome`
- **Antigravity MCP Server**: `chrome-devtools` (registered in `~/.gemini/config/mcp_config.json`)

## Quick Automation Commands

### 1. Check Connection and Auth Status
```powershell
node C:\Users\Joshu\Tools\LSATU-Agent\agent-browser.mjs status
```

### 2. Capture a Viewport Screenshot
```powershell
node C:\Users\Joshu\Tools\LSATU-Agent\agent-browser.mjs screenshot "C:/Users/Joshu/Tools/LSATU-Agent/current.png" 1440 900
```

### 3. Run the 5-Viewport Sweep
Runs standard viewports (desktop, laptop, tablet, mobile) and saves full diagnostic screenshots:
```powershell
node C:\Users\Joshu\Tools\LSATU-Agent\verify-viewports.mjs "https://lsatprep.study/classroom/drill?section=lr"
```

### 4. Launch or Relaunch Browser (if closed)
```powershell
python C:\Users\Joshu\Tools\LSATU-Agent\launch_browser.py
```
Or launch via the desktop shortcut: `LSAT U Agent Browser.lnk`.
