import sys
sys.setrecursionlimit(100001)
def input():
    return sys.stdin.readline().rstrip()
def dfs(node,graph):
    visited[node] = True
    ret = 0
    for next_node in graph[node]:
        if not visited[next_node]:
            ret += dfs(next_node,graph)
    return ret + 1
            

N,M,X = map(int,input().split())


child = [[] for _ in range(N+1)]
parent = [[] for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,input().split())
    child[x].append(y)
    parent[y].append(x)

visited = [False for _ in range(N+1)] 
u = dfs(X,parent)
visited = [False for _ in range(N+1)] 
v = N-dfs(X,child)+1

print(u,v)