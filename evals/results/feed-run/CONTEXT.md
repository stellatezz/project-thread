# Fieldnotes client snapshot

The shipping app uses UIKit view controllers and an injected, main-actor-isolated FeedStore. The deployment floor is iOS 16; current CI uses Swift 6 language mode. This fixture contains the extracted state owner only, not the Xcode app project, controller, media pipeline, or server. Do not claim to have tested those absent surfaces.

The server returns stable item identifiers and an opaque next cursor scoped to a particular feed snapshot. A nil next cursor means exhausted. Page boundaries can overlap. Failure leaves the requested cursor valid for retry. The networking layer can deliver a result after cancellation.

Refresh preserves the current visible items until replacement succeeds. A refresh supersedes any prior page or refresh. Cancellation must leave useful content and must not show a failure alert. A next-page error should leave the existing list and a retry path. The screen may issue a refresh while a page is pending.

Phase 1 is the extracted state-owner fix, with deterministic regression evidence. Controller integration, memory-bounded media loading, running-app accessibility, simulator journeys, and physical-device scrolling are a later phase because those artifacts are not included here. Do not expand into a rewrite or implement that later phase in this fixture.

## Implemented fixture behavior (2026-09-05)

`FeedStore.swift` retains the injected `@MainActor` owner, `FeedAPI`, and awaited `refresh()` / `loadNext()` actions. `isLoading` is now derived from a private active request identifier. Every completion, error, and cleanup must still own that identifier before changing state. A started refresh invalidates all earlier requests; an already cancelled action is a no-op.

The visible items and their cursor remain a coherent snapshot until refresh succeeds. A failed or cancelled refresh preserves both; old requests remain invalid even if that refresh fails. The existing snapshot cursor can still be used by a later explicit next-page action. A next-page failure preserves the cursor for explicit retry and reports an error; cancellation reports no error. Starting a current action clears the previous error. The public error remains a string; the controller must associate retry presentation with the action it initiated.

Items are deduplicated by stable ID, retaining first occurrence and existing server order. A refresh replaces the list; a page appends previously unseen IDs. Empty pages preserve items and adopt the returned cursor, including nil exhaustion. A repeated non-nil cursor stays eligible for a subsequent explicit action; the store does not automatically request another page or claim the server guarantees progress. The model contains only IDs, so content-update or deletion reconciliation is not added.

The controller retains ownership of its calling tasks, and the store awaits the existing API directly. This fix adds no detached requests or dependencies. Supersession invalidates publication rather than forcibly stopping transport work. Caller cancellation is propagated naturally through the awaited call and rechecked before commit, including when the API ignores it. If that API never returns, cancellation alone does not immediately settle the awaiting action or its loading state; actual transport completion/cancellation behavior and controller teardown remain integration concerns.

These are in-memory fixture facts, not shipping-app verification. The [plan](docs/plans/feed-refresh.md), [testing evidence](docs/testing.md), and [checkpoint](docs/checkpoints/current.md) own completion status and the handoff.
