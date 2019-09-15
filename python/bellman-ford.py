import sys
sys.setrecursionlimit(10**6)
INF = 10**10
 
def dfs(edge, visited, n):
    if visited[n]:
        return
    visited[n] = True
    for to, _ in edge[n]:
        dfs(edge, visited, to)

def bellman_ford(edge, mask):
    dist = [INF] * n
    dist[0] = 0

    for _ in range(n):
        update = False
        for i, es in enumerate(edge):
            if not mask[i]:
                continue
            for to, cost in es:
                if not mask[to]:
                    continue
                if dist[i] != INF and dist[i] + cost < dist[to]:
                    dist[to] = dist[i] + cost
                    update = True
        if not update:
            return dist
    else:
        # Minus loops detected
        return -INF

if __name__ == "__main__":
    n, m, p = [int(item) for item in input().split()]
    edge = [[] for _ in range(n)]
    redge = [[] for _ in range(n)]
    for i in range(m):
        a, b, c = [int(item) for item in input().split()]
        # Think as penalty costs per walk
        a -= 1; b -= 1; c -= p
        # Reverse cost to assume as shortest path problem
        c *= -1
        edge[a].append((b, c))
        redge[b].append((a, c)) 
    
    # Is the node can be arrived from start?
    visited = [False] * n
    dfs(edge, visited, 0)
    # Can the node go to the end?
    rvisited = [False] * n
    dfs(redge, rvisited, n-1)
    mask = [forward and backward for forward, backward in zip(visited, rvisited)]

    dist = bellman_ford(edge, mask)
    if dist == -INF:
        print(-1)
    else:
        print(max(0, -dist[n-1]))
