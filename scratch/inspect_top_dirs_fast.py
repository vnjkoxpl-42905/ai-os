import os, subprocess

root_dir = r"C:\Users\Joshu\dev\ai-os"

# Get tracked files once from git ls-files
tracked_files = set(subprocess.check_output(f'git -C "{root_dir}" ls-files', shell=True, text=True).splitlines())
print(f"Total git tracked files: {len(tracked_files)}")

items = os.listdir(root_dir)
dirs = [d for d in items if os.path.isdir(os.path.join(root_dir, d))]

for d in sorted(dirs):
    full = os.path.join(root_dir, d)
    tracked_count = sum(1 for f in tracked_files if f.startswith(d + "/") or f.startswith(d + "\\"))
    
    # count local files
    local_count = 0
    total_size = 0
    for r, subdirs, files in os.walk(full):
        if any(ign in r.lower() for ign in ["node_modules", ".git", "dist", "build", ".venv"]):
            continue
        local_count += len(files)
        for f in files:
            try:
                total_size += os.path.getsize(os.path.join(r, f))
            except:
                pass
                
    status = "Tracked" if tracked_count > 0 else "Untracked/Ignored"
    print(f"{d:25} | Tracked files: {tracked_count:4} | Total files: {local_count:4} | Size: {total_size/1024/1024:6.2f} MB | {status}")

