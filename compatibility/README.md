# Host compatibility

This file owns setup and evidence distinctions. The specification owns required
behavior; dated evaluation records own actual outcomes. No generic host-family
checkmark substitutes for a tested surface/build.

| Host target | Project skills | Personal bootstrap directory | Native action |
| --- | --- | --- | --- |
| Codex CLI | .agents/skills/ | ~/.agents/skills/remora-bootstrap/ | Select/mention the skill through the current host; restart if absent |
| Cursor editor Agent | .agents/skills/ | ~/.agents/skills/remora-bootstrap/ or ~/.cursor/skills/remora-bootstrap/ | Use the skill selector in Agent chat; start a fresh session after installation |
| Antigravity IDE | .agents/skills/ | ~/.gemini/config/skills/remora-bootstrap/ | Inspect Customizations and explicitly invoke the discovered skill |

Codex and Cursor can share one personal bootstrap copy. Inspect all discovered
personal/project locations for duplicates; never install the same identity twice
merely to make it appear. Do not put the seven project skills under a personal
directory. The builder carries them as inert archive entries.

Official documentation checked October 21, 2026:
[Codex skills](https://learn.chatgpt.com/docs/build-skills),
[Cursor skills](https://cursor.com/docs/skills),
[Cursor rules](https://cursor.com/docs/rules),
[Antigravity skills](https://antigravity.google/docs/skills/), and
[Antigravity rules](https://antigravity.google/docs/rules/).
These document the shared project location; they do not establish a Remora pass.
The [operational record](../evals/records/2026-10-21-operational.md) contains bounded
Codex CLI Windows observations. Cursor editor and Antigravity IDE are documented
targets with pending native execution, not tested support claims.
Antigravity CLI uses a different personal location and is not certified by IDE tests.
Local skills do not imply remote/cloud availability.

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
Codex CLI workspace-write may protect an existing .agents/skills directory. On the
tested Windows alpha build, --add-dir for its writable descendant prevented shell
startup with a read-only-carveout error; do not prescribe that workaround as tested.
Use a narrowly reviewed installer command through normal host permissions, then
test native adoption/idempotence separately. Prepared F05 adoption is not evidence
of unassisted installation under this sandbox. Do not enable broad automatic
approval or disable sandbox controls to force a pass. Apply the same native session
permission profile to both comparison conditions. For baseline sessions after
personal bootstrap installation, disable that skill through session-local
skills.config; do not rewrite the user's global configuration.
Record host, surface/build, model/effort where exposed, OS, date, source pin,
installation location privately, scenario outcomes, and retained failures.

Use documented, tested, and unsupported/unverified as separate statuses. See the
[Milestone 5 packet](../evals/milestone-5.md) for the execution matrix and evidence.
