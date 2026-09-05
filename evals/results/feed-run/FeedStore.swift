// Extracted state owner from a UIKit app. The controller awaits these public actions.
import Foundation

struct FeedItem: Equatable, Sendable {
    let id: String
}

struct FeedPage: Sendable {
    let items: [FeedItem]
    let nextCursor: String?
}

@MainActor
protocol FeedAPI {
    func page(cursor: String?) async throws -> FeedPage
}

@MainActor
final class FeedStore {
    private let api: any FeedAPI
    private(set) var items: [FeedItem] = []
    private(set) var cursor: String?
    private var activeRequestID: UUID?
    var isLoading: Bool { activeRequestID != nil }
    private(set) var error: String?

    init(api: any FeedAPI) { self.api = api }

    func refresh() async {
        guard !Task.isCancelled else { return }
        let requestID = UUID()
        activeRequestID = requestID
        error = nil
        defer { finish(requestID) }
        do {
            let page = try await api.page(cursor: nil)
            guard activeRequestID == requestID, !Task.isCancelled else { return }
            items = uniqueItems(page.items)
            cursor = page.nextCursor
        } catch {
            record(error, for: requestID)
        }
    }

    func loadNext() async {
        guard !Task.isCancelled, !isLoading, let cursor else { return }
        let requestID = UUID()
        activeRequestID = requestID
        error = nil
        defer { finish(requestID) }
        do {
            let page = try await api.page(cursor: cursor)
            guard activeRequestID == requestID, !Task.isCancelled else { return }
            items = uniqueItems(items + page.items)
            self.cursor = page.nextCursor
        } catch {
            record(error, for: requestID)
        }
    }

    private func finish(_ requestID: UUID) {
        // A superseded request cannot finish the current owner's loading state.
        guard activeRequestID == requestID else { return }
        activeRequestID = nil
    }

    private func record(_ error: any Error, for requestID: UUID) {
        guard activeRequestID == requestID, !Task.isCancelled,
              !(error is CancellationError),
              (error as? URLError)?.code != .cancelled else { return }
        self.error = String(describing: error)
    }

    private func uniqueItems(_ candidates: [FeedItem]) -> [FeedItem] {
        var seen = Set<String>()
        return candidates.filter { seen.insert($0.id).inserted }
    }
}
