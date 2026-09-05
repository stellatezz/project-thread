---
name: make-codebase-agentic-phase
description: Execute or resume an agreed software feature phase, verify its acceptance criteria, and update repository records for continuation. Use when a plan is ready or work is already underway.
---

# Execute a phase

Recover the active phase file or plan section, its parent plan and roadmap, linked issues/decisions, and [checkpoint](../make-codebase-agentic/references/checkpoints.md); inspect the actual working tree and relevant records. Preserve unrelated changes. Confirm the next phase's scope and unresolved dependencies without re-requesting settled authorization. Use [delivery-record guidance](../make-codebase-agentic/references/delivery-records.md) to keep phase evidence and issue state with their owners.

Apply [engineering](../make-codebase-agentic-engineering/SKILL.md), plus [iOS](../make-codebase-agentic-ios/SKILL.md) for native iOS work or [web](../make-codebase-agentic-web/SKILL.md) for web clients. Use established repository patterns and cookbooks. Implement the phase through the real application entry path, including the accepted failure and recovery states.

When evidence invalidates the plan, update the owning plan and Agent Note. Resolve changed business behavior or public contracts before implementing that dependent change. Continue independent authorized work rather than inventing backend behavior or expanding scope to unblock yourself.

## Verify and close

Map each criterion to a result. Run the target's required checks and risk-relevant journeys. Tests must detect the intended regression; inspect visible behavior where the criterion concerns interaction. Record unavailable checks and mocked boundaries explicitly.

Update included issues with resolution evidence or their remaining scope and blockers. An implemented Agent Note does not resolve an issue or complete a phase. A resolved issue does not replace the phase's own acceptance checks. Keep detailed results in the phase owner and link them from summaries.

Follow [record ownership](../make-codebase-agentic/references/records.md) for completion. Update affected current docs, the owning [Agent Note](../make-codebase-agentic-agent-notes/SKILL.md), useful learned cookbooks, plan and owning roadmap evidence, and the checkpoint. Reflect changed cross-area dependency readiness in linked roadmaps and the index; consuming phases still require their own acceptance evidence. A required simulator, device, migration, or integration check that has not run remains open. Report implemented behavior, checks, remaining gaps, and the next action.
