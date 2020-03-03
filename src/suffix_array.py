from disjoint_sparse_table import DisjointSparseTable

class SuffixArray:
    def __init__(self, a):
        self.a = a + [0]
        self.k = max(self.a) + 1
        self.n = len(self.a)
        self.sa = self.SA_IS(self.a, self.n, self.k)
        # Construct LCP disjoint sparse table
        self.rank = [0] * self.n
        for i, item in enumerate(self.sa):
            self.rank[item] = i
        self.lcp = self.build_LCP(self.a, self.sa, self.rank)
        self.lcp_dst = DisjointSparseTable(self.lcp, op=lambda a,b : min(a,b), e=0)

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
            if j >= 0 and not is_stype[j]:
                sa[bucket[a[j]]] = j
                bucket[a[j]] += 1

    def induce_SAs(self, a, sa, n, k, is_stype):
        bucket = self.get_buckets(a, k, end=True)
        for i in range(n-1, -1, -1):
            j = sa[i] - 1
            if j >= 0 and is_stype[j]:
                bucket[a[j]] -= 1
                sa[bucket[a[j]]] = j
    
    def SA_IS(self, a, n, k):
        # LS-type array, initialized with S-type first
        is_stype = [1] * n
        for i in range(n-2, -1, -1):
            if a[i] > a[i + 1] or (a[i] == a[i+1] and not is_stype[i+1]):
                is_stype[i] = 0
        is_lms = [1 if is_stype[i] and not is_stype[i-1] else 0 for i in range(n-1)] + [1]
        # Bucket array
        bucket = self.get_buckets(a, k)
        # Find ends of buckets
        sa = [-1] * n
        for i in range(n - 1, 0, -1):
            if is_lms[i]:
                bucket[a[i]] -= 1
                sa[bucket[a[i]]] = i
        self.induce_SAl(a, sa, n, k, is_stype)
        self.induce_SAs(a, sa, n, k, is_stype)

        lcm_cnt = 0
        for i in range(n):
            if is_lms[sa[i]]:
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
                if a[pos + d] != a[prev + d] or is_stype[pos + d] != is_stype[prev + d]:
                    diff = True
                    break
                elif d > 0 and (is_lms[pos + d] or is_lms[prev + d]):
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
            if is_lms[i]:
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
        self.induce_SAl(a, sa, n, k, is_stype)
        self.induce_SAs(a, sa, n, k, is_stype)
        return sa

    def build_LCP(self, a, sa, rank):
        # Add sentinel
        sa.append(-1)
        lcp = [0] * len(a)
        same_cnt = 0
        for index1 in range(len(a)):
            if same_cnt != 0:
                same_cnt -= 1
            index2 = sa[rank[index1] + 1]
            while a[index1 + same_cnt] == a[index2 + same_cnt]:
                same_cnt += 1
            lcp[rank[index1]] = same_cnt
        # Remove sentinel
        sa.pop()
        return lcp

    def get_lcp(self, l, r):
        return self.lcp_dst.fold(l, r)

    def search(self, b):
        m = len(b)
        l = 0; r = self.n + 1
        matched = 0
        while r - l > 1:
            mid = (l + r) // 2
            lm_lcp = self.get_lcp(l, mid)
            if matched < lm_lcp:
                l = mid
            elif matched > lm_lcp:
                r = mid
            else:
                a_itr = self.sa[mid] + matched; b_itr = matched
                diff = 0
                while b_itr < m and a_itr < self.n:
                    if b[b_itr] != self.a[a_itr]:
                        diff = b[b_itr] - self.a[a_itr]
                        break
                    a_itr += 1; b_itr += 1
                if diff >= 0:
                    l = mid
                    matched = b_itr
                else:
                    r = mid
        return matched, l

def toyproblem():
    s = "honifuwadijkstrabababa"
    ord_base = ord("a") - 1
    a = [ord(ch) - ord_base for ch in s]
    SA = SuffixArray(a)
    print("suffix array          :", SA.sa)
    print("rank                  :", SA.rank)
    print("longest common prefix :", SA.lcp)

    print("check suffix array:")
    sa_naive = [""]
    for i in range(len(s)):
        sa_naive.append(s[i:])
    sa_naive.sort()
    ok = True
    for i, index in enumerate(SA.sa):
        print(i, s[index:], sa_naive[i])
        if s[index:] != sa_naive[i]:
            print("wrong!")
            ok = False
    if ok:
        print("sa verified!")
    
    print("")
    t = "dijkstra"
    print("search:", t)
    b = [ord(ch) - ord_base for ch in t]
    length, sa_index = SA.search(b)
    if length != len(t):
        print("not found...")
    else:
        print("found in sa-index:", sa_index, b, SA.a[SA.sa[sa_index]: SA.sa[sa_index] + len(b)])

def verify():
    # Verify: https://judge.yosupo.jp/problem/suffixarray
    s = input().rstrip()
    ord_base = ord("a") - 1
    a = [ord(ch) - ord_base for ch in s]
    SA = SuffixArray(a)
    print(*SA.sa[1:])

if __name__ == "__main__":
    toyproblem()