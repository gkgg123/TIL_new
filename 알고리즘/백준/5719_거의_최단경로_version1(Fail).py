
import sys
import heapq

def dijkstra(start,end):
    global INF,N
    visited = [True]*N
    node = start
    dj_distance = [INF]*N
    dj_distance[start] = 0
    path = [-1]*N
    while True:
            visited[node] = False
            for next_node in graph[node]:
                if dj_distance[next_node] > dj_distance[node] + distance[node][next_node]:
                    dj_distance[next_node] = dj_distance[node] + distance[node][next_node]
                    path[next_node] = node                
            if node == end:
                cu = end
                while path[cu] != -1:
                    prev_path = path[cu]
                    distance[prev_path][cu] = 0
                    graph[prev_path].remove(cu)
                    cu = prev_path

                return dj_distance[end]

            next_node = -1
            next_min_distance = INF
            for ind in range(N):
                if visited[ind] and next_min_distance > dj_distance[ind]:
                    next_min_distance = dj_distance[ind]
                    next_node = ind
            if next_node != -1:
                node = next_node
            else:
                return INF


INF = float('inf')
while True:
    N,M = map(int,sys.stdin.readline().split())
    if not N+M:
        break 
    S,D = map(int,sys.stdin.readline().split())

    distance = [[0]*N for _ in range(N)]
    graph = [[] for _ in range(N)]
    for _ in range(M):
        U,V,P = map(int,sys.stdin.readline().split())
        graph[U].append(V)
        distance[U][V] = P
    min_distance = dijkstra(S,D)


    while True:
        cu_distance = dijkstra(S,D)
        if cu_distance != min_distance:
            if cu_distance != INF:
                print(cu_distance)
            else:
                print(-1)
            break