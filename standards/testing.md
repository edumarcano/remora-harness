# Test assurance

Explain what would have to go wrong for a test to fail and why that matters.
Trace a meaningful sample from requirement or behavior, through a plausible
defect and the production path, to an observable assertion and failure signal.
Mark each link as established, inferred, or missing; name the sample and omissions.

Inspect whether setup exercises production code or duplicates its implementation.
Mocks can isolate legitimate external boundaries; they can also replace the very
behavior under examination. Assertions must distinguish correct behavior from
relevant incorrect outcomes. Representation assertions are useful when that
representation is itself a stable contract. Check boundary/error cases,
synchronization, and cleanup where they affect the behavior.

Similar tests can protect different transformations, wiring, persistence, or
lifecycle boundaries. Overlapping coverage and similar wording do not establish
redundancy. Retain uncertain coverage. A deletion recommendation must identify
the lost protection and evidence that it is preserved or no longer required.
Never weaken expectations to agree with a defect.

Keep evidence levels separate: inspection supports a reasoned hypothesis; running
a test establishes that outcome in that environment; a known broken revision or
isolated controlled fault demonstrates detection of that particular defect.
Coverage reports describe execution, not assertion strength. A passing suite
alone does not establish protection or equivalence. Prefer failure before repair
and success afterward when practical; disclose when either is unavailable.

Auditing does not authorize test edits, deletion, generation, or fault injection.
Deliberate faults require explicit authorization and a disposable copy/worktree,
never the active user's tree. Do not install mutation tooling as an audit step.
Recommend retention, a stronger assertion, a missing case, a better owning layer,
or investigation only with a specific behavior and failure signal. No changes
needed is a valid conclusion.
