import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()

def dfs(distance,s,e):
    stack = [s]
    acc_distance = 0
    while stack[-1] != e:
        cur_node = stack[-1]
        for next_node in sorted(graph[cur_node]):
            if acc_distance + distance[next_node] + graph[cur_node][next_node] != distance[s]:
                continue
            stack.append(next_node)
            acc_distance += graph[cur_node][next_node]
            break
    
    for node in stack[1:-1]:
        graph[node].clear()

def dijkstra(s,e,flag=True):
    INF = float('inf')
    distance_list = [INF for _ in range(N+1)]
    distance_list[s] = 0
    node_list = []
    heapq.heappush(node_list,(0,s))
    while node_list:
        cur_dis,cur_node = heapq.heappop(node_list)
        if distance_list[cur_node] < cur_dis:
            continue
        if cur_node == e:
            break
        for next_node in graph[cur_node]:
            if distance_list[next_node] > cur_dis + graph[cur_node][next_node]:
                distance_list[next_node] = cur_dis + graph[cur_node][next_node]
                heapq.heappush(node_list,(distance_list[next_node], next_node))
    if flag:
        dfs(distance_list, e, s)     
    return distance_list[e]

N,M = map(int,input().split())


graph = [{} for _ in range(N+1)]

for _ in range(M):
    x,y,pay = map(int,input().split())
    graph[x][y] = pay
    graph[y][x] = pay

S,E = map(int,input().split())
route_a = dijkstra(E,S)
route_b = dijkstra(S,E,False)
print(route_b + route_a)
