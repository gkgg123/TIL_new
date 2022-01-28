import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()
def dijkstra(node_num):
    distance = [INF for _ in range(N+1)]
    node_list = [(0,node_num)]
    distance[node_num] = 0
    while node_list:
        cur_dis,cur_node = heapq.heappop(node_list)
        if cur_dis > distance[cur_node]:
            continue

        for next_node,next_pay in graph[cur_node]:
            if distance[next_node] > cur_dis + next_pay:
                distance[next_node] = cur_dis + next_pay
                heapq.heappush(node_list,(distance[next_node],next_node))
    return distance


N,W = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(W):
    x,y,pay = map(int,input().split())
    graph[x].append((y, pay))
    graph[y].append((x,pay))
start_node,end_node = map(int,input().split())

P = int(input())
mid_nodes = list(map(int,input().split()))

INF = float('inf')


st_distance = dijkstra(start_node)
ed_distance = dijkstra(end_node)

result = INF
for i in range(P):
    if st_distance[mid_nodes[i]] == INF or ed_distance[mid_nodes[i]] == INF:
        continue
    mid_distance = dijkstra(mid_nodes[i])
    for j in range(P):
        if i == j:
            continue
        if mid_distance[mid_nodes[j]] == INF or st_distance[mid_nodes[j]] == INF: 
            continue
        if st_distance[mid_nodes[j]] + mid_distance[mid_nodes[j]] >= result:
            continue
        for k in range(P):
            if i == k or j == k:
                continue
            if ed_distance[mid_nodes[k]] == INF or st_distance[mid_nodes[k]] == INF or mid_distance[mid_nodes[k]] == INF:
                continue
            temp = st_distance[mid_nodes[j]] + mid_distance[mid_nodes[j]] + mid_distance[mid_nodes[k]] + ed_distance[mid_nodes[k]]
            if result > temp:
                result = temp

if result == INF:
    print(-1)
else:
    print(result)
