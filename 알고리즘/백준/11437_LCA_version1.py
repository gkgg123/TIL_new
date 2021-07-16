import sys
sys.setrecursionlimit(100000)
def input():
    return sys.stdin.readline()

def dfs(node,d):
    visited[node] = False
    depth[node] = d
    for next_node in tree[node]:
        if not visited[next_node]:
            continue
        parents[next_node][0] = node
        dfs(next_node,d+1)



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
N = int(input())
MAX_NODE = 17
tree = [[] for _ in range(N+1)]
parents =  [[0 for _ in range(MAX_NODE)] for _ in range(N+1)]
depth = [0 for _ in range(N+1)]
for i in range(N-1):
    x,y = map(int,input().split())
    tree[y].append(x)
    tree[x].append(y)

M = int(input())
visited = [True for _ in range(N+1)]
dfs(1,0)


for y in range(1,MAX_NODE):
    for x in range(1,N+1):
        parents[x][y] = parents[parents[x][y-1]][y-1]

for _ in range(M):
    x,y = map(int,input().split())
    print(LCA(x,y))