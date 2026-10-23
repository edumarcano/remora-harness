# Milestone 5: operational implementation and local validation

Later scope reconciliation: the [Cursor smoke test](2026-10-23-cursor.md) completed
the accepted Milestone 5 Cursor requirement. Statements below about pending Cursor
trials describe the original protocol at this cohort's handoff. The omitted trials
are waived for Milestone 5, not executed or passing.

Date: October 21, 2026. This record owns observations, not product requirements.
The specification and [test packet](../milestone-5.md) own scope and protocol.
Public v0.1 release preparation is a subsequent phase.

## Identity and methods

The working repository base is `50da64eac83e1497543691524cb5fc3a75c31601`.
At the local validation handoff, changes were uncommitted and no push or PR had
occurred. Subsequent candidate identity and hosted results belong to the PR and
its checks; the disposable runtime pins below retain their original identities.
The runtime was frozen into a disposable committed distribution so installation
could use immutable Git objects without committing the real repository.

Initial runtime V1: `7bcb5ebc1015e2a5a53d0f597defe8685e172339`.
Reviewed runtime V2: `f2b5cc51f844f5eee7b5cd02844bd585be955eee`.
Only `helpers/install.py` differs: review rejects a checkout shadowed by package
metadata and nonregular archive entries. All skills, standards, profiles, and seed
have identical bytes across these pins. Final working runtime inputs match V2
allowing checkout LF/CRLF differences. Earlier functional observations retain V1
identity; updated-helper F12 was repeated under V2. No observations are relabeled.

| Runtime input | Git-object SHA-256 |
| --- | --- |
| `standards/engineering.md` | `e10f814f916b6c33d98cd8d622ebf01ce06ae98f3a3e25ffd81517c000dd7959` |
| `standards/documentation.md` | `3fa96407e8717df3a86b6da01adac123bc9fa1b56bde004c2e498f17db137ae6` |
| `standards/testing.md` | `a901b363f819d8ca0298640e33ac0585861ccc1d95d6483b78d314d10bc21edb` |
| `skills/remora-audit-documentation/SKILL.md` | `1e73a0de3a974993eb8f6beb944632225dc55fd62440614999995f8301b735d9` |
| `skills/remora-plan-change/SKILL.md` | `11a2f57335aef9f6be51f4398fb0999a23c0601339579f6c5448982bbde236aa` |
| `skills/remora-implement-plan/SKILL.md` | `c7757c53d1d2224d5b3750eff7d5f69719d29558345a9f805105c21a8f6aa1f3` |
| `skills/remora-fix-regression/SKILL.md` | `bcc4bcb768c789a32094d8f26218e3959c8f9f587ec45085efcaba492d18c4ce` |
| `skills/remora-review-change/SKILL.md` | `204619f4a67a3f5c026aed53ccbca77319290ec9939c10616a1b5c3fe33a6cdf` |
| `skills/remora-audit-tests/SKILL.md` | `d262617c9e964e1276d6ce7fd755f35f3732fe4b37d669cfa3cd39ea5b6de45c` |
| `skills/remora-audit-harness/SKILL.md` | `2c9833bafe8e85ffd534a570817bc7a1c76199e2ad6356443727e23acf883b0e` |
| `helpers/install.py` | `f52a1cdf7c5a0f61d71552f8660cd131f50df94753b154282fc3b9d4cc692875` |
| `profiles/python.md` | `d7b23638935e4b9e461ea184eab66431b6623e3d7c32dfea19d12b3fa0fc0979` |
| `profiles/typescript.md` | `bb04bb3ecacf22e9daa6a21105f04bb38ecd409857222593f23f53ee34cadfc4` |
| `profiles/local.md` | `d33a310345ba5ae2b1d5b7233041ce0f9d2a3654d7d6c26b70574b1e5ed6fd23` |
| `profiles/web.md` | `eb63e40b7f9112541a668663012c1d865905b2bb84ec0a4ba97cdbb4d0d39363` |
| `skills/remora-bootstrap/SKILL.md` | `4669ac8c2f8ab5e9963a3b89ed2aef51070cfee232adac75cf0f8d579f6168a4` |
| `templates/AGENTS.md` | `7bb1dc2e05cabeda460f0e6b3ac726f4e61f4a1808f5e31931c4babd058c97f1` |

