# Tavily execution receipt

Date: 2026-10-28. Provider requested: Tavily. No provider substitution performed.

Read the installed `tavily-cli` and `tavily-search` skills. Resolved executable to `C:\Users\Joshu\.local\bin\tvly.exe`.

Attempted command from the AI OS root:

```powershell
tvly search 'interactive training session performance charts feedback interface Linear Rive Raycast design system' --depth advanced --max-results 12 --include-raw-content --json -o .tavily/conditional-design-20261028/discovery.json
```

The shell failed before contacting Tavily:

```text
Program 'tvly.exe' failed to run: An error occurred trying to start process
'C:\Users\Joshu\.local\bin\tvly.exe' with working directory
'C:\Users\Joshu\dev\ai-os'. An Application Control policy has blocked this file.
```

Exit code: 1 (`ResourceUnavailable`). This was an operating-system launch failure, not a Tavily authentication or quota response.

No Tavily MCP tool is available in the current tool inventory. A uv package directory exists under `C:\Users\Joshu\AppData\Roaming\uv\tools\tavily-cli`, but it was not launched through another interpreter to bypass Application Control.

Verified successful provider calls: 0. Verified usage: no provider usage returned. Authentication and remaining credits: unknown. No search results, source screenshots or live-source claims were produced by Tavily.
