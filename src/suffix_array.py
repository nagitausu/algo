class SuffixArray:
    def __init__(self, a):
        self.a = a + [0]
        self.k = max(self.a) + 1
        self.n = len(self.a)
        self.sa = self.SA_IS(self.a, self.n, self.k)

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

    def induce_SAl(self, a, sa, n, k, lstype):
        bucket = self.get_buckets(a, k, end=False)
        for i in range(n):
            j = sa[i] - 1
            if j >= 0 and (not lstype & (1 << j + 1)):
                sa[bucket[a[j]]] = j
                bucket[a[j]] += 1

    def induce_SAs(self, a, sa, n, k, lstype):
        bucket = self.get_buckets(a, k, end=True)
        for i in range(n-1, -1, -1):
            j = sa[i] - 1
            if j >= 0 and lstype & (1 << j + 1):
                bucket[a[j]] -= 1
                sa[bucket[a[j]]] = j
    
    def is_LMS(self, index, lstype):
        return lstype >> (index+1) & 1 and not (lstype >> index & 1)

    def is_stype(self, index, lstype):
        return lstype >> (index+1) & 1

    def SA_IS(self, a, n, k):
        # L-type or S-type
        # LS-type array in bits, 1-indexed, initialized with S-type first
        lstype = 1
        prev_type = 0
        prev_item = self.k
        for i, item in enumerate(a[::-1]): 
            shift = n - i
            if item == prev_item:
                lstype |= prev_type << shift 
            elif item < prev_item:
                lstype |= 1 << shift 
                prev_type = 1
            else:
                prev_type = 0
            prev_item = item
        # Bucket array
        bucket = self.get_buckets(a, k)
        # Find ends of buckets
        sa = [-1] * n
        for i in range(n - 1, 0, -1):
            if self.is_LMS(i, lstype):
                bucket[a[i]] -= 1
                sa[bucket[a[i]]] = i
        self.induce_SAl(a, sa, n, k, lstype)
        self.induce_SAs(a, sa, n, k, lstype)

        lcm_cnt = 0
        for i in range(n):
            if self.is_LMS(sa[i], lstype):
                sa[lcm_cnt] = sa[i]
                lcm_cnt += 1
        for i in range(lcm_cnt, n):
            sa[i] = -1

        # Rename LCM strings
        name = 1; prev = sa[0] 
        sa[lcm_cnt + sa[0] // 2] = 0
        for pos in sa[1: lcm_cnt]:
            diff = False
            for d in range(n):
                if a[pos + d] != a[prev + d] or (self.is_stype(pos + d, lstype) != self.is_stype(prev + d, lstype)):
                    diff = True
                    break
                elif d > 0 and (self.is_LMS(pos + d, lstype) or self.is_LMS(prev + d, lstype)):
                    break
            if diff:
                name += 1; prev = pos
            pos //= 2
            sa[lcm_cnt + pos] = name - 1
        sub_a = []
        for i in range(lcm_cnt, n):
            if sa[i] >= 0:
                sub_a.append(sa[i])
            
        # Recursively sort LMS sub strings
        if name < lcm_cnt:
            sub_sa = self.SA_IS(sub_a, len(sub_a), name + 1)
        else:
            sub_sa = sa[:lcm_cnt]
            for i in range(lcm_cnt):
                sub_sa[sub_a[i]] = i
        bucket = self.get_buckets(a, k, end=True)
        j = 0
        for i in range(1, n):
            if self.is_LMS(i, lstype):
                sub_a[j] = i
                j += 1
        # Earn correctly sorted LCMs
        for i in range(lcm_cnt):
            sa[i] = sub_a[sub_sa[i]]
        for i in range(lcm_cnt, n):
            sa[i] = -1
        for i in range(lcm_cnt - 1, -1, -1):
            j = sa[i]; sa[i] = -1
            bucket[a[j]] -= 1
            sa[bucket[a[j]]] = j

        # Correct induced sorting
        self.induce_SAl(a, sa, n, k, lstype)
        self.induce_SAs(a, sa, n, k, lstype)
        return sa

if __name__ == "__main__":
    s = "honifuwadijkstrababababa"
    ord_base = ord("a") - 1
    a = [ord(ch) - ord_base for ch in s]
    SA = SuffixArray(a)
    print(SA.sa)

    sa_naive = [""]
    for i in range(len(s)):
        sa_naive.append(s[i:])
    sa_naive.sort()
    ok = True
    for i, index in enumerate(SA.sa):
        print(s[index:], sa_naive[i])
        if s[index:] != sa_naive[i]:
            print("wrong!")
            ok = False
    if ok:
        print("\nverified!")