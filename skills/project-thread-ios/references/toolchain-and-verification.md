# Discover tools and record evidence

The adopting app's commands and CI are authoritative. Discover available tooling before promising simulator, device, or archive work. Do not install or upgrade Xcode, change the selected toolchain globally, alter signing, or add dependencies merely to make an assumed command work.

Useful discovery on a Mac includes:

```sh
xcode-select -p
xcodebuild -version
xcrun swift --version
rg --files -g '*.xcworkspace/contents.xcworkspacedata' -g '*.xcodeproj/project.pbxproj' -g '*.xcscheme' -g '*.xctestplan' -g '*.xcconfig' -g 'Package.swift' -g 'Package.resolved'
xcrun simctl list devices available
```

Inspect project settings and scripts for the deployment floor, language mode, isolation settings, configurations, targets, test plans, scheme, and dependencies. For the discovered container, run `xcodebuild -list` and `-showdestinations` with the correct workspace or project and scheme. Do not invent a simulator name or assume a Swift package contains the app target.

The following illustrates command shape only; replace each example value from discovery and prefer the project's wrapper/CI command:

```sh
xcodebuild -workspace App.xcworkspace -scheme App -showdestinations
xcodebuild -workspace App.xcworkspace -scheme App -destination 'platform=iOS Simulator,id=DISCOVERED-UDID' -resultBundlePath /tmp/app-journey.xcresult test
```

Use a fresh artifact path per run. Choose `-project` when that is the actual container. Building or unit-testing a package is useful logic evidence but does not establish that the app compiles, launches, or completes a UI journey. Launch and exercise the app using available simulator/UI tools; if interaction tooling is unavailable, record that gap.

## Evidence tiers

| Evidence | What it establishes |
| --- | --- |
| Compiled | Named target/configuration builds for the stated SDK; no journey claim |
| Logic/integration tested | Named behaviors pass under the recorded harness and mock boundaries |
| Simulator-tested | Specific running-app journeys pass on named simulator/OS/settings |
| Device-tested | Specific journeys or measurements pass on named hardware/OS/configuration |
| Unverified | Code or a planned procedure exists, but required observation has not occurred |

Record code revision/worktree scope, command or journey, toolchain, environment, workload, outcome, and artifact. Track failed attempts separately. Simulator evidence does not establish real camera/GPS, background scheduling, energy, thermal, or hardware-performance behavior.

## Performance

Set product-specific budgets against named supported devices and representative workloads. Measure relevant startup, interaction responsiveness, scrolling, peak/steady memory, disk, energy, and media operations. Use realistic data volume, media dimensions/duration, network conditions, cache states, and release-like configuration. Record baseline and subsequent results; do not invent a target or call an app scalable because an empty feed is smooth.

Use Xcode Instruments, XCTest measurements, and available production diagnostics. Apple's [responsiveness guidance](https://developer.apple.com/documentation/xcode/improving-app-responsiveness) distinguishes lab testing/profiling from observing hangs and hitches in released apps. Keep those evidence sources distinct. Check for work accidentally retained on the main actor under the actual toolchain settings. Prefer physical devices for performance/energy claims and retain traces or result bundles.

## Release preparation when requested

Review bundle identifiers, environments, endpoints, secrets handling, entitlements, privacy declarations required by used APIs/SDKs, signing teams/profiles, build configuration, versioning, and archive/export settings. Use the project's distribution method and current Apple guidance; do not invent credentials or bypass signing to claim a releasable archive.

Build and validate the actual archive where possible. Review diagnostics/crash reporting and release notes, recovery/migration expectations, and remaining device verification. Preparing artifacts does not authorize TestFlight/App Store submission or other publishing.
