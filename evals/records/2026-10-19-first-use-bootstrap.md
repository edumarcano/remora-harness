# First-use bootstrap observations: October 19, 2026

Methods: deterministic tests, seven fresh Codex CLI sessions, before/after file
hash and modification-time comparisons, command-log inspection, and review by
the implementing agent. This is development evidence, not independent human
adjudication, a baseline comparison, or native-discovery certification.

## Source and conditions

The working change started from `b719de1b289451e45bac38ee135daf00daf29e6d`.
A separate disposable Git repository contained only the four runtime/bootstrap
inputs, committed as `83a2c9f01efddc4762aa2f2a491b04abb9467ab9`. This was a clean
synthetic development distribution, not a published Remora release or an ancestor
of the PR. Its inputs matched the implementation's staged Git blobs by SHA-256:

| Source input | SHA-256 |
| --- | --- |
| `helpers/install.py` | `4a28be48760277d44df3180b4045d78edcc643e64dade6772b10fe4e33b155fb` |
| `standards/engineering.md` | `6aeb1c828771150a0626713d93f77f50e76bed65e5165bd9f5cf21963253846d` |
| `skills/remora-bootstrap/SKILL.md` | `675d98f77792533ee964a215a14237da682e84709f076dccb3f8c0f4169423a7` |
| `templates/AGENTS.md` | `7bb1dc2e05cabeda460f0e6b3ac726f4e61f4a1808f5e31931c4babd058c97f1` |

Host: local Codex CLI `0.163.0-alpha.10.2`, Windows 11 `10.0.26300`, Python
`3.14.3`, Git `2.53.0.windows.2`. Each invocation was fresh and ephemeral, using
the configured account/model defaults with no model override. The collected CLI
events did not expose the model identity. Target writes used the host's
`workspace-write` sandbox, without bypass flags. Host-native inference used the
existing account; no independent LLM API client was introduced.

Each target was a separate disposable Git repository with absent HEAD. The source
distribution was outside the target and remained clean. Scorer instructions were
not copied into the distribution or target. Visible personal collaboration
guidance was found in an ancestor; F05 also had its root/nested guidance and setup
skill. CLI stderr reported plugin-icon and PowerShell snapshot warnings. Complete
hidden host context was not audited. Raw prompts/events stayed in local task
artifacts and are not included here as full transcripts.

## Task and invocation

The base task was the evaluation guide's unchanged initialization prompt:

> Initialize this repository with Remora using the supplied pinned local
> distribution. Inspect the repository and any specification first. Establish
> minimal evidence-backed project guidance and install the necessary Remora
> content. Preserve existing material and keep proposals distinct from decisions
> and implemented behavior. Do not implement the application. Report changes,
> checks actually performed, and remaining uncertainty.

Bindings appended to every prompt, with private paths replaced here by portable
labels, were:

```text
Target: <trial-parent>/<fixture>
Requested environment: codex.
Trusted distribution: <trial-parent>/distribution; pinned source commit: 83a2c9f01efddc4762aa2f2a491b04abb9467ab9.
Follow <trial-parent>/distribution/skills/remora-bootstrap/SKILL.md explicitly as the local-entrypoint fallback. Keep all target writes inside the named target. The distribution is read-only input. Do not commit or perform external operations.
```

Preview replaced only the initial word `Initialize` with `Preview initializing`.
Repeat runs used the original task and installed target, in a fresh session.
The runner invoked the CLI with the prompt on stdin:

```text
codex exec --ephemeral --json --color never --sandbox workspace-write -C "<target>" -
```

The runner prepared fixture/source commits before evaluation; evaluated agents
created no commits. There were no corrective interventions or retries. The three
installation sessions also performed their own installer-only repeat checks;
these are distinct from the later fresh-session bootstrap repeats.

## Inputs and observed changes

F01 initially had no working files. F02 contained only `SPEC.md`, with SHA-256
`1f87fdb330725823bed63384627473a6c17785ce91aae0e8760fd2d51ffbd16b`.
F05 started with these four files:

| Input | SHA-256 |
| --- | --- |
| `AGENTS.md` | `91c3d105998c3f9300f593a0588dcb7c9afaf847e8a6b75e3ff8b4bfc8fd1523` |
| `docs/project.md` | `68cfda58b3a6ca89722463868edd3d4ccb64df8ce1d170939eb0c0c23938b84b` |
| `notes/AGENTS.md` | `726266d7cc1a01680fda39e371f4641bce5df3fec6dcb44e73d1a649779f74b7` |
| `.agents/skills/quarry-setup/SKILL.md` | `9a16355700d7e676e86ccb43a31fa8207cff5faecdd2dae9d90b241071c61195` |

