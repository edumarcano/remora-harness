# Ledger project instructions

Ledger is a local Python label utility. Preserve label order and duplicates;
deduplication is not a product requirement.

Read `docs/development.md` for verification and environment setup. Keep that file
authoritative for commands rather than maintaining another command list here.
Verification runs only the unit suite; no separate syntax check is configured.

Do not replace the custom verification entrypoint with pytest or introduce a
package manager as part of harness adoption.
