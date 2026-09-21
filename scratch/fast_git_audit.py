import os, subprocess

root_dir = r"C:\Users\Joshu\dev\ai-os"

output = subprocess.check_output(f'git -C "{root_dir}" ls-files', shell=True, text=True)
tracked_set = set(output.splitlines())
print(f"Total tracked files in ai-os repo: {len(tracked_set)}")

# Group by top-level directory or file
counts = {}
for f in tracked_set:
    parts = f.replace("\\", "/").split("/")
    top = parts[0]
    counts[top] = counts.get(top, 0) + 1

items = os.listdir(root_dir)
dirs = [d for d in items if os.path.isdir(os.path.join(root_dir, d))]

print("\n=== Top-level Directories & Tracked File Counts ===")
for d in sorted(dirs):
    c = counts.get(d, 0)
    print(f"  {d:25} : {c:5} tracked files")