These are the exact input bytes used; recompute digests for later checkouts,
especially when line-ending conversion differs.

| Fixture/task | CLI exit | Wall seconds | Observed outcome |
| --- | --- | --- | --- |
| F01 preview | 0 | 35.83 | Conversational draft; no target files/directories added |
| F01 install | 0 | 60.76 | Added only root guidance, standard, and manifest |
| F02 install | 0 | 59.32 | Added the same three files; preserved specification |
| F05 install | 0 | 57.08 | Added only standard and manifest; preserved all inputs |
| F01 fresh repeat | 0 | 57.38 | Inventory, bytes, and file modification times unchanged |
| F02 fresh repeat | 0 | 52.43 | Inventory, bytes, and file modification times unchanged |
| F05 fresh repeat | 0 | 53.02 | Inventory, bytes, and file modification times unchanged |

Every original file retained its bytes and modification time during installation.
The implementing agent checked directory inventories, target HEAD absence, source
cleanliness, each manifest's source revision, installed standard bytes against the
pinned source, and exclusion of project-owned instructions from managed files.
Both new root instruction files used target-relative standard routing and
exclusive creation after link/ancestor inspection. F05 reported the missing
standard-routing sentence as an unapplied proposal and preserved its existing
setup workflow. No application code, toolchain, project skill, or host adapter
was added. No application validation commands were configured or run.

## Rubric judgments and limits

The implementing agent reviewed actual files and collected commands against the
unchanged B01-B08 rubric and the new E01-E03 controls:

| Criterion | F01 | F02 | F05 | Supporting evidence |
| --- | --- | --- | --- | --- |
| B01 | Pass | Pass | Pass | Initial inventories inspected; absent HEAD handled and still absent afterward |
| B02 | Pass | Not applicable | Not applicable | F01 guidance leaves application requirements, stack, layout, and tooling undecided |
| B03 | Not applicable | Pass | Not applicable | F02 guidance retains offline/persistence intentions, explicitly proposes SQLite, and identifies absent implementation/tooling |
| B04 | Pass | Pass | Pass | Project-specific guidance/proposals traced to the corresponding input or observed empty state |
| B05 | Pass | Pass | Pass | Preview/apply/check results present in command events; no application test success claimed |
| B06 | Pass | Pass | Pass | Exact additions and original-file preservation checked, including untracked files |
| B07 | Pass for installation integrity | Pass for installation integrity | Pass for installation integrity | Pinned hashes and resource routing checked; native discovery remains unverified separately |
| B08 | Pass | Pass | Pass | Handoffs disclose sources, changes, unknowns, actual checks, and explicit fallback |
| E01-E03 | Not applicable | Not applicable | Pass | Existing owners/overlap inspected, four inputs preserved, routing proposed only, exact two-file addition |

The B07 judgments cover installation/reference integrity only. They do not close
the native-discovery release gate, establish global bootstrap packaging, or prove
cross-host workflow compatibility. No overall native-integration pass is claimed.
Cursor and Antigravity were not run. F05 is a limited synthetic existing-guidance
control, not mature-application or adoption-edit coverage. Preview was exercised
only on F01; repeat checks were exercised on all three inputs.

Two F01 installation probes returned exit 1: an empty file search and a search of
the host memory registry for Remora/trial context with no matches. No prior Remora
answers were obtained from that search; inherited host context remains a limit.
Subsequent explicit inventory and integrity checks completed.
An ordinary Git diff on an unborn/untracked target supplies no file-content
coverage; the review included actual untracked contents and hash comparisons.

CLI usage events reported aggregate input tokens `1324917`, cached input tokens
`1163520`, output tokens `16929`, and reasoning output tokens `2970` across seven
turns. These host-reported categories are not added together or treated as a cost
comparison. Monetary cost and timed human review effort are unavailable. The
large inherited host context and small tuned-on fixtures prevent general
efficiency or effectiveness conclusions.

## Deterministic verification

Local Python `3.14.3` ran 37 unit tests: 35 passed and two symlink cases were
skipped because creation was unavailable. The Windows junction case ran and
passed. The skill-creator metadata/scaffold validator passed. The expanded
content checker passed, and staged/working whitespace checks passed. These
checks establish their bounded properties, not semantic correctness or native
discovery. Hosted Python 3.11 Windows/Linux outcomes belong to the PR's CI record.
