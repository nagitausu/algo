class KMP:
    # Search t in s O(n + m)
    @staticmethod
    def search(s, t):
        # Construct prefix-suffix matching table
        tbl = KMP.calc_suffix_prefix_matching(t)

        # Searching t from s with O(n)
        s_idx = 0; t_idx = 0
        while s_idx < len(s) and t_idx < len(t):
            if s[s_idx] == t[t_idx]:
                s_idx += 1; t_idx += 1
            elif t_idx == 0:
                s_idx += 1
            else:
                t_idx = tbl[t_idx]
        return s_idx - t_idx if t_idx == len(t) else -1

    @staticmethod
    def calc_suffix_prefix_matching(t):
        tbl = [-1] + [0] * len(t)
        sp_match = -1
        for t_idx in range(len(t)):
            while sp_match >= 0 and t[t_idx] != t[sp_match]:
                sp_match = tbl[sp_match]
            sp_match += 1
            tbl[t_idx+1] = sp_match
        return tbl

    @staticmethod
    def get_period(t):
        period = [0] * len(t)
        # Construct prefix-suffix matching table
        tbl = KMP.calc_suffix_prefix_matching(t)
        for i, item in enumerate(tbl[1:]):
            period[i] = i - item + 1
        return period


if __name__ == "__main__":
    s = "aabaabaaaabababaababaab"
    t = "babaa"
    print(KMP.calc_suffix_prefix_matching(t))
    print(KMP.get_period(t))
    print(KMP.search(s, t))
