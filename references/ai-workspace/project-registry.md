# Project and checkout registry

Observed 2026-11-14. This is navigation, not a declaration that other working folders are disposable. Verify branch, HEAD and dirty state in the actual checkout before writing.

| Project | Navigation home | Other work |
|---|---|---|
| AI OS | C:/Users/Joshu/dev/ai-os | Own Git repository and project instructions. |
| LSAT U | C:/Users/Joshu/dev/lsatu | Separate C:/Users/Joshu/dev/ai-os-projects/lsatu repository and its registered worktrees remain active/recovery locations. Both roots have the same GitHub remote and unfinished changes. |
| Job Search | C:/Users/Joshu/dev/ai-job-search | Scratch workspaces remain preserved pending task-by-task review. |

The LSAT U navigation home was on main at 258d41b5 and the worktree hub on codex/rc-quality at 7958d032 during inspection. These are point-in-time observations, not claims of cleanliness or current remote freshness. The documented sync covers ai-os and ai-os-projects; do not assume it covers dev/lsatu. Nested automation worktrees remain unverified. The sidebar project ID `3b28914b-43f5-40a0-a8d0-c017d018ffa5`, absent from list_projects, is associated by native chat metadata with `C:/Users/Joshu/dev/ai-os-projects/lsatu-design-11-claude`. The folder exists but Git reports an invalid gitfile; preserve it for recovery and do not treat it as disposable.

The original Codex project/sidebar mapping is preserved in ignored setup/github-sync/state/workspace-redesign-20261114/sidebar-before.json. Temporary registered projects were moved into a separate reversible sidebar section. No project, checkout or native history was deleted. See the [implementation plan](../../brainstorms/2026-11-14-claude-codex-workspace-redesign.md) and ignored tmp/workspace-lsatu-worktrees-2026-11-14.txt for evidence.
