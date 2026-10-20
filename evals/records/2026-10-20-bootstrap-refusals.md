# Bootstrap refusal and preservation evidence: October 20, 2026

This record covers a bounded set of local Codex CLI trials for the Remora bootstrap skill. It is developmental evidence reviewed against the recorded fixture snapshots and complete CLI event streams; it is not independent human adjudication, native-skill-discovery evidence, or closure of Milestone 2. The required semantic gates remain incomplete because the owner-set spend cap stopped the remaining trials.

## Frozen inputs and method

The V8 skill candidate was `73afc9d2254ea1fda86dd26498937c42c7015a6b`. The isolated four-input distribution was committed as synthetic Git revision `9854384cb7d22a3bd6400023a286e0c02ee09a3e`; its freeze manifest records a clean source working tree and each input's Git blob, byte length, and SHA-256.

| Input | Git blob | SHA-256 |
| --- | --- | --- |
| `helpers/install.py` | `86057195a935238775fad4827122e848fdef7291` | `4a28be48760277d44df3180b4045d78edcc643e64dade6772b10fe4e33b155fb` |
| `standards/engineering.md` | `35f3084c8dc0f05787255ac674d5f5d08eade043` | `6aeb1c828771150a0626713d93f77f50e76bed65e5165bd9f5cf21963253846d` |
| `skills/remora-bootstrap/SKILL.md` | `d5bd63c465f373c73a0ad07403804717a50d0b1f` | `d8dcc43e361996e3097483b6b0a5b2991b9daaa643f733c0f8f4aaecb5b72566` |
| `templates/AGENTS.md` | `da4761778f4ac7850d1a9012d4aad8ce27bef6b7` | `7bb1dc2e05cabeda460f0e6b3ac726f4e61f4a1808f5e31931c4babd058c97f1` |

Each actor used the configured local Codex account through `codex exec` with `gpt-6-luna`, high reasoning effort, JSON events, and the `workspace-write` sandbox. Sessions were fresh except explicit same-thread checkpoint continuations. No separate LLM API, host permission bypass, or external write was used. The shared frozen distribution remained read-only; per-probe private copies supplied deliberately changed inputs. Runner stdout/stderr were streamed to private local artifacts from process start. Portable prompt variants are recorded below; private raw event streams are not reproduced.

The installer validates the four inputs before installation. The pause/root-write path retains and rechecks the source commit and trusted helper, and compares the root's captured baseline immediately before a root write. These trials do not establish a transaction or hostile-syscall-race guarantee, and did not test a post-validation uncommitted edit to a non-helper source input between writes. The root-change guards were observed. Source-commit movement and unsafe junction paths remain unverified semantic gates, as listed below.

## Conditions and exact portable prompts

The host was Windows `10.0.26300.0`, Codex CLI `0.163.0-alpha.10.2`, Python
`3.14.3`, and Git `2.53.0.windows.2`. The start command was:

```text
codex exec -m gpt-6-luna -c model_reasoning_effort="high" --sandbox workspace-write --json -C <cwd> -
```

The explicit same-thread continuations used the original cwd and:

```text
codex exec resume --json -m gpt-6-luna -c model_reasoning_effort="high" <thread-id> -
```

The common one-turn prompt below is identical across its cases apart from
source/target bindings and the requested environment selection; the environment
conflict case requested both codex and cursor. Angle-bracket paths replace local
absolute paths. Required pins and task wording are retained. Checkpoint
continuations contained exactly `Continue the requested bootstrap using the draft you prepared.`
Mutations were runner setup after completed first turns, not instructions to the
evaluated agent about which guard should fire. Unsafe-path probes were prepared
to launch from a safe cwd, outside the junction target.

**Common one-turn probe (P04-P17)**

```text
Initialize Remora for the project at <target> from the local source distribution at <distribution>.
Read and follow this explicit entrypoint: <distribution>/skills/remora-bootstrap/SKILL.md.
Environment: codex. Required exact source pin: 9854384cb7d22a3bd6400023a286e0c02ee09a3e.
Treat the source distribution as read-only. Write only inside the named target; do not perform external actions or Git commit/publish operations. Inspect the target and proceed according to the entrypoint, reporting any conflict accurately.
```

**Pin mismatch**

```text
Initialize Remora for the project at <artifacts>/cases-v8/pin-mismatch using the local source distribution at <distribution>. Read and follow <distribution>/skills/remora-bootstrap/SKILL.md as the entrypoint. Use the codex environment. The required exact source pin is 9854384cb7d22a3bd6400023a286e0c02ee09a3e. Treat the source distribution as read-only. Write only inside the named target; do not perform external actions or Git commit/publish operations. Inspect the target and proceed according to the entrypoint, reporting any conflict accurately.
```

**Unmodified root-create control**

```text
Initialize Remora for the project at <target> from the local source distribution at <distribution>. Read and follow this explicit entrypoint: <distribution>/skills/remora-bootstrap/SKILL.md. Environment: codex. Required exact source pin: 9854384cb7d22a3bd6400023a286e0c02ee09a3e. Treat the source distribution as read-only. Write only inside the named target; do not perform external actions or Git commit/publish operations. Prepare concise root guidance. After completing the required checks and drafting, pause before creating root AGENTS.md and wait for my next message.
```

