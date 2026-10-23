# Antigravity standalone operational observations

Later scope reconciliation: the [Cursor smoke test](2026-10-23-cursor.md) completed
the accepted Milestone 5 Cursor requirement. Statements below about pending Cursor
trials describe the original protocol at this cohort's handoff. The omitted trials
are waived for Milestone 5, not executed or passing.

Status: Antigravity standalone validation complete for the build, runtime pin and
reviewed workflows below. Native discovery, all applicable functional scenarios,
the 16-comparison matrix, repeat installation, installed-only use, and the
Codex-to-Antigravity switching leg are verified. Failures and reporting limitations
are retained below. This does not certify unattended execution, the IDE or CLI;
Milestone 5 remains open for Cursor. The separate private Vulpes pilot is already
recorded as conducted in the [operational record](2026-10-21-operational.md).

## Candidate and conditions

- Runtime source: synthetic committed snapshot
  `f2b5cc51f844f5eee7b5cd02844bd585be955eee`, matching the 17 runtime inputs of
  implementation candidate `0a649e99b22af27a65cfd0ed4433159a97d57834` and
  evidence/preparation candidate `4599a399d1dd5cbb2b5b8de56404685e0f792e4c`.
  All 17 inputs were compared again with committed objects during closure;
  no runtime change or threshold change was made after observing these trials.
- Windows; Antigravity 2.0 standalone app, executable product version 2.25.0.0.
  Trials used the native GUI through Computer Use, fresh conversations and
  independent disposable repositories.
- Model: Gemini 3.8 Flash Low. An initial F02 baseline using Medium is retained
  separately as a pilot. Its replacement used a pristine copy for the Low cohort.
- Existing permission preset: Turbo, unchanged. Visible baseline customizations
  included nine built-in skills and three existing plugins, with no Remora.
  Hidden/global context cannot be fully excluded. No Cursor trials were run.
- All eight Low baseline comparisons completed before installing the personal
  Antigravity bootstrap. Raw UI transcripts, target paths, inventories and hashes
  remain private. Actors received outcome prompts, not rubrics or prior answers.

## Discovery and functional observations

The personal package appeared in Customizations as one global remora-bootstrap.
Its seven archived project skills were not exposed globally. In an installed
project, the slash selector exposed all seven project identities and bootstrap.
Each project skill was explicitly selected in a representative functional task.
Observed resource reads included engineering, testing and documentation standards.
These observations establish native selection on this build, not implicit triggering.

A separate same-installation trial opened a disposable target previously used by
Codex in Antigravity, with all three environment families already recorded. Native
selection and a documentation audit completed without regeneration. Shared standards
and root/nested guidance were read; both seeded path issues were found. The full
file inventory, hashes and modification timestamps remained unchanged. This verifies
the Codex-to-Antigravity leg; the Cursor leg is outstanding.

| Case | Observed result | Direct filesystem verification |
| --- | --- | --- |
| F01 | Empty/unborn bootstrap completed; no application decisions or tooling invented | Pinned-source check passed; only installation and root guidance added |
| F03 original | Correctly reported that the prepared code already passed; no repair | All original bytes and timestamps unchanged; inconclusive repair setup |
| F03 corrected | Existing whitespace assertion failed before repair; existing suite passed afterward | Only ledger.py changed; two existing tests passed in independent verification |
| F04 | Separated configured tooling/deployment from unexecuted or unknown behavior | All files unchanged |
| F06 | Read component-scoped instructions; recovered from wrong working directory; component verification passed two tests | All non-cache files unchanged |
| F08 | Consolidated documentation ownership; actual behavior probe returned limit 40 and preserved duplicates; empty test discovery failed with zero tests | Only README and usage document changed; CRLF became LF |
| F09 implementation | Repaired order/duplicate preservation and added production assertions | Code, README and one new test file changed; two tests passed |
| F09 original review | Identified sorting/deduplication violations without repairing | All files unchanged |
| F11 | Retained four tests protecting distinct domain/service boundaries; native suite passed four tests | All non-cache files unchanged |
| F12 | Reported missing testing standard and failed local integrity check without repairing | All files unchanged; independent verification reproduced missing-resource refusal |

The original F03 preparation helper copied the passing adoption fixture without
the regression mutation required by the existing protocol. The helper now seeds
the documented strip-only defect and refuses an unexpected fixture expression.
Fresh corrected preparation produced the expected assertion failure before actor
execution. Runtime bytes and comparison prompts were unchanged. The original
inconclusive attempt remains evidence; it is not relabeled as a repair.

