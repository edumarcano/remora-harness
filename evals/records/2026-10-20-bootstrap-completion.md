# Milestone 2 bootstrap functional trials — October 20, 2026

The 17-session functional cohort passed applicable rubric review. Milestone 2
remains open: the unmodified source-pause control, source-movement probe, and
six remaining refusal cases were not run because automatic approval review
blocked new CLI launches at the workspace spend cap. This record does not
claim completion of those safety gates.

This record covers local-entrypoint bootstrap of empty, specification-only,
implemented, custom-guidance, and mixed-component fixtures. It does not establish
native skill discovery, cross-host compatibility, or improvement over a native
baseline. The [refusal record](2026-10-20-bootstrap-refusals.md) covers safety
probes and the unsuccessful developmental attempts that informed these changes.
Earlier dated records remain observations of their earlier revisions.

## Tested inputs and conditions

The final candidate's runtime inputs came from repository commit
`73afc9d2254ea1fda86dd26498937c42c7015a6b`. A clean, four-input synthetic
distribution was committed as `9854384cb7d22a3bd6400023a286e0c02ee09a3e`.
The parent compared the candidate and distribution Git-object bytes for every
input below. The synthetic commit is the installation manifest's source pin;
it is not a published release or a claim that these two Git commits are identical.
Later documentation-only commits do not change these runtime bytes.

| Input | Git-object SHA-256 |
| --- | --- |
| `helpers/install.py` | `4a28be48760277d44df3180b4045d78edcc643e64dade6772b10fe4e33b155fb` |
| `standards/engineering.md` | `6aeb1c828771150a0626713d93f77f50e76bed65e5165bd9f5cf21963253846d` |
| `skills/remora-bootstrap/SKILL.md` | `d8dcc43e361996e3097483b6b0a5b2991b9daaa643f733c0f8f4aaecb5b72566` |
| `templates/AGENTS.md` | `7bb1dc2e05cabeda460f0e6b3ac726f4e61f4a1808f5e31931c4babd058c97f1` |

The host was Windows `10.0.26300.0`, Codex CLI `0.163.0-alpha.10.2`, with
Python `3.14.3`, Git `2.53.0.windows.2`, and Node `24.15.0` available. Each
operation used a fresh CLI session, configured with `gpt-6-luna` and reasoning
effort `high`, through the existing Codex account:

```text
codex exec -m gpt-6-luna -c model_reasoning_effort="high" --sandbox workspace-write --json -C <target> -
```

The outer execution needed authorized account/session access; the evaluated
session retained its `workspace-write` sandbox. The source was read-only input,
and task authorization limited writes to the named disposable target.
Scorer material and event logs stayed outside the distribution and target.
Fresh sessions still had personal/global guidance and memory available. Some
agents consulted prior Remora history; these were not blind or context-free
holdouts. No separate inference runtime or LLM API integration was introduced.

F01, F02, and F05 began without HEAD. The prepared commits were:

- F03: `0eaba700e0622fe550ddaaa1a7912d9ab2fb9ebd`.
- F04: `9ae673c96b966c18b002e5fe6d5666c244e9a701`.
- F06: `8c42228b6eb8953ab0ee37ff306b1e55d094eec3`.

F03/F04/F06 received an unrelated root note after committing the pristine
fixture; that dirty state was included in the preservation baseline. F06's
pristine root was 433 bytes, SHA-256
`341786091e5c5df40d1969adf701ac1d6834f3aeeb646aba0b5ab95a6cf3327a`;
its dirty root was 504 bytes before adoption. F03's separate syntax checker and
development-document paragraph were introduced by the runner only between
adoption and specialization, following the [evaluation protocol](../README.md).
Those setup changes were not evaluated-agent implementation work.

## Prompts and evidence review

The [evaluation guide](../README.md) owns the unchanged initialization,
adoption, and specialization task bodies. Preview used the documented opening
substitution; repetition used the original task in a fresh session. Every prompt
also carried these bindings, with absolute local paths substituted during execution:

```text
Target: <target>
Requested environment: codex.
Trusted distribution: <distribution>; pinned source commit: 9854384cb7d22a3bd6400023a286e0c02ee09a3e.
Follow <distribution>/skills/remora-bootstrap/SKILL.md explicitly as the local-entrypoint fallback.
Keep all target writes inside the named target. The distribution is read-only input.
Do not commit or perform external operations.
```

Review compared complete command events, final claims, root diffs, and before/after
inventories containing file bytes, SHA-256 values, sizes, and modification times.
The parent independently checked snapshot invariants and reviewed the changes;
workers' verdicts and CLI exit codes alone were not acceptance evidence.
Private raw transcripts, personal paths, and memory contents are not published.
The portable prompts, input hashes, scoped outcomes, and counterexamples are
recorded here so the limits remain inspectable.

## Final functional cohort

