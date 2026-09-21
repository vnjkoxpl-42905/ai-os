import os, subprocess

root_dir = r"C:\Users\Joshu\dev\ai-os"

items = os.listdir(root_dir)
dirs = [d for d in items if os.path.isdir(os.path.join(root_dir, d))]

for d in sorted(dirs):
    # check if directory has any tracked file
    try:
        res = subprocess.check_output(f'git -C "{root_dir}" ls-files "{d}"', shell=True, text=True)
        tracked_count = len(res.strip().splitlines()) if res.strip() else 0
        
        # check if ignored
        ign_res = subprocess.run(f'git -C "{root_dir}" check-ignore "{d}"', shell=True, capture_output=True, text=True)
        is_ignored = (ign_res.returncode == 0)
        
        print(f"{d:25} | Tracked files: {tracked_count:4} | Ignored: {str(is_ignored):5}")
    except Exception as e:
        print(f"{d:25} | Error: {e}")

