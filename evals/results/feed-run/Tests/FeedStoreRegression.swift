import Foundation

struct CheckFailure: Error, CustomStringConvertible {
    let description: String
}

enum StubFailure: Error { case offline }

@MainActor
final class ControlledAPI: FeedAPI {
    private(set) var requestedCursors: [String?] = []
    private var pending: [Int: CheckedContinuation<FeedPage, any Error>] = [:]
    private var waiter: (count: Int, continuation: CheckedContinuation<Void, Never>)?

    func page(cursor: String?) async throws -> FeedPage {
        try await withCheckedThrowingContinuation { continuation in
            let index = requestedCursors.count
            requestedCursors.append(cursor)
            pending[index] = continuation
            if let waiter, requestedCursors.count >= waiter.count {
                self.waiter = nil
                waiter.continuation.resume()
            }
        }
    }

    func waitForRequests(_ count: Int) async {
        if requestedCursors.count >= count { return }
        await withCheckedContinuation { continuation in
            precondition(waiter == nil)
            waiter = (count, continuation)
        }
    }

    func succeed(_ index: Int, _ ids: [String], cursor: String?) {
        pending.removeValue(forKey: index)!.resume(returning:
            FeedPage(items: ids.map { FeedItem(id: $0) }, nextCursor: cursor))
    }

    func fail(_ index: Int, _ error: any Error = StubFailure.offline) {
        pending.removeValue(forKey: index)!.resume(throwing: error)
    }
}

struct Snapshot: Equatable, Sendable, CustomStringConvertible {
    let ids: [String]
    let cursor: String?
    let loading: Bool
    let error: String?

    @MainActor init(_ store: FeedStore) {
        ids = store.items.map(\.id)
        cursor = store.cursor
        loading = store.isLoading
        error = store.error
    }

    var description: String {
        "items=\(ids), cursor=\(cursor ?? "nil"), loading=\(loading), error=\(error ?? "nil")"
    }
}

@MainActor
func expect(_ condition: @autoclosure () -> Bool, _ message: String) throws {
    if !condition() { throw CheckFailure(description: message) }
}

@MainActor
func seed(_ api: ControlledAPI, _ store: FeedStore) async {
    let task = Task { await store.refresh() }
    await api.waitForRequests(1)
    api.succeed(0, ["old"], cursor: "old-1")
    await task.value
}

enum Completion: String, CaseIterable {
    case success, failure, cancellation

    @MainActor
    func deliver(_ index: Int, to api: ControlledAPI) {
        switch self {
        case .success: api.succeed(index, ["stale"], cursor: "stale-2")
        case .failure: api.fail(index)
        case .cancellation: api.fail(index, CancellationError())
        }
    }
}

@MainActor
func staleCompletion(oldIsRefresh: Bool, oldFirst: Bool, result: Completion) async throws {
    let api = ControlledAPI()
    let store = FeedStore(api: api)
    await seed(api, store)
    let old = Task {
        if oldIsRefresh { await store.refresh() } else { await store.loadNext() }
    }
    await api.waitForRequests(2)
    let refresh = Task { await store.refresh() }
    await api.waitForRequests(3)
    let before = Snapshot(store)
    let afterFirst: Snapshot
    if oldFirst {
        result.deliver(1, to: api)
        await old.value
        afterFirst = Snapshot(store)
        api.succeed(2, ["fresh"], cursor: "fresh-1")
        await refresh.value
    } else {
        api.succeed(2, ["fresh"], cursor: "fresh-1")
        await refresh.value
        afterFirst = Snapshot(store)
        result.deliver(1, to: api)
        await old.value
    }
    let after = Snapshot(store)
    try expect(before.ids == ["old"] && before.cursor == "old-1" && before.loading,
               "refresh must preserve content while pending: \(before)")
    if oldFirst {
        try expect(afterFirst == before, "stale completion changed newer pending state: \(afterFirst)")
    } else {
        try expect(afterFirst == after, "stale completion changed refreshed state: \(after)")
    }
    try expect(after.ids == ["fresh"] && after.cursor == "fresh-1" && !after.loading && after.error == nil,
               "latest refresh must own all state: \(after)")
}

