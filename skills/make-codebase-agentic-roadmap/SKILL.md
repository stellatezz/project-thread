---
name: make-codebase-agentic-roadmap
description: Create or revise area and initiative roadmaps that connect requirements, feature plans, phases, issues, and decisions, with a project index for shared priorities and dependencies. Use to organize substantial project delivery, not to design individual implementations.
---

# Maintain area and initiative roadmaps

Read current business goals, constraints, existing plans, and the [record ownership rules](../make-codebase-agentic/references/records.md). Identify the smallest valuable outcome before ordering later capabilities. A demanding reference product demonstrates workflows, not a requirement to copy its infrastructure.

## Choose the owning roadmap

For a substantial project, scope roadmaps to cohesive product areas or major initiatives, such as account and identity, feed and discovery, or media editing. Each owns its outcomes, priorities, milestones, dependencies, and deferrals. Use `docs/roadmaps/<area-or-initiative>/README.md` or established equivalents. Avoid both one detailed project-wide delivery list and a separate roadmap for every small feature.

Keep a lightweight index, normally `docs/roadmaps/README.md`, linking the roadmaps and summarizing shared priorities and cross-area dependencies. An existing `docs/roadmap.md` can serve as that index. Preserve useful existing boundaries and links when splitting a large roadmap; retain the original file as an index where practical. Do not create empty areas just to fill a hierarchy.

The area's overview is the entry point for its plans, issues, phase records, and relevant Agent Notes. Group delivery files in the area folder by default; keep decision notes canonical in the shared lifecycle tree. Read [delivery-record guidance](../make-codebase-agentic/references/delivery-records.md) to connect these records and preserve established layouts.

## Sequence requirements and plans

For each outcome, record user value, scope, priority/order, milestone, dependencies, and the owning requirements and feature plan when available. Feature-specific requirements and acceptance criteria belong in the plan or an existing requirements owner; shared business rules stay in product documentation. Summarize and link those records. A candidate can name an unresolved requirement without inventing a ready implementation plan.

Give each feature plan one primary roadmap owner. A capability used by several areas has one owning plan; consuming roadmaps link to it and state the required behavior or milestone. Record what must be delivered, which outcome depends on it, and what evidence will unblock the consumer. Surface cycles or incompatible priorities in the index for resolution. Do not duplicate the shared work or mark consumers complete when only their dependency finishes.

Sequence learning and risk reduction: prove a useful vertical slice before expanding catalogs, onboarding, monetization, or platform breadth without a product requirement.

Separate committed work from candidates. Resolve consequential priority or product changes with the user unless already authorized; continue independent work while questions are open. Do not fabricate estimates or mark milestones complete because implementation began.

Update the owning roadmap from plan/phase evidence using [phase execution](../make-codebase-agentic-phase/SKILL.md). Update affected issue, dependency, and index summaries when readiness or shared priority changes; keep detailed execution state in its plan/phase owner. Record changed rationale in [Agent Notes](../make-codebase-agentic-agent-notes/SKILL.md), and identify the roadmap, plan, phase, and relevant issue blockers in the checkpoint.
