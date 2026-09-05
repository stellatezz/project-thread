---
name: make-codebase-agentic-simplify
description: Investigate evidence-backed opportunities to remove or reduce software complexity and record concrete proposals. Use for simplification surveys or a suspected redundant mechanism; it is not a mandatory audit after routine edits.
---

# Investigate simplification

Read business rules, architecture, consumer contracts, relevant implemented and rejected notes, and local testing guidance. Follow [the investigation reference](references/investigation.md). Preserve intentional capabilities and compatibility until evidence and an authorized decision justify changing them.

A useful candidate removes, folds, or demotes real surface area: duplicate state, unused contracts, speculative variation, unnecessary packaging, or custom machinery that a compatible maintained dependency can replace. Complexity alone is not proof; a wrapper that relocates the same obligations may save nothing.

Survey the requested scope, trace consumers and lifecycle responsibilities, then prove or reject candidates. Prefer a few well-supported proposals. Record durable proposals using [Agent Notes](../make-codebase-agentic-agent-notes/SKILL.md), including what would be lost and the strongest reason to retain the existing design. Do not silently implement behavior-changing proposals during an investigation-only request.

If implementation is authorized, use the feature plan and [engineering](../make-codebase-agentic-engineering/SKILL.md), then verify the removal through production entry paths and update affected records. Note consolidation follows the shared lifecycle rules. Report surveyed scope, evidence, proposals, rejected candidates, and actual checks.
