# Codex Windows runner setup

**Date:** 2026-11-14
**Tags:** tooling

## Summary

Codex appended the requested network and shell settings after creating a dated backup. Both sandbox probes reached PyPI with HTTP 200. Test b used the runner's legacy `workspace-write` flags with approval disabled. All five PATH checks and the file hash check passed. The temporary script was removed.

## Open threads

The requested setup and checks are complete. The transcript records non-blocking PowerShell and plugin warnings.

## Handoff prompt

```text
Read C:/Users/Joshu/dev/ai-os/handoffs/2026-11-14_codex-windows-runner-setup.md for the Windows Codex runner setup and verification. Use the recorded test results as context for the runner work we’re doing. Test b used the runner’s legacy launch flags and returned NET OK 200 without a command-line network override. Treat this as a completed setup report. Leave the Codex configuration alone unless I ask for a change.
```

## Chat transcript

### User

You are setting up this Windows machine so Codex can run with the widest practical access when it is launched by an outside runner. Joshua owns this machine and has explicitly asked for this. Work carefully and verify everything you claim.\
\
BACKGROUND (verified 2026-11-14)\
\- The runner launches Codex with: codex exec -s workspace-write -c approval_policy="never" (the older "legacy" sandbox flags), using Windows sandbox mode mxc. Config: C:\Users\Joshu\\.codex\config.toml. It already has [features] prefer_mxc = true.\
\- Inside that sandbox \`python\` works but \`py\` does not. Network access is OFF, so downloads fail (getaddrinfo failed).\
\- Official docs: https\://learn.chatgpt.com/docs/permissions and https\://learn.chatgpt.com/docs/windows/windows-sandbox\
\- The docs say a profile such as [permissions.open] with extends = ":workspace" and [permissions.open.network] enabled = true turns network on. The built-in profile :danger-full-access removes all local restrictions. The docs also say not to combine default_permissions with the older sandbox_mode or [sandbox_workspace_write] settings, because the older settings win if either is present.\
\
YOUR TASKS, IN ORDER\
1\. Back up C:\Users\Joshu\\.codex\config.toml to config.toml.before-open-access-\<today's date>.bak. Do not delete or rewrite any existing setting. Only add.\
2\. Add exactly these, if they are not already present:\
&#x20;  [sandbox_workspace_write]\
&#x20;  network_access = true\
\
&#x20;  [shell_environment_policy]\
&#x20;  inherit = "all"\
\
&#x20;  [permissions.open]\
&#x20;  description = "Open access for runner-launched builds"\
&#x20;  extends = ":workspace"\
\
&#x20;  [permissions.open.network]\
&#x20;  enabled = true\
&#x20;  Do not set default_permissions. Do not change sandbox_mode, approval settings, trusted projects, plugins, notify, or anything else.\
3\. Confirm the file still parses: python -c "import tomllib;tomllib.load(open(r'C:\Users\Joshu\\.codex\config.toml','rb'));print('parses ok')".\
4\. Test each of these and report the real output. Put the test script in a file first so quoting cannot break it: write C:\Users\Joshu\\.codex\nettest.py containing  import urllib.request; print('NET OK', urllib.request.urlopen('https\://pypi.org/simple/pip/', timeout=15).status)\
&#x20;  a. codex -c windows.sandbox=mxc sandbox --include-managed-config --permission-profile open -- python C:\Users\Joshu\\.codex\nettest.py\
&#x20;  b. codex exec -s workspace-write -c approval_policy="never" --skip-git-repo-check -C C:\Users\Joshu\\.codex "Run python C:\Users\Joshu\\.codex\nettest.py and reply with only its output"\
&#x20;  Test b is the one that matters: it is exactly how the runner launches Codex. If b still says getaddrinfo failed, try adding -c sandbox_workspace_write.network_access=true on the command line, and tell me whether that changes the result. Do not claim the setting works unless b prints NET OK.\
5\. Also report, from inside the sandbox in test b: whether python, git, node, npm and gh are found on PATH, and whether PowerShell's Get-FileHash works.\
6\. Delete C:\Users\Joshu\\.codex\nettest.py when finished.\
\
RULES\
\- Touch nothing outside C:\Users\Joshu\\.codex. Do not install software unless a tool in step 5 is missing; if one is, tell me what is missing and how you would install it, and wait.\
\- Do not use py; use python.\
\- If a step fails, stop and report the exact error. Do not guess.\
\
REPORT\
List every line you added, the backup file name, each test with its real output, and anything that still does not work. Also say plainly whether the runner's launch mode (test b) can now download files.


### Codex

I’ll check the referenced Windows permissions docs and inspect the relevant config settings before making any changes.

### Codex

The backup hash matched the original config, the updated TOML parsed, and test a printed `NET OK 200`. I’ll now test the runner’s legacy launch flags.

### Codex

**Yes. The runner’s legacy launch mode reached PyPI and printed `NET OK 200` in test b.** It succeeded without the `-c sandbox_workspace_write.network_access=true` override.

I created [config.toml.before-open-access-2026-11-14.bak](C:/Users/Joshu/.codex/config.toml.before-open-access-2026-11-14.bak), verified its hash against the original, and confirmed the updated config preserves every original byte. I appended these lines:

```toml
[sandbox_workspace_write]
network_access = true

[shell_environment_policy]
inherit = "all"

[permissions.open]
description = "Open access for runner-launched builds"
extends = ":workspace"

[permissions.open.network]
enabled = true
```

| Check | Observed output |
|---|---|
| TOML parse | `parses ok` |
| Test a, MXC with the `open` profile | `NET OK 200` |
| Test b, `workspace-write` with `approval_policy="never"` | `NET OK 200` |
| PATH under the test b launch flags | `python found`, `git found`, `node found`, `npm found`, `gh found` |
| `Get-FileHash` under the test b launch flags | `SHA256 728C27F394A0B944BF3454BA585809D3803D3A2464F44A76AA33ACCDF571CAC5` |

I deleted `nettest.py` and verified it was gone. No software was installed.

The runner emitted startup warnings about plugin loading and unsupported PowerShell snapshots. The PowerShell profile also reported denied Terminal-Icons cache writes and `The file cannot be accessed by the system` for `oh-my-posh.exe`. The Python probe succeeded in a `-NoProfile` shell.

### User

write what u jsut en me as an md file icna downaldo and it of to claude to givit obe bael to se therustl of your setup 


### Codex

I’ll save the setup report as a Markdown file you can give to Claude.

### Codex

[Download the Windows runner setup report](C:/Users/Joshu/.codex/visualizations/2026/11/15/01a1dd00-1c20-73a2-a277-d27b7bbdb558/codex-windows-runner-setup.md) and attach it to Claude. It includes the exact config changes, test commands, and the verified `NET OK 200` result from the runner’s legacy launch mode.

### User

no carte a chat exprot ot point it owhre it should red it im nto gonto downalod it sned me a prompiitnot wher it ncarad it andsuc h


### Codex

I’ll use the chat-export skill to save the exchange in the vault and give you a prompt that points Claude to the file.
