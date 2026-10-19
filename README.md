# Remora

Remora is a portable, agent-native engineering harness for AI-assisted software development.

It is intended to provide reusable instructions, skills, and workflows that help coding agents establish consistent development practices, adapt to different projects, and maintain software quality as projects evolve.

Remora is designed to work alongside existing coding environments rather than replace their execution capabilities. Its initial targets are Codex, Cursor, and Antigravity.

## Status

Remora is in early development. Milestone 1 established skill contracts, F01/F02 bootstrap fixture preparation and rubrics, and a bounded content checker with tests. The installation foundation for Milestone 2 provides preview, explicit installation, and integrity checks for one shared engineering standard. The bootstrap skill, project-guidance drafting, and native-host compatibility remain unimplemented or unverified.

The [product and technical specification](docs/product-spec.md) defines intended behavior. The [evaluation guide](evals/README.md) explains fixture preparation, calibration, and development checks; the [dated baseline record](evals/records/2026-10-19-baseline.md) records the initial design inputs and testing candidates.

## Local installation foundation

Use Python 3.11+ and Git with a trusted local checkout pinned to the commit you
intend to install. The installer and standard must be committed and have no local
modifications. No download or dependency installation occurs. From that checkout:

```text
python helpers/install.py --target "<existing-project>" --environment codex
python helpers/install.py --target "<existing-project>" --environment codex --apply
python helpers/install.py --check --target "<existing-project>"
```

The first command previews without writing. Only `--apply` creates files. Repeat
`--environment` to record additional requested families: `codex`, `cursor`, and
`antigravity`. These selections do not certify compatibility. Using an absolute
path to the script also works from another working directory.

Installation creates `.remora/standards/engineering.md` from the committed
[engineering standard](standards/engineering.md) and `.remora/installation.json`.
The manifest records schema version 1, the `development` release label, exact
source commit, requested environments, no selected profiles, and managed-file
SHA-256 hashes. Installed bytes come from Git objects, independent of checkout
line endings. Root `AGENTS.md`, project context, specifications, existing skills,
and unrelated files remain project-owned and unchanged. No skills or automatic
instruction routing are installed yet.

An identical rerun makes no changes. Occupied unmanaged destinations, modified or
missing managed files, malformed metadata, unsafe links, or different source and
environment selections stop the operation. Updates and automatic recovery are
not implemented. On interrupted writes, inspect the reported created files and
Git state before deciding how to recover; the installer preserves partial files
and refuses to adopt them silently. Filesystem writes are not a whole-tree
transaction or protection against hostile concurrent filesystem changes.

`--check` compares the installation to the same pinned source checkout, including
the source hashes; keep that checkout available for this foundation's checks.
Exit codes are 0 for success, 1 for conflicts or integrity failures, and 2 for
invalid invocation or incomplete checks. Checks establish bounded installation
integrity, not authorship, instruction loading, or workflow effectiveness.

## Design principles

- **Agent-native:** Use the reasoning and execution capabilities of existing coding environments.
- **Portable:** Share engineering practices across environments, languages, and project architectures.
- **Project-aware:** Adapt guidance to actual requirements and repository evidence.
- **Maintainable:** Treat documentation integrity, test quality, and configuration health as ongoing responsibilities.
- **Lightweight:** Avoid unnecessary infrastructure, dependencies, and complexity.

## Documentation

See [Product and Technical Specification](docs/product-spec.md) for the intended architecture, requirements, development milestones, and acceptance criteria.
