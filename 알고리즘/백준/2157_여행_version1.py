import sys
sys.setrecursionlimit(10000)
def input():
    return sys.stdin.readline().rstrip()


def dfs(cur_node,cnt):
    if cnt <= M and cur_node == N:
        return 0
    if cnt == M:
        return -float('inf')
    if dp[cur_node][cnt] != -1:
        return dp[cur_node][cnt]
    dp[cur_node][cnt] = -float('inf')

    for next_node in graph[cur_node]:
        dp[cur_node][cnt] = max(dp[cur_node][cnt], graph[cur_node][next_node] +dfs(next_node,cnt+1))
    return dp[cur_node][cnt]

N,M,K = map(int,input().split())


graph = [{} for  _ in range(N+1)]

for _ in range(K):
    x,y,pay = map(int,input().split())
    if x>y:
        continue
    graph[x][y] = max(graph[x].get(y,0),pay)

dp = [[-1 for _ in range(M+1)] for _ in range(N+1)]

print(dfs(1,1))