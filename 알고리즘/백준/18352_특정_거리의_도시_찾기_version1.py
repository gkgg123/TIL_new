from collections import deque

def bfs(x):
    queue = deque()
    queue.append(x)
    distance[x] = 0
    while queue:
        now = queue.popleft()
        for next_node in graph[now]:
            if visited[next_node] == False:
                visited[next_node] = True
                if distance[next_node] == -1:
                    distance[next_node] = distance[now] + 1
                    queue.append(next_node)
                
                

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
visited = [False] * (n + 1)

bfs(x)

result = []
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        result.append(i)
        check = True
if len(result):
    for i in range(len(result)):
        print(result[i])
else:
    print(-1)

