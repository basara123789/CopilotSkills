---
name: ci-cd
description: Build reliable continuous integration workflows and safe deployment processes.
---

# ci-cd

Use when the user asks for ci cd work.

## Workflow
1. Identify supported environment and trust boundaries.
2. Separate lint, tests, build and deploy.
3. Pin dependencies appropriately, scope credentials and avoid exposing secrets.
4. Add caching only when safe.
5. Ensure failure stops deployment and document rollback.

## Verification
State which checks were executed, what passed, and what could not be verified. Favor existing project conventions. Use local resources; do not require network access merely to read this skill.
