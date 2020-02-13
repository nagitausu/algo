import heapq
INF = 10**9

class Dijkstra:
    def __init__(self, adj):
        self.adj = adj
        self.dist = [INF] * len(adj)
        self.q = []

    def calc(self, start):
        self.dist[start] = 0
        heapq.heappush(self.q, (0, start))
        while len(self.q) != 0:
            prov_cost, src = heapq.heappop(self.q)
            if self.dist[src] < prov_cost:
                continue
            for dest, cost in self.adj[src]:
                if self.dist[dest] > self.dist[src] + cost:
                    self.dist[dest] = self.dist[src] + cost
                    heapq.heappush(self.q, (self.dist[dest], dest))
        return self.dist

if __name__ == "__main__":
    adj = [[(1, 2), (2, 8)], [(0, 2), (2, 5)], [(0, 8), (1, 5)]]
    dijk = Dijkstra(adj)
    print(dijk.calc(1))
