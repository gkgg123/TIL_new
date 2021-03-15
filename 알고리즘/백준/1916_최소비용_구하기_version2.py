import sys
import heapq
sys.stdin = open('1916_test_input.txt','r')
input = sys.stdin.readline

N = int(input())
M = int(input())
graph =[[] for i in range(N+1)]
for i in range(M):
    node_x,node_y,fee = map(int,input().split())
    graph[node_x].append((node_y,fee))

start,end = map(int,input().split())
INFS = float('inf')
min_fees = [INFS] *(N+1)
node_list = []
heapq.heappush(node_list,(0,start))
min_fees[start] = 0
while node_list:
    cu_distance, node = heapq.heappop(node_list)
    if min_fees[node] < cu_distance:
        continue
    for next_node,fee in graph[node]:
        if fee + cu_distance < min_fees[next_node]:
            min_fees[next_node] = fee + cu_distance
            heapq.heappush(node_list,(min_fees[next_node],next_node))
print(min_fees[end])