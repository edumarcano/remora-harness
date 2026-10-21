# Development and assurance evidence: October 21, 2026

Milestone 4 adds planning, implementation, regression, review, test-audit, and
harness-audit entrypoints around shared engineering/testing guidance. This record
reports local installed-entrypoint trials and deterministic verification. It does
not establish native discovery, cross-host portability, baseline improvement,
real-project usefulness, or independent human validation.

The [evaluation guide](../README.md) owns tasks, preparation, frozen rubrics, and
recording conventions. The [specification](../../docs/product-spec.md) owns intended
behavior. Semantic judgments below are the implementing agent's review of sources,
actual command events, outputs, diffs, and snapshots; owner adjudication of ambiguous
recommendations remains part of PR review.

## Runtime identities and conditions

The initial candidate was `80dec733f97fa1817edb0e711f7ed3e42880b818`; its minimal
synthetic distribution was `6b12736aeb8476a8601a6be475d2a6d8df3fdade` (V1).
Review tightened the helper's plain-string metadata validation. The final runtime
candidate is `61ab247464054d838e82cc6a31b005cc2f789ef1`, with synthetic distribution
`a7d8085cf262502064e569db8821108073243646` (V2).

Only `helpers/install.py` differs between those runtime distributions. All eight
skill entrypoints, three standards, and the seed have identical Git-object bytes.
The final helper rejects YAML boolean/null-like descriptions and mapping/comment
delimiters in the documented authored subset. Source-dependent harness and bootstrap
cases were repeated under V2; the unchanged development/test/documentation skill
observations retain their V1 installation identity. They are not misrepresented as
V2 sessions. The parent compared all thirteen final inputs against the repository
Git objects. Later test, CI-timeout, and evidence edits do not alter these inputs.

| Final runtime input | Git-object SHA-256 |
| --- | --- |
| `helpers/install.py` | `8ac48701dccbe7ac5e0910f1266d1aeeba8e10f4f825e297bb12f4e0ed730c2f` |
| `standards/engineering.md` | `46b20a4caa564c2f5b6d687fcd53ae5eed1253245b9c1218414dc2e893da82af` |
| `standards/documentation.md` | `3fa96407e8717df3a86b6da01adac123bc9fa1b56bde004c2e498f17db137ae6` |
| `standards/testing.md` | `a901b363f819d8ca0298640e33ac0585861ccc1d95d6483b78d314d10bc21edb` |
| `skills/remora-audit-documentation/SKILL.md` | `1e73a0de3a974993eb8f6beb944632225dc55fd62440614999995f8301b735d9` |
| `skills/remora-plan-change/SKILL.md` | `11a2f57335aef9f6be51f4398fb0999a23c0601339579f6c5448982bbde236aa` |
| `skills/remora-implement-plan/SKILL.md` | `c7757c53d1d2224d5b3750eff7d5f69719d29558345a9f805105c21a8f6aa1f3` |
| `skills/remora-fix-regression/SKILL.md` | `bcc4bcb768c789a32094d8f26218e3959c8f9f587ec45085efcaba492d18c4ce` |
| `skills/remora-review-change/SKILL.md` | `204619f4a67a3f5c026aed53ccbca77319290ec9939c10616a1b5c3fe33a6cdf` |
| `skills/remora-audit-tests/SKILL.md` | `d262617c9e964e1276d6ce7fd755f35f3732fe4b37d669cfa3cd39ea5b6de45c` |
| `skills/remora-audit-harness/SKILL.md` | `b85637c84113effb5b621b1732207cf4934a13a8ad26bab5a06cb8d1cfdaf0d0` |
| `skills/remora-bootstrap/SKILL.md` | `af65dc32c9f27ee17e576dde49be8c01b396d50fae8ed572f2732279b35df3cb` |
| `templates/AGENTS.md` | `7bb1dc2e05cabeda460f0e6b3ac726f4e61f4a1808f5e31931c4babd058c97f1` |

Trials used Windows `10.0.26300`, Codex CLI `0.163.0-alpha.11`, Python `3.14.3`,
and the existing host account's configured `gpt-6.1-sol` with high reasoning effort.
No model override or independent API was used. Actors ran with:

```text
codex exec --json --color never --sandbox workspace-write -C <target> -
```

