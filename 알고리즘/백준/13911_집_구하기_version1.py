import heapq
import sys
input = sys.stdin.readline
def dijkstra(start_list,flag):
    global V,mac,star,INF,limit_x,limit_y,home_info
    distance = [INF]*(V+1)
    node_list = []
    limited = limit_x
    if flag:
        limited = limit_y
    for ind in start_list:
        distance[ind] = 0 
        heapq.heappush(node_list,(0,ind))

    while node_list:
        current_distance,node = heapq.heappop(node_list)
        if current_distance > limited:
            break
        if current_distance > distance[node]:
            continue
        for next_node in graph[node]:
            temp_distance = current_distance + graph[node][next_node]
            if distance[next_node] > temp_distance:
                distance[next_node] = temp_distance
                heapq.heappush(node_list,(temp_distance,next_node))
    for ind in home:
        if limited >= distance[ind]:
            home_info[ind][int(flag)] = distance[ind]
    

V,E = map(int,input().split())
INF = float('inf')
graph = [{} for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u][v] = w
    graph[v][u] = w
mac_cnt,limit_x = map(int,input().split())
mac = set(map(int,input().split())) 
star_cnt,limit_y = map(int,input().split())
star = set(map(int,input().split()))

home = set(range(1,V+1))- mac - star
home_info = [[INF,INF] for _ in range(V+1)]

dijkstra(mac,False)
dijkstra(star,True)
min_sum = INF
for home_ind in home:
    if sum(home_info[home_ind]) < min_sum:
        min_sum = sum(home_info[home_ind]) 

if min_sum != INF:
    print(min_sum)
else:
    print(-1)
