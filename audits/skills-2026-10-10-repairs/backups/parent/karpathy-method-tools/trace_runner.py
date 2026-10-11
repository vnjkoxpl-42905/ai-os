"""Trace actual Python file execution for the local run gate."""
import json
from pathlib import Path
import runpy
import sys

files = set()


def trace(frame, event, arg):
    if event == 'line' and not frame.f_code.co_filename.startswith('<'):
        files.add(str(Path(frame.f_code.co_filename).resolve()))
    return trace


record = Path(sys.argv[1])
args = sys.argv[2:]
sys.settrace(trace)
try:
    if args[:1] == ['-m'] and len(args) >= 2:
        sys.argv = [args[1], *args[2:]]
        runpy.run_module(args[1], run_name='__main__', alter_sys=True)
    elif args[:1] == ['-c'] and len(args) >= 2:
        sys.argv = ['-c', *args[2:]]
        exec(compile(args[1], '<string>', 'exec'), {'__name__': '__main__'})
    elif args and not args[0].startswith('-'):
        sys.argv = args
        sys.path.insert(0, str(Path(args[0]).resolve().parent))
        runpy.run_path(args[0], run_name='__main__')
    else:
        raise ValueError('Use Python file.py, -m module or -c code for traced execution.')
finally:
    sys.settrace(None)
    record.write_text(json.dumps(sorted(files)), encoding='utf-8')
