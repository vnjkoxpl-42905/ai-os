# Loophole routing across Claude, Codex and Gemini

Verified 2026-10-19 on Joshua's Windows machine. This is an execution receipt, not another retrieval guide.

## One shared procedure

[AI-RETRIEVAL.md](../AI-RETRIEVAL.md) owns discovery, `search`, `open`, full authored `instructions`, ambiguity, pagination and source qualifications. [The library map](../library-map.generated.md) owns inventory and gaps. No global skill, vendor configuration merge or duplicate source library was created.

Each runtime's workspace entry routes here automatically:

- Codex: `C:/Users/Joshu/dev/ai-os/AGENTS.md`.
- Claude: `C:/Users/Joshu/dev/ai-os/CLAUDE.md`.
- Gemini / Antigravity: `C:/Users/Joshu/dev/ai-os/GEMINI.md`.

The same thin machine-level Loophole route is present in:

- `C:/Users/Joshu/.codex/AGENTS.md`.
- `C:/Users/Joshu/.claude/CLAUDE.md`.
- `C:/Users/Joshu/.gemini/GEMINI.md`.

These global routes identify the absolute guide and vault root even when another project is open. Existing unrelated global bytes were preserved with compare-and-swap checks. Global skills and vendor settings were not changed. On another machine the library location and source bytes must be restored appropriately; this is not proof that every device has the archives.

Within the library, [AGENTS.md](../AGENTS.md) and [CLAUDE.md](../CLAUDE.md) share a byte-identical contract. [GEMINI.md](../GEMINI.md) is a thin adapter to that contract. Root routing, retrieval and guardrail sections were checked for Claude/Codex parity. Shared documentation links resolve.

## What was actually tested

| Runtime / layer | Result | Evidence boundary |
|---|---|---|
| Codex | Global routing appeared in the refreshed instruction context; prior independent fresh-agent retrieval tests passed | See [acceptance report](fresh-agent-acceptance.generated.md). This does not imply automatic reload in every existing session. |
| Claude Code native CLI | Passed a new noninteractive, read-only test using normal workspace instructions, without paths or retrieval command hints | The native run independently discovered the shared guide through CLAUDE.md, used search/open/instructions, read full Decaf written notes, and retrieved the complete Conditional Rehab procedures on one page with no gaps. No permission denials or source edits. Only the opening 80 caption lines were read; no complete lecture listening claim. |
| Gemini / Antigravity | Saved global/workspace/domain route and target files verified | Neither `gemini` nor `antigravity` CLI was available on PATH. No native Gemini inference session was run. |
| Shared local engine | Search-to-open resolved the exact Decaf instruction package with video present; exact Conditional Rehab instruction query succeeded | No provider-specific skill or live website was required. Media presence is not a new binary hash or listening audit. |

The native Claude test used the configured default model, 9 turns, no session persistence, and reported a list-price estimate of USD 2.5752931. It required no browser, web search, source-site login or parent retrieval directions. Further native calls were not repeated.

New sessions should use their normal instruction loading. Existing sessions may require their normal reload or restart to pick up saved instructions. Runtime availability and configuration checks remain distinct from a live acceptance test.
