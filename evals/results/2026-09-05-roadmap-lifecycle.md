# Roadmap lifecycle and date verification

Date: 2026-09-05. Bundle version: 0.2.1.

An independent Codex agent received the [five-case task](../fixtures/roadmap-lifecycle/TASK.md), a fresh temporary workspace, and the roadmap skill entry point. It did not receive the parent conversation, scoring criteria, previous results, or validator tests. The [response](roadmap-lifecycle/RESPONSE.md) and [evaluation record](roadmap-lifecycle/EVALUATION.md) are retained unchanged, alongside the supplied task.

## Outcome review

| Case | Observed decision |
| --- | --- |
| Ongoing area with all listed milestones complete | Retained active area ownership and separate dated milestone evidence |
| Cancelled initiative with unfinished acceptance | Retired the roadmap, preserved unmet tests and successor ownership, and retained the still-consumed format note as implemented |
| Paused initiative whose condition is satisfied | Resumed active only with the supplied authorization; did not confuse device access with completed verification |
| New request related to an archived roadmap | Preserved the sealed overview and proposed a distinct draft follow-on with unresolved scope |
| Legacy draft with no creation evidence | Used unknown Created with provenance, retained the real edit date, rejected filesystem time as creation evidence, and left unspecified area/initiative kind unresolved |

The author reviewed all five cases against the task facts and the owning references. The response kept roadmap and note lifecycles independent, preserved stable note dates and archive history, and named missing information instead of inventing metadata. No guidance correction was needed after this exercise. This is a decision exercise, not an executed application or proof that every future roadmap will be classified correctly.

## Structural and implementation checks

The bundle checker and 23 helper tests pass on Python 3.14.4. Seven new tests cover calendar errors, reversed dates, unknown-date provenance, duplicate/header-only metadata, roadmap states and their required fields, archival restrictions, note filename dates, and validation integration with frozen records. The original installation/migration/archive tests also pass. An initial test-file import failed because of an unmatched parenthesis; it was corrected before the complete passing run.

The changed roadmap skill passes Codex skill validation; the plugin manifest passes validation. Existing legacy records received Created dates from first Git appearance, following renames, all on 2026-09-05. Historical evaluation sources were excluded from the new metadata requirements and preserved. The [plan](../../docs/roadmaps/skill-suite/plans/roadmap-lifecycle.md) owns final archive and installed-source verification.

The checker validates this bundle's paths and header conventions. It does not prove dates truthful, names unchanged across history, evidence sufficient for completion, or archives immutable. Frozen bodies can retain historical links; metadata remains checked. No app, device, or automatic host-loading verification was performed.
