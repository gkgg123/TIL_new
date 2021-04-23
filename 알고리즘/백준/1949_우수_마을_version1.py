import sys

sys.setrecursionlimit(100000)
def dfs(node):
    
    if visited[node]:
        return
    visited[node] = True
    child_nodes = []
    for next_node in graph[node]:
        if not visited[next_node]:
            child_nodes.append(next_node)

    if not len(child_nodes):
        dp[node][0] = town_person[node]
        return

    for child_node in child_nodes:
        dfs(child_node)
        dp[node][0] += dp[child_node][1]
        dp[node][1] +=  max(dp[child_node][0],dp[child_node][1])
    dp[node][0] += town_person[node]





N = int(input())
town_person = [0] +list(map(int,input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False]*(N+1)
dp = [[0]*2 for _ in range(N+1)]
# 0번 인덱스 : 참여를 했을때
# 1번 인덱스 : 참여를 안 했을때
dfs(1)

print(max(dp[1]))