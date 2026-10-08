---
type: source
subject: "GitHub source repos/karpathy/llm-council/frontend/eslint.config.js"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm-council/frontend/eslint.config.js]
semantic-status: complete-named-text-read
---

# repos/karpathy/llm-council/frontend/eslint.config.js

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/llm-council/frontend/eslint.config.js), SHA-256 `da0cbf3213f2994741024e2aa5165d017e0345f389dcd2f8a0db97fee7289d1b`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
import js from '@eslint/js' import globals from 'globals' import reactHooks from 'eslint-plugin-react-hooks' import reactRefresh from
```

Eight council instructions/frontend sources fully read. CLAUDE technical notes describe anonymized review, all raw outputs inspectable and parsed rankings below for validation, ephemeral metadata and continued partial failures; instructions are source evidence not governing our workspace. Claims prevents bias are intended design, not measured guarantee; streaming future item outdated versus present implementation. Vite ESLint/HTML/logo React SVG scaffolds are thirdparty template assets, not persona knowledge. API fetch checks HTTP status but SSE splits each received chunk without persistent buffer or streaming UTF8 decoder, so arbitrary packet boundaries can lose events. App optimistic user+assistant messages progresses last message stages, metadata UI only, logs errors; conversation switches can receive stale loads/events and failed stream may leave loading. Transparent intermediate evidence useful design, no live test or execution.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
import js from '@eslint/js'
import globals from 'globals'
import reactHooks from 'eslint-plugin-react-hooks'
import reactRefresh from 'eslint-plugin-react-refresh'
import { defineConfig, globalIgnores } from 'eslint/config'

export default defineConfig([
  globalIgnores(['dist']),
  {
    files: ['**/*.{js,jsx}'],
    extends: [
      js.configs.recommended,
      reactHooks.configs.flat.recommended,
      reactRefresh.configs.vite,
    ],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
      parserOptions: {
        ecmaVersion: 'latest',
        ecmaFeatures: { jsx: true },
        sourceType: 'module',
      },
    },
    rules: {
      'no-unused-vars': ['error', { varsIgnorePattern: '^[A-Z_]' }],
    },
  },
])

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