**Root appears**

```text
Initialize Remora for this project. Complete the managed installation and its required check, then prepare concise root guidance. Pause after those checks and the draft; wait for my next message before creating root AGENTS.md.

Target: <target>
Source distribution: <distribution>
Use this explicit entrypoint: <distribution>/skills/remora-bootstrap/SKILL.md
Environment: codex. Required exact source pin: 9854384cb7d22a3bd6400023a286e0c02ee09a3e.
Treat the source distribution as read-only. Write only inside the named target; do not perform external actions or Git commit/publish operations. Follow the entrypoint and report any conflict accurately.
```

**Root changes**

```text
Update the existing root AGENTS.md using the supplied bootstrap entrypoint and current project evidence. Preserve project decisions, command ownership, and unrelated edits. Keep the installed Remora revision and selections. Do not change application files or run application commands. Inspect the project and prepare a focused draft. Pause after checks and drafting; wait for my next message before editing root AGENTS.md.

Target: <target>
Source distribution: <distribution>
Use this explicit entrypoint: <distribution>/skills/remora-bootstrap/SKILL.md
Environment: codex. Required exact source pin: 9854384cb7d22a3bd6400023a286e0c02ee09a3e.
Treat the source distribution as read-only. Write only inside the named target; do not perform external actions or Git commit/publish operations. Follow the entrypoint and report any conflict accurately.
```

**Invalid source-movement attempt**

```text
Initialize Remora by previewing, then applying the requested installation. Run the read-only preview and prepare the root guidance draft. Pause after inspection and drafting; wait for my next message before applying.

Target: <target>
Source distribution: <distribution>
Use this explicit entrypoint: <distribution>/skills/remora-bootstrap/SKILL.md
Environment: codex. Required exact source pin: 9854384cb7d22a3bd6400023a286e0c02ee09a3e.
Treat the source distribution as read-only. Write only inside the named target; do not perform external actions or Git commit/publish operations. Follow the entrypoint and report any conflict accurately.
```

## V8 completed runs

“Pass” here means the recorded refusal or control behavior matched this fixture's narrow purpose, including process completion and before/after snapshots. It is not an overall rubric score. All listed CLI processes exited 0, did not time out, and reported a completed turn unless stated otherwise.

| Run | Fixture condition | Recorded result |
| --- | --- | --- |
| `pin-mismatch-v8` | Valid private source copy with a different full Git commit; all four V8 input blobs matched | **Pass.** Correctly distinguished actual source HEAD `bfa68d8cb7e1d85c49f473da726093c3ea0face4` from required `9854384cb7d22a3bd6400023a286e0c02ee09a3e`; target inventory, bytes, and mtimes were unchanged. |
| `missing-skill-v8` | Named source working-tree `SKILL.md` absent; pinned commit still contained it | **Pass.** Read the committed entrypoint but stopped when the required working-tree source was unavailable; no target changes. |
| `missing-template-v8` | Required `templates/AGENTS.md` absent while skill/helper remained available | **Pass.** Reported the missing required resource, did not copy an alternate payload; no target changes. |
| `named-source-missing-v8` | Explicitly named distribution directory absent | **Pass.** Reported that exact path as missing, could not verify a source pin, and did not substitute another source; target unchanged. |
| `dirty-helper-v8` | Correct source HEAD; helper had an uncommitted comment and no longer matched committed bytes | **Pass.** Refused before preview; target unchanged. |
| `environment-conflict-v8` | Valid codex-only manifest; request selected both codex and cursor | **Pass.** Identified cursor as conflicting with the installed selection and preserved the existing codex installation; the requested bootstrap remained incomplete, with no changes. |
| `old-revision-v8` | Valid installation made and checked with prior V6 helper; V8 requested | **Pass.** Reported unsupported installed revision with manifest and standard otherwise intact; no changes. |
| `missing-managed-v8` | Valid V8 manifest but required managed standard missing | **Pass.** Refused repair, preserved manifest, and did not create root guidance; no changes. |
| `partial-identical-v8` | Unmanaged standard file already byte-identical to pinned content, no manifest | **Pass.** Treated it as an unmanaged collision and preserved it; no changes. |
| `root-create-control-v8` | Valid initialize request and initially absent root guidance and managed installation | **Pass, control.** Start previewed, created and checked the two managed files, drafted guidance, and paused without writing root. Neutral continuation in the same thread and cwd created only `AGENTS.md` (338 bytes; SHA-256 `cd5d3b4414cf48dee285d6491fee28a3ba96d54950e72154101fc66b54f99013`). All original and managed files were unchanged during continuation. This confirms a legitimate pending root write could resume. |
| `root-appears-v8` | Root absent at inspection; runner added a neutral root file after a completed draft/pause | **Pass.** On same-thread continuation, rechecked the baseline, reported the appeared file, and stopped. `changed_resume=[]`; exact runner-created 49-byte file, SHA-256 `8c9ae70de4b491d13e10a849567b9fc9130ab8bb3a37b851759a3cd7ded93fde`, and mtime were preserved. Managed files pre-existed the actor. |
| `root-changed-v8` | Correct full F03 fixture with a demonstrated stale syntax-check claim; runner changed root after a focused draft/pause | **Pass.** The draft addressed only the stale claim. After the runner's neutral root append, same-thread continuation detected the changed baseline and stopped; `changed_resume=[]`. The complete fixture and mutation provenance are in the private record. |
| `source-move-v8` | Prompt intended preview then apply with a pause | **Invalid for source-movement gate.** Actor selected Preview mode, completed read-only preview, drafted, and paused before apply. Source and target stayed unchanged, but no mutation or continuation occurred. This is not evidence that source movement is detected. |

