# Connect roadmaps, plans, phases, issues, and decisions

Use one place to navigate an area's work, with distinct authoritative records for its different concerns. The default organization for a substantial initiative is:

```text
docs/roadmaps/<area>/
  README.md
  plans/<feature>.md
  phases/<feature>/<phase>.md
  issues/<issue>.md
.agents/notes/<lifecycle>/<kind>/<date>-<decision>.md
```

Preserve established equivalents. Short phases can stay as sections in their feature plan until separate files help execution or handoff. A small task does not need an issue, plan, and phase file merely to fill every directory. If an issue tracker already owns work-item state, link its records; do not create a competing Markdown tracker. Never invent an external issue URL or state, or assume authorization to post it.

## Ownership and links

| Record | Owns | Links to |
| --- | --- | --- |
| Roadmap overview | Area scope, priorities, milestone summaries, dependencies | Its plans, active phases/issues, relevant decisions, and project index |
| Feature plan | Requirements and feature acceptance; selected approach and ordered phases | Primary roadmap, existing requirements authority if any, phase owners, relevant issues and decisions |
| Phase | The next deliverable, scope, phase acceptance, execution status, evidence, outstanding blockers | Parent plan and roadmap, included issues, prerequisite phases/plans, decision notes |
| Issue | A concrete defect, missing capability, or work item; expected outcome, status, resolution | Owning roadmap, implementing plan/phase when assigned, related issues, decision notes |
| Agent Note | Problem, consequential choice, genuine alternatives, consequences, and verification rationale | Affected issues, plans, phases, and current authoritative docs |

A phase belongs to one plan. An issue belongs to one roadmap; several phases can address it incrementally, with remaining scope explicit until its expected outcome is satisfied. Use existing identifiers or stable filenames and relative links for local records. Include links back to the owner so a session starting from an issue or note can recover its scope.

Keep requirements in the plan or existing requirements authority. A phase can describe the observable subset it delivers and link the parent criterion. Issue descriptions contain the necessary problem evidence or reproducer and expected outcome; avoid pasting the entire feature specification into each issue. Store detailed execution status and results once, with concise linked summaries in roadmaps/plans.

## State and completion

An overview carries the [roadmap lifecycle](../../make-codebase-agentic-roadmap/references/lifecycle.md) and [record dates](record-dates.md). Keep area/initiative status distinct from the progress of its individual outcomes. The navigation index summarizes those statuses; it does not become a separate delivery roadmap.

Reuse existing issue states. Without an established scheme, `open`, `in-progress`, `blocked`, and `resolved` are sufficient; record a reason for work cancelled or deferred. A blocker names the missing requirement, capability, or evidence and its owner when known. Opening an issue does not itself schedule or authorize its implementation.

Resolve an issue when its stated outcome is established and linked verification supports the resolution. An explicit duplicate or no-longer-needed disposition records the reason and surviving owner. A phase remains open while an included acceptance criterion or required verification is unmet, even if a related issue has been resolved. Completing a shared dependency can unblock consuming phases but does not complete them.

Apply the existing [phase completion rules](records.md) and [Agent Note lifecycle](../../make-codebase-agentic-agent-notes/references/lifecycle.md). An implemented decision note may accompany an unfinished phase with named verification gaps. Do not equate note lifecycle, issue resolution, and delivery completion.

## Cross-area example

A media-platform roadmap owns resumable upload behavior used by feed posting and editor export. Its upload plan owns the contract; its interruption issue links to the implementing phase and an upload-identity decision note. Feed and editor roadmaps link to that capability and required milestone instead of copying the issue or decision. Each consumer retains its own end-to-end acceptance criteria. A decision spanning both consumers remains one shared Agent Note with links to all affected owners.

## Recovery

Checkpoint the roadmap, plan, active phase, relevant issue blockers, and decision links, plus actual results and next executable action. Inspect source and evidence on resumption; linked summaries can drift. When moving an active record or transitioning a note's lifecycle, repair incoming links in the same change. Preserve historical evaluation artifacts and frozen notes as historical evidence rather than silently rewriting their claims.
