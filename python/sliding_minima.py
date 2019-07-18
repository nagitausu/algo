from collections import deque

def sliding_minima(a, k):
    dq = deque()
    l = r = 0
    ret = []
    for i, item in enumerate(a):
        while(dq and a[dq[-1]] >= a[i]):
            dq.pop()
        dq.append(i)
        if i < k - 1:
            continue
        if dq[0] == i - k:
            dq.popleft()
        ret.append(a[dq[0]])
    return ret

def sliding_maxima(a, k):
    dq = deque()
    l = r = 0
    ret = []
    for i, item in enumerate(a):
        while(dq and a[dq[-1]] <= a[i]):
            dq.pop()
        dq.append(i)
        if i < k - 1:
            continue
        if dq[0] == i - k:
            dq.popleft()
        ret.append(a[dq[0]])
    return ret

if __name__ == "__main__":
    import random
    random.seed(0)
    n = 20; k = 5
    a = [random.randrange(0,100) for _ in range(n)] 
    print("raw", a)
    print("min", sliding_minima(a, k))
    print("max", sliding_maxima(a, k))
