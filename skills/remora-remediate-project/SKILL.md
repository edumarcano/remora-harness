---
name: remora-remediate-project
description: Orchestrate repository onboarding and cleanup across grounding, documentation sanitization, test protection, and scoped debt remediation through checkpointed review gates.
---

# Remediate a repository

Establish the target root and explicitly read `.remora/standards/engineering.md`,
`.remora/standards/documentation.md`, and `.remora/standards/testing.md` from that root,
plus applicable root and scoped project instructions. Paths are target-root relative.
Missing resources mean an incomplete installation; report the gap without inventing
replacements. Use native host tools without a separate service, daemon, or runtime.

Remediation brings an existing codebase up to Remora's engineering standards as if it had
used the harness from Day 1. It is an **order-of-operations sequence** divided into four
distinct phases. **Never execute these phases as an unmonitored batch mutation.** Pause at
each designated Review Gate for explicit user review before advancing to the next phase.

## Initial assessment and remediation plan

Before making any modifications, conduct a read-only assessment across four axes:

| Axis | Focus | Target Evidence |
| :--- | :--- | :--- |
| **1. Grounding** | Instructions and orientation | Root `AGENTS.md`, scoped guidance, verified build/test commands vs unverified trivia. |
| **2. Documentation** | Clarity and authority | Project docs, specifications, guides, AI slop markers, patch accumulation, missing decision records. |
| **3. Test Protection** | Verification confidence | Existing test suite, empirical artifact proof, brittle proxies, tautologies, external API isolation. |
| **4. Technical Debt** | Architectural health | Known hotspots, deprecated interfaces, and missing regression defense. |

Output the assessment as a prioritized Remediation Punch List directly in chat, detailing
the planned scope for each phase. Request authorization to proceed with Phase 1.

## Phase 1: Grounding and orientation

Align root project guidance with reality:

1. **Purge discoverable trivia:** Remove descriptions of directory trees, tool tutorials,
   and obvious language syntax that the agent discovers directly.
2. **Verify commands:** Test candidate build, test, and lint commands locally. Distinguish
   commands verified in this environment from merely configured manifest entries.
3. **Establish boundaries:** Formulate concise non-goals, reproduction rules, and safety
   constraints.
4. **Link shared standards:** Ensure `AGENTS.md` points to `.remora/standards/engineering.md`
   and lists available installed skills.

> **Review Gate 1:** Present the proposed `AGENTS.md` diff. Do not proceed to documentation
> or test audits until the user approves the grounded project instructions.

## Phase 2: Documentation sanitization

Apply the documentation standard across all project documentation:

1. **Audit document roles:** Identify the canonical owner of each subject (specifications,
   architecture guides, operational manuals, decision records).
2. **Apply the refactoring threshold:**
   - Use surgical patches for single factual updates (paths, flags).
   - If a section has accumulated multiple caveats ("previously X, now Y unless Z") or
     architecture has drifted, perform a **clean-room rewrite of that section in the
     present tense**, explaining current behavior as if designed that way from the start.
   - Relocate historical transitions and rejected alternatives to `docs/decisions.md`.
3. **Enforce anti-slop editorial standard:**
   - Remove throat-clearing preambles and meta-announcements.
   - Eliminate decorative em-dashes (`—`) used as conversational crutches.
   - Purge AI marketing buzzwords ("seamless", "delve", "tapestry", "rich ecosystem").
   - Format 3 or more structured items (parameters, states, options) into Markdown tables.
   - Keep paragraphs under 4 sentences in active voice.

> **Review Gate 2:** Present the documentation diffs or a scoped PR for review. Verify that
> local Markdown links pass before requesting approval to proceed to Phase 3.

## Phase 3: Test protection audit

Audit test usefulness following `.remora/standards/testing.md`:

1. **Distinguish empirical proof from proxies:** Flag tests that only verify mock calls or
   reproduce implementation details rather than production behavior.
2. **Detect tautological assertions:** Identify tests that pass vacuously or assert conditions
   that cannot fail.
3. **Check external API boundaries:** Ensure external or paid LLM/cloud APIs are explicitly
   isolated, with automated tests covering deterministic behavior and manual reproduction
   steps documented for paid boundaries.
4. **Identify failure signals:** Confirm that key regression tests actually fail when their
   underlying behavior is removed or altered.

> **Review Gate 3:** Present a prioritized Test Protection Gap Report. Do not modify test
> assertions or production code in this phase.

## Phase 4: Scoped technical debt remediation

For identified architectural defects or critical test gaps:

1. **Deconstruct into work packets:** Formulate bite-sized, independent implementation
   packets with clear acceptance criteria.
2. **Execute via standard skills:** Hand off individual packets to `remora-plan-change` and
   `remora-implement-plan`.
3. **Apply Split-Axis review:** Evaluate each packet independently against Axis 1
   (Specification Fulfillment) and Axis 2 (Standards & Anti-Slop).

## Operational boundaries

- **Never edit production code and test assertions simultaneously** during remediation.
- **Never delete existing project skills** simply because Remora provides generic equivalents.
- **Stop on material contradictions:** If code contradicts an approved specification, surface
  the discrepancy to the user rather than altering either to match the other.
- **Handoff:** Conclude with a clean audit report and recommendations for ongoing maintenance.
