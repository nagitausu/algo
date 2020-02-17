class DisjointSparseTable:
    def __init__(self, a, op, e):
        # Operator
        self.op = op
        # Identity element
        self.e = e 
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

class DisjointSparseTable2D:
    def __init__(self, mat):
        # Operator
        self.op = lambda a, b : max(a, b)
        # Identity element
        self.e = 0
        self.n_col = len(mat)
        self.n_row = len(mat[0])
        self.level_col = (self.n_col - 1).bit_length()
        self.level_row = (self.n_row - 1).bit_length()
        self.size_col = 2**self.level_col
        self.size_row = 2**self.level_row
        self.table = [[[] for _ in range(self.size_row)] for _ in range(self.level_row)]
        self.build(mat)

    # Takes O(nmlognlogm)
    def build(self, mat):
        dsts = []
        for line in mat:
            item = DisjointSparseTable(line, self.op, self.e)
            dsts.append(item)
        for lv_row in range(self.level_row):
            for row in range(self.size_row):
                tbl = [[self.e] * self.size_col for _ in range(self.level_col)]
                for i in range(self.n_col):
                    tbl[-1][i] = dsts[i].table[lv_row][row]
                for i in range(1, self.level_col):
                    step = 2**i
                    lv_col = self.level_col - 1 - i
                    for mid in range(step, self.n_col + step, step*2):
                        # Forward
                        val = self.e
                        for j in range(step):
                            val = self.op(val, tbl[-1][mid + j])
                            tbl[lv_col][mid + j] = val
                        # Backward
                        val = self.e
                        for j in range(step):
                            val = self.op(tbl[-1][mid - 1 - j], val)
                            tbl[lv_col][mid - 1 - j] = val
                self.table[lv_row][row] = tbl

    # Returns f([u:d), [l:r))
    def fold(self, u, d, l, r):
        lv_col = self.level_col - (u ^ d-1).bit_length()
        lv_row = self.level_row - (l ^ r-1).bit_length()
        # width = 0 or height = 0
        if u == d or l == r:
            return self.e
        # width = 1 and height = 1
        elif u == d - 1 and l == r - 1:
            return self.table[-1][l][-1][u]
        # width = 1 xor height = 1
        elif l == r - 1:
            return self.op(self.table[-1][l][lv_col][u], self.table[-1][l][lv_col][d - 1])
        elif u == d - 1:
            return self.op(self.table[lv_row][l][-1][u], self.table[lv_row][r-1][-1][u])
        # width > 1 nand height > 1
        up = self.op(self.table[lv_row][l][lv_col][u], self.table[lv_row][r-1][lv_col][u])
        down = self.op(self.table[lv_row][l][lv_col][d-1], self.table[lv_row][r-1][lv_col][d-1])
        return self.op(up, down)

if __name__ == "__main__":
    a = [[1, 2, 3, 4], 
         [5, 4, 3, 2], 
         [1, 5, 2, 4],
         [0, 2, 9, 8]]
    DST2D = DisjointSparseTable2D(a)
    print(DST2D.fold(2,4,3,4))