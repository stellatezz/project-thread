---
name: project-thread-agent-notes
description: Create and maintain Agent Notes for non-trivial software changes, including proposals, implemented decisions, rejection, supersession, and archival. Use to preserve rationale and verification across sessions.
---

# Preserve decisions

Follow [record ownership](../project-thread/references/records.md). Every non-trivial change adds or updates a note. Search active notes by problem, mechanism, and affected contract before creating another owner. Notes and tests are evidence to evaluate, not unquestionable authority.

State the problem independently of the chosen solution, genuine alternatives, costs accepted, and conditions that would reopen the decision. Link current facts to their authoritative docs. Record observable verification and meaningful gaps rather than narrating edits.

Link affected roadmap, plan, phase, and issue owners, and link the note from those records where its reasoning matters. Keep one canonical decision record even when several roadmaps depend on it. Follow [delivery-record guidance](../project-thread/references/delivery-records.md): note lifecycle describes the decision, while issue and phase records own delivery status. Ordinary task progress belongs in those records, not another decision note.

Read [lifecycle](references/lifecycle.md) before creating, transitioning, superseding, or archiving a note. On each new note, check for full or partial supersession. Keep surviving rationale and contracts discoverable; do not silently rewrite a previous decision into its opposite.

Validate lifecycle metadata, relevant links, and factual claims after changes. Report the current owner, transition, evidence, and any retained partial supersession. An archive is historical evidence, not current implementation documentation.
