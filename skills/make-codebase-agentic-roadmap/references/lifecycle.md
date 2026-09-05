# Roadmap lifecycle

A roadmap owns intended outcomes and their sequencing. An Agent Note owns a consequential decision and its rationale. Keep separate records linked from the roadmap overview; adopting a decision does not finish its delivery roadmap. Existing repository equivalents remain valid when their meanings are explicit.

## Declare scope and status

Use `Kind: area` for an ongoing product or capability area and `Kind: initiative` for a bounded outcome. Record `Status` and dates in the overview using [record dates](../../make-codebase-agentic/references/record-dates.md).

| Status | Meaning and transition evidence |
| --- | --- |
| `draft` | Candidate direction; scope, priority, or dependencies are not yet agreed for active pursuit |
| `active` | An agreed direction is being pursued; its individual outcomes can be candidate, underway, or complete |
| `paused` | Pursuit is intentionally suspended; record `Pause reason` and `Resume when` |
| `completed` | The defined scope is delivered and its acceptance criteria are satisfied; link `Completion evidence` |
| `retired` | Remaining direction is abandoned or replaced; record `Retirement reason` and link the successor when one exists |

Move a draft to active when its direction is agreed. Resume a paused roadmap when the stated condition is met and pursuit is authorized. A dependency blocking one phase does not automatically pause the whole roadmap. Use retired when cancelling unfulfilled scope; do not label it completed to clear the active list.

An area roadmap can stay active while every currently listed milestone is complete. Complete it only when its own defined remit ends and the required scope is delivered. A bounded initiative completes against its plan/phase evidence. An implemented Agent Note or a successful shared dependency cannot substitute for consumer acceptance.

If a completed or retired roadmap needs new work, prefer a linked follow-on initiative when the outcome differs. Reopening the same scope is possible with an explicit reason, preserved prior completion/retirement evidence, and revised criteria. Consequential direction changes follow the existing planning and decision rules; status editing does not grant execution authority.

## Archive after completion or retirement

Archiving is preservation, not another delivery status. Retain `Status: completed` or `Status: retired`, add `Archived: YYYY-MM-DD` and `Archive reason`, and leave a discoverable link in the project index. A roadmap can remain at its stable path or move to an existing archive convention. If it moves, repair active incoming links in the same change. Do not move shared Agent Notes or referenced plans automatically: they may still guide another area.

Only archive when the roadmap no longer guides current work and its useful dependencies, decisions, and successor links have maintained owners. Preserve the sealed overview and historical evidence; ordinary updates should reference a new active owner. Its archived state does not archive its linked Agent Notes, whose [lifecycle](../../make-codebase-agentic-agent-notes/references/lifecycle.md) is independent.

## Minimal examples

An ongoing feed area may say `Kind: area`, `Status: active` while its pagination milestone is complete. An upload-recovery initiative with unmet interruption tests remains active or paused even if its architecture note is implemented. If the product drops uploads entirely, retire that initiative with the cancellation reason rather than claiming delivery.

The project index summarizes roadmap status and links to its owner. It has dates but no delivery lifecycle of its own. Verification must inspect the actual scope and evidence; metadata validation can check fields and dates, not prove completion, authorization, or archival immutability.
