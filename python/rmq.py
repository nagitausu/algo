class RMQ:
    def __init__(self, a):
        # Operator
        self.op = lambda a, b : min(a, b)
        # Identity element
        self.e = 10**9

        self.n = len(a)
        self.lv = (self.n - 1).bit_length()
        self.size = 2**self.lv
        self.data = [self.e] * (2*self.size - 1)
        # Bisect checking function 
        self._check = lambda x, acc : acc <= x
        self._acc = self.e

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
    def fold(self, l, r):
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

    def _bisect_forward(self, x, start, k):
        # When segment-k is at the bottom, accumulate and return.
        if k >= self.size - 1:
            self._acc = self.op(self._acc, self.data[k])
            if self._check(x, self._acc):
                return k - (self.size - 1)
            else:
                return -1
        width = 2**(self.lv - (k+1).bit_length() + 1)
        mid = (k+1) * width + width // 2 - self.size 
        # When left-child isn't in range, just look at right-child. 
        if mid <= start:
            return self._bisect_forward(x, start, 2*k + 2)
        # When segment-k is in range and has no answer in it, accumulate and return -1
        tmp_acc = self.op(self._acc, self.data[k])
        if start <= mid - width // 2 and not self._check(x, tmp_acc):
            self._acc = tmp_acc
            return -1
        # Check left-child then right-child
        vl = self._bisect_forward(x, start, 2*k + 1)
        if vl != -1:
            return vl
        return self._bisect_forward(x, start, 2*k + 2)
    
    # Returns min index s.t. start <= index and satisfy check(data[start:idx)) = True
    def bisect_forward(self, x, start=None):
        if start:
            ret = self._bisect_forward(x, start, 0)
        else:
            ret = self._bisect_forward(x, 0, 0)
        self._acc = self.e
        return ret

    def _bisect_backward(self, x, start, k):
        # When segment-k is at the bottom, accumulate and return.
        if k >= self.size - 1:
            self._acc = self.op(self._acc, self.data[k])
            if self._check(x, self._acc):
                return k - (self.size - 1)
            else:
                return -1
        width = 2**(self.lv - (k+1).bit_length() + 1)
        mid = (k+1) * width + width // 2 - self.size 
        # When right-child isn't in range, just look at right-child. 
        if mid >= start:
            return self._bisect_backward(x, start, 2*k + 1)
        # When segment-k is in range and has no answer in it, accumulate and return -1
        tmp_acc = self.op(self._acc, self.data[k])
        if start > mid + width // 2 and not self._check(x, tmp_acc):
            self._acc = tmp_acc
            return -1
        # Check right-child then left-child
        vl = self._bisect_backward(x, start, 2*k + 2)
        if vl != -1:
            return vl
        return self._bisect_backward(x, start, 2*k + 1)
    
    # Returns max index s.t. index < start and satisfy check(data[idx:start)) = True
    def bisect_backward(self, x, start=None):
        if start:
            ret = self._bisect_backward(x, start, 0)
        else:
            ret = self._bisect_backward(x, self.n, 0)
        self._acc = self.e
        return ret

if __name__ == "__main__":
    b = [12, 10, 8, 6, 4, 2, 0, 1, 3, 5, 7, 9, 11]
    n = len(b)
    rmq = RMQ(b)
    print(b)

    print("Fold forward")
    for i in range(1, n+1):
        print(rmq.fold(0, i), end=" ")
    print("")

    print("Bisect forward")
    for i in range(n):
        print("query:", i, "ret:", rmq.bisect_forward(i))

    print("Fold backward")
    for i in range(0, n):
        print(rmq.fold(i, n), end=" ")
    print("")

    print("Bisect backward")
    for i in range(n):
        print("query:", i, "ret:", rmq.bisect_backward(i))