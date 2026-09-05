# Fieldnotes client snapshot

The shipping app uses UIKit view controllers and an injected, main-actor-isolated FeedStore. The deployment floor is iOS 16; current CI uses Swift 6 language mode. This fixture contains the extracted state owner only, not the Xcode app project, controller, media pipeline, or server. Do not claim to have tested those absent surfaces.

The server returns stable item identifiers and an opaque next cursor scoped to a particular feed snapshot. A nil next cursor means exhausted. Page boundaries can overlap. Failure leaves the requested cursor valid for retry. The networking layer can deliver a result after cancellation.

Refresh preserves the current visible items until replacement succeeds. A refresh supersedes any prior page or refresh. Cancellation must leave useful content and must not show a failure alert. A next-page error should leave the existing list and a retry path. The screen may issue a refresh while a page is pending.

Phase 1 is the extracted state-owner fix, with deterministic regression evidence. Controller integration, memory-bounded media loading, running-app accessibility, simulator journeys, and physical-device scrolling are a later phase because those artifacts are not included here. Do not expand into a rewrite or implement that later phase in this fixture.
