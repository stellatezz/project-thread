# Feeds, media loading, and uploads

Load for scrolling content, pagination, optimistic social actions, or uploads. Read the server cursor, media, mutation, and authentication contracts before designing client state.

## Pagination and refresh

Own the query/account identity, current generation, items, cursor, and each operation's loading/error state. Scope cursors to the exact query and generation. On refresh or account change, invalidate prior work; a late page or error must not append old items, replace the cursor, or clear a newer loading state. Deduplicate by stable server identity under the product's ordering rules.

Distinguish initial, refresh, and next-page failure so retry targets the right operation. A failed page retains a valid retry cursor; successful exhaustion stops pagination according to the API contract. Specify behavior for empty pages, repeated cursors, deletion, and changed ordering instead of assuming every page adds items. Preserve scroll position and stable cell identity where the interaction requires it.

Test with controlled response ordering: start an old page, refresh, complete the refreshed request, then deliver old success or error. Repeat with cancellation and account/query changes. Assert visible items, cursor, loading, and error state. Drive a corresponding scrolling/refresh journey through the app.

## Media loading and interaction

Use stable content identity when cells are reused or async media arrives. Cancel or deprioritize offscreen work, cap concurrent downloads/decodes, downsample to display needs, and bound memory/disk caches. Eviction must release decoded images/players, not merely remove URL entries. Avoid one persistent player per item in an unbounded feed; define active playback ownership and background behavior.

Measure scrolling and memory with a representative long feed, large media, repeated navigation, warm/cold cache, and network failures. A small fixture does not prove bounded long-session use.

For optimistic actions, define local operation identity, pending/failure presentation, ordering, and server reconciliation. A late failure for an earlier like must not undo a later unlike or a confirmed newer action. Blind rollback to a captured old value can overwrite subsequent user intent.

## Upload durability

Separate selected asset ownership, prepared file, transfer, server processing, and publication. Record durable operation identity, account, source/destination references, known server identifier, meaningful progress/recovery state, and error category as required. Do not persist a progress percentage as if it were enough to resume bytes.

Retain source media until the required success point or authorized cancellation cleanup. Define retries, server-supported idempotency, ambiguous completion reconciliation, cancellation, and relaunch behavior. If resumable transfer is unsupported, preserve enough information to restart safely with an honest message. A request that timed out may already have created the remote item.

Use background transfer APIs only with their actual file/lifetime requirements and target SDK support. Exercise interruption during preparation, transfer, remote acceptance, and response delivery; also test expiry/logout, missing files, low disk space, duplicate completion, and user cancellation. Check no duplicate publication, no false success, and no leaked account data. Device background-transfer verification remains separate from logic and simulator evidence.

Capture a proven add-section or upload procedure in the adopting repository's [cookbooks](../../make-codebase-agentic-documentation/references/cookbooks.md).
