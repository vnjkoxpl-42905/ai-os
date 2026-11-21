"""Focused capture safety regressions; no capture, cloud access or source edits."""
import ast
import shutil
import sqlite3
import tempfile
from pathlib import Path
from types import SimpleNamespace

source = Path(__file__).with_name('new-machine-backup.py')
tree = ast.parse(source.read_text())
guard = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'require_headroom')
namespace = {'shutil': shutil, 'stage': Path.home(), 'minimum_free': 10**20,
             'a': SimpleNamespace(min_free_gib=20)}
exec(compile(ast.Module(body=[guard], type_ignores=[]), str(source), 'exec'), namespace)
try:
    namespace['require_headroom']()
except RuntimeError:
    print('PASS insufficient headroom rejected')
else:
    raise AssertionError('Headroom guard accepted impossible reserve')

with tempfile.TemporaryDirectory() as directory:
    path = Path(directory) / 'wal.db'
    connection = sqlite3.connect(path)
    try:
        connection.execute('PRAGMA journal_mode=WAL')
        connection.execute('PRAGMA wal_autocheckpoint=0')
        connection.execute('CREATE TABLE t (x BLOB)')
        connection.executemany('INSERT INTO t VALUES (?)', [(b'x' * 4096,)] * 1024)
        connection.commit()
        connection.execute('BEGIN')
        connection.execute('SELECT count(*) FROM sqlite_master').fetchone()
        logical = connection.execute('PRAGMA page_count').fetchone()[0] * connection.execute('PRAGMA page_size').fetchone()[0]
        assert logical > path.stat().st_size * 2
        print('PASS committed WAL exceeds main-file size allowance')
    finally:
        connection.close()

for relative in ['app-server-control/app-server-control.sock', 'app-server-daemon/daemon-updater.sock']:
    socket = Path.home() / '.codex' / relative
    if socket.exists():
        assert getattr(socket.stat(), 'st_reparse_tag', 0) == 0x80000023
        print('PASS actual Windows AF_UNIX socket tag:', relative)
    else:
        print('SKIP live socket unavailable:', relative)
