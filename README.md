# Remora

Remora is a portable, agent-native engineering harness for AI-assisted software
development. It supplies reusable skills, project adaptation, maintenance
procedures, and small local helpers to the user's existing coding agent.

Remora includes bootstrap, nine project workflows, shared standards, optional
language/runtime references, installed integrity checks, and reviewed updates and
removal. Helpers require Python 3.11+ and use the standard library.

See [host compatibility](compatibility/README.md) for tested surfaces and evidence.
The [specification](docs/product-spec.md) defines intended behavior. Public v0.1
release preparation follows operational validation.

## First use

Use a trusted local checkout pinned to an exact commit. Installer inputs must be
committed and unmodified. Ask the host to read skills/remora-bootstrap/SKILL.md
alone before any target operation, then follow it for the named target and hosts.
The whole checkout accompanies the entrypoint; copying that skill alone is invalid.

For native personal discovery, build a self-contained directory:

```text
python tools/package.py --output "<new-directory>/remora-bootstrap"
```

The output contains one discoverable SKILL.md, its helper/references/seed, and an
inert payload.zip plus bundle.json. It needs no source checkout or Git for payload
copying. Review and preserve the full directory. Hashes detect inconsistency;
they are not signatures. Never fetch or execute a moving remote script.
Install the directory into the host's documented personal skill location, avoiding
other copies of the same identity. See [host notes](compatibility/README.md).

Ask to initialize/install to create managed files and absent root guidance.
Existing AGENTS.md stays byte-identical unless you explicitly request adoption
or specialization edits. Preview/audit never writes. A specification can establish
intentions without establishing application implementation or test commands.

## Installation and selection

From the pinned checkout or personal bootstrap directory:

```text
python helpers/install.py --target "<project>" --environment codex
python helpers/install.py --target "<project>" --environment codex --apply
python helpers/install.py --check --target "<project>"
```

Default invocation previews. Repeat --environment for codex, cursor, antigravity.
Requested hosts are metadata, not certification. Add --profile python,
--profile typescript, --profile local, or --profile web only when target evidence
justifies those independent dimensions. No profile is the default. References do
not choose frameworks, tooling, architecture, or executable commands.

The installation owns .remora/standards/, .remora/helpers/install.py, selected
.remora/profiles/, nine .agents/skills/remora-* entrypoints, and
.remora/installation.json. The schema-1 manifest records development, exact source
revision, requested hosts, selected profiles, and managed SHA-256 hashes.
Root/nested instructions, specifications, existing skills, project context, and
unrelated files remain project-owned. Remora's own root AGENTS.md is never a seed.

An identical rerun preserves bytes and modification times. Ordinary installation
refuses different revisions/selections, occupied unmanaged destinations even when
identical, drift, missing managed assets, malformed metadata, and unsafe paths.
No dependencies, network access, host configuration, or application execution occur.
Installed bytes are pinned Git objects or validated package bytes, independent of
checkout line endings. Writes are bounded checks, not a whole-tree transaction or
protection against hostile concurrent filesystem changes.

## Installed checks and lifecycle

Normal workflows need no separate checkout. Inspect the installed helper before
executing it. From the target:

```text
python .remora/helpers/install.py --check --target .
python .remora/helpers/install.py --check --target . --source "<trusted-distribution>"
```

The first checks local manifest/hash consistency only. The second compares with
a separately trusted matching distribution. An installed helper and manifest cannot
certify their own provenance. Missing tools/source are explicit verification gaps;
manual inspection is not an equivalent source check. Exit codes: 0 completed,
1 conflict/integrity failure, 2 invalid invocation or incomplete execution.

Explicit update uses both trusted old and desired distributions:

```text
python "<new>/helpers/install.py" --target "<project>" --update --previous-source "<old>"
```

Repeat desired --environment/--profile options, or omit them to retain selections.
Use --clear-profiles to deliberately select none. Preview reports changes and a
Plan SHA-256; apply the same arguments with --apply --expect-plan <digest>
--backup "<new-private-directory-outside-project>". A changed source, target, or
selection invalidates the preview. An unchanged update preserves timestamps and
creates no backup directory. No semantic merging or silent upgrade occurs.
Known earlier inventories require a genuine matching trusted source.

Removal uses the matching distribution with --remove --previous-source <matching>
and the same preview/digest/backup process. It removes only verified managed files,
leaving project guidance and unrelated files. Review obsolete routing separately;
project-owned edits need explicit authorization. No recursive directory deletion.
For installations predating lifecycle support, run the current reviewed helper
and supply the old matching distribution through --previous-source; the historical
helper itself does not gain new commands.

The helper stores before-images and operation.json outside the target, invalidates
the completion manifest before mutation, and publishes a new manifest last.
Failures retain diagnostics and partial work. [Recovery instructions](compatibility/recovery.md)
explain narrow inspection/restoration; there is no automatic rollback engine.
Do not reset/clean a target or bypass host permission controls.

## Workflows

| Installed skill | Outcome |
| --- | --- |
| remora-plan-change | Read-only, repository-grounded decision-complete plan |
| remora-implement-plan | Authorized implementation, verification, and diff review |
| remora-fix-regression | Read-only diagnosis or explicitly requested repair |
| remora-review-change | Read-only review of a named implementation or exact surface |
| remora-prepare-pr | Read-only pull request description and empirical evidence brief |
| remora-prepare-release | Read-only release checklist, changelog update, and GitHub notes |
| remora-audit-documentation | Read-only audit or authorized coherent reconciliation |
| remora-audit-tests | Sampled protection chains; retain uncertain coverage |
| remora-audit-harness | Installation, ownership, drift, and overlap assessment |

Select a skill through the host's native interface. Fallback: first read
<target>/.agents/skills/<name>/SKILL.md alone, then follow it. That establishes
fallback execution only. Every skill explicitly reads relevant shared standards
and project guidance; links are not assumed automatic imports.

Name outcome, constraints, scope, and acceptance criteria. Review/audit does not
authorize repairs, dependency installs, publication, or faults. Deliberate faults
need explicit permission and a disposable copy. Ordinary reports remain in the
conversation; saved evaluation evidence excludes private data and full transcripts.

See the [evaluation guide](evals/README.md) and [Milestone 5 test packet](evals/milestone-5.md)
for preparation, required comparisons, remaining manual actions, and closure gates.
Public publication, marketplace packaging, and release notes are a subsequent phase.
