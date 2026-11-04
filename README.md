# CopilotSkills — VS Code GitHub Copilot Agent offline skills

A curated **offline-first** collection of 12 self-contained GitHub Copilot Agent skills located at `.github/skills/<name>/SKILL.md`. These 12 are available without internet once cloned.

## Included
| Skill | Purpose |
|---|---|
| frontend-ui-engineering | UI components, layouts, interaction states |
| debugging | Reproduce, isolate, repair defects |
| code-review | Review reliability, changes, maintainability |
| performance | Measure and improve bottlenecks |
| security | Apply safe engineering and threat modeling |
| python-testing | pytest and regression coverage |
| python-error-handling | Exception and recovery design |
| e2e-testing | Browser integration tests |
| accessibility | Keyboard, semantics, WCAG considerations |
| react-state | Predictable React state management |
| ci-cd | Reliable CI validation and deployments |
| docs-adr | Architecture decision records and docs |

## Use
Clone/open this repository in VS Code; Agent mode should detect repository-local skills as needed. To use skills **in another project**, copy the relevant `.github/skills/<skill>/` directory into that project's `.github/skills/`. An unrelated repo is not automatically loaded globally.

Example: "Use the python-testing skill to add pytest regression tests for this Flask route, without external network calls."

## Selected upstream references (optional)
`selected-upstream.json` tracks 14 original `SKILL.md` sources selected from:
- [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) — MIT; 8 selected
- [wshobson/agents](https://github.com/wshobson/agents) — MIT; 6 selected

**All 14 selected original `SKILL.md` files have now been copied into `vendor/` in GitHub**, alongside both upstream MIT LICENSE files and three identified linked reference documents. No local download is required. These vendored files are stored as an offline archive; they are not auto-discovered as project skills until installed under `.github/skills/` or a supported personal skills location. The optional `scripts/vendor_upstream.py` can refresh the copies later, but is not needed for initial use. Some instructions may depend on optional tooling not shipped here.

The other three projects reviewed were [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) (MIT), [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) (Apache-2.0 top level), and [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) (MIT). These were not copied: their primary artifacts are agent personas, plugins, and example apps rather than directly portable Copilot skills.

## Offline constraints
These skills are text instructions and require no package downloads to read. The model/VS Code environment may still need its normal Copilot connection; "offline" means **the skill files themselves are local**, not that Copilot's model inference runs offline.

This repo is a selection, not a mirror or derivative claiming authorship of upstream works.
