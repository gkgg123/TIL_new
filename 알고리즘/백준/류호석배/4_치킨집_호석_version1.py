import sys
from itertools import combinations
input = sys.stdin.readline

N,M = map(int,input().split())
INF = float('inf')
graph = [[INF if i !=j else 0 for j in range(N+1)] for i in range(N+1)]


for k in range(M):
    node_a,node_b = map(int,input().split())
    graph[node_a][node_b] = 1
    graph[node_b][node_a] = 1

for mid in range(1,N+1):
    for start in range(1,N+1):
        for end in range(1,N+1):
             if graph[start][end] > graph[start][mid] + graph[mid][end]:
                graph[start][end] = graph[start][mid] + graph[mid][end]

result = []
min_val = INF
for combi in combinations(range(1,N+1),2):
    temp = 0
    x,y = combi
    for ind in range(1,N+1):
        temp += min(graph[x][ind],graph[y][ind])
    if temp < min_val:
        result = [(x,y)]
        min_val = temp
    elif temp == min_val:
        result.append((x,y))
result.sort()

print(*result[0],min_val*2)