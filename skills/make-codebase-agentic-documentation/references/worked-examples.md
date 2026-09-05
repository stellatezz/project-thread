# Examples of structure and precise writing

These fictional examples illustrate editorial decisions. They do not establish behavior in an adopting application. Check the actual implementation before using a guarantee. The [writing reference](technical-writing.md) owns the principles.

## Preserve scope, timing, and failure

Weak: “The exporter reliably saves the project and carefully handles failures.”

Improved, when verified: “The exporter saves a project revision before starting the render. If the save fails, rendering does not start and the caller receives the storage error.”

The improved version identifies the actor, ordering, failure consequence, and observer. Shortening it to “The exporter persists state” loses information needed to reason about recovery.

## Keep enough detail beside the API

Weak: “See the upload decision for cancellation.”

Improved, when verified: “Cancellation stops scheduling additional chunks. A chunk already accepted by the server may still complete. The next attempt reconciles the saved upload identifier with server progress. See the upload decision for retry ownership.”

The caller needs the partial-completion behavior locally. The rationale and full reconciliation algorithm can remain in the linked decision. If the backend does not support this reconciliation, the documentation must state the actual limitation instead.

## Explain a race without narrating branches

Weak comment: “First we compare the request IDs, then return if they differ, and otherwise update the list.”

Useful comment, where the constraint is non-obvious: “An earlier refresh can complete after cancellation; only the active generation may replace the visible list.”

If the surrounding names and state transition already make this invariant clear, no additional comment is needed. The reason to keep a comment is the invariant it protects, not the number of lines in the implementation.

## Locate detail at its owner

Weak architecture section: an overview of the editor followed by every project-file field, all migration cases, and a walkthrough of export tests.

Improved structure:

- Architecture explains how editor state, project storage, and export cooperate.
- The storage reference owns the project format, compatibility, and migration failures.
- The export reference owns rendering behavior and cancellation.
- A cookbook explains how to add and verify a new editing operation.
- The decision note explains the chosen persistence boundary and alternatives.

Each detailed document links back to its context. A reader can understand the overall design before choosing the relevant detail, while an agent can search for the exact format or operation.

## Put prerequisites before dependent actions

Weak tutorial: begins by configuring authentication and background work, then reveals near the end that a local sample can run without either.

Improved tutorial: states the supported toolchain, runs the local sample, verifies an observable result, and then links the optional authenticated and background-work guides.

The tutorial's promised outcome determines the sequence. A production-integration tutorial may legitimately require authentication from the start; do not remove a real prerequisite to shorten onboarding.

## Keep test rationale and observable evidence

Weak: “Create a mock, call refresh twice, resolve the second promise, resolve the first, and expect three rows.”

Improved rationale: “Complete the cancelled request after the new refresh to verify that a late result cannot replace the current feed.”

The test code carries the mechanics. The comment explains why the ordering detects a specific regression. A phase record can say which behavior passed and where the result is recorded; it need not repeat every fixture line.

## Write useful diagnostics

Weak: “Operation failed unexpectedly.”

Improved user message, when accurate: “Export could not finish because the device ran out of storage. Your project is saved. Free space and try again.”

Keep “Your project is saved” only when the application has established that fact. Internal diagnostics can identify the failing export stage without exposing media paths or credentials in the user message.

## Preserve a rule when simplifying an instruction

Weak shortened instruction: “Run relevant tests.”

Improved instruction, for a repository with this requirement: “Changes to the project format must pass save/reopen checks using the oldest supported fixture. The storage testing reference owns the command and compatibility range.”

The trigger, observable behavior, and fixture requirement survive. The command and supported versions remain at their maintained owner.

## Retain depth when it carries a consequence

Existing: “The image cache releases decoded previews when the editor closes; project assets remain on disk until the project is deleted.”

Unhelpful shortening: “The editor manages its image cache.”

Keep the existing sentence. It distinguishes disposable previews from durable user assets, identifies two lifetimes, and prevents an incorrect cleanup. Word count alone provides no reason to change it.
