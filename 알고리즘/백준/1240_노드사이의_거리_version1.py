import sys
from math import log2
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
def LCA(X,Y):
    if depth[X] != depth[Y]:
        if depth[X]>depth[Y]:
            X,Y = Y,X
        for i in range(MAX_NODE-1,-1,-1):
            if (depth[Y]-depth[X] >= (1<<i)):
                Y = parents[Y][i]
    if X == Y:
        return X
    if (Y != X):
        for i in range(MAX_NODE-1,-1,-1):
            if parents[X][i] != parents[Y][i]:
                X = parents[X][i]
                Y = parents[Y][i]
    return parents[X][0]

N,M = map(int,input().split())


graph = [{} for _ in range(N+1)]

for _ in range(N-1):
    x,y,pay = map(int,input().split())
    graph[x][y] = pay
    graph[y][x] = pay
MAX_NODE = int(log2(N))+1
distance = [0 for _ in range(N+1)]
parents = [[0 for _ in range(MAX_NODE)] for _ in range(N+1)]
depth = [0 for _ in range(N+1)]
visited = [True for _ in range(N+1)]
queue = deque()
visited[1] = False
queue.append([1,0])

while queue:
    node, d = queue.popleft()

    for next_node in graph[node]:
        if not visited[next_node]:continue
        visited[next_node] = False
        parents[next_node][0] = node
        depth[next_node] = d + 1
        distance[next_node] = distance[node] + graph[node][next_node]
        queue.append((next_node,d+1))

for y in range(1,MAX_NODE):
    for x in range(1,N+1):
        temp = parents[x][y-1]
        parents[x][y] = parents[temp][y-1]

for _ in range(M):
    x,y = map(int,input().split())
    lca_node = LCA(x,y)
    print(distance[x] + distance[y] - 2*distance[lca_node])