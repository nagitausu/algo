def factorize(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct

if __name__ == "__main__":
    print(factorize(354))