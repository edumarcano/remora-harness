# Remora

Remora is a portable, agent-native engineering harness for AI-assisted software development.

It is intended to provide reusable instructions, skills, and workflows that help coding agents establish consistent development practices, adapt to different projects, and maintain software quality as projects evolve.

Remora is designed to work alongside existing coding environments rather than replace their execution capabilities. Its initial targets are Codex, Cursor, and Antigravity.

## Status

Remora is in early development. Bootstrap installs a pinned project payload and
supports explicitly requested adoption or later updates to root project guidance
using the same Remora revision. The documentation workflow provides read-only
auditing and authorized reconciliation. Installation includes engineering and
documentation/testing standards and seven project-local development and maintenance
skills. Native-host
discovery remains unverified.

Milestone 2's bounded bootstrap implementation and local verification are recorded
in the [functional trials](evals/records/2026-10-20-bootstrap-completion.md) and
[refusal probes](evals/records/2026-10-20-bootstrap-refusals.md).
The [documentation workflow record](evals/records/2026-10-20-documentation.md)
covers Milestone 3's local trials, development feedback, and remaining review
limits. The [development and assurance record](evals/records/2026-10-21-development.md)
records Milestone 4's installed-entrypoint trials, controlled failure signals,
preservation checks, and verification limits. These use the documented read-first fallback; native discovery and
Codex/Cursor/Antigravity portability verification remain Milestone 5 work.

The [product and technical specification](docs/product-spec.md) defines intended behavior. The [evaluation guide](evals/README.md) explains fixture preparation, calibration, and development checks; the [dated baseline record](evals/records/2026-10-19-baseline.md) records the initial design inputs and testing candidates.

## First-use bootstrap

Open your target project in the coding host and supply a trusted local Remora
checkout pinned to the intended commit. Ask the agent to read
[the bootstrap entrypoint](skills/remora-bootstrap/SKILL.md) by itself before
inspecting the target, then follow it with the target path,
requested environments, and either preview or installation as the outcome. For
example, replacing the bracketed inputs:

```text
First read <distribution>/skills/remora-bootstrap/SKILL.md by itself, before
any target inspection. Do not batch that read with target operations.
Then follow it to initialize <target>
with Remora for <environment>. Inspect the project and specification first.
Preserve existing guidance and do not implement the application.
```

This is explicit local-entrypoint fallback, not native skill discovery. Supply the
whole pinned checkout; copying the skill file alone omits required resources.
The bootstrap source files and installer inputs must be committed and unmodified.
The bootstrap procedure requires comparing a supplied exact commit with the
distribution and retaining that identity through installation. It requires root
path checks before reading guidance and stopping affected writes after unsafe
path findings, source-commit movement, or root changes since inspection. These
agent instructions reduce accidental writes; they are not an enforced filesystem
transaction.

Preview stays read-only and drafts guidance in the conversation. Installation uses
the helper below, validates it, and exclusively creates root `AGENTS.md` only when
absent. That file remains project-owned and outside the installation manifest.
Installation alone preserves existing instructions; necessary adoption edits are proposals.
The [seed](templates/AGENTS.md) is adapted from target evidence, with no invented
stack or commands. Installation requests authorize these described local changes
without another approval step; material unresolved conflicts stop affected writes.

To authorize minimal edits to existing root guidance, ask explicitly:

```text
First read <distribution>/skills/remora-bootstrap/SKILL.md by itself, before
any target inspection. Do not batch that read with target operations.
Then follow it to install and adopt Remora
in <target> for <environment>. Update root AGENTS.md only where repository
evidence justifies it. Preserve existing project decisions and workflow owners.
```

For an installed project, request an update to root `AGENTS.md` after tooling or
requirements change, using the same pinned distribution and environment selections.
Bootstrap drafts the scoped changes, checks installation integrity, and applies
only authorized root edits. Preview remains read-only. Adequate guidance needs no
rewrite; nested instructions and existing skills remain outside the edit scope.
Changed files or unsafe paths stop affected edits. Guidance stays project-owned
and outside the manifest; semantic decisions are made by the host agent.

The bootstrap entrypoint and its seed stay in the source checkout; the seven
development and maintenance skills are installed project-locally. Global bootstrap packaging,
managed-content updates, profiles, and automatic recovery are subsequent work.
An installation from an older source revision cannot be upgraded through guidance
specialization.

The [first-use trial record](evals/records/2026-10-19-first-use-bootstrap.md)
documents initial local Codex CLI fallback observations. The
[adoption trial record](evals/records/2026-10-19-adoption-bootstrap.md) covers
implemented-project guidance edits and specialization, with their limits.

## Installation helper

Use Python 3.11+ and Git with a trusted local checkout pinned to the commit you
intend to install. The installer, standards, skills, and seed must be
committed and have no local modifications. No download or dependency installation
occurs. From that checkout:

```text
python helpers/install.py --target "<existing-project>" --environment codex
python helpers/install.py --target "<existing-project>" --environment codex --apply
python helpers/install.py --check --target "<existing-project>"
```

The first command previews without writing. Only `--apply` creates files. Repeat
`--environment` to record additional requested families: `codex`, `cursor`, and
`antigravity`. These selections do not certify compatibility. Using an absolute
path to the script also works from another working directory.

