# Reading Center build: lessons from review

Gemini reads this file **before starting every chunk**. Claude appends a lesson after each review that
found a mistake. Each lesson is a rule to follow from now on. Newest at the bottom. Never delete lines.

1. Never stash, restore or switch branches in the shared checkout `C:\Users\Joshu\dev\ai-os-projects\lsatu`. Work only in `lsatu-reading-center`.
2. When a plan-supplied test fails, stop and hand off with the exact failure (as you did in chunk B). Do not edit the test or the code to force a pass. The plan can be wrong; the supervisor decides.
3. Before handing off, run `git status --short`; it must be empty. Commit any work in progress with a `WIP:` prefix rather than leaving it uncommitted.
4. Reading font, size and line spacing apply ONLY to passage text. `ReaderSurface` exposes them as CSS variables; put `style={READING_TEXT_STYLE}` (exported from `components/ReaderSurface.tsx`) on the element that holds the passage words. Never on bars, buttons or dialogs.
