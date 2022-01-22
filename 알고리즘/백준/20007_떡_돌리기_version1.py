import sys
from collections import defaultdict
import heapq
def input():
    return sys.stdin.readline().rstrip()

N,M,X,Y = map(int,input().split())

graph = defaultdict(dict)
for _ in range(M):
    x,y,c = map(int,input().split())
    graph[x][y] = c
    graph[y][x] = c



node_list = [(0,Y)]
distance_list = [float('inf') for _ in range(N)]
distance_list[Y] = 0
cnt = 0
cur_val = X
while node_list:
    dis,node =  heapq.heappop(node_list)

    if distance_list[node] < dis:
        continue
    if 2*dis > X:
        cnt = -1
        break

    if cur_val - 2*dis>=0:
        cur_val = cur_val-2*dis
    else:
        cur_val = X
        cur_val = cur_val-2*dis
        cnt +=1

    for next_node in graph[node]:

        if distance_list[next_node] > dis + graph[node][next_node]:
            distance_list[next_node] = dis + graph[node][next_node]

            heapq.heappush(node_list,(distance_list[next_node],next_node))


if cnt != -1:
    print(cnt+1)
else:
    print(cnt)