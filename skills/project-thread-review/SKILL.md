---
name: project-thread-review
description: Review a software change against its intended behavior, contracts, lifecycle, and verification evidence. Use for code or phase reviews; report substantiated defects and gaps rather than running a general simplification survey.
---

# Review the result

Establish the actual base, change scope, and working-tree state. Read the plan, applicable instructions, relevant current docs, notes, and surrounding consumers. Assess correctness before style; do not treat a green test suite or implemented note as proof that requirements were met.

Use [engineering](../project-thread-engineering/SKILL.md) to inspect interfaces, state ownership, failure semantics, compatibility, and trust boundaries. For iOS, load [iOS](../project-thread-ios/SKILL.md) and only the relevant specialist references. Trace changed behavior through the actual application entry path.

Check that meaningful transitions have one owner, async results remain valid when applied, cancellation and disposal settle correctly, and data survives failure or migration as required. Evaluate new abstractions against demonstrated consumers and retained complexity. Investigating broad opportunities to remove existing complexity belongs to [simplify](../project-thread-simplify/SKILL.md) when requested or warranted.

Verify that assertions would fail on the intended regression, interaction claims were examined in the running app, and performance claims name a device, workload, and measurement. Distinguish compiled, logic-tested, simulator-tested, device-tested, and unverified behavior. Check docs, note lifecycle, and phase/checkpoint claims using [record ownership](../project-thread/references/records.md).

For each finding, give the defect, tight location, triggering scenario, impact, and evidence. Separate blockers, suggestions, and unavailable verification. If no defects are found, say so with the scope and remaining gaps. Do not publish a review to an external service without authorization.
