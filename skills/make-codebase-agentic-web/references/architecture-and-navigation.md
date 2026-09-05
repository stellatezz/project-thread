# Architecture and navigation

Start from the route and its consumers. Identify which component owns transient interaction state, which route owns shareable URL state, which data layer owns remote state, and where durable drafts belong. Keep derived values derived; avoid competing copies in component state, a store, and the URL. Introduce shared capabilities when responsibilities or reuse justify them.

Choose rendering per product need: public content, discoverability, first load, interactivity, authentication, and hosting constraints. In server-rendered applications, distinguish request-scoped data from browser state. Keep user data out of shared server caches unless partitioning and authorization are established. Browser-only APIs need an appropriate client boundary; initial markup and client initialization must agree. Check installed framework documentation before relying on version-specific rendering or caching behavior.

Treat URLs as contracts. Define path and query parsing, invalid or missing values, direct navigation, refresh, back/forward, and not-found behavior. Preserve useful links and browser conventions, including opening links in a new tab. Decide whether a state change replaces or adds history; avoid making every keystroke a history entry. Route transitions need deliberate focus and scroll behavior.

For example, a catalog can keep committed search/filter values in the URL, editable text in a form, and results in its established query layer. Changing filters invalidates pagination for the previous query. Back navigation restores the prior committed query through the same loading path. This does not require a new global store.

For a new application, first deliver one route with meaningful data and a complete interaction. Record navigation, state ownership, rendering, and dependencies in existing architecture and plan owners. A proven procedure for adding a route, its loader, and recovery tests can later become a project cookbook.
