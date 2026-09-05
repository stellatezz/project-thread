# Choose evidence from the risk

Map each acceptance criterion to an observable outcome, the entry path that produces it, and the evidence needed to believe it. Use existing project commands and test conventions. Do not impose a universal coverage percentage, performance threshold, or test framework.

| Risk | Useful evidence |
| --- | --- |
| Business transition or transformation | Focused examples and boundary cases with observable state/output assertions |
| Changed interface or persistence contract | Integration across both sides, representative old data, failure injection |
| Async result applied to changed state | Controlled completions in both orders, cancellation, and late error/success assertions |
| User journey or interaction | Exercise the shipped route, check recovery and visible behavior; screenshots supplement behavior |
| Performance/resource cost | Named environment and representative workload, baseline, measurement, repeatability, artifacts |
| External system dependency | Contract/integration evidence with mock boundaries and unavailable services identified |

For a defect, reproduce it first when practical. Use a negative control or run the new regression test against the old behavior when it materially strengthens confidence. Assert the actual user-visible output, persisted state, request effects, or teardown outcome. An assertion that merely counts calls to the new helper can miss the defect.

Separate compilation, logic tests, integration tests, running-app journeys, and measurements in the evidence record. Include code revision or meaningful worktree state, command, environment, result, and artifact location. A test that did not run is unverified; a failed launch is not a tested journey.

When a required tool or environment is absent, finish independent work and leave the phase's outstanding criteria open. Record the exact next verification action. Complete the phase only under [the shared rules](../../project-thread/references/records.md), with affected docs, notes, and checkpoint current.
