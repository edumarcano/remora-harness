# Ledger development

Ledger currently normalizes whitespace in labels without changing their order
or removing duplicates. It has no database, network integration, or release
packaging. Python 3.11+ and its standard library are sufficient.

An optional local environment can be created with `python -m venv .venv` from
the Ledger component root (`components/ledger/` within this fixture). There are
no third-party dependencies to install.

From the Ledger component root (`components/ledger/` within this fixture), run
`python tools/verify.py`. This custom entrypoint runs the standard-library unit
suite under `tests/` and exits unsuccessfully if a test fails. Do not substitute
pytest. This document describes configured tooling; it does not record whether
checks passed in a particular environment.
