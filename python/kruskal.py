n = int(input())
xy = [[int(item) for item in input().split()] + [i] for i in range(n)]
xsort = sorted(xy, key=lambda x : x[0])
ysort = sorted(xy, key=lambda x : x[1])

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * (n)
        self.rank = [0] * (n)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

edge = []
for i in range(1, n):
    xdif = abs(xsort[i-1][0] - xsort[i][0])
    ydif = abs(ysort[i-1][1] - ysort[i][1])
    edge.append([xsort[i-1][2], xsort[i][2], xdif])
    edge.append([ysort[i-1][2], ysort[i][2], ydif])
edge.sort(key=lambda x : x[2])

UF = UnionFind(n)
cost = 0
for e in edge:
    if not UF.same_check(e[0], e[1]):
        # Add edge if it is smallest and will not create any loop
        UF.union(e[0], e[1])
        cost += e[2]

print(cost)