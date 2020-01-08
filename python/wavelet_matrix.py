class WaveletMatrix:
    def __init__(self, a):
        self.n = len(a)
        self.data = a[:]
        self.bit_len = max(a).bit_length()
        self.bit_vector = [0] * self.bit_len
        self.sep = [0] * self.bit_len
        self.num_lr = dict()
        self.select_tbl = [[[], []] for _ in range(self.bit_len)]
        self.build()

    def build(self):
        tmp = self.data[:]
        for lv in range(self.bit_len):
            front = []; back = []
            for i, item in enumerate(tmp):
                # bit[i] is 1
                if item >> (self.bit_len - 1 - lv) & 1:
                    back.append(item)
                    self.bit_vector[lv] |= 1 << (self.n - 1 - i)
                    self.select_tbl[lv][1].append(i)
                # bit[i] is 0
                else:
                    front.append(item)
                    self.select_tbl[lv][0].append(i)
            self.sep[lv] = len(front)
            tmp = front + back
        for i, item in enumerate(tmp):
            if item not in self.num_lr:
                self.num_lr[item] = [i, i+1]
            else:
                self.num_lr[item][1] += 1

    def rank(self, x, k=None):
        if not k:
            return self.rank(x, self.n)
        for lv in range(self.bit_len):
            key_bit = x >> (self.bit_len - 1 - lv) & 1
            k = self.rank_bit_vector(lv, key_bit, k)
            if key_bit:
                k += self.sep[lv]
        return k - self.num_lr[x][0]

    # Returns index of k-th x (0-indexed)
    def select(self, x, k):
        if x not in self.num_lr or k >= self.num_lr[x][1] - self.num_lr[x][0]:
            return False
        k += self.num_lr[x][0]
        for lv in range(self.bit_len-1, -1, -1):
            key_bit = x >> (self.bit_len - 1 - lv) & 1
            if key_bit:
                k -= self.sep[lv]
            k = self.select_bit_vector(lv, key_bit, k)
        return k

    def rank_bit_vector(self, lv, key_bit, k):
        return bin(self.bit_vector[lv] >> (self.n - k)).count(str(key_bit))

    # Returns index of k-th bit (0-indexed)
    def select_bit_vector(self, lv, key_bit, k):
        # Since select() of succinct bit vector is hard to implement,
        # here we use select()-table O(nlogm)
        if k >= len(self.select_tbl[lv][key_bit]):
            return False
        return self.select_tbl[lv][key_bit][k]

if __name__ == "__main__":
    # See https://takeda25.hatenablog.jp/entry/20130303/1362301095
    a = [11, 0, 15, 6, 5, 2, 7, 12,
         11, 0, 12, 12, 13, 4, 6, 13,
         1, 11, 6, 1, 7, 10, 2, 7,
         14, 11, 1, 7, 5, 4, 14, 6]
    WM = WaveletMatrix(a)
    print("wavelet matrix:")
    for item in WM.bit_vector:
        print("{:032b}".format(item))
    print("rank(11, n):", WM.rank(11))
    ret = []
    for i in range(5):
        ret.append(WM.select(11, i))
    print("select(11, 0) ~ (11, 4):", ret)
