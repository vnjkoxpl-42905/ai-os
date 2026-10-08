---
type: source
subject: "GitHub source repos/karpathy/nanochat/nanochat/execution.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/nanochat/execution.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/nanochat/nanochat/execution.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/nanochat/nanochat/execution.py), SHA-256 `122ce1457100a5cb20fbe9666a57006df3b0fe78c014240d2f87c35ccade2c1a`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
""" Sandboxed execution utilities for running Python code that comes out of an LLM. Inspired
```

Execution utility clearly distinguishes fresh subprocess, scrubbed environment, memory limits, hard timeout and accidental-destructive-function guards from actual adversarial security: network and ctypes remain unrestricted, and no kernel isolation exists. Default resource import is Unix-specific and macOS intentionally skips limits. Flash attention switches by actual kernel availability and compute dtype, offers testing overrides, handles SDPA GQA and explicit chunk/window masks, and preserves KV insertion interface. Broad loader exceptions silently select fallback; despite causal argument in public API the SDPA helper always applies causal masking for multi-token paths, so full API equivalence is qualified. Cache fallback assumes uniform batch positions. Historical compatibility and timings were not executed.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""
Sandboxed execution utilities for running Python code that comes out of an LLM.
Inspired by the OpenAI HumanEval code:
https://github.com/openai/human-eval/blob/master/human_eval/execution.py

The code runs in a fresh Python subprocess. What is covered:
- Each execution runs in its own process (killed hard by the parent on timeout)
- A fresh interpreter: no access to the parent process memory, and a scrubbed environment
- Memory limits are enforced via rlimits (256MB by default)
- stdout and stderr are captured, stdin is disabled
- Code runs in a temporary directory that is deleted afterwards
- Destructive functions are disabled (examples: os.system, os.kill, shutil.rmtree, subprocess.Popen)

What is not covered:
- Not a true security sandbox
- Network access is not blocked (e.g. sockets could be opened)
- Python's dynamic features (e.g. ctypes) could bypass restrictions
- No kernel-level isolation (no seccomp, no containers, no virtualization)

Overall this sandbox is good for evaluation of generated code and protects against
accidental destructive behavior, but it is not safe against malicious adversarial code.
"""

import subprocess
import sys
import tempfile
from dataclasses import dataclass
from typing import Optional

# -----------------------------------------------------------------------------

@dataclass
class ExecutionResult:
    """Result of executing Python code in a sandbox."""
    success: bool
    stdout: str
    stderr: str
    error: Optional[str] = None
    timeout: bool = False
    memory_exceeded: bool = False


# The guard runs in the subprocess before the untrusted code. It applies the
# resource limits and disables destructive functions to protect against
# accidents (a fork bomb, deleting files, killing other processes, ...).
# It is trivially bypassable by adversarial code, see docstring above.
GUARD = r"""
import faulthandler, builtins, os, shutil, subprocess, sys
maximum_memory_bytes = {maximum_memory_bytes}
if maximum_memory_bytes is not None and sys.platform != "darwin":
    # (the resource limit calls seem to fail on macOS, skip them there)
    import resource
    resource.setrlimit(resource.RLIMIT_AS, (maximum_memory_bytes, maximum_memory_bytes))
    resource.setrlimit(resource.RLIMIT_DATA, (maximum_memory_bytes, maximum_memory_bytes))
    resource.setrlimit(resource.RLIMIT_STACK, (maximum_memory_bytes, maximum_memory_bytes))
faulthandler.disable()
builtins.exit = None
builtins.quit = None
builtins.help = None
os.environ["OMP_NUM_THREADS"] = "1"
for name in ("kill", "system", "putenv", "remove", "removedirs", "rmdir", "fchdir",
             "setuid", "fork", "forkpty", "killpg", "rename", "renames", "truncate",
             "replace", "unlink", "fchmod", "fchown", "chmod", "chown", "chroot",
             "lchflags", "lchmod", "lchown", "getcwd", "chdir"):
    setattr(os, name, None)
for name in ("rmtree", "move", "chown"):
    setattr(shutil, name, None)
subprocess.Popen = None
for name in ("ipdb", "joblib", "resource", "psutil", "tkinter"):
    sys.modules[name] = None
"""


def execute_code(
    code: str,
    timeout: float = 5.0, # 5 seconds default
    maximum_memory_bytes: Optional[int] = 256 * 1024 * 1024, # 256MB default
) -> ExecutionResult:
    """
    Execute Python code in a sandboxed environment.

    Args:
        code: Python code to execute as a string
        timeout: Maximum execution time in seconds (default: 5.0)
        maximum_memory_bytes: Memory limit in bytes (default: 256MB, None to disable)

    Returns:
        ExecutionResult with success status, stdout/stderr, and error information

    Example:
        >>> result = execute_code("print('hello world')")
        >>> result.success
        True
        >>> result.stdout
        'hello world\\n'
    """
    # the guard runs first, then the untrusted code (with fresh globals, as a repr'd literal)
    guard = GUARD.format(maximum_memory_bytes=maximum_memory_bytes)
    program = guard + f"\nexec(compile({code!r}, '<llm>', 'exec'), {{'__name__': '__main__'}})\n"

    with tempfile.TemporaryDirectory() as tmpdir:
        try:
            process = subprocess.run(
                [sys.executable, "-c", program],
                cwd=tmpdir, # writes land in the tempdir, deleted afterwards
                env={"PATH": "/usr/bin:/bin"}, # scrub the environment
                stdin=subprocess.DEVNULL,
                capture_output=True,
                text=True,
                timeout=timeout,
            )
        except subprocess.TimeoutExpired:
            # subprocess.run kills the child process on timeout
            return ExecutionResult(
                success=False,
                stdout="",
                stderr="",
                error="Execution timed out (process killed)",
                timeout=True,
            )

    success = process.returncode == 0
    stderr = process.stderr
    # the last line of the traceback identifies the exception, e.g. "TypeError: ..."
    error = None if success else (stderr.strip().splitlines() or ["Execution failed"])[-1]
    memory_exceeded = "MemoryError" in stderr
    result = ExecutionResult(
        success=success,
        stdout=process.stdout,
        stderr=stderr,
        error=error,
        memory_exceeded=memory_exceeded,
    )
    return result

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
