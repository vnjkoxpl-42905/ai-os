import os, json, re

ext_dir = r"C:\Users\Joshu\AppData\Local\Programs\Antigravity IDE\resources\app\extensions\antigravity"

print("=== Extension schemas directory ===")
schema_dir = os.path.join(ext_dir, "schemas")
if os.path.exists(schema_dir):
    for item in os.listdir(schema_dir):
        print(f"Schema file: {item}")
        with open(os.path.join(schema_dir, item), "r", encoding="utf-8") as f:
            print(f.read()[:500])

print("\n=== Grepping dist for model names and MODEL_PLACEHOLDER ===")
dist_dir = os.path.join(ext_dir, "dist")
if os.path.exists(dist_dir):
    for root, dirs, files in os.walk(dist_dir):
        for fname in files:
            if fname.endswith(".js"):
                full = os.path.join(root, fname)
                with open(full, "r", encoding="utf-8", errors="ignore") as jf:
                    text = jf.read()
                    matches = set(re.findall(r"MODEL_PLACEHOLDER_[A-Za-z0-9_]+", text))
                    if matches:
                        print(f"In {fname}: found {len(matches)} placeholders: {matches}")
                    
                    # Search for enum or mapping with MODEL_PLACEHOLDER
                    for m in list(matches)[:5]:
                        idx = text.find(m)
                        snippet = text[max(0, idx-100):min(len(text), idx+200)]
                        print(f"Context for {m}:\n{snippet}\n")

print("\n=== Checking bin directories ===")
for b in [
    os.path.join(ext_dir, "bin"),
    r"C:\Users\Joshu\.gemini\antigravity\bin",
    r"C:\Users\Joshu\AppData\Local\Programs\antigravity\resources\bin"
]:
    if os.path.exists(b):
        print(f"In {b}: {os.listdir(b)}")

