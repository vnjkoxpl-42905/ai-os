---
name: tailwind-prose-classes-are-inert
description: "LSAT U's prose classes emitted nothing for months; the plugin is now registered with the app's own token palette in both keys."
metadata: 
  node_type: memory
  type: project
  originSessionId: 9a2e34c3-6cc3-41c2-b75a-b0b02f16c2dc
  modified: 2026-09-09T21:55:09.052Z
---

`@tailwindcss/typography` was in `package.json` but not in `tailwind.config.ts`'s `plugins`
array. Measured 2026-09-09: zero `.prose` rules in the served stylesheets, and a rendered
`<h2>` inside `.prose` computed to the inherited body colour at 16px. Thirteen live
surfaces were styling markdown with classes that did not exist.

Registered 2026-09-09 (PR #108). Registering alone would have made things worse: the app
is dark at `:root` and flips to light with a `.light` class, so `darkMode: ["class"]`
means the `dark:` variant almost never fires, and the call sites written as
`dark:prose-invert` would have landed on Tailwind's gray-700 body text on a near-black
ground.

**Why:** both the `DEFAULT` and `invert` typography keys now resolve from `--foreground`,
`--muted-foreground`, `--border` and `--muted`. Prose is correct in either theme whether
or not a call site asks for `prose-invert`.

**How to apply:** never restore Tailwind's own gray palette to either key — that
reintroduces the dark-mode failure. `.classroom-prose` is separate and stays hand-written.
Teacher-side markdown outside `.classroom-root` uses `TEACHER_MARKDOWN_CLASS` in
`src/components/teacher/teacherMarkdown.ts`, which is explicit arbitrary variants.

Related: [[classroom-prose-loses-list-markers]], [[shebang-plus-crlf-breaks-vitest]]
