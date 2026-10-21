# Component map

- Ledger: [instructions](../components/ledger/AGENTS.md) and
  [development](../components/ledger/docs/development.md). A local Python label
  utility with a standard-library unit runner.
- Beacon: [instructions](../components/beacon/AGENTS.md) and
  [development](../components/beacon/docs/development.md). A browser TypeScript
  page with its own npm scripts and deployment configuration.

These components have separate execution contexts; their co-location does not
create a shared workspace toolchain.
