# Adoption and specialization observations: October 19, 2026

Methods: fresh Codex CLI fallback sessions, complete non-Git file inventories,
before/after bytes and modification times, command-event inspection, and review
by the implementing agent. These are development observations, not independent
human adjudication, paired baseline comparisons, or native-discovery evidence.

## Distribution and conditions

The change started at merged PR #3, `b34a907928ca1f46be59d014eb38562e56e35dba`.
Trials used a clean synthetic Git distribution containing the four runtime inputs,
committed as `2a4f0435fc2a3afbbf521318340e1a545ebc2a01`. It is not a published
release or an ancestor of this PR. Its Git-object inputs match this implementation
after checkout CRLF normalization:

| Input | SHA-256 |
| --- | --- |
| `helpers/install.py` | `4a28be48760277d44df3180b4045d78edcc643e64dade6772b10fe4e33b155fb` |
| `standards/engineering.md` | `6aeb1c828771150a0626713d93f77f50e76bed65e5165bd9f5cf21963253846d` |
| `skills/remora-bootstrap/SKILL.md` | `8f9ae66ca8031326aab9fad941109879615eb0f2d83da0e1f9b44010ab2408ab` |
| `templates/AGENTS.md` | `7bb1dc2e05cabeda460f0e6b3ac726f4e61f4a1808f5e31931c4babd058c97f1` |

Host: Codex CLI `0.163.0-alpha.10.2`, Windows 11 `10.0.26300`, Python `3.14.3`,
Git `2.53.0.windows.2`. Sessions used the existing account and configured defaults,
without a model override; collected events did not expose model identity. Each
session used `workspace-write`, without sandbox-bypass flags. Targets and the
separate read-only distribution lived in the task's allowed artifact directory,
outside the Remora repository. Scorer files stayed outside target workspaces and
the distribution. The distribution remained clean.

Visible inherited guidance included personal collaboration instructions and host
memory instructions. Some sessions searched the memory registry; no prior Remora
answer was obtained or used. Complete hidden host context was not audited. CLI
stderr included plugin-icon and unsupported PowerShell-snapshot warnings.

Before these runs, six sessions across two external temporary parents were blocked
by filesystem access. Both recreation attempts preserved all target files. Their
CLI exit codes were zero, but their responses reported incomplete inspection and
installation: these are blocked attempts, not functional passes. Moving fresh
inputs into an explicitly allowed root resolved access without changing host
permissions or weakening the sandbox. No workflow correction prompts were sent.

## Preparation and tasks

F03 and F04 used initial synthetic commits `01cb0226e9159dafac44aa64afb12c27819d225f`
and `55a440ce7c1ccf7be3f1058b4763f233135397cf`. A corrected F04 copy used
`0f658f59193fc63c8504ccf79147740e5247c247`. After committing, the runner
appended this unrelated local note to each root file, with CRLF endings:

```text
Preserve this local note: use plain language in handoffs.
```

The original F03/F04 fixture files used LF, so the trial root files deliberately
contained mixed endings. F01/F02/F05 retained absent HEAD throughout. The runner
created commits only for source/fixture preparation, with synthetic identity,
hooks disabled, and signing disabled. Evaluated agents created none.

Task bodies were exactly the initialization, adoption, preview, and specialization
prompts in the [evaluation guide](../README.md). F01/F02 and the F04 installation
control used initialization; F03 preview used the documented opening-word
replacement. The following bindings were appended, with private locations replaced
here by portable labels:

```text
Target: <trial-parent>/<fixture>
Requested environment: codex.
Trusted distribution: <trial-parent>/distribution; pinned source commit: 2a4f0435fc2a3afbbf521318340e1a545ebc2a01.
Follow <trial-parent>/distribution/skills/remora-bootstrap/SKILL.md explicitly as the local-entrypoint fallback.
Keep all target writes inside the named target. The distribution is read-only input.
Do not commit or perform external operations.
```

Invocation, with the complete prompt on stdin:

```text
codex exec --ephemeral --json --color never --sandbox workspace-write -C "<target>" -
```

Each task used a fresh session. Sequential tasks intentionally retained the same
installed target: F03 preview, adoption, controlled tooling change, specialization,
repeat; F04 installation-only, adoption, repeat. F05 adoption and F01/F02 regression
installations each used separate fresh targets. Independent targets ran concurrently.

The F03 tooling change was exactly the guide's runner-prepared syntax-check script
and development-document paragraph. It left root guidance obsolete intentionally.
The specialization baseline included those changes; they were not agent edits.

Staged review subsequently renamed F04's `name` DOM variable to `nameInput` to
avoid a collision with the browser global under TypeScript script-scope checking.
The first F04 installation/adoption/repeat sequence used the earlier spelling.
The corrected fixture received a fresh adoption/repeat sequence; neither variant
was type-checked or built. The bootstrap distribution itself did not change.
An additional repeat was started before corrected adoption had fully finished its
whitespace correction. Its before/after snapshots show root guidance changing
while the repeat agent reported no writes. This overlapping probe is excluded
from no-op scoring; the scored repeat started only after both processes exited.

## Outcomes and review

