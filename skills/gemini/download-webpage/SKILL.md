---
name: download-webpage
description: Download, archive, and extract any webpage as a self-contained offline HTML file, CDP MHTML snapshot, raw SSR source, full-page screenshot, and clean Markdown text. Use whenever Joshua asks to download a webpage, save a site as HTML, export a page to hand off, capture a webpage, or create an offline bundle.
---

# Download Webpage Skill

This skill captures and archives complete, high-fidelity representations of any live webpage for offline handoff, inspection, or ingestion. It uses Joshua's dedicated Agent Browser on port 9223 over Chrome DevTools Protocol (CDP) to fully render client-side frameworks, execute scroll-triggered hydration, and generate self-contained bundles.

## Trigger Phrases
Activate this skill whenever Joshua says:
- "download this page" / "download webpage"
- "save this site as html"
- "get this page downloaded as an html I can hand off"
- "export webpage to hand off"
- "save page offline"
- "capture webpage bundle"

## Output Formats Produced

Every run generates five distinct files inside a dedicated handoff folder (`C:\Users\Joshu\Desktop\<slug>-handoff\`):

1. **Standalone Executed HTML (`<slug>-standalone.html`)**:
   - The fully rendered live DOM after scroll-based hydration.
   - All external stylesheets are fetched, rewritten (converting relative `url(...)` declarations to absolute URLs), and inlined into `<style>` blocks in the `<head>`.
   - Relative `src`, `href`, and `srcset` attributes are converted to absolute URLs.
   - Client-side hydration scripts (`<script>` tags and framework router announcers) are stripped so opening the file locally via `file://` does not crash or erase the DOM.
   - By default, a copy is also placed directly at `C:\Users\Joshu\Desktop\<slug>.html` for instant drag-and-drop handoff.

2. **CDP MHTML Web Archive (`<slug>.mhtml`)**:
   - Single-file MIME multipart archive (RFC 2557) captured natively via Chrome DevTools Protocol (`Page.captureSnapshot`).
   - Bundles binary images, custom web fonts, SVG graphics, and stylesheets into one file.
   - Opens natively in Google Chrome and Microsoft Edge with 100% offline visual fidelity.

3. **Raw SSR Source HTML (`<slug>-raw-source.html`)**:
   - The original HTTP response payload before client JavaScript runs.
   - Preserves initial SSR state (`__NEXT_DATA__`, meta tags, JSON-LD schemas, inline JSON payloads).

4. **Full-Page Screenshot (`<slug>-fullpage.png`)**:
   - High-resolution visual capture of the entire scrollable height (1440px wide).

5. **Extracted Markdown (`<slug>-content.md`)**:
   - Clean structured text extraction containing the page title, metadata, headings (H1-H4), paragraphs, lists, and quotes. Ideal for pasting into prompt context or sending to another agent.

## Execution Procedure

Run the dedicated runner script using Node:

```powershell
node C:\Users\Joshu\dev\ai-os\skills\gemini\download-webpage\scripts\download_webpage.mjs "<URL>" [options]
```

### Common Command Variations

1. **Standard Download (leaves page visible in Agent Browser + Desktop shortcut)**:
   ```powershell
   node C:\Users\Joshu\dev\ai-os\skills\gemini\download-webpage\scripts\download_webpage.mjs "https://example.com"
   ```

2. **Custom Output Directory**:
   ```powershell
   node C:\Users\Joshu\dev\ai-os\skills\gemini\download-webpage\scripts\download_webpage.mjs "https://example.com" --out-dir "C:/Users/Joshu/dev/ai-os/raw/sources/example"
   ```

3. **Background Capture (close tab when done, no Desktop shortcut)**:
   ```powershell
   node C:\Users\Joshu\dev\ai-os\skills\gemini\download-webpage\scripts\download_webpage.mjs "https://example.com" --close --no-desktop
   ```

4. **Custom Viewport (e.g. Mobile or Tablet)**:
   ```powershell
   node C:\Users\Joshu\dev\ai-os\skills\gemini\download-webpage\scripts\download_webpage.mjs "https://example.com" --width 390 --height 844
   ```

## Infrastructure and Fallbacks

- **Primary Browser**: Connects to the dedicated Agent Browser on Port 9223 (`http://127.0.0.1:9223`, profile `C:\Users\Joshu\AppData\Local\LSATU-Agent-Chrome`).
- **Auto-Launch**: If the Agent Browser is not running when the script is invoked, it automatically triggers `C:\Users\Joshu\Tools\LSATU-Agent\launch-agent-browser.ps1` via PowerShell and waits for port 9223 to become available.
- **Scroll Step Delay**: Executes progressive 450px vertical scroll sweeps with 120ms pauses across the document height to trigger all `IntersectionObserver` callbacks, Framer Motion transitions, and lazy image loaders before capturing snapshots.
