# Verification and performance

Discover the package manager from project configuration and lockfiles, then inspect the actual build, typecheck, lint, test, and preview scripts. Use the existing runtime and test stack. Do not assume a package command or install a second toolchain because another project used it. Resolve framework and browser API details against the installed versions and current official documentation.

Select tests from the failure risk. Unit tests can exercise parsing or state transitions; integration tests can control response order, errors, and session changes; browser journeys establish that real routes, DOM, navigation, and input work together. Assertions must detect the intended regression. A DOM mock or passing build does not establish browser behavior.

Run the app through its real entry URL using the available browser automation or manual tools. Exercise direct navigation and refresh, back/forward, critical forms, repeated actions, and relevant error/recovery paths. Check console and network failures. Use representative browsers and mobile layouts from the support matrix; browser emulation is distinct from a physical device. Record exact commands, environment, routes, outcomes, and remaining gaps. If browser tooling is unavailable, complete independent checks and leave browser acceptance explicitly unverified.

Set performance budgets from named environments and representative workloads. Investigate initial loading, interaction latency, layout stability, bundle and media transfer, long lists, retained memory, and relevant editing or upload work. Compare like-for-like runs and preserve enough setup to reproduce a measurement. Avoid arbitrary score, coverage, or bundle-size requirements.

Lab measurements help diagnose regressions under controlled conditions; field measurements describe actual users and require suitable production instrumentation. Do not claim a Lighthouse result proves production performance. [Web.dev's field measurement guidance](https://web.dev/articles/vitals-field-measurement-best-practices) explains the need for field evidence. Distinguish initial loads from client-side route changes and record what the chosen measurement tool covers.

Before a requested release, verify the production build and relevant routing, asset paths, environment exposure, cache behavior, and diagnostics against the hosting configuration. Preparation does not itself authorize publishing. Record mocked integrations and unavailable backend/device/field checks; do not mark their acceptance criteria satisfied.
