class LowLink:
    def __init__(self, adj):
        self.n = len(adj)
        self.adj = adj
        self.used = [0] * n
        self.ord = [0] * n
        self.low = [0] * n
        self.bridge = []
        self.articulation = []

    def dfs_lowlink(self, v, order, prev):
        order += 1
        self.used[v] = 1
        self.ord[v] = order
        self.low[v] = self.ord[v]

        is_articulation = False
        cnt = 0
        for to in self.adj[v]:
            if not self.used[to]:
                cnt += 1
                order = self.dfs_lowlink(to, order, v)
                self.low[v] = min(self.low[v], self.low[to])
                if prev != -1:
                    is_articulation |= self.low[to] >= self.ord[v]
                if(self.ord[v] < self.low[to]):
                    if v < to:
                        self.bridge.append((v, to))
                    else:
                        self.bridge.append((to, v))
            elif to != prev:
                self.low[v] = min(self.low[v], self.low[to])
        if prev == -1:
            is_articulation |= cnt > 1
        if is_articulation:
            self.articulation.append(v)
        return order

    def calc_lowlink(self):
        order = 0
        for i in range(self.n):
            if not self.used[i]:
                order = self.dfs_lowlink(i, order, -1)

    def dfs_decompose(self, v, label, prev):
        if prev != -1 and self.ord[prev] >= self.low[v]:
            self.comp[v] = self.comp[prev]
        else:
            label += 1
            self.comp[v] = label
        for to in self.adj[v]:
            if self.comp[to] == -1:
                label = self.dfs_decompose(to, label, v)
        return label

    def decompose(self):
        self.calc_lowlink()
        self.comp = [-1] * self.n

        label = -1
        for i in range(self.n):
            if self.comp[i] == -1:
                label = self.dfs_decompose(i, label, -1)
        edge = [[] for _ in range(label + 1)]
        for u, v in self.bridge:
            x = self.comp[u]; y = self.comp[v]
            edge[x].append(y)
            edge[y].append(x)
        return edge

if __name__ == "__main__":
    n, m = [int(item) for item in input().split()]
    edge = [[] for _ in range(n)]

    for i in range(m):
        a, b = [int(item) for item in input().split()]
        edge[a].append(b)
        edge[b].append(a)

    LL = LowLink(edge)
    # LL.calc_lowlink()
    new_edge = LL.decompose()
    print(LL.bridge)
    print(LL.articulation)
    print(LL.comp)
    print(new_edge)
