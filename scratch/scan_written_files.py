import sqlite3
import os
import json

conn = sqlite3.connect(r'C:\Users\Joshu\.gemini\antigravity\conversation_summaries.db')
cursor = conn.cursor()

rows = cursor.execute("""
    SELECT conversation_id, title 
    FROM conversation_summaries 
    WHERE project_id = 'outside-of-project'
""").fetchall()

written_files = set()
commands_run = []

for cid, title in rows:
    transcript_path = os.path.join(r"C:\Users\Joshu\.gemini\antigravity\brain", cid, ".system_generated", "logs", "transcript.jsonl")
    if os.path.exists(transcript_path):
        with open(transcript_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                try:
                    data = json.loads(line)
                    for call in data.get('tool_calls', []):
                        name = call.get('name')
                        args = call.get('args', {})
                        if name in ('write_to_file', 'replace_file_content'):
                            target = args.get('TargetFile')
                            if target:
                                written_files.add((cid[:8], title or 'Untitled', target.strip('"')))
                        elif name == 'run_command':
                            cwd = args.get('Cwd', '').strip('"')
                            cmd = args.get('CommandLine', '').strip('"')
                            if cwd and not cwd.startswith(('C:\\Users\\Joshu\\dev\\ai-os', 'c:\\Users\\Joshu\\dev\\ai-os')):
                                commands_run.append((cid[:8], title or 'Untitled', cwd, cmd[:60]))
                except:
                    pass

print(f"Total files written by outside-of-project conversations: {len(written_files)}")
for cid, title, target in sorted(written_files, key=lambda x: x[2]):
    print(f"[{cid}] {title}: {target}")

print(f"\nCommands run in non-ai-os directories ({len(commands_run)}):")
for cid, title, cwd, cmd in commands_run[:15]:
    print(f"[{cid}] {title} in {cwd}: {cmd}")
