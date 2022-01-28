import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()
def dijkstra(node_num,ind):
    global distance_list
    node_list = [(0,node_num)]
    distance_list[ind][node_num] = 0
    while node_list:
        cur_dis,cur_node = heapq.heappop(node_list)
        if cur_dis > distance_list[ind][cur_node]:
            continue

        for next_node,next_pay in graph[cur_node]:
            if distance_list[ind][next_node] > cur_dis + next_pay:
                distance_list[ind][next_node] = cur_dis + next_pay
                heapq.heappush(node_list,(distance_list[ind][next_node],next_node))


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
distance_list = [[INF for _ in range(N+1)] for _ in range(P+1)]


dijkstra(start_node,P)

match_ind = {}
for ind,num in enumerate(mid_nodes):
    dijkstra(num,ind)
    match_ind[ind] = num

result = INF

for ind1 in range(P):
    temp1 = 0
    if distance_list[P][match_ind[ind1]] == INF:
        continue
    temp1 += distance_list[P][match_ind[ind1]]
    if temp1>result:
        continue
    for ind2 in range(P):
        if ind1 == ind2 or distance_list[ind1][match_ind[ind2]] == INF:
            continue
        temp2 = temp1 + distance_list[ind1][match_ind[ind2]]
        if temp2>result:
            continue
        for ind3 in range(P):
            if ind2 == ind3 or ind1 == ind3 or distance_list[ind2][match_ind[ind3]] == INF:
                continue

            temp3 = temp2 + distance_list[ind2][match_ind[ind3]] + distance_list[ind3][end_node]
            if temp3 < result:
                result = temp3

if result == INF:
    print(-1)
else:
    print(result)