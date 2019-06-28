n = 5
INF = 10**5
ngraph = [[INF] * n for _ in range(n)]
graph = [[0,21,18,11,28],
         [21,0,13,10,26],
         [18,13,0,23,13],
         [11,10,23,0,17],
         [28,26,13,17,0]]
        
for i in range(n):
    for j in range(n):
        for k in range(n):
            ngraph[i][j] = min(ngraph[i][j], graph[i][k] + graph[k][j])

for item in ngraph:
    print(item)
