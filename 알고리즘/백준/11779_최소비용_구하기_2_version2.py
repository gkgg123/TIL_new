import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [{} for _ in range(N+1)]

path = [-1 for _ in range(N+1)]
for _ in range(M):
    x,y,pay = map(int,input().split())
    graph[x][y] = min(graph[x].get(y,float('inf')),pay)

INF = float('inf')
distance = [INF]*(N+1)

start_city,end_city = map(int,input().split())

distance[start_city] = 0
node_list = []
heapq.heappush(node_list,(0,start_city))

while node_list:
    cur_dis,cur_node = heapq.heappop(node_list)

    if distance[cur_node] < cur_dis:
        continue
    for next_node in graph[cur_node]:
        if distance[next_node] > cur_dis + graph[cur_node][next_node]:
            distance[next_node] = cur_dis + graph[cur_node][next_node]
            heapq.heappush(node_list,(distance[next_node],next_node))
            path[next_node] = cur_node


print(distance[end_city])
result = []
city = end_city

while True:
    if city == start_city:
        result.append(city)
        break
    result.append(city)
    city = path[city]
print(len(result))
result.reverse()
print(*result)
    


