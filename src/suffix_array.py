class SuffixArray:
    def __init__(self, a):
        self.a = a + [0]
        self.k = max(self.a) + 1
        self.n = len(self.a)
        self.sa = None
        self.sa = self.SA_IS(self.a, self.sa, self.n, self.k)

    # Find the start or end of each bucket
    def get_buckets(self, a, k, end=True):
        bucket = [0] * k
        for item in a:
            bucket[item] += 1
        sumation = 0
        for i in range(k):
            sumation += bucket[i]
            if end:
                bucket[i] = sumation
            else:
                bucket[i] = sumation - bucket[i]
        return bucket

    def induce_SAl(self, a, sa, n, k, is_stype):
        bucket = self.get_buckets(a, k, end=False)
        for i in range(n):
            j = sa[i] - 1
            if j >= 0 and (not is_stype & (1 << j)):
                sa[bucket[a[j]]] = j
                bucket[a[j]] += 1

    def induce_SAs(self, a, sa, n, k, is_stype):
        bucket = self.get_buckets(a, k, end=True)
        for i in range(n-1, -1, -1):
            j = sa[i] - 1
            if j >= 0 and is_stype & (1 << j):
                bucket[a[j]] -= 1
                sa[bucket[a[j]]] = j

    def SA_IS(self, a, sa, n, k):
        # LS-type array in bits
        is_stype = 0
        prev_type = 0
        prev_item = self.k 
        for i, item in enumerate(a[::-1]): 
            shift = n - 1 - i
            if item == prev_item:
                is_stype |= prev_type << shift 
            elif item < prev_item:
                is_stype |= 1 << shift 
            prev_type = item <= prev_item
            prev_item = item
        # Bucket array
        bucket = self.get_buckets(a, k)
        # Find ends of buckets
        sa = [-1] * n
        for i in range(n - 1, 0, -1):
            is_LMS = is_stype & (1 << i) and (not is_stype & (1 << i-1))
            if is_LMS:
                bucket[a[i]] -= 1
                sa[bucket[a[i]]] = i
        self.induce_SAl(a, sa, n, k, is_stype)
        self.induce_SAs(a, sa, n, k, is_stype)

        n1 = 0
        for i in range(n):
            if sa[i] == 0: continue
            is_LMS = is_stype & (1 << sa[i]) and (not is_stype & (1 << sa[i]-1))
            if is_LMS:
                sa[n1] = sa[i]
                n1 += 1
        for i in range(n1, n):
            sa[i] = -1

        name = 1; prev = 0 
        names = [0]
        sa[n1] = 0
        for pos in sa[1: n1]:
            if pos == 0:
                continue
            diff = False
            for d in range(n):
                is_LMS1 = is_stype & (1 << pos+d) and (not is_stype & (1 << pos+d-1))
                is_LMS2 = is_stype & (1 << prev+d) and (not is_stype & (1 << prev+d-1))
                if a[pos + d] != a[prev+d] or (is_stype >> (pos + d) & 1) != (is_stype >> (prev + d) & 1):
                    diff = True
                    break
                elif d > 0 and (is_LMS1 or is_LMS2):
                    break
            if diff:
                name += 1; prev = pos
            pos //= 2
            sa[n1 + pos] = name - 1
            names.append(name - 1)

        j = n - 1
        for i in range(n-1, n1 - 1, -1):
            if sa[i] >= 0:
                sa[j] = sa[i]
                j -= 1
        sa1 = sa[:n1]; a1 = sa[-n1:] 
        if name < n1:
            sa1 = self.SA_IS(a1, sa1, n1, name)
        else:
            for i in range(n1):
                sa1[a1[i]] = i
        bucket = self.get_buckets(a, k, end=True)
        j = 0
        for i in range(n):
            if i <= 0: continue
            is_LMS = is_stype & (1 << i) and (not is_stype & (1 << i-1))
            if is_LMS:
                a1[j] = i
                j += 1
        for i in range(n1):
            sa1[i] = a1[sa1[i]]
        for i in range(n1, n):
            sa[i] = -1
        for i in range(n1 - 1, -1, -1):
            j = sa[i]; sa[i] = -1
            bucket[a[j]] -= 1
            sa[bucket[a[j]]] = j
        self.induce_SAl(a, sa, n, k, is_stype)
        self.induce_SAs(a, sa, n, k, is_stype)
        return sa

if __name__ == "__main__":
    s = "mmiissiissiippii"
    ord_base = ord("a") - 1
    a = [ord(ch) - ord_base for ch in s]
    SA = SuffixArray(a)
    print(SA.sa)