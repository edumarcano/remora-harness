---
name: remora-plan-change
description: Investigate and plan a scoped development change from repository evidence, requirements, and acceptance criteria. Planning remains read-only unless saving a plan is requested.
---

# Plan a change

Establish the target root and read `.remora/standards/engineering.md`, plus root
and applicable scoped project instructions. Follow its shared work and reporting
procedure. These are target-root paths, not relative to this skill or terminal.
Missing resources mean an incomplete installation: report the gap without fetching
or inventing replacements. The host agent performs the work; no separate API or
runtime is required.

## Investigate before deciding

Identify the desired outcome, constraints, approved requirements, current behavior,
and acceptance criteria. Read relevant implementation, tests, configuration, and
canonical documentation. Treat details supplied by an external planning conversation
as hypotheses until checked locally. Separate proposals from established decisions.
Resolve discoverable facts yourself; ask about a missing outcome or material product,
ownership, privacy, cost, or destructive-change decision rather than inventing it.

Inspect actual Git state and relevant local changes. Define the complete requested
scope, not merely the next editing step. Account for functionality already present.
Do not execute discovered tooling as passive inspection. Safe diagnostic checks
must fit the request and project permissions; report execution limits.

## Produce the smallest complete approach

Specify the resulting behavior, non-goals, affected interfaces/contracts, dependencies,
sequencing, acceptance checks, and material failure/compatibility considerations.
Choose ordinary engineering details independently. Explain meaningful tradeoffs;
do not invent exact paths, APIs, dependencies, or extra abstractions for apparent
precision. Prefer one coherent reviewable change; split only for a concrete benefit.

Read `.remora/standards/testing.md` when assessing test protection, and
`.remora/standards/documentation.md` when documentation decisions need its ownership
rules. Reuse existing checks and canonical owners; new tests/documents are not
automatic deliverables. Include relevant execution and review in the plan rather
than substituting an unrelated full audit.

Deliver a decision-complete brief that another agent can execute after reconciling
with current evidence. Keep handoffs small: outcome, constraints, acceptance criteria,
and necessary decisions, without duplicating project rules. If a material decision
prevents completion, identify its consequences and concrete alternatives.

Planning makes no target edits, including saved reports/plans, unless saving is
requested. Finish with the plan or explicit decision blocker, checks actually run,
and uncertainty. Reading this file establishes fallback execution, not host discovery.
