"""Export portable skills and memories; credentials and machine settings stay out."""
from __future__ import annotations
import json, os, shutil, sqlite3
from pathlib import Path

SKIP_DIRS = {'.git', 'node_modules', '.venv', 'venv', '__pycache__', '.cache'}
BINARY_SUFFIXES = {'.exe', '.dll', '.so', '.dylib', '.pyd', '.pyc', '.node'}

def linked(path):
    return path.is_symlink() or bool(getattr(path.lstat(), 'st_file_attributes', 0) & 0x400)

def copy_tree(source, destination, warnings):
    source, destination = Path(source), Path(destination)
    count = 0
    if not source.exists():
        warnings.append('Missing source: ' + str(source)); return count
    if linked(source):
        warnings.append('Skipped linked source: ' + str(source)); return count
    for directory, dirs, files in os.walk(source, followlinks=False):
        base = Path(directory)
        allowed = []
        for name in dirs:
            item = base / name
            if name in SKIP_DIRS: continue
            if linked(item): warnings.append('Skipped linked directory: ' + str(item))
            else: allowed.append(name)
        dirs[:] = allowed
        for name in files:
            item = base / name
            if linked(item):
                warnings.append('Skipped linked file: ' + str(item)); continue
            lower = name.lower()
            if item.suffix.lower() in BINARY_SUFFIXES:
                continue
            if lower.startswith('.env') or lower in {'auth.json', 'credentials.json', '.credentials.json', 'tokens.json', 'token_cache.json'}:
                warnings.append('Excluded credential source: ' + str(item)); continue
            target = destination / item.relative_to(source)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(item, target)
            count += 1
    return count

def plugin_skills(source, destination, warnings):
    source = Path(source)
    if not source.exists(): return [], 0
    if linked(source):
        warnings.append('Skipped linked plugin cache: ' + str(source)); return [], 0
    owners = []
    for directory, dirs, files in os.walk(source, followlinks=False):
        base = Path(directory)
        dirs[:] = [name for name in dirs if name not in SKIP_DIRS and not linked(base / name)]
        if 'SKILL.md' in files and 'skills' in base.relative_to(source).parts and not linked(base / 'SKILL.md'):
            owners.append(base)
            # This owning skill includes nested references; do not copy nested
            # SKILL.md bundles a second time under another registry entry.
            dirs[:] = []
    index, files = [], 0
    for owner in sorted(owners):
        relative = owner.relative_to(source)
        count = copy_tree(owner, destination / relative, warnings)
        index.append({'source_path': str(owner), 'relative_path': relative.as_posix(), 'files': count})
        files += count
    return index, files

def codex_memories(source, target, warnings):
    source = Path(source)
    if not source.exists(): return 0
    if linked(source):
        warnings.append('Skipped linked memory database: ' + str(source)); return 0
    connection = sqlite3.connect(source.resolve().as_uri() + '?mode=ro', uri=True, timeout=10)
    snapshot = sqlite3.connect(':memory:')
    try:
        connection.backup(snapshot)
        tables = {row[0] for row in snapshot.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        rows = []
        if 'stage1_outputs' in tables:
            columns = {row[1] for row in snapshot.execute('PRAGMA table_info(stage1_outputs)')}
            chosen = [name for name in ('thread_id', 'raw_memory', 'rollout_summary', 'rollout_slug', 'generated_at') if name in columns]
            if {'thread_id', 'raw_memory'}.issubset(columns):
                rows = [dict(zip(chosen, row)) for row in snapshot.execute('SELECT ' + ','.join(chosen) + ' FROM stage1_outputs ORDER BY thread_id')]
            else: warnings.append('Codex memory schema lacks supported fields')
        else: warnings.append('Codex memory schema lacks stage1_outputs')
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps({'format': 'codex-stage1-memory-export-v1', 'memories': rows}, indent=2), encoding='utf-8')
        return len(rows)
    finally:
        snapshot.close(); connection.close()

def export_runtime(destination, config):
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    home = Path(config.get('runtime_home', Path.home()))
    supplied = config.get('runtime_sources', {})
    defaults = {'agents_skills': home / '.agents/skills', 'claude_skills': home / '.claude/skills', 'codex_skills': home / '.codex/skills', 'claude_instruction': home / '.claude/CLAUDE.md', 'codex_instruction': home / '.codex/AGENTS.md', 'claude_projects': home / '.claude/projects', 'codex_memories': home / '.codex/memories_1.sqlite', 'claude_plugin_cache': home / '.claude/plugins/cache', 'codex_plugin_cache': home / '.codex/plugins/cache'}
    sources = {key: Path(supplied.get(key, value)) for key, value in defaults.items()}
    warnings, counts = [], {}
    for key, path in (('agents_skills', 'agents/skills'), ('claude_skills', 'claude/skills'), ('codex_skills', 'codex/skills')):
        counts[key] = copy_tree(sources[key], destination / path, warnings)
    plugins = {}
    for runtime in ('claude', 'codex'):
        bundles, file_count = plugin_skills(sources[runtime + '_plugin_cache'], destination / runtime / 'plugins', warnings)
        plugins[runtime] = bundles
        counts[runtime + '_plugin_skills'] = len(bundles)
        counts[runtime + '_plugin_files'] = file_count
    for key, path in (('claude_instruction', 'claude/CLAUDE.md'), ('codex_instruction', 'codex/AGENTS.md')):
        source = sources[key]
        if source.is_file() and not linked(source):
            target = destination / path
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
            counts[key] = 1
        else: warnings.append('Missing or linked global instructions: ' + str(source))
    roots = config.get('_allowed_roots', [])
    encoded = {str(Path(root)).replace(':', '-').replace('\\', '-').replace('/', '-') for root in roots}
    projects = sources['claude_projects']
    counts['claude_memory_files'] = 0
    if projects.is_dir() and not linked(projects):
        for project in sorted(projects.iterdir()):
            if project.name in encoded and project.is_dir() and not linked(project):
                memory = project / 'memory'
                if memory.exists(): counts['claude_memory_files'] += copy_tree(memory, destination / 'claude/memories' / project.name, warnings)
    counts['codex_memory_records'] = codex_memories(sources['codex_memories'], destination / 'codex/memories.json', warnings)
    warnings.append('Plugin skill bundles are readable context. Plugin tools, connectors and binaries require separate cloud installation/authentication; native caches are excluded.')
    index = {'format': 'portable-runtime-export-v1', 'counts': counts, 'source_paths': {key: str(value) for key, value in sources.items()}, 'plugin_skills': plugins, 'warnings': warnings}
    (destination / 'INDEX.json').write_text(json.dumps(index, indent=2), encoding='utf-8')
    (destination / 'README.md').write_text('# Portable runtime context\n\nRead INDEX.json, then the relevant runtime instruction file, skills and memories. Preserve agents, Claude and Codex skills as separate catalogs. Plugin skill bundles and their references are under claude/plugins/ and codex/plugins/ with source lineage preserved; INDEX.json lists them. Claude memories are under claude/memories/<original-project-key>/; remap to the cloud checkout rather than recreating a Windows path. Codex memories.json is readable context, not a native Claude memory database.\n\nThese are exported sources. Do not blindly activate Windows paths, hooks or shell commands. Check cloud compatibility before installing a skill. Plugin tools and connectors need separate installation and authentication. Settings, credentials, OAuth sessions, browser state, native caches and executables are excluded. The enclosing snapshot secret scan applies to every exported file.\n', encoding='utf-8')
    return index
