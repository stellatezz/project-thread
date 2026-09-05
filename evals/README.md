# Behavioral fixtures

These fixtures evaluate skill behavior, not production iOS readiness. They complement metadata/link checks. Use an isolated workspace and supply the task plus raw artifacts to an evaluator without the rubric or previous results. Read only the skill entry points and the references the task calls for. Record outputs, actual actions, evidence, and gaps; do not score keyword matching as correctness.

## Executable feed exercise

Copy [the feed fixture](fixtures/feed/TASK.md), its [context](fixtures/feed/CONTEXT.md), and [Swift state owner](fixtures/feed/FeedStore.swift) into a temporary workspace. Ask an independent agent to complete the task using the installed suite or source skill paths. It should implement a focused fix, add deterministic checks, run available Swift tooling, and leave usable records. No iOS application target is supplied, so a compile/logic result cannot become a simulator or device claim.

Review the resulting observable behavior against [the rubric](rubric.md). Preserve a compact run record and durable evidence in `evals/results/`; do not replace the original faulty input with the answer.

## Scenario exercises

Give an evaluator one request and context at a time from [scenarios.json](scenarios.json). Ask it to use the matching skills and produce the next concrete work decisions, appropriate verification, and repository handoff. These are instruction/decision exercises, not executed app tests. For continuity, introduce a fresh evaluator using only the checkpoint and linked records produced by an earlier exercise.

Use the rubric to identify material failures, revise only guidance supported by those failures, and rerun affected scenarios. Mark scenarios not exercised as pending. A source/reference coverage review alone is not a behavioral pass.

## Documentation and adoption exercises

Copy [the prose fixture](fixtures/prose/TASK.md) or [the instruction fixture](fixtures/instructions/TASK.md), with its sibling artifacts, into a fresh temporary directory. Give the evaluator only that task, its input, and the relevant skill entry point. Keep intended findings and previous outputs separate from the evaluator's inputs.

For prose, review the result against the actual source: parent-directory requirements, serialization limits, replacement behavior, visible errors, caller serialization, and unsupported export or crash guarantees. Check that useful behavior remains available near the API and that the reading path separates orientation from detailed reference. Confirm executable behavior is unchanged.

For adoption, inspect preservation of unique root, subtree, and Claude instructions; current product ownership; a practical context/checkpoint path; and executed CLI verification. A fresh Codex task can establish its explicit reading path, but it cannot establish automatic Claude discovery when that runtime is unavailable. Do not reward extra files or matching headings.

Retain actual outputs, semantic findings, commands, and limitations under a dated result record. Compare the artifacts themselves before marking the exercise complete.
