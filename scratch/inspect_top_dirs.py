import os, subprocess, json

root_dir = r"C:\Users\Joshu\dev\ai-os"

print("=== Top level directories in ai-os ===")
items = os.listdir(root_dir)
dirs = [d for d in items if os.path.isdir(os.path.join(root_dir, d))]

for d in sorted(dirs):
    full = os.path.join(root_dir, d)
    # count files and total size
    total_files = 0
    total_size = 0
    for r, subdirs, files in os.walk(full):
        # don't walk huge vendor trees deep
        if any(ign in r.lower() for ign in ["node_modules", ".git", "dist", "build", ".venv"]):
            continue
        total_files += len(files)
        for f in files:
            try:
                total_size += os.path.getsize(os.path.join(r, f))
            except:
                pass
    
    # Check git tracking status of directory
    try:
        git_res = subprocess.check_output(f'git -C "{root_dir}" status --porcelain -uall "{d}"', shell=True, text=True).strip()
        git_tracked = "Tracked" if not git_res.startswith("??") else "Untracked"
    except:
        git_tracked = "Unknown"
        
    print(f"Directory: {d:25} | Files: {total_files:5} | Size: {total_size/1024/1024:6.2f} MB | Git: {git_tracked}")

