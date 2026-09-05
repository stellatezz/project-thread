# Structure documentation around its use

Use this reference to organize documentation, place new detail, or review a document that has become difficult to navigate. [Record ownership](../../make-codebase-agentic/references/records.md) defines the record types and default locations. This reference explains how to shape their content; it does not require adopting those paths.

## Give each document a clear subject

Identify who uses the document, what they need to understand or do, and what the document owns. Begin with its purpose and relevant prerequisites. Choose headings that name reader questions, operations, or mechanisms. Use names from the code so both readers and search tools can find the same subject.

A parent document explains its own subject and how its immediate children fit together. Describe each child by responsibility and relationship, then link to the owner for implementation detail. An architecture page may explain how editing, storage, and export cooperate; storage migration details belong with storage. A child document can be extensive when that detail is necessary to use or maintain its subject.

Before moving text, inspect its incoming links and the surrounding explanation. Move the content and repair references in the same change, including fragment links and references in code comments. Keep a redirect or navigation stub when an established external entry path needs it. Do not reorganize a working tree solely to match a preferred template.

## Separate learning from lookup

A tutorial guides a reader from a stated starting point to an observable result. Introduce prerequisites before the operations that depend on them. Show enough commands, inputs, and expected behavior to reproduce the result. Put optional advanced material after the first working outcome or in a linked guide.

A reference supports lookup without sequential reading. Organize by responsibility, operation, configuration, or failure category. Explain defaults, relationships, limitations, and behavior where readers need them. Tables work for parallel fields or options; connected prose explains causality and tradeoffs.

A cookbook is a repository procedure with known prerequisites and verification. Use the [cookbook guidance](cookbooks.md) for its required substance. A small reference section can accompany a tutorial, but a long API catalog should have its own owner. Agent Notes follow their [decision lifecycle](../../make-codebase-agentic-agent-notes/references/lifecycle.md); do not force them into a tutorial. Incident reports preserve the chronology needed to establish cause and prevention.

## Control duplication without removing useful context

Keep architecture explanations, algorithms, and decision rationale at their owners. Other documents summarize their relevance and link there. A local API description still needs the behavior required for correct use; a link alone may hide a cancellation guarantee, mutation, or failure that the caller must know.

Generate exhaustive catalogs when existing tooling can derive them reliably from source. Edit the generator input before its output. A generated summary must make sense in the location where it appears, even when the full source paragraph contains more context. Keep current reference prose separate from execution status, which belongs in plans, phases, and checkpoints.

## Review depth and navigation

When a document feels long, identify the cause: several subjects mixed together, repeated facts, premature detail, or necessary explanation. Relocate misplaced material first and remove repetition next. Preserve useful depth. Use a contents list for a long reference when headings alone do not make navigation easy; no universal word limit or compression target applies.

Verify one realistic reading path: a new maintainer starts from the repository entry point, finds the relevant component, understands the rule that affects the task, and locates its verification command. Missing or contradictory ownership is a defect even when every link resolves. File and link checks establish structure; an actual reading or task exercise establishes whether that structure is useful.
