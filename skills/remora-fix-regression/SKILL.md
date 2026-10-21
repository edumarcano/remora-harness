---
name: remora-fix-regression
description: Diagnose a reported failure or repair a regression through production-path evidence and proportional before/after verification. Diagnosis-only requests remain read-only.
---

# Diagnose or repair a regression

Establish the target root and read `.remora/standards/engineering.md` and
`.remora/standards/testing.md`, plus applicable root/scoped project instructions.
These are target-root paths. Follow the shared procedures using host-native tools;
missing resources are installation gaps, not permission to fetch replacements or
use another inference runtime.

## Establish the failure and permitted action

Distinguish diagnosis-only from an authorized repair. Diagnosis makes no source,
test, configuration, or report edits. A repair request permits the smallest complete
fix and necessary test/documentation changes, without another routine approval.
Neutral continuations do not broaden that scope.

Identify observed failure, expected behavior and its authority, affected environment,
revision/local changes, and available reproduction. Inspect the actual command
before running it. Trace the production path, inputs, transformations, boundaries,
and observable failure; distinguish a supported cause from a hypothesis. A missing
tool or inaccessible environment is an evidence gap, not a fabricated reproduction.

Prefer a failing existing test or narrow safe reproduction before editing. Historical
revisions can be inspected or exercised in disposable copies; do not reset the active
tree. Deliberate faults require separate explicit authorization and isolation. Do
not install dependencies or contact live services merely to reproduce a report.

## Repair when requested

Fix the supported cause while preserving unrelated behavior. Keep existing failure
signals and add a regression test only if meaningful protection is missing. Do not
change the approved specification or weaken expectations to agree with the defect.
For documentation impact, read `.remora/standards/documentation.md` and update its
existing owner only where necessary.

Run the reproduction and relevant checks after repair. Record failure before and
success afterward when practical, naming the exact check and production behavior;
otherwise explain which evidence is unavailable. Explicitly review the actual diff
and changed/untracked inventory against scope. Correct supported in-scope issues
and rerun affected checks, stopping at verified repair or an explicit blocker.

Report cause/confidence, evidence, repair rationale, retained or added protection,
actual outcomes, and residual uncertainty. A diagnosis may finish with no change
and a concrete next diagnostic step. Do not claim native discovery from this file.
