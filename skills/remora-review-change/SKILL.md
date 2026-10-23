---
name: remora-review-change
description: Review a named implementation, diff, or revision range using independent split-axis analysis (spec fulfillment vs. engineering standards). Read-only review never applies repairs.
---

# Review the declared change

Establish the target root and explicitly read `.remora/standards/engineering.md`,
plus applicable root and scoped project instructions. Follow its shared procedure and
reporting rules. Paths are target-root relative. Missing resources are an incomplete
installation; do not fetch replacements or silently install/update Remora. Use the
host agent without a separate API or runtime.

## Resolve the review surface

Identify the named implementation or actual base/head range, relevant requirements,
and whether staged, unstaged, and untracked changes are included. Do not guess a
branch or release. If surface identity/base is materially ambiguous, ask before
claiming a completed review. An explicitly named implementation can be reviewed
without history; report that limitation. Account for renames, removed paths, and
applicable scoped instructions beyond edited lines.

## Execute split-axis review

Read the actual code and affected callers/contracts, not only summaries or changed
lines. Formally evaluate the diff across two strictly independent axes:

### Axis 1: Specification and requirement fulfillment
- **Outcome verification:** Did the change actually deliver the agreed outcome and
satisfy all acceptance criteria?
- **Contract & edge-case compliance:** Are public interfaces, boundary conditions,
and error handling respected? Are non-goals preserved?
- **Blocking gate:** An issue on Axis 1 is a **blocking defect**. Beautiful code
that builds the wrong feature or misses edge cases must be rejected.

### Axis 2: Engineering standards, architecture and anti-slop
- **Foundational thinking:** Are data structures, types, and module seams sound?
- **Model the domain:** Is the logic free of boolean soup? Are state lifecycles
modeled cleanly with explicit states or lookup tables?
- **Proportional simplicity (anti-slop):** Is the code free of unnecessary wrappers,
speculative abstractions, dead code, or redundant comments that merely restate code?
- **Test assurance:** Read `.remora/standards/testing.md`. Does testing include
meaningful assertions and real artifact proof rather than shallow mocks?
- **Paid & external boundaries:** Are external/paid calls properly protected or
declared unverified?

## Report findings and boundaries

Review is read-only: do not repair source, tests, guidance, or documentation, save
reports unless requested, or automatically invoke implementation. A supplied plan
does not expand review authorization.

Structure the review report with findings clearly categorized by Axis 1 and Axis 2.
For each actionable issue, provide the trigger, consequence, and exact file location.
Conclude with a clear verdict: **Blocked** (unmet requirements or contract flaws on
Axis 1) or **Approved with optional observations** (Axis 1 satisfied; minor Axis 2
hygiene suggestions). No findings is valid; it does not mean exhaustive proof.
