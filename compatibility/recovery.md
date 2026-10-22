# Inspect an interrupted lifecycle operation

Recovery is an explicitly authorized, narrow repair, not automatic rollback.
Before-images and operation.json reside in the new private --backup directory
printed by apply. Keep them outside the target and public evaluation records.
The installation manifest is deliberately removed before managed mutation; its
absence means incomplete work, not permission to adopt surviving files.

1. Verify the exact target/backup roots and their ordinary paths, including all
   ancestors; reject links/reparse points. Read operation.json as untrusted data.
   Match its target identity and supported relative managed paths to the reviewed
   operation. Do not follow arbitrary paths or execute backup content.
2. Inspect Git state and current affected bytes. For each operation path compare
   SHA-256 with its recorded before and after values. A null value means absence.
   Verify each backup before-image against its before hash. A file matching neither
   value contains newer/unknown work: preserve it and stop that affected restore.
3. Already-before files need no write. Restore a before-image only where current
   state matches the operation's after state. A failed write may leave missing or
   partial bytes; do not overwrite those automatically. Inspect their exact origin
   and obtain a scoped recovery decision before changing them.
4. Remove an operation-created file only when its current hash matches the recorded
   after hash and its before value was null. Never delete an unrelated file or
   directory, use a blanket reset/clean, or overwrite newer edits.
5. Restore the old installation manifest last, only after every old managed asset
   matches the trusted old distribution and operation-created files have been
   handled. Use exclusive creation if absent. Check the recovered installation
   against that separately trusted old source and review the actual diff.

Initial installation also preserves partial writes but has no automatic rollback.
Inspect its reported created paths and source bytes with the same ownership/newer
edit discipline. Root guidance is project-owned; an incomplete managed operation
does not authorize restoring or deleting it.

Keep failed attempts and unresolved paths in the private record. If the operation
completed and the user wants a reversal, treat that as a new reviewed lifecycle
operation rather than replaying a stale backup.
