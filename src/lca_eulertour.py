class RMQ:
    def __init__(self, a):
        self.n = len(a)
        self.e = 10**9
        self.size = 2**(self.n - 1).bit_length()
        self.data = [(self.e, self.e) for _ in range(2*self.size-1)]
        self.initialize(a)

    # Initialize data
    def initialize(self, a):
        for i in range(self.n):
            self.data[self.size + i - 1] = a[i][:]
        for i in range(self.size-2, -1, -1):
            self.data[i] = min(self.data[i*2 + 1], self.data[i*2 + 2])[:]

    # Min value in [l, r)
    def query(self, l, r):
        L = l + self.size; R = r + self.size
        s = (self.e, self.e)
        while L < R:
            if R & 1:
                R -= 1
                s = min(s, self.data[R-1])[:]
            if L & 1:
                s = min(s, self.data[L-1])[:]
                L += 1
            L >>= 1; R >>= 1
        return s

class LowestCommonAncestor:
    def __init__(self, edge, root=0):
        self.edge = edge[:]
        self.path = []
        self.depth = []
        self.index = [0] * n
        self.euler_tour(-1, root, 0)
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

    def euler_tour(self, prev, v, d):
        st = []
        st.append((prev, v, d, True))
        k = 0
        while st:
            prev, v, d, forward = st.pop()
            self.index[v] = k
            self.path.append(v)
            self.depth.append(d)
            k += 1
            if forward:
                if d > 0:
                    st.append((v, prev, d-1, False))
                for nv in self.edge[v]:
                    if prev == nv:
                        continue
                    st.append((v, nv, d+1, True))

if __name__ == "__main__":
    # Verify: https://judge.yosupo.jp/problem/lca
    n, q = map(int, input().split())
    edge = [[] for _ in range(n)]
    for i, p in enumerate([int(item) for item in input().split()]):
        i += 1
        edge[i].append(p)
        edge[p].append(i)
    LCA = LowestCommonAncestor(edge)
    for _ in range(q):
        u, v = map(int, input().split())
        print(LCA.get_lca(u, v))