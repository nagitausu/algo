#!/usr/bin/env python3
import sys
input = sys.stdin.readline

class DisjointSparseTable:
    def __init__(self, a):
        # Operator
        self.op = lambda a, b : max(a, b)
        # Identity element
        self.e = 0
        self.n = len(a)
        self.level = (self.n - 1).bit_length()
        self.size = 2**self.level
        self.table = [[self.e] * self.size for _ in range(self.level)]
        # Set bottom first
        for i, item in enumerate(a):
            self.table[-1][i] = item
        self.build()

    def build(self):
        for i in range(1, self.level):
            step = 2**i
            lv = self.level - 1 - i
            for mid in range(step, self.n + step, step*2):
                # Forward
                val = self.e
                for j in range(step):
                    val = self.op(val, self.table[-1][mid + j])
                    self.table[lv][mid + j] = val
                # Backward
                val = self.e
                for j in range(step):
                    val = self.op(self.table[-1][mid - 1 - j], val)
                    self.table[lv][mid - 1 - j] = val

    # Returns f[l:r)
    def fold(self, l, r):
        if l == r:
            return self.e
        elif l == r - 1:
            return self.table[-1][l]
        lv = self.level - (l ^ r-1).bit_length()
        return self.op(self.table[lv][l], self.table[lv][r-1])

class DisjointSparseTable2D:
    def __init__(self, a):
        # Operator
        self.op = lambda a, b : max(a, b)
        # Identity element
        self.e = 0
        self.n = len(a)
        self.n_inner = a[0].n
        self.level = (self.n - 1).bit_length()
        self.level_inner = a[0].level
        self.size = 2**self.level
        self.size_inner = 2**self.level_inner
        self.table = [[[] for _ in range(self.size_inner)] for _ in range(self.level_inner)]
        self.build(a)

    def build(self, a):
        tbl = [[self.e] * self.size for _ in range(self.level)]
        for k in range(1, self.level_inner):
            for l in range(self.size_inner):
                for i in range(self.n):
                    tbl[-1][i] = a[i].table[k][l]
                for i in range(1, self.level):
                    step = 2**i
                    lv = self.level - 1 - i
                    for mid in range(step, self.n + step, step*2):
                        # Forward
                        val = self.e
                        for j in range(step):
                            val = self.op(val, tbl[-1][mid + j])
                            tbl[lv][mid + j] = val
                        # Backward
                        val = self.e
                        for j in range(step):
                            val = self.op(tbl[-1][mid - 1 - j], val)
                            tbl[lv][mid - 1 - j] = val
                self.table[k][l].append(tbl)

    # Returns f[l:r)
    def fold(self, u, d, l, r):
        if u == d:
            return self.e
        elif l == r:
            return self.e
        elif u == d - 1:
            if l == r - 1:
                return self.table[-1][l][-1][u]
            else:
                return self.table[-1][l][-1][u]
        lv_inner = self.level_inner - (l ^ r-1).bit_length()
        lv = self.level - (u ^ d-1).bit_length()
        val = self.e
        self.op(val, self.table[lv_inner][l][lv][u])
        self.op(val, self.table[lv_inner][l][lv][d-1])
        self.op(val, self.table[lv_inner][r-1][lv][u])
        self.op(val, self.table[lv_inner][r-1][lv][d-1])
        return val


a = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 5, 2, 4, 3]]
b = []
for line in a:
    dst = DisjointSparseTable(line)
    b.append(dst)
for line in a:
    print(line)
dst2d = DisjointSparseTable2D(b)
print(dst2d.fold(0,1,0,1))
