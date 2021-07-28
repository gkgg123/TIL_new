import sys

def input():
    return sys.stdin.readline().rstrip()

sys.setrecursionlimit(100001)
def dfs(node,parent):
    child_list = []
    dp[node][blub_bright[node]] = 1
    for next_node in graph[node]:
        if next_node != parent:
            child_list.append(next_node)
    if child_list:
        for next_node in child_list:
            dfs(next_node,node)
            for val in range(10):
                dp[node][val] += dp[next_node][val]
                dp[node][val]%=mod
            for next_val in range(blub_bright[node],10):
                dp[node][blub_bright[node]] += dp[next_node][next_val]
                dp[node][blub_bright[node]]%=mod

N = int(input())

mod = 10**9+7

blub_bright = [0] + list(map(int,input().split()))

graph = [[] for _ in range(N+1)]


for _ in range(N-1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
dp = [[0 for _ in range(10)] for _ in range(N+1)] 
visited = [True for _ in range(N)]
dfs(1,1)

print(sum(dp[1])%mod)