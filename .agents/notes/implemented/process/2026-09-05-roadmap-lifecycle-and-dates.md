# Roadmap lifecycle and record dates

Status: implemented

## Problem

Roadmaps connected delivery records but had no explicit lifecycle or consistent date metadata. An implemented Agent Note could be mistaken for completed delivery, and dates in note filenames lacked an explicit first-proposal meaning.

## Decision

Roadmaps keep independent status: draft, active, paused, completed, or retired. Their kind identifies an ongoing area or bounded initiative. Archiving preserves a completed or retired overview with its terminal status, sealing date, reason, and discoverable links. Linked Agent Notes retain their independent lifecycle and current owners.

The [roadmap lifecycle](../../../../skills/make-codebase-agentic-roadmap/references/lifecycle.md) owns state meanings and transition evidence. [Record dates](../../../../skills/make-codebase-agentic/references/record-dates.md) owns Created/Updated metadata, stable note filename dates, archive dates, and unknown legacy creation dates. The bundle checker enforces the local record paths and simple header fields, calendar validity, known chronology, and required transition metadata. It does not prove semantic completion, historical truth, authorization, or archive immutability.

## Alternatives considered

Combining roadmaps and notes would conflate ongoing delivery with decisions already adopted. Marking an area complete whenever its listed milestones finish would lose its continuing remit. Using archived as a delivery status would hide whether scope was completed or abandoned. Updating note filenames on every edit would break stable links and erase their original date meaning. Backfilling dates from filesystem timestamps or the current day would invent history.

## Consequences and provenance

The skill-suite area remains active; the unselected iOS-adoption initiative is draft. Existing roadmap/index/plan/phase/issue Created dates come from their first Git appearance, including followed renames; each is 2026-09-05. Updated records use the actual edit date, 2026-09-05. Existing note dates and retained evaluation artifacts are unchanged.

The [area-roadmap decision](2026-09-05-area-roadmaps.md) remains active and is refined by this metadata/lifecycle contract. The checker recognizes this bundle's paths; adopting projects map their equivalents rather than applying the checker as a generic migration tool. Frozen record bodies are excluded from ordinary link/prose checks, while their local archive metadata is checked.

## Verification

The [completed plan](../../../../docs/roadmaps/skill-suite/plans/roadmap-lifecycle.md) records structural checks, 23 helper tests, skill/plugin validation, archive extraction/install and reproducibility, and current user-link verification. The [five-case evaluation](../../../../evals/results/2026-09-05-roadmap-lifecycle.md) retains independent lifecycle/date decisions and semantic review. No roadmap is declared complete merely because a note is implemented.
