---
name: remora-review-change
description: Review a named implementation, diff, or exact revision range for supported correctness and requirement findings. Read-only review never applies repairs.
---

# Review the declared change

Establish the target root and explicitly read `.remora/standards/engineering.md`,
plus applicable root/scoped instructions. Follow its shared procedure and reporting
rules. Paths are target-root relative. Missing resources are an incomplete
installation; do not fetch replacements or silently install/update Remora. Use the
host agent without a separate API or runtime.

## Resolve the review surface

Identify the named implementation or actual base/head range, relevant requirements,
and whether staged, unstaged, and untracked changes are included. Do not guess a
branch or release. If surface identity/base is materially ambiguous, ask before
claiming a completed review. An explicitly named implementation can be reviewed
without history; report that limitation. Account for renames, removed paths, and
applicable scoped instructions beyond edited lines.

## Trace behavior and consequences

Read the actual code and affected callers/contracts, not only summaries or changed
lines. Look for concrete incorrect outcomes, integration/error-path problems, and
violations of approved requirements. Explain the trigger, consequence, and precise
location for each actionable finding. Separate suspected issues and missing evidence
from confirmed defects; preferences alone are advisory.

Read `.remora/standards/testing.md` for protection questions and
`.remora/standards/documentation.md` for claim/ownership questions when relevant.
Inspect test production paths and meaningful assertions; passing checks alone
do not establish correctness. Execute only inspected checks permitted by the task,
reporting outcomes and gaps. No dependency installation, controlled faults, or live
operations are implied by review.

Review is read-only: do not repair source, tests, guidance, or documentation, save
reports unless requested, or automatically invoke implementation. A supplied plan
does not expand review authorization. Finish the declared surface with supported
findings, sampling limits, checks actually run, and residual risks. No findings is
valid; it does not mean exhaustive proof. Explicit reading is fallback execution,
not evidence that the host discovered the skill.
