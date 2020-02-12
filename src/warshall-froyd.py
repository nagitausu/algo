n = 5
INF = 10**5
dist = [[0,21,2,11,39],
         [21,0,INF,10,INF],
         [2,INF,0,23,INF],
         [11,10,23,0,INF],
         [39,INF,INF,INF,0]]

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

print("dist")
for line in dist:
    print(line)