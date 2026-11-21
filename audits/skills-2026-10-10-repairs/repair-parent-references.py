"""Repair supporting examples for the parent-owned MCP scaffolds."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).parent
changes = {
    'build-mcp-app/references/widget-templates.md': [
        ('      li.innerHTML = `<div>${it.label}</div><div class="sub">${it.sub ?? ""}</div>`;',
         '      const label = document.createElement("div");\n'
         '      label.textContent = it.label ?? "";\n'
         '      const sub = document.createElement("div");\n'
         '      sub.className = "sub";\n'
         '      sub.textContent = it.sub ?? "";\n'
         '      li.append(label, sub);'),
    ],
    'build-mcpb/references/local-security.md': [
        ('import { resolve, relative, isAbsolute } from "node:path";\n\n'
         'function safeJoin(root: string, userPath: string): string {\n'
         '  const full = resolve(root, userPath);\n'
         '  const rel = relative(root, full);\n'
         '  if (rel.startsWith("..") || isAbsolute(rel)) {',
         'import { resolve, relative, isAbsolute, sep } from "node:path";\n'
         'import { realpath } from "node:fs/promises";\n\n'
         'async function safeJoin(root: string, userPath: string): Promise<string> {\n'
         '  if (isAbsolute(userPath)) throw new Error("Use a relative path");\n'
         '  const base = await realpath(root);\n'
         '  const full = await realpath(resolve(base, userPath));\n'
         '  const rel = relative(base, full);\n'
         '  if (rel === ".." || rel.startsWith(".." + sep) || isAbsolute(rel)) {'),
        ('`resolve` normalizes `..`, symlink segments, etc. `relative` tells you if the result left the root. Don\'t just `String.includes("..")` — that misses encoded and symlink-based escapes.',
         '`resolve` normalizes lexical segments; it does not resolve symlinks. `realpath` resolves existing symlink/junction targets before containment is checked. '
         'Await `safeJoin` before reading. This example accepts existing targets only; validate a real parent separately for new writes. '
         'Concurrent filesystem replacement still requires handle-based protections or OS isolation.'),
        ('import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";\n\nconst server',
         'import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";\n'
         'import { fileURLToPath } from "node:url";\n\nconst server'),
        ('allowedRoots = roots.map(r => new URL(r.uri).pathname);',
         'allowedRoots = roots.map(r => fileURLToPath(r.uri));'),
    ],
}
records = []
for runtime in ('claude', 'codex', 'gemini'):
    for relative, replacements in changes.items():
        path = ROOT / 'skills' / runtime / relative
        if not path.exists():
            continue
        original = path.read_bytes()
        text = original.decode('utf-8').replace('\r\n', '\n')
        for old, new in replacements:
            if old not in text:
                raise RuntimeError(f'Inspect missing anchor: {path}: {old[:50]}')
            text = text.replace(old, new, 1)
        backup = OUT / 'backups' / 'parent' / path.relative_to(ROOT)
        backup.parent.mkdir(parents=True, exist_ok=True)
        if backup.exists():
            raise RuntimeError(f'Backup exists: {backup}')
        backup.write_bytes(original)
        if path.read_bytes() != original:
            raise RuntimeError(f'Concurrent edit: {path}')
        path.write_text(text, encoding='utf-8', newline='\n')
        records.append({'path': str(path), 'before_sha256': hashlib.sha256(original).hexdigest(),
                        'after_sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'backup': str(backup)})
(OUT / 'parent-reference-repairs.json').write_text(json.dumps(records, indent=2), encoding='utf-8')
print(f'Repaired {len(records)} existing supporting references.')
