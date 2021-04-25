from collections import deque

def bfs(node):
    stack = deque()
    stack.append(node)

    while stack:
        node = stack.popleft()

        for next_node in graph[node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[node] + 1

                stack.append(next_node)



N, M = map(int,input().split())
INF = float('inf')
visited = [-1]*(N+1)


visited[1] = 0

graph =[[] for _ in range(N+1)]


for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
bfs(1)

max_value = max(visited)
max_ind = -1
for k in range(1,N+1):
    if visited[k] == max_value:
        max_ind = k
        break
print(max_ind,max_value,visited.count(max_value))
