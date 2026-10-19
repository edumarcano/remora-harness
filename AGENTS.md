# Remora Repository Instructions

## Project

Remora is a portable, agent-native engineering harness for AI-assisted software development.

`docs/product-spec.md` defines the intended product behavior, architecture, scope, and development milestones. Consult it when planning or implementing changes.

The project is initially targeting Codex, Cursor, and Antigravity.

## Engineering

- Inspect the relevant repository state and specification before making changes.
- Prefer the smallest complete solution that satisfies the current requirements.
- Avoid speculative abstractions, premature infrastructure, and unnecessary dependencies.
- Preserve the agent-native, skill-first architecture. Do not introduce a separate agent runtime or independent LLM API dependency without an approved design change.
- Keep shared guidance portable. Introduce environment-specific configuration only when required.
- Distinguish implemented functionality from specifications, proposals, and unverified assumptions.

## Development workflow

- For planning tasks, investigate and propose changes without modifying the repository unless implementation is requested.
- For implementation tasks, follow the agreed scope and applicable specification requirements.
- Add meaningful verification proportional to the behavior being introduced. Avoid tests that merely reproduce implementation details or duplicate existing coverage.
- Review changes for correctness, unnecessary complexity, and documentation impact.
- Keep documentation coherent and current. Prefer updating canonical explanations over appending incremental patches.
- Report validation actually performed, its results, and any remaining uncertainty.

## Development checks

Run from the repository root with Python 3.11+:

- `python tools/check_content.py` checks the documented subset of local Markdown file links. It excludes fixture payloads and does not validate anchors, external URLs, or semantic claims. See `evals/README.md` for its exact scope.
- `python -m unittest discover -s tests` verifies the content checker using isolated temporary files.
- `git diff --check` checks working changes; also run `git diff --check <base>...HEAD` with the actual PR base to cover committed changes.

These checks do not establish native skill discovery or workflow compatibility.

## Project evolution

Remora's own reusable standards and skills will be established during development. Do not assume that planned skills or tooling already exist.

As the harness becomes usable, adopt its validated workflows within this repository without duplicating or unnecessarily replacing existing guidance.
