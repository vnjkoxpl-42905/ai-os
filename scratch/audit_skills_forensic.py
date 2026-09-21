import os
import re
import yaml

skills_root = r"C:\Users\Joshu\dev\ai-os\.gemini\skills"

dirs = sorted(os.listdir(skills_root))

results = {
    "total_dirs": len(dirs),
    "valid_skills": [],
    "inactive_archival": [],
    "project_forks": [],
    "snapshots": [],
    "examples_templates": [],
    "malformed": [],
    "missing_skill_md": [],
    "duplicate_ids": {},
}

for d in dirs:
    dpath = os.path.join(skills_root, d)
    if not os.path.isdir(dpath):
        continue
    
    if d == "_inactive":
        # Check contents
        sub = os.listdir(dpath)
        results["inactive_archival"].append((d, sub))
        continue
    elif d == "_project-forks":
        sub = os.listdir(dpath)
        results["project_forks"].append((d, sub))
        continue
    elif d == "_snapshots":
        sub = os.listdir(dpath)
        results["snapshots"].append((d, sub))
        continue
    elif d in ("example-command", "example-skill"):
        results["examples_templates"].append(d)
        
    skill_md = os.path.join(dpath, "SKILL.md")
    if not os.path.exists(skill_md):
        results["missing_skill_md"].append(d)
        continue
        
    try:
        with open(skill_md, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            if not m:
                results["malformed"].append((d, "No YAML frontmatter markers (---)"))
                continue
            fm = m.group(1)
            name_m = re.search(r'^name:\s*(.+)$', fm, re.MULTILINE)
            desc_m = re.search(r'^description:\s*(.+)$', fm, re.MULTILINE)
            if not name_m or not desc_m:
                results["malformed"].append((d, "Missing name or description in frontmatter"))
                continue
            name = name_m.group(1).strip()
            desc = desc_m.group(1).strip()
            results["valid_skills"].append((d, name, desc[:100]))
            
            # check duplicate IDs
            if name not in results["duplicate_ids"]:
                results["duplicate_ids"][name] = []
            results["duplicate_ids"][name].append(d)
    except Exception as e:
        results["malformed"].append((d, str(e)))

print("=== Forensic Breakdown of .gemini/skills ===")
print(f"Total directories at root: {results['total_dirs']}")
print(f"Valid skills with SKILL.md: {len(results['valid_skills'])}")
print(f"Missing SKILL.md (containers): {results['missing_skill_md']}")
print(f"Inactive / Archival container: {results['inactive_archival']}")
print(f"Project forks container: {results['project_forks']}")
print(f"Snapshots container: {results['snapshots']}")
print(f"Examples/Templates: {results['examples_templates']}")
print(f"Malformed: {results['malformed']}")

# Let's inspect subdirectories inside _inactive, _project-forks, _snapshots
print("\n--- Subdirectories inside _inactive ---")
p_inact = os.path.join(skills_root, "_inactive")
for s in os.listdir(p_inact):
    print(f"  _inactive/{s}: has SKILL.md = {os.path.exists(os.path.join(p_inact, s, 'SKILL.md'))}")

print("\n--- Subdirectories inside _project-forks ---")
p_pf = os.path.join(skills_root, "_project-forks")
for s in os.listdir(p_pf):
    subpath = os.path.join(p_pf, s)
    if os.path.isdir(subpath):
        for subsub in os.listdir(subpath):
            print(f"  _project-forks/{s}/{subsub}: has SKILL.md = {os.path.exists(os.path.join(subpath, subsub, 'SKILL.md'))}")

print("\n--- Subdirectories inside _snapshots ---")
p_snap = os.path.join(skills_root, "_snapshots")
for s in os.listdir(p_snap):
    print(f"  _snapshots/{s}: has SKILL.md = {os.path.exists(os.path.join(p_snap, s, 'SKILL.md'))}")
