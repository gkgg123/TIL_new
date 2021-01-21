import heapq
import sys
N,M = map(int,input().split())
start = int(input())

graph = {i:[] for i in range(N+1)}

for _ in range(M):
    n1,n2,d = map(int,sys.stdin.readline().split())
    graph[n1].append((n2,d))
visited = [True] * (N+1)
INF = float('inf')
distance = [INF]*(N+1)
distance[start] = 0

node_list = []
heapq.heappush(node_list,(0,start))

while node_list:
    current_distance,node= heapq.heappop(node_list)
    visited[node] = True
    if distance[node]<current_distance:
        continue
    for next_node,next_dis in graph[node]:
        if visited[next_node]:
            temp_distance = current_distance + next_dis
            if distance[next_node] > temp_distance:
                distance[next_node] = temp_distance
                heapq.heappush(node_list,(distance[next_node],next_node))

for ind in range(1,N+1):
    if distance[ind] == INF:
        print('INF')
    else:
        print(distance[ind])