

def solution(start,flag):
    global N
    stack = [start]
    visited = [True]*(N+1)
    ind = 0
    if flag:
        ind = -1
    result = []
    while stack:
        node_number = stack.pop(ind)
        if not visited[node_number]:
            continue
        visited[node_number] = False
        result.append(node_number)
        for next_node in sorted(graph[node_number],reverse=flag):
            if visited[next_node]:
                stack.append(next_node)
    return result




N,M,V = map(int,input().split())


graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)



print(*solution(V,True))
print(*solution(V,False))
