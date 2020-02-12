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
                if item >> (self.bit_len - 1 - lv) & 1:
                    back.append(item)
                    self.bit_vector[lv] |= 1 << (self.n - 1 - i)
                    self.select_tbl[lv][1].append(i)
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

    # Retruns num of x in [0:k)
    def rank(self, x, k=None):
        if k == None:
            return self.rank(x, self.n)
        for lv in range(self.bit_len):
            key_bit = x >> (self.bit_len - 1 - lv) & 1
            k = self.rank_bit_vector(lv, key_bit, k)
            if key_bit:
                k += self.sep[lv]
        return k - self.num_lr[x][0]
    
    # Retruns num of x in [l:r)
    def count(self, x, l, r):
        return self.rank(x, r) - self.rank(x, l)

    # Retruns num of x s.t. d <= x < u in [l:r)
    def freq(self, d, u, l, r, get_list=False):
        queue = []
        queue.append((0, 0, l, r))
        ret = 0
        if get_list:
            ret_list = []
        while queue:
            lv, d_val, l, r = queue.pop()
            if l == r: 
                continue
            if lv == self.bit_len:
                if d <= d_val < u:
                    ret += r - l
                    ret_list.append((d_val, r - l))
                continue
            u_val = d_val | 1 << (self.bit_len - 1 - lv)
            lim = u_val + 1 << (self.bit_len - 1 - lv)
            if lim <= d or d_val >= u: 
                continue
            if not get_list and d <= d_val and lim <= u:
                ret += r - l
                continue
            l_rank = self.rank_bit_vector(lv, 1, l)
            r_rank = self.rank_bit_vector(lv, 1, r)
            queue.append((lv + 1, d_val, l - l_rank, r - r_rank))
            queue.append((lv + 1, u_val, self.sep[lv] + l_rank, self.sep[lv] + r_rank))
        if get_list:
            return ret_list
        else:
            return ret

    # Returns index of k-th x (0-indexed)
    def select(self, x, k):
        if x not in self.num_lr or k >= self.num_lr[x][1] - self.num_lr[x][0]:
            return None
        k += self.num_lr[x][0]
        for lv in range(self.bit_len-1, -1, -1):
            key_bit = x >> (self.bit_len - 1 - lv) & 1
            if key_bit:
                k -= self.sep[lv]
            k = self.select_bit_vector(lv, key_bit, k)
        return k

    def rank_bit_vector(self, lv, key_bit, k):
        return bin(self.bit_vector[lv] >> (self.n - k)).count(str(key_bit))

    def count_bit_vector(self, lv, key_bit, l, r):
        return self.rank_bit_vector(lv, key_bit, r) - self.rank_bit_vector(lv, key_bit, l)

    # Returns index of k-th bit (0-indexed)
    def select_bit_vector(self, lv, key_bit, k):
        # Since succinct-bit-vector.select() is hard to implement,
        # so I use select-table:O(nlogm) here.
        if k >= len(self.select_tbl[lv][key_bit]):
            return None
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
    print("count(11, 1, 9):", WM.count(11, 1, 9))
    print("freq(0, 11, 1, 9):", WM.freq(0, 11, 1, 9))
    print("freq(0, 11, 1, 9, get_list=True):", WM.freq(0, 11, 1, 9, True))