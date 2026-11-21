# Integration evaluation, 2026-10-29

The guide links and recommendations are source claims, not proof of a working integration. This check used the saved guide text, current project files, upstream repositories and the local Claude CLI.

| Resource | Outcome |
|---|---|
| [calibrate](https://github.com/robonuggets/calibrate), `c9bbde8b5f5822fb63d71db08cea7ec3a6bddc4e` | Installed in `skills/codex`, `skills/claude`, `.agents/skills` and `.claude/skills` with MIT license and provenance. It reviews current-session corrections and proposes changes; existing user/runtime rules govern permissions and memory. Its behavior was inspected but not invoked in a fresh agent session. |
| [ASD-STE100 skill](https://github.com/danyuchn/asd-ste100-skill), `8da6b6340aa22faf46fd07db8efbdea010cd38d9` | Installed in the same four project locations with license, references and linter. The linter accepted `The system may have failed.` with no violations. This tool does not include the official dictionary and cannot establish full standard compliance. |
| [Ribbon](https://github.com/robonuggets/ribbon), `eecb8f9e384e8ae0ebbafb85f5c6490e8d561f72` | Inspected UI hook and cloned at `C:/Users/Joshu/dev/ai-os-projects/ribbon-20261029`. `claude plugin test` with Claude Code 2.1.309 passed 7 tests. It is Claude-specific; it displays usage and estimated cache cost, not an authoritative bill. Not installed: Claude's `--marketplace` option adds a marketplace in user settings even with project scope; the requested project-scoped route has not been established. No UI session verification. |
| Jev through OpenRouter | Guide says a separate API account/key is required. No verified upstream exact identity, current cost, credentials or local test. No routing, billing or model calls enabled. |
| RUBRIC, Recos, Editor, Generations, Carousels, `/quick`, `/search-connectors` | Described as community resources; payloads were not in supplied PDFs. No access or usable implementation established. |
| `bro`, `wait-what`, `no-ai-slop`, `i-have-adhd`, `be-ambitious` | Already installed project-scoped in both runtime trees during initial ingest. The first four are on-demand communication tools; the last supports outcome and method planning. Fresh-session discovery remains untested. |
| Canvas UI, orbs, beam, metal | Canvas UI already routes through the design library. These are components for a specific target build, not workspace-wide integrations. License, accessibility and performance must be checked in the target before use. |
| Scheduled cache pings and correction-learning automation | Not enabled. Existing schedulers and knowledge systems already exist. Guide gives no authorization to run a recurring paid request or silently promote memories. |

All installed skill files were fetched at the pinned commits and copied without changing upstream instructions. Project and user instructions take precedence over conflicting upstream suggestions. No credentials, recurring jobs, billing or user-wide marketplace settings were changed by this evaluation.
