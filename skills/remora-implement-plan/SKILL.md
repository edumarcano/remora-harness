---
name: remora-implement-plan
description: Implement an approved plan or clear scoped development request, including relevant verification, documentation impact, and explicit diff review.
---

# Implement the agreed outcome

Establish the target root and read `.remora/standards/engineering.md`, plus root
and applicable scoped project instructions. Follow its shared work and reporting
procedure. These paths are relative to the target root. Report missing resources
as an incomplete installation; do not invent or fetch them. Use the existing host
agent and project tools, without an independent runtime or API.

## Reconcile the request with the repository

An approved plan or clear implementation request is sufficient; a separately saved
plan is not mandatory. Establish outcome, boundaries, acceptance criteria, and actual
Git/local state. Recheck supplied paths, APIs, requirements, and dependencies against
current implementation. Preserve project decisions and unrelated changes. Surface
material contradictions before affected edits; resolve ordinary details yourself
and continue safe independent work.

## Implement and demonstrate behavior

Follow the agreed dependencies and complete the requested behavior. Prefer the
smallest sufficient implementation using existing conventions. Do not widen the
milestone, introduce speculative infrastructure, or install dependencies merely
because a plan mentions them. Report blocked acceptance criteria explicitly.

Read `.remora/standards/testing.md` for test decisions. Trace meaningful acceptance
behavior through production paths and assertions. Reuse adequate coverage; add or
improve tests where the change creates a real protection gap. Run relevant inspected
checks within authorization, distinguishing configured commands from execution.
Never weaken a test to bless a defect or fabricate a before/after result.

Read `.remora/standards/documentation.md` when changing explanations or contracts.
Update affected canonical documentation where needed; preserve adequate sections,
approved requirements, and accurate history. Assess surrounding examples and links.
Do not require a separate repository-wide documentation/test audit for a local edit.

Explicitly review the actual diff, including relevant staged, unstaged, and untracked
files, against requirements and acceptance criteria. Use the installed
`.agents/skills/remora-review-change/SKILL.md` for its review procedure; reading and
following it in the current agent is sufficient. Delegation is optional and requires
host/user authorization; review is evidence, not an independent correctness proof.
Fix supported in-scope findings and recheck affected behavior.

Finish with delivered behavior, actual check/review outcomes, remaining risks, and
any unmet acceptance criteria. Do not automatically commit, publish, or perform
external operations. Reading an installed skill proves fallback execution only.
