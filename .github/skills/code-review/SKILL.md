---
name: code-review
description: Review changes for correctness, security, accessibility, testability, and maintainability.
---

# code-review

Use when the user asks for code review work.

## Workflow
1. Read diff and surrounding context.
2. Prioritize concrete issues by impact and likelihood.
3. Cite exact file and line, reproduction scenario and a repair suggestion.
4. Avoid speculative complaints and style-only noise.
5. Confirm tests and compatibility implications.

## Verification
State which checks were executed, what passed, and what could not be verified. Favor existing project conventions. Use local resources; do not require network access merely to read this skill.
