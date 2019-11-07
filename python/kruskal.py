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

        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

if __name__ == "__main__":
    # edge_i : [u, v, cost]
    edge = []
    edge.sort(key=lambda x : x[2])

    DJ = DisjointSet(n)
    cost = 0
    for e in edge:
        if not DJ.has_same_root(e[0], e[1]):
            # Add edge if it is smallest and will not create any loop
            DJ.unite(e[0], e[1])
            cost += e[2]
    print(cost)
