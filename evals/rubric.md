# Evaluator rubric

Assess observable decisions and artifacts rather than wording. Mark each item pass, fail, or unverified with a concrete reason.

| Scenario | Required outcome |
| --- | --- |
| Existing app | Preserves established UIKit/coordinator/repository architecture; implements only the approved slice; deviations need evidence and rationale |
| New app | Establishes business context, navigation, state/data ownership, and a bounded Swift/SwiftUI slice; no invented deployment target or extra product scope |
| Feed | Rejects stale success/error/cleanup across refresh; deduplicates stable IDs; retains retry cursor on failure; bounds decoded media/resources; measures representative scrolling separately |
| Upload | Preserves source ownership and durable recovery identity; separates transfer/acceptance/publication; treats missing server idempotency/reconciliation as dependency; never guarantees safe blind retry |
| Location | Handles permission changes and stale accuracy/timestamps, ends subscriptions, reconciles reconnect gaps/conflicts, and keeps background/battery claims device-dependent |
| Editor | Preserves old/new projects and assets; defines undo/redo and timebase; exports a defined revision; arbitrates cancel/completion and validates actual output without losing work |
| Concurrency | Recognizes reentrancy across await, invalidates account/operation identity, handles late results and stale cleanup, and verifies controlled completion ordering |
| Accessibility | Designs reachable alternatives and meaningful state feedback; verifies the complete supported journey in the running app or leaves it explicitly unverified |
| Continuity | Reads the working tree and owners, catches overstated checkpoint progress, preserves unrelated edits, and leaves the correct next action without needing old conversation |
| Evidence | Distinguishes compiled, logic, simulator, device, and unverified results; failed launch is not a journey pass; unmet required criteria keep the phase open; no unauthorized publishing |

For the feed exercise, examine production code and run tests, including a negative control against the original fixture where feasible. Ensure tests assert observable items, cursor, error, and loading state. Verify a stale error cannot clear a newer request's loading state and overlapping page IDs do not duplicate visible items. A cancellation path should not leave the owner stuck loading or display an error for user cancellation.

Structural validation, guided scenario reasoning, isolated Swift execution, and real iOS app/device verification are different evidence. Keep the evaluation summary explicit about which occurred.
