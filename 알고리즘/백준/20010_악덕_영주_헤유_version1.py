import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()

def dfs(node):
    distance_list = [0 for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    visited[node] = True
    stack = [(node,0)]
    while stack:
        node,distance = stack.pop()
        distance_list[node] = distance
        for next_node in new_graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append((next_node,new_graph[node][next_node]+distance))
    return distance_list


N,K = map(int,input().split())

graph = [{} for _ in range(N)]


for _ in range(K):
    x,y,pay = map(int,input().split())
    graph[x][y] = min(graph[x].get(y,float('inf')),pay)
    graph[y][x] = min(graph[y].get(y,float('inf')),pay)

INF = float('inf')
distance = [INF for _ in range(N)]
distance[0] = 0
new_graph = [{} for _ in range(N)]
node_list = []

heapq.heappush(node_list,(0,0,0))
visisted = [False for _ in range(N)]
result = 0
while node_list:
    cur_pay,cur_node,parent_node = heapq.heappop(node_list)
    if visisted[cur_node]:
        continue
    visisted[cur_node] = True
    result += cur_pay
    if cur_node != parent_node:
        new_graph[cur_node][parent_node] = min(new_graph[cur_node].get(parent_node,INF),cur_pay)
        new_graph[parent_node][cur_node] = min(new_graph[parent_node].get(cur_node,INF),cur_pay)

    for next_node in graph[cur_node]:
        if distance[next_node] > graph[cur_node][next_node]:
            distance[next_node] = graph[cur_node][next_node]
            heapq.heappush(node_list,(distance[next_node],next_node,cur_node))

print(result)

distance1 = dfs(0)
far_point1 = distance1.index(max(distance1))
distance2 = dfs(far_point1)
print(max(distance2))