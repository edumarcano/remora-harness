---
name: remora-prepare-pr
description: Prepare a comprehensive, evidence-backed pull request description and verification summary from the completed Git branch diff.
---

# Prepare a pull request

Establish the target root and explicitly read `.remora/standards/engineering.md`,
plus applicable root and scoped project instructions. Follow its shared procedure and
reporting rules. Paths are target-root relative. Missing resources mean an incomplete
installation; report the gap without fetching replacements. The host agent performs
the work using native tools; no separate API or service is required.

## Resolve the branch change surface

Identify the current branch, target base branch (defaulting to `main` or repository
default), and actual revision range. Inspect the full diff, including staged,
unstaged, and untracked changes, using `git diff <base>...HEAD` or equivalent range
commands. Do not guess commit history.

Reconcile the actual diff with the original requirements, acceptance criteria, and
plan. Verify that all in-scope work packets are complete and that split-axis review
has been satisfied. If uncommitted changes exist, ask whether they belong in the PR
or should be stashed.

## Assemble the pull request brief

Generate a professional, structured PR description containing:

1. **Summary of changes:** Clear explanation of what problem was solved, the
resulting behavior, and the underlying architectural approach. Explain the "why"
behind key design decisions using the Senior Technical Mentor persona.
2. **Empirical verification evidence:** Include real artifact proof (exact commands
executed, CLI stdout snippets, test suite results, exit codes). A passing test
suite alone is not sufficient; show the output of the real executable interface.
3. **Non-goals & boundaries:** Explicitly list what was intentionally left out of
scope to guide reviewer expectations.
4. **Unverified areas & external boundaries:** Disclose any unverified areas,
especially paid external services (such as LLM APIs) or environment-specific checks,
and supply copy-pasteable manual verification steps with expected outcomes for the
reviewer.
5. **Breaking changes & migrations:** Note any modified public contracts, schema
migrations, or configuration adjustments.

## Safety and boundaries

Preparing a pull request description is **read-only**:
- Do not automatically create commits, push branches, open GitHub pull requests via
API, or merge code unless explicitly authorized covering those actions.
- Present the prepared PR description directly in the chat conversation (or save
to an approved file location only when requested).
- Review remaining risks and ask the user for confirmation before any subsequent Git
operations.