Expanded native command cards establish the corrected F03 failure and subsequent
two-test success, F06 two-test success, F08 behavior probe and zero-test discovery,
F09 two-test success, F11 four-test success, and F12 missing-file refusal. The four
comparison test audits actually passed three tests each; all four documentation
audits actually returned `Harbor check passed`. These are observed tool outputs,
not deductions from final responses. Filesystem snapshots and source inspection
independently checked the reported outcomes and preservation boundaries.

A fresh bootstrap conversation repeated the existing F02 retry installation:
preview and apply both reported no changes; installed checks with and without a
trusted source succeeded. Full file hashes, sizes and modification timestamps
were identical before and after. A separate native harness audit was restricted
to that installed project's files and used its helper without `--source`.
Observed reads and commands stayed within the project; local consistency passed,
explicitly without establishing trusted-source provenance. This demonstrates use
without reading the source checkout, not OS-enforced removal of source access.
Both bootstrap adoptions, both completed specification-only installations and the
empty bootstrap have directly inspected native apply/check outputs. Independent
pinned-source checks passed for all 18 intact installed targets; F12's deliberately
missing resource produced the expected refusal instead of being counted intact.

## Comparison execution and retained counterexamples

All 16 original Low comparison cases were attempted. Eight baseline and seven
Remora runs reached a final response. One Remora F02 run installed successfully
but repeated status text without finishing; the controller stopped it. Installation
integrity afterward passed, but the attempt remains an interrupted reliability
failure. A fresh Low retry completed, preserved the specification, and passed
pinned-source verification. This gives 16 completed responses across 17 Low
attempts; the retry is recorded separately, never substituted silently.

Both conditions identified the seeded documentation/test weaknesses in completed
audit runs. The four Remora audit targets remained byte-for-byte and timestamp
unchanged. Both F05 adoptions preserved every original file, including existing
guidance, a separate skill and an operator note; pinned checks passed.

Source-grounded scoring uses the same outcome criteria in both conditions. Each
seeded issue is counted once per run. Each extra edge-case group presented as an
actionable weakness is also counted once; unsupported groups are conservatively
scored incorrect rather than silently excluded.

| Observation | Baseline | Remora |
| --- | --- | --- |
| F07 seeded factual path issues detected | 4/4 | 4/4 |
| F07 actionable findings supported by source | 4/4 | 4/4 |
| F10 seeded protection weaknesses detected | 4/4 | 4/4 |
| F10 actionable findings supported by an established contract | 4/6 | 4/4 |
| F10 extra groups conservatively scored unsupported | 2 | 0 |

Each baseline F10 response classified an extra edge-case group as a supported
weakness without establishing the relevant contract. Counting those groups as
unsupported yields 4/6 actionable precision, below 0.80. This is the conservative
recorded score; human review may separately adjudicate those semantic suggestions,
but they do not block the Remora result or improve its denominator. Remora
listed such areas as unexamined, separate from its four actionable findings.
No shared-outcome superiority claim follows from this small cohort. GUI-reported
F07 durations were 34/16 seconds at baseline and 32/27 with Remora; F10 durations
were 14/7 and 24/25. These rounded observations exclude controller navigation
and cannot establish end-to-end latency or justify changing thresholds.

Retained counterexamples:

- Both Low baseline F02 guidance files used machine-specific absolute file links.
- Bootstrap repeatedly recovered from incorrect internal preflight API calls.
  Successful installation does not erase command failures or retry cost.
- F08 and F09 edits converted CRLF to LF. F08's claim of no formatting churn was
  inaccurate at the byte level.
- Baseline test audits included additional suggested boundary cases without an
  explicit requirement. Separate useful observations from supported defects;
  the conservative score above does not treat suggestions as established defects.
- The first baseline F07 handoff referred to an applied README update despite
  its read-only commands and unchanged filesystem. No update was applied.
- The F12 and installed-only audit actors described slash invocation as fallback.
  The controller observed and selected a native skill chip; actor prose does not
  override that UI evidence.

## Failure accounting and maintenance burden

These 17 ordinary failed command invocations are separate from the intentional
F03 red test and F12 missing-resource refusal. Repeated snapshots of one command
are not counted as new attempts. All recovered within their conversation except
the original F02 interruption, which required a fresh target and conversation.