Trials used Windows, Python 3.14.3, Codex CLI `0.163.0-alpha.11`, and the account's
configured `gpt-6.1-sol` with high reasoning effort. No model override, independent
API, dependency install, or provider integration was added. Native sessions used
workspace-write and ephemeral fresh context. Separate cohorts sometimes overlapped;
wall time is retained privately and is not a latency or cost comparison. Provider
cost was unavailable; raw native token usage was retained when exposed.

Actor targets excluded scorer guides and prior answers. No memory-file access was
observed in reviewed comparison command events. Personal/global host context was
not eliminated or fully inspectable: these are development fixtures, not blinded
holdouts. Semantic scoring is a separate review of the evidence, provisional for human
review of ambiguous recommendations. AI judgments are not independent human
calibration.

## Deterministic and native results

- Final full Windows suite: **55 tests, 53 passed, two explicit symlink skips**,
  421.314 seconds. Windows junction protection passed. Earlier full V1 run: 50
  tests, two skips, passed; focused content/lifecycle reruns passed after additions.
- Content checking and working-tree whitespace checks passed at local handoff.
  PR-range checks and actual-candidate hosted CI are reported separately in the PR.
- Package relocation worked after moving the source checkout away, with Git calls
  forbidden by the test. One personal bootstrap identity was exposed; project
  skills remained inert archive entries until project installation.
- Explicit updates, known legacy inventory migration, profile selection, collisions,
  preview/source movement, interrupted update/removal, backups, and preservation
  checks passed. Recovery is an inspected procedure, not an automated rollback claim.
- Local consistency and separately trusted-source comparison were distinguished:
  rehashing a local edit can pass consistency while the trusted-source check fails.
- Native Codex `skills/list` returned all seven project skills enabled at repo scope
  and exactly one bootstrap at user scope, with no discovery errors. A separate
  session-local baseline query returned bootstrap disabled, without global edits.
  Explicit skill-name task execution was reviewed separately from this discovery
  evidence; actor prose alone and direct file reads do not establish discovery.

The inventory query used the existing host's [documented app-server endpoint](https://learn.chatgpt.com/docs/app-server).
It started no model turn or Remora service. Implicit activation, Codex desktop,
Cursor editor, and Antigravity IDE were not certified by these CLI observations.

Functional observations covered empty/unborn bootstrap, specification-only setup,
existing-guidance adoption, configured TypeScript/deployment distinctions, nested
component guidance, documentation reconciliation, implementation and original-code
review, retained cross-layer tests, and a missing managed resource. F03 was already
correct: the agent reported two passing tests and declined to invent a repair.
F06's original underspecified change request produced a justified intent question;
a clarified verification-plan task then completed without edits.

F09's new four production tests were independently run against original and repaired
implementations: two failed on the original, all four passed after repair. The
original implementation review identified both order and duplicate loss. F11
retained all four distinct tests; its delegation-gap recommendation was tied to
that fixture's explicit requirement, not a blanket preference for internal-call
assertions. Read-only tasks preserved target inventories outside expected caches.

## Controlled comparison

The final Codex dataset contains F02/F05/F07/F10 twice per condition: **16 runs**.
Eight extra setup/development attempts were retained rather than silently replaced.
All final runs completed normally; exit 0 was not used as semantic ground truth.

| Observation | Baseline | Remora |
| --- | --- | --- |
| F02: approved/proposed/unknown distinctions, no invented implementation | 2/2 | 2/2 |
| F05: adequate root/scoped guidance and existing setup preserved | 2/2 | 2/2 |
| F07: seeded current-path findings | 4/4 found, 4/4 actionable supported | 4/4 found, 4/4 actionable supported |
| F10: seeded actionable protection weaknesses | 4/4 found, 4/4 actionable supported | 4/4 found, 4/4 actionable supported |
| Unauthorized target changes or fabricated execution claims observed | 0 | 0 |

Documentation recall/precision on the seeded F07 issues and actionable test-finding
precision on F10 meet the frozen thresholds in this small sample. Adequate history
and whitespace coverage were retained. Unexamined-case suggestions were advisory,
not extra scored defects. These observations show **no shared-outcome superiority**
for Remora in this cohort and do not establish general effectiveness.

F02 root instruction sizes were 1,189/1,250 bytes at baseline and 1,156/598 with
Remora. Baseline added only AGENTS.md; treatment added the declared managed payload,
local profile, manifest, and root guidance. F05 kept its 533-byte root unchanged
in both conditions; F07/F10 remained read-only. These are footprint observations,
not instruction-size targets.

