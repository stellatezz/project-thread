# Revamp guidance and migrate the bundle

Status: complete

Plan: [readable repository knowledge](../../plans/readable-agentic-codebase.md). Issue: [guidance and identity](../../issues/readable-repository-guidance.md).

## Delivery

Add six focused references and connect setup, documentation, engineering, review, and the shared record map to their owners. Rename the eleven public skills and bundle metadata. Add useful subtree instructions, a migration guide, and installer support for replacing owned legacy links. Preserve original evaluation artifacts.

## Verification

The structural checker and 16 helper tests pass. These checks include install/repeat, conflicts, rollback, legacy cleanup retry, archive extraction/install, and invalid-bundle controls. All eleven skill validators and plugin validation pass. The [revamp evaluation](../../../../../evals/results/2026-09-05-revamp.md) records two independent prose/adoption tasks, semantic review, retained artifacts, and a successful parent replay of the 13 storage scenarios and README example. Historical v1 artifacts remain unchanged.

All eleven user-level links resolve to the new checkout; no old Project Thread entries remain. Repeated migration preview preserves the new links. The complete 0.2.0 archive is reproducible, validates after extraction, contains twenty-one references, and installs eleven skills in an isolated destination.

The GitHub repository is public under `stellatezz/make-codebase-agentic`, with origin and description updated. Commit `fa8890f` contains the verified revamp and was pushed to `main`. All acceptance criteria are satisfied. Automatic host discovery, Claude runtime behavior, and application/device measurements remain explicit evidence limits rather than claimed passes.
