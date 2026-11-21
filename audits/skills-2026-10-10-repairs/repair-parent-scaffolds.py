"""Apply the two parent-owned scaffold repairs without replacing unrelated text."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).parent
REPLACEMENTS = {
    'build-mcp-app': [
        ('      li.innerHTML = `<div>${c.name}</div><div class="sub">${c.email}</div>`;',
         '      const name = document.createElement("div");\n'
         '      name.textContent = c.name ?? "";\n'
         '      const email = document.createElement("div");\n'
         '      email.className = "sub";\n'
         '      email.textContent = c.email ?? "";\n'
         '      li.append(name, email);'),
        ('**Server (`src/server.ts`):**',
         '**Server (`src/server.ts`):**\n\n'
         'Supply your own `db.contacts.search` adapter before running this illustrative scaffold. '
         'Contact names and emails are untrusted display data; render them using text nodes.'),
    ],
    'build-mcpb': [
        ('MCPB is a local MCP server **packaged with its runtime**. The user installs one file; it runs without needing Node, Python, or any toolchain on their machine. It\'s the sanctioned way to distribute local MCP servers.',
         'MCPB packages a local MCP server and its manifest. Runtime availability depends on the host and bundle: '
         'Claude Desktop supplies Node.js, while other hosts must provide a compatible runtime or use a bundled executable. '
         'The example below launches `node`; it does not embed Node in the archive. '
         'Verify the target host on a clean machine. See the [official runtime guidance](https://github.com/modelcontextprotocol/mcpb#language-choice-recommendation).'),
        ('import { readFile, readdir } from "node:fs/promises";\nimport { join } from "node:path";',
         'import { readFile, readdir, realpath } from "node:fs/promises";\nimport { join, resolve, relative, isAbsolute, sep } from "node:path";'),
        ('const ROOT = (process.env.ROOT_DIR ?? join(homedir(), "Documents"));',
         'const ROOT = await realpath(process.env.ROOT_DIR ?? join(homedir(), "Documents"));\n\n'
         'async function confinedPath(path) {\n'
         '  if (isAbsolute(path)) throw new Error("Use a path relative to ROOT");\n'
         '  const candidate = await realpath(resolve(ROOT, path));\n'
         '  const rel = relative(ROOT, candidate);\n'
         '  if (rel === ".." || rel.startsWith(".." + sep) || isAbsolute(rel)) {\n'
         '    throw new Error("Path escapes ROOT");\n'
         '  }\n'
         '  return candidate;\n'
         '}'),
        ('readdir(join(ROOT, path), { withFileTypes: true })',
         'readdir(await confinedPath(path), { withFileTypes: true })'),
        ('readFile(join(ROOT, path), "utf8")',
         'readFile(await confinedPath(path), "utf8")'),
        ('**Sandboxing is entirely your job.**',
         'This read-only example checks existing real paths, including symlink/junction targets. '
         'It is not a process sandbox and does not prevent a malicious concurrent filesystem change between validation and access. '
         'Use OS isolation or handle-based protections when that threat applies; new write targets need a separate validated-parent procedure.\n\n'
         '**Sandboxing is entirely your job.**'),
    ],
}


def main():
    records = []
    for name, changes in REPLACEMENTS.items():
        paths = [ROOT / 'skills' / runtime / name / 'SKILL.md'
                 for runtime in ('claude', 'codex', 'gemini')]
        paths += [ROOT / runtime / 'skills' / name / 'SKILL.md'
                  for runtime in ('.claude', '.agents', '.gemini')]
        for path in paths:
            if not path.is_file():
                continue
            if path.is_symlink() or path.parent.is_symlink():
                raise RuntimeError(f'Unexpected vendor link: {path}')
            original = path.read_bytes()
            text = original.decode('utf-8').replace('\r\n', '\n')
            for old, new in changes:
                if old not in text:
                    raise RuntimeError(f'Repair anchor absent; inspect before editing: {path}: {old[:60]}')
                text = text.replace(old, new, 1)
            digest = hashlib.sha256(original).hexdigest()
            backup = OUT / 'backups' / 'parent' / path.relative_to(ROOT)
            backup.parent.mkdir(parents=True, exist_ok=True)
            if backup.exists():
                raise RuntimeError(f'Backup already exists: {backup}')
            backup.write_bytes(original)
            if path.read_bytes() != original:
                raise RuntimeError(f'Concurrent change: {path}')
            path.write_text(text, encoding='utf-8', newline='\n')
            records.append({'path': str(path), 'name': name, 'before_sha256': digest,
                            'after_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                            'backup': str(backup)})
    (OUT / 'parent-scaffold-repairs.json').write_text(json.dumps(records, indent=2), encoding='utf-8')
    print(f'Repaired {len(records)} existing scaffold entrypoints; originals preserved.')


if __name__ == '__main__':
    main()
