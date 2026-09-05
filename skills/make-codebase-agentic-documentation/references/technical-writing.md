# Write complete, precise technical prose

Use this reference when authoring or reviewing prose, including Markdown, code comments, API documentation, and agent instructions. Improve clarity while preserving every relevant fact. Read [worked examples](worked-examples.md) when a passage has more than one plausible treatment.

## Preserve the meaning before editing the words

Identify the actor, action, object, conditions, ordering, ownership, side effects, completion point, failures, and exceptions that the passage communicates. Preserve distinctions such as must versus may, requested versus completed, and saved versus queued. If source and prose disagree, inspect the owning implementation and consumers before deciding which claim is correct.

A concise sentence is useful when it says the same thing more clearly. A shorter sentence that drops a recovery condition or guarantee is incomplete. Restore missing explanation when readers would otherwise misuse the API or make an incorrect change. Treat uncertain claims as questions to resolve or explicit limitations; polished prose must not turn an assumption into a fact.

## Name the thing and explain its behavior

Use concrete subjects and verbs: who changes which state, when, and with what result. Prefer the actual component, field, operation, or failure name over vague words such as system, handling, robustness, or appropriate behavior. Keep established technical terms when they name the subject accurately; briefly define unfamiliar project vocabulary near its first relevant use.

Put the main point first, then explain the condition, consequence, or supporting detail. Develop one main idea per paragraph. Use a list for independent requirements or ordered actions, a table for comparisons, and prose for explanation. Headings should describe the content beneath them. Examples should resolve likely confusion, not repeat an obvious assignment or branch.

Preserve searchable identifiers and meaningful emphasis. Ordinary rules do not all need bold text, capitals, or repeated warnings. Use a diagram when relationships or timing become clearer visually, and keep its labels consistent with the owning code and prose.

## Keep explanation at the right location

Current references describe implemented behavior. Plans describe intended behavior. Agent Notes preserve consequential reasoning, alternatives, and evidence under their lifecycle rules. A checkpoint records work state for continuation. Keep these purposes visible when editing; a document's grammatical tense alone does not establish its authority.

Code comments explain non-obvious obligations or rationale that is difficult to infer locally. Remove narration of the sequence of edits, investigation, or obvious control flow. Retain the condition that makes a seemingly simpler implementation wrong. Put a lengthy rationale in its owning note and retain a concise consequence at the point of use.

Statements such as “this is safe” or “the operation is resilient” need the mechanism and limit that justify them. Name the permitted inputs, state assumptions, or failure behavior instead of asserting quality. Avoid marketing claims in technical references and avoid internal implementation details in product UI unless they help a person make a decision.

## Review meaning and presentation separately

First assess factual completeness and correct ownership. Then assess organization, language, and redundancy. A passage can need expansion, relocation, restoration, a smaller edit, or no change. Do not require a deletion quota or rewrite every sentence into the same rhythm.

For wording shown to users or models, inspect the output that actually reaches them. Prompts, diagnostics, and UI strings may change behavior; use relevant behavioral checks when semantics change. For documentation-only edits, validate examples and claims proportionately. Report unresolved facts and unavailable checks explicitly. A style checker or word count can locate candidates, but it cannot decide whether a guarantee survived an edit.