@MainActor
func staleCleanupDuringFreshPagination() async throws {
    let api = ControlledAPI()
    let store = FeedStore(api: api)
    await seed(api, store)
    let old = Task { await store.loadNext() }
    await api.waitForRequests(2)
    let refresh = Task { await store.refresh() }
    await api.waitForRequests(3)
    api.succeed(2, ["fresh"], cursor: "fresh-1")
    await refresh.value
    let next = Task { await store.loadNext() }
    await api.waitForRequests(4)
    let before = Snapshot(store)
    api.fail(1)
    await old.value
    let afterOld = Snapshot(store)
    api.succeed(3, ["fresh-2"], cursor: nil)
    await next.value
    try expect(afterOld == before && afterOld.loading, "old cleanup interrupted fresh page: \(afterOld)")
    try expect(api.requestedCursors[3] == "fresh-1", "new page used old snapshot cursor")
    try expect(store.items.map(\.id) == ["fresh", "fresh-2"] && store.cursor == nil && store.error == nil,
               "fresh page state incorrect: \(Snapshot(store))")
}

@MainActor
func failedPageRetriesSameCursor() async throws {
    let api = ControlledAPI()
    let store = FeedStore(api: api)
    await seed(api, store)
    let page = Task { await store.loadNext() }
    await api.waitForRequests(2)
    api.fail(1)
    await page.value
    let failed = Snapshot(store)
    let retry = Task { await store.loadNext() }
    await api.waitForRequests(3)
    let retrying = Snapshot(store)
    api.succeed(2, ["next"], cursor: nil)
    await retry.value
    try expect(failed.ids == ["old"] && failed.cursor == "old-1" && !failed.loading && failed.error != nil,
               "page failure lost retry state: \(failed)")
    try expect(api.requestedCursors[1] == "old-1" && api.requestedCursors[2] == "old-1", "retry cursor changed")
    try expect(retrying.loading && retrying.error == nil, "retry did not clear previous error")
    try expect(store.items.map(\.id) == ["old", "next"] && store.cursor == nil && !store.isLoading,
               "retry did not append and exhaust")
}

@MainActor
func failedRefreshPreservesSnapshot() async throws {
    let api = ControlledAPI()
    let store = FeedStore(api: api)
    await seed(api, store)
    let task = Task { await store.refresh() }
    await api.waitForRequests(2)
    api.fail(1)
    await task.value
    let failed = Snapshot(store)
    let retry = Task { await store.refresh() }
    await api.waitForRequests(3)
    api.succeed(2, ["replacement"], cursor: nil)
    await retry.value
    try expect(failed.ids == ["old"] && failed.cursor == "old-1" && failed.error != nil && !failed.loading,
               "failed refresh lost visible snapshot: \(failed)")
    try expect(api.requestedCursors[2] == nil && store.items.map(\.id) == ["replacement"] && store.error == nil,
               "refresh retry used wrong entry path")
}

@MainActor
func failedNewRefreshStillSupersedesOld() async throws {
    let api = ControlledAPI()
    let store = FeedStore(api: api)
    await seed(api, store)
    let old = Task { await store.loadNext() }
    await api.waitForRequests(2)
    let fresh = Task { await store.refresh() }
    await api.waitForRequests(3)
    api.fail(2)
    await fresh.value
    let before = Snapshot(store)
    api.succeed(1, ["stale"], cursor: nil)
    await old.value
    try expect(Snapshot(store) == before && store.items.map(\.id) == ["old"] && store.error != nil,
               "failed refresh allowed superseded page to commit")
}

@MainActor
func duplicatesAndExhaustion() async throws {
    let api = ControlledAPI()
    let store = FeedStore(api: api)
    await store.loadNext()
    try expect(api.requestedCursors.isEmpty, "uninitialized pagination must be a no-op")
    let first = Task { await store.refresh() }
    await api.waitForRequests(1)
    api.succeed(0, ["a", "a", "b"], cursor: "p1")
    await first.value
    let initialIDs = store.items.map(\.id)
    let next = Task { await store.loadNext() }
    await api.waitForRequests(2)
    await store.loadNext()
    let requestCountWhilePending = api.requestedCursors.count
    api.succeed(1, ["b", "c", "c", "a", "d"], cursor: nil)
    await next.value
    await store.loadNext()
    try expect(initialIDs == ["a", "b"], "refresh duplicates were not removed stably")
    try expect(store.items.map(\.id) == ["a", "b", "c", "d"], "overlapping pages changed order or duplicated IDs")
    try expect(requestCountWhilePending == 2 && api.requestedCursors.count == 2, "duplicate or exhausted page requested")
}

