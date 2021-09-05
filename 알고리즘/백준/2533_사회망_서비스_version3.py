import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()


N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

dp = [[0,1] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
stack = deque([1])
parents = [0 for _ in range(N+1)]
queue = deque()
indegree = [0 for _ in range(N+1)]

while stack:
    node = stack.pop()
    visited[node] = True
    for next_node in graph[node]:
        if visited[next_node]:
            continue
        parents[next_node] = node
        indegree[node] += 1
        if len(graph[next_node]) == 1:
            queue.append(next_node)
        else:
            stack.append(next_node)
while queue:
    node = queue.popleft()
    if node == 1:
        break
    next_node = parents[node]
    # 0은 선택 안했을때
    dp[next_node][0] += dp[node][1] 
    dp[next_node][1] += min(dp[node][0],dp[node][1])
    indegree[next_node] -= 1
    if indegree[next_node] == 0:
        queue.append(next_node)

print(min(dp[1][0],dp[1][1]))