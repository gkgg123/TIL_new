# 플로이드 와샬

N = int(input())
graph = [[0]+[50]*N if i!=0 else [50]*(N+1) for i in range(N+1)]
while True:
    a,b = map(int,input().split())
    if a == b == -1:
        break
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1,N+1):
    graph[i][i] = 0

for k in range(1,N+1):
    for from_node in range(1,N+1):
        for to_node in range(1,N+1):
            if graph[from_node][to_node] == 1 or graph[from_node][to_node] == 0:
                continue
            elif graph[from_node][to_node] > graph[from_node][k] + graph[k][to_node]:
                graph[from_node][to_node] = graph[from_node][k] + graph[k][to_node]


min_result = list(map(max,graph))

print(min(min_result),min_result.count(min(min_result)))
min_ind = []
for ind,val in enumerate(min_result):
    if val == min(min_result):
        min_ind.append(ind)
print(*min_ind)