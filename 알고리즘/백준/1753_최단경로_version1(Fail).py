import collections

N,M = map(int,input().split())
start = int(input())

graph = {i:[] for i in range(N+1)}

for _ in range(M):
    n1,n2,d = map(int,input().split())
    graph[n1].append((n2,d))
visited = [True] * (N+1)
INF = float('inf')
distance = [INF]*(N+1)
distance[start] = 0

node = start

while True:
    visited[node] = False
    for ind,dis in graph[node]:
        distance[ind] = min(distance[ind],distance[node]+dis)
    next_node = -1
    next_min_distance = INF
    for ind in range(N+1):
        if visited[ind] and next_min_distance > distance[ind]:
            next_min_distance = distance[ind]
            next_node = ind
    if next_node != -1:
        node = next_node
    else:
        break

for ind in range(1,N+1):
    if distance[ind] == INF:
        print('INF')
    else:
        print(distance[ind])