# Evidence before removal

Adapted from DeepSeek's investigation-and-proposal workflow. Its repository-specific backends, package rules, and tool commands are not universal requirements.

## Trace consumers

Use `rg` for exact symbols, configuration keys, wire names, exports, registration paths, and alternate spellings. Read the callers. Separate production consumers from tests/docs and inspect ambiguous demos, scripts, generated code, dynamic registration, public clients, and persisted formats. Absence from a static search is not proof that an external API is unused.

Read the relevant notes, including rejected attempts. For each candidate name the exact surface removed, consumers affected, capability given up, compatibility or migration cost, and observable acceptance criteria. Reject or downgrade candidates whose cost exceeds demonstrated benefit, or whose load-bearing contract has no replacement.

## Trace ownership and lifetimes

Map each state flag, pending promise, cancellation path, retry loop, disposer, and durable record to a distinct owner or transition. Mirrored liveness facts may collapse into one owner, but preserve separate mechanisms for publication/rollback, callback containment, terminal-outcome arbitration, process ownership, and completed teardown when they protect different obligations.

At defensive code, identify the source and next owner of the value. Parsers, network input, durable files, processes, and external callbacks may be actual trust boundaries. Do not assume arbitrary hostile typed objects in an internal call are a product contract, or remove validation from a real boundary because typed callers exist.

For a dependency swap, inspect exact coverage, residual glue, platform/deployment compatibility, maintenance, license, transitive footprint, and migration cost. Weigh net retained complexity including tests and docs. Existing code is not automatically better; fewer local lines are not automatically simpler.

## Produce a reviewable proposal

Include evidence paths, production versus non-production callers, concrete removal/folding steps, affected docs/tests/configuration, alternatives, risks, and reintroduction conditions. Consolidate with an existing proposed note when it already owns the idea. Tiny local improvements can be actionable inline notes if the repository uses them; do not accumulate speculative complaints.

During authorized implementation, verify the real entry path and meaningful negative guarantees. Search removed names across code, configuration, migrations, docs, and tests; determine why each remaining occurrence is valid. Update the implemented note and retain partial supersessions. Use the repository's real validation commands, never inherited commands from the source inspiration.
