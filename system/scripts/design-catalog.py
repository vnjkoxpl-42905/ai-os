"""Stable entry point for the audit-backed design registry renderer."""
from pathlib import Path
import runpy

if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).with_name("design-registry.py")), run_name="__main__")
