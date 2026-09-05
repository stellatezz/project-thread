# Feed fixture checkpoint

Updated: 2026-09-05

Objective: prevent a stale page/refresh result, error, or cleanup from changing the newer feed; preserve useful content and retry state. [Active plan](../plans/feed-refresh.md): phase 1 complete, phase 2 pending. Phase 1 has no open acceptance criteria. The original task explicitly defers the app integration and device surfaces absent from this fixture.

Workspace: `/private/tmp/project-thread-feed-eval`. This is an isolated copy, not a Git repository; there is no branch or revision. Preserve `FeedStore.swift`, the test harness, `scripts/check.py`, copied task/context, all docs, the implemented Agent Note, and evidence artifacts. [Environment and SHA-256 hashes](../../artifacts/environment.json) identify the verified source. The original bundle and fixture have not been changed.

Implemented paths: `FeedStore.swift` owns request identity, guarded publication/cleanup, quiet cancellation, derived loading, and stable-ID deduplication. `Tests/FeedStoreRegression.swift` drives public actions with controlled fake completions. Current contract facts remain in [CONTEXT.md](../../CONTEXT.md). The [implemented decision owner](../../.agents/notes/implemented/behavior/2026-09-05-feed-request-ownership.md) explains alternatives, cancellation ownership, retained snapshot cursor, and costs. No prior decision was superseded.

Evidence, all on 2026-09-05:

- `python3 scripts/check.py`: macOS executable compiled with Apple Swift 6.1.2, Swift 6 language mode, complete concurrency checking, warnings-as-errors; 29 passed, 0 failed. [Exact log](../../artifacts/fixed/check.log).
- `python3 scripts/check.py --baseline`: original store compiles; identical harness gives 3 passed, 26 failed, exit 1 as expected. [Reproducer log](../../artifacts/baseline/check.log). The first failure shows old page items appended after refreshed rows; the next shows an old pagination error after refresh success.
- iOS source typecheck: standalone store, target `arm64-apple-ios16.0`, iPhoneOS 18.5 SDK, Xcode 16.4; exit 0. [Command and interpretation](../testing.md), [diagnostics log](../../artifacts/ios-typecheck.log).
- An initial harness-only protocol isolation compile failure was corrected; both superseded logs remain linked from testing.md.

Unverified: app target compilation/linking, UIKit rendering and retries, actual networking/server behavior, cancellation completion and controller teardown, simulator journeys, accessibility, media resource bounds, physical-device scrolling and lifecycle, performance, energy, and thermal behavior. The fake is intentionally cancellation-insensitive. The store has no independent transport handle and does not promise prompt cancellation while that API never returns. No backend or package has been added.

Next executable action: in the actual Fieldnotes app repository, read repository instructions and discover the project/workspace, scheme, CI commands, controller call sites, task ownership, and networking cancellation contract. Compare this checkpoint's source hashes with the fixture before porting the store fix and tests into the existing target. Then run the app's real build/test command and the controlled refresh-during-pagination controller journey in [phase 2](../plans/feed-refresh.md). The prerequisites are app source and phase 2 authorization; neither is supplied by this extracted fixture. Do not invent a scheme or claim simulator/device success from the macOS harness.
