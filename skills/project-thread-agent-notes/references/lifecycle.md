# Agent Note lifecycle

Reuse established repository semantics where present. Otherwise use `.agents/notes/<lifecycle>/<kind>/<date>-<topic>.md`, with a title and `Status: <lifecycle>`. Useful kinds include architecture, behavior, process, and simplification; create kinds only when needed.

| Lifecycle | Required substance |
| --- | --- |
| `proposed` | Problem, proposal, genuine alternatives, observable acceptance criteria, risks and unresolved decisions |
| `implemented` | Problem, present-tense decision, genuine alternatives, consequences, actual verification and gaps |
| `rejected` | Evaluated problem and proposal, alternatives, explicit verdict and reason |
| `archived` | Frozen historical snapshot of an implemented decision, with previous lifecycle and archival reason/date |

Move and rewrite a proposal when implementation is established. Implementation can have named device or release verification gaps; the note must not imply those criteria passed, and the feature phase remains incomplete if they are required. A rejected proposal preserves what was considered and why it lost. A reversal gets a new cross-linked decision, not an edit that erases the earlier choice.

## Supersession and retention

Identify the current owner from code, configuration, contracts, and incoming links. Dates and titles are discovery hints. Any surviving behavior, durable format, compatibility obligation, or still-useful rejected alternative makes supersession partial: retain and cross-link both records.

For full supersession, transfer every useful rationale, alternative, consequence, verification result, coverage gap, and reintroduction condition to the surviving owner before consolidation. A current negative decision may deserve its own note even when its old implementation is gone. Do not turn every code edit into a repository-wide archival audit.

Only implemented records enter the default archive. Proposals stay active or become rejected. Archive by adding date/reason and a current-owner link, then moving the complete record and its companions. Repair current inbound links; historical outbound links may remain as a snapshot. Do not edit frozen content during ordinary maintenance.

A rejected record may be removed only when its reasoning no longer prevents a plausible mistake and the task authorizes that cleanup. Consolidation similarly requires proving that unique decision information survives. Inspect inbound references and search removed names afterward. Do not delete solely due to age or word count.

Restore through the repository's established integrity procedure. Without one, create a new active note linking the frozen artifact instead of silently thawing history.
