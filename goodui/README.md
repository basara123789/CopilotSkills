# GoodUI Free — offline component vault

Source: https://goodui.dev/ · Installation docs: https://goodui.dev/docs/installation · License: https://goodui.dev/legal/license

This directory initially contains **no copied GoodUI components** because this runtime could not download registry JSON directly. The Copilot Skill under `.github/skills/goodui-free/` works offline as a selection/implementation policy, and can use vendored items once they have been synced.

## Sync free items using an internet-enabled environment

```bash
python scripts/sync_goodui_free.py --name resource-timeline
```

The tool accepts only names in `goodui/free-allowlist.json`; items not verified as free should not be added without checking GoodUI's current license and free listing. Downloaded JSON files include the actual component source as registry `files[].content`, but **do not include npm dependencies**.

```bash
git add goodui/free goodui/manifest.json
git commit -m "Vendor GoodUI free registry components"
git push
```

Free is not necessarily dependency-free. The resulting files can be read offline by Copilot; actual execution depends on a local React, shadcn/ui, Tailwind and npm package environment. Do not include any Pro component.
