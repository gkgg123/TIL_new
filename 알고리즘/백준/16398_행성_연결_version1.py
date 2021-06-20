import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()


N = int(input())

graph = [list(map(int,input().split())) for _ in range(N)]

node_list = []

INF = float('inf')
distance_list = [INF for _ in range(N)]
visited = [False for _ in range(N)]
heapq.heappush(node_list,(0,0))
distance_list[0] = 0
result = 0
while node_list:
    cur_dis,cur_node = heapq.heappop(node_list)
    if visited[cur_node]:continue
    if cur_dis > distance_list[cur_node]:continue
    result += cur_dis
    visited[cur_node] = True
    for next_node in range(N):
        if next_node == cur_node:continue
        if visited[next_node]:continue
        if distance_list[next_node] > graph[cur_node][next_node]:
            distance_list[next_node] = graph[cur_node][next_node]
            heapq.heappush(node_list,(distance_list[next_node],next_node))

print(result)
