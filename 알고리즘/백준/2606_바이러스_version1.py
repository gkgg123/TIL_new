def bfs(N):
    stack = [1]
    visted = [0]*(N+1)
    cnt = 0
    visted[1] = 1
    while stack:
        num = stack.pop()
        cnt += 1
        for ind in graph[num]:
            if not visted[ind]:
                visted[ind] = 1
                stack.append(ind)
    return cnt - 1

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


print(bfs(N))