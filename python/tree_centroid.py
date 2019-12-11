#!/usr/bin/env python3
n = 6
edge = [[1, 2, 3], [0, 4, 5], [0], [0], [1], [1]]
centroid = []
weight = [0] * n
def dfs_centroid(v, p):
    weight[v] = 1
    ok = True
    for nv in edge[v]:
        if nv != p:
            dfs_centroid(nv, v)
            weight[v] += weight[nv]
            ok &= weight[nv] <= n // 2
    ok &= (n - weight[v]) <= n // 2
    if ok:
        centroid.append(v)

dfs_centroid(0, -1)
print(centroid)