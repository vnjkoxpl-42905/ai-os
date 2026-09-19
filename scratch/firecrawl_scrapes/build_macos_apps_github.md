[Skip to content](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps) to refresh your session.Dismiss alert

{{ message }}

[openai](https://github.com/openai)/ **[plugins](https://github.com/openai/plugins)** Public

- [Notifications](https://github.com/login?return_to=%2Fopenai%2Fplugins) You must be signed in to change notification settings
- [Fork\\
902](https://github.com/login?return_to=%2Fopenai%2Fplugins)
- [Star\\
6.9k](https://github.com/login?return_to=%2Fopenai%2Fplugins)


## Collapse file tree

## Files

main

Search this repository(forward slash)` forward slash/`

/

# build-macos-apps

/

Copy path

## Directory actions

## More options

More options

## Directory actions

## More options

More options

## Latest commit

[![jameswt-oai](https://avatars.githubusercontent.com/u/247462917?v=4&size=40)](https://github.com/jameswt-oai)[jameswt-oai](https://github.com/openai/plugins/commits?author=jameswt-oai)

[\[codex\] Reapply plugin categories and bump all versions (](https://github.com/openai/plugins/commit/cd0fccd4ed62dded584c16246685b232d7bfe7f6) [#321](https://github.com/openai/plugins/pull/321) [)](https://github.com/openai/plugins/commit/cd0fccd4ed62dded584c16246685b232d7bfe7f6)

Open commit details

3 months agoJun 8, 2026

[cd0fccd](https://github.com/openai/plugins/commit/cd0fccd4ed62dded584c16246685b232d7bfe7f6) · 3 months agoJun 8, 2026

## History

[History](https://github.com/openai/plugins/commits/main/plugins/build-macos-apps)

Open commit details

[View commit history for this file.](https://github.com/openai/plugins/commits/main/plugins/build-macos-apps) History

/

# build-macos-apps

/

Copy path

Top

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| ### parent directory<br> [..](https://github.com/openai/plugins/tree/main/plugins) |
| [.codex-plugin](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps/.codex-plugin ".codex-plugin") | [.codex-plugin](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps/.codex-plugin ".codex-plugin") | [\[codex\] Reapply plugin categories and bump all versions (](https://github.com/openai/plugins/commit/cd0fccd4ed62dded584c16246685b232d7bfe7f6 "[codex] Reapply plugin categories and bump all versions (#321)  Reapply the reviewed plugin category update from #303 now that the temporary wait period documented in #319 has ended.  Update marketplace and plugin manifest categories to the canonical taxonomy. Patch-bump all 172 catalog plugin versions so the ingest batch can publish fresh releases and refresh category metadata for every plugin record in the database, including plugins whose checked-in category did not change.  Each version is exactly one patch above its version on current `main`. Base44 preserves the repository’s established prerelease convention (`1.0.1-beta.1` to `1.0.2-beta.1`). Changes merged after the temporary revert, including the latest Google Drive release, are preserved.  Validation: - Verified all 172 catalog manifests are exactly one patch above current `main`. - Verified categories use the approved taxonomy and marketplace/manifest values agree. - Verified no manifest fields other than `version` and the reviewed `interface.category` changes were modified. - Ran `cloud-plugin-admin catalog validate .agents/plugins/marketplace.json` (`valid=172`, `invalid=0`). - Parsed the marketplace and every plugin manifest as JSON.") [#321](https://github.com/openai/plugins/pull/321) [)](https://github.com/openai/plugins/commit/cd0fccd4ed62dded584c16246685b232d7bfe7f6 "[codex] Reapply plugin categories and bump all versions (#321)  Reapply the reviewed plugin category update from #303 now that the temporary wait period documented in #319 has ended.  Update marketplace and plugin manifest categories to the canonical taxonomy. Patch-bump all 172 catalog plugin versions so the ingest batch can publish fresh releases and refresh category metadata for every plugin record in the database, including plugins whose checked-in category did not change.  Each version is exactly one patch above its version on current `main`. Base44 preserves the repository’s established prerelease convention (`1.0.1-beta.1` to `1.0.2-beta.1`). Changes merged after the temporary revert, including the latest Google Drive release, are preserved.  Validation: - Verified all 172 catalog manifests are exactly one patch above current `main`. - Verified categories use the approved taxonomy and marketplace/manifest values agree. - Verified no manifest fields other than `version` and the reviewed `interface.category` changes were modified. - Ran `cloud-plugin-admin catalog validate .agents/plugins/marketplace.json` (`valid=172`, `invalid=0`). - Parsed the marketplace and every plugin manifest as JSON.") | 3 months agoJun 8, 2026 |
| [agents](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps/agents "agents") | [agents](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps/agents "agents") | [Trim Build macOS plugin prompts (](https://github.com/openai/plugins/commit/2464aee42116fc51482c84ceb053369380a8b5ce "Trim Build macOS plugin prompts (#263)  ## Summary - normalize the Build macOS Apps plugin starter prompt to the current plugin prompt-array contract - shorten the plugin-level prompt and all macOS skill trigger descriptions so discovery metadata stays compact - defer detailed sidebar/split-view and window modifier examples into references while keeping skill entrypoints focused  ## Why `build-macos-apps` could not be scored by `plugin-eval` while its manifest starter prompt was still a string. After that prompt shape was normalized, the static report showed both trigger and invocation budget failures driven by long skill trigger metadata and detailed examples in always-loaded `SKILL.md` entrypoints.  This PR keeps the same macOS skill inventory and routing terms, but moves detailed examples out of the entrypoint path where they can be loaded only when the task needs them.  ## Impact Build macOS Apps keeps its existing workflows while its starter prompt metadata matches the current plugin contract, trigger descriptions are smaller, and high-detail SwiftUI/window examples live in references instead of always-loaded skill bodies.  ## plugin-eval report progression The same local report command was used throughout:  ```sh cd plugins/plugin-eval node ./scripts/plugin-eval.js analyze ../build-macos-apps --format markdown ```  Before the manifest prompt was normalized, `plugin-eval` could not emit a scored report because the string-shaped `defaultPrompt` hit:  ```text ((intermediate value) || []).join is not a function ```  | State | Score | Risk | Checks | Trigger | Invoke | Deferred | Active | Total | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | First scored report after starter-prompt shape normalization | 67 / D | high | 2 fail, 1 warn, 2 info | 899 | 15529 | 7722 | 16428 | 24150 | | After compacting all Build macOS skill descriptions | 77 / C | high | 1 fail, 2 warn, 2 info | 464 | 15092 | 7722 | 15556 | 23278 | | Final after deferring sidebar/split and window API examples | 86 / B | medium | 0 fail, 3 warn, 2 info | 464 | 14291 | 8507 | 14755 | 23262 |  The final report clears the trigger and invocation budget failures. Remaining warnings are static budget warnings for trigger, invoke, and deferred text.  ## Validation - `node ./scripts/plugin-eval.js analyze ../build-macos-apps --format markdown` - `git diff --check`") [#263](https://github.com/openai/plugins/pull/263) [)](https://github.com/openai/plugins/commit/2464aee42116fc51482c84ceb053369380a8b5ce "Trim Build macOS plugin prompts (#263)  ## Summary - normalize the Build macOS Apps plugin starter prompt to the current plugin prompt-array contract - shorten the plugin-level prompt and all macOS skill trigger descriptions so discovery metadata stays compact - defer detailed sidebar/split-view and window modifier examples into references while keeping skill entrypoints focused  ## Why `build-macos-apps` could not be scored by `plugin-eval` while its manifest starter prompt was still a string. After that prompt shape was normalized, the static report showed both trigger and invocation budget failures driven by long skill trigger metadata and detailed examples in always-loaded `SKILL.md` entrypoints.  This PR keeps the same macOS skill inventory and routing terms, but moves detailed examples out of the entrypoint path where they can be loaded only when the task needs them.  ## Impact Build macOS Apps keeps its existing workflows while its starter prompt metadata matches the current plugin contract, trigger descriptions are smaller, and high-detail SwiftUI/window examples live in references instead of always-loaded skill bodies.  ## plugin-eval report progression The same local report command was used throughout:  ```sh cd plugins/plugin-eval node ./scripts/plugin-eval.js analyze ../build-macos-apps --format markdown ```  Before the manifest prompt was normalized, `plugin-eval` could not emit a scored report because the string-shaped `defaultPrompt` hit:  ```text ((intermediate value) || []).join is not a function ```  | State | Score | Risk | Checks | Trigger | Invoke | Deferred | Active | Total | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | First scored report after starter-prompt shape normalization | 67 / D | high | 2 fail, 1 warn, 2 info | 899 | 15529 | 7722 | 16428 | 24150 | | After compacting all Build macOS skill descriptions | 77 / C | high | 1 fail, 2 warn, 2 info | 464 | 15092 | 7722 | 15556 | 23278 | | Final after deferring sidebar/split and window API examples | 86 / B | medium | 0 fail, 3 warn, 2 info | 464 | 14291 | 8507 | 14755 | 23262 |  The final report clears the trigger and invocation budget failures. Remaining warnings are static budget warnings for trigger, invoke, and deferred text.  ## Validation - `node ./scripts/plugin-eval.js analyze ../build-macos-apps --format markdown` - `git diff --check`") | 4 months agoMay 27, 2026 |
| [assets](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps/assets "assets") | [assets](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps/assets "assets") | [Add build macOS apps plugin (](https://github.com/openai/plugins/commit/c989653d89097f901adbead90921fcb82b907fad "Add build macOS apps plugin (#130)  ## Summary - add `build-macos-apps` as a new public Codex plugin for macOS app development workflows - include macOS-focused skills for build/run/debug loops, SwiftUI/AppKit guidance, Liquid Glass, window management, telemetry, signing, packaging, SwiftPM, and test triage - add command entrypoints, assets, plugin metadata, marketplace registration, and root README discovery - document maintainable new-app scaffolding guidance so non-trivial SwiftUI/macOS apps start with separate App, Views, Models, Stores, Services, and Support files  ## Notes - keeps the plugin skills-first at the plugin level, matching the public `build-ios-apps` shape - uses public OpenAI metadata, policy URLs, MIT licensing, and Coding category conventions - preserves the `script/build_and_run.sh` and `.codex/environments/environment.toml` run-button guidance while keeping it separate from app source  ## Validation - `git diff --check` and `git diff --cached --check` - JSON parsing for `plugins/build-macos-apps/.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json` - alignment checks against `plugins/build-ios-apps/.codex-plugin/plugin.json` - skill frontmatter, asset path, marketplace ordering, and metadata scrub checks - grep/diff review for scaffold guidance consistency across `swiftui-patterns`, `view-refactor`, `build-run-debug`, and directly referenced component docs") [#130](https://github.com/openai/plugins/pull/130) [)](https://github.com/openai/plugins/commit/c989653d89097f901adbead90921fcb82b907fad "Add build macOS apps plugin (#130)  ## Summary - add `build-macos-apps` as a new public Codex plugin for macOS app development workflows - include macOS-focused skills for build/run/debug loops, SwiftUI/AppKit guidance, Liquid Glass, window management, telemetry, signing, packaging, SwiftPM, and test triage - add command entrypoints, assets, plugin metadata, marketplace registration, and root README discovery - document maintainable new-app scaffolding guidance so non-trivial SwiftUI/macOS apps start with separate App, Views, Models, Stores, Services, and Support files  ## Notes - keeps the plugin skills-first at the plugin level, matching the public `build-ios-apps` shape - uses public OpenAI metadata, policy URLs, MIT licensing, and Coding category conventions - preserves the `script/build_and_run.sh` and `.codex/environments/environment.toml` run-button guidance while keeping it separate from app source  ## Validation - `git diff --check` and `git diff --cached --check` - JSON parsing for `plugins/build-macos-apps/.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json` - alignment checks against `plugins/build-ios-apps/.codex-plugin/plugin.json` - skill frontmatter, asset path, marketplace ordering, and metadata scrub checks - grep/diff review for scaffold guidance consistency across `swiftui-patterns`, `view-refactor`, `build-run-debug`, and directly referenced component docs") | 5 months agoApr 8, 2026 |
| [commands](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps/commands "commands") | [commands](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps/commands "commands") | [Add build macOS apps plugin (](https://github.com/openai/plugins/commit/c989653d89097f901adbead90921fcb82b907fad "Add build macOS apps plugin (#130)  ## Summary - add `build-macos-apps` as a new public Codex plugin for macOS app development workflows - include macOS-focused skills for build/run/debug loops, SwiftUI/AppKit guidance, Liquid Glass, window management, telemetry, signing, packaging, SwiftPM, and test triage - add command entrypoints, assets, plugin metadata, marketplace registration, and root README discovery - document maintainable new-app scaffolding guidance so non-trivial SwiftUI/macOS apps start with separate App, Views, Models, Stores, Services, and Support files  ## Notes - keeps the plugin skills-first at the plugin level, matching the public `build-ios-apps` shape - uses public OpenAI metadata, policy URLs, MIT licensing, and Coding category conventions - preserves the `script/build_and_run.sh` and `.codex/environments/environment.toml` run-button guidance while keeping it separate from app source  ## Validation - `git diff --check` and `git diff --cached --check` - JSON parsing for `plugins/build-macos-apps/.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json` - alignment checks against `plugins/build-ios-apps/.codex-plugin/plugin.json` - skill frontmatter, asset path, marketplace ordering, and metadata scrub checks - grep/diff review for scaffold guidance consistency across `swiftui-patterns`, `view-refactor`, `build-run-debug`, and directly referenced component docs") [#130](https://github.com/openai/plugins/pull/130) [)](https://github.com/openai/plugins/commit/c989653d89097f901adbead90921fcb82b907fad "Add build macOS apps plugin (#130)  ## Summary - add `build-macos-apps` as a new public Codex plugin for macOS app development workflows - include macOS-focused skills for build/run/debug loops, SwiftUI/AppKit guidance, Liquid Glass, window management, telemetry, signing, packaging, SwiftPM, and test triage - add command entrypoints, assets, plugin metadata, marketplace registration, and root README discovery - document maintainable new-app scaffolding guidance so non-trivial SwiftUI/macOS apps start with separate App, Views, Models, Stores, Services, and Support files  ## Notes - keeps the plugin skills-first at the plugin level, matching the public `build-ios-apps` shape - uses public OpenAI metadata, policy URLs, MIT licensing, and Coding category conventions - preserves the `script/build_and_run.sh` and `.codex/environments/environment.toml` run-button guidance while keeping it separate from app source  ## Validation - `git diff --check` and `git diff --cached --check` - JSON parsing for `plugins/build-macos-apps/.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json` - alignment checks against `plugins/build-ios-apps/.codex-plugin/plugin.json` - skill frontmatter, asset path, marketplace ordering, and metadata scrub checks - grep/diff review for scaffold guidance consistency across `swiftui-patterns`, `view-refactor`, `build-run-debug`, and directly referenced component docs") | 5 months agoApr 8, 2026 |
| [skills](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps/skills "skills") | [skills](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps/skills "skills") | [Trim Build macOS plugin prompts (](https://github.com/openai/plugins/commit/2464aee42116fc51482c84ceb053369380a8b5ce "Trim Build macOS plugin prompts (#263)  ## Summary - normalize the Build macOS Apps plugin starter prompt to the current plugin prompt-array contract - shorten the plugin-level prompt and all macOS skill trigger descriptions so discovery metadata stays compact - defer detailed sidebar/split-view and window modifier examples into references while keeping skill entrypoints focused  ## Why `build-macos-apps` could not be scored by `plugin-eval` while its manifest starter prompt was still a string. After that prompt shape was normalized, the static report showed both trigger and invocation budget failures driven by long skill trigger metadata and detailed examples in always-loaded `SKILL.md` entrypoints.  This PR keeps the same macOS skill inventory and routing terms, but moves detailed examples out of the entrypoint path where they can be loaded only when the task needs them.  ## Impact Build macOS Apps keeps its existing workflows while its starter prompt metadata matches the current plugin contract, trigger descriptions are smaller, and high-detail SwiftUI/window examples live in references instead of always-loaded skill bodies.  ## plugin-eval report progression The same local report command was used throughout:  ```sh cd plugins/plugin-eval node ./scripts/plugin-eval.js analyze ../build-macos-apps --format markdown ```  Before the manifest prompt was normalized, `plugin-eval` could not emit a scored report because the string-shaped `defaultPrompt` hit:  ```text ((intermediate value) || []).join is not a function ```  | State | Score | Risk | Checks | Trigger | Invoke | Deferred | Active | Total | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | First scored report after starter-prompt shape normalization | 67 / D | high | 2 fail, 1 warn, 2 info | 899 | 15529 | 7722 | 16428 | 24150 | | After compacting all Build macOS skill descriptions | 77 / C | high | 1 fail, 2 warn, 2 info | 464 | 15092 | 7722 | 15556 | 23278 | | Final after deferring sidebar/split and window API examples | 86 / B | medium | 0 fail, 3 warn, 2 info | 464 | 14291 | 8507 | 14755 | 23262 |  The final report clears the trigger and invocation budget failures. Remaining warnings are static budget warnings for trigger, invoke, and deferred text.  ## Validation - `node ./scripts/plugin-eval.js analyze ../build-macos-apps --format markdown` - `git diff --check`") [#263](https://github.com/openai/plugins/pull/263) [)](https://github.com/openai/plugins/commit/2464aee42116fc51482c84ceb053369380a8b5ce "Trim Build macOS plugin prompts (#263)  ## Summary - normalize the Build macOS Apps plugin starter prompt to the current plugin prompt-array contract - shorten the plugin-level prompt and all macOS skill trigger descriptions so discovery metadata stays compact - defer detailed sidebar/split-view and window modifier examples into references while keeping skill entrypoints focused  ## Why `build-macos-apps` could not be scored by `plugin-eval` while its manifest starter prompt was still a string. After that prompt shape was normalized, the static report showed both trigger and invocation budget failures driven by long skill trigger metadata and detailed examples in always-loaded `SKILL.md` entrypoints.  This PR keeps the same macOS skill inventory and routing terms, but moves detailed examples out of the entrypoint path where they can be loaded only when the task needs them.  ## Impact Build macOS Apps keeps its existing workflows while its starter prompt metadata matches the current plugin contract, trigger descriptions are smaller, and high-detail SwiftUI/window examples live in references instead of always-loaded skill bodies.  ## plugin-eval report progression The same local report command was used throughout:  ```sh cd plugins/plugin-eval node ./scripts/plugin-eval.js analyze ../build-macos-apps --format markdown ```  Before the manifest prompt was normalized, `plugin-eval` could not emit a scored report because the string-shaped `defaultPrompt` hit:  ```text ((intermediate value) || []).join is not a function ```  | State | Score | Risk | Checks | Trigger | Invoke | Deferred | Active | Total | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | First scored report after starter-prompt shape normalization | 67 / D | high | 2 fail, 1 warn, 2 info | 899 | 15529 | 7722 | 16428 | 24150 | | After compacting all Build macOS skill descriptions | 77 / C | high | 1 fail, 2 warn, 2 info | 464 | 15092 | 7722 | 15556 | 23278 | | Final after deferring sidebar/split and window API examples | 86 / B | medium | 0 fail, 3 warn, 2 info | 464 | 14291 | 8507 | 14755 | 23262 |  The final report clears the trigger and invocation budget failures. Remaining warnings are static budget warnings for trigger, invoke, and deferred text.  ## Validation - `node ./scripts/plugin-eval.js analyze ../build-macos-apps --format markdown` - `git diff --check`") | 4 months agoMay 27, 2026 |
| [README.md](https://github.com/openai/plugins/blob/main/plugins/build-macos-apps/README.md "README.md") | [README.md](https://github.com/openai/plugins/blob/main/plugins/build-macos-apps/README.md "README.md") | [Add build macOS apps plugin (](https://github.com/openai/plugins/commit/c989653d89097f901adbead90921fcb82b907fad "Add build macOS apps plugin (#130)  ## Summary - add `build-macos-apps` as a new public Codex plugin for macOS app development workflows - include macOS-focused skills for build/run/debug loops, SwiftUI/AppKit guidance, Liquid Glass, window management, telemetry, signing, packaging, SwiftPM, and test triage - add command entrypoints, assets, plugin metadata, marketplace registration, and root README discovery - document maintainable new-app scaffolding guidance so non-trivial SwiftUI/macOS apps start with separate App, Views, Models, Stores, Services, and Support files  ## Notes - keeps the plugin skills-first at the plugin level, matching the public `build-ios-apps` shape - uses public OpenAI metadata, policy URLs, MIT licensing, and Coding category conventions - preserves the `script/build_and_run.sh` and `.codex/environments/environment.toml` run-button guidance while keeping it separate from app source  ## Validation - `git diff --check` and `git diff --cached --check` - JSON parsing for `plugins/build-macos-apps/.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json` - alignment checks against `plugins/build-ios-apps/.codex-plugin/plugin.json` - skill frontmatter, asset path, marketplace ordering, and metadata scrub checks - grep/diff review for scaffold guidance consistency across `swiftui-patterns`, `view-refactor`, `build-run-debug`, and directly referenced component docs") [#130](https://github.com/openai/plugins/pull/130) [)](https://github.com/openai/plugins/commit/c989653d89097f901adbead90921fcb82b907fad "Add build macOS apps plugin (#130)  ## Summary - add `build-macos-apps` as a new public Codex plugin for macOS app development workflows - include macOS-focused skills for build/run/debug loops, SwiftUI/AppKit guidance, Liquid Glass, window management, telemetry, signing, packaging, SwiftPM, and test triage - add command entrypoints, assets, plugin metadata, marketplace registration, and root README discovery - document maintainable new-app scaffolding guidance so non-trivial SwiftUI/macOS apps start with separate App, Views, Models, Stores, Services, and Support files  ## Notes - keeps the plugin skills-first at the plugin level, matching the public `build-ios-apps` shape - uses public OpenAI metadata, policy URLs, MIT licensing, and Coding category conventions - preserves the `script/build_and_run.sh` and `.codex/environments/environment.toml` run-button guidance while keeping it separate from app source  ## Validation - `git diff --check` and `git diff --cached --check` - JSON parsing for `plugins/build-macos-apps/.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json` - alignment checks against `plugins/build-ios-apps/.codex-plugin/plugin.json` - skill frontmatter, asset path, marketplace ordering, and metadata scrub checks - grep/diff review for scaffold guidance consistency across `swiftui-patterns`, `view-refactor`, `build-run-debug`, and directly referenced component docs") | 5 months agoApr 8, 2026 |
| View all files |

## [README.md](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps\#readme)

Outline

# Build macOS Apps Plugin

[Permalink: Build macOS Apps Plugin](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps#build-macos-apps-plugin)

This plugin packages macOS-first development workflows in `plugins/build-macos-apps`.

It currently includes these skills:

- `build-run-debug`
- `test-triage`
- `signing-entitlements`
- `swiftpm-macos`
- `packaging-notarization`
- `swiftui-patterns`
- `liquid-glass`
- `window-management`
- `appkit-interop`
- `view-refactor`
- `telemetry`

## What It Covers

[Permalink: What It Covers](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps#what-it-covers)

- discovering local Xcode workspaces, projects, and Swift packages
- building and running macOS apps with shell-first desktop workflows
- creating one project-local `script/build_and_run.sh` entrypoint and wiring `.codex/environments/environment.toml` so the Codex app Run button works
- implementing native macOS SwiftUI scenes, menus, settings, toolbars, and multiwindow flows
- adopting modern macOS Liquid Glass and design-system guidance with standard SwiftUI structures, toolbars, search, controls, and custom glass surfaces
- tailoring SwiftUI windows with title/toolbar styling, material-backed container backgrounds, minimize/restoration behavior, default and ideal placement, borderless window style, and launch behavior
- bridging into AppKit for representables, responder-chain behavior, panels, and other desktop-only needs
- refactoring large macOS view files toward stable scene, selection, and command structure
- adding lightweight `Logger` / `os.Logger` instrumentation for windows, sidebars, menu commands, and menu bar actions
- reading and verifying runtime events with Console, `log stream`, and process logs
- triaging failing unit, integration, and UI-hosted macOS tests
- debugging launch failures, crashes, linker problems, and runtime regressions
- inspecting signing identities, entitlements, hardened runtime, and Gatekeeper issues
- preparing packaging and notarization workflows for distribution

## What It Does Not Cover

[Permalink: What It Does Not Cover](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps#what-it-does-not-cover)

- iOS, watchOS, or tvOS simulator control
- desktop UI automation
- App Store Connect release management
- pixel-perfect visual design or design-system generation

## Plugin Structure

[Permalink: Plugin Structure](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps#plugin-structure)

The plugin lives at:

- `plugins/build-macos-apps/`

with this shape:

- `.codex-plugin/plugin.json`
  - required plugin manifest
  - defines plugin metadata and points Codex at the plugin contents
- `agents/`
  - plugin-level agent metadata
  - currently includes `agents/openai.yaml` for the OpenAI surface
- `commands/`
  - reusable workflow entrypoints for common macOS development tasks
- `skills/`
  - the actual skill payload
  - each skill keeps the normal skill structure (`SKILL.md`, optional
    `agents/`, `references/`, `assets/`, `scripts/`)

## Notes

[Permalink: Notes](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps#notes)

This plugin is currently skills-first at the plugin level. It does not ship a
plugin-local `.mcp.json`, matching the public `plugins/build-ios-apps` shape.

The default posture is shell-first. Unlike the iOS build plugin, this plugin
does not assume simulator tooling or touch-driven UI inspection for its main
workflows. The core execution model leans on `xcodebuild`, `swift`, `open`,
`lldb`, `codesign`, `spctl`, `plutil`, and `log stream`, with a compact desktop
UI layer for native SwiftUI scene design, AppKit interop, and macOS-specific
refactoring.

You can’t perform that action at this time.