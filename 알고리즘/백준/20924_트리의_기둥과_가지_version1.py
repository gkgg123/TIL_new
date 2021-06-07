import sys
input = sys.stdin.readline
sys.setrecursionlimit(500000)
def root_dfs(node):
    if visited[node]:
        return
    visited[node] = True
    child_list = []
    for next_node in tree[node]:
        if not visited[next_node]:
            child_list.append(next_node)

    if len(child_list)==2:
        return [node,0]
    elif len(child_list) == 1:
        return_value = root_dfs(child_list[0])
        return_value[1] += tree[node][child_list[0]]
        return return_value
    else:
        return [node,0]

def leef_dfs(node):
    if visited[node]:
        return
    visited[node] = True
    child_list = []
    for next_node in tree[node]:
        if not visited[next_node]:
            child_list.append(next_node)
    
    if len(child_list)==0:
        return 0
    else:
        result = 0
        for child_node in child_list:
            result = max(result,leef_dfs(child_node)+tree[node][child_node])
        return result
N,R = map(int,input().split())
tree = [{} for _ in range(N+1)]
for _ in range(N-1):
    x,y,b = map(int,input().split())
    tree[x][y] = b
    tree[y][x] = b


visited = [False for _ in range(N+1)]

root_node_info = root_dfs(R)
visited[root_node_info[0]] = False
leef_dis = leef_dfs(root_node_info[0])
print(root_node_info[1],leef_dis)