| Task | CLI exit | Wall seconds | Observed changes |
| --- | --- | --- | --- |
| F01 install | 0 | 86.36 | Standard, manifest, minimal root guidance |
| F02 install | 0 | 70.25 | Standard, manifest, specification-backed root guidance; specification unchanged |
| F03 preview | 0 | 48.41 | None, including file modification times |
| F03 adopt | 0 | 84.44 | Standard, manifest, one root routing paragraph |
| F03 specialize | 0 | 69.83 | Only the obsolete root tooling statement |
| F03 specialization repeat | 0 | 63.92 | None, including file modification times |
| F04 installation-only | 0 | 57.49 | Standard and manifest; all seven inputs unchanged |
| F04 adopt | 0 | 82.97 | One root routing paragraph; managed files unchanged |
| F04 adoption repeat | 0 | 50.34 | None, including file modification times |
| F04 corrected adopt | 0 | 106.24 | Standard, manifest, one root routing paragraph |
| F04 corrected repeat | 0 | 50.99 | None, including file modification times; fully sequential |
| F05 adopt | 0 | 101.62 | Standard, manifest, one root routing paragraph |

The reviewer compared exact inventories, hashes, modification times, manifests,
root diffs, and command events. Each manifest had the six supported fields, source
revision above, requested `codex` selection, empty profiles, and only the standard
in managed hashes. Installed standard hashes matched the source Git object.
Root guidance was excluded. No target revisions or source inputs changed.

Removing the exact routing addition from each F03/F04/F05 adopted root reproduced
its complete original bytes, including the local note and mixed/CRLF endings.
Specialization replaced only the two-line tooling statement, retaining routing,
decisions, and the command owner. All other original files retained bytes and
modification times. No project skills, profiles, host adapters, application code,
dependency setup, or saved agent reports were added.

F03 kept label order/duplicate semantics and its custom verification entrypoint.
F04 retained its named scripts, local greeting behavior, accessible output, and
the distinction between deployment configuration and verified deployment. F05
inspected the overlapping setup skill, reported the proposed addition before
editing, and preserved product decisions, nested guidance, and that skill.

Command inspection confirmed source validation and installation integrity checks
before root writes. Root-edit commands checked regular-file/path safety and
compared retained original bytes before focused writes. F05's first write guard
failed because the agent mistyped its expected hash; it disclosed the error,
re-read the unchanged file, corrected the typo, and then applied the draft. This
was an agent self-correction, not a real concurrent-change refusal test.

Default whitespace checks flagged CRLF characters in the runner's pre-existing
local notes. Agents disclosed and preserved them; additional CRLF-aware checks
in F03/F04 distinguished the preserved warning from new whitespace. Other nonzero
commands were no-match searches or F01's expected empty inventory search. No
application commands, dependency installs, provider calls, deployments, commits,
or external publication occurred in evaluated tasks.

| Criteria | Judgment and evidence |
| --- | --- |
| D01 | Pass: preview untouched, installation-only root unchanged, explicit adoption permitted the scoped edits. |
| D02 | Pass: actual Python/npm workflow owners retained; configured commands not reported as executed or deployed. |
| D03 | Pass: root changes limited to routing or changed evidence; all unrelated bytes and custom work retained. |
| D04 | Pass: specialization changed only obsolete guidance; both implemented-project repeats retained inventory/bytes/mtimes. |
| D05 | Pass for observed paths: matching pinned integrity checks preceded edits; root remained project-owned. Negative native refusal cases remain unverified. |
| F05 E02 | Pass: setup overlap and existing owners identified, without replacement or deletion. |
| B01/B04-B08 | Pass for scoped inspection, authorization, evidence, and integrity; native discovery remains unverified separately from B07's bounded integrity result. |
| F01 B02 / F02 B03 | Pass: empty-project choices stayed undecided; specification-only guidance retained offline/persistence intentions and SQLite's proposal status. |

These judgments assess the scoped development trials, not a complete native-host
pass. Controlled concurrent-root edits and root symlink/reparse refusal were not
injected into native sessions. Managed-file collision/link/refusal coverage is
provided by existing deterministic tests; it does not prove the new semantic
procedure's negative paths. Cursor, Antigravity, native discovery, full mature
projects, real-project adoption, and baseline superiority remain unverified.

## Maintainer checks

The existing unittest suite passed outside the restricted temporary-directory
sandbox: 37 tests, 35 passes and two unavailable-symlink skips. The Windows
junction case ran and passed. The initial sandbox run failed while creating and
cleaning up temp fixtures, before product behavior was exercised.

Outside evaluated sessions, `python -B tools/verify.py` in F03 ran two passing
unit tests. The runner-prepared syntax-check script also passed. Node `v24.15.0`
accepted F04's TypeScript syntax with `node --check`; Python parsed its JSON/TOML.
F04 dependencies were not installed; TypeScript type checking, Vite build,
browser execution, and deployment were not performed.

The skill metadata validator and content checker passed (10 authored Markdown
files). Working/staged whitespace checks passed; the actual PR base was confirmed
as `b34a907928ca1f46be59d014eb38562e56e35dba`. Committed-range whitespace and
hosted CI results are reported with the PR. Local results do not substitute for the existing
Python 3.11 Windows/Linux CI matrix. Raw prompts/events and snapshots remain local
task artifacts; no full transcripts or private workstation paths are published.
Monetary cost and timed human review effort are unavailable.
