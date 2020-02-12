INF = 10**9

class RMQ:
    def __init__(self, a):
        self.n = len(a)
        self.size = 2**(self.n - 1).bit_length()
        self.data = [(INF, INF) for _ in range(2*self.size-1)]
        self.initialize(a)

    # Initialize data
    def initialize(self, a):
        for i in range(self.n):
            self.data[self.size + i - 1] = a[i][:]
        for i in range(self.size-2, -1, -1):
            self.data[i] = min(self.data[i*2 + 1], self.data[i*2 + 2])[:]

    # Update ak as x
    def update(self, k, x):
        k += self.size - 1
        self.data[k] = x
        while k > 0:
            k = (e - 1) // 2
            self.data[k] = min(self.data[2*k+1], self.data[2*k+2])[:]

    # Min value in [l, r)
    def query(self, l, r):
        L = l + self.size; R = r + self.size
        s = (INF, INF)
        while L < R:
            if R & 1:
                R -= 1
                s = min(s, self.data[R-1])[:]
            if L & 1:
                s = min(s, self.data[L-1])[:]
                L += 1
            L >>= 1; R >>= 1
        return s

class LCA:
    def __init__(self, edge, root):
        self.edge = edge[:]
        self.path = []
        self.depth = []
        self.index = [0] * n
        self.euler_tour(-1, root, 0, 0)
        dat = list(zip(self.depth, self.path))
        self.rmq = RMQ(dat)

    # Lowest ancestor of u, v
    def get_lca(self, u, v):
        l, r = self.index[u], self.index[v]
        if l > r:
            l, r = r, l
        return self.rmq.query(l, r+1)[1]

    def get_depth(self, v):
        return self.depth[self.index[v]]

    def euler_tour(self, prev, v, d, k):
        self.index[v] = k
        self.path.append(v)
        self.depth.append(d)
        k += 1
        for item in self.edge[v]:
            if prev == item:
                continue
            k = self.euler_tour(v, item, d + 1, k)
            self.path.append(v)
            self.depth.append(d)
            k += 1
        return k

if __name__ == "__main__":
    n = int(input())
    edge = [[] for _ in range(n)]

    for i in range(n-1):
        u, v, c, w = [int(item) for item in input().split()]
        u -= 1; v -= 1
        edge[u].append(v)
        edge[v].append(u)

    lca = LCA(edge, 3)
    print("i j lca d")
    for i in range(n):
        for j in range(i+1, n):
            v = lca.get_lca(i, j)
            d = lca.get_depth(v)
            print(i, j, v, d)
