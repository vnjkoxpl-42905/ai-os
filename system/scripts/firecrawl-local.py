"""Run Firecrawl with its saved AI OS key, without exposing unrelated secrets."""
from pathlib import Path
import os
import shutil
import subprocess
import sys


def main() -> int:
    command = shutil.which("firecrawl")
    if not command:
        raise SystemExit("Firecrawl CLI is not on PATH.")
    env = os.environ.copy()
    if not env.get("FIRECRAWL_API_KEY"):
        source = Path(__file__).resolve().parents[2] / ".env"
        for raw in source.read_text(encoding="utf-8-sig").splitlines():
            line = raw.strip()
            if line.startswith("export "):
                line = line[7:]
            if line.startswith("#") or "=" not in line:
                continue
            name, value = line.split("=", 1)
            if name.strip() == "FIRECRAWL_API_KEY":
                env[name.strip()] = value.strip().strip('"').strip("'")
                break
    if not env.get("FIRECRAWL_API_KEY"):
        raise SystemExit("No saved Firecrawl API key is available.")
    return subprocess.run([command, *sys.argv[1:]], env=env, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
