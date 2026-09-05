# Proposed record changes

These are proposals against the exercise facts, dated 2026-09-05 in the project timezone. Existing paths and canonical record owners should be preserved. Only the successor path and upload-format note filename were supplied; other link destinations must be resolved from the actual repository rather than invented.

## 1. Media library area

Set or retain the overview metadata:

```text
Kind: area
Status: active
Created: 2026-09-01
Updated: 2026-09-05
```

Record all three listed milestones as complete, linking their existing acceptance evidence and dating those results 2026-09-04. This substantive summary update is dated today; the test results retain yesterday's date. The ongoing browsing/import remit still has an owner and no agreed end, so the area remains active even with no unfinished listed milestones. Do not add an archive date or invent new milestones. If the overview already contains this exact milestone update and no substantive edit is needed, preserve its existing Updated date instead.

Keep the media entry in the active index with a concise summary that listed milestones are complete and the ongoing remit continues. Linked Agent Notes retain their independent lifecycle and canonical locations; milestone completion alone does not archive or implement a note.

## 2. Legacy upload initiative

```text
Kind: initiative
Status: retired
Created: 2026-09-01
Updated: 2026-09-05
Retirement reason: Product owner cancelled the remaining legacy upload scope and selected the new-upload roadmap as successor.
Successor: docs/roadmaps/new-upload/README.md
```

The two required interruption tests remain unimplemented. Explicitly preserve that gap and distinguish cancellation from delivery completion in the owning plan/phase and related issue records. Use their established cancelled/no-longer-needed disposition if applicable, including the cancellation reason and successor link; do not fabricate test passes, mark the phase complete, or silently transfer the tests into the successor's committed scope. The successor must explicitly own any retained work before it is represented as transferred. Its selection alone does not establish its complete scope, priority, or acceptance criteria.

Update the index entry to retired and link the successor. Preserve the legacy roadmap's historical verification and decision links, and add a predecessor link from the successor where appropriate. Do not archive yet: the exercise does not establish that maintained owners cover all useful dependencies, decisions, and successor links or that the old overview no longer guides compatibility work.

Keep `2026-08-28-upload-format.md` implemented, at its canonical current location, with its filename date unchanged. An existing client still consumes the format, so the decision remains relevant; retiring its roadmap is not full supersession. Link it from the successor and the current compatibility owner where relevant, retain the old roadmap link for context, and document surviving obligations. Do not reject, rename to today's date, or automatically archive this note. If cancellation changes consequential decision rationale, search for its existing owner and update that owner or create a separate cross-linked cancellation decision; do not rewrite the format decision into its opposite. Any new replacement decision must preserve and link the still-live format rationale.

## 3. Accessibility initiative

```text
Kind: initiative
Status: active
Created: 2026-09-02
Updated: 2026-09-05
```

Remove the pause reason and resume condition from current blocker fields, preserving them in transition history: paused for unavailable required device; resumed 2026-09-05 after device availability and explicit product-owner authorization. Both the stated condition and authorization are satisfied. Keep the agreed scope and required journey verification open; device access is readiness evidence, not acceptance evidence.

Update the index to active and affected dependency/blocker summaries to show device access restored. Link the current plan/phase and the remaining journey verification as the next work. Retain actual plan/phase states based on their own evidence rather than marking them complete. No linked Agent Note changes lifecycle merely because the roadmap resumed. An implemented note may retain a named journey verification gap until the actual check passes; a proposed note stays proposed unless its decision is independently implemented. Routine resumption belongs in delivery records; update decision rationale only if it actually changed.

## 4. Archived migration roadmap

Leave the sealed overview unchanged: retain `Status: completed`, `Archived: 2026-09-04`, its existing Created/Updated dates, archive reason, and verification/decision links. Do not refresh its dates, reopen it, or edit frozen history to describe a different migration.

Create a linked follow-on candidate at an appropriate existing-convention path, for example `docs/roadmaps/new-format-migration/README.md` (proposed path, not an observed record):

```text
Kind: initiative
Status: draft
Created: 2026-09-05
Updated: 2026-09-05
```

Describe the stakeholder's new-data-format migration request and explicitly list scope and acceptance criteria as unresolved. Link the sealed migration as predecessor/evidence from this new overview. No implementation is authorized by creating this candidate; agree scope, acceptance, and priority through planning before activating it. Keep the old entry discoverable under archived/completed roadmaps and add the follow-on draft to the index, with the relationship expressed there so the sealed overview need not change.

Linked Agent Notes retain their own states. Leave frozen notes frozen; reference them from a new active note if new rationale is needed. Search existing decision owners before creating a proposed note for consequential new migration choices, and assess partial/full supersession only with actual contract evidence. The new request alone proves neither.

## 5. Imported search roadmap

```text
Status: draft
Created: unknown
Updated: 2026-09-05
Date provenance: Original creation cannot be established: the export has no Git history, original creation timestamp, or dated proposal. Updated records the substantive scope clarification on 2026-09-05.
```

Retain draft status because scope clarification does not establish agreement for active pursuit. Preserve an existing valid Kind if present. Otherwise resolve whether this owns a standing search remit (`area`) or a bounded search outcome (`initiative`) from its scope before supplying Kind; the exercise does not establish that distinction. Do not infer original creation from the filesystem modification time of 2026-09-04, or substitute today's date. Keep unknown until trustworthy evidence is recovered, then document any correction's basis.

Reflect the clarified scope and draft status in the existing index entry and link the requirement/plan owner if present. Preserve note filenames and note states. If the clarification changes consequential direction, update the existing rationale owner or propose a new note using today's date only as the actual first-proposed date of that new note. It is not the imported roadmap's creation date.

## Shared navigation and checkpoint maintenance

For each index, plan, phase, or issue substantively changed today, preserve known Created metadata and set Updated to 2026-09-05; backfill unknown creation only with evidence and otherwise use unknown with provenance. The roadmap index itself has dates but no delivery lifecycle. Keep acceptance details in their canonical plan/phase owners and decision rationale in shared Agent Notes, linking summaries rather than duplicating them. Preserve current paths by default; any necessary moves require repaired active incoming links.

Update the current checkpoint with the changed roadmap owners, relevant existing plan/phase/issue and decision links, cancellation and resumption rationale, remaining interruption/journey evidence gaps, and the new migration's planning next step. Verification timestamps stay tied to actual checks. This exercise supplies no real record inventory or test logs, so record targets and acceptance evidence links require repository inspection before applying these proposals.
