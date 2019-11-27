n = 16 
bit = [0] * (n + 1) 

# Initialize BIT with non-zero value
def bit_init():
    for i in range(1, n):
        if i + (i & -i) > n:
            continue
        bit[i + (i & -i)] += bit[i]

# Add w to a[x] (0-indexed) 
def bit_add(x, w):
    x += 1
    while x <= n:
        bit[x] += w
        x += x & -x

# Get Sum of a[0 : x) (0-indexed) 
def bit_sum(x):
    ret = 0
    while x > 0:
        ret += bit[x]
        x -= x & -x
    return ret

bit_init()
print(bit[1:])
for i in range(0, n):
    bit_add(i, 1)
print(bit[1:])
for i in range(1,n+1):
    print(bit_sum(i))