# Fixture verification

Recorded 2026-09-05. Environment: macOS 15.3.1 arm64, Apple Swift 6.1.2, Xcode 16.4 (16F6). [Environment and source hashes](../artifacts/environment.json) identify the tested copy. There is no Git branch/revision: this is an isolated three-file fixture copy with local additions.

Run from `/private/tmp/project-thread-feed-eval`:

```sh
python3 scripts/check.py
python3 scripts/check.py --baseline
```

The first command compiles `FeedStore.swift` and `Tests/FeedStoreRegression.swift` into a native macOS executable using `swiftc -swift-version 6 -strict-concurrency=complete -warnings-as-errors -parse-as-library`, with a workspace-local module cache. It then executes the harness with a 60-second deadlock timeout. Full exact commands, stdout/stderr, and exit codes are recorded in [fixed/check.log](../artifacts/fixed/check.log). Result: compiler exit 0, harness exit 0, **29 passed, 0 failed**.

The second command compiles the identical test source with [the original store](../artifacts/baseline/FeedStore.swift). Compilation succeeds, and execution intentionally exits 1: **3 passed, 26 failed**. [baseline/check.log](../artifacts/baseline/check.log) reproduces old items appended after refreshed content, stale pagination alerts, stale loading cleanup, duplicate IDs, and cancellation failures. This nonzero exit is the expected negative-control evidence, not the fixed implementation result.

The harness invokes public awaited actions with a main-actor fake API and checked continuations. Request arrival and completion are explicitly coordinated, without sleeps or timing assumptions. The fake intentionally ignores cancellation and can deliver late success or errors. A separate immediate fake checks already-cancelled entry. Tests observe items, cursor, loading, errors, and requested cursors. No real controller, networking stack, backend, or persistence runs.

The standalone store was also typechecked with:

```sh
swiftc -swift-version 6 -strict-concurrency=complete -warnings-as-errors -module-cache-path artifacts/ios-module-cache -target arm64-apple-ios16.0 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.sdk -typecheck FeedStore.swift
```

Result: exit 0, no diagnostics; [ios-typecheck.log](../artifacts/ios-typecheck.log). This proves source compatibility for that target/SDK, not an iOS app build, link, launch, or runtime journey. The test executable ran on macOS, not an iOS simulator.

The initial harness compilation failed because `Snapshot.description` inherited main-actor isolation while satisfying a nonisolated protocol requirement. The helper now has immutable Sendable fields and only its store-reading initializer is main-actor isolated. No unsafe isolation/concurrency escape was added. These superseded failures remain in [fixed/initial-compile-failure.log](../artifacts/fixed/initial-compile-failure.log) and [baseline/initial-compile-failure.log](../artifacts/baseline/initial-compile-failure.log).

Xcode SDK discovery emitted sandbox-related filesystem event/cache warnings but returned the SDK path and version. No Xcode project or simulator journey was attempted because the fixture contains no app. Follow the [phase 2 plan](plans/feed-refresh.md) for integration evidence; do not treat logic checks as UI or device evidence.
