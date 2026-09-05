# Adapt architecture and concurrency

## Start from the app

Inspect the workspace/project, supported OS versions, Swift language mode, strict-concurrency/default-isolation settings, build configurations, dependency lockfiles, and extension targets. Read how one existing feature enters navigation, owns state, accesses data, and is tested. Do not infer execution semantics from the Swift compiler version alone.

For new apps, use Swift and SwiftUI by default; incorporate UIKit for justified interactions or platform integration. Existing UIKit, SwiftUI, or mixed apps retain their architecture unless the feature exposes a concrete problem. Apple supports both directions of [UIKit/SwiftUI integration](https://developer.apple.com/documentation/swiftui/uikit-integration). Record bridge ownership, updates, delegate/task lifetime, and teardown where the frameworks meet.

Organize substantial apps around cohesive product features and shared capabilities with demonstrated consumers. Document who owns navigation, session state, feature state, data access, and persistent assets. Choose Observation, ObservableObject, reducers, persistence tools, or dependency mechanisms based on deployment and project needs rather than applying one library everywhere. Modularize when build, ownership, reuse, or testing benefits justify the boundary; a feature folder does not require a separate package.

Represent navigation and business transitions so stale routes, deep links, restoration, and authentication changes have defined behavior. UI rendering should reflect owned state rather than become a second source of truth. A reopened feature must not inherit an old request merely because its view has the same type.

## Isolation is only part of correctness

Identify the isolation boundary of each mutable owner and the values crossing it. Keep UI-facing mutations appropriately isolated and use checked transfer mechanisms supported by the toolchain. Do not silence concurrency diagnostics with unchecked sendability or unsafe isolation without proving and documenting the synchronization contract.

Structured children should belong to the operation that awaits them. Store and cancel intentionally unstructured work under a clear owner; define any handoff that survives view disappearance. A task created from UI code may inherit actor isolation: making work `async` does not by itself establish that expensive work runs away from the UI. Confirm the target language/settings behavior before choosing an execution mechanism.

An actor may process other work at suspension points. Recheck account, generation, selected item, revision, or operation identity after `await` before publishing. A stale request must not overwrite refreshed data or clear a newer request's loading/error state. Cancellation is cooperative: handle late success, error, and cancellation for the correct identity, and do not turn cancellation into a user-visible failure by default.

See the [Swift data-race safety guide](https://www.swift.org/migration/documentation/swift-6-concurrency-migration-guide/dataracesafety/), [actor reentrancy specification](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0306-actors.md#actor-reentrancy), and [Swift concurrency reference](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/) for platform semantics; verify APIs and availability against the actual toolchain.

Exercise controlled races through the feature's public action: begin A, change identity or begin B, complete B then A, and reverse success/error orders. Include cancellation/logout while suspended. Assert resulting items, progress, errors, and state ownership, not merely whether `cancel()` was invoked.
