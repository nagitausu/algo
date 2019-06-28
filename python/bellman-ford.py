n = 4
m = 4
inf = 10**10
edge = [[0,1,-4], [1,2,-2], [2,3,-0]]

def BellmanFord(start):
    dist = [inf for i in range(n)]
    dist[0] = 0
    for i in range(n):
        for u, v, c in edge:
            if dist[u] != inf and (dist[u] + c) < dist[v]:
                dist[v] = dist[u] + c
                if i == n-1 and v == n-1:
                    return "inf"
    return -dist[-1]

ret = BellmanFord(0)
print(ret)
