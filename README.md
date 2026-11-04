# CopilotSkills — Offline-first VS Code GitHub Copilot Agent Skills

A curated, **deduplicated set of 12 active Agent Skills** for VS Code GitHub Copilot. All active `SKILL.md` files and their linked local Markdown references are stored under `.github/skills/` for local discovery.

## Active skills

| Skill | Core tasks | Source |
|---|---|---|
| `frontend-ui-engineering` | UI components, responsive design, interaction | addyosmani |
| `code-review-and-quality` | Code review and quality gates | addyosmani |
| `debugging-and-error-recovery` | Root cause analysis, regression fixes | addyosmani |
| `performance-optimization` | Profiling and optimization | addyosmani |
| `security-and-hardening` | Security reviews and secure code | addyosmani |
| `ci-cd-and-automation` | Tests, builds and deployment pipelines | addyosmani |
| `documentation-and-adrs` | Technical docs and architecture decisions | addyosmani |
| `python-testing-patterns` | pytest, mocking and Python test coverage | wshobson |
| `python-error-handling` | Python exceptions, validation and recovery | wshobson |
| `e2e-testing-patterns` | Playwright / Cypress E2E testing | wshobson |
| `wcag-audit-patterns` | WCAG accessibility auditing | wshobson |
| `react-state-management` | React client and server state | wshobson |

**Optional archived originals** in `vendor/` (NOT auto-loaded as skills):
- `browser-testing-with-devtools` — requires Chrome DevTools MCP integration; do not activate without installing/configuring the corresponding MCP server.
- `code-review-excellence` — overlaps with the selected `code-review-and-quality`, intentionally inactive.

## Use in VS Code

Open this repository in VS Code and select GitHub Copilot **Agent** mode. It can discover the 12 skills from `.github/skills/`.

For **another project**, copy the desired skill directory (including its `references/` directory, if any) into that project's `.github/skills/`. A separate repository is **not automatically available** to a different workspace.

Suggested requests:
- "Use the python-testing-patterns skill to write regression tests for my Flask route."
- "Use the frontend-ui-engineering skill to create an accessible dashboard."
- "Use debugging-and-error-recovery to diagnose this traceback, then run tests."

These are locally stored instructions and examples. GitHub Copilot **model inference itself may still require online service access**. Browser automation, testing, CI integrations, and other tools mentioned by a skill also need to be available in the target environment.

## Structure

```text
.github/skills/               # 12 active, distinct Skills
  performance-optimization/references/optimization-patterns.md
  security-and-hardening/references/hardening-patterns.md
  python-testing-patterns/references/advanced-patterns.md
vendor/                       # 14 preserved original Skills and two MIT licenses
selected-upstream.json        # Upstream origin and file paths
scripts/vendor_upstream.py    # Optional future refresh (online only)
```

## License & attribution

The original upstream content is reproduced under the respective MIT licenses, retained in:
- `vendor/addyosmani/agent-skills/LICENSE`
- `vendor/wshobson/agents/LICENSE`

Original sources: [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills), [wshobson/agents](https://github.com/wshobson/agents). `vendor/` preserves all 14 chosen upstream Skills. Their 12 active counterparts have been copied unchanged from the selected sources, plus their three identified linked reference Markdown files.

Other projects considered, **not copied**: [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) (MIT), [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) (Apache-2.0 top level), and [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) (MIT).

No automatic updates are enabled. New upstream changes should be reviewed before synchronization.
