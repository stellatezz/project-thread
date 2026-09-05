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
    private(set) var isLoading = false
    private(set) var error: String?

    init(api: any FeedAPI) { self.api = api }

    func refresh() async {
        isLoading = true
        error = nil
        defer { isLoading = false }
        do {
            let page = try await api.page(cursor: nil)
            items = page.items
            cursor = page.nextCursor
        } catch {
            self.error = String(describing: error)
        }
    }

    func loadNext() async {
        guard !isLoading, let cursor else { return }
        isLoading = true
        error = nil
        defer { isLoading = false }
        do {
            let page = try await api.page(cursor: cursor)
            items += page.items
            self.cursor = page.nextCursor
        } catch {
            self.error = String(describing: error)
        }
    }
}
