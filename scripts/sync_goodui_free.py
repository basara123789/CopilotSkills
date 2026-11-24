#!/usr/bin/env python3
"""Download *allowlisted free* GoodUI shadcn registry JSON for offline storage.
Standard-library only; must be run once where goodui.dev is reachable.
"""
import argparse
import json
import pathlib
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
BASE = ROOT / "goodui"
ALLOW = json.loads((BASE / "free-allowlist.json").read_text(encoding="utf-8"))
MANIFEST = BASE / "manifest.json"
OUT = BASE / "free"

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--name", action="append", required=True, help="Free verified registry item name (repeatable)")
    args = p.parse_args()
    names = list(dict.fromkeys(args.name))
    unknown = [n for n in names if n not in ALLOW or ALLOW[n].get("status") != "free-verified"]
    if unknown:
        p.error("Not in verified free allowlist: " + ", ".join(unknown) + ". Verify free status before changing allowlist.")
    downloaded = []
    for name in names:
        url = f"https://goodui.dev/r/{name}.json"
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent":"CopilotSkills-GoodUI-Free/1.0"}), timeout=30) as response:
                raw = response.read(3_000_001)
        except (urllib.error.URLError, TimeoutError) as exc:
            raise SystemExit(f"Cannot retrieve {url}: {exc}")
        if len(raw) > 3_000_000:
            raise SystemExit(f"{name}: file unexpectedly large; inspect manually.")
        data = json.loads(raw)
        if not isinstance(data, dict) or not isinstance(data.get("files"), list):
            raise SystemExit(f"{name}: registry format unexpected; not saved.")
        if not any(isinstance(item, dict) and isinstance(item.get("content"), str) for item in data["files"]):
            raise SystemExit(f"{name}: registry contains no source code; not saved.")
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / f"{name}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
        downloaded.append({"name":name,"registry_url":url,"files":len(data["files"])})
        print(f"Saved goodui/free/{name}.json ({len(data['files'])} files)")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    by_name = {x["name"]: x for x in manifest.get("downloaded_free_components", [])}
    for x in downloaded: by_name[x["name"]] = x
    manifest["downloaded_free_components"] = sorted(by_name.values(), key=lambda x:x["name"])
    manifest["status"] = "contains_vendored_free_components"
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")

if __name__ == "__main__":
    main()
