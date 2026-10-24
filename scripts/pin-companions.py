#!/usr/bin/env python3
"""Pin each companion plugin in marketplace.json to the latest commit on its default branch.

Usage: scripts/pin-companions.py [name ...]   (no names = all companions)
Review the diff and test an install before committing.
"""
import json
import subprocess
import sys
from pathlib import Path

MARKETPLACE = Path(__file__).resolve().parent.parent / ".claude-plugin" / "marketplace.json"


def repo_url(source):
    repo = source.get("repo") or source.get("url")
    return repo if "://" in repo or repo.startswith("git@") else f"https://github.com/{repo}"


def head_sha(url):
    out = subprocess.run(["git", "ls-remote", url, "HEAD"], check=True, capture_output=True, text=True).stdout
    return out.split()[0]


def main(names):
    data = json.loads(MARKETPLACE.read_text())
    for plugin in data["plugins"]:
        source = plugin["source"]
        if not isinstance(source, dict) or (names and plugin["name"] not in names):
            continue
        sha = head_sha(repo_url(source))
        if source.get("sha") != sha:
            print(f"{plugin['name']}: {source.get('sha', '(unpinned)')[:12]} -> {sha[:12]}")
            source["sha"] = sha
    MARKETPLACE.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main(sys.argv[1:])
