#!/usr/bin/env python3
import sys
input = sys.stdin.readline
INF = 10**10
 
class ExtendedBellmanFord:
    def __init__(self, edge):
        self.f_edge = edge
        self.b_edge = [[] for _ in range(len(edge))]
        for src, es in enumerate(edge):
            for dst, cost in es:
                self.b_edge[dst].append((src, -cost))

    def bellman_ford(self, mask, start):
        dist = [INF] * n
        dist[start] = 0
        for _ in range(n):
            update = False
            for i, es in enumerate(self.f_edge):
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

    def calc(self, start, end):
        visited = [False] * n
        visited[start] = True
        st = [start]
        while st:
            node = st.pop()
            for to, _ in self.f_edge[node]:
                if not visited[to]:
                    visited[to] = True
                    st.append(to)
        rvisited = [False] * n
        rvisited[end] = True
        st = [end]
        while st:
            node = st.pop()
            for to, _ in self.b_edge[node]:
                if not rvisited[to]:
                    rvisited[to] = True
                    st.append(to)
        mask = [forward and backward for forward, backward in zip(visited, rvisited)]
        dist = self.bellman_ford(mask, start)
        if dist == -INF:
            return -INF
        else:
            return dist[end]

if __name__ == "__main__":
    n, m, p = [int(item) for item in input().split()]
    edge = [[] for _ in range(n)]
    for i in range(m):
        a, b, c = [int(item) for item in input().split()]
        a -= 1; b -= 1; c -= p
        c *= -1
        edge[a].append((b, c))
    
    EBF = ExtendedBellmanFord(edge)
    ret = EBF.calc(0, n-1)
    if ret == -INF:
        print(-1)
    else:
        print(max(0, -ret))