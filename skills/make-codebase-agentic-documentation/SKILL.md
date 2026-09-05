---
name: make-codebase-agentic-documentation
description: Write and maintain software documentation that people and coding agents can navigate and rely on. Use for documentation structure, technical prose, code comments, instruction layers, and project cookbooks.
---

# Maintain current knowledge

Use [record ownership](../make-codebase-agentic/references/records.md). Inspect source behavior, configuration, and current consumers before editing a claim. Update the existing owner; link from summaries rather than copying facts into each plan. Edit generator input before generated references.

Establish the requested scope and intended reader. For an audit, report findings; for an authorized edit, improve the relevant owners. A local correction does not require a repository-wide survey. Preserve existing user work, generated-source ownership, and frozen history.

## Choose the needed guidance

| Task | Reference |
| --- | --- |
| Organize documentation or decide where detail belongs | [Document structure](references/document-structure.md) |
| Write, review, shorten, or restore technical prose | [Technical writing](references/technical-writing.md) |
| Document a module, API, configuration, test, or diagnostic | [Codebase documentation](references/codebase-documentation.md) |
| Add or revise root/local agent instructions | [Instruction hierarchy](references/instruction-hierarchy.md) |
| Resolve a writing tradeoff using concrete examples | [Worked examples](references/worked-examples.md) |

Read only what the task needs. Keep enough detail for correct use and maintenance. Preserve conditions, ordering, ownership, failure behavior, and limitations when restructuring or shortening a passage. Current facts use present tense; proposals and unavailable behavior remain explicit. A useful local explanation can link to deeper rationale while retaining the behavior its reader needs.

Place repeatable procedures learned during implementation in a project cookbook. Use [the cookbook guide](references/cookbooks.md) when a procedure is worth repeating. Product-specific instructions belong in the adopting repository, while general iOS patterns remain in the iOS skill's references.

Use [Agent Notes](../make-codebase-agentic-agent-notes/SKILL.md) for rationale and lifecycle; use the plan for future work. Keep `AGENTS.md` focused on relevant local rules and pointers. Do not copy an upstream project's language, tooling, or package conventions without local justification.

Verify the changed claims against source, consumers, examples, and commands. Check incoming links when moving documents and confirm that both a person and a fresh agent can navigate to the relevant owner. Structural checks cannot establish meaning or guarantee that an agent loaded an instruction. Report semantic findings and executed checks separately. Leave the [checkpoint](../make-codebase-agentic/references/checkpoints.md) current when changes affect ongoing work.
