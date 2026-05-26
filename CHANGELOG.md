# Changelog

## v1.0.0 - 2026-05-26

### Added

- Stage 1–8 runnable learning path for agent loop, RAG/memory, Claude Code harness study, multi-agent coordination, Skills, Browser agent, Eval/safety, and a shippable CLI agent.
- `scripts/bootstrap.sh` for clone-time setup and offline smoke checks.
- `scripts/hub_progress.py` for local stage progress tracking.
- `scripts/scaffold_skill.py` for Cursor Agent Skill scaffolding.
- Stage 7 eval tasks, results generation, trace logs, and HTML report rendering.
- Stage 8 CLI agent with settings, tools, safety gate, trace writer, retry/timeout controls, and smoke tests.
- GitHub issue templates and public guides for 30-day check-ins and good first issues.

### Notes

- Release should be tagged after the clone-ready PR stack is merged into `main`.
- No API key is required for the offline smoke path.
# Changelog

## Unreleased

### Added

- `scripts/bootstrap.sh` — one-shot deps install and stage smoke tests
- `scripts/hub_progress.py` — local stage-1–7 progress tracker CLI
- `scripts/scaffold_skill.py` — Cursor Agent Skill scaffold from eval/lark/minimal templates
- `scripts/check_github_setup.sh` — verify git email / gh auth for contributions
- `scripts/milestone_check.sh` — Fork/Star milestone dashboard via GitHub CLI
- `stage-7/scripts/render_eval_report.py` — HTML eval report generator
- Skill templates: `eval-skill`, `lark-skill`, `minimal-skill`
- GitHub issue templates: good first issue, 30-day check-in
- `docs/talent-plan/` — policy verification, contribution sprint, community launch, milestone review
