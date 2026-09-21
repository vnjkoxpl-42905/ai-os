import os

base = r"C:\Users\Joshu\dev\ai-os\projects\lsatu"
print(f"=== Searching for nested instruction files in {base} ===")

nested = []
for root, dirs, files in os.walk(base):
    # skip node_modules and .git to be fast
    if 'node_modules' in dirs:
        dirs.remove('node_modules')
    if '.git' in dirs:
        dirs.remove('.git')
    for f in files:
        if f.upper() in ['AGENTS.MD', 'GEMINI.MD', 'CLAUDE.MD']:
            full_p = os.path.join(root, f)
            size = os.path.getsize(full_p)
            rel_p = os.path.relpath(full_p, base)
            nested.append((rel_p, full_p, size))

for rel_p, full_p, size in sorted(nested):
    print(f"- {rel_p} ({size} bytes): {full_p}")
