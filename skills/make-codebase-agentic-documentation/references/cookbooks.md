# Learn a repository cookbook

Write a cookbook when a non-obvious procedure is likely to recur and has been exercised in this repository. State its trigger, prerequisites, owning components, ordered actions, recovery behavior, and the verification that establishes success. Link the product or technical contract instead of redefining it. Record the relevant toolchain or API version if the steps depend on it.

Examples to adapt after implementing and verifying the procedure:

| Procedure | Details the repository must supply |
| --- | --- |
| Add a feed section | Route and state owner, cursor contract, stable identity, reusable media loader, refresh test, accessibility journey |
| Introduce an upload type | Durable job record, asset ownership, authentication, server reconciliation, retry/cancel UI, interrupted-transfer test |
| Add an editing operation | Project format, command or state transition, undo boundary, timing rules, save/load compatibility, preview and export checks |
| Add a location-driven screen | Authorization owner, accuracy/freshness contract, subscription lifetime, stale/offline presentation, device checks |

Do not publish a generic checklist as a proven project procedure. If steps have not run, label the recipe provisional and identify its validation gap. Do not encode credentials, local machine paths, or temporary workarounds as permanent conventions.
