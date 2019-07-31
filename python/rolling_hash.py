class RollingHash():
    def __init__(self, s):
        self.length = len(s)
        self.base1 = 1009
        self.base2 = 1007
        self.mod1 = 10**9 + 7
        self.mod2 = 10**9 + 9
        self.hash1 = [0] * (self.length + 1)
        self.hash2 = [0] * (self.length + 1)
        self.pow1 = [1] * (self.length + 1)
        self.pow2 = [1] * (self.length + 1)

        for i in range(self.length):
            self.hash1[i+1] = (self.hash1[i] + ord(s[i])) * self.base1 % self.mod1
            self.hash2[i+1] = (self.hash2[i] + ord(s[i])) * self.base2 % self.mod2
            self.pow1[i+1] = self.pow1[i] * self.base1 % self.mod1
            self.pow2[i+1] = self.pow2[i] * self.base2 % self.mod2
        
    def get(self, l, r):
        t1 = self.hash1[r] - self.hash1[l] * self.pow1[r-l] % self.mod1
        t1 = (t1 + self.mod1) % self.mod1
        t2 = self.hash2[r] - self.hash2[l] * self.pow2[r-l] % self.mod2
        t2 = (t2 + self.mod2) % self.mod2
        return (t1, t2)


if __name__ == "__main__":
    a = "homuhomu"
    RH = RollingHash(a)
    print(RH.get(0,4))

    a = "poehomu"
    RH = RollingHash(a)
    print(RH.get(3,7))
