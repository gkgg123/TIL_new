def dfs(ind):
    global N,result
    visited = [True]*(N+1)
    stack = [(ind,0)]
    while stack:
        cu_ind,distance = stack.pop()
        if not visited[cu_ind]:
            continue
        visited[cu_ind] = False
        if distance > result:
            result = distance
        for next_ind in graph[cu_ind]:
            if visited[next_ind]:
                stack.append((next_ind,distance+graph[cu_ind][next_ind]))

N = int(input())
graph = [{} for _ in range(N+1)]
parents = [0]*(N+1)
for _ in range(N-1):
    A,B,C = map(int,input().split())
    graph[A][B] = C
    graph[B][A] = C
    parents[A] += 1

leef_nodes = []

for ind in range(1,N+1):
    if not parents[ind]:
        leef_nodes.append(ind)

result = 0

for ind in leef_nodes:
    dfs(ind)
print(result)