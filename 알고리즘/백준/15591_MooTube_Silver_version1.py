# 15591 MooTube

N,Q = map(int,input().split())

graph = {i:[] for i in range(N+1)}

for _ in range(N-1):
    A,B,USADO = map(int,input().split())
    graph[A].append((B,USADO))
    graph[B].append((A,USADO))


for _ in range(Q):
    K,start = map(int,input().split())
    visited = [True]*(N+1)
    visited[start] = False
    stack = [(start,float('inf'))]
    result = 0
    while stack:
        node,usado = stack.pop()

        for next_node,next_usado in graph[node]:
            next_usado = min(usado,next_usado)
            if next_usado >= K and visited[next_node]:
                result += 1
                stack.append((next_node,next_usado))
                visited[next_node] = False
    print(result)
