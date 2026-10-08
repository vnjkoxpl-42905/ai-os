# Browser Agent Playbook and Operational Lessons

This document is the mandatory pre-flight checklist and operational manual for all browser agents operating on Joshua's Windows environment. Every browser agent must read this file before performing web automation, scraping, or platform actions, and update it whenever new edge cases, mistakes, or shortcuts are discovered.

---

## 1. Pre-Flight Checklist (Run Before Every Browsing Task)

1. **Verify Browser Port 9223 First:**
   * Do not assume Chrome is running. Check port 9223 before sending commands.
   * If not running, spawn via WMI to detach from IDE process management:
     ```powershell
     powershell -ExecutionPolicy Bypass -File C:\Users\Joshu\Tools\LSATU-Agent\launch-agent-browser.ps1
     ```
   * Never launch an unattached or secondary Chrome instance. All sessions, cookies, and logins live in `%LOCALAPPDATA%\LSATU-Agent-Chrome`.

2. **Protect the 4 Managed Tabs:**
   * Before interacting with tabs, call `list_pages` to inspect open targets.
   * Never navigate or close the four primary tabs:
     * Tab 1: Reddit (`https://chat.reddit.com`)
     * Tab 2: Facebook Messenger (`https://www.facebook.com/messages`)
     * Tab 3: 7Sage (`https://7sage.com`)
     * Tab 4: LSAT U (`https://lsatprep.study`)
   * For any ad-hoc, research, or external scraping task (e.g. X, news, docs), always create a new tab via `new_page` or select a designated scratch tab.

3. **Verify Authentication State Before Scraping:**
   * Never blindly scrape a page that requires a login.
   * Check for the presence of login forms (e.g., input elements for password or "Sign in" buttons).
   * If logged out, stop immediately and alert Joshua to log in. Never attempt to guess or auto-fill credentials on protected personal platforms without explicit instruction.

---

## 2. Hard Mistakes Made and Lessons Learned

### Mistake 1: Calling MCP Tools Without Required Parameters
* **What went wrong:** Calling `take_snapshot` or `take_screenshot` without specifying `pageId` throws: `MCP error -32602: Input validation error: Required at pageId`.
* **The Rule:** Always pass the specific `pageId` returned from `list_pages` (e.g. `{"pageId": 5}`).

### Mistake 2: Single-Page Infinite Scrolling on Virtual DOMs
* **What went wrong:** Scrolling down a long profile page (like `x.com/username`) to collect hundreds of posts causes modern web frameworks (React/Virtual DOM) to unmount off-screen items. Memory bloats, items vanish from the DOM, and scrolling stops or skips data.
* **The Shortcut:** Use date-bounded search queries instead of infinite scroll.
  * Query format for X: `from:username since:YYYY-MM-DD until:YYYY-MM-DD` in 7-day or 14-day slices.
  * This guarantees 100% complete coverage and avoids virtual DOM drops.

### Mistake 3: Windows Console Encoding Failures (cp1252)
* **What went wrong:** When scraping tweets, titles, or transcripts containing emojis, foreign characters, or music notes, printing directly to PowerShell/cmd crashed Python scripts with: `UnicodeEncodeError: 'charmap' codec can't encode characters...`.
* **The Rule:** Every Python extraction script on Windows must include this line at the top:
  ```python
  import sys
  if sys.platform == "win32":
      sys.stdout.reconfigure(encoding="utf-8")
  ```

### Mistake 4: Slow Manual MCP Tool Loops for High-Volume Extraction
* **What went wrong:** Firing separate MCP tool calls (`evaluate_script` -> `wait_for` -> `scroll`) across hundreds of items creates massive latency and risks turn limits.
* **The Shortcut:** For high-volume scraping, write a standalone Node.js or Python script that connects directly over CDP (`http://127.0.0.1:9223`) and runs locally. Save output incrementally to `.jsonl` files so progress survives interruptions.

---

## 3. High-Efficiency Browser Shortcuts

* **Direct CDP WebSocket Connection:**
  * Endpoint: `http://127.0.0.1:9223/json/version` gives the browser WebSocket debugger URL.
  * `http://127.0.0.1:9223/json/list` gives all open target tabs and their individual WebSocket URLs.
* **Resumable Extraction Pattern:**
  * Always append extracted data to an append-only JSON Lines file (`posts.jsonl` or `items.jsonl`).
  * Log completed progress windows into a separate index (`windows.jsonl` or `completed_ids.txt`).
  * If the script or connection is stopped, it can resume from the exact last completed window without duplicating data.
* **Zero Credential Export Rule:**
  * Never export cookies, session tokens, or auth headers to disk, vault files, or git.
  * Let the persistent browser profile handle authentication state internally.

---

## 4. Maintenance and Updating

Whenever an agent encounters a new browser error, timeout pattern, or platform anti-bot behavior:
1. Append the specific error and cause under "Hard Mistakes Made".
2. Add the proven workaround under "High-Efficiency Browser Shortcuts".
3. Keep instructions concise and actionable.
