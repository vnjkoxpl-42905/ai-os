import os

root_dir = r"C:\Users\Joshu\dev\ai-os"
items = os.listdir(root_dir)
dirs = [d for d in items if os.path.isdir(os.path.join(root_dir, d))]
files = [f for f in items if os.path.isfile(os.path.join(root_dir, f))]

print("=== Top Level Directories ===")
for d in sorted(dirs):
    print(" ", d)

print("\n=== Top Level Files ===")
for f in sorted(files):
    print(" ", f)