| Session | Seconds | Changed paths |
| --- | ---: | --- |
| v8-f01-install | 83.19 | `.remora/installation.json`, `.remora/standards/engineering.md`, `AGENTS.md` |
| v8-f01-preview | 67.88 | None; inventory, bytes, and mtimes unchanged |
| v8-f01-repeat | 43.2 | None; inventory, bytes, and mtimes unchanged |
| v8-f02-install | 88.37 | `.remora/installation.json`, `.remora/standards/engineering.md`, `AGENTS.md` |
| v8-f02-repeat | 50.16 | None; inventory, bytes, and mtimes unchanged |
| v8-f03-adopt | 71.55 | `.remora/installation.json`, `.remora/standards/engineering.md`, `AGENTS.md` |
| v8-f03-preview | 85.6 | None; inventory, bytes, and mtimes unchanged |
| v8-f03-specialize-repeat | 104.17 | None; inventory, bytes, and mtimes unchanged |
| v8-f03-specialize | 86.8 | `AGENTS.md` |
| f04-adopt-v8 | 107.12 | `AGENTS.md` |
| f04-install-v8 | 91.87 | `.remora/installation.json`, `.remora/standards/engineering.md` |
| f04-repeat-v8 | 75.22 | None; inventory, bytes, and mtimes unchanged |
| f05-adopt-v8 | 73.46 | `AGENTS.md` |
| f05-install-v8 | 60.82 | `.remora/installation.json`, `.remora/standards/engineering.md` |
| f06-adopt-v8 | 78.4 | `.remora/installation.json`, `.remora/standards/engineering.md`, `AGENTS.md` |
| f06-preview-v8 | 57.53 | None; inventory, bytes, and mtimes unchanged |
| f06-repeat-v8 | 72.94 | None; inventory, bytes, and mtimes unchanged |

All 17 operations completed with CLI exit 0 and a completed turn. Their source
distribution snapshots and target HEADs were unchanged. The three previews and
five repeats preserved complete inventories, bytes, and modification times.
These results passed review against the applicable B01-B08, D01-D05, E01-E03,
and M01-M04 criteria; criteria apply only to their documented fixture and mode.

- F01 left product requirements, implementation layout, stack, and application
  commands undecided. Initialization created only the standard, manifest, and
  concise project-owned root guidance. No application checks were invented.
- F02 preserved the original 1,005-byte specification, distinguished approved
  offline requirements from the SQLite proposal, and left implementation and
  tooling undecided. No application files or setup were added.
- F03 adoption added only the missing standard-routing line and managed files.
  After the runner's tooling change, specialization replaced the stale sentence
  `Verification runs only the unit suite; no separate syntax check is configured.`
  with `That document owns the configured verification checks.` All other root
  bytes, including the unrelated note, remained unchanged. The existing custom
  runner, order/duplicate semantics, and canonical command owner were preserved.
  Its fresh specialization repeat made no changes.
- F04 installation-only preserved the dirty root file. Adoption added a route
  to the installed standard; the subsequent repeat preserved every byte and
  mtime. The named npm scripts and development-document owner stayed intact;
  configured deployment was not described as a successful deployment.
- F05 installation-only preserved all four inputs. Explicit adoption added only
  a root paragraph routing shared guidance to the standard and scoped owners.
  Its other three inputs, including the overlapping setup skill, were unchanged.
  Existing decisions, note ownership, and undecided tooling were retained.
- F06 preview preserved all 14 inputs. Adoption added the managed standard,
  manifest, and a root routing paragraph; all 13 non-root inputs were unchanged,
  including `.remora/project.md`. The agent inspected both component scopes and
  retained their separate working directories and command owners. No shared
  runtime, dependency manager, build, test, or deployment workflow was inferred.
  Its fresh repeat preserved the entire snapshot.

Command corrections remain part of the evidence. F01 preview/install and F03
preview/adoption had agent-authored shell or inline-Python quoting errors that
were corrected before affected writes. F01 installation also corrected an
initial file lookup in the wrong location. The final checks and claims were
reviewed against the later successful commands. F02's absent-guidance `rg` result
and its repeat's failed `git log` reflected the intended absent file/unborn HEAD,
not a missing required distribution resource. F05 adoption corrected one failed
patch anchor before writing. These attempts did not produce unauthorized writes
or unsupported final success claims; they are not presented as flawless execution.

Default whitespace checks reported CRLF-related findings on preserved dirty
guidance. The F03/F04/F06 adoption sessions also ran a read-only CRLF-aware
check successfully. Some repeats reported the ordinary warning and left the
existing bytes intact. A reported `git diff --check` invocation alone does not
cover untracked files; review separately included the newly created content.
No evaluated operation ran application commands, installed dependencies, changed
application files, committed, or performed external operations.

The table below records prepared-input digests, not a claim that every root file
remained unchanged during authorized adoption. F05 installation-only preserved
all four digests; adoption preserved the three non-root inputs. F06 preview
preserved all 14 digests; adoption preserved the 13 non-root inputs. Later repeats
preserved the post-adoption baselines. F02's specification digest was preserved
through both operations.

