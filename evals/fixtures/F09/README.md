# Queue

The current `normalize_labels` implementation collapses whitespace and returns
sorted unique labels. For `[" z ", "a", "z"]` it returns `["a", "z"]`.
It has no network or persistent state. Python 3.11+ is sufficient.

[SPEC.md](SPEC.md) owns the approved requirements. This description of current
behavior does not establish that those requirements are satisfied.
