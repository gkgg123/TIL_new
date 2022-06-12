import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()

N,M = map(int,input().split())

graph = [{} for _ in range(N+1)]


for _ in range(M):
    x,y,pay = map(int,input().split())

    graph[x][y] = min(graph[x].get(y,float('inf')),pay)
    graph[y][x] = min(graph[y].get(x,float('inf')),pay)



node_list = []
heapq.heappush(node_list,(0,1))
distance_list = [float('inf') for _ in range(N+1)]
distance_list[1] = 0
while node_list:
    cur_pay,node = heapq.heappop(node_list)

    if distance_list[node] > cur_pay:
        continue
    if node == N:
        break
    for next_node in graph[node]:
        if distance_list[next_node] > graph[node][next_node] + cur_pay:
            distance_list[next_node] = graph[node][next_node] + cur_pay
            heapq.heappush(node_list,(distance_list[next_node],next_node))

print(distance_list[N])