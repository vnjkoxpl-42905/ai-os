import importlib.util
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('runtime_export', Path(__file__).parents[1] / 'runtime_export.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class RuntimeTests(unittest.TestCase):
    def test_separate_catalogs_and_covered_memories_only(self):
        with tempfile.TemporaryDirectory() as temp:
            home = Path(temp) / 'home'
            for folder, text in (('.agents/skills/shared', 'agents'), ('.claude/skills/shared', 'claude'), ('.codex/skills/shared', 'codex')):
                path = home / folder
                path.mkdir(parents=True)
                (path / 'SKILL.md').write_text(text)
                (path / '.env').write_text('should never copy')
                (path / 'node_modules').mkdir()
                (path / 'node_modules/package.json').write_text('dependency')
            root = Path(temp) / 'vault'
            encoded = str(root).replace(':', '-').replace('\\', '-').replace('/', '-')
            covered = home / '.claude/projects' / encoded / 'memory'
            covered.mkdir(parents=True)
            (covered / 'MEMORY.md').write_text('context')
            other = home / '.claude/projects/unrelated/memory'
            other.mkdir(parents=True)
            (other / 'private.md').write_text('not covered')
            target = Path(temp) / 'export'
            result = module.export_runtime(target, {'runtime_home': str(home), '_allowed_roots': [str(root)]})
            self.assertEqual(result['counts']['claude_memory_files'], 1)
            for runtime in ('agents', 'claude', 'codex'):
                self.assertEqual((target / runtime / 'skills/shared/SKILL.md').read_text(), runtime)
                self.assertFalse((target / runtime / 'skills/shared/.env').exists())
                self.assertFalse((target / runtime / 'skills/shared/node_modules').exists())
            self.assertFalse((target / 'claude/memories/unrelated').exists())

    def test_sqlite_export_includes_wal_committed_memory(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'memory.sqlite'
            writer = sqlite3.connect(path)
            writer.execute('PRAGMA journal_mode=WAL')
            writer.execute('CREATE TABLE stage1_outputs(thread_id TEXT PRIMARY KEY, raw_memory TEXT, rollout_summary TEXT)')
            writer.execute('INSERT INTO stage1_outputs VALUES(?,?,?)', ('one', 'memory', 'summary'))
            writer.commit()
            target = Path(temp) / 'export.json'
            try:
                self.assertEqual(module.codex_memories(path, target, []), 1)
                result = json.loads(target.read_text())
                self.assertEqual(result['memories'][0]['raw_memory'], 'memory')
                self.assertEqual(writer.execute('SELECT COUNT(*) FROM stage1_outputs').fetchone()[0], 1)
            finally: writer.close()

    def test_unknown_sqlite_schema_is_explicit(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'memory.sqlite'
            db = sqlite3.connect(path)
            db.execute('CREATE TABLE unexpected(x TEXT)')
            db.commit()
            db.close()
            warnings = []
            self.assertEqual(module.codex_memories(path, Path(temp) / 'export.json', warnings), 0)
            self.assertTrue(any('schema' in message for message in warnings))

if __name__ == '__main__': unittest.main()
