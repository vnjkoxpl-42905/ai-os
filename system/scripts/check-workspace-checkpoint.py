#!/usr/bin/env python3
"""Read-only verifier for the workspace redesign checkpoint."""
from __future__ import annotations
import argparse
from dataclasses import dataclass
import os
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
DEFAULT = ROOT/'brainstorms/2026-11-14-workspace-redesign-checkpoint.md'

@dataclass(frozen=True)
class Finding:
    check: str
    state: str
    detail: str


def field(text, label):
    pattern = r'^- \*\*' + re.escape(label) + r':\*\*\s*(.*?)\s*$'
    matches = re.findall(pattern, text, re.M)
    return matches[0] if len(matches) == 1 else None


def parse(text):
    checkout = field(text, 'Canonical repository and actual checkout')
    revision = field(text, 'Branch and observed HEAD')
    writer = field(text, 'Active writer')
    if not checkout or not revision or not writer:
        return None
    match = re.match(r'^\s*\x60?([^,\x60]+)\x60?\s*,\s*\x60?([0-9a-fA-F]{40}|[0-9a-fA-F]{64})\x60?(?:\s*,|\s*$)', revision)
    if not match:
        return None
    return checkout.strip().strip(chr(96)), match.group(1).strip(), match.group(2).lower(), writer.strip()


def git(checkout, *args):
    env = dict(os.environ)
    env.update({'GIT_OPTIONAL_LOCKS': '0', 'GIT_TERMINAL_PROMPT': '0'})
    try:
        return subprocess.run(['git', '-C', str(checkout), '-c', 'core.fsmonitor=false', '-c', 'gc.auto=0', *args],
                              capture_output=True, text=True, env=env, timeout=15)
    except (OSError, subprocess.TimeoutExpired):
        return None


def verify(path):
    try:
        text = path.read_text(encoding='utf-8')
    except OSError:
        return [Finding('Checkpoint', 'failed', 'Checkpoint cannot be read.')]
    except UnicodeError:
        return [Finding('Checkpoint', 'failed', 'Checkpoint is not valid UTF-8.')]
    values = parse(text)
    if values is None:
        return [Finding('Checkpoint', 'failed', 'Required fields are absent, duplicated, or do not include a full HEAD.')]
    checkout, expected_branch, expected_head, writer = values
    findings = [Finding('Checkpoint', 'pass', 'Required fields parsed.')]
    if writer.casefold() == 'yielded':
        findings.append(Finding('Ownership', 'pass', 'The record explicitly says Yielded.'))
    else:
        findings.append(Finding('Ownership', 'failed', 'Ownership is not explicitly Yielded; do not take over.'))
    directory = Path(checkout)
    if not directory.is_absolute() or not directory.is_dir():
        findings.append(Finding('Checkout', 'failed', 'The recorded checkout is not an existing absolute directory.'))
        return findings
    top = git(directory, 'rev-parse', '--show-toplevel')
    if top is None or top.returncode != 0:
        findings.append(Finding('Checkout', 'unknown', 'Git could not inspect the recorded directory.'))
        return findings
    try:
        matches_root = Path(top.stdout.strip()).resolve() == directory.resolve()
    except OSError:
        matches_root = False
    if not matches_root:
        findings.append(Finding('Checkout', 'failed', 'The recorded directory is not the Git worktree root.'))
        return findings
    findings.append(Finding('Checkout', 'pass', 'The recorded directory is a Git worktree root.'))
    head = git(directory, 'rev-parse', '--verify', 'HEAD')
    if head is None or head.returncode != 0:
        findings.append(Finding('HEAD', 'unknown', 'Git could not resolve HEAD.'))
    elif head.stdout.strip().lower() == expected_head:
        findings.append(Finding('HEAD', 'pass', 'Current full HEAD matches the checkpoint.'))
    else:
        findings.append(Finding('HEAD', 'failed', 'Current full HEAD differs from the checkpoint.'))
    branch = git(directory, 'symbolic-ref', '--quiet', '--short', 'HEAD')
    if branch is None or branch.returncode not in (0, 1):
        findings.append(Finding('Branch', 'unknown', 'Git could not determine the current branch.'))
    else:
        actual = branch.stdout.strip() if branch.returncode == 0 else 'detached'
        if actual == expected_branch:
            findings.append(Finding('Branch', 'pass', 'Current branch matches the checkpoint.'))
        else:
            findings.append(Finding('Branch', 'failed', 'Current branch differs from the checkpoint.'))
    return findings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('checkpoint', nargs='?', type=Path, default=DEFAULT)
    args = parser.parse_args()
    findings = verify(args.checkpoint)
    for item in findings:
        print(f'{item.state.upper()}: {item.check}: {item.detail}')
    print('Working-tree status, native chat identity, and actual writer activity were not verified.')
    return 0 if all(item.state == 'pass' for item in findings) else 1

if __name__ == '__main__':
    raise SystemExit(main())
