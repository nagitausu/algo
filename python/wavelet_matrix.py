class WaveletMatrix:
    def __init__(self, a):
        self.n = len(a)
        self.data = a[:]
        self.bit_len = max(a).bit_length()
        self.bit_vector = [0] * self.bit_len
        self.sep = [0] * self.bit_len
        self.begin = dict()
        self.build()

    def build(self):
        tmp = self.data[:]
        for j in range(self.bit_len):
            front = []; back = []
            for i, item in enumerate(tmp):
                if item >> (self.bit_len - 1 - j) & 1:
                    back.append(item)
                    self.bit_vector[j] |= 1 << (self.n - 1 - i)
                else:
                    front.append(item)
            self.sep[j] = len(front)
            front.extend(back)
            tmp = front[:]
        for i, item in enumerate(tmp):
            if item in self.begin:
                continue
            self.begin[item] = i


    def rank(self):
        pass

    def select(self):
        pass

    def rank_bit_vector(self, lv, x):
        return bin(self.bit_vector[lv] >> (self.n - x)).count("1")

    def select_bit_vector(self):
        pass

if __name__ == "__main__":
    # See https://takeda25.hatenablog.jp/entry/20130303/1362301095
    a = [11, 0, 15, 6, 5, 2, 7, 12,
         11, 0, 12, 12, 13, 4, 6, 13,
         1, 11, 6, 1, 7, 10, 2, 7,
         14, 11, 1, 7, 5, 4, 14, 6]
    WM = WaveletMatrix(a)
    for item in WM.bit_vector:
        print("{:032b}".format(item))
    print(WM.sep)
    for key in WM.begin.keys():
        print(key, WM.begin[key])
