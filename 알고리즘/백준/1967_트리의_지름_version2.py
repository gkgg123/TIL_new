import sys
sys.setrecursionlimit(10000)
def dfs(node):
    if not graph[node]:
        return 0
    ind = 0
    for next_node in graph[node]:
        distance_nodes[node][ind] += dfs(next_node) + graph[node][next_node]
        ind += 1
    return max(distance_nodes[node])
N = int(input())
graph = [{} for _ in range(N+1)]
parents = [0]*(N+1)
for _ in range(N-1):
    A,B,C = map(int,input().split())
    graph[A][B] = C
    parents[A] += 1

distance_nodes = [[0]*(parents[ind]+2) for ind in range(N+1)]

dfs(1)
result = 0
for ind in range(1,N+1):
    distance_nodes[ind].sort(reverse=True)
    result = max(result,distance_nodes[ind][0]+distance_nodes[ind][1])
print(result)