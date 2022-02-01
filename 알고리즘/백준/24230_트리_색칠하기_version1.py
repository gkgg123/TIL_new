import sys
sys.setrecursionlimit(200001)
def input():
    return sys.stdin.readline().rstrip()

def dfs(node,parent):
    global answer
    cur_colors[node] = cur_colors[parent]
    visited[node] = False
    if cur_colors[node] != end_colors[node]:
        cur_colors[node] = end_colors[node]
        answer += 1
    for child_node in tree[node]:
        if visited[child_node]:
            dfs(child_node,node)
N = int(input())


end_colors = [0] + list(map(int,input().split()))
cur_colors = [0 for _ in range(N+1)]
answer = 0


tree = [[] for _ in range(N+1)]


for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [True for _ in range(N+1)]
dfs(1,1)
print(answer)