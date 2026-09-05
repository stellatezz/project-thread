# Boundaries, state, and failure

## Make ownership observable

For a stateful resource, identify who creates it, who can mutate it, who observes it, and when it is released or made durable. This applies to a request, subscription, authenticated session, file, upload, editor project, transaction, and navigation flow. A test seam should expose the behavior that varies, not require a new generic framework.

Model meaningful transitions and invariants. For an upload, “bytes sent,” “server accepted,” and “published” may be different facts. For an edit, “visible,” “saved locally,” and “exported” may differ. Do not report success before the product's success point. Derive presentation flags from owned state where possible.

## Treat suspension as a possible state change

State can change while an operation waits. After each suspension, check the assumptions needed to apply its result: identity, account, request generation, revision, selection, or operation status. Cancellation requests alone may not prevent a callback or late result. Settle success, error, and cancellation for the correct operation; stale cleanup must not clear a newer operation's state.

Use lifetimes tied to the owning feature/session, with explicit handoff for work that survives it. Avoid orphan tasks and callbacks. Releasing an owner must stop or detach its work according to the contract. Test cancellation before start, during suspension, after remote completion, and during teardown when those races matter.

## Define remote ambiguity

At external boundaries validate payloads, authorization assumptions, identifiers, and limits. A timeout or connection loss does not establish that a remote write failed. Retry only when the contract permits it; distinguish retryable failures from permanent errors, cap attempts/backoff, and use server-supported idempotency or reconciliation for ambiguous mutations. A local request identifier cannot create server deduplication guarantees.

Define pagination and stream ordering, cursor scope, duplicate handling, staleness, and reconnect resynchronization with the backend contract. Missing support becomes a dependency or an explicitly limited local phase. Never present a mock or inferred server behavior as an integrated guarantee.

## Preserve what the product promises

Decide which data is durable, reconstructible, or disposable. Define atomic save/commit boundaries, ownership of referenced assets, schema versioning, and recovery from partial writes, low disk space, or failed upgrades. Verify migrations against representative old data and preserve recoverable originals until the migration succeeds. Resetting storage is a product decision when users can lose meaningful data.

Evaluate a new abstraction or dependency by its current responsibility, supported variation, compatibility floor, maintenance, transitive costs, migration, and residual glue. Record a consequential tradeoff in the owning note; do not treat a popular architecture or dependency as a universal default.
