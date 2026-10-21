# Documentation workflow evidence: October 20, 2026

Milestone 3 implements purpose-aware documentation audit and authorized
reconciliation. The final local documentation cohort completed eleven fresh
Codex CLI sessions across F07-F09, including repository/range scope, structural
correction, accurate history, code/specification conflict, repeats, and a clean
unborn repository. Snapshot and command-event review found no unauthorized
documentation-trial writes or fabricated execution claims. Editorial judgments
and ambiguous labels remain subject to owner adjudication during PR review.

These are development observations, not native discovery, cross-host certification,
paired-baseline comparisons, independent human validation, or statistical proof of
improvement. The [evaluation guide](../README.md) owns preparation, exact portable
task bodies, and the frozen rubric. The
[specification](../../docs/product-spec.md) owns requirements and release gates.

## Runtime identities and conditions

The final implementation is repository commit
`bf17a3a0d9d6f7a7491a9dd39f81b708dd957686`. A clean six-input synthetic distribution
was committed as `1db8125dd6aa883e67329cb1024bb187237793b4` (V2). The parent compared
every runtime input's Git-object bytes with that implementation commit; all six
match. The distribution pin identifies the fixture installation, not a published
release or an assertion that the two Git commits are identical.

| Final input | Git-object SHA-256 |
| --- | --- |
| `helpers/install.py` | `6c5edd1e9a24100a4d889eb708740e573f998641ddf657d2e845b9acc9843a68` |
| `skills/remora-audit-documentation/SKILL.md` | `1e73a0de3a974993eb8f6beb944632225dc55fd62440614999995f8301b735d9` |
| `skills/remora-bootstrap/SKILL.md` | `5427ae7f845b4d60e964f17433e90010c2903fa89908e3c8a6500904063d4c00` |
| `standards/documentation.md` | `3fa96407e8717df3a86b6da01adac123bc9fa1b56bde004c2e498f17db137ae6` |
| `standards/engineering.md` | `6aeb1c828771150a0626713d93f77f50e76bed65e5165bd9f5cf21963253846d` |
| `templates/AGENTS.md` | `7bb1dc2e05cabeda460f0e6b3ac726f4e61f4a1808f5e31931c4babd058c97f1` |

The host was Windows `10.0.26300.0`, Codex CLI `0.163.0-alpha.10.2`, Python
`3.14.3`, and Git `2.53.0.windows.2`. Sessions used the existing Codex account and
configured `gpt-6.1-sol` model with high reasoning effort, without model overrides
or a separate LLM API. The outer runner used normal account/session access; actor
commands retained the `workspace-write` sandbox:

```text
codex exec --json --color never --sandbox workspace-write -C <target> -
```

Each documentation operation began with the guide's installed-skill read-first
preamble, followed by its unchanged audit or reconciliation task. The range task
received the exact prepared `base..HEAD` and explicitly included staged, unstaged,
and untracked changes. Repeats reused the reconciliation task in fresh sessions.
The coding host performed inference; no provider integration was added to Remora.

Targets and supplied distributions excluded scorer material. Actors nonetheless
had personal/global guidance and memory available, and consulted prior Remora
history or searched memory. These were not blind or context-free holdouts.
Command review found no use of this scoring guide or another trial's answers.
Raw events, prompts, snapshots, and review summaries stayed private outside the
repository; no personal paths or full transcripts are published here.
The timings below are actor wall time, excluding preparation and human review.
Cost was unavailable; no token-efficiency or cost comparison is claimed.

## Preparation and review

The parent copied the complete fixture inputs, installed/checked the pinned
payload as runner setup, and committed synthetic starting states with hooks and
signing disabled. It then added an unrelated README appointment note and
untracked `notes/local.txt`. The clean control had corrected current paths and no
HEAD. The range case had two commits for the check/sample moves plus a staged
current-path claim and an unstaged current-command claim, as specified in the guide.
The synthetic README suffix was a blank line followed by
`Local note: retain the harbor review appointment on Friday.`; runner append used
Windows CRLF. `notes/local.txt` contained `Unrelated local planning note.`.

| Final target | Starting HEAD or range |
| --- | --- |
| F07 repository | `12d43273bf9be05bab927a1858914a7ea2ab8e2e` |
| F08 | `5aecf0eb63291ce70934daf4af8a8378bad5ebc1` |
| F09 | `4b1920d91d66cb437ab025cefd0ea263a6a73915` |
| F07 range | `5175a6c7dfea9c77db90ef7b40b254ee3a302aaf..07539c182ed93b3b78104b81210424b1f16a0cf6` |
| Clean F07 | Absent; filesystem inventory used |

