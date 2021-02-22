import collections


def bfs(i):
    global N,graph,result
    stack = collections.deque()
    stack.append((i,0))
    visited = [True] * (N+1)
    visited[i] = False
    while stack:
        ind,dep = stack.popleft()
        for next_ind in graph[ind]:
            if visited[next_ind]:
                stack.append((next_ind,dep+1))
                visited[next_ind] = False
    return dep







N = int(input())
graph = [[] for _ in range(N+1)] 
while True:
    a,b = map(int,input().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)


result = [50]*(N+1)
for i in range(1,N+1):
    result[i] = bfs(i)


min_list = [min(result),result.count(min(result))]
print(*min_list)
min_result = []
for i in range(1,N+1):
    if result[i] == min_list[0]:
        min_result.append(i)
print(*min_result)