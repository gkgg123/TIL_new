import sys

input = sys.stdin.readline

from collections import deque

N, M = map(int,input().split())

graph = [{} for _ in range(N+1)]
parents_cnt = [0]*(N+1)
result = []
visited = [True]*(N+1)
for _ in range(M):
    A,B = map(int,input().split())
    graph[A][B] = 1
    parents_cnt[B] += 1

que = deque()
for i in range(1,N+1):
    if not parents_cnt[i]:
        que.append(i)
for i in range(N):
    x = que.popleft()
    result.append(x)

    for next_node in graph[x]:
        parents_cnt[next_node] -= 1
        if parents_cnt[next_node] == 0:
            que.append(next_node)
print(*result)


