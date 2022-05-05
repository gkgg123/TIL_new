import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()


INF = float('inf')

N,M = map(int,input().split())

graph = [{} for _ in range(N+1)]

for _ in range(M):
    x,y,pay = map(int,input().split())
    if graph[x].get(y):
        graph[x][y] = min(graph[x][y],pay)
        graph[y][x] = min(graph[y][x],pay)
    else:
        graph[x][y] = pay
        graph[y][x] = pay


distance_list = [INF for _ in range(N+1)]
visited = [False for _ in range(N+1)]
distance_list[1] = 0

node_list = []

heapq.heappush(node_list,(0,1))
cnt = 0
answer = 0
remove_edge = 0
while node_list:
    cur_dis, node = heapq.heappop(node_list)

    if visited[node]:
        continue
    visited[node] = True
    cnt += 1
    answer += cur_dis
    remove_edge = max(cur_dis,remove_edge)
    if cnt == N:
        break

    for next_node in graph[node]:
        if visited[next_node]:continue
        if distance_list[next_node] > graph[node][next_node]:
            distance_list[next_node] = graph[node][next_node]
            heapq.heappush(node_list,(distance_list[next_node],next_node))


print(answer-remove_edge)
