from collections import deque


def dfs():
    graph = [[0] * N for _ in range(N)]
    for i in range(M):
        x, y = arr[i]
        graph[x - 1][y - 1] += 1
        graph[y - 1][x - 1] += 1

    result = [V]
    stack = [V - 1]
    
    while stack:
        x = stack.pop()
        if x + 1 not in result:
            result.append(x + 1)
        for k in range(N - 1, -1, -1):
            if graph[x][k] >= 1:
                graph[x][k] = 0
                graph[k][x] = 0
                stack.append(k)
    
    return result


def bfs():
    graph = [[0] * N for _ in range(N)]
    for i in range(M):
        x, y = arr[i]
        graph[x - 1][y - 1] += 1
        graph[y - 1][x - 1] += 1

    result = [V]
    q = deque()
    q.append(V - 1)

    while q:
        x = q.popleft()
        if x + 1 not in result:
            result.append(x + 1)
        for k in range(N):
            if graph[x][k] >= 1:
                graph[x][k] -= 1
                graph[k][x] -= 1
                
                q.append(k)
    
    return result



N, M, V = map(int, input().split())
arr = [list(map(int ,input().split())) for _ in range(M)]

dfs_res = dfs()
for i in range(len(dfs_res)):
    print(dfs_res[i], end=" ")
print()
bfs_res = bfs()
for i in range(len(bfs_res)):
    print(bfs_res[i], end=" ")
print()