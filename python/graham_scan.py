import math
from functools import reduce
n = int(input())
xy = []
for i in range(n):
    x, y = [int(item) for item in input().split()]
    xy.append([x, y, i])

def convex_hull_graham(points):
    TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

    def cmp(a, b):
        return (a > b) - (a < b)

    def turn(p, q, r):
        return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

    def _keep_left(hull, r):
        while len(hull) > 1 and turn(hull[-2], hull[-1], r) == TURN_RIGHT:
            hull.pop()
        if not len(hull) or hull[-1] != r:
            hull.append(r)
        return hull

    points = sorted(points)
    l = reduce(_keep_left, points, [])
    u = reduce(_keep_left, reversed(points), [])
    return l.extend(u[i] for i in range(1, len(u) - 1)) or l

ret = convex_hull_graham(xy)
ret.append(ret[0])
ret.append(ret[1])
thetas = [0.0] * n
for i in range(1, len(ret)-1):
    v1 = [-ret[i][1] + ret[i-1][1], ret[i][0] - ret[i-1][0]]
    v2 = [-ret[i+1][1] + ret[i][1], ret[i+1][0] - ret[i][0]]
    v1_norm = math.sqrt(v1[0]**2.0 + v1[1]**2.0)
    v2_norm = math.sqrt(v2[0]**2.0 + v2[1]**2.0)
    thetas[ret[i][2]] = math.acos((v1[0]*v2[0] + v1[1]*v2[1]) / (v1_norm * v2_norm))
for item in thetas:
    print(item / (math.pi * 2.0))