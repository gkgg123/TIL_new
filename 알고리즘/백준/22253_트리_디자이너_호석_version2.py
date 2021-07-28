import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()


N = int(input())
bright_list = list(map(int,input().split()))

mod = 10**9+7
graph = [[] for _ in range(N)]
for _ in range(N-1):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    graph[x].append(y)
    graph[y].append(x)


dp =[ [0 if bright_list[node] != val else 1 for val in range(10)] for node in range(N)]

stack = []
que = deque()
que.append([0,0])

while que:
    cur_node,parent = que.popleft()
    stack.append((cur_node,parent))
    for next_node in graph[cur_node]:
        if next_node != parent:
            que.append((next_node,cur_node))



while stack:
    cur_node,parent = stack.pop()
    if cur_node == 0:
        break
    for val in range(10):
        dp[parent][val] = (dp[parent][val] + dp[cur_node][val])%mod
    parent_val = bright_list[parent]
    for next_val in range(parent_val,10):
        dp[parent][parent_val] = (dp[parent][parent_val]+dp[cur_node][next_val])%mod
print(sum(dp[0])%mod)