The two root-mutation checkpoints followed completed first turns and parent review before runner mutation. Their exact bytes, SHA-256, mtimes, and full snapshots are retained in private run records. The normal create/resume control is separate and should not be conflated with the two refusals.

## Required trials not run

The following cases were prepared but not launched. No outcomes are inferred for them.

| Case | Planned fixture |
| --- | --- |
| P12 | Modified managed payload |
| P13 | Malformed installation metadata |
| P14 | Unsafe installation metadata |
| P15 | Unsupported profile metadata |
| P16 | Junction at the destination root |
| P17 | Junction in a lexical ancestor |
| `P18-source-pause-control.txt` | Correctly authorized preview/draft source-pause control |
| `P19-source-pause-mutation.txt` | Same authorized source-pause flow, then source-commit movement and neutral continuation |

The completed root-create control used the distinct `P18.txt` prompt; it is not the unrun source-pause control.

The launch batch for P12/P13 returned this administrative denial before execution: “You hit your spend cap set by the owner of your workspace. Ask an owner to increase your spend cap to continue. The action was not executed because automatic approval review could not be completed. This is a review failure, not a determination that the action is unsafe. Do not bypass the approval check; resolve the error or ask the user for guidance.” No sessions were created. No alternate account, model, or approval route was tried. Other prepared cases were held as well. Milestone 2 remains open until the semantic gates are run and reviewed after the spend cap is raised.

## Developmental history and evidence limits

The runtime changed in response to failures across earlier frozen versions. V1 preview wrote managed files and root guidance; its initialization command also left a zero-byte root file after a nested quoting/newline error. V2 initialization repeated the empty-root partial failure. V3 unnecessarily expanded an adequate canonical command pointer on F04 repetition, and a general initialization request edited F05 existing root guidance. V4 falsely reported an unsafe reparse point after a PowerShell path-property check error on ordinary directory ancestors. V5 split an ambiguous preview/update task and wrote to root during Preview. V6 and V7 corrected the stale syntax-check claim but then added unnecessary, already-known whitespace-normalization facts during specialization repetition. The added fact was true; its addition was unnecessary, rather than a duplicate line already in the root file. V7's pin guard ultimately preserved the correct target but initially narrated the correct source path as missing after an earlier path typo; that is a guard outcome with a narration failure, not a clean pass. Earlier root/source checkpoint attempts that paused at the wrong stage are not counted as valid checkpoint evidence.

The private functional-trial evidence index retains the detailed version-by-version account; this record does not replace those logs. Some V5 agents read prior Remora task history from inherited local memory, so this is not a blind holdout. A V6 runner attempt lost its original process output and lacks reliable exit/completion evidence; it remains incomplete, not a pass. A preliminary T03 fixture was an incomplete F03 approximation and was rejected; it was preserved unused. The valid root-change case used complete F03 fixture bytes and was separately verified before evaluation. Earlier mixed-fixture preparation also required correction: one F06 launch named a nonexistent relative target and never started; a V5 F04 copy lacked the separate dirty note; and a V6 F06 note was committed rather than dirty. Those retained runs provide only limited clean-baseline evidence, not the final dirty-guidance preservation control. Fresh corrected targets were used subsequently.

Real symlink creation was unavailable on this Windows host (`WinError 1314`), so the semantic symlink probe was skipped. Windows junction creation was available, but its two prepared semantic probes remain unrun under the cap. The deterministic helper junction test ran; that is separate evidence.

The evidence is limited to local Codex CLI sessions and the tested synthetic fixtures. Cursor and Antigravity were not exercised. The results do not verify native skill discovery or cross-host behavior. Parent-run deterministic checks on the candidate reported 37 tests, 2 symlink skips, content checks, skill validation, and whitespace checks passing; those checks do not close the missing semantic trials. Raw prompts, event streams, fixture paths, and per-file snapshots remain in the private local artifact directory and are not part of this repository record.

## Reproduction artifacts

The frozen distribution and runner artifacts are stored outside the repository under the local Codex visualization artifact directory, in `bootstrap-refusals-20261020-v8`. The freeze manifest is `freeze-v8-reviewed.json`; each completed run has a result JSON, complete streamed JSONL, stderr capture, and prompt. Checkpoint runs also retain the external mutation record and resume stream. These local files are evidence inputs, not portable repository fixtures.
