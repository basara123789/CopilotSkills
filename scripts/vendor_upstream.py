#!/usr/bin/env python3
"""One-time online download of selected upstream files for later offline reference.
Run from anywhere: python scripts/vendor_upstream.py
Only pins single SKILL.md files; review their linked dependencies before enabling.
"""
import hashlib
import json
import pathlib
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "selected-upstream.json").read_text(encoding="utf-8"))
REPOS = sorted({x["repository"] for x in MANIFEST})

def download(repository, path, destination):
    url = f"https://raw.githubusercontent.com/{repository}/main/{path}"
    with urllib.request.urlopen(url, timeout=30) as response:
        data = response.read()
    dest = ROOT / destination
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    print(f"{destination}: sha256={hashlib.sha256(data).hexdigest()}")

def main():
    try:
        for repo in REPOS:
            download(repo, "LICENSE", f"vendor/{repo}/LICENSE")
        for item in MANIFEST:
            download(item["repository"], item["path"], item["destination"])
    except Exception as exc:
        print(f"Download failed: {exc}", file=sys.stderr)
        return 1
    print("Saved selected upstream sources. Review ancillary references before activation.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
