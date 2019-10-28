MOD = 10**9 + 7
MAX_N = 10**5 

fac = [1] + [0] * MAX_N
fac_inv = [1] + [0] * MAX_N
for i in range(1, MAX_N+1):
    fac[i] = fac[i-1] * (i) % MOD
    # Fermat's little theorem says
    # a**(p-1) mod p == 1
    # then, a * a**(p-2) mod p == 1
    # it means a**(p-2) is inverse element
    fac_inv[i] = fac_inv[i-1] * pow(i, MOD-2, MOD) % MOD

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

if __name__ == "__main__":
    for i in range(11):
        print(pow(10, i, MOD))
    print("nCr")
    for i in range(-2, 12):
        print(10, i)
        print(mod_nCr(10, i))
        print(single_mod_nCr(10, i))
