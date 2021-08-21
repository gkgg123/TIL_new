import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()

def dfs(distance,s,e):
    stack = []
    heapq.heappush(stack,([s],s))
    visited_set = set()
    while stack:
        path, node = heapq.heappop(stack)
        if node == e:
            for pa in path[1:-1]:
                graph[pa].clear()
            break
        if node not in visited_set:
            visited_set.add(node)
            for next_node in graph[node]:
                if graph[node][next_node] + distance[node] == distance[next_node]:
                    heapq.heappush(stack,(path + [next_node], next_node))


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
        dfs(distance_list, s, e)     
    return distance_list[e]

N,M = map(int,input().split())


graph = [{} for _ in range(N+1)]

for _ in range(M):
    x,y,pay = map(int,input().split())
    graph[x][y] = pay
    graph[y][x] = pay

S,E = map(int,input().split())
route_a = dijkstra(S,E)
route_b = dijkstra(E,S,False)
print(route_b + route_a)
