import sys

input = sys.stdin.readline
def dfs(node):
    distance_list = [0 for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    visited[node] = True
    stack = [(node,0)]
    while stack:
        node,distance = stack.pop()
        distance_list[node] = distance
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append((next_node,graph[node][next_node]+distance))
    return distance_list

N = int(input())
graph = [{} for _ in range(N+1)]

for _ in range(N-1):
    x,y,pay = map(int,input().split())
    graph[x][y] = pay
    graph[y][x] = pay


distance1 = dfs(1)
far_point1 = distance1.index(max(distance1))
distance2 = dfs(far_point1)
far_point2 = distance2.index(max(distance2))
distance3 = dfs(far_point2)
result = sorted(distance2+distance3)[-3]
print(result)