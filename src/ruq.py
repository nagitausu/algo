INF = 10**9
n = 8
size = 2**(n - 1).bit_length()
data = [None] * (2*size-1)

# Overwrite v in range [l, r+1)
def update(l, r, v):
    update.cnt += 1
    L = l + size; R = r + size
    while L < R:
        if R & 1:
            R -= 1
            data[R-1] = [update.cnt, v]
        if L & 1:
            data[L-1] = [update.cnt, v]
            L += 1
        L >>= 1; R >>= 1
update.cnt = 0

# Get latest ak
def query(k):
    k += size - 1
    s = [0, INF]
    while k >= 0:
        if data[k]:
            s = max(s, data[k])
        k = (k - 1) // 2
    return s[1]

update(0, 2, 5)
update(3, 5, 2)
update(0, 1, 1)
update(5, 8, 11)
for i in range(n):
    print(query(i))
print(data)
