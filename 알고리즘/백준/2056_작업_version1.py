import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N = int(input())

time_idx = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
parent_cnt = [0 for _ in range(N+1)]
for idx in range(1,N+1):
    time,cnt,*arr = list(map(int,input().split()))
    time_idx[idx] = time
    if cnt:
        for prev_node in arr:
            graph[prev_node].append(idx)
        parent_cnt[idx] = cnt
queue = deque()
dp = [0 for _ in range(N+1)]
for idx in range(1,N+1):
    if not parent_cnt[idx]:
        queue.append(idx)
        dp[idx] = time_idx[idx]
answer = 0
while queue:
    node = queue.popleft()
    for next_node in graph[node]:
        parent_cnt[next_node] -= 1
        dp[next_node] = max(dp[node] + time_idx[next_node], dp[next_node])
        if not parent_cnt[next_node]:
            queue.append(next_node)

print(max(dp))