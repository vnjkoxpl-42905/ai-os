---
name: 7sage-browser-operations
description: Direct CDP automation, session verification, and notification extraction for 7Sage LSAT platform on port 9225.
---

# 7Sage Browser Operations

## Overview
Controls the dedicated, persistent Chrome browser instance for 7Sage operations.
- **Port**: `9225` (CDP endpoint: `http://127.0.0.1:9225`)
- **Profile**: `C:\Users\Joshu\AppData\Local\7Sage-Agent-Chrome`
- **Tooling Directory**: `C:\Users\Joshu\Tools\7Sage-Agent\`
- **Target URL**: `https://7sage.com`

All sessions and cookies persist in `7Sage-Agent-Chrome`. Authentication is performed once by Joshua and remains permanently saved across reboots.

## Commands

### 1. Launch Browser
Spawns the browser via WMI detached process:
```bash
python C:\Users\Joshu\Tools\7Sage-Agent\launch_browser.py
```

### 2. Inspect Session Status
Checks active tabs and titles via CDP:
```bash
python C:\Users\Joshu\Tools\7Sage-Agent\check_session.py
```

### 3. Check Authentication State
Verifies if session cookies are present:
```bash
node C:\Users\Joshu\Tools\7Sage-Agent\check_auth.mjs
```

### 4. Pull Notifications / Messages
Pulls notifications and updates:
```bash
node C:\Users\Joshu\Tools\7Sage-Agent\pull_7sage_messages.mjs
```
