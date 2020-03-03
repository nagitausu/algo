class DisjointSet:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * n
        self.rank = [0] * n

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def has_same_root(self, x, y):
        return self.root(x) == self.root(y)

    def get_size(self, x):
        return self.size[self.root(x)]

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x] 
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

def verify():
    # Vefiry: https://judge.yosupo.jp/problem/unionfind
    n, q = map(int, input().split())
    DS = DisjointSet(n)
    for _ in range(q):
        t, u, v = map(int, input().split())
        if t == 0:
            DS.unite(u, v)
        else:
            print(int(DS.has_same_root(u, v)))

if __name__ == "__main__":
    verify()