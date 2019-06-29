MOD = 10**9 + 7
MAX_N = 10**5 

fac = [1] + [0] * MAX_N
fac_inv = [1] + [0] * MAX_N
for i in range(1, n+1):
    fac[i] = fac[i-1] * (i) % MOD
    # Fermat's little theorem says
    # a**(p-1) mod p == 1
    # then, a * a**(p-2) mod p == 1
    # it means a**(p-2) is inverse element
    fac_inv[i] = fac_inv[i-1] * pow(i, MOD-2, MOD) % MOD

def mod_nCr(n, r):
    if n == 0 and r == 0:
        return 1
    if n < r or n < 0:
        return 0
    tmp = fac_inv[n-r] * fac_inv[r] % MOD
    return tmp * fac[n] % MOD 

if __name__ == "__main__":
    for i in range(11):
        print(pow(10, i, MOD))
    for i in range(11):
        print(mod_nCr(10, i))
