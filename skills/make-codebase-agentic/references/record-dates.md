# Dates in repository records

Use ISO calendar dates (`YYYY-MM-DD`) in the project's agreed timezone. Dates identify recorded events; they are not delivery estimates or proof of correctness. Preserve established equivalent metadata when adopting an existing repository.

## Roadmaps and delivery records

Roadmap overviews and indexes, feature plans, separate phase files, and Markdown issues carry `Created` and `Updated` fields near their title. `Created` is the original recorded creation date and remains stable when a record moves or changes status. `Updated` is the date of the latest substantive content or lifecycle change, not the date someone merely read it. Several updates on the same day share that date; Git retains detailed history.

```text
Kind: initiative
Status: active
Created: 2026-09-01
Updated: 2026-09-05
```

Kind and roadmap status follow the [roadmap lifecycle](../../make-codebase-agentic-roadmap/references/lifecycle.md). Plans, phases, and issues retain their own states. A phase kept inside a plan shares that file's date metadata; it does not require a duplicate header. A tracker-owned issue uses the tracker's dates rather than a competing local mirror.

For existing files, use trustworthy evidence such as recorded creation metadata, a dated proposal, or Git history that establishes first appearance. Document the basis when backfilling a group of records. Do not use filesystem modification time or today's date as a guessed creation date. If history is unavailable, write `Created: unknown` and `Date provenance: <why creation cannot be established>`; `Updated` still records the real adoption/edit date. Do not silently convert an unknown creation date into a known one later without evidence.

## Agent Notes

Use `YYYY-MM-DD-topic.md`; the date is when the topic was first proposed or first recorded if it began as an implemented decision. Keep the filename date unchanged through implementation, rejection, factual maintenance, and archival. The [note lifecycle](../../make-codebase-agentic-agent-notes/references/lifecycle.md) owns those transitions. Notes do not need duplicate Created/Updated headers by default; Git records subsequent edits.

Keep existing legitimate dates when adopting a repository. If a legacy note has no recoverable original date, retain its established identifier and document the gap under that repository's conventions rather than inventing a dated filename. The bundle's own new notes require valid dated filenames; its checker is not an automatic migration tool for arbitrary repositories.

## Checkpoints and archives

Checkpoints carry `Updated` and date their verification evidence. Refresh that field when the checkpoint's work state changes. A recent update does not make older test results current; retain each result's actual date and environment.

Archiving a roadmap or Agent Note adds `Archived` with the actual sealing date and a reason. A roadmap retains its terminal delivery status. An Agent Note retains the framework's existing archive lifecycle metadata. Preserve the filename/creation date and existing substantive update date; `Archived` is at or after the last known update or original note date. Do not refresh dates inside frozen history during routine maintenance.

Validation checks calendar validity and chronological ordering where dates are known. It cannot establish whether a supplied date is truthful, reconstruct unknown history, detect every later edit to an archive, or prove that completed work met acceptance criteria. Existing retained evaluation artifacts are historical inputs and outputs, not records to retrofit to a new schema.
