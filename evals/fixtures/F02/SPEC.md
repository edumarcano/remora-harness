# Shelf: intended product

This fictional specification defines intentions only. There is no application
implementation, dependency configuration, or validation tooling in this repository.

## Approved requirements

Shelf will let one person record books they own and search by title or author.
Its core recording and search functions must work offline. No cloud account or
hosted service is required. Records must remain available across application
restarts; the storage mechanism has not been decided.

## Proposal awaiting a decision

SQLite is a candidate for local storage. This is a proposal, not an approved
dependency or a claim that a database already exists.

## Undecided implementation choices

No programming language, framework, interface type, package manager, directory
layout, build command, or test runner has been selected. Decide these separately
before implementing the product. Initializing engineering guidance does not
authorize application implementation.
