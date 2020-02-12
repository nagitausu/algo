MOD = 10**9 + 7
MAX_N = 10**5

# Construct factorial table
fac = [1] + [0] * MAX_N
for i in range(1, MAX_N+1):
    fac[i] = fac[i-1] * (i) % MOD

fac_inv = [1] + [0] * MAX_N
# Femrmat's little theorem says a**(p-1) mod p == 1
# then, a * a**(p-2) mod p == 1
# it means that a**(p-2) is the inverse element
# Here, Get 1 / n! first
fac_inv[MAX_N] = pow(fac[MAX_N], MOD-2, MOD)
for i in range(MAX_N, 1, -1):
    fac_inv[i-1] = fac_inv[i] * i % MOD

def mod_nCr(n, r):
    if n < r or n < 0 or r < 0:
        return 0
    tmp = fac_inv[n-r] * fac_inv[r] % MOD
    return tmp * fac[n] % MOD

def single_mod_nCr(n, r):
    if n < r or n < 0 or r < 0:
        return 0
    if r > n - r:
        r = n - r
    ret = 1
    for i in range(r):
        ret *= n - i
        ret *= pow(i+1, MOD-2, MOD)
        ret %= MOD
    return ret

def extgcd(a, b):
    if a == 0:
        return b, 0, 1
    d, y, x = extgcd(b % a, a)
    x -= b // a * y
    return d, x, y

if __name__ == "__main__":
    for i in range(11):
        print(pow(10, i, MOD))
    print("nCr")
    for i in range(-2, 12):
        print(10, i)
        print(mod_nCr(10, i))
        print(single_mod_nCr(10, i))
    print("ext gcd")
    print(extgcd(11, 13))
