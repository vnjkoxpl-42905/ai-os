---
name: facebook-browser-operations
description: Direct CDP automation, session verification, and message extraction for Facebook Messenger on port 9226.
---

# Facebook Browser Operations

## Overview
Controls the dedicated, persistent Chrome browser instance for Facebook Messenger operations.
- **Port**: `9226` (CDP endpoint: `http://127.0.0.1:9226`)
- **Profile**: `C:\Users\Joshu\AppData\Local\Facebook-Agent-Chrome`
- **Tooling Directory**: `C:\Users\Joshu\Tools\Facebook-Agent\`
- **Target URL**: `https://www.facebook.com/messages`

All sessions, login state, and cookies persist in `Facebook-Agent-Chrome`. Authentication is performed once by Joshua and remains permanently saved across reboots.

## Commands

### 1. Launch Browser
Spawns the browser via WMI detached process:
```bash
python C:\Users\Joshu\Tools\Facebook-Agent\launch_browser.py
```

### 2. Inspect Session Status
Checks active tabs and titles via CDP:
```bash
python C:\Users\Joshu\Tools\Facebook-Agent\check_session.py
```

### 3. Check Authentication State
Verifies if user session cookies are present:
```bash
node C:\Users\Joshu\Tools\Facebook-Agent\check_auth.mjs
```

### 4. Pull Messenger Conversations
Pulls recent message threads and senders:
```bash
node C:\Users\Joshu\Tools\Facebook-Agent\pull_facebook_messages.mjs
```
