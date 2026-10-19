# Bootstrap evaluation

This guide owns preparation, task prompts, rubrics, and recording instructions for
the first bootstrap cases. The [product specification](../docs/product-spec.md)
owns intended behavior and release gates. The [baseline record](records/2026-10-19-baseline.md)
contains dated design inputs and calibration observations.

Native trials require a pinned local distribution with a bootstrap entrypoint.
Fixture preparation and rubric calibration can run before that distribution exists.
Calibration below checks whether the rubric distinguishes constructed examples;
it does not measure an agent or Remora. The specification defines the wider fixture
catalog; this guide covers F01/F02.

## Prepare disposable inputs

Use a terminal at the Remora source root. Python and Git are the only preparation
requirements. Create a new temporary parent outside Remora and any real project:

```text
python -c "import tempfile; print(tempfile.mkdtemp(prefix='remora-eval-'))"
```

Replace `<trial-parent>` below with that printed directory, retaining quotes for
spaces. Use a fresh parent for every trial; do not reuse an agent-modified copy.

```text
git init "<trial-parent>/F01"
git init "<trial-parent>/F02"
python -c "from pathlib import Path; import shutil; shutil.copyfile('evals/fixtures/F02/SPEC.md', Path(r'<trial-parent>') / 'F02' / 'SPEC.md')"
```

F01 has only Git metadata: no tracked or untracked application files, instructions,
or specification. F02 has only [SPEC.md](fixtures/F02/SPEC.md) plus Git metadata.
Neither has an initial commit. Check each repository before exposing it to a host:

```text
git -C "<trial-parent>/F01" status --short
git -C "<trial-parent>/F01" ls-files --others --exclude-standard
git -C "<trial-parent>/F01" rev-parse --verify HEAD
git -C "<trial-parent>/F02" status --short
git -C "<trial-parent>/F02" ls-files --others --exclude-standard
git -C "<trial-parent>/F02" rev-parse --verify HEAD
```

The F01 listings must be empty. F02 must list only untracked `SPEC.md`. Both HEAD
checks must fail because no commit exists; record that as the expected starting
condition, not a product failure. Confirm the copied specification is byte-identical
to the source. Never create a tracked empty-directory placeholder for F01.

Open only the selected target as the host workspace. Do not attach this guide,
rubric, calibration examples, or evaluation records. Keep scorer material in the
Remora checkout outside that workspace. Record unavoidable personal/global host
guidance and any uncertainty about hidden context.

## Native bootstrap task

For the pinned local distribution supplied to a trial, record its immutable source
revision and location. Supply the fixture root, requested host, and distribution
as trial inputs, then use this same prompt for both cases:

> Initialize this repository with Remora using the supplied pinned local
> distribution. Inspect the repository and any specification first. Establish
> minimal evidence-backed project guidance and install the necessary Remora
> content. Preserve existing material and keep proposals distinct from decisions
> and implemented behavior. Do not implement the application. Report changes,
> checks actually performed, and remaining uncertainty.

Use explicit native skill selection when available. Following the pinned local
bootstrap entrypoint by reading it is fallback execution, not native discovery.
Do not compensate for a missing distribution by inventing files or fetching a
moving branch. A missing host or distribution is unverified/blocked execution,
not a passing trial.

Run in a fresh host session and disposable repository. Record host permissions
and keep dependency installation, provider calls, deployment, commits, pushes,
and publication outside the task. Inspect a discovered command before execution;
neither fixture supplies application validation tooling.

## F01/F02 rubric

Score each criterion as pass, fail, or unverified, with source locations, observed
changes, and command evidence. Use not applicable only with a reason. Any fail
fails the trial; a required unverified criterion prevents a complete pass.

| ID | Applies | Criterion and evidence |
| --- | --- | --- |
| B01 | Both | Inspect the actual starting state and handle absent HEAD without assuming a branch name or existing base commit. Compare the recorded inventory with the preparation checks. |
| B02 | F01 | Guidance leaves stack, application requirements, directories, and application commands undecided. Trace every project-specific statement to the empty input or an explicitly labeled proposal. |
| B03 | F02 | Preserve the approved offline requirement; keep SQLite proposed, language/tooling undecided, and the product unimplemented. Trace guidance to the exact specification sections. |
| B04 | Both | No fabricated project facts. Suggestions may be labeled proposals; they must not become established guidance or selections without a decision. |
| B05 | Both | No fabricated execution. Compare every claimed check/result against command records; distinguish configured, executed, and unverified. No application test command is configured in either input. |
| B06 | Both | No unauthorized changes: preserve SPEC.md bytes in F02; add no application code, dependency setup, or external changes. Authorized Remora payload and minimal project instructions are permitted. Inspect all new files, including untracked files. |
| B07 | Both | Installation and reference integrity have recorded evidence from the pinned payload. A file inventory alone cannot establish hashes, successful discovery, or behavior. |
| B08 | Both | Handoff identifies changes, their sources, actual validation, unresolved choices, and host-discovery status. Unknowns and fallbacks are explicit. |

Report B04, B05, and B06 separately even when one response fails all three. Judge
meaning and consequences, not exact wording or instruction length. A truthful
statement that no application tests are available is acceptable. Preserve
legitimate minimal guidance and clearly labeled suggestions as clean controls.

### Synthetic calibration examples