Before trials, the implementing agent classified the guide's five constructed
calibration examples as specified: supported current-path findings, historical
rewrite failure, specification-laundering failure, incoherent appended-caveat
failure, and valid clean no-op. This checked rubric consistency, not agent quality
or human agreement.

Review compared complete command events and reported outcomes, final documents,
actual diffs, and every non-Git file's SHA-256, size, and modification time.
The parent independently verified allowed change surfaces. F07's corrected README
matched exactly the two expected path substitutions, with the original local-note
bytes intact. F08 retained its introduction, valid example, local-only boundaries,
canonical usage link, and unrelated notes. History, scoped/root instructions,
specifications, application code, and managed assets were preserved throughout the
documentation trials.

## Final documentation cohort (V2)

| Operation | Seconds | Changed files | Factual precision | Seed recall |
| --- | ---: | --- | --- | --- |
| F07 repository audit | 44.48 | None | 2/2 | 2/2 |
| F07 reconciliation | 69.44 | `README.md` | 2/2 | 2/2 |
| F07 repeat | 57.94 | None | N/A, 0/0 | N/A, 0/0 |
| F07 range audit | 64.38 | None | 2/2 | 2/2 |
| F08 repository audit | 80.09 | None | 2/2 | 2/2 |
| F08 reconciliation | 100.71 | `README.md`, `docs/usage.md` | 2/2 | 2/2 |
| F08 repeat | 50.03 | None | N/A, 0/0 | N/A, 0/0 |
| F09 repository audit | 65.20 | None | 1/1 | 1/1 |
| F09 reconciliation | 49.72 | None | 1/1 | 1/1 |
| Clean/unborn audit | 48.01 | None | N/A, 0/0 | N/A, 0/0 |
| Clean/unborn reconciliation | 48.10 | None | N/A, 0/0 | N/A, 0/0 |

Counts normalize grouped report IDs to the rubric's conceptual factual issues;
repeated occurrences count once per issue per operation. Advisory editorial
comments and retained/informational observations are excluded from factual
precision. Corrected repeats have no remaining factual seed. Zero denominators
are not perfect scores. Positive-denominator operations meet the frozen 0.80
precision/0.70 recall targets under the implementing agent's provisional scoring.

- F07 found the missing current command/sample paths while preserving dated old
  paths. The range audit inspected both versions of the staged/unstaged document
  and the actual renames; no branch name or guessed base was substituted.
- F08 corrected the default and duplicate behavior, removed contradictory current
  follow-up explanations, and retained one configuration owner with a README
  pointer. It did not add another document or keep patching exceptions.
- F09 identified lost order/duplicates as a code/specification discrepancy. Both
  operations preserved the approved requirement, buggy code, and accurate
  current-behavior description. The implementation repair remains outside scope.
- Audits, F09 reconciliation, corrected repeats, and clean controls preserved
  complete inventories, bytes, and modification times. No report files were added.

All eleven sessions completed with CLI exit 0. That alone was not the success
criterion. Execution evidence included the reviewed Harbor check, targeted Tally
behavior probes, and Queue's expected failing specification comparison. Inspection
was distinguished from execution; no claim of Python 3.11 execution was made.
Some `rg` memory searches returned 1 for no matches. Default whitespace checks
flagged CRLF endings in pre-existing local notes; actors preserved those bytes
and reported the limitation, sometimes also running a CRLF-aware check.

Several audits still offered optional editorial advice about the synthetic
appointment note, including the clean audit. This is maintenance-noise feedback,
not factual drift or authorization to remove it. The clean reconciliation kept it.

## Development feedback and earlier cohort (V1)

V1 used synthetic pin `75872a623e74f337c4bb09312ad4ce9f9e5b5045` and the same six
runtime inputs except `standards/documentation.md`, whose hash was
`42b9dd41d7cf8a59a45bcb2464176a5d63389f97d65d90688e595ddf6886c105`.
It ran the same eleven-operation documentation cohort on separate fresh targets.
All seeded issues were found; the changed-file surfaces were the same as V2.

The F08 audit additionally interpreted “bounded prefix” as potentially promising
bounded input consumption. The returned prefix was bounded; no requirement
promised lazy input consumption. It presented this possible reading as a medium
finding requiring clarification. Conservative provisional scoring counts that as
an unsupported actionable inference: precision 2/3, recall 2/2, below the precision
target. Owner adjudication could instead classify it as advisory ambiguity; the
disagreement is retained rather than hidden.

The documentation standard was clarified to assess the stated contract and treat
an unpromised property as advisory uncertainty absent supporting requirements or
a concrete reader error. No fixture labels or numerical targets were changed.
The entire documentation cohort was rerun under V2. Its F08 audit reported only
the two supported factual defects. This is a developmental correction on inspected
fixtures, not a claim of measured general improvement or untouched holdout success.

