---
name: setup-pre-commit
description: Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to add pre-commit hooks, set up Husky, configure lint-staged, or add commit-time formatting/typechecking/testing.
---

# Setup Pre-Commit Hooks

## What This Sets Up

- **Husky** pre-commit hook
- **lint-staged** running Prettier on all staged files
- **Prettier** config (if missing)
- **typecheck** and **test** scripts in the pre-commit hook

## Steps

### 1. Preserve existing configuration and detect package manager

Record dirty/staged baseline. Inspect package scripts, `core.hooksPath`, `.husky/`, current pre-commit hook and existing lint-staged/Prettier configuration. Merge required checks without overwriting existing commands, secrets or unrelated entries; reuse installed versions and repo conventions. Back up any configuration changed. Never run `husky init` blindly over an existing setup.

Check for `package-lock.json` (npm), `pnpm-lock.yaml` (pnpm), `yarn.lock` (yarn), `bun.lockb` (bun). Use whichever is present. Default to npm if unclear.

### 2. Install dependencies

Install as devDependencies:

```
husky lint-staged prettier
```

### 3. Initialize Husky

```bash
npx husky init
```

Use initialization only for a missing Husky setup after checking its installed version. Preserve any existing `prepare` behavior when adding Husky; do not replace it unconditionally.

### 4. Create `.husky/pre-commit`

Merge these checks into the existing hook, preserving its behavior. For a new Husky v9+ file this is an example (older versions may require their existing bootstrap):

```
npx lint-staged
npm run typecheck
npm run test
```

**Adapt**: Replace `npm` with detected package manager. If repo has no `typecheck` or `test` script in package.json, omit those lines and tell the user.

### 5. Create `.lintstagedrc`

```json
{
  "*": "prettier --ignore-unknown --write"
}
```

### 6. Create `.prettierrc` (if missing)

Only create if no Prettier config exists. Use these defaults:

```json
{
  "useTabs": false,
  "tabWidth": 2,
  "printWidth": 80,
  "singleQuote": false,
  "trailingComma": "es5",
  "semi": true,
  "arrowParens": "always"
}
```

### 7. Verify

- [ ] `.husky/pre-commit` exists and is executable
- [ ] `.lintstagedrc` exists
- [ ] `prepare` script in package.json is `"husky"`
- [ ] `prettier` config exists
- [ ] Run the hook/checks on an isolated fixture or only scoped staged paths; lint-staged may modify files/stash the index, so preserve unrelated staged work

### 8. Commit

Commit only when authorized by the current task. Stage only the reviewed hook/config/package/lockfile paths owned by this setup and inspect the staged diff, preserving the prior index. Suggested message: `Add pre-commit hooks (husky + lint-staged + prettier)`. Otherwise leave changes for review.

This will run through the new pre-commit hooks: a good smoke test that everything works.

## Notes

- Husky v9+ doesn't need shebangs in hook files
- `prettier --ignore-unknown` skips files Prettier can't parse (images, etc.)
- The pre-commit runs lint-staged first (fast, staged-only), then full typecheck and tests
