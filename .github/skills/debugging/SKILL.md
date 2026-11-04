---
name: debugging
description: Diagnose code failures systematically and create minimal verified fixes.
---

# debugging

Use when the user asks for debugging work.

## Workflow
1. Reproduce the bug, gather stack traces and exact inputs.
2. Narrow the first failing boundary.
3. Form and test one hypothesis at a time.
4. Fix root cause, add a regression test, and report evidence.
5. Avoid speculative unrelated changes.

## Verification
State which checks were executed, what passed, and what could not be verified. Favor existing project conventions. Use local resources; do not require network access merely to read this skill.
