def dfs(i,cnt):
    global result
    visited[i] = False
    if cnt >= 5:
        result = True
        return
    for ind in graph[i]:
        if visited[ind]:
            dfs(ind,cnt+1)
    visited[i] = True


N,M = map(int,input().split())
graph = [[] for _ in range(N)]


for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [True]*N
result = False
for i in range(N):
    dfs(i,1)
    if result:
        break
print(int(result))