from pathlib import Path
import hashlib, json, shutil
config = Path.home()/'.codex/config.toml'
before = config.read_bytes()
digest = hashlib.sha256(before).hexdigest()
text = before.decode('utf-8')
if '[mcp_servers.21st]' in text or '[mcp_servers."21st"]' in text:
    raise SystemExit('Existing 21st registration requires inspection; no write made.')
backup = Path('research/2026-10-24-design-skill-doctor/config-before-21st.toml.backup')
# Home config may contain unrelated secrets: keep the backup outside the repository.
backup = config.with_name('config.toml.before-21st-20261024.bak')
if backup.exists():
    raise SystemExit('Backup already exists; no overwrite made.')
shutil.copy2(config, backup)
addition = '\n[mcp_servers.21st]\ncommand = "C:/Program Files/nodejs/node.exe"\nargs = ["C:/Users/Joshu/dev/ai-os/system/scripts/start-21st-mcp.mjs"]\nstartup_timeout_sec = 30\n'
if hashlib.sha256(config.read_bytes()).hexdigest() != digest:
    raise SystemExit('Config changed during registration; no write made.')
config.write_bytes(before + addition.encode('utf-8'))
import tomllib
registered = tomllib.loads(config.read_text(encoding='utf-8'))['mcp_servers']['21st']
print(json.dumps({'registered':registered['args'][0].endswith('start-21st-mcp.mjs'),'backup':str(backup),'secrets_added_to_config':False}))
