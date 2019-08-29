n = 5
INF = 10**5
dist = [[INF] * n for _ in range(n)]
graph = [[0,21,2,11,39],
         [21,0,INF,10,INF],
         [2,INF,0,23,INF],
         [11,10,23,0,INF],
         [39,INF,INF,INF,0]]

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], graph[i][k] + graph[k][j])

print("graph")
for line in graph:
    print(line)

print("dist")
for line in dist:
    print(line)