The outer runner required normal filesystem/session access. Actors retained the
workspace-write sandbox. Independent cases used at most two concurrent sessions
per cohort; the linked loop and bootstrap repetitions remained sequential. The
first installed-skill read was explicitly requested alone. Scorer guides, records,
calibration outputs, and prior answers were excluded from targets and distributions;
only the intended plan handoff crossed the linked loop's fresh sessions. Personal
guidance and memory remained available, and some actors searched memory. These
are development trials, not blind holdouts. Raw events/prompts and snapshots remain
private; no transcripts or personal paths are published here. Cost was unavailable;
times below are actor wall time, not human review effort or a cost comparison.

## Preparation and independent controls

The runner copied complete fixture inputs and installed/checked the pinned payload
before actor work. Synthetic commits disabled hooks/signing and used LF inputs.
Each existing-project target retained a local README appointment note and untracked
`notes/local.txt`. Full file hashes, sizes, and modification times were recorded
outside Git metadata and expected Python bytecode caches. Root/scoped guidance,
requirements, and managed content remained outside implementation edit scope.

The frozen fault controls ran before agent trials: F10 baseline and a sorted-output
fault both passed three tests; strip-only normalization failed its meaningful
whitespace assertion. F11 baseline passed four tests; raw service output and changed
error mapping failed their respective service checks while domain tests passed.
Constructed rubric cases were reviewed as consistency checks, not measured actor
performance or independent human calibration.

The parent independently ran the implementation's nine new F09 tests against the
original production function: five failed and four passed. Against the repaired
function all nine passed. Parent execution also reconfirmed F03's existing failure
before repair and both tests passing afterward. These are specific production-path
signals, not test-count or coverage-based claims.

## Development and test-assurance observations

| V1 operation | Seconds | Actual changes or result |
| --- | ---: | --- |
| F09 planning | 64.35 | No changes; grounded repair and acceptance plan |
| F09 implementation | 77.40 | Function, current README, and new `test_queue_labels.py`; five failures before, nine passes after |
| F09 corrected review | 54.36 | No changes or invented correctness findings; nine passing tests |
| F09 original-implementation review | 48.58 | No changes; both sorting and duplicate-loss violations found |
| F03 diagnosis | 40.55 | No changes; existing test reproduces internal-whitespace defect |
| F03 repair | 63.96 | Only `ledger.py`; existing failure repaired, two tests pass, no redundant test added |
| F10 inspection-only audit | 71.06 | No changes; fake/production disconnect and length-only assertion identified |
| F10 authorized fault audit | 128.56 | Active target unchanged; order/duplicate loss escape, whitespace/cardinality faults detected |
| F11 inspection-only audit | 62.79 | No changes; all four distinct protections retained |
| F11 authorized fault audit | 223.18 | Active target unchanged; four defects detected, inline-delegation bypass escapes |
| F07 documentation smoke | 64.44 | No changes; both current-path seeds found, history retained, configured check passes |

For the linked review, the runner committed the production repair into an exact
base..head range; the corrected README and new tests remained local changes,
explicitly included in review alongside unrelated notes. The reviewer inspected
all those surfaces and disclosed that the test was untracked, rather than claiming
it belonged to the committed range. No actor committed anything.

F10 inspection found both seeded actionable weaknesses: provisional precision
**2/2**. The fault audit found those two and an additional supported input weakness:
the fake's `b, a, b` sequence is symmetric, so connecting that assertion to production
alone still would not distinguish reversal. Counting conceptual causes rather than
bullet headings gives **3/3** correct actionable weaknesses. Both operations meet
the frozen 0.80 target; optional unexamined input suggestions are advisory rather
than extra scored defects. Both retained the sound whitespace assertion.

F10's actor used unchanged tests in disposable copies. Reversal and duplicate removal
each passed all three tests; skipping normalization failed the whitespace test;
dropping the last label failed the length and whitespace tests. The target remained
unchanged. These observations support only those sampled faults.

F11 had no unsupported deletion recommendation. Its actor demonstrated distinct
domain and service failure signals and retained all four tests. It also identified
a legitimate extra gap: fixture guidance explicitly requires the service to call
domain normalization, but equivalent inline implementation passes all four tests.
That control is adequate for the distinct boundaries measured, not a flawless
suite. The proposed focused delegation assertion is supported by that explicit
requirement and the controlled escape, not a universal demand to assert internal
calls. Exact error assertions protect the fixture's stated stable response.
Additional edge-case suggestions remain advisory and subject to owner review.

## Final source-dependent observations

