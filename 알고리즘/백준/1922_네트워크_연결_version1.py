import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [{} for i in range(N)]

for _ in range(M):
    a,b,c = map(int,input().split())
    if a != b:
        graph[a-1][b-1] = c
        graph[b-1][a-1] = c

INF = float('inf')
distance = [INF]*N
visited = [False] *N
distance[0] = 0
node_list = []
heapq.heappush(node_list,(0,0))
result = 0
while node_list:
    dis, node = heapq.heappop(node_list)
    if visited[node]:
        continue
    result += dis
    visited[node] = True
    for next_node in graph[node]:
        if distance[next_node] > graph[node][next_node]:
            distance[next_node] = graph[node][next_node]
            heapq.heappush(node_list,(distance[next_node],next_node))

print(result)