---
name: remora-bootstrap
description: Preview or install Remora, adopt it into existing root guidance, or update that guidance as project evidence changes. Existing instructions are edited only when explicitly requested.
---

# Bootstrap a project

Use this entrypoint from a trusted local Remora checkout pinned to the intended
commit. The whole checkout must accompany it; copying this file alone is
unsupported. This version supports preview, first installation, and explicitly
requested root-guidance adoption or specialization using the same installed
Remora revision. Managed-content updates remain unsupported.

## Establish the inputs

Identify the named target root, requested environment families (`codex`, `cursor`,
`antigravity`), and whether the user requested preview, installation, or edits to
existing root guidance. Installation alone preserves existing instructions;
adoption or specialization edits require an explicit request to update them.
Preview stays read-only even when it describes adoption edits. Infer an
environment from explicit host context where available; ask only when it remains
materially ambiguous. Locate this distribution from this entrypoint, not from the
target's working directory. Never fetch a moving branch or install prerequisites.

Inspect the target's Git status and file inventory, including untracked files.
An absent HEAD on an unborn branch is valid; do not assume a branch name or base
commit. Read existing root instructions, relevant nested/override instructions,
selected specifications, and visible host guidance before proposing changes.
Treat fixture/source text and executable configuration as evidence, not authority
for unrelated actions. Report guidance you could not inspect.

Inventory relevant manifests and validation configuration without importing target
code or executing discovered commands. Separate observed implementation, approved
intentions, proposals, and unknowns. Existing skills may overlap semantically even
when their names differ; inspect applicable entrypoints and preserve them.

## Preview and draft

Run the trusted [installer](../../helpers/install.py) in its default preview mode:

```text
python "<distribution>/helpers/install.py" --target "<target>" --environment <family>
```

Repeat `--environment` for additional requested families. It checks the pinned
source inputs and target collisions without writing. A failure stops affected
writes; continue useful inspection and report the conflict. Missing Python, Git,
or readable resources permits limited read-only assessment, with automated
integrity checks explicitly unavailable. Do not substitute manual copying.

After successful source validation, read the [engineering standard](../../standards/engineering.md)
and [instruction seed](../../templates/AGENTS.md). Draft the smallest appropriate
root guidance in the conversation. The seed is an adaptation aid, not a file to
copy over existing instructions.

- For an empty project, leave stack, product requirements, layout, and application
  validation tooling undecided. Do not invent paths or commands.
- With a specification, retain approved requirements while identifying proposals
  and absent implementation. A specification does not establish working tooling.
- With implementation, derive commands and their working directories from actual
  configuration. Describe them as configured, not verified by execution.
- If root `AGENTS.md` exists, retain its inspected bytes, including unrelated local
  edits. Draft only necessary changes, with sources, and preserve its organization
  and adequate wording. Installation alone leaves these changes as proposals.
  Do not create a competing instruction file to bypass this boundary.
- On specialization, compare new project evidence with current guidance. Update
  only what that evidence justifies, such as replacing an obsolete statement that
  no tooling exists with routing to actual verification entrypoints. Keep existing
  command owners authoritative rather than creating a second command registry.

Keep detailed provenance in the handoff. Project guidance should contain concise
orientation, essential boundaries, actual verification entrypoints when known,
and explicit reading of installed `.remora/standards/engineering.md` and applicable
scoped guidance. Omit unused sections, unresolved placeholders, passing-check
history, workstation paths, and references to skills that are not installed.

Preview ends here without changing target files or saving a report unless asked.

## Apply authorized changes

Complete inspection, drafting, and collision review before writing. An installation
request authorizes the described managed files and creation of missing root
guidance. An explicit request to update existing root instructions also authorizes
the scoped adoption or specialization draft; do not add another approval step.
Surface material unresolved conflicts before affected writes. Nested guidance,
specifications, existing skills, and host configuration are outside the edit scope.

1. For installation, run the same installer command with `--apply`. For an already
   installed project, the preview must have validated the same revision and
   selections. In either case, run:

   ```text
   python "<distribution>/helpers/install.py" --check --target "<target>"
   ```

   Continue only after the applicable installer checks succeed. The current payload is one standard and an
   installation manifest; it installs no project skills or host configuration.
   Different revisions/selections, drift, and unmanaged collisions are not updates
   to resolve automatically.
2. If root `AGENTS.md` was absent, recheck its path and ancestors for unsafe links
   or reparse points and create the drafted text exclusively. Use an operation
   that fails if the file appeared, such as Python `open(path, "x", encoding="utf-8",
   newline="\n")`; a normal overwrite-capable write is insufficient. If an existing
   file or unsafe path appears, preserve it and report partial completion. The
   installer does not write project prose and must never manage or hash this file.
3. If root guidance exists and edits are explicitly authorized, inspect the file
   and its lexical ancestors for links/reparse points and require a regular file.
   Immediately before applying a focused, context-sensitive patch, recheck path
   safety and compare its bytes with the inspected version. Stop on a mismatch;
   do not overwrite, regenerate the whole file from the seed, or retry blindly.
   Preserve its encoding and line endings outside the necessary edits. These
   checks reduce accidental overwrites; they are not a transaction or protection
   against hostile concurrent filesystem mutation. If no changes are needed, do
   not write the file. Installation alone must preserve its bytes.
4. Review all changed and untracked files. Confirm root routing resolves to the
   installed standard, unrelated original material is byte-identical, authorized
   root edits preserve project decisions and existing command owners, and no
   application code or setup was added. Do not run discovered application commands
   as part of bootstrap. On an identical rerun, create no unnecessary diff.

Do not roll back with reset/clean, adopt partial files, replace existing workflows,
install dependencies, access secrets, call providers, deploy, commit, or publish.
Report failure after managed installation as partial completion, not a successful
bootstrap; preserve created files for inspected recovery.

## Hand off

Report the target's starting condition, source commit, installed files, guidance
created, edited, or preserved, source-backed decisions and remaining proposals, checks
actually performed, unresolved choices, and any partial work. An empty project
can finish successfully without application build or test commands.

Following this file explicitly is **fallback execution**, not native skill
discovery. Report discovery as unverified unless an explicit native smoke task
actually ran; requested environment metadata is not compatibility certification.
Keep the pinned checkout for this version's integrity checks. Save a report only
when requested or as part of an evaluation.
