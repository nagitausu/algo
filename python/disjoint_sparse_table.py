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
                    val = self.op(self.table[-1][mid + j], val)
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

if __name__ == "__main__":
    a = [1, 4, 3, 8, 5, 0, 7, 2, 9, 11, 2, 4, 5, 10, 11, 12, 11]
    DST = DisjointSparseTable(a)
    for line in DST.table:
        print(line)
    for i in range(4, len(a)):
        print(DST.fold(4, i+1))