n = 16 
bit = [1] * (n + 1) 

# Initialize BIT with non-zero value
def bit_init():
    for i in range(1, n):
        if i + (i & -i) > n:
            continue
        bit[i + (i & -i)] += bit[i]

# Add w to ax 
def bit_add(x, w):
    while x <= n:
        bit[x] += w
        x += x & -x

# Sum a1 to ax 
def bit_sum(x):
    ret = 0
    while x > 0:
        ret += bit[x]
        x -= x & -x
    return ret

bit_init()
print(bit[1:])
for i in range(1,n+1):
    bit_add(i, 1)
print(bit[1:])
for i in range(1,n+1):
    print(bit_sum(i))