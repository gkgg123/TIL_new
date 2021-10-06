import sys
from math import log2
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def LCA(X,Y):
    min_value = float('inf')
    max_value = 0
    if depth[X] != depth[Y]:
        if depth[X]>depth[Y]:
            X,Y = Y,X
        for i in range(MAX_NODE-1,-1,-1):
            if (depth[Y]-depth[X] >= (1<<i)):
                min_value = min(min_value, min_dp[Y][i])
                max_value = max(max_value, max_dp[Y][i])
                Y = parents[Y][i]
    if X == Y:
        return [min_value,max_value]

    if (Y != X):
        for i in range(MAX_NODE-1,-1,-1):
            if parents[X][i] != parents[Y][i]:
                min_value = min(min_value,min_dp[X][i],  min_dp[Y][i])
                max_value = max(max_value,max_dp[X][i], max_dp[Y][i])
                X = parents[X][i]
                Y = parents[Y][i]
        min_value= min(min_value,min_dp[X][0],  min_dp[Y][0])
        max_value = max(max_value,max_dp[X][0], max_dp[Y][0])
    return [min_value,max_value]

N = int(input())


graph = [{} for _ in range(N+1)]
MAX_NODE = int(log2(N))+1
parents = [[0 for _ in range(MAX_NODE)] for _ in range(N+1)]
max_dp = [[0 for _ in range(MAX_NODE)] for _ in range(N+1)]
min_dp = [[0 for _ in range(MAX_NODE)] for _ in range(N+1)]
depth = [0 for _ in range(N+1)]
visited = [True for _ in range(N+1)]
for _ in range(N-1):
    x,y,pay = map(int,input().split())
    graph[x][y] = pay
    graph[y][x] = pay
Q = int(input())
queue = deque()
queue.append([1,0])
visited[1] = False
while queue:
    node,d = queue.popleft()

    for next_node in graph[node]:
        if not visited[next_node]:continue
        visited[next_node] = False
        parents[next_node][0] = node
        depth[next_node] = d + 1
        max_dp[next_node][0] = graph[node][next_node]
        min_dp[next_node][0] = graph[node][next_node]
        queue.append((next_node,d+1))

for y in range(1,MAX_NODE):
    for x in range(1,N+1):
        temp = parents[x][y-1]
        parents[x][y] = parents[temp][y-1]
        max_dp[x][y] = max(max_dp[temp][y-1],max_dp[x][y-1])
        min_dp[x][y] = min(min_dp[temp][y-1],min_dp[x][y-1])
for _ in range(Q):
    a,b = map(int,input().split())
    print(*LCA(a,b))