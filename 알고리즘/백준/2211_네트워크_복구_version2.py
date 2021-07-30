import sys
from collections import defaultdict
import heapq
def input():
    return sys.stdin.readline().rstrip()
N,M = map(int,input().split())



graph = [defaultdict(list) for _ in range(N+1)]

for _ in range(M):
    x,y,pay = map(int,input().split())
    graph[x][y].append(pay)
    graph[y][x].append(pay)


node_list = []
INF = float('inf')
distance_list = [INF for _ in range(N+1)]
distance_list[1] = 0
heapq.heappush(node_list,(0,1,1))
result = []

while node_list:
    cur_dis, cur_node , parent_node  = heapq.heappop(node_list)
    if cur_dis > distance_list[cur_node]:
        continue
    if cur_node != parent_node:
        result.append((parent_node, cur_node))
    for next_node in graph[cur_node]:


        for pay in graph[cur_node][next_node]:
            if cur_dis + pay < distance_list[next_node]:
                distance_list[next_node] = cur_dis + pay
                heapq.heappush(node_list,(distance_list[next_node], next_node , cur_node ))

print(len(result))

for row in result:
    print(*row)