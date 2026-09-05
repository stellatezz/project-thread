# Explain the code where readers use it

Use this reference when a feature changes module responsibilities, callable behavior, configuration, diagnostics, or non-obvious implementation rules. Read the owning code and representative callers first. [Code structure](../../make-codebase-agentic-engineering/references/code-structure.md) owns implementation decisions; this reference owns their explanation.

## Modules and component references

Explain the component's purpose, responsibilities, consumers, dependencies, and state or resource ownership. Document behavior that consumers rely on: configuration and defaults, success and failure, lifecycle, extension points, and limitations. Describe relationships rather than inventorying every private helper. A short module may need only a focused comment; a subsystem used by several features may justify a reference page.

Keep project-wide composition in architecture documentation. Link decisions and extended algorithms to their owners. Document operational constraints such as a cache that lasts until process restart or a migration that requires exclusive access. Routine cleanup tasks belong in issues or plans rather than a permanent contract.

## Functions, APIs, and events

Explain facts the signature cannot express: input preconditions, distinct return meanings, mutations, thrown or returned errors, ordering, concurrency isolation, cancellation, retryability, and durability. Cover only the relevant facts. Do not restate every parameter whose name and type are already clear.

Distinguish requesting cancellation from stopping work, acceptance from completion, and local persistence from remote confirmation. For events and callbacks, state when they occur relative to observable changes, whether listeners can change the current operation, and who owns subscriptions. For an adapter, explain information that is intentionally transformed or discarded and what callers can still rely on.

Keep essential guarantees near the API. A caller should not need to read an entire decision record to discover that an operation may partially succeed. Link detailed implementation reasoning without hiding the behavior needed for correct use.

## Internal comments and test explanations

Use comments for invariants, non-local dependencies, race ordering, unusual ownership, or failure recovery that a maintainer might accidentally break. Prefer code with clear names and explicit transitions when that expresses the rule directly. A comment cannot repair contradictory control flow.

Test comments explain non-obvious observation or setup: why a late response must be released in a particular order, why an actual entry path matters, or why a platform accommodation exists. Assertions and test names should carry ordinary behavior. Avoid walkthroughs of fixture construction or an inventory of every test in a README.

## Configuration, errors, and visible text

Configuration references state units, defaults, valid combinations, precedence, and when changes take effect. Comments explain surprising ordering or scope, while the configuration itself shows the entries. Prefer generated option lists when the repository already has an authoritative schema and generator.

A useful diagnostic identifies the failing operation or subject, the relevant condition, and a recovery action when known. Do not expose credentials, sensitive payloads, or private filesystem details merely to make a message specific. User-facing messages should describe the consequence and available action; internal traces can carry technical context under the project's diagnostic policy.

Prompts and model-visible summaries are observable behavior. Document strings at the component that owns them and inspect any generator or renderer that changes the final output. Avoid copying another component's text or schema into a competing reference.

## Verify the explanation

Walk through one successful call and one meaningful failure or interruption using the implementation and its actual consumers. Check that the prose identifies who observes the result and what state survives. Exercise examples when runnable; distinguish source inspection from executed evidence. Preserve links when symbols or files move, and update current notes without rewriting archived history.