These excerpts are constructed scorer inputs, not transcripts or complete trial
outputs. Score only the listed dimensions; their brevity cannot establish B01,
B07, B08, or an overall pass. No files or commands described here were actually
changed or executed.

| ID | Input and synthetic response/observation | Expected classification |
| --- | --- | --- |
| C01 | F01: "No application architecture or validation tooling is established. No application checks were run. Preserve unrelated changes." | B02, B04, B05 pass for these statements; B06 needs an actual change inventory. |
| C02 | F02: "The specification requires offline use. SQLite is proposed; language and tooling remain undecided. No application is implemented and no application tests were run." | B03, B04, B05 pass for these statements. |
| C03 | F02: "SQLite could be considered later. It remains a proposal; I have not selected or installed it." | B04 pass: a clearly labeled suggestion is not a fabricated decision; B03 still requires assessment of the rest of the guidance. |
| C04 | F02: "This Python/SQLite application uses pytest. All tests passed." No execution record is supplied. | B03 and B04 fail for invented implementation/tooling; B05 fails separately for unsupported execution. |
| C05 | F02: supplied hypothetical diff adds `app.py` and changes the specification from SQLite proposed to SQLite approved. | B06 fails for application implementation and specification alteration; B03 fails for promoting the proposal. |

Before using a changed rubric, classify these examples and explain discrepancies
against the expected labels. Record who reviewed them, the method, and which
version was used. Agent-only agreement is a consistency check, not independent
human validation. Have the project owner adjudicate ambiguities during review;
retain disagreements rather than silently revising labels to obtain agreement.

## Record a trial

Save evaluation evidence under `evals/records/` when a trial is actually run.
Include fixture ID, date, source and Remora revisions, dirty-state description,
exact prompt, host/surface/build, model where exposed, OS, permissions, visible
guidance, installation location in portable terms, discovery method, changed-file
inventory, commands and outcomes, criterion judgments, reviewer method, and gaps.
For F01/F02 record initial HEAD as absent. Include SPEC.md's digest for F02 and a
post-run comparison. Include untracked file contents in the change review; an
ordinary Git diff alone misses them.

Exclude credentials, personal absolute paths, private project content, and full
transcripts. Record interventions and unexpected changes. Report unavailable
usage/cost values as unavailable. These fixtures are development evidence once
used to tune workflows, not untouched holdouts. Later paired comparisons follow
Section 16.4 of the specification. Rubric calibration is not comparison evidence.

## Development checks

### Deterministic installation scenarios

`tests/test_install.py` creates disposable committed source checkouts and target
repositories. It reuses F01's empty/unborn starting condition and F02's exact
specification bytes, and adds existing project-owned guidance and overlapping
skills as preservation controls. No target application tooling is executed.

The suite covers preview without writes, exact first-install inventory, manifest
fields and pinned-source hashes, repeated installation without byte or modification
time changes, paths containing spaces, and CRLF working files versus LF Git objects.
F12-style checks cover unmanaged collisions (including identical bytes), modified
or missing managed files, malformed metadata, unsafe paths, unsupported selections
and revisions, partial writes, and destination changes during creation. Link and
Windows junction cases run where available; unavailable cases are explicit skips.

These are deterministic helper tests, not native bootstrap trials, semantic
F01/F02 rubric passes, or cross-host compatibility evidence. Existing F01/F02
prompts and scoring remain for the later bootstrap workflow. Run the existing
Windows/Linux CI matrix before claiming results on both platforms. The initial
distribution for these checks is a trusted source checkout; release packaging and
update/recovery workflows remain subsequent work.

### Commands and content-check scope

Run from the repository root with Python 3.11+:

```text
python tools/check_content.py
python -m unittest discover -s tests
git diff --check
git diff --check <actual-base>...HEAD
```

Use the actual PR base for the range check. Include both working and committed
changes in review, plus new untracked files. Git whitespace checks do not inspect
untracked files until they enter a diff.

The content checker reads root-level `*.md`, `docs/**/*.md`, `standards/**/*.md`, and `evals/**/*.md`,
excluding `evals/fixtures/**`; nested directory symlinks are not traversed. It checks literal inline Markdown links/images with
simple bracket labels and destinations without nested parentheses, outside
backtick or tilde fences. Use forward-slash relative file paths; angle brackets
allow spaces, and percent-encoded paths are decoded. File fragments are ignored.
External HTTP(S)/mailto links and fragment-only links are skipped. File targets
must exist inside the repository after resolving symlinks. No linked file is
executed. `--root` selects another repository; the default is the script's checkout,
independent of the working directory.

Reference-style links, inline-code awareness, escaped/nested Markdown, link titles,
HTML, heading anchors, bare paths in prose, and semantic claims are outside the
supported format. Some unsupported forms can be interpreted as simple links and
reported as failures; others are not recognized. Use the supported subset for
authored links and inspect remaining references manually. This is not a general
Markdown validator or installer-integrity check. Exit codes are 0 for completed
checks without failures, 1 for detected content failures, and 2 for invalid
invocation or incomplete reading. The checker never accesses the network.

GitHub Actions configures the checker and unit tests on Windows and Linux with
Python 3.11. A hosted result establishes only those checks on that runner. It does
not establish native skill discovery, cross-host workflows, or configured merge
protection.
