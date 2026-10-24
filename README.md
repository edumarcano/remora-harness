# Remora

Remora is a portable, agent-native engineering harness for AI-assisted software
development. It equips existing coding agents with deterministic engineering standards,
disciplined development workflows, and verifiable lifecycle tooling.

Remora targets **Codex**, **Cursor**, and **Antigravity** without requiring background daemons,
external model proxies, or third-party package dependencies.

> **The Remora Metaphor:** In nature, a remora is a small fish that attaches to a larger marine host in a mutualistic relationship, traveling alongside it and keeping it clean without impeding its movement. Remora takes this exact approach: it attaches directly to your existing AI coding agent (Codex, Cursor, or Antigravity) without introducing an independent daemon or heavy runtime, riding along to keep the codebase disciplined, verified, and grounded.

---

## Architectural Principles

- **Host-native execution:** Remora runs entirely inside the host agent via standard skill discovery (`.agents/skills/`). It introduces no background services, local servers, or network daemons.
- **Zero runtime dependencies:** Helpers require only Python 3.11+ and the Python standard library.
- **Zero external model routing:** Reasoning belongs exclusively to the host environment's agent. Remora does not make direct LLM API calls, manage API credentials, or route model traffic.
- **Deterministic safety & provenance:** Installations use committed Git objects, cryptographic SHA-256 manifests, atomic previews, and mandatory before-image backups.
- **Evidence-based workflows:** Workflows enforce reproduction-first defect repairs, consequence-based split-axis code reviews, artifact proof, and anti-slop documentation standards.
- **Preservation of project ownership:** Target instructions (`AGENTS.md`), project specifications, tests, and custom skills remain project-owned. Remora never overwrites unmanaged files.

---

## Installed Workflows

Remora installs ten specialist workflows under `.agents/skills/`:

| Workflow | Role |
| :--- | :--- |
| `remora-plan-change` | Repository-grounded, decision-complete change planning. |
| `remora-implement-plan` | Authorized implementation, checkpoint verification, and diff review. |
| `remora-fix-regression` | Reproduction-first defect diagnosis and test-first repairs. |
| `remora-review-change` | Independent split-axis review evaluating Specification Fulfillment and Standards Compliance. |
| `remora-prepare-pr` | Scannable, reviewer-focused PR descriptions emphasizing artifact proof over CI dumps. |
| `remora-prepare-release` | Pre-flight hygiene, Keep a Changelog updates, and SemVer release notes. |
| `remora-remediate-project` | Checkpointed 4-phase repository onboarding (grounding, docs, tests, and technical debt). |
| `remora-audit-documentation` | Documentation ownership, refactoring thresholds, and anti-slop hygiene. |
| `remora-audit-tests` | Protection-chain verification, failure signal isolation, and assertion auditing. |
| `remora-audit-harness` | Remora installation integrity, drift detection, and guidance conflict analysis. |

---

## Host Compatibility

Remora is validated across three primary AI coding environments:

| Host Environment | Surface | Discovery Root | Status |
| :--- | :--- | :--- | :--- |
| **OpenAI Codex** | Codex CLI | `.agents/skills/` | Verified |
| **Cursor** | Agents Window / Composer | `.agents/skills/` | Verified |
| **Google Antigravity** | Standalone Desktop App | `.agents/skills/` | Verified |

See the [host compatibility guide](compatibility/README.md) for surface notes and empirical test records.

---

## Quickstart

### 1. Build the Standalone Bootstrap Bundle

To discover Remora globally in your coding host, package the self-contained bootstrap skill:

```bash
python tools/package.py --output "<personal-skills-dir>/remora-bootstrap"
```

The output contains `SKILL.md`, installation helpers, and an inert `payload.zip` with `bundle.json`. It requires no Git access or network operations at runtime.

### 2. Initialize a Project

To install Remora into a project repository from a pinned checkout:

```bash
# Preview proposed additions (read-only by default)
python helpers/install.py --target "<project-root>" --environment antigravity

# Apply the installation
python helpers/install.py --target "<project-root>" --environment antigravity --apply
```

Flags:
- `--environment`: Target host family (`codex`, `cursor`, `antigravity`). Repeat for multiple hosts.
- `--profile`: Optional language or architectural guidance (`python`, `typescript`, `local`, `web`). Default is no profile.

### 3. Verify Installation Integrity

Target repositories do not require a separate Remora checkout. Run the vendored helper directly:

```bash
# Verify local manifest and SHA-256 digest consistency
python .remora/helpers/install.py --check --target .

# Verify against a trusted external source revision
python .remora/helpers/install.py --check --target . --source "<trusted-distribution>"
```

Exit codes: `0` = verified clean, `1` = integrity or conflict failure, `2` = invalid invocation.

---

## Lifecycle Operations

### Safe Updates

Updates require both the previous source and desired target distribution:

```bash
# Generate preview and plan digest (read-only)
python "<new-distribution>/helpers/install.py" --target "<project>" --update --previous-source "<old-source>"

# Apply update with explicit plan verification and mandatory backup
python "<new-distribution>/helpers/install.py" --target "<project>" --update --previous-source "<old-source>" \
  --apply --expect-plan "<plan-sha256>" --backup "<backup-dir-outside-project>"
```

### Clean Removal

Removal removes only managed Remora assets, leaving project guidance and source code untouched:

```bash
python "<matching-distribution>/helpers/install.py" --target "<project>" --remove --previous-source "<matching-source>" \
  --apply --expect-plan "<plan-sha256>" --backup "<backup-dir-outside-project>"
```

Before mutations occur, the helper writes before-images to the backup location. Consult the [recovery guide](compatibility/recovery.md) for manual restoration procedures if interrupted.

---

## Repository Verification

Run the validation suite locally with Python 3.11+:

```bash
# Validate local Markdown file links
python tools/check_content.py

# Execute deterministic test suite (60 tests across real Git checkouts)
python -m unittest discover -s tests

# Verify Git formatting and whitespace
git diff --check
```

See the [evaluation guide](evals/README.md) for empirical trial rubrics, fixture scenarios, and evaluation methodology. The [specification](docs/product-spec.md) defines architectural requirements and behavioral contracts.

---

## License

This project is licensed under the terms of the [MIT License](LICENSE).
