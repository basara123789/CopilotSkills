---
name: security
description: Apply practical application security reviews and secure-by-default changes.
---

# security

Use when the user asks for security work.

## Workflow
1. Map trust boundaries and sensitive assets.
2. Check input validation, auth/authz, secret handling, injection risks, dependencies and logging.
3. Recommend least privilege and safe defaults.
4. Never put secrets in code or logs.
5. Validate the fix with tests.

## Verification
State which checks were executed, what passed, and what could not be verified. Favor existing project conventions. Use local resources; do not require network access merely to read this skill.
