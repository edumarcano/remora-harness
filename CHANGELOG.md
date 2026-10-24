# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-10-23

### Added
- **Ten specialist workflows:** Installed under `.agents/skills/` for end-to-end development lifecycles (`remora-plan-change`, `remora-implement-plan`, `remora-fix-regression`, `remora-review-change`, `remora-prepare-pr`, `remora-prepare-release`, `remora-remediate-project`, `remora-audit-documentation`, `remora-audit-tests`, and `remora-audit-harness`).
- **Core engineering standards:** Introduced `.remora/standards/engineering.md`, `.remora/standards/documentation.md`, and `.remora/standards/testing.md`, defining core principles, the documentation refactoring threshold, anti-slop rules, reproduction-first defect repairs, and artifact proof.
- **Deterministic installation & lifecycle helper:** Added `helpers/install.py` supporting preview/apply modes, atomic updates with Plan SHA-256 tokens, before-image backups, manifest integrity verification, and safe removal.
- **Standalone bootstrap package:** Added `tools/package.py` to build an inert, self-contained `remora-bootstrap` bundle (`bundle.json`, `payload.zip`) for global host discovery without runtime Git dependencies.
- **Multi-host compatibility:** Validated discovery and execution across OpenAI Codex CLI, Cursor Agents Window / Composer, and Google Antigravity.
- **Evaluation framework:** Added test fixture suite (`evals/fixtures/F01`–`F13`), frozen rubrics in `evals/README.md`, and 11 dated empirical observation records.
- **Repository licensing:** Added standard MIT License.
