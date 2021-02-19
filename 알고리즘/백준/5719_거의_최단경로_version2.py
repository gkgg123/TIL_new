
import sys
import heapq


def dijkstra(start,end,flag=True):
    global INF,N
    distance = [INF]*N
    distance[start] = 0
    node_list = []
    heapq.heappush(node_list,(0,start))
    while node_list:
        current_distance,node = heapq.heappop(node_list)
        if current_distance > distance[node]:
            continue          
        for next_node in graph[node]:
            temp_distance = current_distance + graph[node][next_node]
            if distance[next_node] > temp_distance:
                distance[next_node] = temp_distance
                heapq.heappush(node_list,(temp_distance,next_node))
    if flag and distance[end] != INF:
        stack = [(end,distance[end])]
        path_set = set()
        while stack:
            node,dis = stack.pop()
            for prev_node in parent[node]:
                if (prev_node,node) not in path_set:
                    if distance[prev_node] + graph[prev_node][node] == dis:
                        path_set.add((prev_node,node))
                        stack.append((prev_node,distance[prev_node]))
        
        for prev_node,next_node in path_set:
            del graph[prev_node][next_node]

    return distance[end]
INF = float('inf')
while True:
    N,M = map(int,sys.stdin.readline().split())
    if not N+M:
        break 
    S,D = map(int,sys.stdin.readline().split())

    distance = [[0]*N for _ in range(N)]
    graph = [{} for _ in range(N)]
    parent = [[] for _ in range(N)]
    for _ in range(M):
        U,V,P = map(int,sys.stdin.readline().split())
        graph[U][V] = P
        parent[V].append(U)
    min_distance = dijkstra(S,D)
    if min_distance == INF:
        print(-1)
    else:
        cu_distance = dijkstra(S,D,False)
        if cu_distance != INF:
            print(cu_distance)
        else:
            print(-1)