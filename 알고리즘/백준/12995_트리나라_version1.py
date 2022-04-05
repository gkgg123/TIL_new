import sys

def input():
    return sys.stdin.readline().rstrip()
def dfs(node,parent):
    
    for next_node in graph[node]:
        if next_node != parent:
            tree[node].append(next_node)
            dfs(next_node,node)

def calc(root,nth_idx,select):
    if select == 0:
        return 1
    if nth_idx == len(tree[root]):
        if select == 1:
            return 1
        return 0
    if dp[root][nth_idx][select] != -1:
        return dp[root][nth_idx][select]
    dp[root][nth_idx][select] = 0

    for pick in range(select):
        temp = calc(tree[root][nth_idx],0,pick) * calc(root,nth_idx+1,select-pick)
        dp[root][nth_idx][select] = (dp[root][nth_idx][select] + temp)%  1000000007
    return dp[root][nth_idx][select]
N,K = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

# 현재노드, x번째 자식
dp = [[[-1 for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]
tree = [[] for _ in range(N+1)]

dfs(1,1)
answer = 0
for i in range(1,N+1):
    answer += calc(i,0,K)
    answer = answer% 100000000007
print(answer)