---
name: goodui-free
description: Implement React and Tailwind UI with GoodUI's free shadcn-compatible components and application blocks; use for dashboards, data tables, scheduling, forms, AI chat UI and polished interfaces. Prefer vendored local free registry components and never use Pro items.
---
# GoodUI Free — offline-first implementation

Use when asked to create or improve React/shadcn UI components or application screens.

## Priority and collaboration
- For appearance, composition, spacing and typography: coordinate with `frontend-ui-engineering`.
- For complex animation: use the separate MotionReference repository only when its files are available in the current workspace.
- For GoodUI: **first inspect the local `goodui/free/` directory and `goodui/manifest.json`**. Never assume an item has been downloaded unless its source code is present.
- If there are no vendored components, explain that this skill provides local design/implementation guidance but **not** GoodUI's original source. Create an original shadcn-compatible component or have the user run the optional online sync tool.
- Use only GoodUI free registry items. Never fetch Pro endpoints, use paid keys or copy Pro code.

## Implementation workflow
1. Understand existing React/Tailwind/shadcn environment; do not force it into Python-only apps or other stacks.
2. Identify the relevant free item and look for its vendored registry JSON in `goodui/free/<item>.json`.
3. Inspect registry `files`, `dependencies`, `registryDependencies` and `cssVars` before implementation. Extract TSX from the `files[].content` entries with expected targets, or adapt code manually.
4. Make package dependencies explicit: local source **does not** bundle npm packages. If offline, use already installed dependencies or implement an original dependency-free alternative.
5. Ensure keyboard accessibility, responsive layout, focus states, dark mode, RTL where needed, and `prefers-reduced-motion`.
6. Test in the target app; note untested behavior and missing dependencies.

## Optional online acquisition
Run `python scripts/sync_goodui_free.py --name resource-timeline` on a networked machine, then review and commit the downloaded JSON. The tool is **not** run automatically and never downloads Pro content.

Official registry: https://goodui.dev/r/{name}.json
Official docs: https://goodui.dev/docs/installation
Agent integration docs: https://goodui.dev/docs/ai
License: https://goodui.dev/legal/license

This is an independently authored Skill, not a copy of GoodUI's official agent pack.
