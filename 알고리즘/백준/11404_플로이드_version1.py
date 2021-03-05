import sys

input = sys.stdin.readline
n = int(input())
INF = float('inf')
graph = [[INF if i !=j else 0 for j in range(n)] for i in range(n)]
m = int(input())

for _ in range(m):
    A,B,C = map(int,input().split())
    graph[A-1][B-1] = min(graph[A-1][B-1],C)
for k in range(n):
    for start in range(n):
        for end in range(n):
            if graph[start][end] > graph[start][k] + graph[k][end]:
                graph[start][end] = graph[start][k] + graph[k][end]



for row in graph:
    print(*[j if j != INF else 0 for j in row])