Twenty logical scenarios completed in 29 fresh actor sessions: twenty at V1,
then nine source-dependent repeats at V2. The V2 cohort was:

| V2 operation | Seconds | Actual result |
| --- | ---: | --- |
| harness-clean | 125.97 | Pinned check 0; no actionable defect; no changes |
| harness-missing | 169.36 | Pinned check 1; testing standard missing; no changes |
| harness-drift | 158.70 | Pinned check 1; documentation standard modified; no changes |
| harness-malformed | 121.81 | Pinned check 1; malformed manifest; no changes |
| harness-unsafe | 137.06 | Pinned check 1; unsafe inventory rejected; no changes |
| harness-overlap | 94.08 | Pinned check 0; conflicting project review instruction found; no changes |
| harness-no-source | 142.61 | Local consistency only; trusted-source check explicitly not run; no changes |
| Bootstrap first | 132.98 | Twelve files created; no application/tooling invented |
| Bootstrap repeat | 88.71 | Inventory, bytes, and modification times unchanged |

Harness checks distinguished deterministic integrity from semantic ownership and
native-host evidence. The existing Quarry setup workflow remained valid; its
overlap alone was not classified as a defect. The introduced review skill's command
to repair during read-only review was reported as a project-owned guidance conflict,
while managed integrity remained valid. No repairs were attempted. Unsafe manifest
entries were rejected without reading external referents; the parent checked the
external sentinel remained unchanged. Without trusted source, actors reported local
manifest/hash consistency and explicitly withheld pinned-source/provenance success.

Bootstrap first use created ten managed files, the manifest, and project-owned root
guidance with no invented application/tooling. Both generations' fresh-session
repeats preserved inventory, bytes, and modification times. All audit, planning,
review, and diagnosis targets were unchanged outside expected runtime caches.
Implementation and repair changed only their declared surfaces, preserving notes,
requirements, instructions, and installed content. No saved reports, dependency
installation, publication, or live operations occurred.

## Failures, retries, and verification limits

- **Fixed setup error:** the first independent-cohort runner stopped on a Python
  path/string concatenation error before any evaluated actor started. Corrected
  preparation reused untouched targets; it is not an actor failure.
- **Fixed parser gap:** review identified non-string YAML scalar/mapping descriptions
  accepted by the initial narrow validator. Added negative regression cases and
  tightened the authored subset; V2 repeats cover source-dependent workflows.
- **Environment limitation, successfully retried:** sandbox temporary-directory ACLs
  prevented the initial repository suite setup and F11's first disposable-copy
  attempt. The suite ran with normal filesystem access; the actor retried using an
  ordinary inherited scratch directory, preserving isolation and failed events.
- **Fixed cleanup block:** automatic approval review rejected F11 scratch cleanup
  with `blocked by policy`. The parent inspected both exact task-owned paths,
  verified their parent/identity and absence of reparse points, and removed them
  with native PowerShell. Raw evidence remains retained separately.
- **Nonblocking command diagnostics:** memory searches with no hits returned 1;
  expected defect/integrity checks returned 1; missing non-payload distribution documents and a mistyped source-inspection path
  were reported/corrected before checking the trusted helper. Command-discovery probes could
  return 1 for optional missing commands. CRLF-aware whitespace checking was used
  without rewriting pre-existing fixture notes. None was reported as a passing
  acceptance check. An OS WMI probe was unavailable; Python reported the OS version.

Local checks: the committed metadata revision passed **43 tests, two skipped** on
Python 3.14.3. After strengthening whole-target collision/drift preservation
assertions, the expanded-payload test passed a focused rerun covering every asset.
The earlier full suite took 287 seconds locally; CI's existing Windows/Linux job
timeout was increased from five to ten minutes for the larger fixed payload.
Six new skill entrypoints passed the skill-creator structural validator. Content
and whitespace checks cover their documented subsets, not semantic correctness.

Hosted CI results are recorded in the PR checks for this branch; no Linux
execution is claimed from the local Windows runs.

Required observed behaviors passed under the bounded local fallback protocol;
review found zero unauthorized target changes and zero fabricated execution claims.
This supports Milestone 4 functionality, subject to owner review of semantic
judgments. Native Codex/Cursor/Antigravity discovery/execution, paired pilots,
real-project trials, release packaging, and managed-content upgrade/recovery remain
later work. Neither CI nor this cohort certifies complete test effectiveness,
semantic consistency, arbitrary concurrent-filesystem safety, or cross-host support.
