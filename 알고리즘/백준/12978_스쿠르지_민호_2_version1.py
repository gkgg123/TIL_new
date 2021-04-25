import sys

sys.setrecursionlimit(100001)


def dfs(node):
    visited[node] = True
    child_node = []
    for next_node in graph[node]:
        if not visited[next_node]:
            child_node.append(next_node)
    if not len(child_node):
        dp[node][0] = 1
        return
    else:
        for child in child_node:
            dfs(child)

        for child in child_node:
            if dp[child][0]:
                dp[node][1] = 1
                break
        else:
            dp[node][0] = 1

N = int(input())
graph = [[] for _ in range(N+1)]


for _ in range(N-1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [False]*(N+1)
dp = [[0]*2 for _ in range(N+1)]
dfs(1)

answer = min(list(map(sum,list(zip(*dp)))))
print(answer)