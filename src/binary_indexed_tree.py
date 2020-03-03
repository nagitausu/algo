class BinaryIndexedTree:
    # Initialize BIT with non-zero value
    def __init__(self, array):
        self.len = len(array)
        self.data = [0] + array
        self.build()

    def build(self):
        for i in range(1, self.len):
            if i + (i & -i) > self.len:
                continue
            self.data[i + (i & -i)] += self.data[i]

    # Add w to a[x] (0-indexed)
    def add(self, x, w):
        x += 1
        while x <= self.len:
            self.data[x] += w
            x += x & -x

    # Get Sum of a[0 : x) (0-indexed)
    def sum(self, x):
        ret = 0
        while x > 0:
            ret += self.data[x]
            x -= x & -x
        return ret

    # Get first index s.t. sum a[0 : index) >= w
    def bisect_left(self, w):
        if w <= 0:
            return 0
        x = 0
        delta = pow(2, (self.len - 1).bit_length())
        while delta > 0:
            if x + delta <= self.len and self.data[x + delta] < w:
                w -= self.data[x + delta]
                x += delta
            delta >>= 1
        return x

def toyproblem():
    array = [item + 1 for item in range(16)]
    n = len(array)
    BIT = BinaryIndexedTree(array)
    for i in range(0, n):
        BIT.add(i, i)
    cumsum = []
    for i in range(1, n+1):
        cumsum.append(BIT.sum(i))
    print(cumsum)
    print(BIT.bisect_left(25))

def verify():
    # Verify: https://judge.yosupo.jp/problem/point_add_range_sum
    n, q = map(int, input().split())
    a = [int(item) for item in input().split()]
    BIT = BinaryIndexedTree(a)
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 0:
            BIT.add(a, b)
        else:
            print(BIT.sum(b) - BIT.sum(a))

if __name__ == "__main__":
    toyproblem()