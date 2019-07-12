INF = 10**9

class RMQ:
    def __init__(self, a):
        self.n = len(a)
        self.size = 2**(self.n - 1).bit_length()
        self.data = [INF] * (2*self.size-1)
        self.initialize()

    # Initialize data
    def initialize(self):
        for i in range(self.n):
            self.data[self.size + i - 1] = a[i]
        for i in range(self.size-2, -1, -1):
            self.data[i] = min(self.data[i*2 + 1], self.data[i*2 + 2])

    # Update ak as x
    def update(self, k, x):
        k += self.size - 1
        self.data[k] = x
        while k > 0:
            k = (k - 1) // 2
            self.data[k] = min(self.data[2*k+1], self.data[2*k+2])

    # Min value in [l, r)
    def query(self, l, r):
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
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = len(a)
    rmq = RMQ(a)
    for i in range(n):
        print(rmq.query(i, n), end=" ")
    print("")
    print("update and try agein")
    for i in range(n):
        rmq.update(i, i*2)
    for i in range(n):
        print(rmq.query(i, n), end=" ")
    print("")