## Bootstrap regressions and protected-directory limits

These targeted regressions exercised the expanded payload using the guide's
unchanged bootstrap prompts and read-first preamble. F01 began empty/unborn;
F05 copied its four existing project-owned files and overlapping setup skill.
Installation and adoption were separate fresh actor sessions. The runtime inputs
were V1 or V2 as labeled, not interchangeable observations of one source pin.

| Pin | Operation | Seconds | Observed outcome |
| --- | --- | ---: | --- |
| V1 | F01 preview | 87.38 | No inventory, byte, or modification-time changes |
| V1 | F01 installation | 120.53 | Three managed assets, manifest, and absent root guidance created |
| V1 | F01 repeat | 97.46 | No inventory, byte, or modification-time changes |
| V1 | F05 installation | 130.74 | Partial: two standards created, skill-directory write denied |
| V1 | F05 adoption after partial install | 102.78 | Stopped on unmanaged partial content; no changes |
| V2 | F01 installation | 115.33 | Final payload and absent root guidance created |
| V2 | F05 installation | 127.63 | Partial: two standards created, skill-directory write denied |
| V2 | F05 adoption after partial install | 89.04 | Stopped on unmanaged partial content; no changes |
| V2 | Fresh F05 installation with scoped write directory | 113.10 | Same protected-directory failure and preserved partial files |
| V2 | Adoption of that partial target | 101.67 | Stopped without changes |
| V2, October 21 | Fresh F05 installation using normal approval review | 128.06 | Same protected-directory failure; partial standards preserved |
| V2, October 21 | Adoption of that partial target | 138.83 | Stopped without changes |

The native workspace sandbox protected F05's pre-existing `.agents` directory.
The helper returned an access-denied error while creating the new skill directory,
preserved the standards already created, and did not publish a manifest. Actors
reported partial installation rather than success, checked the preserved content,
and kept all four original files byte-identical. A CLI exit 0 denotes a completed
actor turn here, not a successful installation. Default native installation and
adoption on this protected-directory case remain incomplete; installer unit tests
with normal Windows directory access do not certify that host workflow.

The scoped follow-up used the CLI's supported `--add-dir <target>/.agents` alongside
`workspace-write`. It did not remove the host's protection. No sandbox-bypass flag,
permission modification, manual copying around the failure, or automatic cleanup
was used. README now explains the required host write access and partial-install
boundary instead of changing installer safety behavior to conceal the limit.

An attempt to use normal automatic approval review initially combined incompatible
CLI flags and exited 2 before starting an actor. The corrected `--approve-for-me`
invocation (which selects workspace-write itself) then hit the workspace spend cap
after read-only preview: CLI exit 1, no target changes. That attempt and the
temporarily blocked branch push are retained as account/review interruptions, not
functional passes. Follow-up results after account access resumed are recorded below.

On October 21, after approval/account access resumed, a fresh F05 target was run
with `--approve-for-me` alone. Normal approval-review mode did not itself grant
write access to the existing skill directory: installation again stopped with
two standards and no manifest, and subsequent adoption preserved the partial
target unchanged. This was not a successful existing-project installation or
adoption. No further host-permission experiments were attempted. The same final
payload installed successfully in F01 and through runner preparation with normal
Windows directory access; the existing-directory native sandbox limitation remains
explicit rather than being counted as a Milestone 3 semantic-workflow pass.

## Deterministic verification and limits

The final local suite passed 41 tests with two skips because symlink creation was
unavailable. Windows junction checks exercised both `.remora` and `.agents` and
passed. Other checks covered exact payload/hash inventory, both new assets'
collisions/drift, committed resources, source line endings, interrupted multi-file
installation, and refusal to upgrade an older one-standard inventory.

During development a symlink-test refactor incorrectly used a skip inside a
subtest, allowing a later privileged operation to run. The availability check was
moved outside subtests and the full suite rerun successfully. The initial sandbox
temp-directory ACL failures were environment failures; the unchanged command ran
with normal Windows temporary-directory access. No check was weakened to conceal
a functional failure.

The authored-content checker and skill-creator metadata validator passed. Neither
establishes semantic effectiveness or native discovery. Hosted checks are recorded
by the PR's Actions runs rather than inferred from local results.

The remaining review gate is owner adjudication of structural/editorial judgments
and ambiguous scoring. Native skill discovery, Cursor/Antigravity execution,
the paired pilot, and real-project trials remain Milestone 5. Rechecking baselines
before edits is agent guidance, not a transactional guarantee against concurrent
filesystem changes. Missing-resource and concurrent-edit workflow probes were not
part of this cohort; deterministic installation tests cover their narrower inputs.