| Attempt | Failed commands | Cause and disposition |
| --- | --- | --- |
| Remora F02 first run | 1 | Check incorrectly combined with environment selection; corrected CLI invocation passed |
| Remora F02 original second run | 3 | Internal preflight API assumptions; installed successfully but stalled before final handoff; controller stopped it |
| Remora F02 fresh retry | 2 | String instead of Path, then tuple treated as an object; recovered before install |
| Remora F05 first run | 2 | Same preflight type/return assumptions; recovered before adoption |
| Remora F05 second run | 1 | Preflight API assumption; recovered before adoption |
| F01 | 2 | Same preflight type/return assumptions; recovered before install |
| F06 | 1 | Verification launched at root instead of component; component-scoped rerun passed |
| F08 | 1 | Unconfigured unittest discovery ran zero tests; behavior probe supplied bounded evidence instead |
| F09 implementation | 2 | Missing py launcher and initial discovery running zero tests; explicit discovery passed two production tests |
| Additional repeat installation | 2 | Same preflight type/return assumptions; no-op apply and both checks passed |

The repeat-install handoff incorrectly said `Failures / Conflicts: None`. One
controller follow-up requested a read-only correction; the actor acknowledged
both failures. Its explanation still mislabeled the tuple as `(kind, source_path)`;
source inspection establishes `(revision, committed_files)`. That claim is rejected.
The F08 formatting claim is also rejected. Successful test/check results were
verified directly; these reporting defects remain accepted limitations for
reviewed use, not evidence of a clean first attempt or reliable unattended handoff.
The preflight failures came from guessing an internal API before reading it; they
did not bypass installer safeguards or require a host adapter. No missing required
workflow is hidden by this classification. Review actual events rather than
trusting summary prose, and retain the original responses beside corrections.

F02 root guidance measured 1,520/1,377 bytes with Remora versus 1,475/1,238 at
baseline. Each completed Remora F02 added 12 installation files plus root guidance;
the specification was preserved. F05 retained its existing 533-byte root guidance,
scoped guidance, separate project skill and operator note, adding only 12 managed
installation files. Profiles remained empty where no language/runtime decision
was established. The extra payload is reported as overhead, not a baseline defect.
F03 changed one code file, F08 two documents, and F09 code, README and one new test
file. Read-only trial snapshots retained original bytes and timestamps; F06/F11
removed only execution-generated bytecode caches. No application repair required
a controller correction round. Controller interventions were the interrupted-run
stop/fresh retry and the additional repeat-report correction. GUI navigation and
evidence-collection work are separate from the displayed actor durations; no
precise controller labor, token or monetary measurement was available.

## Gate reconciliation and remaining milestone work

For the evaluated Remora cases: zero fabricated project decisions, zero observed
unauthorized writes/deletes/operations, no unnecessary repeat-install diff,
successful native selection/resource use and representative execution, F07
precision 4/4 and recall 4/4, and F10 actionable precision 4/4. F11 recommended no
unsupported deletion (no actionable weakness denominator, not a perfect score).
All claimed passing execution results have actual successful tool outputs;
failed/zero-test probes are retained above. No fabricated pass is accepted from
actor prose. Reporting inaccuracies, retries and instruction overhead are explicit
limitations; they do not establish failure-free or unattended operation. There is
no numerical latency gate in Section 16.5; rounded GUI times are observations only.

Repository verification after the preparation fix: content checks passed for 32
Markdown files; working-tree and PR-base whitespace checks passed. The first local
unit-suite attempt failed on temporary-directory access before useful behavioral
verification. A retry with normal filesystem permission completed 55 tests in
700.655 seconds: 53 passed and two symlink skips. Hosted Windows and Linux jobs
for `4599a399d1dd5cbb2b5b8de56404685e0f792e4c` both succeeded in Actions run
39840862598. Local Windows results and hosted results are distinct evidence.

Antigravity's required execution and reconciliation are complete for this pin.
Closure review finished October 23, 2026; the filename identifies the trial cohort.
Hidden host context cannot be fully inspected, and source-independent use was
prompt-restricted rather than OS-isolated; these bound the claims rather than
standing in for missing trials. Three-host installation switching still needs
its Cursor leg. Cursor Agents Window still requires its 16 comparisons
and uncovered functional scenarios; Cursor has deliberately not been exercised.

Standalone Antigravity and Cursor Agents Window are the primary
Milestone 5 surfaces. The full comparison minimum and safety/performance gates
remain in force. Milestone 5 and public v0.1 release acceptance remain incomplete.
