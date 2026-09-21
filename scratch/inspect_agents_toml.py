import os
import glob

agents_dir = r"C:\Users\Joshu\dev\ai-os\.gemini\agents"
files = sorted(glob.glob(os.path.join(agents_dir, "*.toml")))

print(f"Total Subagent TOML files: {len(files)}")
for f in files:
    name = os.path.basename(f)
    size = os.path.getsize(f)
    model = "inherit (default)"
    sandbox = "inherit (default)"
    agent_name = ""
    desc = ""
    with open(f, "r", encoding="utf-8", errors="ignore") as fh:
        content = fh.read()
        for line in content.splitlines():
            line_s = line.strip()
            if line_s.startswith("name ="):
                agent_name = line_s.split("=", 1)[1].strip().strip('"')
            elif line_s.startswith("model ="):
                model = line_s.split("=", 1)[1].strip().strip('"')
            elif line_s.startswith("sandbox_mode ="):
                sandbox = line_s.split("=", 1)[1].strip().strip('"')
            elif line_s.startswith("description =") and not desc:
                desc = line_s.split("=", 1)[1].strip().strip('"')[:60]
    print(f"| `{name}` | `{agent_name}` | `{model}` | `{sandbox}` | {size} B | {desc}... |")
