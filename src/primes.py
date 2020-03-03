from fractions import gcd
small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

# O(nloglogn)
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

# O(sqrt(n))
def prime_factorize(n, unique=False):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    if unique:
        return set(fct)
    else:
        return fct

# Millar Rabin primality test, O(k(logn)^3)
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = n - 1
    while d % 2 == 0:
        d //= 2
    for p in small_primes:
        if n <= p:
            break
        t = d
        y = pow(p, t, n)
        while t != n - 1 and y != 1 and y != n - 1:
            y = y * y % n
            t <<= 1
        if y != n - 1 and t % 2 == 0:
            return False
    return True

def calc_primefactor(n):
    if is_prime(n):
        return n
    if n % 2 == 0:
        return 2
    i = 0
    while True:
        i += 1
        x = i; y = (x * x + 1) % n
        while True:
            p = gcd(y - x + n, n)
            if p == 0 or p == n:
                break
            if p != 1:
                return p
            x = (x * x + 1) % n
            y = (y * y + 1) % n
            y = (y * y + 1) % n

# Pollard's rho algorithm, O(n^0.25logn)?
def prime_factorize_fast(n):
    if n == 1:
        return []
    x = calc_primefactor(n)
    if x == n:
        return [x]
    le = prime_factorize_fast(x)
    ri = prime_factorize_fast(n // x)
    le += ri
    return le

def toyproblem():
    print("Prime factorize fast")
    print(prime_factorize_fast(3540))
    print("Prime factorize")
    print(prime_factorize(3540))
    print("Prime factorize unique")
    print(prime_factorize(3540, unique=True))
    print("All primes under N")
    print(primes(354))

# Verify: https://judge.yosupo.jp/problem/factorize
def verify():
    q = int(input())
    for _ in range(q):
        a = int(input())
        ret = prime_factorize_fast(a)
        ret.sort()
        ans = str(len(ret)) + " "
        ans += " ".join([str(item) for item in ret])
        print(ans)

if __name__ == "__main__":
    toyproblem()