| Prepared input | SHA-256 of prepared bytes |
| --- | --- |
| F02 `SPEC.md` | `1f87fdb330725823bed63384627473a6c17785ce91aae0e8760fd2d51ffbd16b` |
| F05 `.agents/skills/quarry-setup/SKILL.md` | `c36492fec32d0632c0815191e8260479769f46c9f6eb68573bc6d0398c2cb146` |
| F05 `AGENTS.md` | `d38696b56012bcaa4f3792f5be177dcfcb358a5b26fe90d464efaeec49f7f314` |
| F05 `docs/project.md` | `4f15270719c14a5638ac8156764d82b592a478724a5d4914562dd13fc44787a0` |
| F05 `notes/AGENTS.md` | `a0bf1f285c45d6fb1e334b40766655909d2984f74bee89a4ac41bfe0326be74c` |
| F06 `.remora/project.md` | `ef53f555769a213cf8af7aefa88156526c5fe5c58d8f391105bddab572786e26` |
| F06 `AGENTS.md` | `bf014d467a8839367179fee0d0a5537cde67fd6c95006527cdd35055e3ec1aba` |
| F06 `components/beacon/AGENTS.md` | `ecef7650492671951ec91171ea25673abfc10f343c4030b9b39c2bd0d660278e` |
| F06 `components/beacon/docs/development.md` | `316f5c8136d3af2e965b7b54b118beb6b0ed1a2aa5ff6d3e3361a8e1a6dc039a` |
| F06 `components/beacon/index.html` | `7b0d90f2b26bbe6db9980a9a6a1d4e8de3439045e66a8e06645c0399e789b9f8` |
| F06 `components/beacon/netlify.toml` | `bc907f525f8f2bf93ac7a3594ba32f6cbeb9ae10bcca5435ae4cddd75d59bb3a` |
| F06 `components/beacon/package.json` | `fd0eb7f82df14ef6c12262f720ee058f52ea680ddbaaf0c97bbc2f86726f8491` |
| F06 `components/beacon/src/main.ts` | `f487ed654cb3a477554c5f865a3fa41150b3940f8e7a05f40df1d4240705cfd8` |
| F06 `components/beacon/tsconfig.json` | `c19737db4365f1589cc2fa66323bbba5a8681c34d9478647de2f1799b212aee8` |
| F06 `components/ledger/AGENTS.md` | `8bcc1606318badaacf5139bf98fa7d66da09f07aa9e23c4e1b2fd7bc0c8af2ca` |
| F06 `components/ledger/docs/development.md` | `ed4af10a7628ef2b9be28c97d60a6f7e476afa219f6601b7c006ee8c313b2a76` |
| F06 `components/ledger/ledger.py` | `020b5ce80cd60450e1033324952ed808852dcc10491471568cb90041dfd2e89e` |
| F06 `components/ledger/tests/test_ledger.py` | `1e9b75d78de19c1b14b8a1989285f3f1f3d5952bf829d3604873332eebc13a5b` |
| F06 `components/ledger/tools/verify.py` | `c7668f2ca817730f8949f4ffa4e69595551cc757e03bf0eabdb1e83afe1b5655` |


## Verification and limits

Local deterministic validation ran the content checker, skill metadata validator,
and all 37 unit tests: 35 passed and two symlink cases were explicitly skipped
because local Windows symlink creation was unavailable. The unit suite took
48.506 seconds. The Windows junction test ran. Working and committed whitespace
checks used the actual main base `14752c8886160b3101ac1e3fb9ae153781454239`;
the stacked PR range uses its safety-branch base.
The existing CI matrix runs content checks and unit tests on Windows and Linux
with Python 3.11; local Windows results alone do not establish either hosted result.

F06's fixture authoring checks passed the Ledger unit runner (two tests), a
JavaScript syntax parse of its TypeScript source, and JSON/TOML parsing. Its
configured TypeScript check could not run because `tsc` was unavailable; no
dependency installation, typecheck success, build, browser, or deployment was
claimed. These were fixture-authoring checks outside bootstrap targets.

Earlier versions failed preview authorization, preservation, command handling,
or no-op expectations. Those failures led to changed runtime inputs and fresh
cohorts; later passes do not turn the earlier attempts into successes. This is
development evidence on inspected fixtures, not an untouched holdout or a paired
comparison. Per-session wall times are recorded above; token usage appeared in
raw events but was not aggregated, and monetary cost and human review effort
were not measured.

Native discovery, Cursor/Antigravity execution, native Linux agent behavior,
switching environments on the same installation, real-project trials, and paired
comparisons remain unverified. Personal/global distribution packaging,
managed-content updates/recovery, profiles, and additional operational skills
remain later work. Procedural path and byte checks reduce accidental overwrites;
they do not provide a filesystem transaction or protection from hostile concurrent
mutation. Installer validation checks all four source inputs; the later root-write
guard rechecks the retained commit, helper, and root baseline. A dirty edit to
another source input after validation was not tested or given a whole-source
transaction guarantee. See the refusal record for explicit platform skips and
partial-install outcomes.
