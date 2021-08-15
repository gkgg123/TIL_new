import sys
from collections import deque


N,M = map(int,input().split())

graph = []

subway_routelist = [[] for _ in range(N+1)]


for route_ind in range(M):
    arr = set(map(int,input().split()))
    arr.remove(-1)
    for subway_num in arr:
        subway_routelist[subway_num].append(route_ind)

    graph.append(list(arr))

start_node, end_node = map(int,input().split())
visited = [-1 for _ in range(N+1)]
visited_subway = [-1 for _ in range(M)]
end_subway = []

for route_ind in range(M):
    if end_node in graph[route_ind]:
        end_subway.append(route_ind)


queue = deque()
route_cnt = 0
visited[end_node] = 0
for end_route in end_subway:
    visited_subway[end_route] = route_cnt
    for subway_num in graph[end_route]:
        if visited[subway_num] == -1:
            visited[subway_num] = route_cnt
            queue.append(subway_num)

if visited[start_node] != -1:
    print(0)
else:
        
    while queue:
        N = len(queue)
        for _ in range(N):
            node = queue.popleft()
            for route in subway_routelist[node]:
                if visited_subway[route] == -1:
                    visited_subway[route] = route_cnt + 1
                    for subway_num in graph[route]:
                        if visited[subway_num] == -1:
                            visited[subway_num] = route_cnt + 1
                            queue.append(subway_num)
        route_cnt += 1
        if visited[start_node] != -1:
            break


    print(visited[start_node])