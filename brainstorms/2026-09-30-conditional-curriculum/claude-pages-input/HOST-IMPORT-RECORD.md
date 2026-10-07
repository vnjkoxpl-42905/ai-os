# Host handled the blocked snapshot import

2026-10-03. Claude's headless shell-copy/import commands were denied by the provider permission layer. No permission setting or bypass was enabled. Claude began importing with its approved Read/Write tools.

Before the host ran the authorized importer, all changed/untracked build files were compared with the frozen snapshot. An initial strict hash check rejected five differences. A second text comparison verified that every difference was CRLF versus LF only; there were no builder revisions yet. The host then ran import_snapshot.py, importing all40 hash-verified current files into the authorized isolated checkout. No file deleted or committed. This is host setup/authorship, not Claude-authored changes. The original working checkout and raw inputs were unchanged. Subsequent application revisions remain Claude-owned.
