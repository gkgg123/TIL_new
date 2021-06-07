import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)
def root_dfs(node,dis):
    if visited[node]:
        return
    visited[node] = True
    count = 0
    nexts = -1
    distance = 0
    for next_node in tree[node]:
        if not visited[next_node]:
            count += 1
            nexts = next_node
            distance += tree[node][next_node]
    if count == 1:
        return root_dfs(nexts,dis+distance)
    else:
        return [node,dis]

def leaf_dfs(node,dis):
    global leef_dis
    visited[node] = True
    count = 0
    for next_node in tree[node]:
        if not visited[next_node]:
            leaf_dfs(next_node,dis+tree[node][next_node])
            count += 1
    if not count:
        leef_dis = max(leef_dis,dis)


N,R = map(int,input().split())
tree = [{} for _ in range(N+1)]
for _ in range(N-1):
    x,y,b = map(int,input().split())
    tree[x][y] = b
    tree[y][x] = b


visited = [False for _ in range(N+1)]
root_dis = root_dfs(R,0)
leef_dis = 0
leaf_dfs(root_dis[0],0)
print(root_dis[1],leef_dis)