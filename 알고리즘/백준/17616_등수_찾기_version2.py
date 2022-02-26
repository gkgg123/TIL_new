import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()


N,M,X = map(int,input().split())


child = [[] for _ in range(N+1)]
parent = [[] for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,input().split())
    child[x].append(y)
    parent[y].append(x)


visited = [False for _ in range(N+1)]
visited[X] = True
queue = deque()
queue.append(X)
U = 0
while queue:
    node = queue.popleft()
    U += 1

    for next_node in parent[node]:
        if not visited[next_node]:
            visited[next_node] = True
            queue.append(next_node)


visited = [False for _ in range(N+1)]
visited[X] = True
queue = deque()
queue.append(X)
cnt = 0
while queue:
    node = queue.popleft()
    cnt += 1

    for next_node in child[node]:
        if not visited[next_node]:
            visited[next_node] = True
            queue.append(next_node)

print(U,N-cnt+1)