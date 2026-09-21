import os, json

p1 = r"C:\Users\Joshu\AppData\Roaming\Antigravity IDE\User\settings.json"
if os.path.exists(p1):
    print("=== settings.json ===")
    with open(p1, "r", encoding="utf-8") as f:
        print(f.read())

p2 = r"C:\Users\Joshu\.gemini\antigravity\antigravity_state.pbtxt"
if os.path.exists(p2):
    print("\n=== antigravity_state.pbtxt ===")
    with open(p2, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        print(f"Total length: {len(content)}")
        print(content[:3000])

p3 = r"C:\Users\Joshu\AppData\Local\Programs\Antigravity IDE\resources\app\extensions\antigravity"
if os.path.exists(p3):
    print("\n=== extension antigravity ===")
    for item in os.listdir(p3):
        full = os.path.join(p3, item)
        print(f"{item} ({'dir' if os.path.isdir(full) else f'{os.path.getsize(full)} bytes'})")

