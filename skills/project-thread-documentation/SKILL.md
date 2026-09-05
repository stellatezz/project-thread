---
name: project-thread-documentation
description: Maintain authoritative software documentation and project cookbooks as behavior changes. Use for current business and technical references, testing guides, instruction layers, and reusable repository procedures.
---

# Maintain current knowledge

Use [record ownership](../project-thread/references/records.md). Inspect source behavior, configuration, and current consumers before editing a claim. Update the existing owner; link from summaries rather than copying facts into each plan. Edit generator input before generated references.

Write current facts in present tense. Mark proposals and unavailable behavior explicitly. Document non-obvious contracts, defaults, failure semantics, limitations, and the actual verification commands. Code comments should explain constraints or rationale that a reader cannot recover from the implementation alone.

Place repeatable procedures learned during implementation in a project cookbook. Use [the cookbook guide](references/cookbooks.md) when a procedure is worth repeating. Product-specific instructions belong in the adopting repository, while general iOS patterns remain in the iOS skill's references.

Use [Agent Notes](../project-thread-agent-notes/SKILL.md) for rationale and lifecycle; use the plan for future work. Keep `AGENTS.md` focused on relevant local rules and pointers. Do not copy an upstream project's language, tooling, or package conventions without local justification.

Verify links, examples, and commands appropriate to the changed claims. Inspect prose for correctness and ownership; structural checks cannot establish meaning. Leave the [checkpoint](../project-thread/references/checkpoints.md) current when changes affect ongoing work.
