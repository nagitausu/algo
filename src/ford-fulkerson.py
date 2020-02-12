INF = 10**9

class FordFulkerson:
    def __init__(self, edge):
        self.n = len(edge)
        self.g = edge

    def dfs(self, v, t, f):
        if v == t:
            return f
        used = self.used
        used[v] = 1
        for e in self.g[v]:
            w, cap, rev = e
            if cap and not used[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        f = INF
        while f:
            self.used = [0] * self.n
            f = self.dfs(s, t, INF)
            flow += f
        return flow

if __name__ == "__main__":
    n, g, e = [int(item) for item in input().split()]
    p = [int(item) for item in input().split()]
    ab = [[int(item) for item in input().split()] for _ in range(e)]

    edge = [[] for _ in range(n+1)]
    for a, b in ab:
        e1 = [b, 1, None]
        e1[2] = e2 = [a, 1, e1]
        edge[a].append(e1)
        edge[b].append(e2)
    for item in p:
        e1 = [n, 1, None]
        e1[2] = e2 = [item, 1, e1]
        edge[item].append(e1)
        edge[n].append(e2)

    ff = FordFulkerson(edge)
    print(ff.flow(0, n))
