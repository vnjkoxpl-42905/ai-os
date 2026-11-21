import json
import subprocess
from pathlib import Path

home = Path(__file__).parent
old = json.loads((home.parent / 'claude-remediation/claudex-jk37sikm/result.json').read_text())
scope = sorted(set(old['scope'] + [
    'src/hooks/useNoteReaderTransition.ts', 'src/hooks/useNoteReaderTransition.test.tsx',
    'src/styles/note-reader-transition.css',
    'src/components/classroom/shell/ClassroomLayout.tsx',
    'src/components/classroom/shell/ClassroomLayout.test.tsx',
    'src/components/classroom/ClassroomNotesJourney.test.tsx',
    'src/lib/myWorkNotesNavigation.ts', 'src/lib/myWorkNotesNavigation.test.ts',
]))
args = ['python', 'C:/Users/Joshu/dev/ai-os/.agents/skills/claudex-loop/scripts/runner.py',
        'inspect', '--host', 'codex', '--builder', 'codex',
        '--repo', 'C:/Users/Joshu/dev/ai-os-projects/lsatu-my-work-20261026',
        '--plan', 'docs/plans/my-work-note-reader-transition.md',
        '--base', 'e4035d9c8ec97a3aaec01b0b3464533872328bc8',
        '--model', 'claude-opus-5-5', '--effort', 'medium',
        '--cli', 'C:/Users/Joshu/.local/bin/claude.EXE',
        '--feedback', str(home / 'inspection-context.md'),
        '--artifacts', str(home), '--timeout', '900']
for item in scope:
    args.extend(['--scope', item])
raise SystemExit(subprocess.call(args))
