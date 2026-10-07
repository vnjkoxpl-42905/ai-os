---
name: edge-live-control
description: Elite live automation and interactive control for Microsoft Edge on Windows via Playwright CDP. Enables inspecting active tabs, extracting authenticated DOM/media/transcripts, clicking elements, taking screenshots, and executing JavaScript.
---

# Edge Live Control

Operate, inspect, and interact with Microsoft Edge live on Joshua's Windows environment. This skill attaches directly to the running Edge instance over the Chrome DevTools Protocol (CDP) on port 9223, bypassing cloud scrape auth gates and allowing real-time inspection of authenticated applications (such as Loophole Online, LSAT U, TutorOcean, and Cal.com).

## When to Use

Activate this skill whenever Joshua says:
- "Go to Microsoft Edge" / "Check my Microsoft Edge"
- "Look at what is on my Edge page" / "What is on my browser?"
- "Go to this tab in Edge" / "Switch to tab"
- "Tear down this video" / "Extract the transcript from this video lesson"
- "Click [button/element] in Edge"
- "Take a screenshot of my Edge tab"

## Prerequisites & Architecture

1. **Port Separation**: Chrome occupies port 9222. Edge uses port 9223.
2. **CDP Attachment**: Playwright connects directly to `http://localhost:9223` using `chromium.connectOverCDP`.
3. **Session Preservation**: Using Edge with `--remote-debugging-port=9223` retains all cookies, logins, and open tabs.

## Quick Recipes

All helper scripts reside in:
`.gemini/skills/edge-live-control/scripts/`

### 1. Verify or Start Edge with Debugging Port
Check if Edge is already listening on port 9223. If not, launch or restart Edge with debugging enabled:
```powershell
powershell -ExecutionPolicy Bypass -File .gemini/skills/edge-live-control/scripts/start-edge-debugging.ps1 -Port 9223
```

### 2. List All Open Tabs
List every active tab across all Edge windows:
```powershell
node .gemini/skills/edge-live-control/scripts/edge-control.mjs tabs
```
To get machine-readable JSON:
```powershell
node .gemini/skills/edge-live-control/scripts/edge-control.mjs tabs --json
```

### 3. Inspect a Tab
Target a tab by title or URL substring:
```powershell
node .gemini/skills/edge-live-control/scripts/edge-control.mjs inspect --match "loophole"
```
To dump only visible body text:
```powershell
node .gemini/skills/edge-live-control/scripts/edge-control.mjs inspect --match "loophole" --text-only
```
To query a specific CSS selector:
```powershell
node .gemini/skills/edge-live-control/scripts/edge-control.mjs inspect --match "loophole" --selector "main"
```

### 4. Extract Video Player & Transcript
Inspect HTML5 `<video>`, current playback position, duration, and WebVTT caption tracks:
```powershell
node .gemini/skills/edge-live-control/scripts/edge-control.mjs video --match "loophole"
```

### 5. Click an Element
Click by CSS selector:
```powershell
node .gemini/skills/edge-live-control/scripts/edge-control.mjs click --match "loophole" --selector "button[aria-label='Play']"
```
Or click by visible text:
```powershell
node .gemini/skills/edge-live-control/scripts/edge-control.mjs click --match "loophole" --text "Continue"
```

### 6. Take a Screenshot
Capture the current tab viewport:
```powershell
node .gemini/skills/edge-live-control/scripts/edge-control.mjs screenshot --match "loophole" --out .gemini/output/edge-tab.png
```

### 7. Execute Custom JavaScript in Page
Evaluate arbitrary JavaScript inside the page context:
```powershell
node .gemini/skills/edge-live-control/scripts/edge-control.mjs eval --match "loophole" --code "document.title"
```

## Teardown Protocol for Lesson Videos

When asked to tear down an online video lesson:
1. Identify the tab containing the lesson URL.
2. Run `video --match <term>` to extract the video source, player parameters, and closed-caption cues.
3. Run `inspect --match <term> --selector "main"` to extract the lesson title, accompanying drill problems, and notes.
4. Run `screenshot` if whiteboard or slide diagrams are present.
5. Ingest extracted notes into the LLM wiki or format into a comprehensive strategic teardown report comparing the pedagogy against Joshua's curriculum standards.
