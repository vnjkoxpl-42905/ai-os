import os

paths = {
    ".gemini/skills": r"C:\Users\Joshu\dev\ai-os\.gemini\skills",
    ".agents/skills": r"C:\Users\Joshu\dev\ai-os\.agents\skills",
    "config/skills": r"C:\Users\Joshu\.gemini\config\skills"
}

def classify(root_base, dir_name, full_path):
    rel = os.path.relpath(full_path, root_base)
    parts = rel.split(os.sep)
    if "_inactive" in parts:
        return "ARCHIVAL"
    if "_snapshots" in parts:
        return "SNAPSHOT"
    if "_project-forks" in parts:
        return "FORK"
    if "example" in dir_name.lower():
        return "EXAMPLE"
    if os.path.exists(os.path.join(full_path, "SKILL.md")):
        return "ACTIVE"
    # if it's a container directory
    return "UNKNOWN"

for label, p in paths.items():
    print(f"\n==========================================")
    print(f"TREE FOR: {p} ({label})")
    print(f"==========================================")
    if not os.path.exists(p):
        print("NOT PRESENT")
        continue
    for item in sorted(os.listdir(p)):
        fp = os.path.join(p, item)
        if os.path.isdir(fp):
            # check if it has sub-skills
            c = classify(p, item, fp)
            if item in ["_inactive", "_snapshots", "_project-forks"]:
                print(f"[CONTAINER] {item}/")
                for sub in sorted(os.listdir(fp)):
                    sub_p = os.path.join(fp, sub)
                    if os.path.isdir(sub_p):
                        # check if it has further subdirs (like _project-forks/lsatu/...)
                        sub_c = classify(p, sub, sub_p)
                        if sub == "lsatu":
                            print(f"  [PROJECT] {sub}/")
                            for lsatu_sub in sorted(os.listdir(sub_p)):
                                lsatu_sub_p = os.path.join(sub_p, lsatu_sub)
                                if os.path.isdir(lsatu_sub_p):
                                    lsatu_c = "FORK" if os.path.exists(os.path.join(lsatu_sub_p, "SKILL.md")) else "UNKNOWN"
                                    print(f"    - {lsatu_sub}: {lsatu_c}")
                        else:
                            print(f"  - {sub}: {sub_c}")
            else:
                print(f"- {item}: {c}")
