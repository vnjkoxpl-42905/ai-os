import os, glob

conv_dir = r"C:\Users\Joshu\.gemini\antigravity\conversations"
if os.path.exists(conv_dir):
    files = glob.glob(os.path.join(conv_dir, "*"))
    print(f"Total files in conversations: {len(files)}")
    for f in files[:10]:
        print(f"{os.path.basename(f)} ({os.path.getsize(f)} bytes)")

