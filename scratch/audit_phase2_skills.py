import os
import hashlib
import glob
import re
from collections import defaultdict, Counter

# Skill directories
roots = {
    ".gemini/skills": r"C:\Users\Joshu\dev\ai-os\.gemini\skills",
    ".agents/skills": r"C:\Users\Joshu\dev\ai-os\.agents\skills",
    "global_config_skills": r"C:\Users\Joshu\.gemini\config\skills",
    "plugin_skills": r"C:\Users\Joshu\.gemini\config\plugins",
    "builtin_skills": r"C:\Users\Joshu\.gemini\antigravity\builtin\skills"
}

def get_hash(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

print("=== Scanning All Skills Across Roots ===")
all_skills = [] # (identifier, path, root_name, category, hash, size)

# 1. .gemini/skills
p_gem = roots[".gemini/skills"]
for item in os.listdir(p_gem):
    fp = os.path.join(p_gem, item)
    if os.path.isdir(fp):
        if item == "_inactive":
            for sub in os.listdir(fp):
                sub_p = os.path.join(fp, sub)
                sk = os.path.join(sub_p, "SKILL.md")
                if os.path.exists(sk):
                    all_skills.append((sub, sk, ".gemini/skills", "ARCHIVAL", get_hash(sk), os.path.getsize(sk)))
        elif item == "_snapshots":
            for sub in os.listdir(fp):
                sub_p = os.path.join(fp, sub)
                sk = os.path.join(sub_p, "SKILL.md")
                if os.path.exists(sk):
                    all_skills.append((sub, sk, ".gemini/skills", "SNAPSHOT", get_hash(sk), os.path.getsize(sk)))
        elif item == "_project-forks":
            for proj in os.listdir(fp):
                proj_p = os.path.join(fp, proj)
                if os.path.isdir(proj_p):
                    for sub in os.listdir(proj_p):
                        sub_p = os.path.join(proj_p, sub)
                        sk = os.path.join(sub_p, "SKILL.md")
                        if os.path.exists(sk):
                            all_skills.append((sub, sk, ".gemini/skills", "PROJECT FORK", get_hash(sk), os.path.getsize(sk)))
        elif "example" in item.lower():
            sk = os.path.join(fp, "SKILL.md")
            if os.path.exists(sk):
                all_skills.append((item, sk, ".gemini/skills", "EXAMPLE", get_hash(sk), os.path.getsize(sk)))
        else:
            sk = os.path.join(fp, "SKILL.md")
            if os.path.exists(sk):
                all_skills.append((item, sk, ".gemini/skills", "ACTIVE CANONICAL", get_hash(sk), os.path.getsize(sk)))

# 2. .agents/skills
p_ag = roots[".agents/skills"]
if os.path.exists(p_ag):
    for item in os.listdir(p_ag):
        fp = os.path.join(p_ag, item)
        sk = os.path.join(fp, "SKILL.md")
        if os.path.exists(sk):
            all_skills.append((item, sk, ".agents/skills", "ACTIVE CANONICAL", get_hash(sk), os.path.getsize(sk)))

# 3. global config skills
p_gl = roots["global_config_skills"]
if os.path.exists(p_gl):
    for item in os.listdir(p_gl):
        fp = os.path.join(p_gl, item)
        sk = os.path.join(fp, "SKILL.md")
        if os.path.exists(sk):
            all_skills.append((item, sk, "global_config_skills", "ACTIVE CANONICAL", get_hash(sk), os.path.getsize(sk)))

# 4. plugin skills
p_pl = roots["plugin_skills"]
if os.path.exists(p_pl):
    for root, dirs, files in os.walk(p_pl):
        if "SKILL.md" in files:
            sk = os.path.join(root, "SKILL.md")
            item = os.path.basename(root)
            all_skills.append((item, sk, "plugin_skills", "ACTIVE CANONICAL", get_hash(sk), os.path.getsize(sk)))

# 5. builtin skills
p_bu = roots["builtin_skills"]
if os.path.exists(p_bu):
    for root, dirs, files in os.walk(p_bu):
        if "SKILL.md" in files:
            sk = os.path.join(root, "SKILL.md")
            item = os.path.basename(root)
            all_skills.append((item, sk, "builtin_skills", "ACTIVE CANONICAL", get_hash(sk), os.path.getsize(sk)))

print(f"Total skills parsed across all roots: {len(all_skills)}")

# Count by root and category
root_counts = Counter(s[2] for s in all_skills)
cat_counts = Counter(s[3] for s in all_skills)

print("\n--- By Root ---")
for r, c in root_counts.items():
    print(f"  {r}: {c}")

print("\n--- By Category ---")
for cat, c in cat_counts.items():
    print(f"  {cat}: {c}")

# Detect duplicates
by_id = defaultdict(list)
for s in all_skills:
    by_id[s[0]].append(s)

duplicates = {k: v for k, v in by_id.items() if len(v) > 1}
print(f"\nTotal Duplicate Skill Identifiers: {len(duplicates)}")
for k, v in sorted(duplicates.items()):
    hashes = set(x[4] for x in v)
    status = "IDENTICAL" if len(hashes) == 1 else "DIVERGENT"
    print(f"  * `{k}` ({len(v)} copies, {status}):")
    for item in v:
        print(f"      - {item[2]} [{item[3]}]: {item[1]} (SHA: {item[4][:12]}...)")