@MainActor
func emptyPagesAndRepeatedCursor() async throws {
    let api = ControlledAPI()
    let store = FeedStore(api: api)
    await seed(api, store)
    let page = Task { await store.loadNext() }
    await api.waitForRequests(2)
    api.succeed(1, [], cursor: "old-1")
    await page.value
    let empty = Snapshot(store)
    let next = Task { await store.loadNext() }
    await api.waitForRequests(3)
    api.succeed(2, [], cursor: nil)
    await next.value
    await store.loadNext()
    try expect(empty.ids == ["old"] && empty.cursor == "old-1" && !empty.loading && empty.error == nil,
               "empty page with cursor must remain available for explicit next action")
    try expect(api.requestedCursors.count == 3 && store.items.map(\.id) == ["old"] && store.cursor == nil,
               "empty exhaustion or repeated cursor caused extra requests")
}

@MainActor
func cancellation(refresh: Bool, result: Completion, cancelTask: Bool, urlCancellation: Bool = false) async throws {
    let api = ControlledAPI()
    let store = FeedStore(api: api)
    await seed(api, store)
    let task = Task {
        if refresh { await store.refresh() } else { await store.loadNext() }
    }
    await api.waitForRequests(2)
    if cancelTask { task.cancel() }
    if urlCancellation { api.fail(1, URLError(.cancelled)) }
    else { result.deliver(1, to: api) }
    await task.value
    let after = Snapshot(store)
    try expect(after.ids == ["old"] && after.cursor == "old-1" && !after.loading && after.error == nil,
               "cancellation must retain useful state without alert: \(after)")
    let retry = Task {
        if refresh { await store.refresh() } else { await store.loadNext() }
    }
    await api.waitForRequests(3)
    api.succeed(2, ["retry"], cursor: nil)
    await retry.value
    try expect(api.requestedCursors[2] == (refresh ? nil : "old-1"), "cancellation lost retry entry path")
}

@MainActor
func preCancelledRequests() async throws {
    @MainActor
    final class ImmediateAPI: FeedAPI {
        var calls = 0
        func page(cursor: String?) async throws -> FeedPage {
            calls += 1
            return FeedPage(items: [FeedItem(id: "old")], nextCursor: "old-1")
        }
    }
    let api = ImmediateAPI()
    let store = FeedStore(api: api)
    let refresh = Task { await store.refresh() }
    refresh.cancel()
    await refresh.value
    try expect(api.calls == 0 && store.items.isEmpty && !store.isLoading,
               "pre-cancelled refresh performed a request")
    await store.refresh()
    let before = Snapshot(store)
    let next = Task { await store.loadNext() }
    next.cancel()
    await next.value
    try expect(api.calls == 1 && Snapshot(store) == before,
               "pre-cancelled next page performed a request")
}

@main
struct RegressionRunner {
    @MainActor
    static func main() async {
        var passed = 0
        var failed = 0
        func run(_ name: String, _ body: @MainActor () async throws -> Void) async {
            do {
                try await body()
                passed += 1
                print("PASS \(name)")
            } catch {
                failed += 1
                print("FAIL \(name): \(error)")
            }
        }
        for oldIsRefresh in [false, true] {
            for oldFirst in [false, true] {
                for result in Completion.allCases {
                    await run("stale \(oldIsRefresh ? "refresh" : "page") \(result.rawValue), old finishes \(oldFirst ? "first" : "last")") {
                        try await staleCompletion(oldIsRefresh: oldIsRefresh, oldFirst: oldFirst, result: result)
                    }
                }
            }
        }
        await run("stale cleanup during fresh pagination", staleCleanupDuringFreshPagination)
        await run("page failure retries same cursor", failedPageRetriesSameCursor)
        await run("refresh failure preserves snapshot and retries", failedRefreshPreservesSnapshot)
        await run("failed new refresh still supersedes old page", failedNewRefreshStillSupersedesOld)
        await run("stable deduplication, duplicate requests and exhaustion", duplicatesAndExhaustion)
        await run("empty pages and repeated cursors", emptyPagesAndRepeatedCursor)
        for refresh in [false, true] {
            for result in Completion.allCases {
                await run("cancel \(refresh ? "refresh" : "page") then late \(result.rawValue)") {
                    try await cancellation(refresh: refresh, result: result, cancelTask: true)
                }
            }
            await run("\(refresh ? "refresh" : "page") throws cancellation without caller flag") {
                try await cancellation(refresh: refresh, result: .cancellation, cancelTask: false)
            }
            await run("\(refresh ? "refresh" : "page") reports URL cancellation") {
                try await cancellation(refresh: refresh, result: .cancellation, cancelTask: false, urlCancellation: true)
            }
        }
        await run("pre-cancelled actions do not begin work", preCancelledRequests)
        print("RESULT: \(passed) passed, \(failed) failed")
        if failed > 0 { exit(1) }
    }
}
