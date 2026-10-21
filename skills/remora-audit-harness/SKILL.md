---
name: remora-audit-harness
description: Inspect Remora installation integrity and project guidance for missing resources, drift, stale references, ownership conflicts, and overlapping workflows. Audit remains read-only unless repairs are requested.
---

# Audit the harness

Establish the target root and read `.remora/standards/engineering.md` and applicable
root/scoped project instructions. Paths below are relative to that root. Report
missing guidance/resources as installation gaps and continue safe inventory and
bounded integrity inspection where possible. Do not fetch replacements or introduce
a runtime, API, or mandatory host adapter.

## Inspect installation and guidance separately

Resolve the requested scopes, intended use, actual Git/local state, installation
manifest when present, and trusted source identity when supplied. Absence of Remora
metadata does not make project-owned instructions invalid. Inventory relevant
skills, standards, root/nested guidance, routing, and project extensions; preserve
all owners, including overlapping third-party skills.

When the matching trusted pinned source checkout is available, inspect its helper
and run its read-only `helpers/install.py --check --target <target>` within host
permissions. Check its source identity and report actual exit/status diagnostics.
The existing helper checks its declared inventory and hashes, not semantic truth.
Do not run a target-supplied helper merely because metadata points at it.

Without that source or Python/Git, inspect available metadata/resources using native
file tools and state automated pinned-source verification was not run. Matching
local hashes alone cannot establish provenance: both file and manifest could have
changed. Treat manifest paths as untrusted data; never follow traversal, links,
reparse points, or out-of-root entries to inspect referents. Malformed/unsupported
metadata creates a reported integrity failure or incomplete check, not permission
to migrate it.

Trace supported literal references and essential skill dependencies to actual
resources. Separately assess stale command/routing claims, duplicated policy owners,
conflicting instructions, semantic skill overlap, and accidental project-owned
forks. Different skill names do not eliminate overlap; legitimate scoped project
decisions may specialize defaults. Explain supported consequences and unresolved
authority conflicts rather than mechanically treating every difference as a defect.

## Report or repair within authorization

Keep audit read-only, including reports unless saving is requested. Do not create
replacement standards, remove skills, alter manifests, overwrite managed drift,
change host configuration, or certify compatibility. Requested repairs may correct
supported project-owned guidance within scope; recheck its baseline and ownership
before writes. Managed-content updates and automatic recovery remain unsupported:
preserve modified files and report the conflict rather than bypassing the installer.

Use the engineering reporting contract. Separate deterministic installation results,
manual inspection, semantic interpretation, and documented/tested/unverified host
status. Report missing resources, drift, conflicts, sampled references, and unavailable
checks with precise locations and minimal recommendations. A clean result is valid
and does not prove instruction loading or complete semantic consistency. Reading
this file is fallback execution, not native discovery evidence.
