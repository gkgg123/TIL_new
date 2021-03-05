import sys
import heapq

input = sys.stdin.readline
V,E = map(int,input().split())

graph = [{} for _ in range(V+1)]

for _ in range(E):
    A,B,C = map(int,input().split())
    graph[A][B] = C
    graph[B][A] = C
INF = float('inf')
distance = [INF]*(V+1)
visited = [False]*(V+1)
node_list = []
distance[1] = 0
heapq.heappush(node_list,(0,1))
result = 0
while node_list:
    key,node = heapq.heappop(node_list)
    if visited[node]:
        continue
    visited[node] = True
    result += key
    for next_node in graph[node]:
        if distance[next_node] > graph[node][next_node]:
            heapq.heappush(node_list,(graph[node][next_node],next_node))
            distance[node] = graph[node][next_node]
print(result)