Installation creates engineering, documentation, and testing standards under
`.remora/standards/`, the seven skills listed below under `.agents/skills/`, and
`.remora/installation.json` from the committed payload.
The manifest records schema version 1, the `development` release label, exact
source commit, requested environments, no selected profiles, and managed-file
SHA-256 hashes. Installed bytes come from Git objects, independent of checkout
line endings. Root `AGENTS.md`, project context, specifications, existing skills,
and unrelated files remain project-owned and unchanged. Existing skill names and
owners are preserved; no host configuration or automatic instruction routing is
installed by the helper.

An identical rerun makes no changes. Occupied unmanaged destinations, modified or
missing managed files, malformed metadata, unsafe links, or different source and
environment selections stop the operation. Updates and automatic recovery are
not implemented. On interrupted writes, inspect the reported created files and
Git state before deciding how to recover; the installer preserves partial files
and refuses to adopt them silently. Filesystem writes are not a whole-tree
transaction or protection against hostile concurrent filesystem changes.
The host must permit writes to every declared destination, including existing
`.agents/skills/` directories. A permission failure may leave a partial installation;
use the host's normal permission controls rather than bypassing its protections.

`--check` compares the installation to the same pinned source checkout, including
the source hashes; keep that checkout available for this foundation's checks.
Exit codes are 0 for success, 1 for conflicts or integrity failures, and 2 for
invalid invocation or incomplete checks. Checks establish bounded installation
integrity, not authorship, instruction loading, or workflow effectiveness.

Bundle validation checks Remora's authored frontmatter subset: exactly `name`
and `description` as nonempty single-line plain strings, with a valid name matching
the skill directory. Descriptions start with an ASCII letter; YAML boolean/null
values, mapping delimiters, comments, quoted values, and complex YAML are outside
this subset. In installed skills, backtick-delimited target-root files
under `.remora/standards/` and `.agents/skills/` declare required resources and
must belong to the payload. This is a bounded convention, not arbitrary YAML,
Markdown, shell-command, or semantic validation. Source-relative Markdown links
remain covered by the maintainer content checker within its documented limits.

## Development and maintenance workflows

| Installed skill | Outcome |
| --- | --- |
| `remora-plan-change` | Repository-grounded plan; read-only unless saving is requested |
| `remora-implement-plan` | Complete an approved plan or clear scoped request, verify, and review |
| `remora-fix-regression` | Diagnose read-only or perform an authorized repair with failure evidence |
| `remora-review-change` | Read-only review of an exact change range or named implementation |
| `remora-audit-documentation` | Audit documentation or reconcile when edits are requested |
| `remora-audit-tests` | Explain sampled protection and missing failure signals; retain justified tests |
| `remora-audit-harness` | Inspect installation integrity, guidance ownership, drift, and overlap |

Select the named skill through the host interface where available. For fallback,
ask the agent first to read `<target>/.agents/skills/<name>/SKILL.md` by itself,
then follow it for your scoped task. Include the outcome, constraints, and
acceptance criteria; a separate saved plan is unnecessary for a clear implementation
request. Supply an exact range or named implementation for review, and state
whether local changes are included.

The skills explicitly load shared procedures from the installed standards using
target-root paths. They work through the existing host agent; no independent API,
mutation engine, or orchestration service is involved. Audit/review does not
authorize repairs, dependency installation, publication, or controlled faults.
Faults require explicit permission and isolation in a disposable copy. Results
ordinarily remain in the conversation. Missing tools or a matching trusted source
for installation checks are reported as verification gaps; manual inspection is
not equivalent to automated provenance checking.

Managed-content upgrades remain unsupported. Use the matching source for existing
installation checks; a newer checkout refuses older inventories rather than
silently replacing them. Evaluate the expanded payload in a fresh target.

## Documentation maintenance

After installation, select `remora-audit-documentation` through the host's skill
interface where available. For explicit local-entrypoint fallback, replace the
target path below:

```text
First read <target>/.agents/skills/remora-audit-documentation/SKILL.md by itself.
Then follow it to audit this repository's documentation. Do not edit files or
save a report. Report supported findings and verification gaps.
```

Name particular documents or an exact change range for a narrower task. Explicitly
state whether local staged, unstaged, and untracked changes belong in that range.
For authorized correction, request `Reconcile the current documentation within
<scope> against repository evidence, preserving adequate material, unrelated
changes, accurate history, and approved requirements.` Audit/preview stays
read-only; a reconciliation request authorizes necessary scoped documentation
edits. Source defects or unresolved requirement conflicts are reported rather than
silently resolved by changing documentation. Adequate content needs no diff.

The [skill](skills/remora-audit-documentation/SKILL.md) explicitly reads the
installed [documentation standard](standards/documentation.md) and engineering
standard from the target root. Missing resources are an incomplete installation,
not permission to fetch replacements. No Python runtime is needed to read and
follow the installed workflow; Python and Git are needed for installation checks.
Results ordinarily stay in the conversation. Following an installed file proves
fallback execution only; the [evaluation guide](evals/README.md) separates that
evidence from later native discovery and cross-host evaluation.

## Design principles

- **Agent-native:** Use the reasoning and execution capabilities of existing coding environments.
- **Portable:** Share engineering practices across environments, languages, and project architectures.
- **Project-aware:** Adapt guidance to actual requirements and repository evidence.
- **Maintainable:** Treat documentation integrity, test quality, and configuration health as ongoing responsibilities.
- **Lightweight:** Avoid unnecessary infrastructure, dependencies, and complexity.

## Documentation

See [Product and Technical Specification](docs/product-spec.md) for the intended architecture, requirements, development milestones, and acceptance criteria.
