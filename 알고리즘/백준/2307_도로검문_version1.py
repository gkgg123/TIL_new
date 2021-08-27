import sys
import heapq

def dijkstra(flag=False,*arg):
    distance = [INF for _ in range(N+1)]
    distance[1] = 0
    node_list = []
    if flag:
        remove_node = arg[0]
    heapq.heappush(node_list,(0,1))
    
    while node_list:
        cur_dis,node = heapq.heappop(node_list)
        if cur_dis>distance[node]:
            continue
        for next_node in graph[node]:
            if flag and ((node,next_node) == remove_node or (next_node,node) == remove_node):
                continue 
            temp_distance = cur_dis + graph[node][next_node]
            if distance[next_node] > temp_distance:
                distance[next_node] = temp_distance
                heapq.heappush(node_list,(temp_distance,next_node))
    if not flag:
        stack = [(N,distance[N])]
        while stack:
            node,dis = stack.pop()
            for prev_node in graph[node]:
                if (prev_node,node) not in short_list:
                    if distance[prev_node] + graph[prev_node][node] == dis:
                        short_list.add((prev_node,node))
                        stack.append((prev_node,distance[prev_node]))

    return distance[N]
    

def input():
    return sys.stdin.readline()


N,M = map(int,input().split())

graph = [{} for _ in range(N+1)]
for _ in range(M):
    x,y,pay = map(int,input().split())
    graph[x][y] = pay
    graph[y][x] = pay

INF = float('inf')

short_list = set()
short_time = dijkstra()
short_list = list(short_list)

result = -1
for node in short_list:
    remove_time = dijkstra(True,node)
    result = max(result,remove_time - short_time)

print(result if result != INF else -1)