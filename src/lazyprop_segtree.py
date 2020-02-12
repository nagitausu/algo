INF = 10**9

class LazyPropSegmentTree:
    def __init__(self, a):
        self.n = len(a)
        self.level = (self.n - 1).bit_length()
        self.size = 2**self.level
        self.data = [INF] * (2*self.size-1)
        self.lazy = [None] * (2*self.size-1)
        self.initialize(a)

    def __str__(self):
        ret = "### data ###\n"
        start = 0
        for i in range(self.level + 1):
            ret += "lv" + str(i) + ": "
            ret += (" ".join([str(item) for item in self.data[start : start + 2**i]])) + "\n"
            start += 2**i
        ret += "### lazy ###\n"
        start = 0
        for i in range(self.level + 1):
            ret += "lv" + str(i) + ": "
            ret += (" ".join([str(item) for item in self.lazy[start : start + 2**i]])) + "\n"
            start += 2**i
        return ret

    # Initialize data
    def initialize(self, a):
        for i in range(self.n):
            self.data[self.size + i - 1] = a[i]
        for i in range(self.size-2, -1, -1):
            self.data[i] = min(self.data[i*2 + 1], self.data[i*2 + 2])

    def get_index(self, l, r):
        L = (l + self.size) >> 1; R = (r + self.size) >> 1
        if l & 1:
            lc = 0
        else:
            lc = (L & -L).bit_length()
        if r & 1:
            rc = 0
        else:
            rc = (R & -R).bit_length()
        for i in range(self.level):
            if rc <= i:
                yield R
            if L < R and lc <= i:
                yield L
            L >>= 1; R >>= 1

    def propagate(self, *indexes):
        for i in reversed(indexes):
            v = self.lazy[i - 1]
            if v is None:
                continue
            self.lazy[2 * i - 1] = self.data[2 * i - 1] = self.lazy[2 * i] = self.data[2 * i] = v
            self.lazy[i - 1] = None

    def range_update(self, l, r, x):
        *indexes, = self.get_index(l, r)
        self.propagate(*indexes)
        L = l + self.size; R = r + self.size
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R - 1] = self.data[R - 1] = x
            if L & 1:
                self.lazy[L - 1] = self.data[L - 1] = x
                L += 1
            L >>= 1; R >>= 1
        for i in indexes:
            self.data[i - 1] = min(self.data[2*i - 1], self.data[2*i])
    
    # Update ak as x
    def update(self, k, x):
        self.propagate(*self.get_index(k, k+1))
        k += self.size - 1
        self.data[k] = x
        while k > 0:
            k = (k - 1) // 2
            self.data[k] = min(self.data[2*k+1], self.data[2*k+2])

    # Min value in [l, r)
    def query(self, l, r):
        self.propagate(*self.get_index(l, r))
        L = l + self.size; R = r + self.size
        s = INF
        while L < R:
            if R & 1:
                R -= 1
                s = min(s, self.data[R-1])
            if L & 1:
                s = min(s, self.data[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s

if __name__ == "__main__":
    b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = len(b)
    LPST = LazyPropSegmentTree(b)
    for i in range(n):
        print(LPST.query(i, n), end=" ")
    print("")
    print("update and try agein")
    for i in range(n):
        LPST.update(i, i*2)
    for i in range(n):
        print(LPST.query(i, n), end=" ")
    print("")

    LPST.range_update(0, 4, 10)
    LPST.range_update(3, 8, 20)
    # LPST.update(3, 1)
    for i in range(n):
        print(LPST.query(i, n), end=" ")
    for i in range(n):
        print(LPST.query(i, n), end=" ")
    print("")
    print(LPST)