import heapq
import sys

input = sys.stdin.readline
N,M = map(int,input().split())


graph = [{} for _ in range(N+1)]
total_pay = 0
for _ in range(M):
    x,y,pay = map(int,input().split())
    graph[x][y] = pay
    graph[y][x] = pay
    total_pay += pay

INF = float('inf')

distance = [INF for _ in range(N+1)]
visited = [False for _ in range(N+1)]
node_list = []
heapq.heappush(node_list,(0,1))
result = 0
distance[1] = 0
cnt = 0
while node_list:
    dis,node = heapq.heappop(node_list)

    if visited[node]:
        continue
    result += dis
    cnt += 1
    visited[node] = True
    for next_node in graph[node]:
        if distance[next_node] > graph[node][next_node]:
            distance[next_node] = graph[node][next_node]
            heapq.heappush(node_list,(distance[next_node],next_node))


if cnt == N:
    print(total_pay-result)
else:
    print(-1)
