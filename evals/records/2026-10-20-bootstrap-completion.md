# Milestone 2 bootstrap functional trials — October 20, 2026

The 17-session V9 functional cohort passed applicable review, and the
previously blocked safety scenarios completed as recorded in the refusal record.
Together these changes complete the bounded Milestone 2 bootstrap implementation
and local fixture verification, using the documented explicit-entrypoint handoff.

This record covers local-entrypoint bootstrap of empty, specification-only,
implemented, custom-guidance, and mixed-component fixtures. It does not establish
native skill discovery, cross-host compatibility, or improvement over a native
baseline. The [refusal record](2026-10-20-bootstrap-refusals.md) covers safety
probes and the unsuccessful developmental attempts that informed these changes.
Earlier dated records remain observations of their earlier revisions.

## Tested inputs and conditions

The final candidate's runtime inputs came from repository commit
`c7a06a6fecb8e2700a6e475e6e56ba68c8456df8`. A clean, four-input synthetic
distribution was committed as `cc60e9cd5ad5da6b4f839d8aa0bb06c29b8b6400`.
The parent compared the candidate and distribution Git-object bytes for every
input below. The synthetic commit is the installation manifest's source pin;
it is not a published release or a claim that these two Git commits are identical.
The documentation handoff fix is commit `9578c95`; it documents the first-read activation preamble and does not change the frozen V9 runtime inputs.

| Input | Git-object SHA-256 |
| --- | --- |
| `helpers/install.py` | `4a28be48760277d44df3180b4045d78edcc643e64dade6772b10fe4e33b155fb` |
| `standards/engineering.md` | `6aeb1c828771150a0626713d93f77f50e76bed65e5165bd9f5cf21963253846d` |
| `skills/remora-bootstrap/SKILL.md` | `fd1febaa4da354ddb6903689ffbbe9cc9c490a8376b9b1faf43c96dbb470f8bd` |
| `templates/AGENTS.md` | `7bb1dc2e05cabeda460f0e6b3ac726f4e61f4a1808f5e31931c4babd058c97f1` |

The host was Windows `10.0.26300.0`, Codex CLI `0.163.0-alpha.10.2`, with
Python `3.14.3`, Git `2.53.0.windows.2`, and Node `24.15.0` available. Each
operation used a fresh CLI session, configured with `gpt-6-luna` and reasoning
effort `high`, through the existing Codex account:

```text
codex exec --json --color never --sandbox workspace-write --model gpt-6-luna -c model_reasoning_effort="high" -C <target> -
```

The outer execution used authorized native-account access for SQLite/session startup; the evaluated session retained its `workspace-write` sandbox. The source was read-only input,
and task authorization limited writes to the named disposable target.
Scorer material and event logs stayed outside the distribution and target.
Fresh sessions still had personal/global guidance and memory available. Some
agents consulted prior Remora history; these were not blind or context-free
holdouts. No separate inference runtime or LLM API integration was introduced.

F01, F02, and F05 began without HEAD; F03 began at `c3c707580f397020361fe6fec8697aa098de1743`, F04 at `8994a627f3604357bb50f697a17899528ba264cd`, and F06 at `c057a98ceda8fc390e940b2b6d82eabdd4db277f`. F03, F04, and F06 had an unrelated root note appended after committing each pristine fixture; that dirty state was included in preservation checks. F03's syntax checker and development-document paragraph were introduced by runner setup between adoption and specialization, not by an actor session. The distribution and evaluated source stayed pinned to the same V9 bytes throughout.

## Prompts and evidence review

The [evaluation guide](../README.md) owns the unchanged initialization, adoption, and specialization task bodies; preview used its documented opening substitution and repeats reused their original task in fresh sessions. Every fresh actor prompt began with this activation preamble before the unchanged body and bindings:

```text
First read <distribution>/skills/remora-bootstrap/SKILL.md by itself, before any target inspection.
Do not batch that read with target operations. After reading it, follow its procedure for the task below.
```

All 17 first commands read only the pinned `SKILL.md`. Parent and independent
review passed the initial junction and malformed-metadata handoff gates before
the functional cohort. The task bodies and binding format were retained, with
new disposable targets and the V9 source pin. F02 was prepared from canonical
Git-object LF bytes (982 bytes), rather than the prior V8 checkout's CRLF bytes
(1,005 bytes); this is a recorded setup difference, not an actor conversion. Its
requirements were unchanged, and both final operations preserved its exact new
baseline. Other fixtures retained mixed LF/CRLF preservation controls.

Review compared complete command events, final claims, root diffs, and before/after
inventories with SHA-256, sizes, and modification times. The parent independently
checked all 17 snapshot invariants and reviewed the changes. Private raw
transcripts and personal paths are not published.
The portable prompts, input hashes, scoped outcomes, and counterexamples are
recorded here so the limits remain inspectable.

## Final functional cohort

