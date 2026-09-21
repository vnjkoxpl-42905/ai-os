import sqlite3
import os
import glob

conn = sqlite3.connect(r'C:\Users\Joshu\.gemini\antigravity\conversation_summaries.db')
cursor = conn.cursor()

rows = cursor.execute("""
    SELECT conversation_id, title, preview, step_count, last_modified_time 
    FROM conversation_summaries 
    WHERE project_id = 'outside-of-project'
    ORDER BY last_modified_time DESC
""").fetchall()

print(f"Total 'outside-of-project' conversations: {len(rows)}\n")

for cid, title, preview, steps, last_mod in rows:
    # Check if there are artifacts or user files in this conversation's brain folder
    brain_dir = os.path.join(r"C:\Users\Joshu\.gemini\antigravity\brain", cid)
    artifacts = []
    if os.path.exists(brain_dir):
        for f in os.listdir(brain_dir):
            if f.endswith(('.md', '.json', '.png', '.py', '.txt', '.sh', '.ps1')) and not f.startswith('.'):
                artifacts.append(f)
    
    print(f"[{title or 'Untitled'}] (ID: {cid[:8]}... | Steps: {steps} | Date: {last_mod})")
    if artifacts:
        print(f"  Artifacts in brain: {artifacts}")
    else:
        print(f"  Preview: {preview[:80]}...")
