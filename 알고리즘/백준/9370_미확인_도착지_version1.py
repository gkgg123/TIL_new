import sys
import heapq
def check(node):

    path_set = set()
    stack = [(node,distance[node])]

    while stack:
        node,dis = stack.pop()
        for prev_node in graph[node]:
            if (prev_node,node) not in path_set:
                if distance[prev_node] + graph[prev_node][node] == dis:
                    path_set.add((prev_node,node))
                    stack.append((prev_node,distance[prev_node]))
    if (G,H) in path_set or (H,G) in path_set:
        return True
    return False



def dijkstra(node):
    distance[node] = 0
    node_list = []
    heapq.heappush(node_list,(0,node))
    while node_list:
        cur_dis, cur_node = heapq.heappop(node_list)
        if distance[cur_node] > cur_dis:
            continue
        for next_node in graph[cur_node]:
            if distance[next_node] > graph[cur_node][next_node] + cur_dis:
                distance[next_node] = graph[cur_node][next_node] + cur_dis
                heapq.heappush(node_list,(graph[cur_node][next_node] + cur_dis,next_node))

    


input = sys.stdin.readline

for _ in range(int(input())):
    N,M,T = map(int,input().split())
    graph = [{} for _ in range(N+1)]
    start,G,H = map(int,input().split())
    for _ in range(M):
        x,y,pay = map(int,input().split())
        graph[x][y] = pay
        graph[y][x] = pay
    
    candidate_list = [int(input().rstrip()) for _ in range(T)]
    INF = float('inf')
    distance = [INF]*(N+1)
    dijkstra(start)
    result = []
    for check_node in candidate_list:
        if check(check_node):
            result.append(check_node)

    result.sort()
    print(*result)