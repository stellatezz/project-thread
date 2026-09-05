# Make the implementation understandable

Use this reference when adding a substantial feature, splitting responsibilities, or reviewing code that is difficult to change safely. Inspect existing patterns and actual consumers before proposing a new structure. [Boundaries and failure](boundaries-and-failure.md) owns asynchronous behavior, durability, and external ambiguity.

## Organize around responsibilities

Keep related behavior and the state it owns together. A component should have a responsibility that a maintainer can describe and a lifecycle that its consumers can use correctly. Split code when responsibilities, dependencies, or lifetimes evolve independently. Avoid creating layers solely to fit a familiar architecture diagram.

Trace a real journey through the entry point, feature state, shared capabilities, persistence, and external calls. Dependencies should make that flow understandable without requiring readers to discover hidden registration or unrelated global state. Follow the project's established dependency direction; record a necessary exception with its reason and consumers.

Promote code into a shared capability when multiple real consumers need the same behavior and ownership. Similar syntax alone does not establish a shared responsibility. A generic helper that forces unrelated features to coordinate changes may retain more complexity than two small local implementations.

## Make names and state reveal behavior

Use the product's vocabulary consistently across code, interfaces, documentation, and tests. Distinguish identifiers, revisions, requests, and lifecycle states when confusing them could cause an error. Follow existing naming and type conventions unless a demonstrated ambiguity justifies a change.

Prefer explicit transitions for meaningful business states. Keep invariants near the state owner and expose the operations consumers need rather than unrestricted mutation. Names such as `savedRevision` and `pendingUpload` communicate different facts; a broad `isComplete` flag can conceal whether local or remote completion is meant.

Give functions a coherent operation and make their side effects visible through their interface or local documentation. Use early exits, decomposition, or small types where they clarify the relevant conditions. File length, function length, and abstraction count are signals to inspect, not universal quality limits.

## Keep interfaces and failures usable

An interface should expose meaningful input, output, failure, and lifecycle behavior without requiring consumers to understand private implementation order. Validate where data or authority crosses an actual trust boundary. Do not scatter defensive fallbacks that hide an invalid state the owning component must reject.

Place domain decisions with the product or feature owner. Keep transport, storage, and presentation adapters focused on their responsibilities. A dependency should have an explicit initialization and release path; avoid hidden service lookups that make an ordinary function's requirements impossible to discover.

Handle errors at the level that can recover or explain the consequence. Preserve information needed by callers, and name intentionally ignored failures with their conditions. Use comments for non-obvious constraints; [codebase documentation](../../make-codebase-agentic-documentation/references/codebase-documentation.md) defines what belongs beside the implementation.

## Verify through consumers

Choose an observation that establishes the required behavior at the correct level. A local unit test can pin a state transition; an integration or application journey checks that real consumers wire it correctly. Use substitution at existing dependency boundaries when it improves deterministic evidence. Avoid test-only architecture that exposes every private detail or makes tests mirror the implementation.

Before accepting a restructuring, compare the actual call paths and retained responsibilities. Confirm that compatibility, failure, cancellation, and data guarantees survive. Update the explanation at its owner so the next maintainer can understand the final design without reconstructing the editing session.
