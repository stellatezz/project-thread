---
name: make-codebase-agentic-engineering
description: Design, implement, and verify maintainable software during feature planning, phase execution, or substantial fixes. Use for decisions about component boundaries, state, contracts, reliability, and test evidence; use make-codebase-agentic-review to assess resulting work.
---

# Engineer a maintainable outcome

Read relevant business rules, architecture, current consumers, implemented and rejected decisions, and cookbooks before choosing a structure. Establish the required behavior, failure consequences, compatibility obligations, and actual workload. Apply [shared record ownership](../make-codebase-agentic/references/records.md); decisions go in existing plans, references, and Agent Notes, not a parallel engineering document for every task.

## Define the contract before the structure

For a feature or substantial fix, establish:

- Observable success and recovery criteria through the application's real entry path.
- Component responsibilities, state/resource owners, and lifecycle boundaries.
- Interfaces and their success, error, cancellation, and duplicate-request behavior.
- Persistence, upgrades, migrations, and what data must survive interruption.
- Relevant performance/resource budgets derived from product requirements and representative workloads.
- Verification that can detect the intended failure, including integration boundaries.

Scale this work to the risk; an obvious local correction need not introduce a new plan. Preserve existing patterns unless evidence justifies change. Routine choices within agreed behavior belong to implementation. Changes to business behavior, public contracts, data guarantees, or consequential dependencies must be resolved through the feature plan and owning Agent Note using existing authorization.

## Implement with explicit ownership

Give each stateful resource one clear owner and a defined release or persistence point. Represent meaningful business transitions explicitly; avoid unrelated booleans that permit impossible states. Keep dependencies between features understandable and testable. Introduce abstractions for demonstrated responsibilities or variation, and evaluate dependencies against compatibility, maintenance, and retained complexity. Read [code structure](references/code-structure.md) when organizing features, changing dependencies, or clarifying responsibilities. Use [codebase documentation](../make-codebase-agentic-documentation/references/codebase-documentation.md) when the implementation needs a module explanation, API contract, or non-obvious comment.

Validate at actual trust boundaries. Define timeouts, retry limits, cancellation propagation, idempotency, and reconciliation where the operation needs them. Preserve required data across failure and upgrades. Read [boundaries and failure](references/boundaries-and-failure.md) for async workflows, cross-component contracts, persistence, or dependency choices.

## Verify the requirement

Choose focused unit tests, integration tests, application journeys, or performance measurements according to behavior and risk. An assertion must fail on the intended regression; passing checks alone do not prove the feature matches the user's request. Read [verification](references/verification.md) when selecting evidence or closing a phase.

Update affected facts and the owning Agent Note for every non-trivial change. Record a cookbook only when a useful procedure has been learned. Complete phases under the shared rules, then leave a [checkpoint](../make-codebase-agentic/references/checkpoints.md) with actual evidence and unavailable checks. For native iOS implementation, also use [iOS](../make-codebase-agentic-ios/SKILL.md).
