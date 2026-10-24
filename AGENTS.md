# Remora Repository Instructions

## Project

Remora is a portable, agent-native engineering harness for AI-assisted software development.

`docs/product-spec.md` defines the intended product behavior, architecture, scope, and development milestones. Consult it when planning or implementing changes.

The project is initially targeting Codex, Cursor, and Antigravity.

## Engineering standards and workflows

Before planning or implementing changes, read:
- `.remora/standards/engineering.md` for core engineering principles, mentoring posture, and shared work procedures.
- `.remora/standards/documentation.md` for documentation coherence, the refactoring threshold, and anti-slop rules.
- `.remora/standards/testing.md` for artifact proof, test assurance, and defect reproduction rules.

Remora workflows are installed under `.agents/skills/` (such as `remora-plan-change`, `remora-implement-plan`, `remora-review-change`, `remora-fix-regression`, `remora-prepare-pr`, and `remora-remediate-project`). Use installed skills for engineering tasks.

## Non-goals and operational boundaries

- **No independent runtime or daemon:** Remora is skill-first and runs inside the host agent. Do not introduce a background daemon, server, or mandatory service.
- **No external LLM API dependency:** Do not add direct LLM API calls, credentials, or third-party model routing. Reasoning belongs to the host environment's agent.
- **No speculative dependencies:** Use Python standard library for helpers. Avoid third-party package dependencies without explicit approval.
- **Reproduction-first repairs:** Every bug fix requires demonstrating the failure before modifying production code. If reproduction is genuinely blocked, follow the explicit fallback protocol in `.remora/standards/testing.md`.
- **Preserve project guidance and unrelated files:** Never modify unrelated source files, tests, documentation, or custom project skills.

## Development workflow

- For planning tasks, investigate and propose changes without modifying the repository unless implementation is requested.
- For implementation tasks, follow the agreed scope and applicable specification requirements.
- Add meaningful verification proportional to the behavior being introduced. Avoid tests that merely reproduce implementation details or duplicate existing coverage.
- Review changes for correctness, unnecessary complexity, and documentation impact.
- Keep documentation coherent and current. Prefer updating canonical explanations over appending incremental patches.
- Report validation actually performed, its results, and any remaining uncertainty.

## Development environments

- Windows is the primary local development environment.
- Prioritize running and validating changes on Windows using available local tooling.
- Preserve cross-platform compatibility for Remora's portable skills and deterministic helpers.
- Use GitHub Actions to verify Linux compatibility; a local Linux environment is not required for development.
- Distinguish local verification from hosted CI results. Investigate failures on either platform rather than weakening or removing checks simply to obtain a passing result.
- Do not introduce platform-specific infrastructure without a demonstrated need.

## Development checks

Run from the repository root with Python 3.11+:

- `python tools/check_content.py` checks the documented subset of local Markdown file links. It excludes fixture payloads and does not validate anchors, external URLs, or semantic claims. See `evals/README.md` for its exact scope.
- `python -m unittest discover -s tests` verifies the content checker and installation helper using isolated temporary files and repositories.
- `python .remora/helpers/install.py --check --target .` verifies local self-hosting manifest and hash consistency. Add `--source .` to verify against pinned repository sources.
- `git diff --check` checks working changes; also run `git diff --check <base>...HEAD` with the actual PR base to cover committed changes.

These checks do not establish native skill discovery or workflow compatibility.
