---
name: project-thread-plan
description: Turn feature requirements or a substantial fix into observable acceptance criteria, resolved decisions, and implementable phases, linked to the owning area or initiative roadmap. Use before consequential changes or when an existing plan needs revision.
---

# Plan an outcome

Recover relevant business rules, the owning area or initiative roadmap, related issues, architecture, current consumers, notes, and cookbooks using [record ownership](../project-thread/references/records.md). Reuse the current feature plan when it owns the outcome. Link it to one primary roadmap; record other areas as consumers or dependencies rather than duplicating the plan.

## Make the work implementable

- Own the feature's requirements here, or link the existing requirements authority. State the user journey, success and recovery behavior, scope, and non-goals. Link shared business rules; include important failure consequences and compatibility obligations.
- Apply [engineering](../project-thread-engineering/SKILL.md) to responsibilities, interfaces, state ownership, persistence, migrations, dependencies, and verification. For an iOS client, also apply [iOS](../project-thread-ios/SKILL.md).
- Define acceptance criteria that can be observed through the real entry path. For interaction work, include loading, errors, permissions, accessibility, and supported layouts as relevant.
- Divide the outcome into phases that produce testable behavior. Name dependencies, their owning plans/roadmaps, affected areas, checks, and evidence required for each phase. Keep uncertain later work coarse. A completed shared dependency does not by itself verify a consuming feature's journey.
- Distinguish routine implementation latitude from unresolved business behavior or public contracts. Record alternatives and the decision in the owning Agent Note. Use existing authorization; ask only for decisions that remain consequential and unresolved.

Use [delivery-record guidance](../project-thread/references/delivery-records.md) for issue and phase links. In a substantial feature, keep detailed phase criteria, included issues, and evidence in separate phase files, linked from the plan's ordered overview. Short phases can remain in the plan. Issues describe actionable problems/work; they do not replace feature requirements or confer implementation authorization. Link the relevant decision notes instead of copying their rationale.

Mark the plan ready when the next phase can proceed with its necessary decisions and dependencies resolved. A blocked later integration need not prevent an explicitly scoped local phase, but mocked behavior and deferred acceptance remain visible. Use [phase execution](../project-thread-phase/SKILL.md) to implement; do not rewrite intended behavior as shipped facts.
