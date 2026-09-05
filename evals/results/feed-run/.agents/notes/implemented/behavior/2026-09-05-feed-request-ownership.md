# Feed completions must still own the visible state

Status: implemented

Date: 2026-09-05

## Problem

An awaited page or refresh may finish after a newer refresh has already replaced the feed. Main-actor isolation prevents simultaneous mutation but permits this interleaving across suspension. Old success appends or replaces current rows and cursors; old error shows an irrelevant alert; old deferred cleanup removes current progress.

## Decision and current owner

`FeedStore` owns one active request identifier. A started refresh replaces it; pagination only starts while idle with a non-nil cursor. Every post-await commit, error, and cleanup verifies that identity. Loading derives from its presence. Caller cancellation is checked before request start and before publication, and cancellation errors are silent. Items and cursor commit together on success; failure and cancellation preserve the useful snapshot. Stable IDs are deduplicated in first-occurrence order.

This note is the first decision owner in the isolated fixture. No earlier note exists to supersede. [CONTEXT.md](../../../../CONTEXT.md) owns implemented behavior and limitations; [the plan](../../../../docs/plans/feed-refresh.md) owns phase scope.

## Alternatives and accepted costs

- Serializing refresh behind `isLoading` would avoid overlap by making the requested refresh unavailable while a page waits. That contradicts the screen's accepted behavior.
- Cancelling old transport work alone cannot prevent a late callback under the supplied API contract. A request identity must still guard publication. Introducing store-owned unstructured wrapper tasks would also add task ownership and cancellation bridging absent from the established awaited API. The caller continues to own its task; the store invalidates stale results without promising to terminate transport work.
- Clearing the list/cursor on refresh would simplify state replacement but lose the useful snapshot on failure, contrary to the stated contract. Retaining the coherent prior items/cursor enables recovery.
- A reducer, observation framework, SwiftUI migration, or new dependency offers no demonstrated benefit for this local ownership defect and would expand the accepted phase.

The identifier is a small private implementation detail, not server identity. Superseded calls may continue consuming networking resources until the existing layer settles them. Cancellation of an uncooperative API does not immediately release the waiting action's loading state. First-occurrence deduplication traverses the accumulated IDs; no long-feed memory/performance claim follows. Repeated cursors do not trigger automatic requests, but controller prefetch policy still needs app-level verification. The current error string relies on controller knowledge of which action should be retried.

Revisit this decision if transport/resource cancellation must be prompt, the real controller reveals a retry ownership gap, feed payloads gain mutable content or revisions, account/query switching is added, or measured workloads justify incremental indexing. Such changes require their actual contracts and tests; this fixture does not invent them.

## Evidence and remaining gaps

[Verification](../../../../docs/testing.md) records 29 fixed checks passing under Swift 6 strict concurrency and warnings-as-errors. The same harness exposes 26 failures in the original store; three existing recovery behaviors pass. Standalone source also typechecks for the iOS 16 deployment target with SDK 18.5. The initial harness-only isolation compilation failure is preserved and resolved.

No controller, live API, media pipeline, simulator, or physical-device journey was tested. [Checkpoint](../../../../docs/checkpoints/current.md) names the next integration action. Implementation is established for phase 1 only.
