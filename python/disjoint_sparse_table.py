class DisjointSparseTable:
    def __init__(self, a):
        self.level = (len(a) - 1).bit_length()
        self.size = 2**self.level
        self.table = [[0] * self.size for _ in range(self.level)]
        # Set bottom first
        for i, item in enumerate(a):
            self.table[-1][i] = item
        self.build()

    def build(self):
        for lv in range(1, self.level):
            step = 2**lv
            level = self.level - 1 - lv
            for mid in range(step, self.size, step*2):
                # Calc forward
                val = 0
                for i in range(step):
                    val = max(self.table[-1][mid + i], val)
                    self.table[level][mid + i] = val
                # Calc backward
                val = 0
                for i in range(step):
                    val = max(self.table[-1][mid - 1 - i], val)
                    self.table[level][mid - 1 - i] = val

    # Returns f[l:r)
    def query(self, l, r):
        if l == r:
            return 0
        if l == r - 1:
            return self.table[-1][l]
        level = self.level - (l ^ r-1).bit_length()
        return max(self.table[level][l], self.table[level][r-1])

if __name__ == "__main__":
    a = [1, 4, 3, 8, 5, 0, 7, 2, 9, 11, 2]
    DST = DisjointSparseTable(a)
    for line in DST.table:
        print(line)
    for i in range(4, len(a)):
        print(DST.query(4, i+1))
