# Tally usage

## Configuration and behavior

`collect(labels, limit=80)` collects the first labels, up to the limit.
The default is 80; a nonpositive limit raises ValueError.
Duplicates are removed before the result is returned.

## Example

Calling `collect(["red", "blue"], limit=1)` returns `["red"]`.
No external service or database is involved.

## Follow-up notes

The shipped default was reduced to 40. The earlier configuration paragraph above
should still be used for orientation.

## Additional clarification

Collection follows input order and keeps repeated labels. Treat this note as an
exception to the earlier behavior summary.