| Session | Seconds | Changed files |
| --- | ---: | --- |
| f01-preview | 53.89 | None; inventory, bytes, and mtimes unchanged |
| f01-install | 62.71 | `.remora/installation.json`, `.remora/standards/engineering.md`, `AGENTS.md` |
| f01-repeat | 77.90 | None; inventory, bytes, and mtimes unchanged |
| f02-install | 83.37 | `.remora/installation.json`, `.remora/standards/engineering.md`, `AGENTS.md` |
| f02-repeat | 76.25 | None; inventory, bytes, and mtimes unchanged |
| f03-preview | 69.66 | None; inventory, bytes, and mtimes unchanged |
| f03-adopt | 152.27 | `.remora/installation.json`, `.remora/standards/engineering.md`, `AGENTS.md` |
| f03-specialize | 67.43 | `AGENTS.md` |
| f03-specialize-repeat | 86.25 | None; inventory, bytes, and mtimes unchanged |
| f04-install-handoff-account-access | 81.39 | `.remora/installation.json`, `.remora/standards/engineering.md` |
| f04-adopt-handoff-account-access | 87.18 | `AGENTS.md` |
| f04-repeat-handoff-account-access | 74.80 | None; inventory, bytes, and mtimes unchanged |
| f05-install-handoff-account-access | 92.35 | `.remora/installation.json`, `.remora/standards/engineering.md` |
| f05-adopt-handoff-account-access | 94.94 | `AGENTS.md` |
| f06-preview-handoff-account-access | 71.23 | None; inventory, bytes, and mtimes unchanged |
| f06-adopt-handoff-account-access | 131.05 | `.remora/installation.json`, `.remora/standards/engineering.md`, `AGENTS.md` |
| f06-repeat-handoff-account-access | 67.93 | None; inventory, bytes, and mtimes unchanged |

All 17 operations completed with CLI exit 0 and a completed turn. Their source
distribution snapshots and target HEADs were unchanged. The three previews and
five repeats preserved complete inventories, bytes, and modification times.
These results passed review against the applicable B01-B08, D01-D05, E01-E03,
and M01-M04 criteria; criteria apply only to their documented fixture and mode.

- F01 left product requirements, implementation layout, stack, and application
  commands undecided. Initialization created only the standard, manifest, and
  concise project-owned root guidance. No application checks were invented.
- F02 preserved the original 982-byte LF specification, distinguished approved
  offline requirements from the SQLite proposal, and left implementation and
  tooling undecided. No application files or setup were added.
- F03 adoption added only the missing standard-routing line and managed files.
  After the runner's tooling change, specialization replaced the stale sentence
  `Verification runs only the unit suite; no separate syntax check is configured.`
  with the exact sentence “Verification entrypoints are documented in `docs/development.md`.” All other root
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

Command corrections remain part of the evidence. F01 preview's `rg --files`
returned 1 for its empty target. F01 repeat first tried a nonexistent installed
standard path inside the distribution; the later installer check succeeded.
F02 repeat, F03 adoption, and F03 repeat corrected inline-Python guard syntax
errors before target inspection. F03 preview corrected an undefined `root`
variable in its guard before inventory; a later baseline-read command returned
1. F03 specialization's combined inventory had an expected no-match result.
The affected operations completed their subsequent checks; previews and repeats
remained no-ops.

F04 and F06 initially used text-based Git-object comparisons that reported
mismatches; byte-preserving comparisons succeeded before target inspection.
F05 corrected a guard syntax error before inspection. These are command-level
corrections within completed actors, not clean first-attempt execution. Earlier
outer-sandbox CLI startups failed on account/session access before actors ran;
authorized account access retained the same inner `workspace-write` sandbox.

Whitespace commands also reported preserved CRLF-note findings. Successful
read-only checks in some sessions do not erase those findings or imply every
invocation passed. The original note bytes remained unchanged. Review separately
included untracked content because an ordinary Git diff omits it. No evaluated
operation ran application commands, installed dependencies, changed application
files, committed, or performed external operations.

The table below records prepared-input digests, not a claim that every root file
remained unchanged during authorized adoption. F05 installation-only preserved
all four digests; adoption preserved the three non-root inputs. F06 preview
preserved all 14 digests; adoption preserved the 13 non-root inputs. Later repeats
preserved the post-adoption baselines. F02's specification digest was preserved
through both operations.

| Prepared input | SHA-256 |
| --- | --- |
| F02 `SPEC.md` (982 bytes) | `81fe4719bc029451f08a3f9378372d6196e7641b7d4931a44c5674d44d66b3df` |
| F03 `AGENTS.md` | `eed10ad0b3403b2bb8b582f831101bdc895c24c32a2607047cd8cb9510257b59` |
| F03 `ledger.py` | `06b76fffe5140150479fab2b8efbf1137048c94e48bda0bc8c6a4b845f075754` |
| F03 `docs/development.md` | `0acea60182a4a2759c798c8cec1e2ae39528bcaa6b3aaa1f0be4aaae2b142ca3` |
| F03 `tests/test_ledger.py` | `b6243a5c8b800645aee812299be6725de88c86eac36ac9a9fe56061f3a386cba` |
| F03 `tools/verify.py` | `0722c072c777784e327d07467e080e884184c9d8d89302731abb033e61ed1cd9` |
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
49.470 seconds. The Windows junction test ran. Working and committed whitespace
checks used the actual main base `14752c8886160b3101ac1e3fb9ae153781454239`;
the stacked PR range uses its safety-branch base.
The existing CI matrix runs content checks and unit tests on Windows and Linux
with Python 3.11; local Windows results alone do not establish either hosted result.

F06's fixture authoring checks passed the Ledger unit runner (two tests), a
JavaScript syntax parse of its TypeScript source, and JSON/TOML parsing. Its
configured TypeScript check could not run because `tsc` was unavailable; no
dependency installation, typecheck success, build, browser, or deployment was
claimed. These were fixture-authoring checks outside bootstrap targets.

The prior V8 functional cohort remains in private captures. A resumed V8
ancestor-junction actor enumerated through a junction before its guard; early V9
actors batched skill reading with target inspection. The revised runtime and
documented read-first activation contract were followed by these fresh cohorts.
The refusal record retains the failed and invalid attempts, checkpoint controls,
and source-mutation provenance.

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
