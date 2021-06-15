import sys
sys.setrecursionlimit(20000)
def input():
    return sys.stdin.readline().rstrip()
def trace(cur_node,prev_check):
    visited[cur_node] = False
    flag = 0
    if not prev_check:
        if dp[cur_node][0] < dp[cur_node][1]:
            result.append(cur_node)
            flag = 1
    for next_node in graph[cur_node]:
        if visited[next_node]:
            trace(next_node,flag)

def dfs(node):
    visited[node] = False
    child_node = []
    for next_node in graph[node]:
        if visited[next_node]:
            child_node.append(next_node)
    if not len(child_node):
        dp[node][1] = arr[node]

        return
    else:
        dp[node][1] += arr[node]
        for child in child_node:
            dfs(child)
            dp[node][0] += max(dp[child][1],dp[child][0])
            dp[node][1] += dp[child][0]



N = int(input())
arr = [0] + list(map(int,input().split()))

# 1이 선택 
# 0이 선택 x
dp = [[0 for _ in range(2)] for _ in range(N+1)]

graph = [[] for _ in range(N+1)]
visited = [True for _ in range(N+1)]
for k in range(N-1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)


dfs(1)

print(max(dp[1]))


result = []
visited = [True for _ in range(N+1)]
trace(1,0)
result.sort()
print(*result)