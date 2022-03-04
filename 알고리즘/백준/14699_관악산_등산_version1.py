import sys
sys.setrecursionlimit(10000)
def input():
    return sys.stdin.readline().rstrip()
def dfs(node):
    if cnt[node] != -1:
        return cnt[node]
    cnt[node] = 0
    for next_node in graph[node]:
        cnt[node] = max(cnt[node],dfs(next_node))
    cnt[node] += 1
    return cnt[node]

N,M = map(int,input().split())

heights = [0] + list(map(int,input().split()))

cnt = [-1 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
for i in range(M):
    x,y = map(int,input().split())
    if heights[x] > heights[y]:
        x,y = y,x

    graph[x].append(y)

for i in range(1,N+1):
    if cnt[i] == -1:
        dfs(i)

for i in range(1,N+1):
    print(cnt[i])