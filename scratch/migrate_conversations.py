import sqlite3

db_path = r"C:\Users\Joshu\.gemini\antigravity\conversation_summaries.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

AI_OS_PROJECT_ID = "1e181e2e-860b-48c6-9209-540e3e7a1965"
AI_OS_WORKSPACE_URI = '["file:///c%3A/Users/Joshu/dev/ai-os"]'

# Count rows to update
rows = cursor.execute("SELECT count(*) FROM conversation_summaries WHERE project_id = 'outside-of-project'").fetchone()[0]
print(f"Found {rows} conversations in 'outside-of-project'")

# Perform migration
cursor.execute("""
    UPDATE conversation_summaries 
    SET project_id = ?, workspace_uris = ?
    WHERE project_id = 'outside-of-project'
""", (AI_OS_PROJECT_ID, AI_OS_WORKSPACE_URI))

conn.commit()
print(f"Successfully migrated {rows} conversations to project {AI_OS_PROJECT_ID} (ai-os).")

# Verify
remaining = cursor.execute("SELECT count(*) FROM conversation_summaries WHERE project_id = 'outside-of-project'").fetchone()[0]
ai_os_count = cursor.execute("SELECT count(*) FROM conversation_summaries WHERE project_id = ?", (AI_OS_PROJECT_ID,)).fetchone()[0]
print(f"Remaining outside-of-project: {remaining}")
print(f"Total conversations now under ai-os: {ai_os_count}")

conn.close()
