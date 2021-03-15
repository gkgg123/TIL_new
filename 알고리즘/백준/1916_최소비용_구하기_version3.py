import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
graph =[{} for i in range(N+1)]
for i in range(M):
    node_x,node_y,fee = map(int,input().split())
    if graph[node_x].get(node_y):
        graph[node_x][node_y].append(fee)
    else:
        graph[node_x][node_y] = [fee]

start,end = map(int,input().split())
INFS = float('inf')
min_fees = [INFS] *(N+1)
node_list = []
heapq.heappush(node_list,(0,start))
min_fees[start] = 0
while node_list:
    cu_distance, node = heapq.heappop(node_list)
    for next_node in graph[node]:
        for next_fee in graph[node][next_node]
            if next_fee + cu_distance < min_fees[next_node]:
                min_fees[next_node] = graph[node][next_node] + cu_distance
                heapq.heappush(node_list,(min_fees[next_node],next_node))
print(min_fees[end])