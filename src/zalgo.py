def search(s, t):
    p = t + "$" + s
    zarray = calc_zarray(p)
    ret = []
    for i, item in enumerate(zarray[len(t) + 1:]):
        if item == len(t):
            ret.append(i)
    return ret

def calc_zarray(s):
    zarray = [len(s)] + [0] * (len(s) - 1)
    s_idx = 1; matching = 0
    while s_idx < len(s):
        while s_idx + matching < len(s) and s[matching] == s[s_idx + matching]:
            matching += 1
        zarray[s_idx] = matching
        if matching == 0:
            s_idx += 1
            continue
        # zarray[s_idx:s_idx + matching) corresponds to zarray[0:matching)
        # as long as matching range does not overrun
        k = 1
        while s_idx + k < len(s) and k + zarray[k] < matching:
            zarray[s_idx + k] = zarray[k]
            k += 1
        s_idx += k; matching -= k
    return zarray

def toyproblem():
    s = "aaabbabababaaabaaaab"
    t = "ababa"
    print(s)
    zarray = calc_zarray(s)
    print(zarray)
    print("search: " + t)
    print(search(s, t))

def verify():
    # Verify: https://judge.yosupo.jp/problem/zalgorithm
    s = input().rstrip()
    zarray = calc_zarray(s)
    print(*zarray)

if __name__ == "__main__":
    verify()