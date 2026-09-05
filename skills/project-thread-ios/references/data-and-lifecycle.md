# Client data and lifecycle

Choose the sections relevant to the feature and record the actual contracts in the project, not a duplicate generic checklist.

## Authentication and requests

Keep credential storage behind the established secure-storage owner, typically Keychain for secrets. Define expiry, refresh coordination, failed refresh, account switching, and logout cleanup. Invalidate account-scoped requests, caches, drafts, and callbacks according to the product's retention rules. A late refresh must not resurrect a logged-out session. Never log tokens, raw personal media, or precise location by default.

Define request identity, cancellation, timeouts, retries, deduplication, and staleness. Handle non-success status and malformed payloads at the network boundary. Connectivity observations can guide presentation but do not prove a request will succeed. An interrupted mutation may have succeeded remotely; use supported idempotency or reconciliation rather than blind retry.

For pagination and streams, specify stable identity, cursor scope, server ordering/revision, stale-response rejection, and reconnect resync. Missing server capability remains a dependency, even if a local mock is useful for a limited phase.

## Local data

Separate durable user work from replaceable caches. State the source of truth, cache freshness/invalidation, size/eviction policy, account scope, and behavior offline. Bound media by decoded cost and live resource counts as well as disk bytes. Expiration must not delete the only copy of user work.

For offline edits, record durable operation identity, pending/failed/conflicted state, ordering, retry safety, and reconciliation. Select persistence based on data/query/migration needs and deployment constraints. Define schema evolution and atomic save boundaries; exercise representative older data, interrupted saves, failed migrations, unavailable assets, and low storage. Preserve recoverable data rather than silently resetting it.

## App and system lifetimes

Map foreground/background, scene changes, termination, restoration, and relaunch to owned operations. Save valuable progress at appropriate commit points; do not depend on receiving a final termination callback. Ordinary tasks do not guarantee indefinite background execution. Use platform background mechanisms only for a supported capability and verify its actual restrictions.

For background transfers, persist identifiers and file ownership so the app can reconnect to system-owned work. Define user cancellation, interrupted completion delivery, and missing source files. Do not promise resumability without the transfer API and server contract supporting it. See [background transfers](https://developer.apple.com/documentation/foundation/downloading-files-in-the-background) and verify upload-specific constraints for the target SDK.

Deep links and notification payloads enter through a trust boundary: validate routes and identifiers, apply authentication/authorization, and handle missing content. Make repeated delivery safe. Permission requests need a contextual trigger, correct usage descriptions/entitlements where required, denied/restricted states, and reevaluation after Settings changes.

Keep diagnostics useful: operation identifiers, state transitions, sanitized failure categories, and relevant timing. Respect sensitive data, retention, and consent constraints. Verify memory, disk, energy, and thermal behavior for workloads that retain media, track location, or run sustained processing.
