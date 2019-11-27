class RMQ:
    def __init__(self, a):
        # Operator
        self.op = lambda a, b : min(a, b)
        # Identity element
        self.e = 10**9 
        self.n = len(a)
        self.size = 2**(self.n - 1).bit_length()
        self.data = [self.e] * (2*self.size-1)
        self.initialize(a)

    # Initialize data
    def initialize(self, a):
        for i in range(self.n):
            self.data[self.size + i - 1] = a[i]
        for i in range(self.size-2, -1, -1):
            self.data[i] = self.op(self.data[i*2 + 1], self.data[i*2 + 2])

    # Update ak as x (0-indexed)
    def update(self, k, x):
        k += self.size - 1
        self.data[k] = x
        while k > 0:
            k = (k - 1) // 2
            self.data[k] = self.op(self.data[2*k+1], self.data[2*k+2])

    # Min value in [l, r) (0-indexed)
    def query(self, l, r):
        L = l + self.size; R = r + self.size
        s = self.e
        while L < R:
            if R & 1:
                R -= 1
                s = self.op(s, self.data[R-1])
            if L & 1:
                s = self.op(s, self.data[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s

if __name__ == "__main__":
    b = [8, 3, 2, 6, 9, 11, 2, 7, 0, 2]
    n = len(b)
    rmq = RMQ(b)
    for i in range(n):
        print(rmq.query(i, n), end=" ")
    print("")
    print("update and try agein")
    for i in range(n):
        rmq.update(i, i*2)
    for i in range(n):
        print(rmq.query(i, n), end=" ")
    print("")
