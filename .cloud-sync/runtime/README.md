# Portable runtime context

Read INDEX.json, then the relevant runtime instruction file, skills and memories. Preserve agents, Claude and Codex skills as separate catalogs. Claude memories are under claude/memories/<original-project-key>/; remap to the cloud checkout rather than recreating a Windows path. Codex memories.json is readable context, not a native Claude memory database.

These are exported sources. Do not blindly activate Windows paths, hooks or shell commands. Check cloud compatibility before installing a skill. Settings, credentials, OAuth sessions, browser state, plugin caches and executables are excluded. The enclosing snapshot secret scan applies to every exported file.
