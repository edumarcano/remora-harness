# Host compatibility

This file owns setup and evidence distinctions. The specification owns required
behavior; dated evaluation records own actual outcomes. No generic host-family
checkmark substitutes for a tested surface/build.

| Host target | Project skills | Personal bootstrap directory | Native action |
| --- | --- | --- | --- |
| Codex CLI | .agents/skills/ | ~/.agents/skills/remora-bootstrap/ | Select/mention the skill through the current host; restart if absent |
| Cursor Agents Window | .agents/skills/ | ~/.agents/skills/remora-bootstrap/ or ~/.cursor/skills/remora-bootstrap/ | Inspect native discovery in this surface; start a fresh session after installation |
| Antigravity 2.0 standalone app | .agents/skills/ | ~/.gemini/config/skills/remora-bootstrap/ | Inspect Customizations and select the discovered skill through the slash selector |

Codex and Cursor can share one personal bootstrap copy. Inspect all discovered
personal/project locations for duplicates; never install the same identity twice
merely to make it appear. Do not put the ten project skills under a personal
directory. The builder carries them as inert archive entries.

Official documentation checked October 21, 2026:
[Codex skills](https://learn.chatgpt.com/docs/build-skills),
[Cursor skills](https://cursor.com/docs/skills),
[Cursor rules](https://cursor.com/docs/rules),
[Antigravity skills](https://antigravity.google/docs/skills/), and
[Antigravity rules](https://antigravity.google/docs/rules/).
These document the shared project location; they do not establish a Remora pass.
Recorded Milestone 5 coverage:

| Surface | Evidence |
| --- | --- |
| Codex CLI | Native discovery, functional trials and 16 comparisons: [operational record](../evals/records/2026-10-21-operational.md) |
| Antigravity standalone | Native selection, functional trials, 16 completed comparisons and switching from Codex: [Antigravity record](../evals/records/2026-10-22-antigravity.md) |
| Cursor Agents Window | Composer 2.5 discovery and read-only audit smoke test: [Cursor record](../evals/records/2026-10-23-cursor.md) |

Results apply to the recorded builds and runtime pins. Other surfaces, remote use
and implicit triggering are outside this coverage. Cursor's remaining trials were
waived for Milestone 5; broader workflow behavior was not measured.

Use one project installation recording all three requested families before the
host-switch trial. Snapshot managed bytes and project guidance, then use fresh
sessions in each host without regenerating content. Check selector identities,
activation, explicit shared-resource reads, scoped instructions, and actual task
outcomes. Implicit triggering is a separate usability observation. Report failed
native discovery even if explicit-file fallback succeeds.

Root-to-working-directory discovery differs from file-based nested instruction
loading across hosts. Skills explicitly inspect applicable scoped guidance before
working in an area. Exercise root and nested work separately; do not infer behavior
from file presence. Inspect visible global/team/override guidance and disclose
unknown context. No host adapter is currently justified by a reproduced gap.

Installing into real personal directories and accessing other projects must use
normal host permissions. Finish isolated technical verification first. Do not
change global settings, copy credentials, or bypass controls to make a trial pass.
If sandbox permissions prevent installation, use a narrowly scoped installer
approval through normal host controls. Record prepared adoption separately from
unassisted installation. The operational record retains the Windows alpha-build
failure and attempted workaround; do not assume they apply to other builds.
Keep permission profiles identical within comparison pairs and exclude personal
Remora skills from baseline sessions using supported session controls.
Record host, surface/build, model/effort where exposed, OS, date, source pin,
installation location privately, scenario outcomes, and retained failures.

Use documented, tested, and unsupported/unverified as separate statuses. See the
[Milestone 5 packet](../evals/milestone-5.md) for the execution matrix and evidence.
