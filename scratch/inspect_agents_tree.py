import os

base = r"C:\Users\Joshu\dev\ai-os\.agents"
print(f"=== Directory Tree of {base} ===")
for root, dirs, files in os.walk(base):
    rel = os.path.relpath(root, base)
    indent = "  " * (rel.count(os.sep) if rel != "." else 0)
    folder_name = os.path.basename(root) if rel != "." else ".agents"
    print(f"{indent}[DIR] {folder_name}/")
    for f in sorted(files):
        print(f"{indent}  - {f} ({os.path.getsize(os.path.join(root, f))} B)")
