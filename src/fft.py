import cmath
pi = cmath.pi
exp = cmath.exp

def fft(a, inverse=False):
    n = len(a)
    h = n.bit_length() - 1

    # Swap
    for i in range(n):
        j = 0
        for k in range(h):
            j |= (i >> k & 1) << (h - 1 - k)
        if i < j:
            a[i], a[j] = a[j], a[i]

    # Butterfly calculation
    if inverse:
        sign = 1.0
    else:
        sign = -1.0
    b = 1
    while b < n:
        for j in range(b):
            w = exp(sign * 2.0j * pi / (2.0 * b) * j)
            for k in range(0, n, b*2):
                s = a[j + k]
                t = a[j + k + b] * w
                a[j + k] = s + t
                a[j + k + b] = s - t
        b *= 2

    if inverse:
        for i in range(n):
            a[i] /= n

    return a

def ifft(a):
    return fft(a, inverse=True)

def convolve(f, g):
    n = 2**((len(f) + len(g) - 1).bit_length())
    f += [0] * (n - len(f))
    g += [0] * (n - len(g))
    F = fft(f)
    G = fft(g)
    FG = [Fi * Gi for Fi, Gi in zip(F, G)]
    fg = [int(item.real + 0.5) for item in ifft(FG)]
    return fg

if __name__ == "__main__":
    f = [0,1,0,1]
    g = [0,1,3,9]
    fg = convolve(f, g)
    print(fg)
