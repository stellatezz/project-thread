# Location and real-time experiences

Load for live maps, nearby results, tracking, or reconnecting status streams. Read actual API and business contracts first: a moving marker and a confirmed business transition may have different authorities.

## Location is permissioned and uncertain

Give authorization and location subscriptions clear owners. Define not-determined, denied, restricted, changed/revoked authorization, and reduced-accuracy behavior. Request the minimum access needed for the stated feature, at a contextual moment. Reevaluate when returning from Settings and stop work that is no longer permitted. Check the deployment-specific [Core Location authorization guidance](https://developer.apple.com/documentation/corelocation/requesting-authorization-to-use-location-services).

Specify acceptable accuracy, timestamp age, update frequency/distance, and what the UI does when a position is missing, stale, or approximate. Keep measurement timestamp distinct from receive time. Do not use the last cached coordinate as proof of current presence. Avoid retaining precise movement history when the feature needs only current proximity.

Separate location sampling from map rendering: bound update frequency, reconcile stable marker identities, and respect user-controlled viewport/gestures. Define foreground/background demand and stop subscriptions when the owning journey ends. Background access needs a product reason, platform support/configuration, and device evidence; it is not a battery-free continuity mechanism.

## Live state has ordering and reconnect rules

Specify event identity, ordering/revision, authoritative snapshot, reconnect backoff, deduplication, and how a gap is recovered. Reject obsolete updates and discard callbacks from prior sessions/subscriptions. A connected socket alone does not prove state is current. Show reconnecting or stale state appropriately.

For conflicting transitions, identify the authority and legal next states: cancellation versus acceptance, stale availability versus confirmed assignment, or local intent versus remote final state. Do not resolve by arrival order unless the contract explicitly makes it authoritative. Backend ordering/resync support that is absent becomes a dependency.

## Exercise the journey

Test authorization changes while active, stale/low-accuracy samples, rapid updates, foreground/background transitions, termination/relaunch, network loss, reconnect with missing/duplicate/out-of-order events, and a late event after leaving the flow. Assert map and business state separately. Simulated locations verify selected logic/UI paths; actual accuracy, background continuity, battery, and thermal behavior require named-device checks.

Once the project's procedure is proven, capture its local subscription, route, and verification commands in a cookbook using [the cookbook guide](../../project-thread-documentation/references/cookbooks.md).
