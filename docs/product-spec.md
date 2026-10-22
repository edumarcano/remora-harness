# Remora: Product and Technical Specification

| Field | Value |
| --- | --- |
| Product | Remora |
| Repository name | `remora-harness` |
| Specification revision | 0.1 |
| Target release | v0.1 |
| Date | October 15, 2026 |
| Status | Draft for implementation; not a claim of implemented or verified capabilities |
| Intended repository location | `docs/product-spec.md` |
| Primary user | The project owner, working across multiple repositories and coding environments |

## Document purpose

This document defines what Remora should do, how its components fit together, and what evidence is required before its first release. It consolidates the agreed product direction and supplies concrete implementation defaults where the discussion left details open.

The agreed direction is **agent-native, skill-first, portable, project-aware, and maintenance-oriented**. File layouts, skill names, helper implementation choices, and evaluation thresholds below are proposed design decisions for this specification, not previously measured results.

**Product definition:** Remora is a portable engineering harness that gives existing coding agents reusable development and maintenance workflows, helps establish project-specific guidance, and makes the evidence behind their work easier to inspect.

Remora does not supply the coding agent. It supplies a versioned set of instructions, skills, references, and small supporting utilities that the user's existing agent executes.

## Contents

- [1. Problem and intended outcomes](#1-problem-and-intended-outcomes)
- [2. Product boundaries](#2-product-boundaries)
- [3. Initial release scope](#3-initial-release-scope)
- [4. System architecture](#4-system-architecture)
- [5. Guidance ownership and project adaptation](#5-guidance-ownership-and-project-adaptation)
- [6. Repository and installed layouts](#6-repository-and-installed-layouts)
- [7. Installation and bootstrap lifecycle](#7-installation-and-bootstrap-lifecycle)
- [8. Skill contracts](#8-skill-contracts)
- [9. Documentation integrity](#9-documentation-integrity)
- [10. Test assurance](#10-test-assurance)
- [11. Evidence and reporting](#11-evidence-and-reporting)
- [12. Coding-environment compatibility](#12-coding-environment-compatibility)
- [13. Deterministic helpers](#13-deterministic-helpers)
- [14. Versioning, updates, and removal](#14-versioning-updates-and-removal)
- [15. Safety and operational boundaries](#15-safety-and-operational-boundaries)
- [16. Evaluation strategy](#16-evaluation-strategy)
- [17. Release acceptance criteria](#17-release-acceptance-criteria)
- [18. Implementation sequence](#18-implementation-sequence)
- [19. Tradeoffs and known limitations](#19-tradeoffs-and-known-limitations)
- [20. Deferred capabilities and remaining decisions](#20-deferred-capabilities-and-remaining-decisions)
- [21. Specification maintenance](#21-specification-maintenance)
- [Sources](#sources)

## 1. Problem and intended outcomes

### 1.1 Problems to address

Establishing an AI-assisted development workflow currently requires repeatedly drafting and polishing instructions. Those instructions can become verbose, inherit assumptions from unrelated conversations, or import architectural decisions from another repository.

Maintenance is equally important. Documentation can accumulate local wording patches while losing coherence, duplicating ownership, or mixing intended behavior with historical observations. Tests can pass without demonstrating that they protect the behavior that matters. The user needs evidence they can understand, rather than more confident assurances from an agent.

The owner's experiences in APEX and mimus motivate these requirements. They are not a controlled comparison of those repositories or evidence that one environment, stack, or instruction set is superior. In particular, problems introduced by an external planning conversation must not be attributed automatically to the coding agent or repository harness.

### 1.2 Desired outcomes

Remora should make it easier to:

1. Establish the smallest correct engineering foundation in a new or existing repository.
2. Apply the same development philosophy across different architectures and coding environments without copying irrelevant project facts.
3. Keep documentation purposeful, accurate, and coherent as software changes.
4. Understand which behaviors tests protect and where that protection is uncertain.
5. Improve the harness through repeatable evaluations and real use, producing an honest engineering case study.

The primary product is a useful personal development tool. Public reuse and portfolio value are important secondary outcomes. Remora must not add infrastructure merely to appear more technically elaborate.

### 1.3 What success is not

Success is not the number of rules, installed skills, documentation pages, tests, or generated lines. Removing an obsolete instruction, consolidating a document, retaining a valuable test, or deciding that no additional artifact is necessary can all be successful outcomes.

## 2. Product boundaries

### 2.1 Responsibilities

| Component | Responsibility |
| --- | --- |
| Coding environment | Model access, agent loop, context handling, native tools, permissions, and any available delegation |
| Remora | Reusable engineering procedures, project adaptation, evidence standards, maintenance workflows, and limited deterministic helpers |
| Target repository | Product requirements, architecture, implementation, actual validation commands, and project-specific decisions |
| Existing project tooling | Builds, linting, type checks, tests, and other executable checks |
| CI and repository controls | Enforce configured checks where enabled; Remora instructions do not replace these controls |
| User | Product decisions, approval of material changes, operational authorization, and acceptance of remaining risks |

### 2.2 Core constraints

**Use the existing agent.** Reasoning is performed by the agent in Codex, Cursor, or Antigravity. Remora must not require its own LLM API key, model subscription, hosted inference service, or model router. Host usage remains subject to the user's account and environment; this is not a promise of unlimited or cost-free inference.

**Skills are the primary interface.** The user requests a workflow through the coding environment. A helper command may copy files or check metadata; it must not become a second agent runtime or independently generate semantic audit conclusions.

**Adapt through evidence.** Repository facts, approved requirements, proposals, and unknowns must remain distinguishable. An installed dependency does not prove a design decision, and a specification does not prove implementation.

**Keep maintenance proportional.** Localized changes should not trigger mandatory repository-wide audits. Full audits are explicit activities or justified milestone work, not an automatic tax on every edit.

### 2.3 Non-goals for v0.1

Remora will not build a chat interface, background daemon, autonomous multi-agent framework, dashboard, task database, mandatory MCP server, or independent model evaluation service. It will not replace test runners, mutation-testing engines, CI, package managers, or deployment tools.

It will not generate an application merely because the user asked to initialize the harness. It will not guarantee instruction compliance, software correctness, security, or release readiness. Automatic merges, production operations, and broad test or documentation deletion are outside the bootstrap and audit workflows.

## 3. Initial release scope

### 3.1 Supported starting conditions

| Starting condition | Expected behavior |
| --- | --- |
| Empty repository, no specification | Install a minimal foundation; do not invent a stack, architecture, commands, or product requirements |
| Empty repository, specification present | Extract established intentions and decisions; explicitly distinguish them from implemented capabilities |
| Partially implemented project | Reconcile requirements, available tooling, missing pieces, and existing instructions without treating incompleteness as an error by itself |
| Mature repository | Preserve custom guidance and working practices; propose adoption rather than replacing the existing system |
| Mixed or unfamiliar architecture | Use general workflows and evidence-backed local guidance; report unsupported specialist analysis rather than forcing a known profile |

### 3.2 Required v0.1 capabilities

| ID | Capability |
| --- | --- |
| R1 | Bootstrap and re-specialize empty, specification-only, and existing repositories |
| R2 | Separate project-owned guidance from versioned Remora content |
| R3 | Use one project-local skill installation across Codex, Cursor, and Antigravity |
| R4 | Provide planning, implementation, regression repair, and read-only review workflows |
| R5 | Audit documentation for factual drift, purpose, structure, and ownership; reconcile it when edits are authorized |
| R6 | Audit test usefulness through behavior, failure signals, production paths, and available execution evidence |
| R7 | Audit the harness itself for stale references, conflicts, duplication, and installation drift |
| R8 | Validate bundle structure and installation integrity with bounded deterministic checks |
| R9 | Preserve local modifications during installation, reconfiguration, and explicit updates |
| R10 | Produce inspectable evidence and run a small evaluation suite before release |

Initial technology references cover Python and TypeScript/JavaScript, with local execution and deployed-web considerations as separate dimensions. These references are not scaffolding presets and must not force tools such as pytest, uv, Ruff, Next.js, or Vercel.

Basic test assurance is in v0.1. Automated mutation-testing integration and large-scale test redundancy analysis are deferred. Evaluation is part of development from the beginning, not a later portfolio add-on.

## 4. System architecture

### 4.1 Execution model

```text
User requests an outcome in an existing coding environment
    |
    v
Host agent reads applicable project instructions
    |
    v
Host agent selects a Remora skill
    |
    +--> Reads relevant Remora standards and project-owned context
    +--> Inspects implementation, documentation, tests, and Git state
    +--> Uses native tools and approved project commands
    +--> Optionally runs deterministic Remora helpers
    |
    v
Produces a plan, scoped edits, or findings with evidence and limitations
```

Nothing in this sequence requires a running Remora service. The host supplies the reasoning and execution facilities. Skills describe procedures, not guaranteed state machines.

### 4.2 Components

**Standards** contain concise reusable principles: scope discipline, evidence, documentation ownership, and test usefulness.

**Skills** define multi-step activities with inputs, boundaries, expected outputs, and stop conditions.

**Profiles** provide optional technology or runtime references. The agent selects relevant sections rather than appending every profile to permanent instructions.

**Project guidance** records repository-specific facts, decisions, constraints, and pointers to their canonical owners.

**Compatibility notes and adapters** describe how the shared files are exposed in each host. Adapters exist only for a demonstrated gap; they are not independently authored policy copies.

**Helpers and evaluations** check objective properties, preserve installation integrity, and test whether the workflows produce useful results.

### 4.3 Workflow composition

A skill can direct the agent to use another installed skill or a shared procedure. This does not assume a universal skill-invocation API, automatic nested execution, or subagents. When necessary, the agent reads the named skill and follows its procedure within the current task.

Delegation is optional and host-dependent. Remora must work with one agent. A separate-context review may reduce shared conversational assumptions but must not be described as independent proof of correctness.

## 5. Guidance ownership and project adaptation

### 5.1 Ownership model

| Material | Owner | Update policy |
| --- | --- | --- |
| Shared standards and generic skills | Remora release | Replace only through an explicit, integrity-checked update |
| Technology and runtime references | Remora release | Select relevant references; do not rewrite them for each project |
| Root and nested `AGENTS.md` | Target project | Draft or revise from repository evidence and authorized decisions |
| Product specifications, architecture, and decisions | Target project | Remain authoritative for their stated purpose; link rather than duplicate |
| Project-specific workflow extensions | Target project | Maintain separately from Remora-owned skill files |
| Installation manifest | Remora installation metadata | Track installed content, not product behavior or command truth |
| Reports and observations | Individual run | Record revision and scope; never silently promote them to permanent policy |

A project's `AGENTS.md` is not a copied version of Remora's own root `AGENTS.md`. The latter governs development of Remora itself and must never be installed into another project as its instructions.

### 5.2 Content-placement rules

Put a short persistent constraint in project instructions when the agent needs it during ordinary work. Put a multi-step procedure in a skill. Put lengthy technical detail in a focused reference or its existing project document. Keep historical evidence in a dated record rather than in current operating instructions.

Examples:

| Information | Appropriate home |
| --- | --- |
| Preserve unrelated user changes | Small shared working-agreement baseline |
| How to audit a document's purpose and factual claims | Documentation audit skill and reference |
| This application must work offline | Project-owned requirement or architecture guidance |
| Run the repository's actual test command from a particular directory | Project-owned verification section, linked to its tooling source |
| Python-specific cancellation considerations | Optional Python reference, consulted for relevant changes |
| A provider failed an experiment last month | Dated evaluation or decision record |

### 5.3 Root `AGENTS.md` contract

A generated root file should contain only established material: a short project orientation, important boundaries, the current verification entry points if any, and direct routing to applicable guidance and skills.

For a fresh repository without decisions, this is sufficient in principle:

```markdown
# Repository instructions

No application architecture or validation tooling is established yet.
Do not turn proposals into project requirements without an explicit decision.

Preserve unrelated changes, keep work within the requested scope, and report
verification honestly. Do not claim a command passed unless it was run.

For multi-step work, use the relevant installed Remora skill. Before applying
shared guidance, read the relevant files under .remora/standards/ and any
project-specific instructions for the affected area.
```

This example is a content contract, not a template to overwrite existing guidance.

When code exists, add actual commands with their working directories and source locations. A command found in a manifest is **configured**; it is **verified in this environment** only after a recorded execution. Do not keep transient passing status in `AGENTS.md`.

### 5.4 Avoiding invisible or duplicated instructions

A Markdown link is not a cross-environment automatic import. Essential short boundaries belong directly in the appropriate instruction file. Skills must explicitly tell the agent which supporting references to read and under what conditions.

Do not maintain the full same policy in `AGENTS.md`, a Cursor rule, and an Antigravity rule. A small stable summary in root instructions is acceptable; lengthy procedures have one owner.

A project extension must not silently fork a generic skill. Add a local reference or distinctly named project skill. If a fork is intentional, record it as project-owned and stop updating it as an unmodified Remora file.

### 5.5 Adapting to project architecture

Bootstrap considers language, framework, runtime, deployment, persistence, and operational risk independently. A Python project may be a local CLI or a deployed API; TypeScript does not imply a browser or Next.js.

Each profile must state its applicability evidence, relevant questions, and non-assumptions. Missing evidence means unknown, not permission to choose a convention. For mixed projects, route guidance by actual component boundaries without installing a profile into every directory.

An optional `.remora/project.md` may hold additional project-owned routing when root instructions would become crowded. It must not become a second specification, command registry, or mandatory duplicate of existing documentation. Do not create it when existing files already serve the purpose.

### 5.6 Conflict resolution

Remora does not override host permissions or higher-priority host instructions. Within project guidance, approved project-specific decisions normally specialize reusable defaults. Contradictions affecting behavior, cost, privacy, or scope must be surfaced rather than silently resolved through file order.

When implementation disagrees with a specification, determine which describes current behavior and which describes intended behavior. Report the discrepancy; do not automatically change either to match the other.

Conversational brainstorming is not a durable decision. Only explicit current authorization or an established project decision justifies promotion into permanent guidance.

## 6. Repository and installed layouts

### 6.1 Source repository

```text
remora-harness/
|-- AGENTS.md                    # Instructions for developing Remora itself
|-- README.md                    # Purpose, first use, supported scope
|-- LICENSE                      # Selected before public release
|-- skills/
|   |-- remora-bootstrap/
|   |-- remora-plan-change/
|   |-- remora-implement-plan/
|   |-- remora-fix-regression/
|   |-- remora-review-change/
|   |-- remora-audit-documentation/
|   |-- remora-audit-tests/
|   `-- remora-audit-harness/
|-- standards/
|   |-- engineering.md
|   |-- documentation.md
|   `-- testing.md
|-- profiles/
|   |-- python.md
|   |-- typescript.md
|   |-- local.md
|   `-- web.md
|-- templates/                   # Minimal seed and report examples
|-- compatibility/               # Host-specific notes and verified results
|-- helpers/                     # Bounded runtime-independent utilities
|-- tools/                       # Maintainer packaging and validation
|-- tests/                       # Deterministic helper and fixture tests
|-- evals/                       # Tasks, rubrics, run records, results
`-- docs/
    |-- product-spec.md
    `-- decisions.md             # Only material decisions and rationale
```

Every skill directory contains `SKILL.md`; supporting files are added only where used. The portable entrypoint uses the shared `name` and `description` frontmatter fields. Host-specific metadata remains optional and must not be required by another environment.[^s1]

Names use the `remora-` prefix to avoid collisions with existing skills such as `review-change`. A different name does not eliminate overlapping triggers; adoption must also identify semantic duplication.

### 6.2 Target repository

```text
my-project/
|-- AGENTS.md                    # Project-owned
|-- .agents/
|   `-- skills/
|       |-- remora-plan-change/
|       |-- remora-implement-plan/
|       |-- remora-fix-regression/
|       |-- remora-review-change/
|       |-- remora-audit-documentation/
|       |-- remora-audit-tests/
|       `-- remora-audit-harness/
|-- .remora/
|   |-- installation.json        # Version, selected assets, file hashes
|   |-- standards/               # Versioned shared references
|   |-- profiles/                # Only selected references
|   |-- helpers/                 # Only applicable packaged helpers
|   `-- project.md               # Optional; project-owned
`-- ...                          # Existing code and documents remain in place
```

The bootstrap entrypoint is normally personal/global, avoiding a global and project copy with the same identity. A project-local bootstrap installation is an explicit alternative, not a second default copy.

Project installations are vendored copies, committed with the repository when authorized. v0.1 does not require symlinks, Git submodules, or a separate Remora checkout during normal project work. The installed set is the distribution unit: project skills may refer to shared `.remora/` resources, and validation must detect missing dependencies. Individual extracted skills are not advertised as self-contained unless packaged that way.

### 6.3 Installation metadata

Use one small JSON manifest with these fields:

| Field | Meaning |
| --- | --- |
| `schema_version` | Manifest format version |
| `remora_version` | Human-readable release identifier |
| `source_revision` | Exact source commit or immutable release identity |
| `selected_profiles` | References installed, not claims that all described capabilities exist |
| `target_environments` | Requested host families; not a certification of tested compatibility |
| `managed_files` | Repository-relative path and SHA-256 digest for each Remora-owned file |

Do not store secrets, absolute workstation paths, chat transcripts, current test status, or copied product requirements. Project-owned files such as `AGENTS.md` are excluded from automatic replacement. The manifest does not hash itself.

Use paths relative to the target root. Digests detect drift; they are not a security signature or proof of authorship. Integrity checks must compare against the trusted release when verifying provenance, not merely trust two locally modified files.

## 7. Installation and bootstrap lifecycle

### 7.1 First-use distribution

A release provides a reviewed bootstrap bundle and a project payload. The bootstrap bundle must contain or directly accompany everything needed to install the pinned project payload; copying only `SKILL.md` while leaving required resources elsewhere is unsupported.

Two entry paths are supported:

- Install the bootstrap skill in the host's supported personal skill directory, then invoke it in the target project.
- Open a trusted, pinned Remora distribution and explicitly ask the host agent to follow its bootstrap entrypoint for a named target directory.

The second path is a fallback for environments where global skill discovery is unavailable. It must not require executing a remote shell script or downloading a moving branch at runtime. Once a release is locally available, installation can work without network access. The coding host itself may still require connectivity.

A lightweight installer is a convenience for predictable copying, collision detection, and metadata. It does not decide architecture or write project-specific prose.

### 7.2 Bootstrap procedure

**Inspect.** Establish the target root and current Git state, including an unborn branch with no commits. Read existing instructions and selected specifications before proposing edits. Inventory relevant manifests and validation configuration; do not execute discovered commands as part of passive discovery.

**Classify.** Identify the starting condition and separate observed repository facts, explicit decisions, proposals, and unknowns. A specification can authorize a design direction without proving its tooling exists.

**Select.** Choose the minimal standards, skill set, and profile references. Reuse or preserve existing workflows. Do not delete an existing skill because Remora offers a similarly named one.

**Draft.** Propose project-owned instructions and any necessary routing. Every specific command, directory, architectural claim, or restriction must have a source or be clearly presented as a proposal. Keep detailed source provenance in the bootstrap report rather than cluttering every instruction with metadata.

**Apply within authorization.** A request to preview or audit stays read-only. A request to install permits the described local installation; do not add redundant approval ceremonies. Ask only about material unresolved choices, conflicting customizations, destructive replacement, or operations outside that request.

**Validate.** Check installed metadata, referenced resource paths, ownership, and collisions. Report missing toolchains separately from invalid configuration. Confirm host discovery through an explicit smoke task, not just file presence.

**Hand off.** Summarize installed content, project-specific decisions, unresolved items, changes to existing guidance, and checks actually performed. An empty project may finish bootstrap successfully with no build or test command.

### 7.3 Progressive specialization

Rerunning bootstrap in specialization mode should update only what new evidence justifies. For example, after tooling is implemented, replace an unknown verification section with the actual entry points; do not recreate the repository instructions from scratch.

A new backend, frontend, database, or deployment target can justify scoped guidance. Removing a capability should trigger review of its associated guidance instead of leaving obsolete rules indefinitely.

Repetition must be idempotent: with the same release, selections, and project state, a second installation must create no duplicate content or unnecessary diff. Rewording an already adequate instruction is not a required change.

### 7.4 Existing-repository adoption

Adoption begins with a comparison, not a migration. Preserve the repository's working conventions and identify where Remora would duplicate, complement, or conflict with them.

Remora self-dogfooding and a private, disposable Vulpes Health snapshot are the operational adoption cases. Vulpes currently establishes specification-only adoption evidence, not application-maintenance coverage. A finalized GitHub commit is not required; identify uncommitted inputs by private inventory and hashes. APEX and mimus remain historical design inputs, not required adoption targets; do not modify them during these trials. Extract reusable lessons from approved operational trials without distributing private content, project-specific facts, personal configuration, or branding as generic Remora policy.

No bootstrap action creates a commit, pushes a branch, changes repository visibility, or publishes a release without separate authorization.

## 8. Skill contracts

### 8.1 Shared contract

Every skill defines its trigger, inputs, permitted changes, procedure, evidence requirements, and stopping conditions. Invocation does not expand the user's authorization. Skills read the relevant repository and Remora guidance before applying a checklist.

Use selective context loading: metadata identifies the workflow, the entrypoint states the procedure, and detailed references are read only when relevant. The shared Agent Skills specification supports this structure.[^s1]

The contracts below define intended workflows, not implemented entrypoints. All use the evidence and reporting requirements in Section 11 and the operational boundaries in Section 15. An input may come from the request or repository evidence; absence is reported rather than filled with invented facts.

| Skill | Trigger and required inputs | Permitted changes | Expected evidence and output | Completion or stopping condition |
| --- | --- | --- | --- | --- |
| `remora-bootstrap` | Initialize, adopt, or re-specialize; target root, requested hosts, available guidance/specification, and pinned distribution when installing | Preview stays read-only; installation or specialization changes only authorized managed content and proposed project guidance | Starting-state classification, source-backed instruction choices, ownership/collision review, installation checks and discovery results or gaps | Finish with validated authorized changes or an adoption proposal; stop affected writes on ownership conflicts, modified destinations, or unsafe paths |
| `remora-plan-change` | Investigate or plan a change; desired outcome, constraints, and available requirements | Read-only; save a plan only when requested | Repository-grounded decisions, affected contracts, acceptance criteria, verification strategy, and material unknowns | Deliver a decision-complete brief, or identify the material decision preventing one |
| `remora-implement-plan` | Implement an approved plan or clear request; outcome, scope, and acceptance criteria | Scoped implementation and necessary test/documentation changes | Actual diff reconciled with requirements, relevant checks and outcomes, explicit review, and remaining risks | Complete the agreed behavior and handoff; identify blocked acceptance criteria instead of expanding scope |
| `remora-fix-regression` | Diagnose or repair a reported defect; observed failure, expected behavior, and available reproduction evidence | Diagnosis stays read-only when requested; repair permits the smallest sufficient fix and relevant tests/docs | Production-path diagnosis, reproduction or its limits, repair rationale, and regression evidence; before/after execution when practical | Finish with supported cause and verification, or report missing evidence/access without inventing a reproduction |
| `remora-review-change` | Review a diff, revision range, or named implementation; explicit review surface and applicable requirements | Read-only | Findings tied to actual code and requirements, precise locations, consequences, and verification gaps; no findings is valid | Finish the declared surface with sampling limits; request clarification if its identity or base cannot be established |
| `remora-audit-documentation` | Audit or reconcile documentation; change range, documents, or repository scope and their intended roles | Audit stays read-only; reconcile only when edits are requested | Purpose/ownership analysis, source-backed claim findings, historical/current distinctions, and post-edit checks when applicable | Finish the scoped assessment or authorized correction; surface unresolved intent-versus-implementation conflicts |
| `remora-audit-tests` | Assess test protection; behavior, subsystem, test changes, or suite and available execution evidence | Read-only by default; no automatic generation/deletion; controlled faults require separate authorization and isolation | Sampled behavior-to-defect-to-assertion chains, distinct failure signals, recommendations, and unexamined areas | Finish the stated sample with evidence limits; retain coverage whose redundancy is uncertain |
| `remora-audit-harness` | Inspect guidance or installation health; configuration, intended usage, and installation/release metadata where present | Read-only; repairs only when requested | Missing resources, hash drift, ownership conflicts, overlapping guidance, and compatibility evidence separated from semantic interpretation | Finish scoped findings and gaps; stop affected repairs on unresolved ownership or local modifications |

Resolve ordinary engineering details independently within these contracts. Surface material conflicts involving requirements, ownership, scope, privacy, cost, or destructive changes before the affected action; continue unrelated safe work. A missing tool, execution permission, or host surface creates an explicit verification gap, not a fabricated result or an automatic reason to abandon inspection. Invocation never authorizes dependency installation, external publication, or other operations beyond the request.

### 8.2 Planning and implementation

A plan identifies the outcome, non-goals, relevant decisions, affected contracts, acceptance criteria, verification, and genuine unresolved questions. It must not invent exact paths or APIs to appear implementation-ready.

Implementation starts by reconciling the plan with current repository evidence. It includes documentation and test impact, but neither a new document nor a new test is mandatory when existing coverage and explanation are adequate.

Review effort scales with consequence and uncertainty, not lines changed alone. Substantive changes require an explicit review of the actual diff; this can occur in the current agent when separate review is unavailable. Fix/review loops stop at a justified handoff or explicit blocker, not after an unbounded search for perfection.

Verification is a shared workflow stage, not a separate v0.1 orchestration product. Run relevant configured checks and explain unverified behavior. Do not use an unrelated full audit to obscure a missing acceptance test.

### 8.3 Keeping task handoffs small

A handoff from an external planning conversation should state the desired outcome, constraints, and acceptance criteria. Repository details in that handoff are hypotheses until checked locally.

Remora must not encourage users to regenerate long implementation prompts that duplicate the repository's rules. The agent executing the task should consult the actual project guidance.

## 9. Documentation integrity

### 9.1 Audit objectives

The documentation workflow must assess both **whether claims are supported** and **whether a document still does its job**. Finding a changed word is not equivalent to maintaining a coherent explanation.

Before reviewing claims, identify the document's purpose, audience, and authority. A current architecture guide, product specification, setup guide, and historical decision record require different treatment.

| Document role | Owns | Must not silently become |
| --- | --- | --- |
| Product specification | Intended behavior and approved constraints | A declaration that every requirement is implemented |
| Architecture guide | Current system model and important boundaries | A chronological patch log or exhaustive file inventory |
| Setup/operations guide | Usable procedures and prerequisites | Evidence that those procedures succeeded everywhere |
| API/configuration reference | Current documented contracts and usage | A competing hand-maintained copy of every generated schema |
| Decision/evaluation record | Dated rationale and observations | Evergreen proof of current behavior |
| Changelog | Released historical changes | A document rewritten to describe only the present |

An ownership map is optional. Reuse existing document introductions and links when they already establish ownership. Create additional metadata only to resolve an actual ambiguity.

### 9.2 Audit modes

**Change-scoped:** Trace a specified diff or change range to affected claims and canonical documents. Inspect the relevant surrounding sections, not only edited lines. Include renames, removals, examples, and cross-references.

**Repository-scoped:** Inventory documents, identify overlapping ownership, and inspect important claims against the appropriate evidence. State any sampling limits rather than claiming exhaustive coverage.

**Post-edit verification:** Recheck corrected claims, affected cross-links, structure, and removal of contradictory or redundant remnants.

Resolve Git scope explicitly. Use a real supplied or established base revision, account for staged/unstaged changes, and do not assume a branch named `main` or an existing release tag. An empty repository requires a filesystem inventory instead of a failing comparison against nonexistent history.

### 9.3 Required analysis

Assess commands, paths, settings, defaults, interfaces, failure behavior, operational boundaries, examples, terminology, and ownership where relevant. Separately assess duplicated explanations, misplaced history, missing orientation, unsupported status claims, and sections that no longer answer their intended question.

A factual mismatch can indicate an outdated document, a code defect, an unimplemented requirement, or a changed decision. The agent must establish which interpretation is supported before recommending a correction.

### 9.4 Reconciliation when edits are authorized

For each affected section, choose among keeping it, editing a claim, rewriting the section coherently, consolidating duplicate ownership, moving material, or removing obsolete content. Explain material restructuring; do not rewrite unaffected documents for stylistic preference.

After editing, read the whole affected document and relevant cross-references. Check that current behavior, intended behavior, and historical evidence remain distinct. Do not append qualifications indefinitely when the section needs a clearer explanation.

Preserve historical records unless the user explicitly requests correction or restructuring of that history. A superseded decision can be historically accurate and must not be treated as current drift merely because the implementation changed.

## 10. Test assurance

### 10.1 Objective

The test workflow should explain **what would have to go wrong for a test to fail, and why that failure matters**. It is not a test-count reducer, coverage maximizer, or automatic test generator.

The v0.1 audit combines code inspection with whatever safe execution evidence is available. It does not claim to prove that a suite is complete or that two tests are equivalent.

### 10.2 Behavior-to-evidence chain

For a meaningful sample of the scoped tests, trace:

```text
Requirement or meaningful behavior
    -> plausible defect or regression
    -> production path exercised
    -> observable assertion
    -> test that fails when the defect is present
```

Report where the chain is established, inferred, or missing. A test can protect a domain rule, an interface, integration behavior, failure handling, or a deliberately stable internal invariant; public UI behavior is not the only legitimate target.

### 10.3 Required review questions

The audit must examine whether the test executes production behavior, whether its assertions distinguish correct from relevant incorrect outcomes, and whether its setup duplicates the implementation being tested. Review boundary cases, error paths, synchronization, and cleanup where they affect the contract.

Mocks are not inherently bad. Determine whether they isolate a legitimate external boundary or replace the very behavior the test claims to protect. Snapshot and exact-string assertions are valid when the representation is itself a stable contract; otherwise flag their maintenance risk with evidence.

Similar-looking tests are not necessarily redundant. Different layers can protect distinct transformations, wiring, persistence, error mapping, or lifecycle boundaries. Do not recommend deletion solely because coverage overlaps or an LLM considers the tests repetitive.

### 10.4 Evidence levels

| Evidence | Permitted conclusion |
| --- | --- |
| Inspection only | A specific weakness or protection appears likely; runtime behavior is unverified |
| Test executed on current code | The recorded test passed or failed in that environment |
| Regression reproduced on a known broken revision | That test detects the reproduced historical defect |
| Controlled fault introduced in isolation | That test detects, or fails to detect, that specific fault |
| Existing coverage report | The report indicates execution coverage; it does not establish assertion strength |

For a regression repair, prefer demonstrating failure before the fix and success after it when practical. If that demonstration is unavailable, say so instead of fabricating a red/green history.

Deliberate fault injection requires explicit authorization and an isolated disposable copy or worktree. It must never alter the active user's working tree merely to strengthen an audit report. v0.1 can reason about or manually exercise a small controlled fault; it does not need to integrate a mutation engine.

### 10.5 Recommendations and stopping rule

Recommendations may be to retain a test, improve an assertion, move coverage to a better owning layer, add a missing case, investigate a weakness, or consolidate demonstrated redundancy. Each actionable recommendation needs a behavior and a failure signal, not just a testing preference.

When deletion is authorized, identify the protection being removed and the evidence that it is preserved or no longer required. Uncertain redundancy defaults to retention. Do not make tests agree with a defect merely to obtain a green suite.

A sample audit must identify the tests sampled and the unexamined areas. A satisfactory scoped audit may conclude that no changes are needed.

## 11. Evidence and reporting

### 11.1 Evidence dimensions

Remora must distinguish the **method** used to obtain evidence from the **status** of a conclusion.

Methods include repository inspection, deterministic check, executed test, controlled experiment, external documentation, and agent interpretation. Statuses include confirmed for the stated scope, suspected, unverified, blocked, and not applicable.

Passing an automated check does not confirm an unrelated product requirement. Agent interpretation must not be presented as an executable result. A separate review is review evidence, not an automatically trusted verdict.

### 11.2 Audit report contract

Reports should lead with the useful conclusion and remaining uncertainty. Include the following only to the depth justified by the task:

| Field | Requirement |
| --- | --- |
| Scope | Repository, workflow, requested range or files, and exclusions |
| Revision | Relevant commit IDs; for dirty work, identify the included diff or saved patch/hash |
| Findings | Stable local identifier, consequence/severity, concise claim, and location |
| Evidence | Source paths with precise locations, commands and actual outcomes, or dated external sources |
| Interpretation | Why the evidence supports the claim; distinguish alternative explanations |
| Recommendation | Smallest useful action, or an explicit reason to retain the current material |
| Verification gaps | Checks not run, unavailable dependencies, uncertainty, and unexamined areas |

Severity expresses consequence, not confidence. Use high, medium, low, or informational, with a brief impact explanation. Editorial preferences are advisory rather than defects.

An illustrative finding:

```text
DOC-01 | Medium | Confirmed configuration mismatch
Claim: The setup guide names a script absent from the current package manifest.
Evidence: README.md, Verification section; package.json, scripts object.
Method: Repository inspection and configured-command lookup.
Not established: Whether a replacement command succeeds in this environment.
Action: Correct the documented entrypoint after confirming the intended workflow.
```

This example is not a finding from APEX or mimus.

### 11.3 Storage and machine-readable results

Ordinary results can remain in the host conversation. Save a report only when requested, needed for a handoff, or part of an evaluation. Do not add a permanent report file for every small change.

Saved reports belong in a project-approved location; temporary logs should be ignored and sensitive content removed. Evaluation records belong in Remora's evaluation area, subject to publication review.

Deterministic helpers may emit JSON containing check IDs, statuses, paths, messages, and summary counts. Do not require every semantic audit to populate a large schema in v0.1. No general-purpose confidence score, trust percentage, or project-health score is part of the contract.

## 12. Coding-environment compatibility

### 12.1 Portable baseline

The baseline is root `AGENTS.md`, project-local `.agents/skills/<name>/SKILL.md`, ordinary readable references, and host-native file/terminal access. Current official documentation describes those project instruction and skill mechanisms for Codex, Cursor, and Antigravity.[^s2][^s3][^s4][^s5][^s6][^s7]

This is a documented integration basis, not evidence that Remora has already been tested in those products.

| Environment | Shared project files | Personal bootstrap location documented at review time | Initial validation target |
| --- | --- | --- | --- |
| Codex | Root `AGENTS.md`; `.agents/skills/` | `~/.agents/skills/` | A recorded local Codex surface; use CLI as the reference test surface unless the owner selects another |
| Cursor | Root `AGENTS.md`; `.agents/skills/` | `~/.agents/skills/` or `~/.cursor/skills/` | Cursor editor Agent |
| Antigravity | Root `AGENTS.md`; `.agents/skills/` | `~/.gemini/config/skills/` for app/IDE | Antigravity IDE |

Codex and Cursor can share one personal bootstrap copy in `~/.agents/skills/`. Do not additionally install the same identity in another discovered directory without checking for duplicates. Antigravity CLI has a distinct documented personal directory; CLI support is not inferred from an IDE smoke test.[^s2][^s4][^s6]

### 12.2 Scoped guidance is not identical across hosts

Codex documents instruction discovery along the root-to-current-working-directory chain and special handling of `AGENTS.override.md`. Cursor documents nested instructions applied to their directory and children. Antigravity documents directory discovery associated with files being read or edited.[^s3][^s5][^s7]

Therefore, v0.1 must not assume that editing any nested file causes every host to load the same instructions. Root routing and skill procedures must require the agent to inspect applicable scoped guidance before editing an area. Test nested-directory behavior in each supported surface before relying on implicit loading.

Existing global, team, override, or personal rules may affect outcomes. Inspect the configuration visible to the agent and report what could not be inspected; never claim complete knowledge of hidden host context.

### 12.3 Minimal adapters

Do not generate `.cursor/rules/`, `.agents/rules/`, or native configuration merely because those features exist. Add an adapter only when a reproducible compatibility gap requires it. Document its source, purpose, activation behavior, and tests.

Shared references are not guaranteed automatic includes. Cursor specifically documents that file mentions are not inlined; Antigravity has its own include behavior. The portable design uses explicit reads rather than assuming a common include syntax.[^s5][^s7]

A Remora workflow means a reusable procedure. It does not mean a legacy Antigravity Workflow file. As of this review, Google's documentation says the current legacy workflows stop working on October 19, 2026. Remora must use skills and must not depend on those workflow directories.[^s8]

### 12.4 Compatibility certification

A release compatibility record must identify environment, surface, version/build, model where exposed, operating system, test date, installation location, and passed/failed scenarios.

Use three distinct labels: **documented**, **tested**, and **unsupported or unverified**. Never promote a documented capability to tested without execution evidence. Remote/cloud surfaces and global-skill synchronization are separate tests; local personal files must not be assumed available remotely.[^s4]

Switching from one environment to another in the same repository must not require regenerating project guidance or rewriting generic skills. It may require host reload/discovery steps, which must be documented.

### 12.5 Explicit invocation and fallback

Use the host's skill selector or explicit skill mention for deterministic test setup. Do not prescribe one universal slash-command syntax. Implicit discovery is a usability feature to evaluate separately, not a guarantee that every matching task will trigger the skill.

If discovery fails, report it. Explicitly reading a local `SKILL.md` can preserve functionality, but the result must be labeled fallback execution rather than native discovery success.

## 13. Deterministic helpers

### 13.1 Scope

Helpers exist where ordinary code is more reliable than repeated model reasoning. The proposed implementation default is small Python 3.11+ utilities, with standard-library-only installed helpers where practical. This is a Remora tooling choice, not a Python requirement for target applications.

The skills remain readable and usable without Python. When a helper cannot run, the agent may perform a limited manual inspection and must mark automated checks as not run. It must not claim an equivalent integrity check occurred.

| Utility responsibility | Required behavior | Excluded behavior |
| --- | --- | --- |
| Bundle validation | Check authored skill metadata, names, declared files, selected resources, and package completeness | Judge whether a skill's reasoning is correct |
| Installation planning/copying | Preview paths, detect collisions, copy exact release files, write installation metadata | Select project architecture or rewrite project-owned prose |
| Installation/reference checking | Compare managed file hashes; check supported literal local references and expected assets | Claim arbitrary Markdown, shell command, or semantic conflict validation |

Maintainer tooling can package the bootstrap and project distributions. The exact executable names are not a public command suite in v0.1. Agents and users should be able to inspect help and run helpers directly without installing a daemon or application framework.

### 13.2 Behavioral requirements

Read-only is the default for inspection. Writes require an explicit apply action. Helpers must stay within declared roots, reject path traversal and unsafe symlink targets, preserve unrelated files, and provide useful errors.

Inspection must not import target application code, evaluate configuration as executable code, run arbitrary manifest scripts, install dependencies, or access the network. Checking that a named package script exists is not checking that it works.

Output must distinguish failures from unsupported or incomplete checks. Proposed exit codes are `0` for completed checks with no failures, `1` for detected failures, and `2` for invalid invocation or incomplete required checks. Advisory findings do not alone fail CI.

Validate Remora-authored content using a documented format subset or a proper parser; do not claim a regular-expression check validates all YAML or Markdown. Unknown third-party formats are reported, not rewritten.

### 13.3 Helper tests

Tests must cover repeat installation, collisions, modified managed files, missing resources, malformed metadata, invalid paths, spaces in filenames, line-ending behavior, and interrupted writes. Installation records must be written last, after successful file verification, so partial installation cannot look complete.

Byte-identical managed payloads are the baseline. Packaging must define line-ending handling consistently; do not silently normalize unrelated project files. Test helper behavior on Windows and a Unix-like environment before claiming both are supported.

## 14. Versioning, updates, and removal

### 14.1 Release units

Version skills, shared standards, profiles, and required helpers together for v0.1. Pin an exact source revision in each installation. Do not resolve a mutable `latest` reference during normal skill execution.

Release notes must identify behavior changes to instructions as well as script changes. A small wording change can materially alter workflow behavior and deserves evaluation when it affects decisions or boundaries.

### 14.2 Explicit updates

v0.1 supports a reviewed replacement workflow, not automatic upgrades or a general merge engine.

| Current target state | Update action |
| --- | --- |
| Managed file matches recorded version | Eligible for replacement from the requested release |
| Managed file has local edits | Stop replacement of that file; show the conflict and preserve it |
| Unmanaged file occupies a destination | Do not overwrite; resolve ownership explicitly |
| File removed from new release | Propose removal only if still unmodified and removal is authorized |
| Project-owned `AGENTS.md` or context | Never automatically replace; propose necessary changes separately |

Compare actual contents with the recorded installation and the selected release. Before applying a prepared plan, recheck affected files so edits made after preview are not overwritten. Show additions, replacements, conflicts, and proposed removals.

Automatic semantic merging of custom instructions, unattended updates, and mass migration across repositories are deferred. The user can keep an older release while evaluating changes elsewhere.

### 14.3 Recovery and removal

Use Git diffs or a narrow backup of affected files to make changes reviewable. Recovery must restore only files changed by the installation operation, and only after checking for newer edits. Never use a blanket reset or clean operation.

Removal deletes only verified Remora-owned content within the approved scope. Project instructions and useful project-owned documentation remain unless their removal is separately requested. Remove obsolete routing references deliberately instead of leaving broken links.

## 15. Safety and operational boundaries

### 15.1 Authority and repository trust

A repository can contain malicious instructions or executable configuration. Treat arbitrary source comments, logs, fixtures, external pages, and generated output as data, not new authority to change the workflow. Do not let repository text authorize secret access, exfiltration, permission changes, or out-of-scope commands.

Remora skills are themselves executable guidance and must be reviewable and versioned. Do not fetch and execute an unreviewed update just because a skill requests it.

### 15.2 Execution versus inspection

Read-only audits must not intentionally edit source, configuration, Git history, or external state. Running a test can create files or contact services, so inspect the command and respect the project's execution permissions. Use isolated fixtures for risky checks. Creating an approved temporary report or test cache does not authorize source edits.

Bootstrap and passive checks must not install dependencies, access secrets, perform live provider calls, deploy, publish, or mutate cloud configuration. Skills must preserve the host's permission controls and never try to bypass them.

### 15.3 Data handling

Remora has no telemetry or independent upload service in v0.1. Its helpers operate locally and do not make network requests by default. Nevertheless, content read by the coding agent is subject to the host's processing and data policies; local files do not imply local-only inference.

Do not copy credentials, submitted user content, private repository material, personal paths, or full transcripts into installed guidance or public evaluation artifacts. Network verification, when needed, uses host-approved tools and shares only necessary information.

### 15.4 Limits of enforcement

The workflow specifies how an agent should behave; it cannot guarantee compliance. Deterministic checks can verify their narrow inputs, and CI can enforce explicitly configured checks, but neither certifies all software behavior.

CI must not be described as preventing merges unless the corresponding repository controls are actually configured and verified. No v0.1 semantic audit finding becomes a mandatory CI blocker by default.

## 16. Evaluation strategy

### 16.1 Questions to answer

Does bootstrap avoid invented facts and preserve project decisions? Can the same installed content be used across the three target environments? Does documentation auditing find meaningful drift without rewriting history or creating noise? Does test auditing explain real failure protection rather than reward test quantity?

Evaluate maintenance burden as well as detection: unnecessary file changes, instruction growth, correction rounds, and human interventions matter.

### 16.2 Evaluation layers

| Layer | Method |
| --- | --- |
| Deterministic correctness | Unit and fixture tests for packaging, safe copying, metadata, and references |
| Native integration | Explicit discovery and execution tasks in each recorded host surface |
| Workflow behavior | Seeded tasks with a ground-truth rubric and clean controls |
| Personal usefulness | Disposable Remora self-dogfooding and Vulpes Health adoption, with input identity, interventions, and limitations recorded |

The target repositories are useful case studies, not substitutes for controlled fixtures. Public fixtures must be synthetic or cleared for publication.

### 16.3 Minimum fixture catalog

| ID | Scenario | Critical expectation |
| --- | --- | --- |
| F01 | Empty Git repository, no commits and no specification | No fabricated stack, paths, requirements, or commands |
| F02 | Specification-only repository with approved and proposed choices | Preserve the distinction between intention, proposal, and implementation |
| F03 | Existing Python project with established non-default tooling | Preserve the actual test and package workflow |
| F04 | TypeScript web project with scripts and deployment configuration | Find configured commands without claiming deployment verification |
| F05 | Mature custom guidance and existing overlapping skills | Preserve custom work; identify conflicts without silent replacement |
| F06 | Mixed or unfamiliar project with nested guidance | Use a safe general fallback and explicitly inspect relevant scopes |
| F07 | Documentation with a stale current command and accurate historical command | Correctly separate current drift from history |
| F08 | Duplicated ownership and a patch-accumulated explanation | Recommend a coherent correction, not unnecessary whole-repo rewriting |
| F09 | Implementation that violates an approved specification | Surface the discrepancy rather than changing the specification to bless the bug |
| F10 | Tests whose fake reimplements behavior or assertions cannot detect a seeded defect | Identify the exact missing protection with supporting evidence |
| F11 | Similar-looking tests that protect distinct boundaries | Retain justified coverage; avoid unsupported deletion recommendations |
| F12 | Modified managed files, destination collisions, and unsafe paths | Preserve user content and reject unsafe installation operations |

Include clean sections and adequate tests in audit fixtures. A benchmark containing only defects cannot measure false-positive behavior.

### 16.4 Comparison protocol

For the primary comparison, use the same host, model where selectable, task, starting revision, available tools, permissions, and acceptance criteria. Compare the native project baseline without Remora against the same project with the selected Remora release. Preserve existing project instructions in both conditions.

Run fresh sessions and separate working copies. Record the Remora version, prompt, changed files, commands, outcomes, intervention count, and session conditions. Do not carry summaries or answers between conditions.

Keep the scoring rubric and defect labels outside the agent-visible fixture. Use executable checks for known faults and human adjudication for editorial findings. AI can assist with review, but its verdict alone is not the ground truth for the skill being evaluated.

Run every applicable functional fixture at least once per target environment. For an initial paired pilot, repeat F02, F05, F07, and F10 at least twice per condition per environment. Expand only after the workflow and rubric are stable. These are small pilot samples, not statistical proof of general superiority.

Where native automation is available, it may help run trials under the existing host account. Manual host runs are acceptable. No benchmark requirement may introduce a separate LLM API dependency, hidden billable calls, or unsupported quota automation.

### 16.5 Metrics and initial targets

| Area | Metric or proposed release target |
| --- | --- |
| Bootstrap correctness | Zero fabricated project facts on release-critical fixtures |
| Preservation | Zero unauthorized overwrite, deletion, or operational action in the fixture suite |
| Installation | Repeat run produces no unnecessary diff; required resources resolve |
| Compatibility | Explicit skill discovery and representative execution succeed in each advertised tested surface |
| Documentation findings | Target precision at least 0.80 and recall at least 0.70 on adjudicated seeded factual issues |
| Test findings | Target precision at least 0.80 on actionable weakness findings; no unsupported deletion recommendation on F11 |
| Evidence integrity | Zero fabricated execution results; clearly report checks not run |
| Maintenance burden | Report instruction size, changed files, correction rounds, and interventions; investigate regressions rather than hide them |

Precision is correct actionable findings divided by all actionable findings; recall is detected seeded issues divided by all seeded issues. Report numerators and denominators, not percentages alone. A zero denominator is not a perfect score.

The numerical targets are initial design thresholds, not measured performance claims or industry benchmarks. Freeze them before a release evaluation. If changed, record the reason and rerun; do not lower them silently after seeing results. Report results per environment and failure category rather than hiding a weak host behind a pooled average.

Do not invent token or cost measurements when the host does not expose them. Record unavailable values as unavailable. Report wall time and human review effort separately when collected.

### 16.6 Interpreting results

Negative results are valid findings. Document unnecessary instructions, missed issues, false positives, activation failures, and cases where the baseline is better. Improvement in a small synthetic benchmark supports only a narrow claim.

Changes prompted by evaluation fixtures make those fixtures development evidence. Reserve fresh examples for later validation when making stronger claims. Do not describe a previously inspected and tuned-on set as an untouched holdout.

## 17. Release acceptance criteria

A release must satisfy the relevant behavioral contract, not simply contain files with the expected names.

| ID | Acceptance criterion | Verification | Requirements |
| --- | --- | --- | --- |
| A01 | Initialize an empty repository without a stack decision, code generation, or invented tooling | F01 in target environments | R1 |
| A02 | Initialize from a specification while preserving proposal/intention/implementation distinctions | F02 and source-to-instruction review | R1, R2 |
| A03 | Adopt existing Python and TypeScript projects without replacing their actual conventions | F03-F05 and reviewed adoption diffs | R1, R2, R9 |
| A04 | Switch coding environments on the same installed project without regenerating skills or guidance | Native integration record for all three hosts | R3 |
| A05 | Complete a scoped plan, implementation or repair, and review using relevant repository evidence | Representative end-to-end fixture | R4 |
| A06 | Find seeded current documentation drift, preserve accurate history, and perform a coherent authorized correction | F07-F09 and post-edit review | R5 |
| A07 | Explain missing test protection and retain justified cross-layer tests | F10-F11 with recorded assertions or fault evidence | R6 |
| A08 | Detect missing shared resources, installation drift, and conflicting guidance without claiming a full semantic proof | Helper tests and harness audit fixture | R7, R8 |
| A09 | Reinstall idempotently and refuse silent overwrite of modified or unmanaged files | F12 and deterministic regression tests | R8, R9 |
| A10 | Keep source edits, dependency installs, external changes, and test faults within authorization | Safety checks across fixtures | R1-R9 |
| A11 | Run without a Remora API key, hosted service, or separate inference runtime | Dependency and execution-path inspection | R1-R10 |
| A12 | Publish compatibility status, pilot results, counterexamples, and limitations without unsupported success claims | Review of release evidence | R3, R10 |

Zero unauthorized writes and zero fabricated execution claims are mandatory release gates on the evaluated fixtures. An untested host is labeled unverified rather than marked supported by assumption. Missing advanced mutation tooling, a dashboard, or a CLI product is not a v0.1 failure.

## 18. Implementation sequence

### Milestone 1: Establish the content and evidence baseline

Create the repository's own concise instructions and development checks. Finalize skill contracts, ownership rules, and fixture rubrics. Inspect APEX and mimus as design inputs without copying their project-specific assumptions. Record exact host surfaces available for compatibility testing.

### Milestone 2: Bootstrap one coherent installation

Implement the bootstrap procedure, minimal shared standards, project-owned instruction template, safe installation helper, and manifest validation. Exercise empty, specification-only, and existing-project fixtures before adding more profiles.

### Milestone 3: Deliver the documentation maintenance workflow

Implement purpose-aware audit and authorized reconciliation. Evaluate stale claims, historical records, duplication, structural corrections, and false positives. Feed results into the workflow without inflating the always-loaded rules.

### Milestone 4: Complete the development loop and basic test assurance

Add or refine planning, implementation, regression, review, test audit, and harness audit entrypoints around shared procedures. Demonstrate meaningful failure signals and preserve justified coverage. Avoid creating independent engines behind each skill.

### Milestone 5: Operational readiness and validation

1. Complete technical prerequisites: pinned personal bootstrap packaging, selected profiles, installed integrity checks, and explicit update/removal with inspected recovery procedures.
2. Complete automated checks, available native Codex trials, and controlled comparisons. Retain the full Section 16 matrix: F02/F05/F07/F10 twice per condition per environment (48 runs total), plus every applicable functional fixture once per target environment.
3. Dogfood existing skills in a disposable Remora checkout through adoption, audits, planning, implementation, review, and historical regression repair.
4. Conduct remaining real-environment trials and private Vulpes Health adoption using an approved disposable snapshot. Involve the owner only for necessary local access/interaction or material unresolved adjudication.

Finish independently verifiable implementation and trials before requesting manual testing. Record implementation/independent-verification completion separately from milestone completion: pending required host or repository trials remain outstanding, never passing by assumption. Preserve all safety gates and evaluation thresholds.

### Subsequent phase: Public v0.1 release preparation

Review license and attribution, public artifact names, release notes, publication-safe evidence, and all Section 17 acceptance criteria. Resolve release blockers and review the exact target before any separately authorized publication. Operational validation does not itself authorize a release or waive a release requirement.

These are dependency-ordered deliverables, not time estimates. Evaluation starts with the first fixture and continues through every milestone.

## 19. Tradeoffs and known limitations

| Choice | Benefit | Cost or limitation |
| --- | --- | --- |
| Agent-native reasoning | Uses the coding environment already in the user's workflow | Outcomes vary with model, host, context, and permissions |
| Vendored project files | Versioned, inspectable, usable across environments | Explicit updates and some repository footprint |
| Project-owned `AGENTS.md` | Preserves local knowledge and avoids a universal template | Adaptation remains a reasoning task that needs evaluation |
| Shared references outside individual skills | Avoids repeated standards in every skill | Installation is a bundle; partial copying can break references |
| Read-only audits by default | Limits accidental churn | Findings still need an authorized correction step |
| Small helpers | Reliable objective checks without a competing application | Cannot settle semantic documentation or test-quality questions |
| Basic test assurance first | Useful behavior-level explanations with manageable scope | No broad proof of suite effectiveness or equivalence |
| No autonomous upgrade service | Predictable behavior and reviewable changes | Owner must initiate and inspect updates |

Portability means the same procedures and evidence expectations can be used across hosts. It does not mean identical responses, identical instruction-loading semantics, or identical native features.

Remora must itself be maintainable. Every new rule, profile, file, or helper should address a recurring problem or a demonstrated failure. Prefer simplifying an existing workflow over adding another layer.

## 20. Deferred capabilities and remaining decisions

### 20.1 Deferred, not implied commitments

Future work may include targeted mutation-tool integration, richer coverage import, additional host adapters, specialized architecture references, optional MCP exposure of deterministic helpers, and more automated evaluation runs. Each requires evidence of user value and must preserve the skill-first model.

Automatic semantic upgrades, a universal policy language, mandatory multi-agent roles, always-on background auditing, a dashboard, and direct LLM API orchestration are not part of the planned initial architecture.

### 20.2 Decisions required before publication

Select the repository license and review attribution for any reused material. Record tested host versions and surfaces, finalize release artifact names, and decide which real-project evidence is safe to publish.

The owner's actual working machines and host versions determine the release compatibility matrix. This specification does not claim those environments were exercised while the document was written.

These publication details do not block implementing the core workflows. A change to agent-native execution, project ownership, or the no-independent-API requirement would be a product-direction change and must be reviewed explicitly.

## 21. Specification maintenance

This document owns intended product behavior and v0.1 boundaries. Source files and tests establish implementation; compatibility records and evaluation reports establish observations. Keep those roles separate.

When an architectural decision changes, rewrite the affected explanation coherently and record material rationale in the decision log. Do not append contradictory exceptions or move transient progress updates into this specification. Release history belongs in release notes or a changelog.

The central constraint remains:

> Remora should reduce the effort needed to establish and maintain an AI-assisted development workflow without becoming another complicated system the user must maintain.

## Sources

External integration facts were checked on October 15, 2026. These references support the compatibility and skill-format discussion; they do not establish that Remora is implemented or effective. Product requirements and proposed architecture are design decisions in this document.

[^s1]: Agent Skills, *Specification*. `https://agentskills.io/specification`. Required metadata, supporting resources, and progressive disclosure.

[^s2]: OpenAI, *Build skills*. `https://learn.chatgpt.com/docs/build-skills` (reached from `https://developers.openai.com/codex/skills`). Codex local skill discovery and locations.

[^s3]: OpenAI, *Custom instructions with AGENTS.md*. `https://learn.chatgpt.com/docs/agent-configuration/agents-md` (reached from `https://developers.openai.com/codex/guides/agents-md`). Instruction discovery, scope, and overrides.

[^s4]: Cursor, *Agent Skills*. `https://cursor.com/docs/skills`. Shared and personal skill directories, discovery, and remote-surface distinctions.

[^s5]: Cursor, *Rules*. `https://cursor.com/docs/rules`. Root/nested instructions and file-reference behavior.

[^s6]: Google Antigravity, *Agent skills*. `https://antigravity.google/docs/skills/`. Shared project skills, personal locations by surface, and invocation.

[^s7]: Google Antigravity, *Rules*. `https://antigravity.google/docs/rules/`. Directory scope, rule formats, and reference behavior.

[^s8]: Google Antigravity, *Migrate from workflows to skills*. `https://antigravity.google/docs/migration/workflows-to-skills`. Dated legacy-workflow transition notice; recheck before implementing compatibility work.