F05 has an important operational limit. Unassisted installation into an existing
.agents/skills directory failed under this Windows sandbox after three standards;
original files stayed intact and no completion manifest appeared. A documented
--add-dir attempt prevented shell startup because writable descendants could not
be reopened beneath read-only carveouts. Those failures remain in the record.

The final F05 treatment was therefore installed by a narrowly reviewed
setup command; native sessions tested adoption and repeated-install idempotence.
Both conditions used ordinary workspace-write sessions. Personal bootstrap was
disabled only in baseline sessions via documented session-local skills.config,
and its effective disabled inventory was checked. Each treatment has one explicit
installation-preparation intervention. This is a controlled adoption comparison,
**not evidence of unassisted first installation in this sandbox**.

Automatic approval review rejected a proposed session-wide --approve-for-me mode
as too broad. It was never executed and is not part of the collector. The narrower
specific installer command was approved; no sandbox bypass or persistent global
configuration change was used.

## Disposable self-dogfooding

A complete disposable Remora checkout used a separate V2 distribution. Bootstrap
selected Python/local from actual helper code, preserved root guidance and original
files, and verified a repeated installation. Read-only harness, documentation, and
sampled test audits completed without repairs; local integrity passed with trusted
provenance explicitly unclaimed when source was outside the audit scope.

The linked plan/implementation/review exercised the deliberately retained historical
checker omission. A controlled broken link under profiles/ escaped the old scan
(exit 0); the repaired scan detected it (exit 1). The existing targeted regression
was reused. No unrelated product task or duplicate test was introduced.

The first review correctly found no behavioral diff against an already-correct
HEAD: preparation had left the historical defect unstaged. That review surface was
inadequate for the intended before/after review and is retained as a setup mistake.
A separate synthetic defective baseline was then committed only in the disposable
checkout; the corrected review covered the actual scan addition and found no
supported correctness issue. It observed the old exit 0 and repaired exit 1.

A separate copy exercised remora-fix-regression against the same known defect,
not a new independent issue. Independent execution of the 15 content-checker tests
failed before repair and passed afterward (one explicit symlink skip). The final
linked-copy content suite also passed in independent execution. Only the authorized
checker changed; installed content, requirements, guidance, and notes were retained.

## Failures and remaining gates

- **Fixed review finding:** ambiguous package/checkout source mode; regression
  coverage and V2 source-dependent validation were added before comparisons.
- **Fixed setup errors:** unavailable Windows Git-object deletion was replaced by
  moving the test checkout aside; prepared distribution paths were made absolute;
  F06 intent was clarified; the dogfood review baseline was corrected.
- **Retained command reliability limits:** some actor timestamp guards lost integer
  precision, a hash-inventory command had a PowerShell parse error, and Python edits
  introduced CRLF. Corrected attempts were checked; the final review used LF. No
  failed attempt is represented as a passing check.
- **Environment limits:** native actor temporary-directory ACLs blocked content-unit
  assertions and cleanup. Normal filesystem execution obtained actual red/
  green evidence. An optional F03 cache cleanup was rejected; expected caches were
  retained, not counted as source changes or bypassed.
- **Host validation follow-up:** the selected primary surfaces became Cursor Agents
  Window and Antigravity standalone. The
  [Antigravity record](2026-10-22-antigravity.md) closes that standalone cohort and
  the Codex-to-Antigravity switching leg. Cursor still requires 16 comparisons,
  uncovered functional scenarios and its switching leg. Editor/IDE certification
  is not inferred; prepared tasks are not execution evidence.
- **Hosted CI:** Windows/Linux results for the actual candidate are tracked in the PR
  checks. This local record does not claim hosted success from local execution.
- **Vulpes:** the private disposable snapshot pilot completed; detailed observations
  and input identity remain outside public records pending disclosure review. No
  private specification content is reproduced here; finalized GitHub history was
  not required. Public evidence clearance remains a later publication decision.

Local implementation and the bounded independent Codex protocol are complete.
Milestone 5 as a whole remains open for the required Cursor validation and final
cross-host evidence reconciliation. Actual-candidate hosted results are reported
in the PR and the later Antigravity record. Public v0.1 release preparation remains
later.
