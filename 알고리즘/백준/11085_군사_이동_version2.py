# hsh8086 님 코드 복기

import sys
import heapq


input = sys.stdin.readline

P,W = map(int,input().split())

start_city,end_city = map(int,input().split())

graph = [{} for i in range(P)]

for _ in range(W):
    x,y,pay = map(int,input().split())
    graph[x][y] = max(graph[x].get(y,0),pay)
    graph[y][x] = max(graph[y].get(x,0),pay)


max_width_list = [0]*P
max_width_list[start_city] = float('inf')

node_list = []

heapq.heappush(node_list,(-float('inf'),start_city))


while node_list:
    maximun_width,cur_node  = heapq.heappop(node_list)
    maximun_width = -maximun_width
    for next_node in graph[cur_node]:
        
        cur_maximun_width = min(graph[cur_node][next_node],maximun_width)

        if cur_maximun_width > max_width_list[next_node]:
            max_width_list[next_node] = cur_maximun_width
            heapq.heappush(node_list,(-max_width_list[next_node],next_node))


print(max_width_list[end_city])